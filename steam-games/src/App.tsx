import AppSearchAPIConnector from "@elastic/search-ui-app-search-connector";
import React from "react";
import ElasticsearchAPIConnector from "@elastic/search-ui-elasticsearch-connector"

import {
  ErrorBoundary,
  Facet,
  SearchProvider,
  SearchBox,
  Results,
  PagingInfo,
  ResultsPerPage,
  Paging,
  WithSearch
} from "@elastic/react-search-ui";
import {
  BooleanFacet,
  Layout,
  SingleLinksFacet,
  SingleSelectFacet
} from "@elastic/react-search-ui-views";
import "@elastic/react-search-ui-views/lib/styles/styles.css";
import { SearchDriverOptions } from "@elastic/search-ui";

const connector = new ElasticsearchAPIConnector({
  host: "http://localhost:9200",
  index: "steam_games"
});

// Helper function to format release_date
function formatDate(dateString: string): string {
  const options: Intl.DateTimeFormatOptions = {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
  };
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', options);
}

const generateYearRanges = () => {
  const yearRanges = [];
  for (let year = 1998; year <= 2023; year += 6) {
    const from = `${year}-01-01T00:00:00Z`;
    const to = `${year + 6}-12-31T23:59:59Z`;
    yearRanges.push({ from, to, name: `${year}-${year + 6}` });
  }
  return yearRanges;
};

const config: SearchDriverOptions = {
  alwaysSearchOnInitialLoad: true,
  apiConnector: connector,
  hasA11yNotifications: true,
  searchQuery: {
    result_fields: {
      title: { snippet: { fallback: true } },
      description: { snippet: { fallback: true } },
      price: { raw: {} },
      release_date: {raw: {}},
      score: { raw: {} },
      reviews: { raw: {} },
      genre: { raw: {} },
      developers: { raw: {} },
      franchise : { raw: {} },
      header_image: {raw: {} },
      url: {raw: {}}
    },
    search_fields: {
      title: {},
      description: {},
      developers: {},
      franchise: {},
    },
    disjunctiveFacets: [""],
facets: {
		"genre.keyword": { type: "value" },
		  price: {
			type: "range",
			ranges: [
			  { from: 0, to: 1000000000, name: "None" },
			  { from: 0, to: 1, name: "One euro or less" },
			  { from: 0, to: 5, name: "Under 5 euros" },
			  { from: 0, to: 25, name: "Under 25 euros" },
			  { from: 0, to: 50, name: "Under 50 euros" },
			]
		  },
		  score: {
			type: "range",
			ranges: [
			  { from: 0, to: 30, name: "0-30" },
			  { from: 30, to: 50, name: "30-50" },
			  { from: 50, to: 70, name: "50-70" },
			  { from: 70, to: 90, name: "70-90" },
			  { from: 90, to: 990, name: "90-100" }
			]
		  },
		  "reviews.keyword":  { type: "value" },
		  release_date: {type: "range", ranges: generateYearRanges(),}
		}
  }
};
export default function App() {
  return (
    <SearchProvider config={config}>
      <WithSearch
        mapContextToProps={({ wasSearched }) => ({
          wasSearched,
        })}
      >
        {({ wasSearched }) => {
          return (
            <div className="App">
              <ErrorBoundary>
                <Layout
                  header={<SearchBox debounceLength={0} />}
                  sideContent={
                    <div>
                      <Facet
                        field="genre.keyword"
                        label="Genre"
                        isFilterable={true}
                      />
                      <Facet
                        field="price"
                        label="Price"
                        view={SingleSelectFacet}
                      />
                      <Facet
                        field="score"
                        label="Score"
                        view={SingleLinksFacet}
                      />
                      <Facet
                        field="reviews.keyword"
                        label="Reviews"
                      />
                      <Facet
                        field="release_date"
                        label="Date"
                        view={SingleLinksFacet}
                      />
                    </div>
                  }
                  bodyContent={
                    <Results
                      titleField="title.raw"
                      urlField="url.raw"
                      thumbnailField="header_image.raw"
                      shouldTrackClickThrough={true}
                      resultView={(props) => (
                        <div className="result-item">
                          <a
                            href={props.result.url.raw}
                            target="_blank"
                            rel="noopener noreferrer"
                            style={{ fontSize: '20px', fontWeight: 'bold' }}
                          >
                            {props.result.title.raw}
                          </a>
                          <div>
                            <img
                              src={props.result.header_image.raw}
                              alt={props.result.title.raw}
                            />
                            <div>
                              <div>
                                <strong>Description:</strong>{' '}
                                {props.result.description.raw}
                              </div>
                              <div>
                                <strong>Price:</strong>{' '}
                                {props.result.price.raw !== '0.0' && props.result.price.raw !== undefined ? `${props.result.price.raw} €` : 'Free to play'}
                              </div>
                              <div>
                                <strong>Genre:</strong>{' '}
                                {Array.isArray(props.result.genre.raw)
                                  ? props.result.genre.raw.join(', ')
                                  : 'none'}
                              </div>
                              <div>
                                <strong>Developers:</strong>{' '}
                                {Array.isArray(props.result.developers.raw)
                                  ? props.result.developers.raw.join(', ')
                                  : 'none'}
                              </div>
                              <div>
                                <strong>Franchise:</strong>{' '}
                                {props.result.franchise.raw || 'none'}
                              </div>
                              <div>
                                <strong>Release Date:</strong>{' '}
                                {formatDate(props.result.release_date.raw)}
                              </div>
                              <div>
                                <strong>Score:</strong>{' '}
                                {props.result.score.raw || 'none'}
                              </div>
                              <div>
                                <strong>Reviews:</strong>{' '}
                                {props.result.reviews.raw || 'none'}
                              </div>
                            </div>
                          </div>
                        </div>
                      )}
                    />
                  }
                  bodyHeader={
                    <React.Fragment>
                      {wasSearched && <PagingInfo />}
                      {wasSearched && <ResultsPerPage />}
                    </React.Fragment>
                  }
                  bodyFooter={<Paging />}
                />
              </ErrorBoundary>
            </div>
          );
        }}
      </WithSearch>
    </SearchProvider>
  );
}

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

const config: SearchDriverOptions = {
  alwaysSearchOnInitialLoad: true,
  apiConnector: connector,
  hasA11yNotifications: true,
  searchQuery: {
    result_fields: {
      title: { snippet: { fallback: true } },
      description: { snippet: { fallback: true } },
      price: { raw: {} },
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
		  "reviews.keyword":  { type: "value" }
		}
  }
};
export default function App() {
  return (
    <SearchProvider config={config}>
      <WithSearch
        mapContextToProps={({ wasSearched }) => ({
          wasSearched
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
					  </div>
					}

                  bodyContent={
                    <Results
                      titleField="title"
                      urlField="url"
                      thumbnailField="header_image"
                      shouldTrackClickThrough={true}
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

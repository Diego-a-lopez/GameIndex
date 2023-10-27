// Wait for the document to be ready
$(document).ready(function () {
  // Define the Elasticsearch endpoint
  const elasticsearchEndpoint = 'http://localhost:9200/games/_search';

  // Get the search button and search input
  const searchButton = $('#searchButton');
  const searchResults = $('#searchResults');

  // When the search button is clicked
  searchButton.click(function () {
    // Get the selected search type and search input
    const searchType = $('#searchType').val();
    const searchInput = $('#searchInput').val();

    // Prepare the query based on the selected search type
    const query = {
      query: {
        match: {
          [searchType]: searchInput
        }
      }
    };

    // Send a POST request to Elasticsearch
    $.ajax({
      type: 'POST',
      url: elasticsearchEndpoint,
      data: JSON.stringify(query),
      contentType: 'application/json',
      success: function (data) {
        // Redirect to output.html and pass the data as a query parameter
        window.location.href = 'output.html?data=' + JSON.stringify(data);
      },
      error: function (error) {
        // Handle errors if any
        searchResults.text('Error: ' + JSON.stringify(error));
      }
    });
  });
});

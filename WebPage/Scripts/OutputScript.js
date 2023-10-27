
$(document).ready(function () {
  // Get the query parameter "data" from the URL
  const searchResults = $('#searchResults');
  const urlParams = new URLSearchParams(window.location.search);
  const searchData = urlParams.get('data');

  // Parse the data
  const data = JSON.parse(searchData);

  // Create a table to display the search results
  const table = $('<table>');
  const tbody = $('<tbody>');

  // Loop through the hits and create rows in the table
  data.hits.hits.forEach(function (hit) {
    const row = $('<tr>');
    row.append('<td>' + hit._source.Title + '</td>');
    row.append('<td>' + hit._source.Genre + '</td>');
    row.append('<td>' + hit._source.Developers + '</td>');
    row.append('<td>' + hit._source.Publishers + '</td>');
    row.append('<td>' + hit._source.Franchise + '</td>');
    tbody.append(row);
  });

  table.append(tbody);

  // Append the table to the searchResults div
  searchResults.append(table);
});

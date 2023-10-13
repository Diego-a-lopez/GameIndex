        const searchButton = document.getElementById('searchButton');
        const searchInput = document.getElementById('searchInput');
        const searchType = document.getElementById('searchType');
        const searchResults = document.getElementById('searchResults');

        searchButton.addEventListener('click', () => {
            const query = searchInput.value;
            const type = searchType.value;

            // Make an AJAX request to your backend API
            // Replace 'your_backend_url' with your actual backend server URL
            //fetch(`your_backend_url/search?type=${type}&query=${query}`)
            //fetch(`https://localhost:9200/games/search?type=${type}&query=${query}`)
            fetch(`https://localhost:9200/games/search?_search?size=50&pretty=true&q=*:*`)
                .then(response => response.json())
                .then(data => {
                    // Display search results
                    displayResults(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                    searchResults.innerHTML = error;//'An error occurred while searching.';
                });
        });

        function displayResults(results) {
            searchResults.innerHTML = ''; // Clear previous results
            if (results.length === 0) {
                searchResults.innerHTML = 'No results found.';
                return;
            }

            results.forEach(result => {
                const resultItem = document.createElement('div');
                resultItem.innerHTML = `<strong>${result._source.Title}</strong><br>${result._source.Description}`;
                searchResults.appendChild(resultItem);
            });
        }

RIWS APP Setup Guide

Prerequisites
Elasticsearch: Install Elasticsearch on your system.

For Windows users, follow the installation guide on the official Elasticsearch website: https://www.elastic.co/guide/en/elasticsearch/reference/current/windows.html

For Linux users, follow these guide : https://www.geeksforgeeks.org/how-to-install-and-configure-elasticsearch-on-ubuntu/

For Docker users, execute the following command:

docker run --rm -p 9200:9200 -p 9300:9300 -e "xpack.security.enabled=false" -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:"your version here" - ESJAVAOPTS=-Xmx2g

Elasticsearch Configuration:
Configure your Elasticsearch installation by updating the elasticsearch.yml file located at C:\"your install location"\elasticsearch-"your version here"\config. Add the following lines to the end of the file:

xpack.security.enabled: false
xpack.security.enrollment.enabled: false
http.cors.enabled: true
http.cors.allow-origin: "*"

Running Elasticsearch
If you are on Windows and have the necessary variables set up, run the command:

elasticsearch
For Docker users, ensure Elasticsearch is running by executing the Docker command mentioned above.

Run the Elasticsearch setup script:

python elastic.py

Setting up Development Environment
Ensure you have Java and Node.js installed on your system.

Java Installation:

For Windows, follow the installation guide: https://www.geeksforgeeks.org/installation-of-node-js-on-windows/
For Linux, follow the installation guide: https://www.geeksforgeeks.org/installation-of-node-js-on-linux/

Navigate to the steam-games subdirectory and set up the project:

npm install

Install project dependencies:

npm add @elastic/search-ui @elastic/react-search-ui-views @elastic/search-ui-app-search-connector @elastic/react-search-ui @elastic/search-ui-elasticsearch-connector

Finally, run the project:

npm start

The application will open in your default browser. Please be patient, as the initial bootup may take 2-3 minutes. If the browser does not open automatically, access the app at http://localhost:3000 and Elasticsearch at http://localhost:9200.
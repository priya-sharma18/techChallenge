# techChallenge

1Challenge_3tier.py

Architecture used - GCP
Programming language - Python

Step by Step process -

1. This python utility will read data from GCS storage which represents data layer, and process data through Cloud Functions which represents Processing layer.
2. Cloud function is used so that the moment a file arrives in a bucket CF will be triggered and starts the processing the input file.
3. This also represents one aspect of real time processing since this use case is for processing and visualising online sales.
4. Once the data is processed it will be moved to a BigQuery table and on top of BQ table a dashboard can be created.
5. for presentation layer- Bigquery, Tableau, and Google Data studio can be used as well.

Note - BQ table schemas has to created first in the BQ envrironment in first place.

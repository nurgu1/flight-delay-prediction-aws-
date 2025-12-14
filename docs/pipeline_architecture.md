## Pipeline Architecture
The pipeline ingests historical flight delay data into Amazon S3, where AWS Glue Crawlers
automatically infer schema information. A Glue ETL job performs basic transformations
and stores processed data in columnar format.

Real-time weather data is ingested from the OpenWeather API using AWS Lambda and stored
as JSON in Amazon S3. Glue Crawlers catalog the weather data, making it queryable via
Amazon Athena.

## Architecture Overview
- Data ingestion: Amazon S3, AWS Lambda
- Data processing: AWS Glue
- Data analysis: Amazon Athena

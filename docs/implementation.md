## Implementation Details
- Historical flight delay data was uploaded to Amazon S3.
- AWS Glue Crawlers were used to automatically infer schemas.
- An AWS Lambda function was implemented to fetch weather data from the OpenWeather API
  and store it in Amazon S3.
- Amazon Athena was used to query both datasets and compute KPIs.

## Analysis Approach
Due to differences in temporal granularity between historical and real-time data,
analysis focused on aggregated patterns rather than direct record-level joins.

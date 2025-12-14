## Data Ingestion

- Historical flight data was transferred to Amazon S3 using AWS DataSync.
- Weather data was collected via OpenWeather API using an AWS Lambda function.

## Data Processing

AWS Glue was used to:
- Clean missing values
- Normalize timestamps
- Convert JSON weather data into tabular format
- Join weather and flight datasets by airport and time

## Analytics

AWS Athena queries were executed to:
- Identify correlation between weather conditions and delays
- Detect high-risk airports
- Analyze seasonal patterns

## Results Interpretation

The analysis shows that strong wind and low visibility significantly
increase the probability of flight delays, especially during winter months.

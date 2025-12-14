## Architecture Overview

The system ingests historical flight delay data and real-time weather data,
stores raw data in Amazon S3, processes it using AWS Glue, and enables
SQL-based analytics with Amazon Athena.

## Services Used

- **Amazon S3**: Central data lake for raw and processed data
- **AWS DataSync**: Transfers historical flight data
- **AWS Lambda**: Fetches weather data from OpenWeather API
- **AWS Glue**: Cleans, joins, and normalizes datasets
- **AWS Athena**: Performs ad-hoc analytical queries

## Cost Estimation (Monthly)

| Service | Estimated Cost |
|------|--------------|
| S3 | ~$1 |
| Lambda | ~$0 |
| Glue | ~$4 |
| Athena | ~$0.3 |
| QuickSight (optional) | ~$21 |

**Total:** ~ $26/month

## Business Alignment
The serverless architecture minimizes infrastructure costs while enabling
scalable analytics aligned with airline operational needs.

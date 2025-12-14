# Proactive Flight Delay Management Using Historical and Real-Time Weather Data on AWS

## Project Overview
This project implements an AWS-based data pipeline to analyze Delta Air airline flight delays
using historical flight performance data and real-time weather data obtained from an
external API. The goal is to support proactive operational decision-making by identifying
delay-prone airports and seasonal risk patterns.

---

## Business Problem
Flight delays impose significant operational and financial costs on airlines.
While historical data reveals long-term delay patterns, it does not capture
current environmental risks. This project combines historical analytics with
real-time weather data to improve situational awareness and reduce disruption risk.

---

## Data Sources
- **Historical Flight Delay Data** (CSV, uploaded to Amazon S3)
- **OpenWeather API** (external REST API, ingested via AWS Lambda)

---

## AWS Services Used
- Amazon S3 (data storage)
- AWS Lambda (API ingestion)
- AWS Glue (schema discovery and ETL)
- Amazon Athena (SQL-based analytics)

---

## Key Performance Indicators (KPIs)
1. Average delay rate by airport  
2. Share of weather-related delay minutes  
3. Seasonal variation in weather-related delays  

---

## Results Summary
Analysis shows that approximately 22–25% of total delay minutes are weather-related,
with higher impact during winter months. Several airports exhibit consistently higher
delay rates, indicating structural operational risks.

---

## Limitations and Future Work
Due to the real-time nature of the Weather API and the historical aggregation of flight
data, direct time-aligned correlation analysis was not performed. Future work includes
collecting weather data over longer periods and integrating live flight status APIs.

---

## Repository Contents
- `/lambda`: AWS Lambda function for OpenWeather API ingestion
- `/athena`: SQL queries used for analysis
- `/architecture`: Pipeline architecture diagram
- `/presentation`: Final presentation slides

## Contributors
- Student: Nurgul Amirkhan
- Instructors: szabild@yahoo.com, balint.matyus@gmail.com

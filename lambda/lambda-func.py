import json
import urllib.request
import os
import boto3
from datetime import datetime

def lambda_handler(event, context):
    API_KEY = os.environ["OPENWEATHER_API_KEY"]
    CITY = "Atlanta"
    LOCATION_CODE = "ATL"
    BUCKET_NAME = "flight-delay-project-mglgx7"
    PREFIX = "raw/weather/"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric"
    )

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())

    weather_record = {
        "timestamp": datetime.utcnow().isoformat(),
        "location": LOCATION_CODE,
        "temperature": data["main"]["temp"],
        "wind_speed": data["wind"]["speed"],
        "weather_condition": data["weather"][0]["main"]
    }

    s3 = boto3.client("s3")
    file_name = f"weather_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=PREFIX + file_name,
        Body=json.dumps(weather_record),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": weather_record
    }

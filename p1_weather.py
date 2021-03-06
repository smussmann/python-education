import datetime

from typing import Any, Dict, List, Tuple

# Copied from https://api.openweathermap.org/data/2.5/onecall?lat=40.7127&lon=-74.0059&exclude=minutely,daily,alerts&units=imperial&appid=<appkey>
# API Docs at https://openweathermap.org/api/one-call-api
data = {
    "lat": 40.7127,
    "lon": -74.0059,
    "timezone": "America/New_York",
    "timezone_offset": -14400,
    "current": {
        "dt": 1648746684,
        "sunrise": 1648723264,
        "sunset": 1648768738,
        "temp": 60.55,
        "feels_like": 59.74,
        "pressure": 1005,
        "humidity": 73,
        "dew_point": 51.85,
        "uvi": 1.8,
        "clouds": 100,
        "visibility": 10000,
        "wind_speed": 21.85,
        "wind_deg": 200,
        "wind_gust": 35.68,
        "weather": [
            {
                "id": 804,
                "main": "Clouds",
                "description": "overcast clouds",
                "icon": "04d",
            }
        ],
    },
    "hourly": [
        {
            "dt": 1648746000,
            "temp": 60.55,
            "feels_like": 59.74,
            "pressure": 1005,
            "humidity": 73,
            "dew_point": 51.85,
            "uvi": 1.8,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 15.95,
            "wind_deg": 190,
            "wind_gust": 36.62,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648749600,
            "temp": 60.26,
            "feels_like": 59.5,
            "pressure": 1005,
            "humidity": 75,
            "dew_point": 52.32,
            "uvi": 1.65,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 16.8,
            "wind_deg": 177,
            "wind_gust": 35.54,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648753200,
            "temp": 59.94,
            "feels_like": 59.2,
            "pressure": 1005,
            "humidity": 76,
            "dew_point": 52.36,
            "uvi": 0.33,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 17.02,
            "wind_deg": 173,
            "wind_gust": 33.35,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.34,
        },
        {
            "dt": 1648756800,
            "temp": 60.01,
            "feels_like": 59.38,
            "pressure": 1004,
            "humidity": 78,
            "dew_point": 53.13,
            "uvi": 0.21,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 17.02,
            "wind_deg": 183,
            "wind_gust": 38.01,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.36,
        },
        {
            "dt": 1648760400,
            "temp": 59.83,
            "feels_like": 59.45,
            "pressure": 1003,
            "humidity": 84,
            "dew_point": 54.99,
            "uvi": 0.1,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 19.64,
            "wind_deg": 183,
            "wind_gust": 40.53,
            "weather": [
                {"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"}
            ],
            "pop": 0.92,
            "rain": {"1h": 0.61},
        },
        {
            "dt": 1648764000,
            "temp": 56.91,
            "feels_like": 56.71,
            "pressure": 1001,
            "humidity": 94,
            "dew_point": 54.93,
            "uvi": 0.07,
            "clouds": 100,
            "visibility": 5707,
            "wind_speed": 19.15,
            "wind_deg": 173,
            "wind_gust": 37.76,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d",
                }
            ],
            "pop": 0.96,
            "rain": {"1h": 1.37},
        },
        {
            "dt": 1648767600,
            "temp": 54.88,
            "feels_like": 54.48,
            "pressure": 1001,
            "humidity": 94,
            "dew_point": 53.11,
            "uvi": 0,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 20.38,
            "wind_deg": 174,
            "wind_gust": 47.07,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d",
                }
            ],
            "pop": 1,
            "rain": {"1h": 1.02},
        },
        {
            "dt": 1648771200,
            "temp": 56.89,
            "feels_like": 56.75,
            "pressure": 1001,
            "humidity": 95,
            "dew_point": 55.67,
            "uvi": 0,
            "clouds": 100,
            "visibility": 3934,
            "wind_speed": 19.1,
            "wind_deg": 191,
            "wind_gust": 41.54,
            "weather": [
                {"id": 500, "main": "Rain", "description": "light rain", "icon": "10n"}
            ],
            "pop": 1,
            "rain": {"1h": 0.99},
        },
        {
            "dt": 1648774800,
            "temp": 57.92,
            "feels_like": 57.83,
            "pressure": 1000,
            "humidity": 94,
            "dew_point": 56.01,
            "uvi": 0,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 17.72,
            "wind_deg": 195,
            "wind_gust": 38.7,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10n",
                }
            ],
            "pop": 0.96,
            "rain": {"1h": 1.17},
        },
        {
            "dt": 1648778400,
            "temp": 57.43,
            "feels_like": 57.4,
            "pressure": 1000,
            "humidity": 96,
            "dew_point": 56.08,
            "uvi": 0,
            "clouds": 100,
            "visibility": 8481,
            "wind_speed": 17,
            "wind_deg": 199,
            "wind_gust": 38.25,
            "weather": [
                {"id": 500, "main": "Rain", "description": "light rain", "icon": "10n"}
            ],
            "pop": 1,
            "rain": {"1h": 0.82},
        },
        {
            "dt": 1648782000,
            "temp": 57.85,
            "feels_like": 57.85,
            "pressure": 1000,
            "humidity": 96,
            "dew_point": 56.61,
            "uvi": 0,
            "clouds": 100,
            "visibility": 2399,
            "wind_speed": 13.85,
            "wind_deg": 199,
            "wind_gust": 32.95,
            "weather": [
                {"id": 500, "main": "Rain", "description": "light rain", "icon": "10n"}
            ],
            "pop": 1,
            "rain": {"1h": 0.77},
        },
        {
            "dt": 1648785600,
            "temp": 57.99,
            "feels_like": 58.05,
            "pressure": 999,
            "humidity": 97,
            "dew_point": 56.89,
            "uvi": 0,
            "clouds": 100,
            "visibility": 5039,
            "wind_speed": 10.4,
            "wind_deg": 217,
            "wind_gust": 24.25,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10n",
                }
            ],
            "pop": 1,
            "rain": {"1h": 2.36},
        },
        {
            "dt": 1648789200,
            "temp": 56.95,
            "feels_like": 56.95,
            "pressure": 999,
            "humidity": 98,
            "dew_point": 56.3,
            "uvi": 0,
            "clouds": 100,
            "visibility": 1147,
            "wind_speed": 9.04,
            "wind_deg": 215,
            "wind_gust": 19.89,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10n",
                }
            ],
            "pop": 1,
            "rain": {"1h": 3.54},
        },
        {
            "dt": 1648792800,
            "temp": 57.52,
            "feels_like": 57.54,
            "pressure": 999,
            "humidity": 97,
            "dew_point": 56.44,
            "uvi": 0,
            "clouds": 100,
            "visibility": 2080,
            "wind_speed": 9.82,
            "wind_deg": 239,
            "wind_gust": 21.25,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10n",
                }
            ],
            "pop": 1,
            "rain": {"1h": 3.49},
        },
        {
            "dt": 1648796400,
            "temp": 57.07,
            "feels_like": 56.71,
            "pressure": 1000,
            "humidity": 90,
            "dew_point": 54.16,
            "uvi": 0,
            "clouds": 99,
            "visibility": 10000,
            "wind_speed": 10.54,
            "wind_deg": 259,
            "wind_gust": 20.76,
            "weather": [
                {"id": 500, "main": "Rain", "description": "light rain", "icon": "10n"}
            ],
            "pop": 0.69,
            "rain": {"1h": 0.68},
        },
        {
            "dt": 1648800000,
            "temp": 55.58,
            "feels_like": 54.55,
            "pressure": 1000,
            "humidity": 79,
            "dew_point": 48.96,
            "uvi": 0,
            "clouds": 91,
            "visibility": 10000,
            "wind_speed": 9.08,
            "wind_deg": 259,
            "wind_gust": 18.28,
            "weather": [
                {"id": 500, "main": "Rain", "description": "light rain", "icon": "10n"}
            ],
            "pop": 0.76,
            "rain": {"1h": 0.33},
        },
        {
            "dt": 1648803600,
            "temp": 54.54,
            "feels_like": 53.35,
            "pressure": 1001,
            "humidity": 78,
            "dew_point": 47.59,
            "uvi": 0,
            "clouds": 93,
            "visibility": 10000,
            "wind_speed": 11.01,
            "wind_deg": 268,
            "wind_gust": 20.78,
            "weather": [
                {"id": 500, "main": "Rain", "description": "light rain", "icon": "10n"}
            ],
            "pop": 0.69,
            "rain": {"1h": 0.12},
        },
        {
            "dt": 1648807200,
            "temp": 53.33,
            "feels_like": 51.84,
            "pressure": 1001,
            "humidity": 74,
            "dew_point": 45.05,
            "uvi": 0,
            "clouds": 95,
            "visibility": 10000,
            "wind_speed": 11.77,
            "wind_deg": 270,
            "wind_gust": 19.77,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0.69,
        },
        {
            "dt": 1648810800,
            "temp": 51.35,
            "feels_like": 49.66,
            "pressure": 1002,
            "humidity": 74,
            "dew_point": 43.23,
            "uvi": 0,
            "clouds": 96,
            "visibility": 10000,
            "wind_speed": 12.48,
            "wind_deg": 265,
            "wind_gust": 21.99,
            "weather": [
                {"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"}
            ],
            "pop": 0.64,
            "rain": {"1h": 0.13},
        },
        {
            "dt": 1648814400,
            "temp": 50.56,
            "feels_like": 48.51,
            "pressure": 1003,
            "humidity": 68,
            "dew_point": 40.55,
            "uvi": 0.32,
            "clouds": 97,
            "visibility": 10000,
            "wind_speed": 13.31,
            "wind_deg": 272,
            "wind_gust": 25.72,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.6,
        },
        {
            "dt": 1648818000,
            "temp": 49.46,
            "feels_like": 44.73,
            "pressure": 1003,
            "humidity": 66,
            "dew_point": 38.73,
            "uvi": 0.9,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 12.06,
            "wind_deg": 272,
            "wind_gust": 22.68,
            "weather": [
                {"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"}
            ],
            "pop": 0.72,
            "rain": {"1h": 0.24},
        },
        {
            "dt": 1648821600,
            "temp": 50.74,
            "feels_like": 48.29,
            "pressure": 1003,
            "humidity": 59,
            "dew_point": 36.68,
            "uvi": 1.83,
            "clouds": 59,
            "visibility": 10000,
            "wind_speed": 16.42,
            "wind_deg": 256,
            "wind_gust": 23.94,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.64,
        },
        {
            "dt": 1648825200,
            "temp": 52.29,
            "feels_like": 49.71,
            "pressure": 1003,
            "humidity": 53,
            "dew_point": 35.44,
            "uvi": 2.84,
            "clouds": 66,
            "visibility": 10000,
            "wind_speed": 15.35,
            "wind_deg": 261,
            "wind_gust": 23.15,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.37,
        },
        {
            "dt": 1648828800,
            "temp": 54.32,
            "feels_like": 51.71,
            "pressure": 1002,
            "humidity": 48,
            "dew_point": 34.81,
            "uvi": 3.12,
            "clouds": 57,
            "visibility": 10000,
            "wind_speed": 17.63,
            "wind_deg": 257,
            "wind_gust": 25.59,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.28,
        },
        {
            "dt": 1648832400,
            "temp": 52.77,
            "feels_like": 50.05,
            "pressure": 1002,
            "humidity": 49,
            "dew_point": 34.05,
            "uvi": 3.36,
            "clouds": 65,
            "visibility": 10000,
            "wind_speed": 18.54,
            "wind_deg": 259,
            "wind_gust": 26.26,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.21,
        },
        {
            "dt": 1648836000,
            "temp": 53.64,
            "feels_like": 50.81,
            "pressure": 1002,
            "humidity": 45,
            "dew_point": 32.74,
            "uvi": 3.08,
            "clouds": 71,
            "visibility": 10000,
            "wind_speed": 18.45,
            "wind_deg": 261,
            "wind_gust": 25.9,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.11,
        },
        {
            "dt": 1648839600,
            "temp": 53.82,
            "feels_like": 50.92,
            "pressure": 1002,
            "humidity": 43,
            "dew_point": 31.78,
            "uvi": 2.93,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 17.92,
            "wind_deg": 265,
            "wind_gust": 27.02,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.17,
        },
        {
            "dt": 1648843200,
            "temp": 53.71,
            "feels_like": 50.79,
            "pressure": 1002,
            "humidity": 43,
            "dew_point": 31.39,
            "uvi": 1.86,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 18.43,
            "wind_deg": 267,
            "wind_gust": 27.72,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.21,
        },
        {
            "dt": 1648846800,
            "temp": 53.11,
            "feels_like": 50.14,
            "pressure": 1003,
            "humidity": 43,
            "dew_point": 31.15,
            "uvi": 0.9,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 19.57,
            "wind_deg": 279,
            "wind_gust": 30.47,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.17,
        },
        {
            "dt": 1648850400,
            "temp": 52.23,
            "feels_like": 49.17,
            "pressure": 1005,
            "humidity": 43,
            "dew_point": 30.27,
            "uvi": 0.31,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 18.54,
            "wind_deg": 282,
            "wind_gust": 31.63,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.17,
        },
        {
            "dt": 1648854000,
            "temp": 49.82,
            "feels_like": 43.79,
            "pressure": 1006,
            "humidity": 48,
            "dew_point": 30.74,
            "uvi": 0,
            "clouds": 95,
            "visibility": 10000,
            "wind_speed": 17.85,
            "wind_deg": 291,
            "wind_gust": 31.29,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0.17,
        },
        {
            "dt": 1648857600,
            "temp": 48.29,
            "feels_like": 41.99,
            "pressure": 1008,
            "humidity": 47,
            "dew_point": 28.83,
            "uvi": 0,
            "clouds": 81,
            "visibility": 10000,
            "wind_speed": 16.98,
            "wind_deg": 293,
            "wind_gust": 30.24,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0.03,
        },
        {
            "dt": 1648861200,
            "temp": 46.56,
            "feels_like": 39.7,
            "pressure": 1009,
            "humidity": 48,
            "dew_point": 27.95,
            "uvi": 0,
            "clouds": 11,
            "visibility": 10000,
            "wind_speed": 17.18,
            "wind_deg": 295,
            "wind_gust": 31.43,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648864800,
            "temp": 45.01,
            "feels_like": 37.69,
            "pressure": 1011,
            "humidity": 49,
            "dew_point": 26.78,
            "uvi": 0,
            "clouds": 11,
            "visibility": 10000,
            "wind_speed": 17.25,
            "wind_deg": 295,
            "wind_gust": 29.93,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648868400,
            "temp": 43.32,
            "feels_like": 35.65,
            "pressure": 1012,
            "humidity": 50,
            "dew_point": 25.93,
            "uvi": 0,
            "clouds": 9,
            "visibility": 10000,
            "wind_speed": 16.64,
            "wind_deg": 300,
            "wind_gust": 27.81,
            "weather": [
                {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}
            ],
            "pop": 0,
        },
        {
            "dt": 1648872000,
            "temp": 41.58,
            "feels_like": 33.51,
            "pressure": 1013,
            "humidity": 55,
            "dew_point": 26.49,
            "uvi": 0,
            "clouds": 13,
            "visibility": 10000,
            "wind_speed": 16.2,
            "wind_deg": 302,
            "wind_gust": 26.11,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648875600,
            "temp": 40.19,
            "feels_like": 31.84,
            "pressure": 1014,
            "humidity": 61,
            "dew_point": 27.82,
            "uvi": 0,
            "clouds": 19,
            "visibility": 10000,
            "wind_speed": 15.82,
            "wind_deg": 304,
            "wind_gust": 29.48,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648879200,
            "temp": 39.38,
            "feels_like": 30.97,
            "pressure": 1015,
            "humidity": 56,
            "dew_point": 24.98,
            "uvi": 0,
            "clouds": 17,
            "visibility": 10000,
            "wind_speed": 15.21,
            "wind_deg": 306,
            "wind_gust": 29.24,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648882800,
            "temp": 38.26,
            "feels_like": 29.71,
            "pressure": 1016,
            "humidity": 56,
            "dew_point": 24.01,
            "uvi": 0,
            "clouds": 13,
            "visibility": 10000,
            "wind_speed": 14.67,
            "wind_deg": 307,
            "wind_gust": 28.27,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648886400,
            "temp": 37.38,
            "feels_like": 28.6,
            "pressure": 1016,
            "humidity": 56,
            "dew_point": 23.22,
            "uvi": 0,
            "clouds": 10,
            "visibility": 10000,
            "wind_speed": 14.65,
            "wind_deg": 304,
            "wind_gust": 26.55,
            "weather": [
                {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}
            ],
            "pop": 0,
        },
        {
            "dt": 1648890000,
            "temp": 36.55,
            "feels_like": 27.59,
            "pressure": 1017,
            "humidity": 58,
            "dew_point": 23.2,
            "uvi": 0,
            "clouds": 8,
            "visibility": 10000,
            "wind_speed": 14.52,
            "wind_deg": 304,
            "wind_gust": 25.88,
            "weather": [
                {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}
            ],
            "pop": 0,
        },
        {
            "dt": 1648893600,
            "temp": 36.23,
            "feels_like": 27.48,
            "pressure": 1018,
            "humidity": 59,
            "dew_point": 23.13,
            "uvi": 0,
            "clouds": 8,
            "visibility": 10000,
            "wind_speed": 13.65,
            "wind_deg": 302,
            "wind_gust": 24.52,
            "weather": [
                {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}
            ],
            "pop": 0,
        },
        {
            "dt": 1648897200,
            "temp": 36.27,
            "feels_like": 27.66,
            "pressure": 1018,
            "humidity": 57,
            "dew_point": 22.46,
            "uvi": 0,
            "clouds": 8,
            "visibility": 10000,
            "wind_speed": 13.24,
            "wind_deg": 299,
            "wind_gust": 24.29,
            "weather": [
                {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}
            ],
            "pop": 0,
        },
        {
            "dt": 1648900800,
            "temp": 37.13,
            "feels_like": 28.65,
            "pressure": 1019,
            "humidity": 54,
            "dew_point": 21.69,
            "uvi": 0.4,
            "clouds": 8,
            "visibility": 10000,
            "wind_speed": 13.58,
            "wind_deg": 303,
            "wind_gust": 23.49,
            "weather": [
                {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}
            ],
            "pop": 0,
        },
        {
            "dt": 1648904400,
            "temp": 38.95,
            "feels_like": 31.05,
            "pressure": 1019,
            "humidity": 49,
            "dew_point": 21.16,
            "uvi": 1.2,
            "clouds": 16,
            "visibility": 10000,
            "wind_speed": 13.29,
            "wind_deg": 312,
            "wind_gust": 19.93,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648908000,
            "temp": 41.31,
            "feels_like": 34.68,
            "pressure": 1019,
            "humidity": 44,
            "dew_point": 20.75,
            "uvi": 2.41,
            "clouds": 26,
            "visibility": 10000,
            "wind_speed": 11.48,
            "wind_deg": 312,
            "wind_gust": 15.79,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648911600,
            "temp": 44.31,
            "feels_like": 39.18,
            "pressure": 1019,
            "humidity": 38,
            "dew_point": 19.96,
            "uvi": 3.75,
            "clouds": 21,
            "visibility": 10000,
            "wind_speed": 9.53,
            "wind_deg": 308,
            "wind_gust": 13.69,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1648915200,
            "temp": 47.44,
            "feels_like": 43.7,
            "pressure": 1018,
            "humidity": 33,
            "dew_point": 19.35,
            "uvi": 4.86,
            "clouds": 18,
            "visibility": 10000,
            "wind_speed": 7.87,
            "wind_deg": 300,
            "wind_gust": 11.92,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d",
                }
            ],
            "pop": 0,
        },
    ],
}


def low(data: Dict[str, Any]) -> Tuple[float, datetime.datetime]:
    """Return the lowest predicted temperature in `data`, and the time it occurs."""
    return 0, datetime.datetime.now()


def high(data: Dict[str, Any]) -> Tuple[float, datetime.datetime]:
    """Return the highest predicted temperature in `data`, and the time it occurs."""
    return 0, datetime.datetime.now()

def daily_high(data: Dict[str, Any]) -> List[Tuple[float, datetime.datetime]]:
    """For each day in `data`, return its high and the time it occurs."""
    return [(0, datetime.datetime.now())]

def daily_low(data: Dict[str, Any]) -> List[Tuple[float, datetime.datetime]]:
    """For each day in `data`, return its low and the time it occurs."""
    return [(0, datetime.datetime.now())]

if __name__ == '__main__':
    high, at = high(data)
    print(f'4-day high of {high} at {at}')

    low, at = low(data)
    print(f'4-day low of {low} at {at}')

    daily_highs = daily_high(data)
    for high, at in daily_highs:
        print(f'daily high of {high} at {at}')

    daily_lows = daily_low(data)
    for low, at in daily_lows:
        print(f'daily low of {low} at {at}')
from _decimal import Decimal
from fastapi import FastAPI

import sentry_sdk


sentry_sdk.init(
    dsn="https://1db3364482b347fea95166dc44bd695b@o4505250926559232.ingest.sentry.io/4505387271716864",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

app = FastAPI(title='C to F converter')


@app.get('/{celsius}')
def celsius_to_fahrenheit(celsius: int | float | Decimal):
    celsius = Decimal(celsius).quantize(Decimal('0.1'))
    fahrenheit: Decimal = (celsius * 9 / 5) + 32
    fahrenheit = Decimal(fahrenheit).quantize(Decimal('0.1'))
    return {
        'message': 'ok',
        'result': fahrenheit,
    }

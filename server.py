import currencies
from flask import Flask, request
import json
import config


app = Flask(__name__)


@app.route("/convert_usd_rub")
def return_convert_result():
    amount_value = request.args.get('amount', type=str)
    if amount_value is None:
        return json.dumps(
            {'input_error': 'Bad data, pls check your input'}
        )
    else:
        amount = currencies.filter_strange_data(amount_value)
        if amount is None:
            return json.dumps(
                {
                    'input_error': 'Wrong amount, pls check your input'
                }
            )
        else:
            daily_value = currencies.get_daily_currencies(config.CURRENCY_URL)
            convert_result = currencies.convert_currency(amount, daily_value)
            return json.dumps(
                {
                    'USD': daily_value,
                    'convert_result': convert_result
                }
            )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

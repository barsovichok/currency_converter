import requests
import config


def get_convert_amount():
    user_input = input('Введите количество $ для конвертации:\n')
    return user_input


def filter_strange_data(user_input):
    user_input = user_input.replace(',', '.')
    user_input = user_input.replace(' ', '')
    try:
        amount = float(user_input)
    except ValueError:
        return None
    else:
        return amount


def get_daily_currencies(currency_url):
    daily_currencies = requests.get(currency_url).json()
    daily_value = daily_currencies['Valute'][config.CHARCODE][config.VALUE]
    return daily_value


def convert_currency(amount, daily_value):
    convert_result = amount*daily_value
    return convert_result


if __name__ == '__main__':
    user_input = get_convert_amount()
    amount = filter_strange_data(user_input)
    daily_value = get_daily_currencies(currency_url=config.CURRENCY_URL)
    convert_result = convert_currency(amount, daily_value)

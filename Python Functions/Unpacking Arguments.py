def currency_value_comparison(value, value_increase, value_depreciation):
    answer = value + (value_increase * 3.25) - value_depreciation
    print(answer)

usd_to_yen = [123.36, 0.008071, 122.36]

currency_value_comparison(*usd_to_yen)


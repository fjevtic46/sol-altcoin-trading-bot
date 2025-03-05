def should_sell_token(token_data,
                      max_h1_buy_ratio=0.8,
                      max_h6_buy_ratio=0.9,
                      min_m5_price_drop_percent=3,
                      max_liquidity_usd=50000,
                      max_volume_usd=5000,
                      min_price_change_percent=-10):
    """
    Determines if a token should be sold based on various criteria.

    Args:
        token_data (list): A list of dictionaries containing token data from Dex Screener's API.
        max_h1_buy_ratio (float): The maximum ratio of buys to sells in the last hour.
        max_h6_buy_ratio (float): The maximum ratio of buys to sells in the last 6 hours.
        min_m5_price_drop_percent (float): The minimum price drop percentage in the last 5 minutes to trigger a sell.
        max_liquidity_usd (float): The maximum liquidity in USD below which a sell is triggered.
        max_volume_usd (float): The maximum 24-hour volume in USD below which a sell is triggered.
        min_price_change_percent (float): The minimum price change percentage in the last 24 hours to trigger a sell.

    Returns:
        bool: True if the token should be sold, False otherwise.
    """

    if not token_data:
        return False

    token = token_data[0]  # Assuming only one token's data is provided

    # Check buy/sell ratios
    if token["txns"]["h1"]["sells"] == 0 or token["txns"]["h6"]["sells"] == 0:
            return False
    h1_buy_ratio = token["txns"]["h1"]["buys"] / token["txns"]["h1"]["sells"]
    h6_buy_ratio = token["txns"]["h6"]["buys"] / token["txns"]["h6"]["sells"]
    if h1_buy_ratio > max_h1_buy_ratio or h6_buy_ratio > max_h6_buy_ratio:
        return True

    # Check recent price drop
    m5_price_drop_percent = token["priceChange"].get("m5",0)
    if m5_price_drop_percent <= -min_m5_price_drop_percent:
        return True

    # Check liquidity and volume
    liquidity_usd = token["liquidity"]["usd"]
    volume_usd = token["volume"]["h24"]
    if liquidity_usd <= max_liquidity_usd or volume_usd <= max_volume_usd:
        return True

    # Check price change
    price_change_percent = token["priceChange"]["h24"]
    if price_change_percent <= min_price_change_percent:
        return True

    # No sell conditions met
    return False
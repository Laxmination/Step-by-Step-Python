#WAF to convert USD to NC.
"""
1 usd = 140 nc
2 usd = 280 nc 
..........
..........
"""
def converter(usd_value):
    nc_value =usd_value *140
    print(usd_value, "USD =", nc_value, "NC")

converter(2000)


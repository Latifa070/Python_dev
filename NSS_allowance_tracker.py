def net_allowance(gross, months):
    deduction = 15
    net_per_month = gross - deduction
    total = net_per_month * months
    return total


result = net_allowance(715.57,6)
savings = 200 * 6

print (f"The net allowance for 6 months is GHC {result}")
print (f"The savings for the six months is GHC {savings}")
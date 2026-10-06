
transaction_amounts =[]

for amount in range(5):
    transaction_amount = float(input("Enter the transaction amount: "))
    transaction_amounts.append(transaction_amount)

total_sales = sum (transaction_amounts)
highest_transaction = max(transaction_amounts)
commission = total_sales * 0.01

print(f"The total sales is : GHC {total_sales}")
print(f"The highest_transaction is : GHC {highest_transaction}")
print(f"Commission earned is : GHC {commission}")



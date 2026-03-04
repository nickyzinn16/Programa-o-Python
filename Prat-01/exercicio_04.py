# Crie um programa que permite a realização da venda de um item, permitindo o máximo de desconto possível desde que o lucro da venda não seja inferior a 80%. Incluir iva

totalCost = 480
salePrice = 520
expectedProfit = salePrice - totalCost
discountPercentage = 1
discount = (expectedProfit * discountPercentage) / 100
finalProfit = 0

while ( (expectedProfit - discount) >= (expectedProfit * 80) / 100):
    discountPercentage += 1
    discount = (expectedProfit * discountPercentage) / 100
    finalProfit = expectedProfit - discount


print(f"Total Cost: {totalCost}\nSale Price: {salePrice}\nExpected Profit: {expectedProfit}\nDiscount Percentage: {discountPercentage}\nDiscount: {discount}\nFinal Profit: {finalProfit}")
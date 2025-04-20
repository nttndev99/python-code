class Price:
    def final_price(self, vat, discount = 0):
        return (self.net_price * (100 + vat) / 100) - discount

p1 = Price() # instance (thể hiện đối tượng cụ thể)
p1.net_price = 100
print(Price.final_price(p1, 20 ,10)) # 110 (100 * 1.2 - 10)
print(p1.final_price(20, 10)) # equivalent
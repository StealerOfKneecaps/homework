# Lesson 5
#shouldn't be too bad. I think count would be cool
cookieSellBuy = input("Yo do the bcbcbc thing ").lower().strip()
bigCookie = cookieSellBuy.count("b")
regCookie = cookieSellBuy.count("c")
bigCookieCost = bigCookie*1.25
regCookieCost = regCookie*0.75
print(f"you sold {bigCookie+regCookie} cookies. You made a profit of ${bigCookieCost+regCookieCost}. You made a total of ${bigCookie*2+regCookie*1.25}.")
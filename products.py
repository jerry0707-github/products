products =[]

while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入價格: ')
#   p = []
#   p.append(name)
#   p.append(price)
    p = [name, price] #上面2維清單簡寫法
#   products.append(p)
    products.append([name, price]) #上面2維清單簡寫法
print(products)
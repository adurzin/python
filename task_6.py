products = []

for i in range(int(input("Сколько товаров в каталоге? "))):
    product_dict = {
        "название": input(f"Название товара №{i + 1}: "),
        "цена": int(input("Цена: ")),
        "количество": int(input("Количество товара: ")),
        "ед": input("единица измерения товара: ")
        }
    product = (i + 1, product_dict)
    products.append(product)

products_dict = {"название": [], "цена": [], "количество": [], "ед": []}

for i in products:
    product_dict = i[1]
    products_dict["название"].append(product_dict.get("название"))
    products_dict["цена"].append(product_dict.get("цена"))
    products_dict["количество"].append(product_dict.get("количество"))
    products_dict["ед"].append(product_dict.get("ед"))

products_dict["ед"] = list(set(products_dict.get("ед")))
print(products_dict)

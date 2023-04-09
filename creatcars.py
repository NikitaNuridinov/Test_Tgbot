# import json, io
 
# with open('C:\\Users\\wilda\\python_class\\git_new\\Telegrambot\\carsBase\\cars.json', 'r', encoding='utf-8') as f:
#     text = json.load(f)


# def none_del(x):
#     if x == None:
#         return 2023
#     else: 
#         return x
    

# def creat_db():
#     lt = list()
#     for brand in text:
#         for mod in brand["models"]:
#             lt.append(
#                 {'country' : brand["country"],
#                 'brand' : brand["name"],
#                 'model' : mod['name'],
#                 's_y' : mod["year-from"],
#                 'e_y' : none_del(mod["year-to"]),
#                 'image' : "https://yandex.ru/images/search?text="+ brand["name"] +"%20"+ mod['name'] +"%20" + str(none_del(mod["year-to"]))}
#             )
#     return lt

# with open("C:\\Users\\wilda\\python_class\\git_new\\Telegrambot\\carsBase\\car.json", 'w') as outfile:
#     json.dump(creat_db(), outfile)


# with io.open("C:\\Users\\wilda\\python_class\\git_new\\Telegrambot\\carsBase\\car.json", "w", encoding="utf-8") as fp:
#     s = json.dumps(creat_db(), ensure_ascii=False)
#     fp.write(s)


print("lista zakupów")
zakupy_dict = {
    "piekarnia":["chleb","bułki","pączek"],
    "warzywniak":["seler","marchew","rukola"]
}
for sklep,zakupy in zakupy_dict.items():
    for i in range(len(zakupy)):
        zakupy[i]=zakupy[i].capitalize()
        i=len(zakupy)
        i+=i
    print(f"Idę do sklepu {sklep.capitalize()} i kupuję tu następujące produkty {zakupy}")
print(f"w sumie kupuję tam {i} produktów")
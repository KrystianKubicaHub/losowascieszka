

def myFormat(l1):

    name = str(l1.get("Nazwa"))
    minW = str(l1.get("MinWiek"))
    maxW = str(l1.get("MaxWiek"))
    wym = str(l1.get("Wymiar"))

    result = "Nazwa zniżki to: " + name +" jej wymiar to " + wym + " przysłujuje ona osobą pomiędzy " + minW + " ,a " + maxW
    return result
def find(age, list):
    x1 = []
    for i in list:
        minAge = i.get("MinWiek")
        maxAge = i.get("MaxWiek")
        if(age>=minAge and age <=maxAge):
            x1.append(i)
    return x1


zniszka1 = {
    "Nazwa": "Młodzieżowa",
    "MinWiek": 10,
    "MaxWiek": 21,
    "wymiar": "37%"

}

zniszka2 = {
    "Nazwa": "Seniorska",
    "MinWiek": 60,
    "MaxWiek": 67,
    "wymiar": "49%"
}

zniszka3 = {
    "Nazwa": "Dziecinna",
    "MinWiek": 0,
    "MaxWiek": 9,
    "wymiar": "82%"

}

myList = [zniszka1, zniszka2, zniszka3]


while True:
    wiek = input("Podaj swój wiek: ")
    if(wiek.isdecimal()):
        w1 = find(int(wiek), myList)

        print("Wszystkie dostępne dla ciebie zniżki: ")
        for i in w1:
            toP = myFormat(i)
            print(toP)





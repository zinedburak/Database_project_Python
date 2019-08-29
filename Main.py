import sqlite3

con = sqlite3.connect("Cs_202.db")
cursor = con.cursor()


def mainMenu():
    print("-----Hello There Welcome To my Python Project-----")
    print("Please select the action by pressing the number")
    print("1 - ADD FARMER")
    print("2 - ADD FARMERS")
    print("3 - ADD PRODUCT")
    print("4 - ADD PRODUCTS")
    print("5 - ADD MARKET")
    print("6 - ADD MARKETS")
    print("7 - REGISTER PRODUCT")
    print("8 - REGISTER PRODUCTS")
    print("9 - SHOW TABLES")
    print("10 - LOAD DATA")
    print("11 - EXIT")


def executeList(queryList):
    for i in queryList:
        cursor.execute(i)


# Query part

def farmerQuery(attributes):
    farmerQueries = list()
    query = "Insert Into Farmers(FName,FSurname,Address,Zipcode,City) VALUES ('{}','{}','{}',{},'{}')".format(
        attributes[0], attributes[1], attributes[2].replace(" ", ""), int(attributes[3]), attributes[4])
    farmerQueries.append(query)
    farmerPhoneQuery(farmerQueries, attributes[0], attributes[1], attributes[5])
    farmerMailQuery(farmerQueries, attributes[0], attributes[1], attributes[6])
    return farmerQueries


def farmerPhoneQuery(farmerQueries, farmerName, farmerSurname, phoneNumbers):
    phoneNumbersList = phoneNumbers.split(">")
    for i in range(0, len(phoneNumbersList)):
        query = "Insert into FarmersPhone(Fname,Fsurname,FphoneNumber) VALUES ('{}','{}','{}')".format(farmerName,
                                                                                                       farmerSurname,
                                                                                                       phoneNumbersList[
                                                                                                           i])
        farmerQueries.append(query)


def farmerMailQuery(farmerQueries, farmerName, farmerSurname, Mails):
    mailList = Mails.split(">")
    for i in range(0, len(mailList)):
        query = "Insert into FarmerMail(Fname,Fsurname,FMail) VALUES ('{}','{}','{}')".format(farmerName, farmerSurname,
                                                                                              mailList[i])
        farmerQueries.append(query)


def ProductQuery(attributes):
    query = "Insert Into Products(Pname,Ppdate,Phdate,Palt,PminTemp,Phardness) VALUES ('{}','{}','{}',{},{},{})".format(
        attributes[0], attributes[1], attributes[2], int(attributes[3]), int(attributes[4]), int(attributes[5]))
    print(query)
    return query


def MarketQuery(attributes):
    query = "Insert Into Markets(Mname,Maddress,Mzipcode,Mcity,Mphone,Mbudget) VALUES ('{}','{}',{},'{}','{}',{})".format(
        attributes[0], attributes[1], int(attributes[2]), attributes[3], attributes[4], int(attributes[5]))
    return query


def registerQuery(attributes):
    query = "Insert Into Registers(Fname,Fsurname,Pname,amount,price,IBAN) VALUES ('{}','{}','{}',{},{},'{}')".format(
        attributes[0], attributes[1], attributes[2], int(attributes[3]), float(attributes[4]), attributes[5])
    return query


def buyQuery(attributes):
    query = "Insert into buys(Fname,Fsurname,Pname,Mname,Maddress,amount,CreditCard) values ('{}','{}','{}','{}','{}',{},'{}')".format(
        attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], int(attributes[5]), attributes[6])
    return query


def producesQuery(attributes):
    query = "insert into produces(Fname,Fsurname,Pname,amount,year) values ('{}','{}','{}',{},{})". \
        format(attributes[0], attributes[1], attributes[2], int(attributes[3]), int(attributes[4]))
    return query


# End of The Query Part


# add Part


def addFarmer(values):
    attributes = values.split(",")
    executeList(farmerQuery(attributes))
    con.commit()


def addFarmers(long_line):
    farmers = long_line.split(";")
    for farmer in farmers:
        attributes = farmer.split(",")
        executeList(farmerQuery(attributes))
    con.commit()


def addProduct(values):
    attributes = values.split(",")
    cursor.execute(ProductQuery(attributes))
    con.commit()


def addProducts(long_line):
    products = long_line.split(";")
    for product in products:
        attributes = product.split(",")
        cursor.execute(ProductQuery(attributes))
    con.commit()


def addMarket(values):
    attributes = values.split(",")
    cursor.execute(MarketQuery(attributes))
    con.commit()


def addMarkets(long_line):
    Markets = long_line.split(";")
    for market in Markets:
        attributes = market.split(",")
        cursor.execute(MarketQuery(attributes))
    con.commit()


def registerProduct(values):
    attributes = values.split(",")
    cursor.execute(registerQuery(attributes))
    con.commit()


def registerProducts(long_line):
    products = long_line.split(";")
    for product in products:
        attributes = product.split(",")
        cursor.execute(registerQuery(attributes))
    con.commit()


# End of add part


# show Tables
def showTables():
    showfarmers()
    showfarmersMail()
    showfarmersPhone()
    showMarkers()
    showProducts()
    showMarkers()
    showRegister()
    showBuys()
    showProduces()


def showfarmers():
    query = "Select * from Farmers"
    print("****Farmers****")
    generalShow(query)
    print("****Farmers End****")


def showfarmersPhone():
    print("****Farmers Phone****")
    query = "Select * from FarmersPhone"
    generalShow(query)
    print("****Farmers Phone End****")


def showfarmersMail():
    print("****Farmers Mail****")
    query = "select * from FarmerMail"
    generalShow(query)
    print(("****Farmers Mail End****"))


def showRegister():
    print("**** Register Table****")
    query = "select * from Registers"
    generalShow(query)
    print("**** Register Table End ****")


def showMarkers():
    print("**** Market Table****")
    query = "SELECT * FROM Markets"
    generalShow(query)
    print("**** Markets Table End ****")


def showProducts():
    print("**** Product Table****")
    query = "select * from Products"
    generalShow(query)
    print("**** Product Table End ****")


def showBuys():
    print("**** Buys Table****")
    query = "select * from buys"
    generalShow(query)
    print("**** Buys Table End ****")


def showProduces():
    print("**** Produces Table ****")
    query = "select * from produces"
    generalShow(query)
    print("Produces Table End")


def generalShow(query):
    cursor.execute(query)
    result = cursor.fetchall()
    for i in range(len(result)):
        print(result[i])


# end of Show Tables


# load Data Part
def loadFarmer():
    with open("farmers.csv", "r", encoding="utf-8") as file:
        allLines = file.readlines()
        attributes = list()
        for i in range(1, len(allLines)):
            line = allLines[i][:-1]
            attributes.append(line.split(";"))
            print(attributes)

        for i in attributes:
            print(i)
            executeList(farmerQuery(i))

        print("executed")
        con.commit()
        print("committed")


def loadMarkets():
    with open("markets.csv", "r", encoding="utf-8") as file:
        allLines = file.readlines()
        attributes = list()
        for i in range(1, len(allLines)):
            line = allLines[i][:-1]
            attributes.append(line.split(";"))
        for i in attributes:
            cursor.execute(MarketQuery(i))
        print("Executed Markets")
        con.commit()
        print("Committed Markets")


def loadproducts():
    with open("products.csv", "r", encoding="utf-8") as file:
        allLines = file.readlines()
        attributes = list()
        for i in range(1, len(allLines)):
            line = allLines[i][:-1]
            attributes.append(line.split(","))
        for i in attributes:
            print(i)
            cursor.execute(ProductQuery(i))
        print("Executed Products")
        con.commit()
        print("Commited Products")


def loadregister():
    with open("registers.csv", "r", encoding="utf-8") as file:
        allLines = file.readlines()
        attributes = list()
        for i in range(1, len(allLines)):
            line = allLines[i][:-1]
            attributes.append(line.split(";"))
        for i in attributes:
            cursor.execute(registerQuery(i))
        print("Executed Registers")
        con.commit()
        print("Commited Products")


def loadbuys():
    with open("buys.csv", "r", encoding="utf-8") as file:
        allLines = file.readlines()
        attributes = list()
        for i in range(1, len(allLines)):
            line = allLines[i][:-1]
            attributes.append(line.split(";"))
        for i in attributes:
            cursor.execute(buyQuery(i))

        print("Executed Buys")
        con.commit()
        print("Commited Buys")


def loadproduces():
    with open("produces.csv", "r", encoding="utf-8") as file:
        allLines = file.readlines()
        attributes = list()
        for i in range(1, len(allLines)):
            line = allLines[i][:-1]
            attributes.append(line.split(";"))

        for i in attributes:
            cursor.execute(producesQuery(i))

        print("Executed Producess")
        con.commit()
        print("Committed Produces")


# end of the load Data
if __name__ == '__main__':
    while True:
        mainMenu()
        choice = int(input())
        if choice == 11:
            con.close()
            break
        elif choice == 1:
            string = input("Please enter a string ")
            try:
                addFarmer(string)
                print("You Added New Farmer")
            except IndexError:
                print("Not enough Data")
            except sqlite3.IntegrityError:
                print("Dublicate Data")

        elif choice == 2:
            string = input("Please enter a string ")
            try:
                addFarmers(string)
                print("You Added New Farmers")
            except IndexError:
                print("Not enough Data")
            except sqlite3.IntegrityError:
                print("Dublicate Data")
        elif choice == 3:
            string = input("Please enter a string")
            try:
                addProduct(string)
                print("You have added new Product")
            except IndexError:
                print("Not enough Data")
            except sqlite3.IntegrityError:
                print("Dublicate Data")
        elif choice == 4:
            string = input("Please enter a string")
            try:
                addProducts(string)
                print("You have added new Products")
            except IndexError:
                print("Not enough Data")
            except sqlite3.IntegrityError:
                print("Dublicate Data")
        elif choice == 5:
            string = input("Please enter a string")
            try:
                addMarket(string)
                print("You have added new Market")
            except IndexError:
                print("Not enough Data")
            except sqlite3.IntegrityError:
                print("Dublicate Data")
        elif choice == 6:
            string = input("Please enter a string")
            try:
                addMarkets(string)
                print("You have added new Markets")
            except IndexError:
                print("Not enough Data")
            except sqlite3.IntegrityError:
                print("Dublicate Data")
        elif choice == 7:
            string = input("Please enter a string")
            try:
                registerProduct(string)
                print("You have register a product")
            except IndexError:
                print("Not enough Data")
            except sqlite3.IntegrityError:
                print("Dublicate Data")
        elif choice == 8:

            string = input("Please enter a string")
            try:
                registerProduct(string)
                print("You have register a product")
            except IndexError:
                print("Not enough Data")
            except sqlite3.IntegrityError:
                print("Dublicate Data")
        elif choice == 9:
            showTables()
        elif choice == 10:
            # loadFarmer()
            # loadMarkets()
            # loadproducts()
            # loadregister()
            # loadbuys()
            loadproduces()
        else:
            print("Wrong comment ")

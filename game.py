import mysql.connector

#tallenna pelaaja clienttiin
user = {
    "id": 0,
    "nimi": "lol",
    "raha": 0,
    "rating": 0,
    "laina": 0,
    "eräpäivä": 0,
    "päivä": 0
}

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='peli',
    user='root',
    password='salasana',
    autocommit=True
)
cursor = connection.cursor()

def login():
    print("Welcome to airport typhoon!")
    print("Are you a new player, or do you want to sign in?")
    userInput = int(input("Sign in (1) New user(2): "))

    if userInput == 2:
        createPlayer()

    if userInput == 1:
        userInput = input("Username: ")
        sql = f"SELECT * FROM `pelaaja` WHERE nimi = %s"

        cursor.execute(sql, (userInput,))

        results = cursor.fetchall()
        for row in results:
            user["id"] = row[0]
            user["nimi"] = row[1]
            user["raha"] = row[2]
            user["rating"] = row[3]
            user["laina"] = row[4]
            user["päivä"] = row[5]

        print(results)

        if not results:
            print("User not found")
        elif results:
            print("löytyy")
            

            startGame()

def createPlayer():
    raha = 1000
    print("Welcome to airport typhoon!")
    print("Start your journey by entering your name")
    playerName = input("Enter your name: ")

    sql = f"INSERT INTO `pelaaja` (nimi, raha) VALUES (%s, %s)"
    cursor.execute(sql, (playerName, raha))

def startGame():
    print("Welcome", user["nimi"])


#It starts here
login()


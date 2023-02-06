import mysql.connector

class Database:
    def __init__(self, host, port, username, password) -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host = self.host, port = self.port, user = self.username, password = self.password, auth_plugin = "mysql_native_password")
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT VERSION()")
            version = self.cursor.fetchone()
            print("MySQL version:", version[0])
            print("Connected Sucessfully.")
        except mysql.connector.Error as error:
            print("Could not login to host with user/password provided.")
            exit()

    def add_word(self, word):
        self.cursor.execute("""INSERT INTO dictionary.word (word) VALUES (%s)""", (word,))
        self.connection.commit()
        print(f"Added the word '{word}' to the database.")
    
    def check_word(self, word):
        self.cursor.execute(""" SELECT * FROM dictionary.word (word) VALUES (%s) """, (word,))
        checked = self.cursor.fetchall()
        self.connection.commit()
        return checked

    def update_word(self, new, old):
        self.cursor.execute("""UPDATE dictionary.word,
        SET word = %s WHERE word = %s, """ (new, old))
        self.connection.commit()
        print(f"Updated the word '{old}' to '{new}'. ")
    



def main():
    host = input("Enter Hostname:") 
    port = input("Enter Port:")
    username = input("Enter Username:")
    password = input("Enter Password:")

    database = Database(host, port, username, password)
    database.connect()

    word = input("What word do you want to add/change:")
    answer = database.check_word(word)
    if answer == True:
        new_answer = input(f"The word '{word}' already exists in the database, enter a new word:")
        database.update_word(word, new_answer)
    else:
        database.add_word(word)

if __name__ == '__main__':
    main()
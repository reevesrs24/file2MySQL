import pymysql.cursors
import os


# GLOBAL CONSTANTS
##########################
HOST="localhost"
PORT=33060
USER="homestead"
PASSWORD="secret"
DATABASE="homestead"
CHARSET="UTF8"
PATH="C:\\Users\\PIP\\Desktop\\wireframes"
##########################

# Function traverses a file and all sub directories
def read_file():

    # open file in designated path
    for root, dirs, files in os.walk(PATH):

        for name in files:

            # replace all white space with '_' in file name
            name = name.replace(" ", "_")

            # Use root path's last dir for 'type'
            dir = root.rsplit('\\', 1)[-1]

            # replace all white space with '_'
            dir = dir.replace(" ", "_")

            # use penultimate sub directory for 'app_type'
            app_type = root.rsplit('\\', 2)[-2]


            upload_to_database(name, dir, app_type)


# Function connects to MySQL database and inserts 3 value into database
def upload_to_database(name, type, app_type):

    # Connect to the database
    connection = pymysql.connect(host=HOST,
                                 port=PORT,
                                 user=USER,
                                 passwd=PASSWORD,
                                 db=DATABASE,
                                 charset=CHARSET,
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            # Create a new record
            sql = "INSERT INTO wireframes (name, type, app_type) VALUES (%s, %s, %s)"

            # execute sql command and input values
            cursor.execute(sql, (name, type, app_type))

        # commit changes to database
        connection.commit()

    finally:
        # close the connection to the database
        connection.close()

# MAIN
def main():
    readFile()


if __name__ == '__main__':
    main()

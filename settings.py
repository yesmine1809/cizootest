import tornado.ioloop
import tornado.web
import pymysql


def create_table():
    rows = db.query("CREATE TABLE videos (id LONGTEXT, titre TINYTEXT, nbvues LONGTEXT)")
    db.close()


if __name__ == "__main__":
    db = pymysql.connect(
        host="localhost", database="cizoodb",
        user="root", password="Cizoo123*")
    create_table()
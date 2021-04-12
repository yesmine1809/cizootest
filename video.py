import tornado.web
import mysql.connector
import json


class List(tornado.web.RequestHandler):
    def get(self):
        db.reconnect()
        cursor = db.cursor()
        cursor.execute("select * from videos")
        rows = cursor.fetchall()
        self.write(json.dumps(rows))
        db.close()

class DBHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print('set headers!!')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                        'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')

    def options(self):
        pass

    def post(self):
        id = self.get_argument('id', 'No data received')
        titre = self.get_argument('titre', 'No data received')
        nbvues = self.get_argument('nbvues', 'No data received')
        db.reconnect()
        cursor = db.cursor()
        sql = "INSERT INTO videos (id, titre, nbvues) VALUES (%s, %s, %s)"
        val = (id, titre, nbvues)
        cursor.execute(sql, val)
        db.commit()
        print(cursor.rowcount, "record inserted.")
        db.close()


application = tornado.web.Application([
    (r"/api/videos", List),
    (r"/api/add_video", DBHandler),
])

if __name__ == "__main__":
    print("starting db **** ")
    db = mysql.connector.connect(
        host="localhost", database="cizoodb",
        user="root", password="Cizoo123*")
    application.listen(8181)
    print("port 8181 **** ")
    tornado.ioloop.IOLoop.instance().start()

# coding = utf-8
# Yufeng Yang
__author__ = "Yufeng Yang"


from mysql.connector import pooling
from mysql.connector import Error
import mysql.connector

from app.models.DB_config import DB_NAME, DB_PASSWORD, DB_USR


class Db:

    def __init__(self):

        self.connection_pool = pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                                      pool_size=8,
                                                      pool_reset_session=True,
                                                      host='localhost',
                                                      database=DB_NAME,
                                                      user=DB_USR,
                                                      password=DB_PASSWORD)

    @staticmethod
    def conn_err():
        return -1

    def get_all_posts(self):
        try:
            conn = self.connection_pool.get_connection()
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Posts;")
                post_lists = cursor.fetchall()
                return post_lists
        except Error:
            self.conn_err()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_one_post(self, _id):
        try:
            conn = self.connection_pool.get_connection()
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Posts WHERE postid=%d;", _id)
                one_post = cursor.fetchone()
                return one_post
        except Error:
            self.conn_err()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_max_id(self):
        try:
            conn = self.connection_pool.get_connection()
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT MAX(postid) FROM Posts;")
                max_id = cursor.fetchone()
                return max_id
        except Error:
            self.conn_err()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def create_new_post(self, new_postid, ts):
        try:
            conn = self.connection_pool.get_connection()
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Posts VALUES(%s, %d, %s, %s, %s, %s)", "YYF", new_postid, "", "", ts, ts)
                max_id = cursor.fetchone()
                return max_id
        except Error:
            self.conn_err()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


db = Db()

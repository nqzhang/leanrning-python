import string
import random
import mysql.connector
import redis

config = {
  'user': 'root',
  'password': '11QQqqWW',
  'host': '127.0.0.1',
  'database': 'learningpython',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def GenInviteCode():
    str = ''.join(random.sample(string.ascii_lowercase, 15))
    add_code = ("insert into invite_code values ('%s')"%str)
    cursor.execute((add_code))
    r.lpush('invite_code',str)

n=0
while n <= 200:
    GenInviteCode()
    n += 1

cnx.commit()
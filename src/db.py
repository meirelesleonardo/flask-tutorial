import pymysql
from decouple import config


mysql = pymysql.connect(host=config('HOST_BD_MYSQL'), port=3306, user=config('USER_BD_MYSQL'), database=config('DATABASE_BD_MYSQL'))
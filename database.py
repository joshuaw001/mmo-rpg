import pymysql as sql

if not users_db and not players_cur:
    users_db = sql.connect("localhost","admin","p@ssword","data/users")
    users_cur = sql.cursor()

if not players_db and not players_cur:
    players_db = sql.connect("localhost","admin","p@ssword","data/players")
    players_cur = sql.cursor()

# create tables if not exists

user_cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, level RANKS);")

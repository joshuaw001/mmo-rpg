import pymysql as sql

if not users_db and not players_cur:
    users_db = sql.connect("localhost","admin","p@ssword","data/users")
    users_cur = sql.cursor()

if not players_db and not players_cur:
    players_db = sql.connect("localhost","admin","p@ssword","data/players")
    players_cur = sql.cursor()

# create tables if not exists
user_cur.execute("ENUM RANKS(beginner=0,starter=1,rookie=2,journeyman=3,master=4,expert=5,king=6,`king2`=7,`king3`=8);")
user_cur.execute("CREATE TABLE IF NOT EXISTS users (id INT,username TEXT, password TEXT, level RANKS);")
user_cur.execute("INSERT INTO users VALUES(1,'admin','p@ssword',`king3`);")
user_cur.fetchone()

player_cur.execute("ENUM RACES(pixel,square,circle,triangle,npc);")
player_cur.execute("CREATE TABLE IF NOT EXISTS players (id INT, user TEXT,health INT,xp INT(5),items INT);"

import asyncio
from model import *

async def insert_Top_Manga_Into_DB(id_anime, name_manga, score, descript_pro, ranked, popularity, poster, genres):
	connect_mysql = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
	cursor = connect_mysql.cursor()
	try:
		sqlite_insert_with_param = """INSERT INTO Top_Manga
						(id_anime, name_manga, score, descript_pro, ranked, popularity, poster, genres) 
						VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

		data_tuple = (id_anime, name_manga, score, descript_pro, ranked, popularity, poster, genres)
		cursor.execute(sqlite_insert_with_param, data_tuple)
		connect_mysql.commit()
		print("Top Manga inserted successfully into table: " + id_anime)
		cursor.close()

	except mysql.connector.Error as error:
		connect_mysql.rollback()
		print("Failed to insert Top Manga variable into sqlite table:", error)
	finally:
		if connect_mysql:
			connect_mysql.close()
			print("The SQLite connection is closed")


async def start_insert_Top_Manga_data_Into_DB(data):
	for anime in data:
		id_anime = anime.get("id_anime")
		name_manga = anime.get("name_manga")
		score = anime.get("score")
		descript_pro = anime.get("descript_pro")
		ranked = anime.get("ranked")
		popularity = anime.get("popularity")
		poster = anime.get("poster")
		genres = anime.get("genres")

		await insert_Top_Manga_Into_DB(id_anime, name_manga, score, descript_pro, ranked, popularity, poster, genres)

data = get_data_json(Top_Manga)
asyncio.run(start_insert_Top_Manga_data_Into_DB(data))
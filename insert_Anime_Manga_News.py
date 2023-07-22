import asyncio
from model import *

async def insert_Anime_Manga_News_Into_DB(idNews, time_news, category, title_news, profile_user_post, images_poster, descript_pro, number_comment):
	connect_mysql = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
	cursor = connect_mysql.cursor()
	try:
		sqlite_insert_with_param = """INSERT INTO Anime_Manga_News
						(idNews, time_news, category, title_news, profile_user_post, images_poster, descript_pro, number_comment) 
						VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

		data_tuple = (idNews, time_news, category, title_news, profile_user_post, images_poster, descript_pro, number_comment)
		cursor.execute(sqlite_insert_with_param, data_tuple)
		connect_mysql.commit()
		print("Anime Manga News inserted successfully into table: " + idNews)
		cursor.close()

	except mysql.connector.Error as error:
		connect_mysql.rollback()
		print("Failed to insert Anime Manga News variable into sqlite table:", error)
	finally:
		if connect_mysql:
			connect_mysql.close()
			print("The SQLite connection is closed")


async def start_insert_Anime_Manga_News_data_Into_DB(data):
	for anime in data:
		idNews = anime.get("idNews")
		time_news = anime.get("time_news")
		category = anime.get("category")
		title_news = anime.get("title_news")
		profile_user_post = anime.get("profile_user_post")
		images_poster = anime.get("images_poster")
		descript_pro = anime.get("descript_pro")
		number_comment = anime.get("number_comment")
		await insert_Anime_Manga_News_Into_DB(idNews, time_news, category, title_news, profile_user_post, images_poster, descript_pro, number_comment)

data = get_data_json(Anime_Manga_News)
asyncio.run(start_insert_Anime_Manga_News_data_Into_DB(data))

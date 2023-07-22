import asyncio
from model import *

async def insert_Reviews_Top_Manga_Into_DB(id_reviews, id_manga, user, avatar_user, profile_user_reviews, content_reviews, time_reviews):
	connect_mysql = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
	cursor = connect_mysql.cursor()
	try:
		sqlite_insert_with_param = """INSERT INTO Reviews_Top_Manga
						(id_reviews, id_manga, user, avatar_user, profile_user_reviews, content_reviews, time_reviews) 
						VALUES (%s, %s, %s, %s, %s, %s, %s);"""

		data_tuple = (id_reviews, id_manga, user, avatar_user, profile_user_reviews, content_reviews, time_reviews)
		cursor.execute(sqlite_insert_with_param, data_tuple)
		connect_mysql.commit()
		print("Reviews Top Manga inserted successfully into table: " + id_reviews)
		cursor.close()

	except mysql.connector.Error as error:
		connect_mysql.rollback()
		print("Failed to insert Reviews Top Manga variable into sqlite table:", error)
	finally:
		if connect_mysql:
			connect_mysql.close()
			print("The SQLite connection is closed")


async def start_insert_Reviews_Top_Manga_data_Into_DB(data):
	for review in data:
		id_reviews = review.get("id_reviews")
		id_manga = review.get("id_manga")
		user = review.get("user")
		avatar_user = review.get("avatar_user")
		profile_user_reviews = review.get("profile_user_reviews")
		content_reviews = review.get("content_reviews")
		time_reviews = review.get("time_reviews")
		await insert_Reviews_Top_Manga_Into_DB(id_reviews, id_manga, user, avatar_user, profile_user_reviews, content_reviews, time_reviews)

data = get_data_json(Reviews_Top_Manga)
asyncio.run(start_insert_Reviews_Top_Manga_data_Into_DB(data))


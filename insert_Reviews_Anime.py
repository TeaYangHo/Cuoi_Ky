import asyncio
from model import *

async def insert_Reviews_Anime_Into_DB(idReview, noi_dung, link_anime, link_avatar_user_comment, link_user, time_review):
	connect_mysql = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
	cursor = connect_mysql.cursor()
	try:
		sqlite_insert_with_param = """INSERT INTO Reviews_Anime
						(idReview, noi_dung, link_anime, link_avatar_user_comment, link_user, time_review) 
						VALUES (%s, %s, %s, %s, %s, %s);"""

		data_tuple = (idReview, noi_dung, link_anime, link_avatar_user_comment, link_user, time_review)
		cursor.execute(sqlite_insert_with_param, data_tuple)
		connect_mysql.commit()
		print("Reviews Anime inserted successfully into table: " + idReview)
		cursor.close()

	except mysql.connector.Error as error:
		connect_mysql.rollback()
		print("Failed to insert Reviews Anime variable into sqlite table:", error)
	finally:
		if connect_mysql:
			connect_mysql.close()
			print("The mysql connection is closed")


async def start_insert_Reviews_Anime_data_Into_DB(data):
	for review in data:
		idReview = review.get("idReview")
		noi_dung = review.get("noi_dung")
		link_anime = review.get("link_anime")
		link_avatar_user_comment = review.get("link_avatar_user_comment")
		link_user = review.get("link_user")
		time_review = review.get("time_review")

		await insert_Reviews_Anime_Into_DB(idReview, noi_dung, link_anime, link_avatar_user_comment, link_user, time_review)

data = get_data_json(Reviews_Anime)
asyncio.run(start_insert_Reviews_Anime_data_Into_DB(data))



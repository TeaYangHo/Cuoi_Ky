import asyncio
from model import *

async def insert_Comment_News_Into_DB(id_comment, id_news, user_comment, profile_user_comment, comment, time_comment):
	connect_mysql = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
	cursor = connect_mysql.cursor()
	try:
		sqlite_insert_with_param = """INSERT INTO Comment_News
						(id_comment, id_news, user_comment, profile_user_comment, comment, time_comment) 
						VALUES (%s, %s, %s, %s, %s, %s);"""

		data_tuple = (id_comment, id_news, user_comment, profile_user_comment, comment, time_comment)
		cursor.execute(sqlite_insert_with_param, data_tuple)
		connect_mysql.commit()
		print("Comment News inserted successfully into table: " + id_comment)
		cursor.close()

	except mysql.connector.Error as error:
		connect_mysql.rollback()
		print("Failed to insert Comment News variable into sqlite table:", error)
	finally:
		if connect_mysql:
			connect_mysql.close()
			print("The SQLite connection is closed")


async def start_insert_Comment_News_data_Into_DB(data):
	for comment in data:
		id_comment = comment.get("id_comment")
		id_news = comment.get("id_news")
		user_comment = comment.get("user_comment")
		profile_user_comment = comment.get("profile_user_comment")
		comment_text = comment.get("comment")
		time_comment = comment.get("time_comment")
		await insert_Comment_News_Into_DB(id_comment, id_news, user_comment, profile_user_comment, comment_text, time_comment)

data = get_data_json(Comment_News)
asyncio.run(start_insert_Comment_News_data_Into_DB(data))


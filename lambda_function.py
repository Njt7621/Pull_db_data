import json
import boto3
import os
import psycopg2

hostname = ''
database = ''
port = 123
username = ''
password = ''

# SQL connection variables
conn = psycopg2.connect(host=hostname, database= database, port=port, user=username, password=password)
cur = conn.cursor()

"""
Open and read the query than format the data and return as a json dict
"""
def pull_info(id1):
	f = open('sql_statment.sql')
	x = f.read()
	
	try:
		SQL = x.format(id1)
		
		cur.execute(SQL)
		conn.commit()
		
		#print(cur.fetchall())
		
		fields1 = [i[0] for i in cur.description]
			#print(fields1)
		
		results1 = []
		for row in cur.fetchall():
			results1.append(dict(zip(fields1, row)))
		
		
		return json.dumps(results1, indent=2)
	except:
		SQL = 'rollback'
		
		cur.execute(SQL)
		conn.commit()
		
		return 'Failed'
		
if __name__ == '__main__':
	user = input("Input Account Id: ")
	print(user)
	results = pull_info(user)
	print(results)
	conn.close()

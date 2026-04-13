from api_request import mock_fetch_data
import psycopg2
import os

def connect_to_db():
    print("Connecting to database...")
    try:
        conn = psycopg2.connect(
            host="db",
            database="weather_project",
            port=5432,
            user= "phongthanh",
            password="thangkhung0993"
        )
        return conn
    except psycopg2.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        raise

def create_table(conn):
    print("Creating table if not exists...")
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE SCHEMA IF NOT EXISTS dev;
                CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                    id SERIAL PRIMARY KEY,
                    city TEXT,
                    temperature FLOAT,
                    weather_description TEXT,
                    wind_speed FLOAT,
                    time TIMESTAMP,
                    inserted_at TIMESTAMP DEFAULT NOW(),
                    utc_offet TEXT
                );
            """)
            conn.commit()
            print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"An error occurred while creating the table: {e}")
        raise
def insert_weather_data(conn,weather_data):
    print("Inserting weather data into database...")
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO dev.raw_weather_data(
                    city,
                    temperature,
                    weather_description,
                    wind_speed,
                    time,
                    inserted_at,
                    utc_offet
                )
                VALUES(%s,%s,%s,%s,NOW(),%s,%s)  
            """, (weather_data['location']['name'],
            weather_data['current']['temperature'],
            weather_data['current']['weather_descriptions'][0],
            weather_data['current']['wind_speed'],
            weather_data['location']['localtime'],
            weather_data['location']['utc_offset']
            ))
        conn.commit()
        print("Data successfully inserted")
    except psycopg2.Error as e:
        print(f"Error with {e}")
        raise
def main ():
    try:
        data=mock_fetch_data()
        conn=connect_to_db()
        create_table(conn)
        insert_weather_data(conn,data)
    except Exception as e:
        print(f"An error:{e}")
        raise
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")
main()
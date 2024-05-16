from django.shortcuts import render
from django.views.generic import TemplateView 
# Create your views here.
import psycopg2
from config import load_config
import csv

def create_tables():
    commands = (
        """
        CREATE TABLE airline_customer_satisfaction (
            airline_customer_id SERIAL PRIMARY KEY,
            satisfaction VARCHAR(255) NOT NULL,
            customer_type VARCHAR(255),
            age INTEGER,
            type_of_travel VARCHAR(255),
            class VARCHAR(255),
            flight_distance INTEGER
            );
""",
    )
    # Flight Distance,Seat comfort,Departure/Arrival time convenient,Food and drink,Gate location,Inflight wifi service,Inflight entertainment,Online support,Ease of Online booking,On-board service,Leg room service,Baggage handling,Checkin service,Cleanliness,Online boarding,Departure Delay in Minutes,Arrival Delay in Minutes
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                
                for command in commands:
                    
                    cur.execute(command)
                    
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_category(category_name):
    sql = """INSERT INTO categories(category_name)
    VALUES(%s) RETURNING category_id;"""
    config = load_config()
    category_id = None
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (category_name,))
                rows = cur.fetchone()
                if rows:
                    category_id = rows[0]
                conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return category_id

def update_category(category_name, category_id):
    updated_row_count = 0
    sql = """UPDATE categories
                SET category_name = %s
                WHERE category_id = %s"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (category_name, category_id))
                updated_row_count = cur.rowcount
            conn.commit()
    except(Exception, psycopg2.DatabaseError ) as error:
        print(error)    
    finally:
        return updated_row_count

def get_categories():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT category_id, category_name FROM categories ORDER BY category_name")
                print("", cursor.rowcount)
                row = cursor.fetchone()

                while row is not None:
                    print(row)
                    row = cursor.fetchone()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    


    

    input_file = 'C:\\Users\\svaju\\Downloads\\archive\\Airline_customer_satisfaction.csv'
    output_file = 'C:\\Users\\svaju\\Downloads\\archive\\Airline_customer_satisfaction_filtered.csv'

    desired_columns = ['satisfaction', 'Customer Type', 'Age', 'Type of Travel', 'Class', 'Flight Distance']

    # Adjust these indices to match your desired columns' positions in the CSV file
    desired_indices = [0, 1, 2, 3, 4, 5]  # Example indices, adjust as needed

    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        header = next(reader)
        writer.writerow([header[i] for i in desired_indices])
        
        for row in reader:
            writer.writerow([row[i] for i in desired_indices])

    print("Filtered CSV file created successfully.")


class HomePageView(TemplateView):
    template_name = "index.html"
   
    




from django.shortcuts import render
from django.views.generic import TemplateView 
# Create your views here.
import psycopg2
from config import load_config

def create_tables():
    commands = (
        """
        CREATE TABLE categories (
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR(255) NOT NULL
            )
""","""
        CREATE TABLE films (
        film_id SERIAL PRIMARY KEY,
        film_name VARCHAR(255) NOT NULL,
        FOREIGN KEY (film_id)
        REFERENCES categories (category_id)
        ON UPDATE CASCADE ON DELETE CASCADE
        )
"""
    )
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
    

class HomePageView(TemplateView):
    template_name = "index.html"
    update_category("Horror", 3)
    




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


class HomePageView(TemplateView):
    template_name = "index.html"
    create_tables()




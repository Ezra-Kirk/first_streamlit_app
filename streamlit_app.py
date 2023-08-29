import streamlit
import pandas

streamlit.title("My Parents' New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega and Blueberry Oats")
streamlit.text("🥗 Kale & Spinach Smoothie")
streamlit.text("🐔 Hard-boiled Egg")
streamlit.text("🥑 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# display dataframe in app
streamlit.dataframe(my_fruit_list)

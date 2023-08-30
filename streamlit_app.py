import streamlit
import pandas
import requests

streamlit.title("My Parents' New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega and Blueberry Oats")
streamlit.text("🥗 Kale & Spinach Smoothie")
streamlit.text("🐔 Hard-boiled Egg")
streamlit.text("🥑 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display dataframe in app
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# New section to import Fruity Vice response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "fruit_choice")


# turn json response into tabular data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# then turn into dataframe
streamlit.dataframe(fruityvice_normalized)

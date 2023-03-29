import streamlit as st;
import pandas;
import requests;

st.title('My Parents New Healthy Diner')
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')


st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# Display the table on the page.
fruit_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruit_to_show)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
st.header("Fruityvice Fruit Advice!")
# st.text(fruityvice_response.json())

# write your own comment -what does the next line do? deserialize json
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?  create table
st.dataframe(fruityvice_normalized)

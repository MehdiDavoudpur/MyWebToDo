import streamlit as st
from Functions import read, delete

my_filepath = "C:/Users/Mehdi/PycharmProjects/pythonProject/To_Do_List.txt"

todos = read(my_filepath)

for key, todo in enumerate(todos):
    checkbox = st.checkbox(todo)
    if checkbox:
        delete(my_filepath, todos[key])

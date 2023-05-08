import streamlit as st
from Functions import read, delete, add

my_filepath = "C:/Users/Mehdi/PycharmProjects/pythonProject/To_Do_List.txt"

new_todo = st.text_input(label="enter new todo".title())

button_add = st.button('Add')

todos = read(my_filepath)

for key, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=key)
    if checkbox:
        delete(my_filepath, todos[key])
        st.experimental_rerun()
if button_add:
    add(my_filepath, new_todo)
    st.experimental_rerun()

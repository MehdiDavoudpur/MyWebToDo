import streamlit as st
from Functions import read, delete, add
import os

my_filepath = 'To_Do_List.txt'


def get_new_todo():
    add(my_filepath, st.session_state['n_todo'])


new_todo = st.text_input(label='', placeholder="enter new todo".title(), key='n_todo', on_change=get_new_todo)

try:
    todos = read(my_filepath)
except FileNotFoundError:
    with open('To_Do_List.txt', 'w') as file:
        todos = read(my_filepath)
        st.write(os.path.abspath('To_Do_List.txt'))

for key, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=key)
    if checkbox:
        delete(my_filepath, todos[key])
        st.experimental_rerun()

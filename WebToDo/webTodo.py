import streamlit as st
from Functions import read, delete, add

my_filepath = '/WebToDo/To_Do_List.txt'


def get_new_todo():
    add(my_filepath, st.session_state['n_todo'])


new_todo = st.text_input(label='', placeholder="enter new todo".title(), key='n_todo', on_change=get_new_todo)

todos = ["a","b","c","d","e"]

for key, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=key)
    if checkbox:
        delete(my_filepath, todos[key])
        st.experimental_rerun()

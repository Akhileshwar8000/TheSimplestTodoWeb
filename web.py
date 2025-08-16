import streamlit as st
import functions

def add_todo():
    todo = st.session_state["todo"]
    functions.append_todo(todo)


todos = functions.get_todos()
st.title("TheSimplestTodo")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos =functions.get_todos()
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo", on_change=add_todo, key="todo")
from flask import Flask, redirect, render_template, request, url_for

from todo_list.server.todo_list import TodoList

app = Flask(__name__)

todo_list = TodoList()


@app.route('/', methods=['GET', 'POST'])
def home():
    todo_list.add_task(request.form.get('new_task_name'))
    todo_list.complete_task(request.form.get('index'))
    todo_list.change_status(request.form.get('status'))
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('home.html', todo_list=todo_list, enumerate=enumerate)

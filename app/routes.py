from flask import Blueprint, render_template, redirect, url_for, request
from .models import Task
from .forms import TaskForm
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('main.index'))

    tasks = Task.query.order_by(Task.due_date).all()
    return render_template('index.html', form=form, tasks=tasks)

@main.route('/complete/<int:task_id>')
def complete(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))
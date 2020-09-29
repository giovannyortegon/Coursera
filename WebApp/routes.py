from app import App, db 
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
from datetime import datetime
import forms

@App.route('/')
@App.route("/index")
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@App.route("/about", methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        # print('Submited title: ', form.title.data)
        #return render_template('about.html', form=form, title=form.title.data)
        t =  Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task added to the database')
        return redirect(url_for('index'))
    return render_template('about.html', form=form)

@App.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task has been update')
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    else:
        flash('Task not found')
    return redirect(url_for('index'))


@App.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been deleted')
            return redirect(url_for('index'))

        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    else:
        flash('Task not found')
    return redirect(url_for('index'))
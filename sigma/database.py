import sqlite3
import os


def create_table():
    if not os.path.isfile("tasks.db"):
        db = sqlite3.connect('tasks.db')
        cur = db.cursor()

        cur.execute('CREATE TABLE tasks (name text, description text, time timestamp, notify boolean)')

        db.commit()
        db.close()


def run_query(query):
    results = []

    db = sqlite3.connect('tasks.db')
    cur = db.cursor()

    for result in cur.execute(query):
        results.append(result)

    db.commit()
    db.close()

    return results


def add_task(task_name, description, task_date, notify):
    db = sqlite3.connect('tasks.db')
    cur = db.cursor()

    cur.execute('''INSERT INTO tasks VALUES (?, ?, ?, ?)''', [task_name, description, task_date, notify])

    db.commit()
    db.close()

from my_sub_project.celery_app import app


@app.task
def add(a, b):
    print('this is the add function')
    return a+b

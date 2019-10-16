from my_sub_project.main_celery.celery import app


@app.task
def main_coll_task():
    print('this is the main collection')
    return 'the run_id of collection'

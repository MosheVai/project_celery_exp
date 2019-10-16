from my_sub_project.main_celery.celery_app import app


@app.task
def main_evaluation_task(run_id):
    print(f'the run id {run_id} passed passed to evaluation')

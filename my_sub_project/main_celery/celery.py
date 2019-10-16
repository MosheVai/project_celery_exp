from celery import Celery

app = Celery('tasks',
             broker='amqp://guest@localhost//',
             backend='amqp://guest@localhost//',
             include=['my_sub_project.collection.main_collection',
                      'my_sub_project.eval.main_eval'])


if __name__ == '__main__':
    app.start()

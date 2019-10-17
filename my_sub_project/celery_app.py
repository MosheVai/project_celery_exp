from celery import Celery

app = Celery('.',
             broker='amqp://guest@localhost//',
             backend='amqp://guest@localhost//',
             include=['calculations.math_funcs']
             )

if __name__ == '__main__':
    app.start()


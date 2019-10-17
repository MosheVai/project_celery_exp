The celery app is located in  `my_sub_project/celery_app.py`

i run it using the following command:

`celery -A celery_app worker -l info -P gevent`

The data flow code is located in `my_sub_project/piplines/run_math_pipeline.py`

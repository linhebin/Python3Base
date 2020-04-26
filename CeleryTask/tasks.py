from celery import Celery


app = Celery('tasks', broker='redis://:ppsredis@10.15.188.22:6379/9', backend='redis://:ppsredis@10.15.188.22:6379/10')


@app.task
def add(x, y):
    return x + y

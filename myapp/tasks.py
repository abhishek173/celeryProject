from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask,IntervalSchedule
import json


# Create Schedule every 40 seconds
# schedule, created = IntervalSchedule.objects.get_or_create(
#     every=40,
#     period=IntervalSchedule.SECONDS,
# )

# PeriodicTask.objects.get_or_create(
#     name="Clear RabbitMQ periodic task",
#     task="myapp.tasks.clear_rabbit_mq_data",
#     interval=schedule,
#     args=json.dumps((["hello"])), # pass the arguments to the task as a JSON-encoded  list
# )

@shared_task
def sub(x,y):
    sleep(10)
    return x-y

@shared_task
def clear_session_cache(id):
    print(f"Session Cache Cleared: {id}")
    return id

@shared_task
def clear_redis_data(key):
    print(f"Redis Data Cleared: {key}")
    return key

@shared_task
def clear_rabbit_mq(key):
    print(f"RabbitMQ Data Cleared: {key}")
    return key 

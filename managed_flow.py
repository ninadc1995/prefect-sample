from datetime import timedelta
from time import sleep

from prefect import flow, task
from prefect.tasks import task_input_hash
from prefect.cache_policies import TASK_SOURCE, INPUTS

cache_policy = (TASK_SOURCE + INPUTS).configure(key_storage="./cache/storage")

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(seconds=300), log_prints=True)
def run_expensive_task(x: int):
    print("----------------------Running expensive task----------------------")
    sleep(15)
    return x * 2


@task
def create_message():
    return f"This is prefect managed flow!"


@flow(log_prints=True)
def managed_flow():
    msg = create_message()
    print(msg)
    y = run_expensive_task(10)
    print(f"Output of expensive task: {y}")

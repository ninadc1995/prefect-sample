from time import sleep

from prefect import flow, task


@task
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

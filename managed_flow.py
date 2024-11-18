from prefect import flow, task


@task
def create_message():
    return f"This is prefect managed flow!"


@flow(log_prints=True)
def managed_flow():
    msg = create_message()
    print(msg)

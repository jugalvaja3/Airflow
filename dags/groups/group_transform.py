from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

def transform_tasks():
    with TaskGroup('transform',tooltip='transform group') as group:
        t1=BashOperator(
            task_id='t1',
            bash_command='sleep 5'
        )

        t2=BashOperator(
            task_id='t2',
            bash_command='sleep 5'
        )

        return group
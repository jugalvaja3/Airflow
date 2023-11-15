from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

def download_tasks(): 
    with TaskGroup('downloads',tooltip='download tasks') as group:

        d1=BashOperator(
            task_id='d1',
            bash_command='sleep 5'
        )
        d2=BashOperator(
            task_id='d2',
            bash_command='sleep 5'
        )
        d3=BashOperator(
            task_id='d3',
            bash_command='sleep 5'
        )

        return group
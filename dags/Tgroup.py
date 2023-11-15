from airflow import DAG
from airflow.operators.bash import BashOperator
from groups.group_downloads import download_tasks
from groups.group_transform import transform_tasks
from datetime import datetime

with DAG('Tgroup', start_date=datetime(2022,1,1), schedule='@daily',catchup=False) as dag:
    
    download=download_tasks()

    c=BashOperator(
        task_id='c',
        bash_command='sleep 5'
    )
    
    transform=transform_tasks()

    download>>c>>transform
    

    
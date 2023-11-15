from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG('parallel_dag',start_date=datetime(2022,1,1),schedule='@daily', catchup=False):
    t1=BashOperator(
        task_id='t1',
        bash_command = 'sleep 5'
    )

    t2=BashOperator(
        task_id='t2',
        bash_command = 'sleep 10'
    )

    t3=BashOperator(
        task_id='t3',
        queue='high_cpu',
        bash_command = 'sleep 30'
    )

    t4=BashOperator(
        task_id='t4',
        bash_command = 'sleep 5'
    )

    t1>>[t2,t3]>>t4
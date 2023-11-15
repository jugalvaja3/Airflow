from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from subdags.subdag_downloads import subdag_downloads

with DAG('group_dag',start_date=datetime(2022,1,1),schedule_interval='@daily',catchup=False) as dag:
    
    args={'start_date':dag.start_date,'schedule':dag.schedule_interval,'catchup':dag.catchup }

    downloads=SubDagOperator(
        task_id='downloads',
        subdag=subdag_downloads(dag.dag_id,'downloads',args)

    )

    check_file=BashOperator(
        task_id='check_file',
        bash_command='sleep 5'
    )

    transform_a=BashOperator(
        task_id='transform_a',
        bash_command='sleep 5'
    )

    transform_b=BashOperator(
        task_id='transform_b',
        bash_command='sleep 5'
    )

    transform_c=BashOperator(
        task_id='transform_c',
        bash_command='sleep 5'
    )

    downloads>>check_file>>[transform_a,transform_b,transform_c]
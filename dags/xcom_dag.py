from airflow import DAG 
from airflow.operators.python import PythonOperator,BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('xcom_dag',start_date=datetime(2022,1,1), schedule='@daily', catchup=False):
    def _t1(ti):
        ti.xcom_push(key='my_val',value=42)

    def _t2(ti):
        print(ti.xcom_pull(key='my_val',task_ids=['t1']))

    def _branch(ti):
        val=ti.xcom_pull(key='my_val',task_ids=['t1'])
        if val==42:
            return 't2'
        return 't3'

    t1=PythonOperator(
        task_id='t1',
        python_callable=_t1
    )

    t2=PythonOperator(
        task_id='t2',
        python_callable=_t2
    )

    branch=BranchPythonOperator(
        task_id='branch',
        python_callable=_branch
    )

    t3=BashOperator(
        task_id='t3',
        bash_command='sleep 5'
    )

    t4=BashOperator(
        task_id='t4',
        bash_command='sleep 5',
        trigger_rule='none_failed_min_one_success'
    )

    t1>>branch>>[t2,t3]>>t4
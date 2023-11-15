from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

my_file=Dataset('/tmp/my_file.txt')
my_file2=Dataset('/tmp/my_file2.txt')

with DAG('producer',start_date=datetime(2022,2,2),schedule='@daily',catchup=False):

    @task(outlets=[my_file])
    def update_file():
        with open(my_file.uri,"+a") as file:
            file.write("producer update...")

    @task(outlets=[my_file2])
    def update_file2():
        with open(my_file2.uri,"+a") as file:
            file.write("producer update2...")

    update_file()>>update_file2() 

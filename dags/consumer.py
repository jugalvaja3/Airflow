from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

my_file=Dataset('/tmp/my_file.txt')
my_file2=Dataset('/tmp/my_file2.txt')

with DAG('consumer', start_date=datetime(2022,2,2),schedule=[my_file,my_file2],catchup=False):

    @task
    def read_file():
        with open(my_file.uri,'r') as f:
            print(f.read())

    read_file()
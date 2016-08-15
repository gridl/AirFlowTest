from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


# Following are defaults which can be overridden later on

default_args = {
    'owner' :'ingvay7',
    'depends_on_past' : True,
    'start_date': datetime(2016, 8, 13),
    'email': ['vishwanath79@outlook.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'preset':'@daily'

}

dag = DAG('s3test', default_args=default_args)

# t1, t2, t3 and t4 are examples of tasks created using operators

t1 = BashOperator(task_id='task_1', bash_command ='aws s3 ls', dag=dag)

t2 = BashOperator(task_id='task_2', bash_command ='echo "Testing s3"', dag=dag)

# t3 = BashOperator(task_id='task_3', bash_command ='echo "Testing Task 3"', dag=dag)
#
# t4 = BashOperator(task_id='task_4', bash_command ='echo "Testing Task 4"', dag=dag)


t2.set_upstream(t1)

# Changed default cfg file post installation to reflect correct path

# print the list of active DAGs
#airflow list_dags

# prints the list of tasks the "tutorial" dag_id
#airflow list_tasks TestingAF

# prints the hierarchy of tasks in the tutorial DAG
#airflow list_tasks TestingAF --tree

# initialize the database
#airflow initdb

# start the web server, default port is 8080
#airflow webserver -p 8080

#airflow backfill TestingAF -s 2015-01-01 -e 2015-01-02

#airflow run s3test task_2 2016-08-13

#airflow clear -s 2016-08-09 -e 2016-08-13 -sd ~/airflow/dags s3test

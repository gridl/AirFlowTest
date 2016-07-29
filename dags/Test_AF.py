from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


# Following are defaults which can be overridden later on

default_args = {
    'owner' :'ingvay7',
    'depends_on_past' : False,
    'start_date': datetime(2016, 7, 29),
    'email': ['vishwanath79@outlook.com'],
    'email_on_feailure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('TestingAF', default_args=default_args)

# t1, t2, t3 and t4 are examples of tasks created using operators

t1 = BashOperator(task_id='task_1', bash_command ='echo "Testing Task 1"', dag=dag)

t2 = BashOperator(task_id='task_2', bash_command ='echo "Testing Task 2"', dag=dag)

t3 = BashOperator(task_id='task_3', bash_command ='echo "Testing Task 3"', dag=dag)

t4 = BashOperator(task_id='task_4', bash_command ='echo "Testing Task 4"', dag=dag)

t5 = BashOperator(task_id='print_date',bash_command='date',dag=dag)

t2.set_upstream(t1)
t3.set_upstream(t1)
t4.set_upstream(t2)
t4.set_upstream(t3)
t5.set_upstream(t3)

# Changed default cfg file post installation to reflect correct path

# print the list of active DAGs
#airflow list_dags

# prints the list of tasks the "tutorial" dag_id
#airflow list_tasks TestingAF

# prints the hierarchy of tasks in the tutorial DAG
#airflow list_tasks TestingAF --tree

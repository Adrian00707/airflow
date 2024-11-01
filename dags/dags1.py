from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime as dt

default_args = {
    'owner': 'etl_user',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 1),
}

dag = DAG('get-currates', default_args=default_args, schedule_interval='0 1 * * *', catchup=True,
          max_activate_task=1, max_activate_runs=1, tags=['aderdyshev'])

task1 = BashOperator(
    task_id='task1',
    bash_command='python3 /airflow/scripts/dag1/task1.py',
    dag=dag)

task2 = BashOperator(
    task_id='task2',
    bash_command='python3 /airflow/scripts/dag1/task2.py',
    dag=dag)

task1 >> task2

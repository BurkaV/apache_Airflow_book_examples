from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
# from airflow.providers.sendgrid.operators.send_email import SendEmailOperator
from datetime import datetime, timedelta
from airflow.operators.email import EmailOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False,
)

# Початкова та кінцева задачі
start_task = DummyOperator(task_id='start_task', dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

def _get_message() -> str:
    return "Hi from forex_data_pipeline"
# Відправка листа за допомогою SendGrid


send_email_notification = EmailOperator(
    task_id="send_email_notification",
    to="spirit.jet@gmail.com",
    subject="forex_data_pipeline",
    html_content="<h3>forex_data_pipeline</h3>"
)
start_task >> send_email_notification >> end_task

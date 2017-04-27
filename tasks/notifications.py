import datetime

from django_cron import CronJobBase, Schedule

from .models import DB_Due, DB_Tasks, DB_User


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'notifications.MyCronJob'

    def do(self):
        check_to_notify()


def fire_safari(task):
    pass


def fire_email(task):
    pass


def fire_chrome(task):
    pass


def notify_all(task):
    print(task)
    fire_safari(task)
    fire_email(task)
    fire_chrome(task)


def check_to_notify():
    list_of_due = DB_Due.objects.all()
    for task in list_of_due:
        if task.due < datetime.datetime.now():
            notify_all(task)
            task.delete()

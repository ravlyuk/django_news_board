from django_cron import CronJobBase, Schedule
from .models import Comment


class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ["00:00"]
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = "bboard.my_cron_job"  # a unique code
    comments = Comment.objects.all()

    def do(self):
        for comment in self.comments:
            comment.likes = 0

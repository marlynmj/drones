from django_cron import CronJobBase, Schedule
from django.utils import timezone
from .models import Dron, Historial


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 #120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.cron'    # a unique code

    def do(self):
        ##pass    # do your thing here
        query = Dron.objects.all()
        dayTime = timezone.now()
        for i in range(len(query)):
            historial = Historial.objects.create(
                dron = query[i],
                batteryLevel = query[i].batteryCapacity,
                dayTime = dayTime
            )
            historial.save()
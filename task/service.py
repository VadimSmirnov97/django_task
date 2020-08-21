from .models import Task


def service(task_id, status):
    queryset = Task.objects.get(task_id=task_id)
    queryset.status = status
    queryset.save(force_update=True)

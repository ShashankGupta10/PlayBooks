from django.urls import path

from . import views as executor_views

urlpatterns = [
    path('task/run', executor_views.task_run),
    path('step/run', executor_views.step_run),

    # Playbooks CRUD
    path('get', executor_views.playbooks_get),
    path('create', executor_views.playbooks_create),
    path('update', executor_views.playbooks_update),
    path('execute', executor_views.playbooks_execute),
]

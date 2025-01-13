from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),

    path('modules', views.ModuleListView.as_view(), name='module_list'),
    path('modules/view/<slug:pk>', views.ModuleDetailView.as_view(), name='module_detail'),
    path('modules/add', views.ModuleCreateView.as_view(), name='module_create'),
    path('modules/del/<slug:pk>', views.ModuleDeleteView.as_view(), name='module_delete'),
    path('modules/put/<slug:pk>', views.ModuleUpdateView.as_view(), name='module_update'),

    path('schedules', views.ScheduleListView.as_view(), name='schedule_list'),
    path('schedules/view/<slug:pk>', views.ScheduleDetailView.as_view(), name='schedule_detail'),
    path('schedules/add', views.ScheduleCreateView.as_view(), name='schedule_create'),
    path('schedules/del/<slug:pk>', views.ScheduleDeleteView.as_view(), name='schedule_delete'),
    path('schedules/put/<slug:pk>', views.ScheduleUpdateView.as_view(), name='schedule_update'),

    path('import/modules', views.import_module_csv, name='module_import'),
    path('import/schedules', views.import_schedule_csv, name='schedule_import'),
    path('stats', views.get_stats),

]
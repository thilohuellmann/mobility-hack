from . import views
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    # general paths
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # senior specific paths begin
    path('senior/create_profile/', views.create_profile_senior, name='create_profile_senior'),
    path('senior/profile/', views.profile_senior, name='profile_senior'),
    path('senior/profile/success', views.profile_senior_success, name='profile_senior_success'),
    path('senior/my_trips/', views.my_trips_senior, name='my_trips_senior'),
    path('senior/trip/{id}/', views.trip_details_senior, name='trip_details_senior'), # ??? TODO
    path('senior/trip/create/step_1/', views.trip_create_1_senior, name='trip_create_1_senior'),
    path('senior/trip/create/step_2/', views.trip_create_2_senior, name='trip_create_2_senior'),
    path('senior/trip/create/step_3/', views.trip_create_3_senior, name='trip_create_3_senior'),
    path('senior/trip/create/step_4_1/', views.trip_create_4_1_senior, name='trip_create_4_1_senior'),
    path('senior/trip/create/step_4_2_1/', views.trip_create_4_2_1_senior, name='trip_create_4_2_1_senior'),
    path('senior/trip/create/step_4_2_2/', views.trip_create_4_2_2_senior, name='trip_create_4_2_2_senior'),
    path('senior/trip/create/step_5/', views.trip_create_5_senior, name='trip_create_5_senior'),
    path('senior/creation_confirmation/', views.trip_creation_confirmation_senior, name='trip_creation_confirmation_senior'),

    # supporter specific paths begin
    path('supporter/create_profile/', views.create_profile_supporter, name='create_profile_supporter'),
    path('supporter/profile/', views.profile_supporter, name='profile_supporter'),
    path('supporter/profile/success', views.profile_supporter_success, name='profile_supporter_success'),
    path('supporter/discover/', views.discover_trips_supporter, name='discover_trips_supporter'),
    path('supporter/my_trips/', views.my_trips_supporter, name='my_trips_supporter'),
    path('supporter/trip/{id}/', views.trip_details_supporter, name='trip_details_supporter'), # ??? TODO
    path('supporter/trip/{id}/application_confirmation', views.trip_application_confirmation_supporter, name='trip_application_confirmation_supporter'), # HttpResponseRedirect
]

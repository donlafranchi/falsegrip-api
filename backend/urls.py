from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from rest_framework_swagger.views import get_swagger_view
from rest_framework_extensions.routers import ExtendedDefaultRouter

from general.views import *
from accounts.views import *


admin.site.site_title = admin.site.index_title = "Humble Rings Administration"

router = ExtendedDefaultRouter()

router.register(r'users', UserViewSet, basename='users')

workout_routes = router.register(
    r'workouts',
    WorkoutViewSet,
    basename='workouts'
)

exercise_routes = router.register(
    r'exercises',
    ExerciseViewSet,
    basename='exercises',
)

set_routes = workout_routes.register(
    r'sets',
    SetViewSet,
    basename='sets',
    parents_query_lookups=["workout"]
)

schema_view = get_swagger_view(title='Humble Rings API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^auth/sign-up/', CustomRegisterView.as_view(), name='sign_up'),
    url(r'^auth/sign-in/', CustomLoginView.as_view(), name='sign_in'),
    path(r'swagger/', schema_view),
]

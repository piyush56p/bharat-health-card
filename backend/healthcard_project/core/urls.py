from urls import path
from .views import UserProfileListCreateView,HospitalListCreateView, DoctorListCreateView

urlpatterns = [
    path('users/', UserProfileListCreateView.as_view(), name='user-list-create'),
    path('hospitals/', HospitalListCreateView.as_view(), name='hospital-list-create'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
]

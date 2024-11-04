from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    #path('api/chart-data/', views.get_chart_data, name='get_chart_data'), 
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('tour/book/<int:tour_id>/', views.book_tour, name='book_tour'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('tour/<int:tour_id>/comment/', views.add_comment, name='add_comment'),

    path('tours/', views.tour_list, name='tour_list'),
    path('tourMap/', views.tour_map, name='tour_map'),
    path('tours/add/', views.tour_create, name='tour_create'),
    path('tours/edit/<int:pk>/', views.tour_edit, name='tour_edit'),
    path('tours/delete/<int:pk>/', views.tour_delete, name='tour_delete'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('booking/success/<int:tour_id>/', views.success, name='booking'),
    path('bookings/delete/<int:pk>/', views.booking_delete, name='booking_delete'),
    path('users/', views.user_list, name='user_list'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('tour/<int:tour_id>/payment/', views.payment_page, name='payment_page'),
    path('tour/<int:tour_id>/payment/complete/', views.complete_payment, name='complete_payment'),
    path('generate-excel-report/', views.generate_excel_report, name='generate_excel_report'),
    path('test-email/', views.test_email, name='test_email'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
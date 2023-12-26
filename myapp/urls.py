from django.urls import path
from .views import (
    home,
    svcs_list, create_svcs, update_svcs, delete_svcs,
    indl_list, create_indl,
    country_list,
    govt_order_list,
    course_list,
    course_offer_list,
    course_acceptance_list,
    visit_list,
    yearly_state_list,
)

urlpatterns = [
    path('', home, name='home'),

    # Svcs URLs
    path('svcs/', svcs_list, name='svcs_list'),
    path('svcs/create/', create_svcs, name='create_svcs'),
    path('svcs/update/<int:pk>/', update_svcs, name='update_svcs'),
    path('svcs/delete/<int:pk>/', delete_svcs, name='delete_svcs'),

    # Indl URLs
    path('indl/', indl_list, name='indl_list'),
    path('indl/create/', create_indl, name='create_indl'),

    # Country URLs
    path('countries/', country_list, name='country_list'),

    # GovtOrder URLs
    path('govt_orders/', govt_order_list, name='govt_order_list'),

    # Course URLs
    path('courses/', course_list, name='course_list'),

    # CourseOffer URLs
    path('course_offers/', course_offer_list, name='course_offer_list'),

    # CourseAcceptance URLs
    path('course_acceptances/', course_acceptance_list, name='course_acceptance_list'),

    # Visit URLs
    path('visits/', visit_list, name='visit_list'),

    # YearlyState URLs
    path('yearly_states/', yearly_state_list, name='yearly_state_list'),

    # Add other URL patterns for your other views
]

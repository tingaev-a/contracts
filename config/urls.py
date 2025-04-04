"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py основного приложения
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),

    # ContractType
    path('contracttype/', views.ContractTypeListView.as_view(), name='contracttype-list'),
    path('contracttype/<int:pk>/', views.ContractTypeDetailView.as_view(), name='contracttype-detail'),
    path('contracttype/create/', views.ContractTypeCreateView.as_view(), name='contracttype-create'),
    path('contracttype/<int:pk>/update/', views.ContractTypeUpdateView.as_view(), name='contracttype-update'),
    path('contracttype/<int:pk>/delete/', views.ContractTypeDeleteView.as_view(), name='contracttype-delete'),

    # Organization
    path('organization/', views.OrganizationListView.as_view(), name='organization-list'),
    path('organization/<int:pk>/', views.OrganizationDetailView.as_view(), name='organization-detail'),
    path('organization/create/', views.OrganizationCreateView.as_view(), name='organization-create'),
    path('organization/<int:pk>/update/', views.OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization/<int:pk>/delete/', views.OrganizationDeleteView.as_view(), name='organization-delete'),

    # Contract
    path('contract/', views.ContractListView.as_view(), name='contract-list'),
    path('contract/<int:pk>/', views.ContractDetailView.as_view(), name='contract-detail'),
    path('contract/create/', views.ContractCreateView.as_view(), name='contract-create'),
    path('contract/<int:pk>/update/', views.ContractUpdateView.as_view(), name='contract-update'),
    path('contract/<int:pk>/delete/', views.ContractDeleteView.as_view(), name='contract-delete'),
]
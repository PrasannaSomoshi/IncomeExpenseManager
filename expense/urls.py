from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('addUser', views.addUser),
    path('addIncome', views.addIncome),
    path('addExpense', views.addExpense),
    path('incomeList', views.incomeList),
    path('expenseList', views.expenseList),
    path('incomeDelete', views.incomeDelete),
    path('incomeEdit', views.incomeEdit),
    path('expenseDelete', views.expenseDelete),
    path('expenseEdit', views.expenseEdit),
    #path('flogin', views.flogin),
    path('login', views.loginv),
    path('logout', views.logoutv),
]

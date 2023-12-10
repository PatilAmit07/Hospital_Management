from django.urls import path
from .import views


urlpatterns=[
    path('',views.FirstPage ),
    path('LoginPage',views.LoginPage),
    path('Patientsdata',views.DataShow),
    path('SecondPage',views.SecondPage),
    path('delete/<int:id>',views.Delete),
    path('edit/<int:id>',views.Edit),
    path('update/<int:id>',views.Update),
    path('LoginPageNurse',views.LoginPageNurse),
    path('SecondPageNurse',views.SecondPageNurse),
    path('Patientsdatanurse',views.DataShowNurse),
    path('deletenurse/<int:id>',views.DeleteNurse),
    path('editnurse/<int:id>',views.EditNurse),
    path('updatenurse/<int:id>',views.UpdateNurse),
]
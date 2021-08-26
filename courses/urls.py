
from .views import (
    RescueScubaView,
    AdvancedScubaView,
    NitroxView,
    OpenWaterView,
    MasterScubaView,
    FirstAidCourseView,
    FullFaceView,
    PublicSafetyView,
    LionFishView,
    DiveMasterView,
    InstructorView,
    CrossOverView,
    TrainerView,
    AidInstructorView,
    DirectorView,
    IntroTechnicalView,
    MixedGasView,
    RebreatherView,
    OverheadView,
    DVPView
)
from django.urls import path

app_name="courses"

urlpatterns = [
    path('rescue/',RescueScubaView.as_view(), name="rescue"),
    path('advanced/',AdvancedScubaView.as_view(), name="advanced"),
    path('nitrox/',NitroxView.as_view(), name="nitrox"),
    path('open_water/',OpenWaterView.as_view(), name="open-water"),
    path('master_scuba/',MasterScubaView.as_view(), name="master-scuba"),
    path('first_aid_course/',FirstAidCourseView.as_view(), name="aid-course"),
    path('full-face/',FullFaceView.as_view(), name="full-face"),
    path('public-safety/',PublicSafetyView.as_view(), name="public-safety"),
    path('hunter/',LionFishView.as_view(), name="hunter"),
    path('divemaster/',DiveMasterView.as_view(), name="divemaster"),
    path('instructor/',InstructorView.as_view(), name="instructor"),
    path('instructor_crossover/',CrossOverView.as_view(), name="instructor-crossover"),
    path('instructor_trainer/',TrainerView.as_view(), name="instructor-trainer"),
    path('fa_intstructor/',AidInstructorView.as_view(), name="fa-instructor"),
    path('course_director/',DirectorView.as_view(), name="director"),
    path('intro_tech/',IntroTechnicalView.as_view(), name="intro-tech"),
    path('mixed_gas/',MixedGasView.as_view(), name="mixed-gas"),
    path('rebreather/',RebreatherView.as_view(), name="rebreather"),
    path('overhead/',OverheadView.as_view(), name="overhead"),
    path('DVP/',DVPView.as_view(), name="DVP"),


    


    
]
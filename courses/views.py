from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RescueScubaView(TemplateView):
    template_name="courses/rescue.html"

class AdvancedScubaView(TemplateView):
    template_name="courses/advanced.html"

class NitroxView(TemplateView):
    template_name="courses/nitrox.html"


class OpenWaterView(TemplateView):
    template_name="courses/certified_scuba.html"

class MasterScubaView(TemplateView):
    template_name="courses/master_scuba.html"


class FirstAidCourseView(TemplateView):
    template_name="courses/first_aid_course.html"

class FullFaceView(TemplateView):
    template_name="courses/full_mask.html"

class PublicSafetyView(TemplateView):
    template_name="courses/public_safety.html"

class LionFishView(TemplateView):
    template_name="courses/hunter.html"

class DiveMasterView(TemplateView):
    template_name="courses/divemaster.html"

class InstructorView(TemplateView):
    template_name="courses/instructor.html"

class CrossOverView(TemplateView):
    template_name="courses/crossover.html"

class TrainerView(TemplateView):
    template_name="courses/trainer.html"

class AidInstructorView(TemplateView):
    template_name="courses/aid_instructor.html"

class DirectorView(TemplateView):
    template_name="courses/director.html"

class IntroTechnicalView(TemplateView):
    template_name="courses/intro_tech.html"

class MixedGasView(TemplateView):
    template_name="courses/mixed_gas.html"

class RebreatherView(TemplateView):
    template_name="courses/rebreather.html"

class OverheadView(TemplateView):
    template_name="courses/overhead.html"

class DVPView(TemplateView):
    template_name="courses/dvp.html"


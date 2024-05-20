from django.urls import path
from .views import AssessmentView



urlpatterns = [
    path(
        "assessment/",
        AssessmentView.as_view(template_name="assessment_form.html"),
        name="assessment-form",
    )
]

from django.views.generic.edit import FormView
from .forms import ReviewForm

class ReviewFormView(FormView):
    form_class = ReviewForm
    template_name = 'review.html'

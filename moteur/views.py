from django.shortcuts import render

def index(request):
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]
	return render(request, 'moteur/index.html')

# TODO: api endpoint

from django.shortcuts import render, redirect 
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from . models import Journal 
from . forms import JournalForm

# Create your views here.

def create_journal(request):
    if request.method == "POST":
        form = JournalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listjournals')
    
    form = JournalForm()
    context = {
        'form':form 
    }
    return render(request, 'journal/create.html',context)

class JournalList(ListView):
    model = Journal
    context_object_name = 'journals'
    template_name='journal/listall.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Journal.objects.filter(favourite=True).count()
        return context


def listjournals(request):
    all = Journal.objects.all()
    context = {
        'journals': all
    }
    return render(request, 'journal/listjournals.html',context)

def search(request):
    if request.method == "POST":
        query = request.POST.get('journal', None)
        if query:
            results = Journal.objects.filter(title__contains=query)
            return render(request, 'journal/search.html',{'results':results})
    
    return render(request, 'journal/search.html')

def delete(request, id):
    obj = get_object_or_404(Journal,id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('listjournals')
    context = {
        'object':obj

    }
    return render(request, 'journal/delete.html',context)

    

def update(request, id):
    obj = get_object_or_404(Journal, id=id)
    form = JournalForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('listjournals')
    context = {
        'form':form
    }
    return render(request, 'journal/update.html',context)



def journal_detail(request, id):
    journal = Journal.objects.get(id=id)
    context = {
        'journal':journal
    }
    return render(request, 'journal/journal_detail.html', context)

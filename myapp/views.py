from django.shortcuts import render, get_object_or_404, redirect
from .models import Svcs, Indl, Country, GovtOrder, Course, CourseOffer, CourseAcceptance, Visit, YearlyState, Sections
from .forms import SvcsForm, IndlForm, CountryForm, GovtOrderForm, CourseForm, CourseOfferForm, CourseAcceptanceForm, VisitForm, YearlyStateForm

def home(request):
    if request.method == 'POST':
        entered_password = request.POST.get('password')
        correct_password = "998877113355"

        if entered_password == correct_password:
            return redirect('section')

        else:
            return render(request, 'home.html', {'message': 'Incorrect password. Please try again.'})

    return render(request, 'home.html')

# Views for Svcs model

def sections(request):
    Section_list = Sections.objects.all()
    return render(request, 'sections.html', {'Section_list': Section_list})



def section_detail(request, section_id):
    section = get_object_or_404(Sections, id=section_id)
    template_name = f"{section.template_name}.html"
    return render(request, template_name, {'section': section})


def create_svcs(request):
    if request.method == 'POST':
        form = SvcsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('svcs_list')
    else:
        form = SvcsForm()

    return render(request, 'svcs_form.html', {'form': form})

def update_svcs(request, pk):
    svcs = get_object_or_404(Svcs, pk=pk)
    if request.method == 'POST':
        form = SvcsForm(request.POST, instance=svcs)
        if form.is_valid():
            form.save()
            return redirect('svcs_list')
    else:
        form = SvcsForm(instance=svcs)

    return render(request, 'svcs_form.html', {'form': form})

def delete_svcs(request, pk):
    svcs = get_object_or_404(Svcs, pk=pk)
    svcs.delete()
    return redirect('svcs_list')

# Repeat the above pattern for other models

# Views for Indl model

def indl_list(request):
    indl_list = Indl.objects.all()
    return render(request, 'indl_list.html', {'indl_list': indl_list})

def create_indl(request):
    if request.method == 'POST':
        form = IndlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indl_list')
    else:
        form = IndlForm()

    return render(request, 'indl_form.html', {'form': form})

# Repeat the pattern for other models...

# Views for Country model

# ... (Repeat the pattern)

# Views for GovtOrder model
def govt_order_list(request):
    govt_orders = GovtOrder.objects.all()
    context = {'govt_orders': govt_orders}
    return render(request, 'govt_order_list.html', context)

def country_list(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'country_list.html', context)

def course_list(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'course_list.html', context)

def course_offer_list(request):
    course_offers = CourseOffer.objects.all()
    context = {'course_offers': course_offers}
    return render(request, 'course_offer_list.html', context)

def course_acceptance_list(request):
    course_acceptances = CourseAcceptance.objects.all()
    context = {'course_acceptances': course_acceptances}
    return render(request, 'course_acceptance_list.html', context)

def visit_list(request):
    visits = Visit.objects.all()
    context = {'visits': visits}
    return render(request, 'visit_list.html', context)

def yearly_state_list(request):
    yearly_states = YearlyState.objects.all()
    context = {'yearly_states': yearly_states}
    return render(request, 'yearly_state_list.html', context)
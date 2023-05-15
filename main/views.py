from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ConditionForm, EqualityForm, MonotoneForm, SelfDualityForm, SheffForm
from algorithms import huffman_coder, hamming_coder, TDNF_coder, equality_coder, monotone_coder, get_vector, \
    self_duality_coder, sheff_coder


def index(request):
    return render(request, "index.html")


def encode(request):
    return render(request, "encode.html")


# def huffman(request):
#     return render(request, "huffman.html")


def hamming(request):
    return render(request, "hamming.html")


# def get_condition(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = ConditionForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ConditionForm()
#
#     return render(request, "huffman.html", {'form': form})

def to_list(cond: str) -> list:
    numbers = cond.split(' ')
    map_cond = map(str, numbers)
    numbers = list(map_cond)
    return numbers


class HuffmanView(generic.FormView):
    template_name = 'huffman.html'
    form_class = ConditionForm
    success_url = '/huffman/'
    huffman_context = dict()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['huffman_context'] = self.huffman_context
        return context

    def form_valid(self, form):
        condition = form.data.get('condition')
        if condition:
            self.huffman_context['result'] = do_huffman(condition)
        return super().form_valid(form)


class HammingView(generic.FormView):
    template_name = 'hamming.html'
    form_class = ConditionForm
    success_url = '/hamming/'
    hamming_context = dict()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hamming_context'] = self.hamming_context
        return context

    def form_valid(self, form):
        condition = form.data.get('condition')
        if condition:
            self.hamming_context['condition'] = condition
            self.hamming_context['result'] = do_hamming(condition)
        return super().form_valid(form)


def do_huffman(cond: str):
    numbers = to_list(cond.strip())
    result = huffman_coder.get_huffman_result(numbers)
    return result


def do_hamming(cond: str):
    result = hamming_coder.get_hamming_result(cond.strip())
    return result


def logic(request):
    return render(request, "logic.html")


class TDNFView(generic.FormView):
    template_name = 'TDNF.html'
    form_class = ConditionForm
    success_url = '/TDNF/'
    TDNF_context = dict()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TDNF_context'] = self.TDNF_context
        return context

    def form_valid(self, form):
        condition = form.data.get('condition')
        if condition:
            self.TDNF_context['condition'] = condition
            self.TDNF_context['result'] = do_TDNF(condition)
        return super().form_valid(form)


def do_TDNF(cond: str):
    result = str(TDNF_coder.get_TDNF_result(cond.strip()))
    return result


def solve_equality(first_condition: str, second_condition: str):
    return equality_coder.check_equivalence(first_condition, second_condition)


def equality(request):
    first_expression = ''
    second_expression = ''

    result = ''
    if request.method == 'POST':
        form = EqualityForm(request.POST)
        if form.is_valid():
            first_expression = form.data.get('firstCondition')
            second_expression = form.data.get('secondCondition')
            result = solve_equality(first_expression, second_expression)
            print(result)

    return render(request, 'equality.html', {'result': result,
                                             'first_expression': first_expression,
                                             'second_expression': second_expression})


def solve_monotone(condition: str):
    vector = get_vector.dnf_vector(condition)
    return monotone_coder.is_monotonic(vector)


def monotone(request):
    result = ''
    condition = ''

    if request.method == 'POST':
        form = MonotoneForm(request.POST)
        if form.is_valid():
            condition = form.data.get('condition')
            result = solve_monotone(condition)

    return render(request, 'monotone.html', {'result': result, 'condition': condition})


def solve_self_duality(condition: str):
    vector = get_vector.dnf_vector(condition)

    return sheff_coder.is_sheffer_function(vector)


def self_duality(request):
    result = ''
    condition = ''

    if request.method == 'POST':
        form = (request.POST)
        if form.is_valid():
            condition = form.data.get('condition')
            result = solve_self_duality(condition)

    return render(request, 'self_duality.html', {'result': result, 'condition': condition})


def solve_sheff(condition: str):
    vector = get_vector.dnf_vector(condition)

    return sheff_coder.is_sheffer_function(vector)


def sheff(request):
    result = ''
    condition = ''

    if request.method == 'POST':
        form = SheffForm(request.POST)
        if form.is_valid():
            condition = form.data.get('condition')
            result = solve_sheff(condition)

    return render(request, 'sheff.html', {'result': result, 'condition': condition})

from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.timezone import now

from demoapp.models import Colors
from djgentelella.forms.forms import CustomForm
from djgentelella.widgets.color import StyleColorInput, DefaultColorInput, HorizontalBarColorInput, VerticalBarColorInput, InlinePickerColor

class ExampleTwoForm(CustomForm, forms.ModelForm):
    color = forms.CharField(widget=DefaultColorInput(attrs={"value": "#0014bb", "id": "c1"}))
    color2 = forms.CharField(widget=StyleColorInput(attrs={"value": "#0014bb", "id": "c2"}))
    color3 = forms.CharField(widget=HorizontalBarColorInput(attrs={"value": "#0014bb", "id": "c3"}))
    color4 = forms.CharField(widget=VerticalBarColorInput(attrs={"value": "#0014bb", "id": "c4"}))
    class Meta:
        model = Colors
        fields = "__all__"

class ExampleForm(CustomForm):

    """  """
   #  your_name = forms.CharField(label='Your name', max_length=100, widget=genwidgets.TextInput)
   #
   #  your_age = forms.IntegerField(widget=genwidgets.NumberInput(attrs={'min_value':2, 'max_value': 8}) )
   #  your_email = forms.EmailField(widget=genwidgets.EmailInput)
   #  your_url = forms.URLField(widget=genwidgets.URLInput)
   #  your_pass = forms.CharField(widget=genwidgets.PasswordInput)
   #
   #  #your_file = forms.FileField(widget=genwidgets.FileInput)
   #  your_area = forms.CharField(widget=genwidgets.Textarea, max_length = 50)
   #  your_date = forms.DateField(widget=genwidgets.DateInput)
   #  your_datetime = forms.DateTimeField(widget=genwidgets.DateTimeInput)
   #  your_daterange = forms.CharField(widget=genwidgets.DateRangeInput)
   #
   #
   # # your_time = forms.TimeField(widget=genwidgets.TimeInput(attrs={'arrow': True}))
   #  your_check = forms.BooleanField(widget=genwidgets.CheckboxInput)
   #
   #
   #  your_nullboolean = forms.NullBooleanField(widget=genwidgets.NullBooleanSelect)
   #
   #  your_choice = forms.ChoiceField(choices=(
   #      ('enero', 'Enero'),
   #      ('febrero', 'Febrero'),
   #      ('marzo', 'abril')
   #  ), widget=genwidgets.Select)
   #
   #  your_test = forms.ChoiceField(choices=(
   #      ('enero', 'Enero'),
   #      ('febrero', 'Febrero'),
   #      ('marzo,abril', 'Marzo,Abril')
   #  ), widget=genwidgets.Select)
   #
   #  your_multiple = forms.ChoiceField(choices=(
   #      ('enero', 'Enero'),
   #      ('febrero', 'Febrero'),
   #      ('marzo,abril', 'Marzo,Abril')
   #  ), widget=genwidgets.SelectMultiple)
   #
   #  your_radio = forms.ChoiceField(choices=(
   #      ('enero', 'Enero'),
   #      ('febrero', 'Febrero'),
   #      ('marzo,abril', 'Marzo,Abril')
   #  ), widget=genwidgets.RadioSelect)
   #
   #  your_checkbox = forms.ChoiceField(choices=(
   #      ('enero', 'Enero'),
   #      ('febrero', 'Febrero'),
   #      ('marzo,abril', 'Marzo,Abril')
   #  ), widget=genwidgets.CheckboxSelectMultiple)
   #
   #  #your_date = forms.DateField(widget=DateInput)
   #  #your_hiddendatime=forms.DateTimeField(widget=SplitHiddenDateTimeWidget)
   #  #your_SplitDateTimeWidget = forms.DateTimeField(widget=SplitDateTimeWidget)
   #
   #  your_selectdate = forms.DateTimeField(widget=genwidgets.SelectDateWidget)
   #
   #  def __init__(self, *args, **kwargs):
   #      kwargs['initial'] = {'your_name': "BINGO", 'your_age': 4,
   #                           'your_SplitDateTimeWidget': now(),
   #                           'your_selectdate': now(),
   #                           'your_time': now(), 'your_nullboolean': True}
   #
   #      super().__init__(*args, **kwargs)

    # your_phone = forms.CharField(widget=genwidgets.PhoneNumberMaskInput)
    # your_boolean = forms.BooleanField(widget=genwidgets.YesNoInput)
    # your_datemask = forms.DateField(widget=genwidgets.DateMaskInput)
    # your_datetimeMask  = forms.DateTimeField(widget=genwidgets.DateTimeMaskInput)
    # you_emailmask = forms.EmailField(widget=genwidgets.EmailMaskInput)

    #your_daterangeinput = forms.CharField(widget=genwidgets.DateRangeInput)
    # your_knobinput = forms.IntegerField(widget=genwidgets.NumberKnobInput(
    #    attrs={ 'max_value':300, 'min_value': 200,
    #            'data-width': 100, 'data-height': 100,
    #            'data-displayPrevious': "true",
    #            'data-fgColor': "#26B99A",
    #            'data-cursor': "true",
    #            'data-thickness': '.3'
    #            } ))
    #
    # your_test = forms.ChoiceField(choices=(
    #     ('enero', 'Enero'),
    #     ('febrero', 'Febrero'),
    #     ('marzo,abril', 'Marzo,Abril')
    # ), widget=genwidgets.SelectMultipleAdd(
    #     attrs={'add_url': reverse_lazy('add_view_select')}
    # ))
    #
    # your_multiple = forms.ChoiceField(choices=(), widget=genwidgets.SelectWithAdd(
    #     attrs={'add_url': reverse_lazy('add_view_select')}))

    #your_wysiwyg = forms.CharField(widget=genwidgets.TextareaWysiwyg)
    default_input = forms.CharField(
        widget=DefaultColorInput(attrs={"value": "#0014bb"})
    )
    style_input = forms.CharField(
        widget=StyleColorInput(attrs={"value": "#0014bb"})
    )
    horizontal_bar_input = forms.CharField(
         widget=HorizontalBarColorInput(attrs={"value": "#0014bb"})
    )
    vertical_bar_input = forms.CharField(
         widget=VerticalBarColorInput(attrs={"value": "#0014bb"})
    )
    inline_picker = forms.CharField(
         widget=InlinePickerColor(attrs={"value": "#0014bb"})
    )
    # text_6 = forms.CharField(
    #     widget=ColorInput
    # )
    # text_7 = forms.CharField(
    #     widget=ColorInput
    # )

def other_place(request):
    form = ExampleForm()
    form_form = ExampleTwoForm()
    if request.method == 'POST':
        form_form = ExampleTwoForm(request.POST)
        form_form.is_valid()
        form_form.save()
    return render(request, 'index-color.html', {'form': form, "form_form": form_form})

def home(request):
    form = ExampleForm()
    if request.method == 'POST':
        form  = ExampleForm(request.POST)
        form.is_valid()
    return render(request, 'gentelella/index.html', {'form': form})


@login_required
def logeado(request):
    return HttpResponse("Wiii")


def add_view_select(request):
    if request.method == 'POST':
        return JsonResponse({'ok': True, 'id': 2, 'text': 'Data example'})
        return JsonResponse({'ok': False,
                             'title': "Esto no dice nada",
                             'message': 'Esto es un errror'})
    data = {
        'ok':  True,
        'title': 'Formulario de ejemplo',
        'message': """
        <form method="post" action="/add_view_select">
            <textarea name="description" > </textarea>
            <input type="text" name="name" />
            <select name="bingo">
               <option value="Nada">Nada</option><option value="otro">Otro</option>
            </select>
        </form>
        """
    }
    return JsonResponse(data)
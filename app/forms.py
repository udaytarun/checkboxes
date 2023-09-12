from django import forms


g=[('male','MALE'),('female','FEMALE')]

C=[('python','PYTHON'),('java','JAVA'),('django','DJANGO')]

class Registrationform(forms.Form):
    Name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password=forms.CharField(max_length=10,widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    Course=forms.MultipleChoiceField(choices=C,widget=forms.CheckboxSelectMultiple)
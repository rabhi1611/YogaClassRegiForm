from django.forms import ModelForm

from . import models


class create_yogaRegi_form(ModelForm):
    
    class Meta:
        model = models.Student
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(create_yogaRegi_form, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Your full name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email     address'
        self.fields['age'].widget.attrs['placeholder'] = 'Your age'




    def clean(self):
 
        # data from the form is fetched using super function
        super(create_yogaRegi_form, self).clean()
         
        # extract the username and text field from the data
        username = self.cleaned_data.get('name')
        age = self.cleaned_data.get('age')
        email = self.cleaned_data.get('email')
    


        # conditions to be met for the username length

        def fun1(username):
            if username is None:
                return 1
            for x in username:
                if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z') or (x == ' '):
                    continue
                else:
                    return 1
            return 0


        def fun2(age):
            if age >= 18 and age <= 65:
              return 0
            return 1


        def fun3(email):
            if email is None:
                return 1
            idx = len(email) - 9
            if email[idx] != 'g':
                return 1
            if(email[idx + 1] != 'm'):
                return 1
            if(email[idx + 2] != 'a'):
                return 1
            if(email[idx + 3] != 'i'):
                return 1
            if(email[idx + 4] != 'l'):
                return 1

            return 0 


        if username is not None and len(username) < 8:
            self._errors['name'] = self.error_class([
                'Minimum 8 characters required'])
        elif (fun1(username)):
            self._errors['name'] = self.error_class([
                'Characters should be uppercase, lowercase or whitespaces.'])


        
        
        if (fun2(age)):
            self._errors['age'] = self.error_class([
                'Age should be between 18 and 65. If your age is not between these constraints, sorry you are not allowed for this yoga class.'])


        if(email is not None and len(email) < 11):
            self._errors['email'] = self.error_class([
                'Email should be of atleast 11 characters.'])

        elif(fun3(email)):
            self._errors['email'] = self.error_class([
                'Last 9 characters should be gmail.com.'])

        

        # return any errors if found
        return self.cleaned_data
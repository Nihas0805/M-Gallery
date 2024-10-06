from django import forms

class MovieForm(forms.Form):

     title=forms.CharField()

     options=(
        ("Action","Action"),
        ("Fiction","Fiction"),
         ("Drama","Drama"),
         ("Comedy","Comedy"),
     )

     genre=forms.ChoiceField(choices=options)

     language=forms.CharField()

     year=forms.CharField()

     run_time=forms.IntegerField()

     director=forms.CharField()


     def clean(self):

        cleaned_data=super().clean()

        year=cleaned_data.get("year")

        run_time=cleaned_data.get("run_time")

        if int(year)<1900:

            error_message="year should be greater than 1900"

            self.add_error("year",error_message)

        if run_time<60 or run_time>210:

            error_mess="run time should be between 60 and 210 minutes"
            
            self.add_error("run_time",error_mess)


        
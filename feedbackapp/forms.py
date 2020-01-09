from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating=forms.IntegerField(
        label='Type Your Rating:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback=forms.CharField(
        label='Type Your Feedback:',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )
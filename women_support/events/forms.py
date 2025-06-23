class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'requirements': forms.Textarea(attrs={'rows': 4, 'placeholder': 'One per line'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'mission': forms.Textarea(attrs={'rows': 4}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

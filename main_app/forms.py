import requests
from django import forms
from django.core.files.base import ContentFile

from main_app.models import Image


class ImageForm(forms.ModelForm):

    def clean(self):
        image = self.cleaned_data['image']
        url = self.cleaned_data['url']
        if not url and image is None:
            raise forms.ValidationError('Заполните одно из полей')
        elif not url:
            return self.cleaned_data
        elif url and image:
            raise forms.ValidationError('Заполните только одно из полей')
        elif url:
            response = requests.get(url)
            if response.status_code != 200:
                raise forms.ValidationError('Неверная ссылка')
        return self.cleaned_data

    def save(self, force_insert=False, force_update=False, commit=True):
        if not self.cleaned_data['image']:
            image = super(ImageForm, self).save(commit=False)
            image_url = self.cleaned_data['url']
            image_name = image_url.split("/")[-1]
            if self.cleaned_data['url']:
                response = requests.get(image_url)
                if response.status_code == 200:
                    image.image.save(image_name, ContentFile(response.content), save=False)
                    image.custom_image.save(image_name, ContentFile(response.content), save=False)
                    image.name = image_name
                    if commit:
                        image.save()
                    return image
        image = self.cleaned_data['image']
        self.instance.custom_image.save(image.name, image)
        self.instance.name = image.name
        super().save()

    class Meta:
        model = Image
        fields = ('url', 'image')


class ResizeImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('width', 'height')

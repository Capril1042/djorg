from django import forms
from . models import Bookmark

class BookmarkForm(forms.ModelForm):
    """form to create bookmarks"""

    class Meta:
        model = Bookmark
        fields= ('url', 'name', 'notes')
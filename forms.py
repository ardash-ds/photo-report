from pydantic import BaseModel

from .models import CATEGORY_PHOTO


class FormPhoto(BaseModel):
    cat1: str
    cat2: int


# delivery_from_city= forms.ChoiceField(widget=forms.RadioSelect, initial='DW', choices=DELIVERI_FROM_CITY)
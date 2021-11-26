from django.views import View
from django.shortcuts import get_object_or_404


class ModelBaseView(View):
    model = None

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None

        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj
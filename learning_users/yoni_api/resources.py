from tastypie.resources import ModelResource
from yoni_api.models import yoni_class
from tastypie.authorization import Authorization

class yoni_classResource(ModelResource):
    class Meta:
        queryset = yoni_class.objects.all()
        resource_name = 'attempt'
        authorization = Authorization()

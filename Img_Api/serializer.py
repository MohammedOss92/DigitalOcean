from rest_framework import serializers
from Img_Api.models import * 

class ImgsTypesSerializer (serializers.ModelSerializer):
    class Meta:
        model = ImageType
        fields = '__all__'


#class ImgsSerializer (serializers.ModelSerializer):
#    class Meta:
#        model = Images
#        fields = '__all__'



from ..models import Team
from ..serializers import TeamSerializer


class TeamService(object):

    response_model = {'result': None, 'has_error': False, 'errors': None}

    def custom_method():
        return Team.objects.all()

    def custom_method_two(self, model):
        serializer_class = TeamSerializer(data=model)
        if not serializer_class.is_valid():
            self.response_model['has_error'] = True
            self.response_model['errors'] = serializer_class.errors['Name']
            return self.response_model
        self.response_model['result'] = serializer_class.save()

        return self.response_model

    def delete_range(self, pk):
        t = Team.objects.filter(id__gt=pk)
        # t = Team.objects.in_bulk(range(pk))
        result = t.delete()
        print(result)
        self.response_model['result'] = "Ok"
        return self.response_model

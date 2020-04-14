from ..models import Profile


class GameService(object):

    def compute_user_points(user1_id, user2_id, user1_score,
                            user2_score):
        user1 = Profile.objects.get(pk=user1_id)
        user2 = Profile.objects.get(pk=user2_id)
        if(user1_score < user2_score and user1.points > user2.points):
            user2.points = user2.points + 3
            user1.points = user1.points - 3
            user2.save()
            user1.save()
        if(user2_score < user1_score and user2.points > user1.points):
            user1.points = user1.points + 3
            user2.points = user2.points - 3
            user2.save()
            user1.save()

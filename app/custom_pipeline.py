from social.pipeline import * 

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        user_profile = user.get_profile()
        if user_profile is None:
            user_profile = UserProfile(user_id=user.id)
        user_profile.facebook_access_token = response.get('access_token')
        user_profile.locale = response.get('locale')
        user_profile.gender = response.get('gender')
        user_profile.email = response.get('email')
        user_profile.facebook_link = response.get('facebook_link')
        user_profile.facebook_id = response.get('facebook_id')
        user_profile.save()

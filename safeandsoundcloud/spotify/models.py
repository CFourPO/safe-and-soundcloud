from django.db import models


class SpotifyUser(models.Model):

    birthdate = models.DateTimeField()
    country = models.CharField()
    display_name = models.CharField()
    email_string = models.EmailField()
    external_urls = models.URLField()
    followers = models.ManyToManyField()

# birthdate	The user’s date-of-birth. This field is only available when the current user has granted access to the user-read-birthdate scope.
# country	string	The country of the user, as set in the user’s account profile. An ISO 3166-1 alpha-2 country code. This field is only available when the current user has granted access to the user-read-private scope.
# display_name	string	The name displayed on the user’s profile. null if not available.
# email	string	The user’s email address, as entered by the user when creating their account. Important! This email address is unverified; there is no proof that it actually belongs to the user. This field is only available when the current user has granted access to the user-read-email scope.
# external_urls	an external URL object	Known external URLs for this user.
# followers	A followers object	Information about the followers of the user.
# href	string	A link to the Web API endpoint for this user.
# id	string	The Spotify user ID for the user.
# images	an array of image objects	The user’s profile image.
# product	string	The user’s Spotify subscription level: “premium”, “free”, etc. (The subscription level “open” can be considered the same as “free”.) This field is only available when the current user has granted access to the user-read-private scope.
# type	string	The object type: “user”
# uri	string	The Spotify URI for the user.
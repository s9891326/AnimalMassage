import os


def env(key, default=None):
    try:
        return os.environ.get(key, default)
    except KeyError:
        raise KeyError(
            'Environment variable {key} required.'.format(key=key)
        )


# SOCIAL_GOOGLE_CLIENT_ID = env("CLIENT_ID")
SOCIAL_GOOGLE_CLIENT_ID = "839807472831-i80bj1oq5fi6kv46gqflk9sr24njn4u1.apps.googleusercontent.com"

from enum import Enum

import requests
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token
from pydantic import BaseModel

from animal_massage.settings import SOCIAL_GOOGLE_CLIENT_ID


class LoginTypeEnum(str, Enum):
    Google = "Google"
    Facebook = "Facebook"


class LoginInput(BaseModel):
    type: LoginTypeEnum
    token: str


class LoginService:
    def __init__(self, login_param: LoginInput):
        self.login_param = login_param

    def login(self):
        id_info = ""
        if self.login_param.type == LoginTypeEnum.Google:
            try:
                id_info = id_token.verify_oauth2_token(self.login_param.token, google_requests.Request(),
                                                       SOCIAL_GOOGLE_CLIENT_ID)
            except Exception as e:
                raise e

            if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            if id_info['aud'] not in [SOCIAL_GOOGLE_CLIENT_ID]:
                raise ValueError('Could not verify audience.')

            # Todo: save to db
        elif self.login_param.type == LoginTypeEnum.Facebook:
            # https://github.com/twtrubiks/Flask-Login-example
            # https://developers.facebook.com/apps/1001993363887699/fb-login/settings/
            try:
                data = requests.post(
                    f"https://graph.facebook.com/me?fields=name,email&access_token={self.login_param.token}")
                if data.status_code == 200:
                    # todo: save to db
                    id_info = data.json()
            except Exception as e:
                raise e
        else:
            raise ValueError("Can not handle")

        return id_info

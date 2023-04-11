import unittest

from fastapi.testclient import TestClient

from app import app

# class LoginApiTests(unittest.TestCase):
#     def setUp(self) -> None:
#         self.t: TestClient = TestClient(app)
#
#     def tearDown(self) -> None:
#         self.t.close()
#
#     def test_google_login(self):
#         test_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjFhYWU4ZDdjOTIwNThiNWVlYTQ1Njg5NWJmODkwODQ1NzFlMzA2ZjMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiODM5ODA3NDcyODMxLWk4MGJqMW9xNWZpNmt2NDZncWZsazlzcjI0bmpuNHUxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiODM5ODA3NDcyODMxLWk4MGJqMW9xNWZpNmt2NDZncWZsazlzcjI0bmpuNHUxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTA2NDg4MDcwNzI2NTkwNDU0MTIzIiwiZW1haWwiOiJlZGR5MTUyMDFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJzMjBkTUUwS0VBQ2JRQkVKWlFJOGp3IiwibmFtZSI6IueOi-W9pea3hyIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BR05teXhhQmgwbnlWMzBOQ1QtMnVpcDBpWi1kRERXNm51T1hQc2VFSlRieD1zOTYtYyIsImdpdmVuX25hbWUiOiLlvaXmt4ciLCJmYW1pbHlfbmFtZSI6IueOiyIsImxvY2FsZSI6InpoLVRXIiwiaWF0IjoxNjc5OTA3NTY2LCJleHAiOjE2Nzk5MTExNjYsImp0aSI6IjZhMzU0NjM3NzA5NWIyNDdjMGExOGE5YjQ3NGZmZGMyZTliY2EzN2MifQ.scsVi5xLVwrAugdvaR7aexUcnjniGIVYqAyblSb3YeQjWcoFfKjO6MmnKA6kyVGnrG6okr-gZ-WYOQ2Mlr5lEUF2665barzm0vUwdPIRQd0BUr3ISehuMvgFkNlynhrgG34nI_CswXeENrUY_UYuTiu7kVtJ-R5P9SGy4mfmcbGTVN_jGs4lJTvY8c2NEGYPHJb89nwPO7JF_DWgeacdJ05_RW4TqDTVy7dJWkdX9U0Jvi49POYBoolH3VytF8jttUVu7p6Tmpe6gDDksfjZSrz9rCQIEM3Yj6WoCV1KUgYLFCFHnFVc8hFeytdMTv6sRomJjp6vgxsCoIA7FdOhow"
#         dto = self.t.post(
#             "/login", json=dict(type="Google", token=test_token)
#         ).json()
#         self.assertEqual("accounts.google.com", dto["iss"])
#         print(dto)
#
#     def test_fb_login(self):
#         test_token = "EAAOPTsKFllMBADPvMeFX6KFnbibvOkzyuHMl3lZCsOWsZAJUO53mWmOMUXUwahiQvZAiq0hlwwcTSBmxoIykiPwBJJYGZCACnnGNFRh6U31YG5hywgFQZBWYmUwZBq5uZC7cTwSkgBl8kIHe6eJXgjR9MgjMLCfI0PWdSMUDEcYrXVPG8V2o5jn3wi0XbhIxd1MWPY4YaUr1ixBhoo5DPpNwxiZBFCH2kDoZD"
#         dto = self.t.post(
#             "/login", json=dict(type="Facebook", token=test_token)
#         ).json()
#
#         fields = ["name", "email", "id"]
#         for field in fields:
#             self.assertTrue(field in dto)
#         print(dto)


# DB_HOST=192.168.223.127;DB_NAME=animal_massage;DB_PASSWORD=postgres;DB_USER=postgres;DB_PORT=5432


# class UserApiTests(unittest.TestCase):
#     def setUp(self) -> None:
#         self.t: TestClient = TestClient(app)
#
#     def tearDown(self) -> None:
#         self.t.close()
#
#     def test_1_create_user(self):
#         # dto = self.t.post("/user")
#         dto = self.t.get("/user?user_id=1").json()
#         print(dto)

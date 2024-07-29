from test_plus.test import TestCase
from django_private_chat.utils import *


class TestUtilsFunctions(TestCase):
    def setUp(self):
        self.user1 = self.make_user(username="user1")
        self.user2 = self.make_user(username="user2")

    def test_get_dialogs_with_user(self):
        self.dialog = Dialog()
        self.dialog.owner = self.user2
        self.dialog.opponent = self.user1
        self.dialog.save()
        dialog = get_dialogs_with_user(self.user1, self.user2)[0]
        self.assertEqual(dialog, self.dialog)

    async def test_get_user_from_session(self):
        await Session.objects.acreate(
            session_key="bla",
            session_data=Session.get_session_store_class()().encode(
                session_dict={"_auth_user_id": 1}),
            expire_date="2030-09-01 00:00:00Z")

        user = await get_user_from_session("bla")
        self.assertEqual(user, self.user1)

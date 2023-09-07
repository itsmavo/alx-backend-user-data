#!/usr/bin/env python3
""" Defines class SessionDBAuth """
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ Class persists session data in a database """

    def create_session(self, user_id=None):
        """
        Creates session_id from user_id
        Args:
            user_id (str)
        """
        if not session_id:
            return None
        kw = {
            "user_id": user_id,
            "session_id": session_id
        }
        user = UserSession(**kw)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns user_id on session_id
        Args:
            session_id (str)
        Return:
            user_id (str) or None
        """
        user_id = UserSession.search({"session_id": session_id})
        if user_id:
            return user_id
        return None


    def destroy_session(self, request=None):
        """Destroy UserSession instance based on session_id from a cookie"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_session = UserSession.search({"session_id": session_id})
        if user_session:
            user_session[0].remove()
            return True
        return False

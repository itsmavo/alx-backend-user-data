#!/usr/bin/env python3
""" Definition class SessionAuth """
import base64
from uuid import uuid4
from typing import TypeVar

from .auth import Auth
from models.user import User

class SessionAuth(Auth):
    """ Implement Session Auth methods """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates Session ID for user with user_id
        Args:
            user_id (str): user's id
        Return:
            None: user_id is None or not str
            session_id (str)
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns user_id based on session_id
        Args:
            session_id (str): session ID
        Return:
            user_id or None if session_id is None or not str
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Return user instance based on cookie value.
        Args:
            request: cookie obj
        Return:
            User instance (JSON)
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ Deletes user session """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True

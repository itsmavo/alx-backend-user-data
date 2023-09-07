#!/usr/bin/env python3
""" Def of class Auth """
import os
from flask import request
from typing import (List, TypeVar)


class Auth:
    """ Manages API Auth """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether path given requires Auth or not.
        Args:
            - path(str): Url to be checked
            - excluded_paths(List[str]): List of paths not requiring Auth.
        Return:
            bool: True if path is not in excluded_paths, else False
        """
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[-1]):
                        return False
        return True


    def authorization_header(self, request=None) -> str:
        """ Returns authorization header from a request object """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return a user instance from info from request obj """
        return None
    
    def session_cookie(self, request=None):
        """
        Returns cookie from a req
        Args:
            request: req obj
        Return:
            value _my_session_id cookie from req obj
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)

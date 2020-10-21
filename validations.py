#!/usr/bin/env python3


def vailidate_user(username, minlen):
    """Checks if the recieved username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1".)
        
        #if length of username is less than min length
        if len(username) < minlen:
            return False
        #if username is not alphabet or numeric
        if not username.isalnum():
            return False
        # Usernames can't begin with a number
        if username [0].isnumeric():
            return False
        #if all the above condition fails then username is correct
        return True

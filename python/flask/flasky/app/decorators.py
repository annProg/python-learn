#!/usr/bin/env python3
#-*- coding:utf-8 -*-  

############################
# Usage:
# File Name: decorators.py
# Author: annhe  
# Mail: i@annhe.net
# Created Time: 2016-05-04 15:28:09
############################

from functools import wraps
from flask import abort
from flask.ext.login import current_user

def permission_required(permission):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			if not current_user.can(permission):
				abort(403)
			return f(*args, **kwargs)
		return decorated_function
	return decorator

def admin_required(f):
	return permission_required(Permission.ADMINISTER)(f)

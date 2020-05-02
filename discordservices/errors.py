class DSException(Exception):
	pass
	
class TokenNotProvided(DSException):
	pass
	
class Unauthorized(DSException):
	pass
	
class BadRequest(DSException):
	pass
	
class NotFound(DSException):
	pass
import json

# TODO: Possible race condition in this class
# What if two users send a request at the same time?
# Should we lock arguments?
class Argument(object):
	def __init__(self):
		self.arguments = []

	def add(self, username, text):
		self.arguments.append({ "text" : text, "user" : username })
	
	def toJSON(self):
		return json.dumps( self.arguments )

	@staticmethod
	def fromJSON(encoded):
		arg = Argument()
		arg.arguments = json.loads( encoded )
		return arg

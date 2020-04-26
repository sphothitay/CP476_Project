# Returns True if the password is good, False if not
# This is based on the ruleset that every password should
# have lowercase, uppercase, and numerical characters, and 
# be at least 6 character long
def isPasswordGood( password ):
	lower = set( x for x in "abcdefghijklmnopqrstuvwxyz" )
	upper = set( x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
	number = set( x for x in "0123456789" )
	pass_set = set( x for x in password )
	
	return len(password) >= 6 and not ( pass_set.isdisjoint(lower)
		or pass_set.isdisjoint(upper)
		or pass_set.isdisjoint(number) )




def relu(value):
	""" Rectified Learning Unit 
		Converts all negative pixel values to 0
	"""
	return max(0, value)
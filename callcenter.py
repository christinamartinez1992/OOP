

class Call(object):
	def __init__(self, unique_id, name, number, time, reason):
		self.unique_id = unique_id
		self.name = name 
		self.number = number
		self.time = time
		self.reason = reason
		
	def display(self):
		print 'unique_id:' + self.unique_id
		print 'name:' + self.name
		print 'number:' + str(self.number)
		print 'time:' + str(self.time)
		print 'reason:' + self.reason

class Call_center(object):
	def __init__(self, queue): 
		self.queue_size = len(queue)

call1 = Call('#10', 'Charlie', 22, 33, 'complaint')
call1.display()

cc1 = Call_center([call1])


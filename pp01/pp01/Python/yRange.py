
class yRange:
	def __init__(self, *args):
		if len(args) == 1:
			start, stop, step = 0, args[0], 1
		elif len(args) == 2:
			start, stop, step = args[0], args[1], 1
		elif len(args) == 3:
			start, stop, step = args[0], args[1], args[2]
		else:
			raise TypeError("args can't be empty, got 0")

		try:
			start, stop, step = int(start), int(stop), int(step)
		except:
			raise TypeError("args must be integers")

		if step == 0:
			raise ValueError("step can't be Zero")

		if step < 0:
			stop = min(stop, start)
		else:
			stop = max(stop, start)

		self._start = start
		self._stop = stop
		self._step = step
		self._counter = 0

		self._len = (self._stop - self._start)/self._step + bool((self._stop - self._start) % self._step)
		self._start_val = self._start - self._step

	def __len__(self):
		return self._len

	def __eq__(self, other):
		return isinstance(other, yRange) and other._start == self._start \
			and other._stop == self._stop and other._step == self._step

	def __iter__(self):
		return self

	def __next__(self):
		self._start_val += self._step
		self._counter += 1
		if self._counter > self._len:
			raise StopIteration()

		return self._start_val

if __name__ == '__main__':
	for case in (
	    (10, ),
	    (0, 10),
	    (0, 10, 2),
	    (0, 10, 7),
	    (10, 0),
	    (10, 0, -1),
	    (10, 0, -5),
	    (-1, -10),
	    (-1, -10, -1),
	    (-1, -10, -5),
	    (10,10,1)):

		print(list(yRange(*case)))
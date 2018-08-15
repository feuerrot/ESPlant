import machine

class Moisture:

	def __init__(self, name, pin, duration, times, callback, timer):
		self.name = name
		self.adc = machine.ADC(machine.Pin(pin))
		self.duration = duration
		self.ctr_max = times
		self.ctr = 0
		self.result = None
		self.storage = []
		self.cb = callback
		self.timer = timer
		self._adc_init()

	def _adc_init(self):
		self.adc.atten(self.adc.ATTN_11DB)
		self.adc.width(self.adc.WIDTH_12BIT)

	def set_timer(self):
		self.timer.add(int(self.duration/self.ctr_max), self.callback)

	def callback(self):
		self.storage.append(self.adc.read())
		self.ctr += 1

		if self.ctr == self.ctr_max:
			self.ctr = 0
			self.result = sorted(self.storage)[int(len(self.storage)/2)]
			self.storage = []
			self.cb(self)
		else:
			self.set_timer()


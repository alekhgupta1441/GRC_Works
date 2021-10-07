'''Convert a pmt pair (freq . f_Hz) to (freq . f_MHz).
'''

import numpy as np
from gnuradio import gr
import pmt

class cvtBlock(gr.basic_block):

	def __init__(self):
		"""arguments to this function show up as parameters in GRC"""
		gr.basic_block.__init__(
			self,
			name='MHz to Hz',
			in_sig=None,
			out_sig=None
		)

		self.message_port_register_in(pmt.intern('freq_MHz_in'))
		self.set_msg_handler(pmt.intern('freq_MHz_in'), self.MHzToHz)

		self.message_port_register_out(pmt.intern('freq_Hz_out'))

	def MHzToHz(self, msg):
		'''msg expected to be pmt pair (freq . val).'''

		cmd = pmt.car(msg)
		freq_Hz = 1e6 * pmt.to_python(pmt.cdr(msg))

		hzDict = pmt.make_dict()
		hzDict = pmt.dict_add(hzDict, cmd, pmt.to_pmt(freq_Hz))
		self.message_port_pub(pmt.intern('freq_Hz_out'), hzDict)

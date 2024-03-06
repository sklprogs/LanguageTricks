#!/usr/bin/python3

import skl_shared.shared as sh
from skl_shared.localize import _


class Converter:
	# Add anchors to GFM TOC. Input is read from clipboard.
	def __init__(self):
		self.Success = True
		self.text = ''
	
	def get(self):
		f = '[LanguageTricks] add_anchors.Converter.get'
		if not self.Success:
			sh.com.cancel(f)
			return
		self.text = sh.Clipboard().paste()
		if not self.text:
			self.Success = False
			sh.com.rep_out(f)
	
	def _convert(self,line):
		line = line.strip()
		if not line:
			return line
		if line.startswith('['):
			return line
		title = index_ = line
		title = title.replace('|',r'\|')
		index_ = index_.replace('|','')
		index_ = index_.lower()
		itext = sh.Text(index_)
		itext.delete_punctuation()
		index_ = itext.delete_figures()
		index_ = index_.replace('+','')
		index_ = index_.replace('=','')
		index_ = index_.replace(' ','-')
		return '[{}](#{})'.format(title,index_)
	
	def parse(self):
		f = '[LanguageTricks] add_anchors.Converter.parse'
		if not self.Success:
			sh.com.cancel(f)
			return
		lst = self.text.splitlines()
		for i in range(len(lst)):
			lst[i] = self._convert(lst[i])
		self.text = '\n'.join(lst)
	
	def debug(self):
		f = '[LanguageTricks] add_anchors.Converter.debug'
		if not self.Success:
			sh.com.cancel(f)
			return
		sh.com.run_fast_debug(f,self.text)
	
	def run(self):
		self.get()
		self.parse()
		self.debug()


if __name__ == '__main__':
	Converter().run()

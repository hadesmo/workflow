#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json

result = [u'<?xml version="1.0"?>', u'<items>']

#精品区
try:
	url = "http://s.video.qq.com/search?comment=1&stype=0&plat=2&otype=json&query={query}&start=0&end=5"

	req = urllib2.Request(url)
	r = urllib2.urlopen(req)

	sou_json_result = json.loads(r.read().replace('QZOutputJson=', '').strip(';'))


	for i,item in enumerate(sou_json_result["list"]):
		ti = item["TI"].replace('<em  class="c_txt3">','').replace('</em>','')
		result.append(u'<item uid="tenvideosou' + str(i) + u'" arg="' + item["AW"] + u'">')
		result.append(u'<title>' + ti + u'</title>')
		result.append(u'<subtitle>观看视频</subtitle>')
		result.append(u'<icon>icon.png</icon>')
		result.append(u'</item>')
except (KeyError) as e:
	pass

#综合区
url = "http://s.video.qq.com/search?comment=0&stype=0&plat=2&otype=json&query={query}&start=0&end=5"

req = urllib2.Request(url)
r = urllib2.urlopen(req)

sou_json_result = json.loads(r.read().replace('QZOutputJson=', '').strip(';'))


for i,item in enumerate(sou_json_result["list"]):
	ti = item["TI"].replace('<em  class="c_txt3">','').replace('</em>','')
	result.append(u'<item uid="tenvideosou' + str(i) + u'" arg="' + item["AW"] + u'">')
	result.append(u'<title>' + ti + u'</title>')
	result.append(u'<subtitle>观看视频</subtitle>')
	result.append(u'<icon>icon.png</icon>')
	result.append(u'</item>')

result.append(u'</items>')
xml = ''.join(result)

print xml.encode("utf8")


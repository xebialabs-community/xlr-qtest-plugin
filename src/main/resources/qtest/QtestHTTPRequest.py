#
# Copyright 2020 Digital.ai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from xlrelease.HttpRequest import HttpRequest
from com.xebialabs.xlrelease.domain.configuration import HttpConnection
from org.apache.commons.codec.binary import Base64
from java.lang import String
from org.apache.http.client.methods import HttpGet, HttpHead, HttpPost, HttpPut, HttpDelete, HttpPatch
from org.apache.http.entity import StringEntity

class QtestHTTPRequest(HttpRequest):

	def __init__(self, params, username = None, password = None, token = None):
		self.params = HttpConnection(params)
		self.username = username
		self.password = password
		self.token = token
	def setCredentials(self, request):
		if self.token:
			request.addHeader('Authorization', self.token)
			return
		elif self.username:
			username = self.username
		elif self.params.getUsername():
			username = self.params.getUsername()
		else:
			return
		encoding = Base64.encodeBase64String(String(username + ':' ).getBytes('ISO-8859-1'))
		request.addHeader('Authorization', 'Basic ' + encoding)
	def buildRequest(self, method, context, body, contentType, headers):
		url = self.quote(self.createPath(self.params.getUrl(), context))

		method = method.upper()

		if method == 'GET':
			request = HttpGet(url)
		elif method == 'HEAD':
			request = HttpHead(url)
		elif method == 'POST':
			request = HttpPost(url)
			request.setEntity(StringEntity(body))
		elif method == 'PUT':
			request = HttpPut(url)
			request.setEntity(StringEntity(body))
		elif method == 'DELETE':
			request = HttpDelete(url)
		elif method == 'PATCH':
			request = HttpPatch(url)
			request.setEntity(StringEntity(body))
		else:
			raise Exception('Unsupported method: ' + method)

		request.addHeader('Content-Type', contentType)
		self.setCredentials(request)
		self.setProxy(request)
		self.setHeaders(request, headers)

		return request

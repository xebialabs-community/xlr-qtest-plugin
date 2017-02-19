#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from xlrelease.HttpRequest import HttpRequest
from com.xebialabs.xlrelease.domain.configuration import HttpConnection
from org.apache.commons.codec.binary import Base64
from java.lang import String
from org.apache.http import HttpHost
from org.apache.http.client.config import RequestConfig
from org.apache.http.client.methods import HttpGet, HttpHead, HttpPost, HttpPut, HttpDelete, HttpPatch
from org.apache.http.util import EntityUtils
from org.apache.http.entity import StringEntity
from org.apache.http.impl.client import HttpClients

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



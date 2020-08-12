#
# Copyright 2020 Digital.ai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import urllib
from qtest.qtestClientUtil import qtestClientUtil
from  xlrelease.CredentialsFallback import CredentialsFallback

qtest_client = qtestClientUtil.create_qtest_client(server, username, password)
credentials = CredentialsFallback(server, username, password).getCredentials()

body = urllib.urlencode({
            "grant_type" : "password",
            "username" : str(credentials['username']),
            "password" : str(credentials['password'])
            })
result = qtest_client.login(body)
token_type = result["token_type"]
access_token = result["access_token"]
token = "%s %s" % (token_type, access_token)
print "Successfully able to authenticate with Qtest Account"

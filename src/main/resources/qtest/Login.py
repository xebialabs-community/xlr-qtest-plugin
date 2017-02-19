#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
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


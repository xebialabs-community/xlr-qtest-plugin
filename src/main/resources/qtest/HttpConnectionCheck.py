#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import urllib
from qtest.qtestClientUtil import qtestClientUtil
from  xlrelease.CredentialsFallback import CredentialsFallback

params = {'url': configuration.url, 'username': configuration.username, 'password': configuration.password,
          'proxyHost': configuration.proxyHost, 'proxyPort': configuration.proxyPort}

qtest_client = qtestClientUtil.create_qtest_client(params, "", "")

body = urllib.urlencode({
            "grant_type" : "password",
            "username" : str(configuration.username),
            "password" : str(configuration.password)
            })
result = qtest_client.login(body)
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from qtest.qtestClient import qtestClient


class qtestClientUtil(object):

    @staticmethod
    def create_qtest_client(container, username, password, token=None):
        client = qtestClient.create_client(container, username, password, token)
        return client

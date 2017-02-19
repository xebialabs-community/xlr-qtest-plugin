#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import json
from qtest.QtestHTTPRequest import QtestHTTPRequest
from org.apache.http.client import ClientProtocolException

class qtestClient(object):
    def __init__(self, http_connection, username, password, token=None):
        self.http_request = QtestHTTPRequest(http_connection, username , password, token) # Should not have to pass the empty P/W string, will work on fix.

    @staticmethod
    def create_client(http_connection, username, password, token=None):
        return qtestClient(http_connection, username, password, token)

    def login(self, body):
        login_endpoint = "/oauth/token"
        try:
            login_response = self.http_request.post(login_endpoint,body, contentType="application/x-www-form-urlencoded")
        except ClientProtocolException:
            raise Exception("URL is not valid")
        if not login_response.isSuccessful():
            reason = "Unknown"
            if login_response.status == 400:
                reason = "Bad request"
            elif login_response.status == 401:
                reason = "Unauthorized"
            elif login_response.status == 403:
                reason = "Forbidden"
            raise Exception("HTTP response code %s (%s)" % (login_response.status, reason))
        return json.loads(login_response.getResponse())
    def lookup_project_by_name(self,projectName):
        lookup_project_by_name_endpoint = "/api/v3/projects"
        lookup_project_by_name_response = self.http_request.get(lookup_project_by_name_endpoint,contentType="application/json")
        result =  json.loads(lookup_project_by_name_response.getResponse())
        return [item for item in result if item["name"].lower().strip() == projectName.lower().strip()][0]

    def lookup_object_by_query(self, project_id, body):
        lookup_object_by_name_endpoint = "/api/v3/projects/%s/search" % (project_id)
        lookup_object_by_name_response = self.http_request.post(lookup_object_by_name_endpoint,body,contentType="application/json")
        return json.loads(lookup_object_by_name_response.getResponse())
    def add_comment(self, project_id, object_type,object_id, body):
        add_comment_endpoint = "/api/v3/projects/%s/%s/%s/comments" % (project_id, object_type, object_id)
        self.http_request.post(add_comment_endpoint,body, contentType="application/json")
    def add_test_case(self,project_id,body):
        add_test_case_endpoint = "/api/v3/projects/%s/test-cases/" % (project_id)
        add_test_case_response = self.http_request.post(add_test_case_endpoint,body, contentType="application/json")
        return json.loads(add_test_case_response.getResponse())
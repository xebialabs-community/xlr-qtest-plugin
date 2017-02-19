#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import urllib
from qtest.qtestClientUtil import qtestClientUtil
from  xlrelease.CredentialsFallback import CredentialsFallback

qtest_client = qtestClientUtil.create_qtest_client(server, "", "",token)

find_object_body = '{ "object_type" : "%s", "fields" : ["*"], "query" : "%s"}' % (str(objectType),str(objectQuery))
add_comment_body = '{ "content" : "%s" }' % (str(comment))
project_obj = qtest_client.lookup_project_by_name(projectName)
print "Found project ID [%s] for Project Name: %s\n" % (project_obj["id"], projectName)
result_obj = qtest_client.lookup_object_by_query(str(project_obj["id"]), find_object_body)
for item in result_obj["items"]:
	print "Adding comment to %s ID [%s]-: %s\n" % (str(objectType), item["id"], item["name"])
	qtest_client.add_comment(project_obj["id"],str(objectType),item["id"],add_comment_body)
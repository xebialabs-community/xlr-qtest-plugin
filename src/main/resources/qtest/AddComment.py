#
# Copyright 2020 Digital.ai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
from qtest.qtestClientUtil import qtestClientUtil

qtest_client = qtestClientUtil.create_qtest_client(server, "", "",token)

find_object_body = '{ "object_type" : "%s", "fields" : ["*"], "query" : "%s"}' % (str(objectType),str(objectQuery))
add_comment_body = '{ "content" : "%s" }' % (str(comment))
project_obj = qtest_client.lookup_project_by_name(projectName)
print "Found project ID [%s] for Project Name: %s\n" % (project_obj["id"], projectName)
result_obj = qtest_client.lookup_object_by_query(str(project_obj["id"]), find_object_body)
for item in result_obj["items"]:
	print "Adding comment to %s ID [%s]-: %s\n" % (str(objectType), item["id"], item["name"])
	qtest_client.add_comment(project_obj["id"],str(objectType),item["id"],add_comment_body)

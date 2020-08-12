#
# Copyright 2020 Digital.ai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import json
from qtest.qtestClientUtil import qtestClientUtil

qtest_client = qtestClientUtil.create_qtest_client(server, "", "",token)

test_case_body = { "name" : str(testName),
	"properties" : [ { "field_id":str(key), "field_value":str(value) } for key, value in properties.iteritems() ],
	"test_steps" : [ { "description":str(key), "expected":str(value) } for key, value in steps.iteritems() ]
}

project_obj = qtest_client.lookup_project_by_name(projectName)
print "Found project ID [%s] for Project Name: %s\n" % (project_obj["id"], projectName)
print "Creating new test case under project with Name : %s\n" % ( testName)


result_obj = qtest_client.add_test_case(project_obj["id"],json.dumps(test_case_body))
testCaseId = result_obj["id"]
print "Test case successfully created with ID[%s]\n" % (result_obj["id"])

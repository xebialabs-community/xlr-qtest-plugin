#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
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
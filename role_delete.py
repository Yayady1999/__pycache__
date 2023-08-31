import boto3

IAM_RESOURCE = boto3.resource('iam')

role = IAM_RESOURCE.Role( 'sy3_test_role')

role.delete()

print('role successfully deleted')



#aws iam delete-role --role-name sy3_test_role (aws CLI command to delte role)
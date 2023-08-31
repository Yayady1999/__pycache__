#import boto3

#client = boto3.client('cloudformation')

sample_str = "Sample Stringaws"    #This string should be the stack name

# Get last 3 character
last_chars = sample_str[-3:]

print('Last 3 character : ', last_chars)

if (last_chars == "rcn") or (last_chars == "RCN"):
    print("RCN stack")
else:
    print("No")

 
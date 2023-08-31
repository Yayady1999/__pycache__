import stack_data


dict= {stack_data: [{'StackId': 'arn:aws:cloudformation:eu-central-1:080781648294:stack/glue-stack-test/c0040210-1c9f-11ee-8259-0661547683ae', 'StackName': 'glue-stack-test', 'StackStatus': 'CREATE_COMPLETE', 'DriftInformation': {'StackDriftStatus': 'NOT_CHECKED'}}, {'StackId': 'arn:aws:cloudformation:eu-central-1:080781648294:stack/SC-080781648294-pp-xn5lhfgi6nohc/e0e9b680-1c92-11ee-aef4-0aa345a5e6ee', 
                                                                                                                                                                                                                                                                         'StackName': 'SC-080781648294-pp-xn5lhfgi6nohc',  'StackStatus': 'CREATE_COMPLETE', 'DriftInformation': {'StackDriftStatus': 'NOT_CHECKED'}}, {'StackId': 'arn:aws:cloudformation:eu-central-1:080781648294:stack/SC-080781648294-pp-iq2cf2eqxtd66/85ef5d20-fa14-11ed-b8a1-024a86086c9a', 'StackName': 'SC-080781648294-pp-iq2cf2eqxtd66',  'StackStatus': 'CREATE_COMPLETE', 'DriftInformation': {'StackDriftStatus': 'NOT_CHECKED'}}, {'StackId': 'arn:aws:cloudformation:eu-central-1:080781648294:stack/TestJoshStack/866530c0-fa11-11ed-90fd-02bdb3df7674', 
'StackName': 'TestJoshStack',   'StackStatus': 'CREATE_COMPLETE', 'DriftInformation': {'StackDriftStatus': 'NOT_CHECKED'}}]}

val = stack_data('StackId')
print(val)
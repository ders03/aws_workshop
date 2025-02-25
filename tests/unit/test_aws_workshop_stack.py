import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_workshop.aws_workshop_stack import AwsWorkshopStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_workshop/aws_workshop_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsWorkshopStack(app, "aws-workshop")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

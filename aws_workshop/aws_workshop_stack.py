from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda, 
    aws_s3 as s3,
    aws_sqs as sqs,  
    aws_lambda_event_sources, 
)
from constructs import Construct

class AwsWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        get_data_lambda = _lambda.Function(
            self, "GetDataLambda", 
            runtime = _lambda.Runtime.PYTHON_3_12, 
            handler = "get_data.handler", 
            code = _lambda.Code.from_asset("lambda"), 
            timeout = Duration.seconds(10),
        ) 

        raw_bucket = s3.Bucket(self, "RawBucket", 
            bucket_name=f"{self.account}-raw-bucket",
        ) 
        raw_bucket.grant_read_write(get_data_lambda) 

        enqueue_raw_data_lambda = _lambda.Function( 
            self, "EnqueueRawDataLambda", 
            runtime = _lambda.Runtime.PYTHON_3_12, 
            handler = "raw_queue.handler", 
            code = _lambda.Code.from_asset("lambda"), 
            timeout = Duration.seconds(5),
        ) 
        raw_bucket.grant_read_write(enqueue_raw_data_lambda)

        s3_put_event_source = aws_lambda_event_sources.S3EventSource( 
            bucket=raw_bucket, 
            events=[s3.EventType.OBJECT_CREATED], 
        )

        enqueue_raw_data_lambda.add_event_source(s3_put_event_source)        
        raw_queue = sqs.Queue(self, "RawQueue")  
        raw_queue.grant_send_messages(enqueue_raw_data_lambda)  

        processed_queue = sqs.Queue(self, "ProcessedQueue") 

        process_raw_queue_lambda = _lambda.Function(
            self, "ProcessRawQueueLambda", 
            runtime=_lambda.Runtime.PYTHON_3_12, 
            handler="process_raw_queue.handler", 
            code=_lambda.Code.from_asset("lambda"), 
            timeout = Duration.seconds(10),
            environment = {
                "PROCESSED_URL": processed_queue.queue_url, 
            }
        )
        raw_queue_event = aws_lambda_event_sources.SqsEventSource(raw_queue) 
        raw_queue.grant_consume_messages(process_raw_queue_lambda)  
        process_raw_queue_lambda.add_event_source(raw_queue_event) 
        processed_queue.grant_send_messages(process_raw_queue_lambda) 

        processed_bucket = s3.Bucket(self, "ProcessedBucket", 
            bucket_name=f"{self.account}-processed-bucket",                             
        ) 

        load_lambda = _lambda.Function(
            self, "LoadLambda", 
            runtime = _lambda.Runtime.PYTHON_3_12, 
            handler = "load.handler", 
            code = _lambda.Code.from_asset("lambda"),
            timeout = Duration.seconds(10), 
            environment = {
                "BUCKET_NAME": processed_bucket.bucket_name, 
            }
        ) 

        load_event = aws_lambda_event_sources.SqsEventSource(processed_queue) 
        load_lambda.add_event_source(load_event) 
        processed_queue.grant_consume_messages(load_lambda)
        processed_bucket.grant_read_write(load_lambda)
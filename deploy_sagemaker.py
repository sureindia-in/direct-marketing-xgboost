## Note: this requires a MLflow pyfunc docker container to already exist in sagemaker

import mlflow.sagemaker as mfs

model_uri = "mlruns/1/2c14fe6785a8417c883f526b907d1c49/artifacts/direct-marketing-xgboost-model"

# The region is chosen, pick whats close to you or your systems!
region = "us-east-1"
# The aws account id can be found in the console
aws_account_id = "794352754851"
# We use these inputs to automatically reference the sagemaker docker container
image_url = aws_account_id \
            + ".dkr.ecr." \
            + region \
            + ".amazonaws.com/mlflow-pyfunc:1.19.0"
print(image_url)
# now we specify the role that we setup for sagemaker in the previous step
#sagemaker_arn = "arn:aws:iam::794352754851:role/AmazonSageMaker-ExecutionRole-20210130T191900"
sagemaker_arn = "arn:aws:iam::794352754851:role/service-role/AmazonSageMaker-ExecutionRole-20210130T191900"


# finally, we pick a name for our endpoint within sagemaker
endpoint_name = "mlflow-xgb-demo"


# with all of the inputs, we run the following to deploy the model it sagemaker
mfs.deploy(app_name=endpoint_name,
           model_uri=model_uri,
           region_name=region,
           mode="create", #this should change to replace if the endpoint already exists
           execution_role_arn=sagemaker_arn,
           image_url=image_url,
           instance_type='ml.t2.medium') # smallest/cheapest sagemaker allowed size
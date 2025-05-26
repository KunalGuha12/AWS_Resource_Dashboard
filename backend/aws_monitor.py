import boto3
from flask import Flask, jsonify

app = Flask(_name_)

# Initialize AWS clients
ec2_client = boto3.client('ec2')
rds_client = boto3.client('rds')
lambda_client = boto3.client('lambda')
ecs_client = boto3.client('ecs')

def get_ec2_instances():
    instances = ec2_client.describe_instances()
    ec2_statuses = []
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            ec2_statuses.append({
                "id": instance["InstanceId"],
                "type": instance["InstanceType"],
                "state": instance["State"]["Name"]
            })
    return ec2_statuses

def get_rds_instances():
    instances = rds_client.describe_db_instances()
    rds_statuses = [{"id": db["DBInstanceIdentifier"], "state": db["DBInstanceStatus"]} for db in instances["DBInstances"]]
    return rds_statuses

def get_lambda_functions():
    functions = lambda_client.list_functions()
    lambda_statuses = [{"name": fn["FunctionName"], "state": "Active"} for fn in functions["Functions"]]
    return lambda_statuses

def get_ecs_clusters():
    clusters = ecs_client.list_clusters()
    cluster_data = []
    for cluster_arn in clusters["clusterArns"]:
        cluster_desc = ecs_client.describe_clusters(clusters=[cluster_arn])
        for cluster in cluster_desc["clusters"]:
            cluster_data.append({"name": cluster["clusterName"], "status": cluster["status"]})
    return cluster_data

@app.route('/aws-resources', methods=['GET'])
def get_aws_resources():
    resources = {
        "EC2": get_ec2_instances(),
        "RDS": get_rds_instances(),
        "Lambda": get_lambda_functions(),
        "ECS": get_ecs_clusters()
    }
    return jsonify(resources)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
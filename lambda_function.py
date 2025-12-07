import boto3
import csv
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = "data006"
    key = "data.csv"
    
    print(f"Processing {key} from {bucket}...")
    
    # Read CSV from S3
    obj = s3.get_object(Bucket=bucket, Key=key)
    lines = obj['Body'].read().decode('utf-8').splitlines()
    reader = csv.DictReader(lines)
    
    results = []
    
    for row in reader:
        p_id = row['product_id']
        shipped = float(row['shipped_units'])
        total = float(row['total_units'])
        
        efficiency = shipped / total
        
        results.append({"id": p_id, "efficiency": efficiency})
        
    print("Success!")
    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }

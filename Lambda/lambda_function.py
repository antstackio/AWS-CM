import boto3
import json

client = boto3.client('comprehendmedical')

def lambda_handler(event, context):
    
    data = event["body"]
    data = json.loads(data)
    
    opt = data["choice"]
    inp = data["body"]

    if opt == 'Detect Entities':
        result = client.detect_entities_v2(Text=inp)
        entities = result['Entities']
        return entities

    elif opt == 'RXNorm':
        result = client.infer_rx_norm(Text=inp)
        entities = result['Entities']
        return entities

    elif opt == 'ICD-10-CM':
        result = client.infer_icd10_cm(Text=inp)
        entities = result['Entities']
        return entities

    elif opt == 'SNOMED CT':
        result = client.infer_snomedct(Text=inp)
        entities = result['Entities']
        return entities
        
    elif opt == 'Detect PHI':
        result = client.detect_phi(Text=inp)
        entities = result['Entities']
        return entities
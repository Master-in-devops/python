import boto3

# 1. Initialize the session
session = boto3.Session(profile_name='my-work-profile')
ec2 = session.resource('ec2')

# 2. Reference your specific instance ID
instance_id = 'i-0fb2d82d7e918d3ad'

try:
    instance = ec2.Instance(instance_id)
    
    # 3. Stop the instance
    print(f"Stopping instance: {instance_id}...")
    instance.stop()
    
    # 4. Wait for confirmation
    instance.wait_until_stopped()
    print(f"Successfully stopped. Current state: {instance.state['Name']}")

except Exception as e:
    print(f"Error: {e}")
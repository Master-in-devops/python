 1. Create the ec2 instance in terminal 
run-instances \
    --image-id ami-01f79b1e4a5c64257 \
    --count 1 \
    --instance-type t2.micro \
    --key-name key-ec2 \
    --security-group-ids sg-006f78394545acaf4 \
    --subnet-id subnet-0b56bd048db890076 \
    --profile my-work-profile

2. Stopping the Instance (Python) create a new file and add the script 

# User-Defined Variables
PROFILE = 'my-work-profile'
INSTANCE_ID = 'i-0fb2d82d7e918d3ad'

def stop_instance():
    # Setup Session
    session = boto3.Session(profile_name=PROFILE)
    ec2 = session.resource('ec2')
    
    try:
        instance = ec2.Instance(INSTANCE_ID)
        
        print(f"Stopping instance: {INSTANCE_ID}...")
        instance.stop()
        
        # Block until the instance reaches the 'stopped' state
        instance.wait_until_stopped()
        print(f"Success! Instance {INSTANCE_ID} is now STOPPED.")
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    stop_instance()

3. Run the script by using python stop-ec2.py

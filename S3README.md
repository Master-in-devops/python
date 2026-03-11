### AWS CLI Profile Commands

**1. Create the profile:**
aws configure --profile my-work-profile

**2. Test the profile:**
aws s3 ls --profile my-work-profile

**3. Set as default for the current session:**
export AWS_PROFILE=my-work-profile

**4. Run commands without profile flag:**
aws s3 ls
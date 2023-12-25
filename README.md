### The way I use to deploy the WireGuard server on AWS.

#### Now here are:
1. SSM_Policy - IAM Role Policy to use System Manager Parameters Store in EC2 instances bootstraping.
2. WG_Docker_EC2_LaunchScript - user-data for EC2 Ubuntu instance bootstraping to setup Docker container with WireGuard. Basis for script took from https://github.com/wg-easy/wg-easy, because there is already UI as well. Thank them!
3. Lambda_EC2_Launch_Policy - IAM Role Policy for Lambda to launch EC2 instance from Launch Template.
4. Create_EC2.py - Lambda function which create EC2 instance from Launch Template. I used Amazon CodeWhisperer and Amazon's documentation.

#### To be continued...
But at the moment I have some another projects.

The way I use to deploy the WireGuard server on AWS.

Now here are:
1. SSM_Policy - IAM Role Policy to use System Manager Parameters Store in EC2 instances bootstraping.
2. WG_Docker_EC2_LaunchScript - user-data for EC2 Ubuntu instance bootstraping to setup Docker container with WireGuard. Basis for script took from https://github.com/wg-easy/wg-easy, because there is already UI as well. Thank them!


curl https://sdk.cloud.google.com | bash
"/tmp/google-cloud-sdk/bin/gcloud" auth login
. /home/workspace/.student_bashrc # reload bash profile
mkdir /tmp/data_waymo
cd /home/workspace
python download_process.py --data_dir /home/workspace/data_waymo --temp_dir /tmp/data_waymo

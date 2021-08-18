gcloud auth login
mkdir /tmp/data_waymo
mkdir ./data
python download_process.py --data_dir ./data --temp_dir /tmp/data_waymo


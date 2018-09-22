## Use Ubuntu 16.04 or other distro compatible to python 3.5 (TK - 2018.09.04)
sudo apt-get update
sudo apt-get dist-upgrade

python3 --version
pip3 --version

sudo apt-get install python3.5 python3-pip
sudo pip3 install --upgrade pip

gsutil cp gs://tklab-ngs/*whl .

sudo -H pip3 install --upgrade ont_albacore-2.3.1-cp35-cp35m-manylinux1_x86_64.whl 
which read_fast5_basecaller.py 

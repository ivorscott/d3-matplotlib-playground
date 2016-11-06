#!/usr/bin/env bash

apt-get update && apt-get install -qq -y apt-transport-https ca-certificates linux-image-extra-$(uname -r)
apt-get update && apt-get build-dep -y python-matplotlib && apt-get install -y docker-engine
service docker stop
service docker start
pip install -r requirements.txt
python run.py

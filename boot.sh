#!/usr/bin/env bash
apt-get update && apt-get build-dep -y python-matplotlib
pip install -r requirements.txt
python run.py

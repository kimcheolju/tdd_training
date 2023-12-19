#!/bin/bash
docker rmi webmonitor:dev
docker build -t webmonitor:dev .
FROM nvidia/cuda:10.2-cudnn7-runtime-centos8 AS DEV

WORKDIR /wrk

RUN yum -y update && \
    yum -y install python3-devel python3-pip gcc gcc-c++ make && \
    yum -y groupinstall 'Development Tools'

COPY ,/requirements.txt ,/requirements.txt
RUN pip3 install -r requirements.txt

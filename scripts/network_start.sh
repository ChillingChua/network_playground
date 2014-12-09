DEBIAN_TAG='debian:latest'
docker run $DEBIAN_TAG
DEBIAN_IP=`docker inspect -f '{{ .NetworkSettings.IPAddress }}' debian`
echo "starting docker image $DEBIAN_TAG with ip: $DEBIAN_IP"

CENTOS_TAG='centos:latest'
docker run $CENTOS_TAG
CENTOS_IP=`docker inspect -f '{{ .NetworkSettings.IPAddress }}' centos`
echo "starting docker image $CENTOS_TAG with ip: $CENTOS_IP"

UBUNTU_TAG='ubuntu:latest'
docker run $UBUNTU_TAG
UBUNTU_IP=`docker inspect -f '{{ .NetworkSettings.IPAddress }}' ubuntu`
echo "starting docker image $UBUNTU_TAG with ip: $UBUNTU_IP"

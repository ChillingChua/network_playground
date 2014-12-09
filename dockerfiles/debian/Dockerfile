FROM debian:latest
MAINTAINER Andreas Werner <andiwerner_AT_gmx.de>

RUN echo 'deb http://apt.puppetlabs.com squeeze main dependencies' >> /etc/apt/sources.list.d/puppetlabs.list

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install apt-utils
RUN apt-get -y install net-tools
RUN apt-get -y install vim
RUN apt-get -y install git
RUN apt-get -y install ntp
RUN apt-get -y install python2.6
RUN apt-get -y install rubygems
RUN apt-get -y --force-yes install puppet

RUN gem install git

# some puppet configurations
RUN echo '[agent]' >> /etc/puppet/puppet.conf
RUN echo 'environment=xmlapi_development' >> /etc/puppet/puppet.conf
RUN echo 'server=f1-v3-puppet-dev1b.infosys.de' >> /etc/puppet/puppet.conf
RUN echo 'masterport=8140' >> /etc/puppet/puppet.conf
RUN echo 'report=False' >> /etc/puppet/puppet.conf
RUN echo 'listen=True' >> /etc/puppet/puppet.conf
RUN echo 'ordering=manifest' >> /etc/puppet/puppet.conf

# remove deprication warning
RUN sed -e s/'templatedir=\$confdir\/templates'/'#templatedir=\$confdir\/templates'/g /etc/puppet/puppet.conf > /tmp/puppet.conf
RUN mv /etc/puppet/puppet.conf /etc/puppet/puppet.conf_orig
RUN mv /tmp/puppet.conf /etc/puppet/puppet.conf

# set timezone for cert verification
RUN echo Europe/Berlin > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

# -t include --detailrd-exitcodes, which returns 2 on change
# this breaks the docker build process because exit code is not 0
RUN /usr/bin/puppet agent --verbose --onetime

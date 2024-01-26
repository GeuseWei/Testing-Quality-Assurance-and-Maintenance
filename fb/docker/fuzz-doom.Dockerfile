#
# Fuzz Doom Docker image 
#

ARG BASE_IMAGE=bionic-scm
# Base image with usual build dependencies
FROM buildpack-deps:$BASE_IMAGE

# Install dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
  apt-get install -yqq software-properties-common && \
  apt-get update && \
  apt-get upgrade -yqq && \
  apt-get install -yqq cmake cmake-data unzip \
      zlib1g-dev \
      ninja-build libgraphviz-dev \
      python3-pip \
      less vim \
      gcc-multilib \
      sudo \
      graphviz libgraphviz-dev python3-pygraphviz \
      lcov ggcov rsync \
      libsdl2-dev libsdl2-mixer-dev libsdl2-net-dev

# Install llvm10 from llvm repo since bionic comes with much older version
WORKDIR /tmp
RUN wget https://apt.llvm.org/llvm.sh && \
  chmod +x llvm.sh && \
  ./llvm.sh 10 && \
  apt-get install -y clang-format-10


# setup default user
RUN useradd -ms /bin/bash doom && \
  echo doom:stqam | chpasswd && \
  usermod -aG sudo doom && \
  echo "PS1='\${debian_chroot:+(\$debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\n\[\033[00m\]\\\$ '" >> /home/doom/.bashrc

# user and directory for when the container starts interactively
USER doom
WORKDIR /home/doom


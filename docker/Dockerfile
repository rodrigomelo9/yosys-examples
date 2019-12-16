from python:3-slim-buster

RUN apt-get update -qq \
 && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
    ca-certificates \
    clang \
    curl \
    libffi-dev \
    libreadline-dev \
    tcl-dev \
    graphviz \
    xdot \
    bison \
    flex \
    gawk \
    gcc \
    git \
    iverilog \
    pkg-config \
 && apt-get autoclean && apt-get clean && apt-get -y autoremove \
 && update-ca-certificates \
 && rm -rf /var/lib/apt/lists

WORKDIR /opt

RUN git clone --depth 1 https://github.com/YosysHQ/yosys.git \
 && cd yosys \
 && make \
 && make install \
 && make test

ENV PATH /opt/yosys/bin:$PATH

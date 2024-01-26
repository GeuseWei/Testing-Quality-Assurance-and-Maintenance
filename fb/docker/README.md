# Docker Images for FuzzDoom

This directory contains scripts for building docker containers to compile and
run FuzzDoom. 

To get a pre-build container from docker hub do:

```shell
$ docker pull uwstqam/fuzz-doom
```

## Building 

These instructions are only necessary if you want to build the container yourself 
instead of using pre-build container from DockerHub.

```shell
$ docker build  -t uwstqam/fuzz-domm -f docker/fuzz-doom.Dockerfile .
```


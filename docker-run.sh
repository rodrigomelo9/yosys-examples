#!/usr/bin/env sh

APP=${@:-/bin/bash}

IMAGE=yosys-pyfpga

DOCKER_BASHRC=/tmp/.docker_${USER}_bashrc

rm -rf ${DOCKER_BASHRC} 2>/dev/null
cp ${HOME}/.bashrc ${DOCKER_BASHRC} 2>/dev/null
echo "PS1=\"($IMAGE docker) \$PS1\"" >> ${DOCKER_BASHRC}

docker run \
    -v "$HOME":"$HOME" \
    -v /etc/passwd:/etc/passwd:ro \
    -v /etc/shadow:/etc/shadow:ro \
    -v /etc/group:/etc/group:ro \
    -v /mnt:/mnt \
    -v /tmp:/tmp \
    -v ${DOCKER_BASHRC}:${HOME}/.bashrc \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /var/run/dbus:/var/run/dbus \
    -v /usr/share/git/completion:/usr/share/git/completion \
    -v /opt:/opt \
    -e DISPLAY=$DISPLAY \
    --privileged \
    --net=host \
    -i -w "$PWD" -u $(id -u):$(id -g) -t --rm \
    --group-add=sudo \
    $IMAGE \
    $APP

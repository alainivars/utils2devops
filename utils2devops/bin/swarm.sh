#!/bin/bash
set +x

#
# Just a quick script to create and destroy a local swarm
#

manager_count=0
worker_count=0
worker=
manager=
actions=()

usage()
{
    echo "usage:"
    echo "  swarm [-h | --help] To get this help"
    echo "      If the docker-swarm don't exist it will be created"
    echo "  swarm -c|--create [-m|--count_manager x -w|--count_worker y] To create node to a swarm"
    echo "      Where x is the number of manager node to create/add in the swarm."
    echo "      Where y is the number of worker node to create/add in the swarm."
    echo "  swarm -r|--remove x] To destroy a swarm"
    echo "      Where x is the number of node in the swarm."
}


if [ -z $1 ];then
    actions=(usage)
fi

while [ "$1" != "" ]; do
    case $1 in
        -c | --create )
            actions=(create_swarm_nodes)
            ;;
        -r | --remove )
            shift
            if [ -z "$1" ]
            then
                echo "You must give a number of node to remove"
                exit 1
            else
                echo "gived a num"
                manager_count=$1
            fi
            actions=(remove_swarm_nodes)
            ;;
        -m | --count_master )
            shift
            if [ -z "$1" ]
            then
                echo "You must give a number of manager to create"
                exit 1
            else
                manager_count=$1
            fi
            ;;
        -w | --count_worker )
            shift
            if [ -z "$1" ]
            then
                echo "You must give a number of worker to create"
                exit 1
            else
                worker_count=$1
            fi
            ;;
        -h | --help )
            actions=(usage)
            exit
            ;;
        * )
            actions=(usage)
            exit 1
    esac
    shift
done

echo "started..."
let nodes=manager_count+worker_count

if [ -z "${DOCKER_MACHINE_DRIVER}" ]; then
    DOCKER_MACHINE_DRIVER=virtualbox
fi

MACHINE_OPTS="--engine-storage-driver overlay2"

function create_swarm_nodes() {

    echo "Create manager swam nodes: "
    for node in $(seq 1 ${nodes})
    do
        if [ $node -le $manager_count ]
        then
            if [ "$node" -eq "1" ];
            then
                echo "Create manager swam nodes on node-1"
                # TODO: case when a dead node with node-1 in the name exist
                inet_ip=`docker-machine ls | grep node-1 | cut -d\/ -f3 | cut -d: -f1`
                ret=`docker-machine ssh node-1 -- docker swarm init --advertise-addr ${inet_ip}`
                worker=`echo ${ret} | grep ${inet_ip} | cut -d: -f3`":2377"
                ret=`docker-machine ssh node-1 -- docker swarm join-token manager`
                manager=`echo ${ret} | grep ${inet_ip} | cut -d: -f2`":2377"
            else
                echo "Create manager swam nodes on node-$node"
                docker-machine ssh node-${node} -- ${manager}
            fi
        else
            echo "Create worker swam nodes on node-$node"
            docker-machine ssh node-${node} -- ${worker}
        fi
    done
}

function remove_swarm_nodes() {
    echo "Remove swam nodes: "
    for i in $(seq 1 ${nodes})
    do
        echo "Remove node-${i}"
        eval "$(docker-machine env )node-${i}"
        docker swarm leave --force
    done
}

for action in "${actions[@]}"
do
    ${action}
    sleep 1
done
echo "Job done..."
echo -ne '\007'

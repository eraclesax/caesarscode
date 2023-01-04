#!/usr/bin/env bash

help()
{
    echo "Usage: caesar.sh key filename [ -d | --decript  ]"
    exit 2
}

# Define short and long arguments

SHORT=d,h
LONG=decript,help

# This mechanism of getting the arguments is quite ugly, but i have to choose it for time
# saving reasons. I'm not so good with bash scripts using options and arguments :/

OPTS=$(getopt -a -n weather --options $SHORT --longoptions $LONG -- "$@")

VALID_ARGUMENTS=$# # Count of arguments that are in short or long options

# Verify that exist at least one argument (that's quite unusefool saw that the script lacks of more important
# tests... but was included in the example i read this stuff from, so \_(-_-)_/ )

if [ "$VALID_ARGUMENTS" -eq 0 ]; then
    help
fi

eval set -- "$OPTS"

# Read arguments and give error if unexpected arguments are passed
decript=0
while :
do
    case "$1" in
        -d | --decript )
        decript=1
        shift 1
        ;;
        -h | --help )
        help
        ;;
        --)
        shift;
        break
        ;;
        *)
        echo "Unexpected option: $1"
        help
        ;;
    esac
done

# read non-keywords arguments

key=$1;
file=$2;

# TODO: Add controls on mandatory keys
# TODO: Mute output for error on python version

{
    python3 caesar_function.py $key $file $decript
} || {
    python caesar_function.py $key $file $decript
}
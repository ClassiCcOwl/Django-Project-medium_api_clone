#!/usr/bin/env bash

countdown(){

    declare desc="A simple countdown."

    local second="${1}"

    local d=$(($(date +%s) + "${second}"))

    while [ "$d" -ge `date +%s` ]; do

        echo -ne "$(date -u --date @$(($d - `date +%s`)) +%H:%M:%S)\r";
        sleep 0.1

    done
}
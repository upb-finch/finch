#!/bin/bash

OPTIONS=ibdr
LONGOPTS=install,build,deploy,remove

! PARSED=$(getopt --options=$OPTIONS --longoptions=$LONGOPTS --name "$0" -- "$@")

if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
  exit 2
fi

i=0 p=0 b=0 d=0

CF_FILE="/tmp/cf_file.txt"
DEPLOYMENTS_BUCKET="saradeployments"

case "$1" in
  -d|--deploy)
    d=1
    shift
    ;;
  --)
    shift
    break
    ;;
  *)
    ;;
esac


if [[ $d -eq 1 ]]; then
  python createAPI.py
  echo deploy    
fi

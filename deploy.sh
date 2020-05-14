#!/bin/bash

OPTIONS=ibdr
LONGOPTS=install,build,deploy,remove

! PARSED=$(getopt --options=$OPTIONS --longoptions=$LONGOPTS --name "$0" -- "$@")

if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
  exit 2
fi

i=0 p=0 b=0 d=0

CF_FILE="/tmp/cf_file.txt"
DEPLOYMENTS_BUCKET="finch-bucket-upb"

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
   python db.py
   sleep 20
   python dbdata.py
   cd 'FIN - Transacciones'/
   ./deploy.sh -i
   ./deploy.sh -b
   ./deploy.sh -d
   sleep 2
   cd ..
   cd 'FIN - Anomalias'/
   ./deploy.sh -i
   ./deploy.sh -b
   ./deploy.sh -d
   sleep 2
   cd ..
   cd 'FIN - Verificaciones'/
   python dbcache.py
   sleep 20
   python dbdatacache.py
   ./deploy.sh -i
   ./deploy.sh -b
   ./deploy.sh -d
   sleep 2
   cd ..
   cd 'FIN - API'/
   ./deploy.sh -d
   sleep 3
   echo DONE!  
fi


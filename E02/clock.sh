#!/bin/bash

countdown()
(
  secs=$1
  while [ $secs -ge 0 ]
  do
    read -t 0.97 # sleep workaroud to allow for execution time
    printf "\r%02d:%02d" $(( (secs/60)%60)) $((secs%60)) &
    secs=$(( $secs - 1 ))
    wait 
  done
  echo
)

countdown 671

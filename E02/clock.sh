#!/bin/bash

countdown()
(
  secs=$1
  while [ $secs -gt 0 ]
  do
    sleep 1 &
    printf "\r%02d:%02d" $(( (secs/60)%60)) $((secs%60))
    secs=$(( $secs - 1 ))
    wait
  done
  echo
)

countdown 671

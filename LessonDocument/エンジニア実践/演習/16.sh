#!/usr/bin/env bash

input=$1

expr "$input" + 1 >&/dev/null
ret=$?
echo $?
if [ $? -lt 2 ];then
  echo "$input is a number"
else
  echo "$input is not a number"
fi
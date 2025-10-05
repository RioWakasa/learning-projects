#!/bin/bash

echo -n 引数を入力してください: 
read str

if expr "$str" : "[0-9]*$" >&/dev/null; then
    echo "number:$str"
    head -$str names.txt
else
    echo "error"
fi

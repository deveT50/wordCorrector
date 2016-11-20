#!/bin/bash

for i in {0..10000}
do
    echo $i >> /tmp/count.log
    python simple_example.py `date "+%Y%m%d" -d "$i day ago"` >> /tmp/yomiuri.log
done
cat /tmp/yomiuri.log | grep -v "<[^>]*>" | grep -v "[◇|◆|□|■|▽|▼|＊|◎|＋|※]"> /tmp/yomiuri.txt

#/bin/bash

event_group='cache-misses,cache-references,L1-dcache-load-misses,L1-dcache-loads,L1-dcache-store-misses,L1-dcache-stores'
# event_group='L1-dcache-load-misses,L1-dcache-store-misses,L1-dcache-stores,raw-ll-cache-miss-rd,raw-ll-cache-rd,raw-mem-access'
for i in $(seq 1 101)  
do
# adb shell "su -c 'cat /data/local/tmp/test_file'"
# adb shell "su -c '/data/local/tmp/simpleperf stat --duration 10 -e $event_group --interval 10 -o /data/local/tmp/cache-misses cat /data/local/tmp/test_file'";
# adb pull /data/local/tmp/cache-misses ./output/cache-misses-$i-np;
# adb shell rm /data/local/tmp/cache-misses;

adb shell "su -c '/data/local/tmp/cache_pollute.out'";
adb shell "su -c '/data/local/tmp/simpleperf stat --duration 10 -e $event_group --interval 10 -o /data/local/tmp/cache-misses cat /data/local/tmp/test_file'";
adb pull /data/local/tmp/cache-misses ./output/cache-misses-$i-pd;
adb shell rm /data/local/tmp/cache-misses;
done


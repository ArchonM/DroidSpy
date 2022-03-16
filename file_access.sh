#/bin/bash
./simpleperf stat --duration 10 -e cache-misses --interval 10 -o /data/local/tmp/cache-misses cat ./test_file
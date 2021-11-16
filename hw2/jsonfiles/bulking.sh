#!/bin/bash

for i in {0..20}; do
    curl -s -XPOST localhost:9200/js_tf/_doc/_bulk -H 'Content-Type: application/json' --data-binary "@javascript$i.json"
    curl -s -XPOST localhost:9200/js_lm/_doc/_bulk -H 'Content-Type: application/json' --data-binary "@javascript$i.json"
    curl -s -XPOST localhost:9200/js_bm/_doc/_bulk -H 'Content-Type: application/json' --data-binary "@javascript$i.json"
done
for i in {0..11}; do
    curl -s -XPOST localhost:9200/java_tf/_doc/_bulk -H 'Content-Type: application/json' --data-binary "@java$i.json"
    curl -s -XPOST localhost:9200/java_lm/_doc/_bulk -H 'Content-Type: application/json' --data-binary "@java$i.json"
    curl -s -XPOST localhost:9200/java_bm/_doc/_bulk -H 'Content-Type: application/json' --data-binary "@java$i.json"
done
for i in {0..7}; do
    curl -s -XPOST localhost:9200/py_tf/_doc/_bulk -H 'Content-Type: application/json' --data-binary "@python$i.json"
    curl -s -XPOST localhost:9200/py_lm/_doc/_bulk -H 'Content-Type: application/json' --data-binary "@python$i.json"
    curl -s -XPOST localhost:9200/py_bm/_doc/_bulk -H 'Content-Type: application/json' --data-binary "@python$i.json"
done

exit 0

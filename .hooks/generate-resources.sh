#!/bin/bash
# Generates resources.ttl from csv-files in the resources/ folder.

# Enter repository root directory
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"/..

datadoc \
    --debug \
    add \
    --context=resources/prefixes.jsonld \
    --keywords=temgo/context/keywords.yaml \
    --dump temgo-resources.ttl \
    resources/sampleholder.csv

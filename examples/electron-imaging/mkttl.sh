#!/bin/sh
# Convert electron-imaging.csv file to turtle

HERE="$(cd "$(dirname "$0")" && pwd)"

datadoc add $HERE/electron-imaging.csv --keywords $HERE/../../temgo/context/0.1/keywords.yaml -d electron-imaging.ttl

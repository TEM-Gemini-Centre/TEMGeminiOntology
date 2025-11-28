#!/bin/bash

# Enter repository root directory
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"/..

# Generate JSON-LD context and keyword documentation
keywords --input=temgo/context/0.1/keywords.yaml \
         --context=temgo/context/0.1/context.json


# Don't crash pre-commit in case the above fails on GitHub
exit 0

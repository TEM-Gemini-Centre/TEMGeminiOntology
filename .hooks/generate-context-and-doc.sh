#!/bin/bash

# Enter repository root directory
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"/..

# Generate JSON-LD context and keyword file/documentation for temgo
keywords \
    --input=temgo.ttl \
    --namespace-filter=temgo \
    --yaml=temgo/context/keywords.yaml \
    --context=temgo/context/context.json \
    --markdown=docs/keywords.md

# Generate json-ld context and keyword file for dependencies
keywords \
    --input=https://tem-gemini-centre.github.io/TEMGeminiOntology/temgo-dependencies.ttl \
    --yaml=temgo/context/keywords-dependencies.yaml \
    --context=temgo/context/context-dependencies.json


# Don't crash pre-commit in case the above fails on GitHub
exit 0

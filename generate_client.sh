#!/usr/bin/bash
PACKAGENAME=dnv_windfarmer_client
APIVERSION=3.3.0
docker run --rm -v ${PWD}/openapi-specs:/local -v ${PWD}/${PACKAGENAME}:/output openapitools/openapi-generator-cli:v7.25.0 generate -i /local/wfservices-final.json -g python -o /output --additional-properties=packageName=${PACKAGENAME},packageVersion=${APIVERSION}


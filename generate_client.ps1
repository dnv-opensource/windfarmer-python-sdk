#!/usr/bin/env pwsh
# PowerShell equivalent of generate_client.sh
$PACKAGENAME = 'dnv_windfarmer_client'
$APIVERSION  = '3.3.0'

$cwd = (Get-Location).Path

& docker run --rm -v "$cwd/openapi-specs:/local" -v "$cwd/${PACKAGENAME}:/output" `
    openapitools/openapi-generator-cli:v7.25.0 generate -i /local/wfservices-final.json -g python -o /output `
    --additional-properties="packageName=$PACKAGENAME,packageVersion=$APIVERSION"

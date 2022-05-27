#!/bin/bash
cookie=$1

curl --location --request POST 'https://api.juejin.cn/growth_api/v1/check_in?aid=2608&uuid=7039226435715155463' \
--header 'authority: api.juejin.cn' \
--header "cookie:${cookie}" \
--header 'pragma: no-cache' \
--header 'sec-ch-ua:" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Windows"' \
--header 'sec-fetch-dest: empty' \
--header 'sec-fetch-mode: cors' \
--header 'sec-fetch-site: same-site' \
--header 'Content-Type: application/json' \
--data-raw '{}'

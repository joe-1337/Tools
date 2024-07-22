#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

if [ $# -ne 2 ]; then
    echo -e "${RED}Usage: $0 <target_url> <wordlist>${NC}"
    exit 1
fi

TARGET_URL=$1
WORDLIST=$2

if [ ! -f "$WORDLIST" ]; then
    echo -e "${RED}Wordlist file not found!${NC}"
    exit 1
fi

echo -e "${BLUE}Starting VHOST Fuzzing on ${TARGET_URL} with wordlist ${WORDLIST}${NC}"

while IFS= read -r VHOST; do
    RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" -H "Host: $VHOST" "$TARGET_URL")
    
    if [ "$RESPONSE" -eq 200 ]; then
        echo -e "${GREEN}Valid VHOST found: ${VHOST} (HTTP ${RESPONSE})${NC}"
    else
        echo -e "${YELLOW}Tested: ${VHOST} (HTTP ${RESPONSE})${NC}"
    fi
done < "$WORDLIST"

echo -e "${BLUE}VHOST Fuzzing completed.${NC}"

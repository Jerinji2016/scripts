#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo -e "${RED}Usage: $0 [patch|release] [dev|stage|prod]${NC}"
    exit 1
fi

# Assign the arguments to variables
MODE=$1
ENV=$2

# Validate mode argument
if [ "$MODE" != "patch" ] && [ "$MODE" != "release" ]; then
    echo -e "${RED}Invalid mode specified. Valid options are [patch ,release]. Exiting...${NC}"
    exit 1
fi

# Validate and set the path for the env argument
ENV_FILE=""
case $ENV in
    dev)
        ENV_FILE=".env/dev.json"
        ;;
    stage)
        ENV_FILE=".env/stage.json"
        ;;
    prod)
        ENV_FILE=".env/prod.json"
        ;;
    *)
        echo -e "${RED}Invalid environment specified. Valid options are [dev, stage, prod]. Exiting...${NC}"
        exit 1
        ;;
esac

# Check if the environment file exists
if [ ! -f "$ENV_FILE" ]; then
    echo -e "${RED}Environment file $ENV_FILE does not exist, exiting...${NC}"
    exit 1
fi

# Output the selected mode and environment file
echo -e "${YELLOW}Mode selected: $MODE${NC}"
echo -e "${YELLOW}Selected environment file: $ENV_FILE${NC}"

# Clean the Flutter build
flutter clean

# Execute the shorebird command with the selected mode and environment file
shorebird $MODE android --artifact apk -- --dart-define-from-file=$ENV_FILE

echo -e "${GREEN}Build completed for mode: $MODE and environment: $ENV${NC}"

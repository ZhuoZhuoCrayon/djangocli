#!/bin/bash

export APP_DESC_YAML=".helm/Chart.yaml"
export DEV_LOG_ROOT="djangocli/docs/dev_log"
export RELEASE_LOG_ROOT="djangocli/docs/release"

current_version=$(python scripts/utils/op_yaml.py -f "$APP_DESC_YAML" --keyword-path version --op get)

echo "current_version -> $current_version"

release_log=$( python scripts/workflows/release/upgrade_release_log.py -v "$current_version" -d "$DEV_LOG_ROOT" -r "$RELEASE_LOG_ROOT" )

echo "release_log -> $release_log"



pending_release_version=$( python scripts/workflows/release/get_pending_release_version.py -d "$DEV_LOG_ROOT" )

echo "pending_release_version -> $pending_release_version"

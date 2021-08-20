export "DIFF=$( printf "deployments/production.yml\ndeployments/staging.yml" )";

# export "DIFF=$( echo "$DIFF" | sed ':a;N;$!ba;s/\n/%0A/g' )";

echo "loop"

while read -r path; do
    if [[ $path == *"deployments/staging.yml"* ]]; then
        echo "stagin is here!"
    fi
    if [[ $path == *"deployments/production.yml"* ]]; then
        echo "production is here!"
    fi
done <<< "$DIFF"
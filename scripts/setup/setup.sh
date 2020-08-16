SCRIPT_PATH=$(dirname $0)

cd $SCRIPT_PATH
if hash python3 2>/dev/null; then
    python3 -m venv venv
else
    if hash python 2>/dev/null; then
       PYTHON_VERSION=$(python --version  | awk \'{print $2}\')
       if [ "$PYTHON_VERSION" -lt "3.0.0" ]; then
            echo "Your Python version is too old, please update your python version"
            exit 1
        else
            python -m venv venv
        fi
    else
        echo "It doesn't look like you have Python installed on your machine."
    fi
fi

if hash jq 2>/dev/null; then
    echo "What's your Reddit client ID?: "
    read client_id
    echo "What's your Reddit client secret?: "
    read client_secret
    echo "What's your Reddit user agent?: "
    read user_agent
    echo "What's your Reddit username?"
    read reddit_username
    echo "What's your Reddit password?"
    read reddit_password
    echo "What's your Discord bot token?"
    read discord_bot_token
    jq -n --arg CLIENT_ID  "$client_id" \
    --arg CLIENT_SECRET  "$client_secret" \
    --arg USER_AGENT  "$user_agent" \
    --arg REDDIT_USERNAME  "$reddit_username" \
    --arg REDDIT_PASSWORD  "$reddit_password" \
    --arg DISCORD_TOKEN  "$discord_bot_token" '{redditClientID: $CLIENT_ID, redditClientSecret: $CLIENT_SECRET, redditUserAgent: $USER_AGENT, redditUser: $REDDIT_USERNAME, redditPassword: $REDDIT_PASSWORD, discordToken: $DISCORD_TOKEN}' > config.json
else
    echo "You need jq to run this script, please install jq: https://stedolan.github.io/jq/"
    exit 1
fi
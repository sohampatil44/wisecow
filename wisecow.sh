#!/usr/bin/env bash

SRVPORT=4499

# check prerequisites
prerequisites() {
    command -v /usr/games/cowsay >/dev/null 2>&1 || { echo "cowsay missing"; exit 1; }
    command -v /usr/games/fortune >/dev/null 2>&1 || { echo "fortune missing"; exit 1; }
    command -v nc >/dev/null 2>&1 || { echo "nc missing"; exit 1; }
}

main() {
    prerequisites
    echo "Wisdom served on port=$SRVPORT..."

    # Bind to 0.0.0.0 so NodePort can reach it
    while true; do
        /bin/bash -c "while true; do echo -e 'HTTP/1.1 200 OK\n\n$(/usr/games/fortune | /usr/games/cowsay)' | nc -l -p $SRVPORT -q 1; done" &
        wait
    done
}

main

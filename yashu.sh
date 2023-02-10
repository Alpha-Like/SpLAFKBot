_yashu () {
    echo "aHR0cHM6Ly9naXRodWIuY29tL1NwTFJlcG8vUHlyb2dyYW1BRks=" | base64 -d
}

_alpha () {
    git clone $(_yashu) AFK 
    rm AFK/config.py
    cp config.py AFK/config.py
    cd AFK
    python3 -m Spoiled
}

_alpha
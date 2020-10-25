
1. Create virtual env.

    python3 -m venv venv

2. Activate virtual env.

    source venv/bin/activate

3. Install discord.py.

    pip install discord.py

3. Setup your environmental variables

    Generate your app token from here: https://discord.com/developers/applications/

    export DISCORD_APP_TOKEN="<token>"

4. Run program:

    python3 reply-bot.py

5. To Exit virtual environment:
   
    deactivate

6. Rerunning
    cd/foo/foo
    source venv/bin/activate
    export DISCORD_APP_TOKEN="<token>"
    python3 reply-bot.py

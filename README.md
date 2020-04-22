# Discordbot
Generic discord bot to handle certain things.... very basic and totally WIP


## Dependencies
Bot runs on python3 make sure to install discordpy and dotenv with pip3
```
pip3 install discordpy
pip3 install dotenv
```

## Usage
Specify Discord bot token in `.env` file - Create your bot on Discord https://discordapp.com/developers/applications

Run the bot once token has been updated and you have invited it to the server you need it on and changed the script up for your identifiers.
`python3 bot.py`

## Optional shit

Make it into a service so you can cronjob it to restart every once in a while.

Example: `/etc/systemd/system/discordbot.service`
Restart service with `service discordbot restart` for example etc...
```bash
[Unit]
Description=Discord bot
After=network.target
StartLimitIntervalSec=0
[Service]
Type=simple
Restart=always
RestartSec=1
User=root
ExecStart=/usr/bin/python3 /root/Discordbot/bot.py

[Install]
WantedBy=multi-user.target
```

Read the docs to customize even more: https://discordpy.readthedocs.io/en/latest/

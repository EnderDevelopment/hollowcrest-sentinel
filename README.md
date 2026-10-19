# Hollowcrest Sentinel

Hollowcrest Sentinel is a Discord security and moderation bot designed for Hollowcrest SMP. It provides configurable staff alerts for suspicious activity and detailed logging for member and player actions. The bot uses Discord slash commands for easy configuration and management, and it stores configuration persistently using SQLite.

## Install

1. Clone the repository: `git clone https://github.com/yourusername/hollowcrest-sentinel.git`
2. Navigate to the project directory: `cd hollowcrest-sentinel`
3. Install Python 3.10 or higher.
4. Install the required dependencies: `pip install -r requirements.txt`
5. Rename `.env.example` to `.env` and fill in your configuration.
6. Run the bot: `python src/bot.py`

## Use

1. Invite the bot to your Discord server.
2. Use the `/setup` slash command to configure the bot.
3. Use the `/logs set` and `/alerts set` commands to configure the logging and alert channels.
4. Use the `/alerts toggle` and `/alerts threshold` commands to enable or disable specific alerts and set thresholds.
5. Monitor the configured channels for staff alerts and logs.

---

More Minecraft plugin projects by EnderDevelopment: https://github.com/EnderDevelopment

Project page: https://dash.enderdevelopment.com/community/637c6a66-9844-450a-b9a3-96eeed591711?utm_source=github&utm_medium=readme&utm_campaign=auto_publish&utm_content=637c6a66-9844-450a-b9a3-96eeed591711

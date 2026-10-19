import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import sqlite3

# Load environment variables
load_dotenv()

# Initialize bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Database setup
def init_db():
    conn = sqlite3.connect(os.getenv('DATABASE_PATH'))
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        details TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        action TEXT NOT NULL,
        details TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

# Bot events
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    init_db()

# Staff alerts
@bot.command()
@commands.has_permissions(administrator=True)
async def alert(ctx, *, message: str):
    staff_channel = bot.get_channel(int(os.getenv('STAFF_ALERTS_CHANNEL')))
    if staff_channel:
        await staff_channel.send(f'🔒・staff-alerts: {message}')
    else:
        await ctx.send('Staff alerts channel not found.')

# Run the bot
if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))
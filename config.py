import os
from os import environ

TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "756596:AAF")
APP_ID = int(os.environ.get("APP_ID", "2355"))
API_HASH = os.environ.get("API_HASH", "4vsavkjahvsdhk")
OWNER_ID = int(os.environ.get("OWNER_ID", "5741918628"))
PORT = os.environ.get("PORT", "8080")
DB_URL = os.environ.get("DB_URI", "mongodb+srv://odb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Rex_sequencebott")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "S_QV_Sbot")
FSUB_PIC = os.environ.get("FSUB_PIC", "https://ibb.co/FL66q5G9")
START_PIC =os.environ.get("START_PIC", "https://ibb.co/FL66q5G9")
START_MSG = os.environ.get("START_MSG", "<b>Bᴀᴋᴀᴀᴀ...!!!{mention}</b> \n<blockquote><b><i>Iᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ sᴇǫᴜᴇɴᴄᴇ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs. I ᴄᴀɴ sᴇǫᴜᴇɴᴄᴇ ʏᴏᴜʀ ғɪʟᴇs ᴇᴀsɪʟʏ ɪɴ ᴀ sᴇᴄᴏɴᴅ...!!</i></b></blockquote>")
ABOUT_TXT = os.environ.get("ABOUT_MESSAGE", "<i><b><blockquote>◈ Bᴏᴛ: Kᴀᴋᴀsʜɪ Sᴇǫᴜᴇɴᴄᴇʀ\n◈ Vᴇʀsɪᴏɴ: 2.0.0\n◈ Lɪʙ: Pyrofork\n◈ Dʙ: MongoDB\n\n◈ Cʀᴇᴀᴛᴏʀ: <a href=https://t.me/fire_blood_demon>Blood Demon</a>\n◈ Dᴇᴠ: <a href=https://t.me/fire_blood_demon>Blood Demon</a>\n◈ Sᴜᴘᴘᴏʀᴛ: <a href=https://t.me/fire_blood_demon>Cʟɪᴄᴋ Hᴇʀᴇ</a></blockquote></b></i>")
HELP_TXT =  os.environ.get("HELP_MESSAGE", "⁉️ Hᴇʏ {mention}\n\n📁 Sᴇǫᴜᴇɴᴄᴇ:\n/ssequence — Sᴛᴀʀᴛ sᴇssɪᴏɴ\n/esequence — Eɴᴅ & sᴇɴᴅ ғɪʟᴇs\n/mode — Cʜᴀɴɢᴇ sᴏʀᴛ ᴍᴏᴅᴇ\n/cancel — Cᴀɴᴄᴇʟ sᴇssɪᴏɴ\n\n📤 Dᴜᴍᴘ:\n/add_dump — Lɪɴᴋ ᴅᴜᴍᴘ ᴄʜᴀɴɴᴇʟ\n/rem_dump — Rᴇᴍᴏᴠᴇ ᴅᴜᴍᴘ ᴄʜᴀɴɴᴇʟ\n/dump_info — Vɪᴇᴡ ᴅᴜᴍᴘ ɪɴғᴏ\n\n🏆 /leaderboard — Tᴏᴘ 10 ᴜsᴇʀs\n\n💬 @naruto0927")
TG_BOT_WORKERS = 10000
FSUB_LINK_EXPIRY = 300
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-10654657458"))
LOG_FILE_NAME = "links-sharingbot.txt"
SEASON_PATTERN = r'[Ss](\d{1,2})'
EPISODE_PATTERN = r'[Ee][Pp]?(\d{1,3})'
QUALITY_PATTERN = r'(480p|720p|1080p|HDRip|2k|4k)'

TEMP_DIR = "temp_files"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

SORTING_MODES = {
  'Quality': lambda x: (x['quality_order']),
  'All': lambda x: (x['season'], x['episode'], x['quality_order']),
  'Episode': lambda x: (x['episode']),
  'Season': lambda x: (x['season'])
}
QUALITY_ORDER = {
  '480p': 1,
  '720p': 2,
  '1080p': 3,
  'HDRip': 4,
  '2k': 5,
  '4k': 6,
  'unknown': 7
}

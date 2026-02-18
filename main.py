import schedule
import time
import requests
import os
from datetime import datetime

# ── CONFIG — set these as environment variables in Railway ───────────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise ValueError("BOT_TOKEN and CHAT_ID must be set as environment variables.")
# ────────────────────────────────────────────────────────────────────────────


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        r = requests.post(url, json=payload, timeout=10)
        if r.status_code == 200:
            print(f"[{datetime.now().strftime('%H:%M')}] Sent: {text[:50]}...")
        else:
            print(f"[{datetime.now().strftime('%H:%M')}]Failed: {r.text}")
    except Exception as e:
        print(f"Error sending message: {e}")


# ── MESSAGES ─────────────────────────────────────────────────────────────────


def workday_reminder():
    send_message(
        ":)*LeetCode – Work Day Check-in*\n\n"
        "Even 1 problem counts today. Pick an easy from your Week list and knock it out.\n\n"
        ":3 No pressure — just keep the streak alive."
    )


def full_session_morning():
    send_message(
        ":0*LeetCode – Full Session (Before 2PM)*\n\n"
        "You've got time before 2. Here's the plan:\n"
        "• 45 min → new problem, full process\n"
        "• 30 min → review your solutions + read top answers\n"
        "• 15 min → write down the pattern you used\n\n"
        "Let's get it :3"
    )


def full_session_evening():
    send_message(
        ":3*LeetCode – Full Session (After 5PM)*\n\n"
        "Session time! Here's the plan:\n"
        "• 45 min → new problem, full process\n"
        "• 30 min → review your solutions + read top answers\n"
        "• 15 min → write down the pattern you used\n\n"
        "You got this Jade 🧠"
    )


def weekend_reminder():
    send_message(
        ":3 *LeetCode – Weekend Session*\n\n"
        "Afternoon grind time. Aim for 2-3 problems today.\n"
        "Try at least one Medium and review anything shaky from the week.\n\n"
        "Consistency > intensity 🔥"
    )


def sunday_reminder():
    send_message(
        "😌 *LeetCode – Light Sunday Session*\n\n"
        "Low pressure today — 1 or 2 problems max.\n"
        "Focus on anything that felt shaky this week and finish strong.\n\n"
        "New week starts tomorrow 🚀"
    )


# ── SCHEDULE ─────────────────────────────────────────────────────────────────
schedule.every().monday.at("10:00").do(workday_reminder)
schedule.every().wednesday.at("10:00").do(workday_reminder)
schedule.every().friday.at("10:00").do(workday_reminder)

schedule.every().tuesday.at("10:00").do(full_session_morning)
schedule.every().tuesday.at("17:00").do(full_session_evening)
schedule.every().thursday.at("10:00").do(full_session_morning)
schedule.every().thursday.at("17:00").do(full_session_evening)

schedule.every().saturday.at("13:00").do(weekend_reminder)
schedule.every().sunday.at("13:00").do(sunday_reminder)

# ── RUN ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("LeetCode reminder bot is running!")
    send_message(
        "🤖 *LeetCode Reminder Bot is live!*\n\nYou'll get reminders based on your study schedule. Good luck this week Jade 💪"
    )

    while True:
        schedule.run_pending()
        time.sleep(30)

import tweepy
import random
import os

# المفاتيح
API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# قائمة التغريدات
tweets = [
    "🔮 تبحث عن مفسر أحلام موثوق وذو خبرة؟ الشيخ أبو ليان يقدم لك تحليلاً شرعياً ودقيقاً لرؤاك وأحلامك ✨\n📲 wa.me/+966536329403",
    "🌙 مفسر أحلام شرعي ومعروف بخبرته الطويلة. تواصل مع الشيخ أبو ليان ✅\n📲 wa.me/+966536329403",
    "✨ كثير يسألون عن مفسر أحلام موثوق، الشيخ أبو ليان يساعدك على فهم رؤاك بدقة وبطريقة شرعية 🌟\n📲 wa.me/+966536329403",
    "🔮 هل رأيت رؤيا وتريد تفسيرها؟ الشيخ أبو ليان، مفسر أحلام بخبرة سنين طويلة، يفسر لك بدقة ووضوح ✅\n📲 wa.me/+966536329403",
    "🌟 تبحث عن تفسير شرعي لرؤاك؟ مفسر الأحلام الشيخ أبو ليان يقدم لك أجوبة واضحة وموثوقة ✨\n📲 wa.me/+966536329403",
    "💫 كثير من الناس يثقون بمفسر الأحلام الشيخ أبو ليان لأنه يفسر الرؤى بالشرع والخبرة 🌙\n📲 wa.me/+966536329403",
    "🌙 عندك رؤيا محيرة؟ مفسر الأحلام الشيخ أبو ليان يفسرها لك بسهولة ووضوح ✨\n📲 wa.me/+966536329403",
    "🔮 لا تبحث كثيراً، مفسر الأحلام الموثوق أبو ليان يشرح لك رموز رؤاك بدقة عالية وشرعية ✅\n📲 wa.me/+966536329403",
    "🌟 إذا أردت تفسير رؤياك بطريقة شرعية صحيحة، مفسر الأحلام الشيخ أبو ليان هو الخيار الأفضل ✨\n📲 wa.me/+966536329403",
    "✨ آلاف الأشخاص يسألون عن مفسر أحلام موثوق، الشيخ أبو ليان يقدم التفسير بخبرة وصدق 🌙\n📲 wa.me/+966536329403"
]

# سجل التغريدات المنشورة
log_file = "log.txt"
if os.path.exists(log_file):
    with open(log_file, "r", encoding="utf-8") as f:
        posted = [line.strip() for line in f.readlines()]
else:
    posted = []

# التغريدات المتاحة للنشر
available = [t for t in tweets if t not in posted]

if not available:
    posted = []
    available = tweets.copy()

tweet = random.choice(available)

try:
    response = client.create_tweet(text=tweet)
    print("✅ تم النشر:", response.data["id"])
    
    # تحديث السجل
    posted.append(tweet)
    with open(log_file, "w", encoding="utf-8") as f:
        for t in posted:
            f.write(t + "\n")
except Exception as e:
    print("❌ خطأ في النشر:", e)

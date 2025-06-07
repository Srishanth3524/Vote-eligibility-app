import streamlit as st
import re
import csv
import os

# ----- Language Dictionary -----
translations = {
    "ENGLISH": {
        "title": "🗳️ Vote Eligibility Checker",
        "name": "Enter your name:",
        "age": "Enter your age:",
        "voter_id": "Enter your Voter ID:",
        "button": "Check Eligibility",
        "eligible": "✅ {name}, you are eligible to vote! 🎉",
        "not_eligible": "❌ Sorry {name}, you are not eligible to vote yet.",
        "invalid_id": "⚠️ Invalid Voter ID. It must be 10-12 characters, letters and numbers only.",
        "missing_name": "⚠️ Please enter your name.",
        "footer": "Built with ❤️ using Streamlit",
        "language": "Choose Language:"
    },
    "HINDI": {
        "title": "🗳️ मतदान पात्रता चेकर",
        "name": "अपना नाम दर्ज करें:",
        "age": "अपनी उम्र दर्ज करें:",
        "voter_id": "मतदाता पहचान पत्र दर्ज करें:",
        "button": "पात्रता जाँचें",
        "eligible": "✅ {name}, आप मतदान करने के पात्र हैं! 🎉",
        "not_eligible": "❌ क्षमा करें {name}, आप अभी मतदान के पात्र नहीं हैं।",
        "invalid_id": "⚠️ अमान्य मतदाता ID। इसमें 10-12 अक्षर और संख्याएँ होनी चाहिए।",
        "missing_name": "⚠️ कृपया अपना नाम दर्ज करें।",
        "footer": "Streamlit ❤️ से बनाया गया",
        "language": "भाषा चुनें:"
    },
    "TELUGU": {
        "title": "🗳️ ఓటింగ్ అర్హత తనిఖీ",
        "name": "మీ పేరు నమోదు చేయండి:",
        "age": "మీ వయస్సు నమోదు చేయండి:",
        "voter_id": "ఓటర్ ID నమోదు చేయండి:",
        "button": "అర్హత తనిఖీ చేయండి",
        "eligible": "✅ {name}, మీరు ఓటు వేయడానికి అర్హులు! 🎉",
        "not_eligible": "❌ క్షమించండి {name}, మీరు ఓటు వేయడానికి అర్హులు కాదు.",
        "invalid_id": "⚠️ చెల్లని ఓటర్ ID. 10-12 అక్షరాలు/సంఖ్యలు ఉండాలి.",
        "missing_name": "⚠️ దయచేసి మీ పేరు నమోదు చేయండి.",
        "footer": "Streamlit ❤️ తో రూపొందించబడింది",
        "language": "భాషను ఎంచుకోండి:"
    }
}

# ----- Choose Language -----
lang = st.sidebar.selectbox("🌐 Choose Language / भाषा चुनें / భాషను ఎంచుకోండి", ["ENGLISH", "HINDI", "TELUGU"])
t = translations[lang]

# ----- App UI -----
st.title(t["title"])
name = st.text_input(t["name"])
age = st.number_input(t["age"], min_value=0, max_value=120, step=1)
voter_id = st.text_input(t["voter_id"])

# ----- Check Button -----
if st.button(t["button"]):
    if not name:
        st.warning(t["missing_name"])
    elif not re.fullmatch(r"[A-Za-z0-9]{10,12}", voter_id):
        st.warning(t["invalid_id"])
    elif age >= 18:
        st.success(t["eligible"].format(name=name))
        status = "Eligible"
    else:
        st.error(t["not_eligible"].format(name=name))
        status = "Not Eligible"

    # Save to file
    if name and re.fullmatch(r"[A-Za-z0-9]{10,12}", voter_id):
        file_exists = os.path.exists("vote_log.csv")
        with open("vote_log.csv", "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Name", "Age", "VoterID", "Status"])
            writer.writerow([name, age, voter_id, status])

# Footer
st.markdown("---")
st.caption(t["footer"])

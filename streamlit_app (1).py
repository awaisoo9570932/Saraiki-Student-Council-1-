from pathlib import Path
from html import escape
import json
import re
import streamlit as st

ROOT = Path(__file__).parent
D = json.loads((ROOT / "council_data.json").read_text(encoding="utf-8"))
st.set_page_config(page_title=D["name"], page_icon="S", layout="wide")
st.html("<style>" + (ROOT / "styles.css").read_text() + "</style>")

def card(tag, title, body):
    st.html(f'<article class="card"><span class="tag">{escape(str(tag))}</span><h3>{escape(str(title))}</h3><p>{escape(str(body))}</p></article>')

def title(label, text):
    st.caption(label)
    st.title(text)

def contacts():
    selected = [m for role in ["Chairman", "President", "General secretary"] for m in D["members"] if m["role"] == role]
    return "\n".join(f"- {m['role']}: {m['name']}" + (f" — {m['public_phone']}" if m.get('public_phone') else " — public number abhi add nahi hua") for m in selected)

PURPOSE = [
    ("STUDENT SUPPORT", "Problem solving", "Students ke academic aur campus concerns ko samajhna aur relevant university office tak guide karna. Council university decisions ko override nahi karti."),
    ("ADMISSIONS", "Admission guidance", "Application process, available information aur scholarship queries par guidance; final admission decision university ka hai."),
    ("ACADEMICS", "Exams & study support", "Study-circle coordination aur official exam notices samajhne mein madad. Date sheets, grades aur results relevant university office se confirm honge."),
    ("COMMUNITY", "Meetings & coordination", "Council meetings, student suggestions aur cultural activities ke liye coordination. Confirmed schedules Meetings section mein publish honge."),
]

def answer(q):
    t = re.sub(r"[^\w%]+", " ", q.lower()).strip()
    has = lambda words: any(w in t for w in words)
    if has(["scholar", "5%", "15%", "5 15", "وظیف", "سکالر"]):
        return D["scholarship_note"] + "\n\nGuidance ke liye:\n" + contacts() + "\n\nOfficial policy: " + D["official_scholarship_url"]
    if has(["admission", "admision", "admisson", "dakhla", "داخل"]):
        return "Admission process mein council se guidance le sakte hain. Admission guaranteed nahi; final decision university ka hai.\n\nIn members se rabta karein:\n" + contacts() + "\n\n" + D["scholarship_note"]
    if has(["founder", "karar", "بانی"]):
        return "Council ke diye hue record ke mutabiq founder " + D["founder"] + " hain."
    if has(["2024", "establish", "kab bani", "kab bani thi", "bunyad", "قیام"]):
        return "Council ke diye hue record ke mutabiq council 2024 mein bani thi."
    if has(["campus", "university", "جامعہ"]):
        return "Di gayi council information ke mutabiq ye " + D["campus"] + " ki council hai. Ye student-council portal hai; university ka official admissions portal nahi."
    if has(["donat", "fund", "chanda", "عطیہ"]):
        return "Donation collection abhi active nahi. Verified recipient, council authorization, use-of-funds aur reporting process confirm hone ke baad details publish hongi. Finance head: Muhammad Zain. Donation totals ke verified records abhi available nahi."
    if has(["meeting", "اجلاس"]):
        return "\n".join(f"{x['title']} — {x['date']} — {x['venue']}" for x in D["meetings"]) if D["meetings"] else "Abhi koi confirmed upcoming meeting publish nahi hui. Date, time aur venue confirm hone par add honge."
    if has(["kitna admission", "kitne admission", "kitna kaam", "achievement", "impact", "کارکردگی"]):
        return "Council ke admissions aur completed projects ke verified figures abhi provide nahi hue. Hum andazay ya sample numbers ko real achievements ke taur par nahi dikhate."
    if has(["exam", "paper", "result", "date sheet", "datesheet", "امتحان"]):
        return "Council exams aur study guidance mein coordination kar sakti hai. Study circle head: Maaz Ali. Confirmed exam dates aur results relevant university office se verify karein; is portal mein abhi official date sheet nahi."
    if has(["purpose", "maqsad", "problem", "solution", "مقصد"]):
        return "Council ka proposed support scope: student problems par guidance, admission information, exams/study-circle support, meetings aur community coordination. In services ki current availability council se confirm karein."
    if has(["members", "team", "ارکان"]):
        return "\n".join(f"- {m['name']} — {m['role']}" for m in D["members"])
    for m in sorted(D["members"], key=lambda x: len(x["role"]), reverse=True):
        if m["role"].lower() in t or m["name"].lower() in t:
            return f"{m['role']}: {m['name']}" + (f". Public contact: {m['public_phone']}" if m.get('public_phone') else ". Public contact number abhi add nahi hua.")
    if t in ["hi", "hello", "salam", "assalam o alaikum", "السلام علیکم"]:
        return "Assalam o alaikum! Main Council Assistant hoon. Founder, members, admission guidance, scholarship, exams, meetings aur donations ke bare mein poochhein."
    return "Is sawal ka verified jawab meri council information mein abhi nahi hai. Main naamaloom baat par andaza nahi lagaunga. Admission aur council guidance ke liye:\n" + contacts()

with st.sidebar:
    st.html('<div class="brand"><b>S</b><div>SARAKI<span>STUDENTS COUNCIL</span></div></div>')
    page = st.radio("Explore", ["Overview", "Purpose", "The Council", "Admission Guidance", "Meetings & Notices", "Donations & Impact", "Council Assistant"], label_visibility="collapsed")
    st.divider()
    st.caption("Student-council portal / Not an official university admissions portal")

st.html('<div class="topbar">SSC / COMMUNITY PORTAL <span>GOLD CAMPUS</span></div>')
if page == "Overview":
    st.html('<section class="hero"><div class="ring"></div><div class="shape"></div><small>YOUR COMMUNITY. YOUR NEXT CHAPTER.</small><h1>One council.<br>Many voices.<br><em>Shared possibilities.</em></h1><p>Saraki Students Council · Superior University Gold Campus</p><span>ESTABLISHED 2024 / COUNCIL-PROVIDED INFORMATION</span></section>')
    cols = st.columns(3)
    for col, tag, heading, text in zip(cols, ["FOUNDER", "ESTABLISHED", "LEADERSHIP"], [D["founder"], str(D["established"]), str(len(D["members"])) + " members"], ["Council-provided information", D["campus"], "Council roster supplied by the app owner"]):
        with col:
            card(tag, heading, text)
    st.subheader("A community built around students")
    for col, content in zip(st.columns(2), PURPOSE[:2]):
        with col:
            card(*content)
    st.info("Admission help chahiye? Admission Guidance ya Council Assistant kholein.")
    st.caption("Founder, campus, establishment year aur members ki details council owner ne provide ki hain; independent verification nahi ki gayi.")

elif page == "Purpose":
    title("WHY WE EXIST", "Purpose of this council")
    st.write("Students ko guidance, representation aur community connection ke liye ek organized platform dena.")
    for item in PURPOSE:
        card(*item)
    st.warning(D["scholarship_note"])
    st.caption("Ye purpose statements requested scope ko describe karti hain; completed projects ya guaranteed services ka claim nahi.")

elif page == "The Council":
    title("PEOPLE BEHIND THE PURPOSE", "Meet the council")
    card("FOUNDER", D["founder"], "Established 2024 — council-provided information")
    query = st.text_input("Search by name or role").strip().lower()
    filtered = [m for m in D["members"] if query in (m["name"] + " " + m["role"]).lower()]
    for start in range(0, len(filtered), 2):
        for col, m in zip(st.columns(2), filtered[start:start+2]):
            with col:
                card(m["role"], m["name"], m.get("public_phone") or "Public contact not yet provided")
    if not filtered:
        st.info("No matching member.")

elif page == "Admission Guidance":
    title("GUIDANCE, NOT GUARANTEES", "Your next chapter starts here.")
    st.write("Application aur scholarship guidance ke liye in council representatives se rabta karein:")
    st.markdown(contacts())
    st.warning(D["scholarship_note"])
    st.link_button("Official university admissions", D["official_admissions_url"])
    st.link_button("Official scholarship policy", D["official_scholarship_url"])
    st.caption("University ki latest policy aur written offer ko priority dein. Council referral se admission ya scholarship automatically approve nahi hoti.")

elif page == "Meetings & Notices":
    title("STAY IN THE LOOP", "Meetings & announcements")
    st.subheader("Upcoming meetings")
    if not D["meetings"]:
        st.info("No confirmed meeting published. Schedule pending council confirmation.")
    for x in D["meetings"]:
        card(x["date"], x["title"], x["venue"])
    st.subheader("Notices")
    if not D["notices"]:
        st.info("No approved notice has been supplied yet.")
    for x in D["notices"]:
        card(x["date"], x["title"], x["text"])

elif page == "Donations & Impact":
    title("TRUST THROUGH TRANSPARENCY", "Donations & council impact")
    st.info("Donation collection is not active. No payment account or collection link has been supplied or verified.")
    card("FINANCE CONTACT", "Muhammad Zain — Finance head", "Public contact details pending permission and verification.")
    st.subheader("Verified record status")
    for label in ["Admissions supported", "Completed council projects", "Donations received", "Funds used"]:
        card("AWAITING RECORDS", label, "Verified figure not provided — this does not mean zero.")
    st.subheader("Activity records")
    if not D["impact_records"]:
        st.caption("No verified activity records supplied yet.")
    else:
        st.dataframe(D["impact_records"], use_container_width=True)
    st.subheader("Donation ledger")
    if not D["donation_records"]:
        st.caption("No verified donation records supplied yet.")
    else:
        st.dataframe(D["donation_records"], use_container_width=True)
    st.subheader("Proposed reporting categories")
    st.write("Admission guidance sessions; exam/study support; cultural activities; student welfare. These are reporting categories, not claims of completed work.")
    st.caption("Before collection: approve recipient and purpose, verify account ownership, define receipts/reporting and publish privacy/refund rules. Do not publish donor names or student details without permission.")

else:
    title("COUNCIL ASSISTANT", "Ask your council.")
    st.caption("Rule-based information assistant, not a general AI model. Answers use the supplied council data. No admission or scholarship guarantee.")
    st.caption("Try: Founder kaun hai? / Maine admission lena hai / Scholarship? / General secretary kaun hai? / Upcoming meeting?")
    if "chat" not in st.session_state:
        st.session_state.chat = [{"role": "assistant", "content": "Assalam o alaikum! Council, admission guidance, members, meetings ya scholarship ke bare mein poochhein. Personal ya sensitive data share na karein."}]
    if st.button("Clear chat"):
        del st.session_state["chat"]
        st.rerun()
    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    if q := st.chat_input("Council se related sawal likhein...", max_chars=1000):
        st.session_state.chat.append({"role": "user", "content": q})
        st.session_state.chat.append({"role": "assistant", "content": answer(q)})
        st.rerun()
    st.caption("Chat current browser session tak rehti hai. Permanent inbox ya database included nahi. Hosting provider ke technical logs alag ho sakte hain.")

st.html('<footer>SARAKI STUDENTS COUNCIL <span>Community first. Always.</span><p>Council-supplied information / Verify admission and scholarship terms directly with the university.</p></footer>')

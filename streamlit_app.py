import streamlit as st
import calendar
from datetime import date

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="India CA Calendar 2026–2099",
    page_icon="📅",
    layout="wide"
)

# ---------------- DARK UI ----------------
st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}
.block-container {
    padding-top: 1.2rem;
}
.calendar-cell {
    background: #0d0d0d;
    border: 1px solid #222;
    border-radius: 14px;
    padding: 12px;
    height: 130px;
}
.day-num {
    font-size: 20px;
    font-weight: 700;
}
.event {
    font-size: 13px;
    color: #00ffcc;
}
.weekday {
    text-align: center;
    font-weight: 700;
    color: #aaaaaa;
}
button {
    background-color: #000 !important;
    color: #fff !important;
    border: 1px solid #555 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "year" not in st.session_state:
    st.session_state.year = 2026
if "month" not in st.session_state:
    st.session_state.month = 1

# ---------------- FESTIVALS ----------------
def festivals(year):
    return {
        date(year,1,1): "🎆 New Year",
        date(year,1,26): "🇮🇳 Republic Day",
        date(year,3,25): "🎨 Holi",
        date(year,4,14): "📘 Ambedkar Jayanti",
        date(year,8,15): "🇮🇳 Independence Day",
        date(year,10,2): "🕊 Gandhi Jayanti",
        date(year,10,20): "🏹 Dussehra",
        date(year,11,1): "🪔 Diwali",
        date(year,12,25): "🎄 Christmas"
    }

# ---------------- CA DUE DATES ----------------
CA_DUE_DATES = [
    ("7", "GST – GSTR-1"),
    ("11", "GST – GSTR-1 (QRMP)"),
    ("15", "PF / ESI Payment"),
    ("20", "GST – GSTR-3B"),
    ("30", "TDS/TCS Payment"),
    ("31", "Income Tax / Audit / ITR (as applicable)")
]

# ---------------- HEADER ----------------
st.title("📅 India CA Compliance Calendar")
st.caption("Festivals • Government Holidays • Tax & Statutory Due Dates")

# ---------------- MONTH NAV ----------------
c1, c2, c3 = st.columns([1,2,1])
with c1:
    if st.button("⬅️ Previous"):
        st.session_state.month -= 1
        if st.session_state.month == 0:
            st.session_state.month = 12
            st.session_state.year -= 1

with c2:
    st.markdown(
        f"<h2 style='text-align:center'>{calendar.month_name[st.session_state.month]} {st.session_state.year}</h2>",
        unsafe_allow_html=True
    )

with c3:
    if st.button("Next ➡️"):
        st.session_state.month += 1
        if st.session_state.month == 13:
            st.session_state.month = 1
            st.session_state.year += 1

# ---------------- CALENDAR ----------------
cal = calendar.Calendar(calendar.SUNDAY)
fest = festivals(st.session_state.year)

weekdays = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
cols = st.columns(7)
for i,w in enumerate(weekdays):
    cols[i].markdown(f"<div class='weekday'>{w}</div>", unsafe_allow_html=True)

for week in cal.monthdatescalendar(st.session_state.year, st.session_state.month):
    cols = st.columns(7)
    for i,day in enumerate(week):
        if day.month == st.session_state.month:
            event = fest.get(day,"")
            cols[i].markdown(
                f"""
                <div class='calendar-cell'>
                    <div class='day-num'>{day.day}</div>
                    <div class='event'>{event}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            cols[i].markdown("<div class='calendar-cell'></div>", unsafe_allow_html=True)

# ---------------- FESTIVALS LIST ----------------
st.divider()
st.subheader("🎉 Government Holidays & Festivals")

for d, name in fest.items():
    st.markdown(f"• **{d.strftime('%d %B %Y')}** — {name}")

# ---------------- CA DUE DATES ----------------
st.divider()
st.subheader("🧾 CA / Tax / Statutory Due Dates (Every Month)")

for d, work in CA_DUE_DATES:
    st.markdown(f"• **{d}** — {work}")

# ---------------- FOOTER ----------------
st.caption("⚫ Ultra-Dark UI • ⚪ White Typography • 🇮🇳 CA-Grade Compliance Tool")

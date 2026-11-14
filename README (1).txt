SARAKI COUNCIL — CONTENT AND ASSISTANT UPDATE

Upload all ZIP contents, not the ZIP itself, to your repository root.
Replace streamlit_app.py, styles.css and requirements.txt. Add council_data.json.
Keep config.toml inside .streamlit/ (create .streamlit/config.toml on GitHub).
Deploy using streamlit_app.py. Reboot an existing deployment if needed.

CONTENT
Founder, establishment year, campus and 18 member entries are owner-supplied,
not independently verified. Confirm spelling, consent and branding before publishing.
No phone numbers were supplied. Add only consented public council contact numbers
in council_data.json, in the relevant member's public_phone field.

ASSISTANT
Rule-based FAQ, not a generative AI model. No API key needed.
Recognizes selected Roman Urdu/English and some Urdu keywords; not every phrasing.
Unknown questions receive a transparent fallback. Chat session is temporary.
It cannot check applications, approve scholarships or send messages.

SCHOLARSHIP
Council-specific 5–15% claim is explicitly marked unconfirmed; the basis of the
percentage is also unknown. Official public policy requires eligibility/assessment.
Official sources checked:
https://www.superior.edu.pk/admissions-2/scholarships/
https://www.superior.edu.pk/admissions-2/
Do not change this into an admission/scholarship guarantee without valid authority.

DONATIONS AND IMPACT
No payments are collected. No achievements, admission counts or donations invented.
Empty records mean not supplied, not zero. Supply verified, privacy-safe records.
meetings entries: title, date, venue.
notices entries: title, date, text.
impact_records/donation_records: add only approved public reporting fields.
Never include confidential student, donor, CNIC, account credentials or medical data.

LIMITATIONS
No login, admin authorization, database, payment integration, Android package,
notification service or real council inbox. This update replaces the older demo's
session feedback/shortlist screens with the requested council sections.
Python syntax, JSON and theme structure checked. No live deployment/device testing.
Custom CSS may require maintenance after Streamlit updates. Acceptance-test all pages.

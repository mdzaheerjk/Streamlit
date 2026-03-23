# Streamlit Complete Reference Notes

## What is Streamlit?

Streamlit is an open-source Python framework for building interactive web apps for data science and machine learning — with **no front-end experience required**. You write pure Python, and Streamlit renders the UI in a browser. Every time a user interacts with a widget, the script reruns from top to bottom.

```bash
pip install streamlit
streamlit run app.py
```

---

## App Structure & Execution Model

Streamlit's core behaviour: **the entire script reruns on every interaction**.

```python
import streamlit as st

st.title("My App")           # Renders a title
x = st.slider("Pick x", 0, 100)  # Widget — triggers rerun when changed
st.write(f"x = {x}")        # Output updates automatically
```

### Page Config (must be first Streamlit call)

```python
st.set_page_config(
    page_title="My App",
    page_icon="🚀",
    layout="wide",          # "centered" (default) | "wide"
    initial_sidebar_state="expanded",  # "auto" | "expanded" | "collapsed"
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        'Report a bug': None,
        'About': "My awesome app!"
    }
)
```

---

## Text & Display Elements

```python
st.title("Main Title")
st.header("Header")
st.subheader("Subheader")
st.text("Fixed-width text")
st.markdown("**Bold**, *italic*, `code`, [link](https://streamlit.io)")
st.caption("Small caption text")
st.code("x = 42", language="python")
st.latex(r"\int_{a}^{b} f(x)\,dx")
st.divider()                # Horizontal rule
st.write("Catches almost anything: text, dataframes, charts, dicts...")
```

### `st.write` is magic — it renders:
- strings, numbers → text
- dicts, lists → formatted tables
- DataFrames → tables
- Matplotlib / Altair / Plotly figures → charts
- Keras / sklearn models → model summary

---

## Data Display

```python
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

st.dataframe(df)                     # Interactive, sortable table
st.table(df)                         # Static table
st.metric("Revenue", "$1.2M", "+12%")  # KPI metric with delta
st.json({"key": "value"})            # Formatted JSON
```

### Dataframe Styling

```python
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "A": st.column_config.NumberColumn("Column A", format="%d"),
        "B": st.column_config.ProgressColumn("B", min_value=0, max_value=10),
    }
)
```

---

## Input Widgets

### Text

```python
name = st.text_input("Your name", placeholder="Enter name...")
bio  = st.text_area("Bio", height=150)
pwd  = st.text_input("Password", type="password")
```

### Numbers

```python
age   = st.number_input("Age", min_value=0, max_value=120, value=25, step=1)
score = st.slider("Score", 0.0, 10.0, 5.0, step=0.5)
rng   = st.slider("Range", 0, 100, (20, 80))   # Returns tuple
```

### Selection

```python
lang  = st.selectbox("Language", ["Python", "R", "Julia"])
langs = st.multiselect("Languages", ["Python", "R", "Julia"], default=["Python"])
color = st.radio("Color", ["Red", "Green", "Blue"])
```

### Boolean / Date / File

```python
agree = st.checkbox("I agree to terms")
dark  = st.toggle("Dark mode")
date  = st.date_input("Pick a date")
time  = st.time_input("Pick a time")
file  = st.file_uploader("Upload CSV", type=["csv", "xlsx"])
files = st.file_uploader("Upload files", accept_multiple_files=True)
```

### Buttons & Actions

```python
if st.button("Submit"):
    st.success("Submitted!")

color = st.color_picker("Pick a color", "#00BFFF")
cam   = st.camera_input("Take a photo")
```

### Forms (batch widget submission)

```python
with st.form("my_form"):
    name = st.text_input("Name")
    age  = st.number_input("Age", min_value=0)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(f"Hello {name}, age {age}")
```

Forms prevent reruns on each widget change — only submit triggers a rerun.

---

## Layout & Containers

### Columns

```python
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Users", "1,234")

with col2:
    st.metric("Revenue", "$5K")

col1, col2 = st.columns([2, 1])   # Ratio: col1 is twice as wide
```

### Tabs

```python
tab1, tab2, tab3 = st.tabs(["Overview", "Data", "Settings"])

with tab1:
    st.write("Welcome!")

with tab2:
    st.dataframe(df)
```

### Expander

```python
with st.expander("Show details"):
    st.write("Hidden by default...")
    st.code("print('revealed!')")
```

### Sidebar

```python
with st.sidebar:
    st.title("Controls")
    threshold = st.slider("Threshold", 0, 100)

# Or shorthand:
threshold = st.sidebar.slider("Threshold", 0, 100)
```

### Container & Empty

```python
placeholder = st.empty()
placeholder.write("Loading...")
# Later:
placeholder.write("Done!")          # Replaces previous content
placeholder.empty()                 # Clears it

with st.container():
    st.write("Grouped content")
```

---

## Charts & Visualisation

### Built-in (fast)

```python
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
st.scatter_chart(df)
st.map(df_with_lat_lon)             # df must have 'lat' and 'lon' columns
```

### Matplotlib / Seaborn

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.pyplot(fig)
```

### Plotly

```python
import plotly.express as px

fig = px.scatter(df, x="A", y="B", color="C")
st.plotly_chart(fig, use_container_width=True)
```

### Altair

```python
import altair as alt

chart = alt.Chart(df).mark_bar().encode(x="A", y="B")
st.altair_chart(chart, use_container_width=True)
```

---

## Media

```python
st.image("image.png", caption="My image", width=300)
st.image(pil_img)                   # PIL Image object also works
st.video("video.mp4")
st.audio("sound.wav")
```

---

## Status & Feedback

```python
st.success("Operation succeeded!")
st.info("Here is some info.")
st.warning("Careful with this.")
st.error("Something went wrong.")
st.exception(err)                   # Displays a traceback

# Progress & Spinner
with st.spinner("Loading..."):
    time.sleep(2)

bar = st.progress(0)
for i in range(100):
    bar.progress(i + 1)
    time.sleep(0.01)

st.toast("Saved!", icon="✅")       # Non-blocking notification
st.balloons()                       # 🎈 Celebration animation
st.snow()                           # ❄️ Snow animation
```

---

## Caching

Caching prevents expensive functions from rerunning on every interaction.

### `@st.cache_data` — for data (DataFrames, arrays, strings)

```python
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

@st.cache_data(ttl=3600)            # Expires after 1 hour
def fetch_from_api(url):
    return requests.get(url).json()

@st.cache_data(max_entries=5)       # LRU, keeps 5 entries
def expensive_query(param):
    ...
```

### `@st.cache_resource` — for shared objects (DB connections, ML models)

```python
@st.cache_resource
def load_model():
    return torch.load("model.pt")   # Loaded once, shared across all users

@st.cache_resource
def get_db_connection():
    return psycopg2.connect(DSN)
```

### Clearing cache

```python
load_data.clear()                   # Clear specific function
st.cache_data.clear()               # Clear all cache_data
st.cache_resource.clear()
```

---

## Session State

Session state persists values **across reruns for a single user session**.

```python
# Initialise safely
if "count" not in st.session_state:
    st.session_state.count = 0

# Read and write
st.session_state.count += 1
st.write(st.session_state.count)

# With attribute or dict syntax (both work)
st.session_state["key"] = "value"
val = st.session_state.key

# Delete
del st.session_state["key"]
```

### Widget state binding

```python
# Pass key= to link widget to session state
st.text_input("Name", key="user_name")
st.write(st.session_state.user_name)   # Updates live
```

### Callbacks

```python
def increment():
    st.session_state.count += 1

st.button("Click me", on_click=increment)

# With args
def greet(name):
    st.session_state.greeting = f"Hello, {name}!"

st.button("Greet", on_click=greet, args=("Alice",))
```

---

## Multi-Page Apps

### File structure

```
my_app/
├── app.py            ← Main page (entry point)
└── pages/
    ├── 1_Dashboard.py
    ├── 2_Analysis.py
    └── 3_Settings.py
```

- Pages appear automatically in the sidebar.
- The number prefix controls ordering (stripped from the display name).
- Emoji at the start becomes the page icon.

### Programmatic navigation (Streamlit ≥ 1.36)

```python
pg = st.navigation([
    st.Page("home.py", title="Home", icon="🏠"),
    st.Page("analysis.py", title="Analysis", icon="📊"),
])
pg.run()
```

---

## Secrets Management

Store API keys and passwords in `.streamlit/secrets.toml`:

```toml
# .streamlit/secrets.toml
db_password = "supersecret"

[api]
key = "abc123"
```

Access in code:

```python
pwd = st.secrets["db_password"]
key = st.secrets["api"]["key"]
```

On Streamlit Community Cloud, add secrets via the app dashboard (never commit `.toml` to git).

---

## Components & Custom HTML

```python
# Embed raw HTML / JS
from streamlit.components.v1 import html
html("<h3 style='color:red'>Custom HTML</h3>", height=100)

# Embed an iframe
from streamlit.components.v1 import iframe
iframe("https://example.com", height=500)
```

### Third-party component examples

```bash
pip install streamlit-aggrid
pip install streamlit-lottie
pip install streamlit-folium
```

```python
from st_aggrid import AgGrid
AgGrid(df)

import streamlit_lottie as stl
stl.st_lottie(animation_json)
```

---

## Theming

Create `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"    # "sans serif" | "serif" | "monospace"
```

---

## Deployment

### Streamlit Community Cloud (free)

1. Push code to a public GitHub repo.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Connect your repo, choose branch and `app.py`.
4. Add secrets in the dashboard.
5. Click **Deploy**.

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
docker build -t my-app .
docker run -p 8501:8501 my-app
```

### Environment variables

```bash
streamlit run app.py \
  --server.port 8080 \
  --server.headless true \
  --browser.gatherUsageStats false
```

---

## Performance Tips

| Tip | Why |
|-----|-----|
| Use `@st.cache_data` on data loaders | Avoids re-reading files on every click |
| Use `@st.cache_resource` for models | One model loaded for all users |
| Use `st.form` for multi-field input | Reduces reruns from intermediate edits |
| Use `st.empty()` for live updates | Prevents layout shifting |
| Avoid global mutable state | Use `st.session_state` instead |
| Use `ttl=` on cached functions | Keeps data fresh in long-running apps |

---

## Common Patterns

### File upload + processing

```python
file = st.file_uploader("Upload CSV")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    st.download_button("Download", df.to_csv(), "result.csv", "text/csv")
```

### Async / streaming text output

```python
import time

placeholder = st.empty()
text = ""
for word in "Hello this is streamed output".split():
    text += word + " "
    placeholder.write(text)
    time.sleep(0.1)
```

### LLM streaming (OpenAI-style)

```python
with st.chat_message("assistant"):
    stream = client.chat.completions.create(model="gpt-4o", messages=msgs, stream=True)
    response = st.write_stream(stream)
```

### Chat interface

```python
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    # Add your LLM call here
```

---

## Quick Reference Card

```
Display         st.title / header / subheader / text / markdown / caption / code / latex / write
Data            st.dataframe / table / metric / json
Input           st.text_input / text_area / number_input / slider / selectbox / multiselect
                st.radio / checkbox / toggle / date_input / time_input / file_uploader / button
Layout          st.columns / tabs / expander / sidebar / container / empty
Charts          st.line_chart / bar_chart / area_chart / scatter_chart / map
                st.pyplot / plotly_chart / altair_chart / vega_lite_chart
Status          st.success / info / warning / error / spinner / progress / toast / balloons
Cache           @st.cache_data   →  DataFrames, JSON, arrays
                @st.cache_resource → DB connections, ML models
State           st.session_state  (dict-like, persists across reruns per user)
Config          st.set_page_config  (must be the first Streamlit call)
```

---

*Streamlit version this covers: 1.35+. Docs: https://docs.streamlit.io*

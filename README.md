# 🚀 Streamlit: Complete Notes — Beginner to Advanced (AI/ML Focus)

> **What is Streamlit?**
> Streamlit is an open-source Python framework that lets you turn data scripts into shareable web apps in minutes — no HTML, CSS, or JavaScript required. It's the #1 choice for AI/ML engineers to demo models, build dashboards, and create interactive tools.

---

## 📋 Table of Contents

1. [Setup & Installation](#1-setup--installation)
2. [Your First Streamlit App](#2-your-first-streamlit-app)
3. [Text & Display Elements](#3-text--display-elements)
4. [Input Widgets](#4-input-widgets)
5. [Layout & Containers](#5-layout--containers)
6. [Data Display](#6-data-display)
7. [Charts & Visualization](#7-charts--visualization)
8. [Media Elements](#8-media-elements)
9. [Session State & Interactivity](#9-session-state--interactivity)
10. [Caching & Performance](#10-caching--performance)
11. [File Upload & Download](#11-file-upload--download)
12. [Forms](#12-forms)
13. [Sidebar & Navigation](#13-sidebar--navigation)
14. [Multi-Page Apps](#14-multi-page-apps)
15. [AI/ML Integration — Beginner](#15-aiml-integration--beginner)
16. [AI/ML Integration — Intermediate](#16-aiml-integration--intermediate)
17. [AI/ML Integration — Advanced](#17-aiml-integration--advanced)
18. [LLM & ChatGPT / Gemini / Claude Apps](#18-llm--chatgpt--gemini--claude-apps)
19. [Deployment](#19-deployment)
20. [Advanced Patterns & Best Practices](#20-advanced-patterns--best-practices)
21. [Quick Reference Cheatsheet](#21-quick-reference-cheatsheet)

---

## 1. Setup & Installation

### Requirements
- Python 3.8 or higher
- pip (Python package manager)

### Install Streamlit

```bash
pip install streamlit
```

### Install with common AI/ML extras

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn plotly
pip install torch torchvision transformers  # for deep learning
pip install openai anthropic google-generativeai  # for LLMs
```

### Verify Installation

```bash
streamlit --version
```

### Run your app

```bash
streamlit run app.py
```

This opens your browser at `http://localhost:8501` automatically.

### Useful CLI commands

```bash
streamlit run app.py                    # Run an app
streamlit run app.py --server.port 8080 # Custom port
streamlit hello                         # Built-in demo
streamlit config show                   # Show all config options
streamlit cache clear                   # Clear all caches
```

---

## 2. Your First Streamlit App

Create a file called `app.py`:

```python
import streamlit as st

st.title("My First Streamlit App 🎉")
st.write("Hello, World!")
```

Run it:

```bash
streamlit run app.py
```

### How Streamlit Works (VERY IMPORTANT)

> Streamlit **re-runs the entire script from top to bottom** every time the user interacts with a widget. This is the mental model you MUST understand.

```python
import streamlit as st

# This runs EVERY TIME the user does anything
st.write("This line runs on every interaction")

name = st.text_input("Enter your name")  # Widget
st.write(f"Hello, {name}!")              # Reacts to widget
```

---

## 3. Text & Display Elements

### Basic Text

```python
import streamlit as st

st.title("This is a Title")           # Large title
st.header("This is a Header")         # H1 equivalent
st.subheader("This is a Subheader")   # H2 equivalent
st.text("This is plain text")         # Fixed-width plain text
st.write("This is st.write()")        # Smart display (most used)
st.markdown("**Bold**, *italic*, `code`")  # Markdown
```

### Magic Write

`st.write()` is the most versatile — it automatically handles strings, numbers, DataFrames, plots, etc.

```python
st.write("A string")          # Renders as text
st.write(42)                  # Renders as number
st.write(df)                  # Renders as table
st.write(fig)                 # Renders matplotlib/plotly figure
st.write({"key": "value"})    # Renders as JSON
```

### Code Display

```python
# Show code with syntax highlighting
st.code("""
def hello(name):
    return f"Hello, {name}!"
""", language="python")

# Inline code
st.markdown("Use `st.write()` for everything")
```

### LaTeX & Math

```python
st.latex(r"\hat{y} = \sigma(W \cdot x + b)")

st.latex(r"""
    \frac{\partial L}{\partial w} = -\frac{2}{n} \sum_{i=1}^{n}(y_i - \hat{y}_i) x_i
""")
```

### Alerts & Callouts

```python
st.success("✅ Model trained successfully!")
st.info("ℹ️ Training may take a few minutes.")
st.warning("⚠️ GPU not detected. Using CPU.")
st.error("❌ Error: Model file not found.")

# Exception display
try:
    1 / 0
except Exception as e:
    st.exception(e)
```

### Metrics (Great for ML!)

```python
st.metric(label="Model Accuracy", value="94.5%", delta="1.2%")
st.metric(label="Loss", value="0.043", delta="-0.005", delta_color="inverse")

# Multiple metrics in columns
col1, col2, col3 = st.columns(3)
col1.metric("Accuracy", "94.5%", "+1.2%")
col2.metric("Precision", "93.1%", "+0.8%")
col3.metric("Recall", "95.2%", "+1.5%")
```

---

## 4. Input Widgets

### Text Inputs

```python
name = st.text_input("Your Name", placeholder="Enter your name...")
bio = st.text_area("Bio", height=150, placeholder="Tell us about yourself...")
password = st.text_input("Password", type="password")
```

### Number Inputs

```python
age = st.number_input("Age", min_value=0, max_value=120, value=25)
lr = st.number_input("Learning Rate", min_value=0.0001, max_value=1.0, value=0.001, step=0.0001, format="%.4f")
```

### Sliders

```python
threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.5)
epochs = st.slider("Epochs", 1, 100, 10)
range_val = st.slider("Select range", 0, 100, (25, 75))  # Range slider

# Slider with step
lr = st.slider("Learning Rate", 0.0001, 0.1, 0.001, step=0.0001)
```

### Select Widgets

```python
model = st.selectbox("Choose Model", ["Logistic Regression", "Random Forest", "XGBoost", "Neural Network"])

# Multiple select
features = st.multiselect("Select Features", ["age", "income", "education", "job"])

# Radio buttons
task = st.radio("Task Type", ["Classification", "Regression", "Clustering"])
```

### Boolean Widgets

```python
normalize = st.checkbox("Normalize Data", value=True)
use_gpu = st.toggle("Use GPU", value=False)
```

### Date & Time

```python
import datetime
date = st.date_input("Training Start Date", datetime.date.today())
time = st.time_input("Set Time", datetime.time(8, 0))
```

### Color Picker

```python
color = st.color_picker("Pick a color", "#FF6B6B")
```

### Buttons

```python
if st.button("Train Model 🚀"):
    st.write("Training started!")

# Download button (covered in File section)
# Link button
st.link_button("Open GitHub", "https://github.com")
```

---

## 5. Layout & Containers

### Columns

```python
col1, col2 = st.columns(2)
with col1:
    st.write("Left column")
    st.image("image.png")

with col2:
    st.write("Right column")
    st.metric("Accuracy", "95%")

# Unequal widths
col1, col2, col3 = st.columns([3, 1, 1])  # Ratios
```

### Expander

```python
with st.expander("📊 Show Model Details"):
    st.write("Model architecture, hyperparameters, etc.")
    st.json({"layers": 4, "units": 128, "dropout": 0.3})
```

### Tabs

```python
tab1, tab2, tab3 = st.tabs(["📈 Training", "🧪 Evaluation", "🔮 Prediction"])

with tab1:
    st.write("Training metrics here")

with tab2:
    st.write("Evaluation results here")

with tab3:
    st.write("Make predictions here")
```

### Container

```python
# Group elements logically
with st.container():
    st.write("Inside container")
    st.bar_chart([1, 2, 3])

# Empty placeholder (useful for dynamic content)
placeholder = st.empty()
placeholder.text("Loading...")
# Later:
placeholder.write("Done!")
# Or clear it:
placeholder.empty()
```

### Popover

```python
with st.popover("⚙️ Settings"):
    st.slider("Temperature", 0.0, 2.0, 0.7)
    st.number_input("Max tokens", 100, 4096, 512)
```

---

## 6. Data Display

### DataFrames & Tables

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [95, 87, 92],
    "Grade": ["A", "B", "A"]
})

st.dataframe(df)           # Interactive, scrollable table
st.table(df)               # Static table (no scrolling)
st.write(df)               # Also works
```

### Styled DataFrames (st.dataframe with formatting)

```python
# Highlight max values
st.dataframe(df.style.highlight_max(axis=0))

# Custom column config
st.dataframe(
    df,
    column_config={
        "Score": st.column_config.ProgressColumn(
            "Score",
            min_value=0,
            max_value=100
        )
    },
    hide_index=True
)
```

### JSON Display

```python
st.json({"model": "gpt-4", "tokens": 1024, "temperature": 0.7})
```

---

## 7. Charts & Visualization

### Built-in Charts (Quick)

```python
import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])

st.line_chart(data)        # Line chart
st.bar_chart(data)         # Bar chart
st.area_chart(data)        # Area chart
st.scatter_chart(data)     # Scatter chart
```

### Matplotlib

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title("My Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")

st.pyplot(fig)
```

### Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data=df, x="Score", kde=True, ax=ax)
st.pyplot(fig)

# Correlation heatmap (common in ML)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
```

### Plotly (Most Powerful & Interactive)

```python
import plotly.express as px
import plotly.graph_objects as go

# Simple scatter
fig = px.scatter(df, x="feature1", y="feature2", color="label", title="Feature Space")
st.plotly_chart(fig, use_container_width=True)

# 3D scatter (great for embeddings)
fig = px.scatter_3d(df, x="x", y="y", z="z", color="label")
st.plotly_chart(fig)

# Confusion matrix heatmap
fig = px.imshow(conf_matrix, text_auto=True, title="Confusion Matrix",
                labels=dict(x="Predicted", y="Actual"))
st.plotly_chart(fig)
```

---

## 8. Media Elements

### Images

```python
from PIL import Image

# From URL
st.image("https://example.com/image.jpg", caption="My image", use_container_width=True)

# From local file
image = Image.open("my_image.png")
st.image(image, caption="Uploaded Image", width=400)

# From numpy array (great for CV models)
import numpy as np
img_array = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
st.image(img_array, caption="Random Image")
```

### Video & Audio

```python
st.video("https://www.youtube.com/watch?v=xyz")
st.audio("audio.mp3")
```

---

## 9. Session State & Interactivity

### The Problem Without Session State

```python
# ❌ This breaks — count resets on every re-run!
count = 0
if st.button("Increment"):
    count += 1
st.write(f"Count: {count}")  # Always shows 0
```

### The Solution: st.session_state

```python
# ✅ Correct way using session state
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(f"Count: {st.session_state.count}")
```

### Session State Basics

```python
# Initialize
if "messages" not in st.session_state:
    st.session_state.messages = []

# Set
st.session_state.model_name = "gpt-4"

# Get
name = st.session_state.get("user_name", "Guest")

# Delete
del st.session_state["old_key"]

# Check existence
if "trained_model" in st.session_state:
    model = st.session_state.trained_model
```

### Chat History (Most Common LLM Pattern)

```python
import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []

# Display chat messages
for message in st.session_state.history:
    with st.chat_message(message["role"]):  # "user" or "assistant"
        st.write(message["content"])

# Get new input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    
    # Get response (placeholder)
    response = f"You said: {prompt}"
    st.session_state.history.append({"role": "assistant", "content": response})
    
    st.rerun()  # Refresh to show new messages
```

### Callbacks

```python
def on_change():
    st.session_state.processed = False

st.selectbox("Choose model", ["RF", "XGB"], key="model", on_change=on_change)
```

---

## 10. Caching & Performance

### Why Caching Matters

Since Streamlit re-runs every time, expensive operations (loading data, training models) would repeat on every click. Caching saves results.

### @st.cache_data — For Data

```python
import streamlit as st
import pandas as pd

@st.cache_data
def load_dataset(path):
    return pd.read_csv(path)

# Runs only ONCE; uses cache on re-runs
df = load_dataset("large_data.csv")
```

### @st.cache_resource — For Models & Connections

```python
import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    # Loads ONCE and shares across all users
    return pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

classifier = load_model()
```

### Key Difference

| `@st.cache_data` | `@st.cache_resource` |
|---|---|
| Returns a new copy each call | Returns the same object (singleton) |
| Use for: DataFrames, arrays, dicts | Use for: ML models, DB connections, tokenizers |
| Serializable objects | Non-serializable objects |
| Thread-safe by default | Shared across threads |

### Cache with Parameters (TTL & Max Entries)

```python
@st.cache_data(ttl=3600, max_entries=10)  # expires in 1 hour, keep 10 versions
def fetch_data(url):
    return requests.get(url).json()

@st.cache_data(show_spinner="Loading model weights...")
def load_weights():
    ...
```

### Clear Cache Programmatically

```python
load_dataset.clear()       # Clear specific function cache
st.cache_data.clear()      # Clear all data cache
st.cache_resource.clear()  # Clear all resource cache
```

---

## 11. File Upload & Download

### Upload Files

```python
uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

# Multiple files
files = st.file_uploader("Upload images", type=["png", "jpg"], accept_multiple_files=True)
for file in files:
    image = Image.open(file)
    st.image(image, width=200)
```

### Process Uploaded File

```python
import pandas as pd
from io import StringIO

uploaded = st.file_uploader("Upload CSV", type="csv")
if uploaded:
    # Read as string
    stringio = StringIO(uploaded.getvalue().decode("utf-8"))
    df = pd.read_csv(stringio)
    st.dataframe(df)
    
    # Show file details
    st.write(f"Filename: {uploaded.name}")
    st.write(f"File size: {uploaded.size} bytes")
```

### Download Files

```python
# Download a DataFrame as CSV
csv_data = df.to_csv(index=False)
st.download_button(
    label="📥 Download CSV",
    data=csv_data,
    file_name="results.csv",
    mime="text/csv"
)

# Download a trained model (pickle)
import pickle
model_bytes = pickle.dumps(trained_model)
st.download_button(
    label="💾 Download Model",
    data=model_bytes,
    file_name="model.pkl",
    mime="application/octet-stream"
)

# Download a plot
import io
fig.savefig(buf := io.BytesIO(), format="png")
st.download_button("📊 Download Plot", buf.getvalue(), "plot.png", "image/png")
```

---

## 12. Forms

Forms collect multiple inputs and only trigger re-runs when the submit button is pressed — great for ML training configurations.

```python
with st.form("training_config"):
    st.subheader("⚙️ Training Configuration")
    
    model_type = st.selectbox("Model", ["Random Forest", "XGBoost", "Neural Net"])
    learning_rate = st.slider("Learning Rate", 0.0001, 0.1, 0.01)
    epochs = st.number_input("Epochs", 1, 200, 50)
    batch_size = st.selectbox("Batch Size", [16, 32, 64, 128])
    
    submitted = st.form_submit_button("🚀 Start Training")

if submitted:
    st.success(f"Training {model_type} for {epochs} epochs with lr={learning_rate}")
    # train_model(model_type, learning_rate, epochs, batch_size)
```

---

## 13. Sidebar & Navigation

### Sidebar

```python
st.sidebar.title("⚙️ Controls")
st.sidebar.write("---")

# All widgets work in sidebar
model = st.sidebar.selectbox("Model", ["RF", "XGB", "NN"])
threshold = st.sidebar.slider("Threshold", 0.0, 1.0, 0.5)

# Also with `with` syntax
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to", ["Home", "Train", "Predict", "Evaluate"])
```

### Page Config

Always set this at the top of your script (MUST be first Streamlit command):

```python
import streamlit as st

st.set_page_config(
    page_title="My ML App",
    page_icon="🤖",
    layout="wide",           # "centered" or "wide"
    initial_sidebar_state="expanded"  # "auto", "expanded", "collapsed"
)
```

---

## 14. Multi-Page Apps

Streamlit supports multi-page apps natively since v1.10.

### Folder Structure

```
my_app/
├── app.py              # Main page (Home)
└── pages/
    ├── 1_📈_Training.py
    ├── 2_🧪_Evaluation.py
    └── 3_🔮_Prediction.py
```

### app.py (Home)

```python
import streamlit as st

st.set_page_config(page_title="ML Dashboard", page_icon="🤖", layout="wide")
st.title("🤖 ML Dashboard — Home")
st.write("Use the sidebar to navigate.")
```

### pages/1_Training.py

```python
import streamlit as st
st.title("📈 Model Training")
# training code here
```

### Sharing Data Between Pages (Session State)

```python
# In Training page
st.session_state.trained_model = model
st.session_state.metrics = {"accuracy": 0.95}

# In Evaluation page
if "trained_model" in st.session_state:
    model = st.session_state.trained_model
```

---

## 15. AI/ML Integration — Beginner

### Basic Scikit-learn Classifier App

```python
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.title("🌸 Iris Flower Classifier")

# Load data
@st.cache_data
def load_data():
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["target"] = data.target
    return df, data.target_names

df, target_names = load_data()

# Sidebar controls
with st.sidebar:
    n_estimators = st.slider("Number of Trees", 10, 200, 100)
    test_size = st.slider("Test Size (%)", 10, 40, 20) / 100

# Train model
X = df.drop("target", axis=1)
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

@st.cache_resource
def train_model(n_est):
    model = RandomForestClassifier(n_estimators=n_est, random_state=42)
    model.fit(X_train, y_train)
    return model

model = train_model(n_estimators)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

st.metric("Test Accuracy", f"{acc:.2%}")

# Prediction interface
st.subheader("🔮 Make a Prediction")
col1, col2 = st.columns(2)
with col1:
    sl = st.number_input("Sepal Length (cm)", 4.0, 8.0, 5.1)
    sw = st.number_input("Sepal Width (cm)", 2.0, 4.5, 3.5)
with col2:
    pl = st.number_input("Petal Length (cm)", 1.0, 7.0, 1.4)
    pw = st.number_input("Petal Width (cm)", 0.1, 2.5, 0.2)

if st.button("Predict"):
    prediction = model.predict([[sl, sw, pl, pw]])
    probabilities = model.predict_proba([[sl, sw, pl, pw]])[0]
    st.success(f"Predicted: **{target_names[prediction[0]]}**")
    
    # Show probabilities
    prob_df = pd.DataFrame({"Species": target_names, "Probability": probabilities})
    st.bar_chart(prob_df.set_index("Species"))
```

### Progress Bars for Training

```python
import time

progress_bar = st.progress(0)
status_text = st.empty()

for i in range(100):
    progress_bar.progress(i + 1)
    status_text.text(f"Training... Epoch {i+1}/100")
    time.sleep(0.05)

status_text.success("✅ Training complete!")
```

---

## 16. AI/ML Integration — Intermediate

### Train + Evaluate + Visualize Pipeline

```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (confusion_matrix, classification_report,
                              roc_auc_score, roc_curve)
from sklearn.preprocessing import label_binarize

st.set_page_config(page_title="ML Pipeline", layout="wide")
st.title("🧠 Full ML Pipeline")

# Upload data
uploaded = st.file_uploader("Upload CSV dataset", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.write("### Preview", df.head())
    
    # Feature selection
    target = st.selectbox("Select Target Column", df.columns)
    features = st.multiselect("Select Features", [c for c in df.columns if c != target], 
                               default=[c for c in df.columns if c != target])
    
    if st.button("Train Model"):
        X = df[features]
        y = df[target]
        
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        with st.spinner("Training model..."):
            model = GradientBoostingClassifier()
            model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        # Metrics
        st.subheader("📊 Evaluation Results")
        col1, col2, col3 = st.columns(3)
        from sklearn.metrics import accuracy_score, precision_score, recall_score
        col1.metric("Accuracy", f"{accuracy_score(y_test, y_pred):.2%}")
        col2.metric("Precision", f"{precision_score(y_test, y_pred, average='weighted'):.2%}")
        col3.metric("Recall", f"{recall_score(y_test, y_pred, average='weighted'):.2%}")
        
        # Confusion Matrix
        st.subheader("🔲 Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred)
        labels = sorted(y.unique().astype(str))
        fig = px.imshow(cm, x=labels, y=labels, text_auto=True,
                        color_continuous_scale="Blues",
                        labels=dict(x="Predicted", y="Actual"))
        st.plotly_chart(fig, use_container_width=True)
        
        # Feature Importance
        st.subheader("📌 Feature Importance")
        fi = pd.DataFrame({
            "Feature": features,
            "Importance": model.feature_importances_
        }).sort_values("Importance", ascending=False)
        
        fig2 = px.bar(fi, x="Importance", y="Feature", orientation="h",
                      title="Feature Importances")
        st.plotly_chart(fig2, use_container_width=True)
        
        # Save model to session state
        st.session_state.model = model
        st.session_state.features = features
```

### Custom Neural Network Visualizer with PyTorch

```python
import streamlit as st
import torch
import torch.nn as nn
import numpy as np
import plotly.graph_objects as go

st.title("🧠 Neural Network Trainer")

@st.cache_resource
def build_model(layers, activation):
    act_map = {"ReLU": nn.ReLU, "Tanh": nn.Tanh, "Sigmoid": nn.Sigmoid}
    modules = []
    in_features = 10
    for out_features in layers:
        modules += [nn.Linear(in_features, out_features), act_map[activation]()]
        in_features = out_features
    modules.append(nn.Linear(in_features, 1))
    return nn.Sequential(*modules)

with st.sidebar:
    layer_sizes = st.multiselect("Hidden Layer Sizes", [16, 32, 64, 128, 256], default=[64, 32])
    activation = st.selectbox("Activation", ["ReLU", "Tanh", "Sigmoid"])
    lr = st.select_slider("Learning Rate", [0.1, 0.01, 0.001, 0.0001], value=0.01)
    epochs = st.slider("Epochs", 10, 500, 100)

model = build_model(layer_sizes, activation)

if st.button("Train on Synthetic Data"):
    X = torch.randn(1000, 10)
    y = torch.randn(1000, 1)
    
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.MSELoss()
    
    losses = []
    progress = st.progress(0)
    
    for epoch in range(epochs):
        optimizer.zero_grad()
        output = model(X)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
        progress.progress((epoch + 1) / epochs)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=losses, mode="lines", name="Training Loss"))
    fig.update_layout(title="Training Loss Curve", xaxis_title="Epoch", yaxis_title="Loss")
    st.plotly_chart(fig, use_container_width=True)
    st.success(f"Final Loss: {losses[-1]:.4f}")
```

---

## 17. AI/ML Integration — Advanced

### Real-time Prediction with Streaming

```python
import streamlit as st
import time

def stream_prediction(text):
    """Simulate streaming model output token by token"""
    words = f"Analysis of '{text}': This text appears to be {'positive' if len(text) % 2 == 0 else 'negative'} in sentiment.".split()
    for word in words:
        yield word + " "
        time.sleep(0.05)

st.title("🔮 Real-time Predictions")
user_input = st.text_area("Enter text to analyze")

if st.button("Analyze") and user_input:
    with st.chat_message("assistant"):
        st.write_stream(stream_prediction(user_input))
```

### Image Classification App (torchvision)

```python
import streamlit as st
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
from PIL import Image
import requests

st.title("🖼️ Image Classifier (ResNet-50)")

@st.cache_resource
def load_model():
    model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)
    model.eval()
    return model

@st.cache_data
def load_labels():
    url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
    return requests.get(url).json()

model = load_model()
labels = load_labels()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

uploaded = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    with st.spinner("Classifying..."):
        tensor = transform(image).unsqueeze(0)
        with torch.no_grad():
            outputs = model(tensor)
        
        probs = torch.nn.functional.softmax(outputs[0], dim=0)
        top5 = torch.topk(probs, 5)
        
    st.subheader("🏆 Top 5 Predictions")
    for prob, idx in zip(top5.values, top5.indices):
        st.progress(float(prob), text=f"{labels[idx]}: {prob:.2%}")
```

### Hugging Face Transformers Pipeline

```python
import streamlit as st
from transformers import pipeline

st.title("🤗 Hugging Face NLP Demos")

task = st.sidebar.selectbox("Choose NLP Task", [
    "Sentiment Analysis",
    "Text Summarization",
    "Named Entity Recognition",
    "Question Answering"
])

@st.cache_resource
def get_pipeline(task_name):
    task_map = {
        "Sentiment Analysis": ("sentiment-analysis", None),
        "Text Summarization": ("summarization", "facebook/bart-large-cnn"),
        "Named Entity Recognition": ("ner", None),
        "Question Answering": ("question-answering", None)
    }
    task_key, model = task_map[task_name]
    return pipeline(task_key, model=model) if model else pipeline(task_key)

nlp = get_pipeline(task)

if task == "Sentiment Analysis":
    text = st.text_area("Enter text", "I love building AI apps with Streamlit!")
    if st.button("Analyze"):
        result = nlp(text)[0]
        if result["label"] == "POSITIVE":
            st.success(f"😊 Positive — Confidence: {result['score']:.2%}")
        else:
            st.error(f"😞 Negative — Confidence: {result['score']:.2%}")

elif task == "Text Summarization":
    text = st.text_area("Enter long text (min 100 words)", height=200)
    if st.button("Summarize") and len(text.split()) >= 50:
        with st.spinner("Summarizing..."):
            summary = nlp(text, max_length=130, min_length=30)[0]["summary_text"]
        st.subheader("Summary:")
        st.write(summary)

elif task == "Named Entity Recognition":
    text = st.text_input("Enter text", "Apple was founded by Steve Jobs in Cupertino, California.")
    if st.button("Extract Entities"):
        entities = nlp(text)
        import pandas as pd
        df = pd.DataFrame(entities)[["word", "entity", "score"]]
        df["score"] = df["score"].apply(lambda x: f"{x:.2%}")
        st.table(df)

elif task == "Question Answering":
    context = st.text_area("Context paragraph", "Streamlit was created by Adrien Treuille, Thiago Teixeira, and Amanda Kelly in 2018...")
    question = st.text_input("Your question", "When was Streamlit created?")
    if st.button("Get Answer"):
        answer = nlp(question=question, context=context)
        st.success(f"Answer: **{answer['answer']}** (score: {answer['score']:.2%})")
```

### Embedding Visualizer (TSNE / UMAP)

```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.manifold import TSNE
from sklearn.preprocessing import LabelEncoder

st.title("🗺️ Embedding Visualizer")

uploaded = st.file_uploader("Upload embeddings CSV (features + label column)", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    label_col = st.selectbox("Select label column", df.columns)
    
    feature_cols = [c for c in df.columns if c != label_col]
    X = df[feature_cols].values
    
    st.info(f"Shape: {X.shape[0]} samples × {X.shape[1]} dimensions")
    
    perplexity = st.slider("TSNE Perplexity", 5, 50, 30)
    
    if st.button("Visualize in 2D"):
        with st.spinner("Running t-SNE (may take a moment)..."):
            tsne = TSNE(n_components=2, perplexity=perplexity, random_state=42)
            coords = tsne.fit_transform(X)
        
        viz_df = pd.DataFrame({"x": coords[:, 0], "y": coords[:, 1], "label": df[label_col]})
        fig = px.scatter(viz_df, x="x", y="y", color="label", title="t-SNE Visualization",
                         hover_data=["label"])
        st.plotly_chart(fig, use_container_width=True)
```

---

## 18. LLM & ChatGPT / Gemini / Claude Apps

### ChatGPT / OpenAI Chatbot

```python
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="ChatGPT App", page_icon="💬")
st.title("💬 ChatGPT Clone")

# Initialize client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

# Display chat messages (skip system message)
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Message ChatGPT..."):
    # Add to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get response with streaming
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages,
            stream=True
        )
        response = st.write_stream(stream)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
```

### Claude (Anthropic) Chatbot

```python
import streamlit as st
import anthropic

st.title("🤖 Claude Assistant")

client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask Claude..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        with client.messages.stream(
            model="claude-opus-4-5",
            max_tokens=1024,
            messages=st.session_state.messages
        ) as stream:
            response = st.write_stream(stream.text_stream)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
```

### Gemini Chatbot

```python
import streamlit as st
import google.generativeai as genai

st.title("✨ Gemini Assistant")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

@st.cache_resource
def get_model():
    return genai.GenerativeModel("gemini-1.5-pro")

model = get_model()

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask Gemini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(prompt)
            reply = response.text
        st.write(reply)
    
    st.session_state.messages.append({"role": "assistant", "content": reply})
```

### RAG (Retrieval-Augmented Generation) App

```python
import streamlit as st
from openai import OpenAI
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

st.title("📚 RAG Document QA")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

@st.cache_data
def get_embedding(text):
    return client.embeddings.create(
        input=[text], model="text-embedding-3-small"
    ).data[0].embedding

# Upload knowledge base
uploaded = st.file_uploader("Upload knowledge base (CSV with 'text' column)", type="csv")

if uploaded:
    kb_df = pd.read_csv(uploaded)
    
    with st.spinner("Indexing documents..."):
        kb_df["embedding"] = kb_df["text"].apply(get_embedding)
    
    st.success(f"Indexed {len(kb_df)} documents!")
    
    query = st.text_input("Ask a question")
    
    if query:
        # Find relevant docs
        query_emb = np.array(get_embedding(query))
        kb_embs = np.stack(kb_df["embedding"].values)
        sims = cosine_similarity([query_emb], kb_embs)[0]
        top_idx = sims.argsort()[-3:][::-1]
        
        context = "\n\n".join(kb_df.iloc[top_idx]["text"].values)
        
        # Generate answer
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Answer based on context:\n{context}"},
                {"role": "user", "content": query}
            ]
        )
        
        st.write("### Answer")
        st.write(response.choices[0].message.content)
        
        with st.expander("📄 Source Documents"):
            for i in top_idx:
                st.info(kb_df.iloc[i]["text"])
```

### Using Secrets Safely

Never hardcode API keys. Use Streamlit Secrets:

```toml
# .streamlit/secrets.toml (never commit this!)
OPENAI_API_KEY = "sk-..."
ANTHROPIC_API_KEY = "sk-ant-..."
GEMINI_API_KEY = "AIza..."
```

```python
# Access in code
api_key = st.secrets["OPENAI_API_KEY"]
```

---

## 19. Deployment

### Streamlit Community Cloud (Free & Easy)

1. Push your app to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Add secrets in the Secrets section of the app settings
5. Click Deploy!

### Required files for deployment

```
my_app/
├── app.py
├── requirements.txt    # ← Required!
└── .streamlit/
    └── secrets.toml    # ← For API keys (add to .gitignore!)
```

### requirements.txt example

```text
streamlit>=1.32.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
openai>=1.0.0
transformers>=4.36.0
torch>=2.1.0
plotly>=5.17.0
```

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
docker build -t my-ml-app .
docker run -p 8501:8501 my-ml-app
```

### Environment Variables for Production

```python
import os
import streamlit as st

# Use env var or fall back to secrets
api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
```

---

## 20. Advanced Patterns & Best Practices

### Custom Components with HTML/CSS/JS

```python
import streamlit.components.v1 as components

# Embed any HTML
components.html("""
<div style="background: linear-gradient(135deg, #667eea, #764ba2);
            padding: 20px; border-radius: 10px; color: white;">
    <h2>Custom Styled Box</h2>
    <p>Any HTML/CSS/JS here!</p>
</div>
""", height=150)

# Embed an iframe
components.iframe("https://docs.streamlit.io", height=600)
```

### Custom CSS Injection

```python
st.markdown("""
<style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)
```

### Status & Spinner

```python
# Simple spinner
with st.spinner("Loading model..."):
    model = load_model()

# Detailed status with multiple steps
with st.status("Training model...", expanded=True) as status:
    st.write("Loading data...")
    load_data()
    
    st.write("Preprocessing...")
    preprocess()
    
    st.write("Training...")
    train()
    
    status.update(label="✅ Training complete!", state="complete", expanded=False)
```

### Toast Notifications

```python
st.toast("Model saved successfully!", icon="✅")
st.toast("Warning: High memory usage", icon="⚠️")
```

### Fragments (Partial Re-runs) — Advanced

Streamlit 1.33+ supports `@st.fragment` to re-run only part of the page:

```python
@st.fragment(run_every="5s")  # Auto-refresh every 5 seconds
def live_metrics():
    import random
    col1, col2 = st.columns(2)
    col1.metric("CPU Usage", f"{random.randint(20, 80)}%")
    col2.metric("GPU Usage", f"{random.randint(50, 95)}%")

live_metrics()
st.write("This part doesn't re-run with the fragment")
```

### Async & Callbacks Pattern

```python
import streamlit as st
import threading

def long_running_task(progress_callback):
    for i in range(100):
        time.sleep(0.1)
        progress_callback(i + 1)

if "result" not in st.session_state:
    st.session_state.result = None

if st.button("Start Task"):
    progress_bar = st.progress(0)
    
    def update_progress(val):
        progress_bar.progress(val / 100)
    
    long_running_task(update_progress)
    st.success("Done!")
```

### App Configuration File

```toml
# .streamlit/config.toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
maxUploadSize = 200

[browser]
gatherUsageStats = false
```

### Key Performance Tips

```python
# 1. Always cache heavy operations
@st.cache_resource
def load_large_model():
    return load_model_from_disk()

# 2. Use st.empty() for updating content without re-rendering
result_placeholder = st.empty()
for epoch in range(100):
    result_placeholder.metric("Loss", compute_loss(epoch))

# 3. Avoid putting large objects in session_state
# BAD: st.session_state.huge_df = df  (serialized on every run)
# GOOD: Use @st.cache_data and pass keys

# 4. Use fragments for selective re-rendering
@st.fragment
def expensive_chart():
    st.plotly_chart(build_complex_chart())

# 5. Profile with st.experimental_get_query_params for URL-based state
```

### Project Structure (Production)

```
my_ml_app/
├── app.py                      # Entry point, page config
├── pages/
│   ├── 1_📊_Dashboard.py
│   ├── 2_🧠_Train.py
│   └── 3_🔮_Predict.py
├── components/
│   ├── charts.py               # Reusable chart functions
│   ├── model_ui.py             # Model-related UI components
│   └── sidebar.py              # Shared sidebar
├── ml/
│   ├── model.py                # Model classes
│   ├── preprocessing.py        # Data pipeline
│   └── evaluation.py           # Metrics & evaluation
├── utils/
│   └── helpers.py
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml            # ← Add to .gitignore!
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 21. Quick Reference Cheatsheet

### Display

| Code | Output |
|------|--------|
| `st.title("text")` | Large title |
| `st.header("text")` | Header |
| `st.subheader("text")` | Subheader |
| `st.write(anything)` | Smart display |
| `st.markdown("**bold**")` | Markdown |
| `st.code("x=1", "python")` | Syntax-highlighted code |
| `st.latex(r"\hat{y}")` | Math formula |
| `st.metric("Label", "95%", "+2%")` | KPI metric |
| `st.success("msg")` | Green alert |
| `st.error("msg")` | Red alert |
| `st.warning("msg")` | Yellow alert |
| `st.info("msg")` | Blue alert |
| `st.json({...})` | JSON viewer |

### Inputs

| Code | Returns |
|------|---------|
| `st.text_input("label")` | str |
| `st.text_area("label")` | str |
| `st.number_input("label")` | float |
| `st.slider("label", min, max)` | float |
| `st.selectbox("label", options)` | any |
| `st.multiselect("label", options)` | list |
| `st.checkbox("label")` | bool |
| `st.toggle("label")` | bool |
| `st.radio("label", options)` | any |
| `st.date_input("label")` | date |
| `st.file_uploader("label")` | file |
| `st.button("label")` | bool |
| `st.chat_input("label")` | str or None |

### Layout

| Code | Usage |
|------|-------|
| `col1, col2 = st.columns(2)` | Side-by-side layout |
| `with st.expander("title")` | Collapsible section |
| `tab1, tab2 = st.tabs(["A","B"])` | Tabbed interface |
| `with st.container()` | Group elements |
| `st.empty()` | Placeholder for dynamic content |
| `with st.sidebar` | Sidebar panel |
| `with st.popover("label")` | Popup panel |

### Caching

| Code | Use for |
|------|---------|
| `@st.cache_data` | DataFrames, arrays, dicts |
| `@st.cache_resource` | Models, DB connections |

### ML-Specific

```python
# Show training progress
progress = st.progress(0)
status = st.empty()
for i, epoch in enumerate(epochs):
    train_epoch()
    progress.progress((i+1)/len(epochs))
    status.text(f"Epoch {i+1}/{len(epochs)}, Loss: {loss:.4f}")

# Load model once
@st.cache_resource
def get_model():
    return load_model()

# Stream LLM response
response = st.write_stream(llm.stream(prompt))

# Chat interface
with st.chat_message("user"):
    st.write(user_message)
with st.chat_message("assistant"):
    st.write(ai_response)
```

---

## 🎯 Learning Path Summary

| Level | Topics | Projects to Build |
|-------|--------|-------------------|
| **Beginner** | Installation, st.write, widgets, layout basics | Hello World app, Simple calculator |
| **Elementary** | DataFrames, charts, session state, forms | CSV explorer, Data dashboard |
| **Intermediate** | Caching, file upload, multi-page apps | Scikit-learn classifier with full UI |
| **Upper-Intermediate** | Transformers, custom models, embeddings | NLP demo app, Image classifier |
| **Advanced** | LLM chatbots, RAG, streaming, fragments | Full chatbot, RAG QA system |
| **Expert** | Custom components, Docker, production patterns | Production ML platform |

---

## 📚 Resources

- Official Docs: https://docs.streamlit.io
- Streamlit Gallery: https://streamlit.io/gallery
- Community Forum: https://discuss.streamlit.io
- GitHub: https://github.com/streamlit/streamlit
- Cheatsheet: https://docs.streamlit.io/develop/quick-reference/cheat-sheet

---

*Notes compiled for AI/ML practitioners — from zero to production. Happy building! 🚀*

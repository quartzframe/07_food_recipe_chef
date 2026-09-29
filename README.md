# Recipe Chef

A standalone chatbot starter focused on **Recipe Chef**.

## Model
Uses Google Gemini API model:

`gemini-3.1-flash-lite`

Google documents this as a GA workhorse model optimized for speed, scale, and cost efficiency.

## Setup

1. Install Python 3.10+.
2. Create a Gemini API key.
3. Copy `.env.example` to `.env`.
4. Put your key in `GEMINI_API_KEY`.
5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run:

```bash
python app.py
```

Then open the local URL shown by Gradio.

## Files

- `app.py` - chatbot UI and Gemini API integration
- `system_prompt.txt` - domain-specific assistant behavior
- `.env.example` - environment variable template
- `requirements.txt` - Python dependencies
- `README.md` - setup notes

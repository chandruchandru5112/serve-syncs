# Volunteer Opportunity Finder (Streamlit)

## Run locally
    pip install -r requirements.txt
    streamlit run app.py

## Deploy on Streamlit Community Cloud
1. Create a GitHub repo and upload these files to its root:
   app.py, index.html, requirements.txt
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click "Create app" -> pick the repo and branch.
4. Set "Main file path" to app.py and click Deploy.

## Notes
- Data is saved in each visitor's browser (localStorage), not on the server.
- If the embedded view is cut off, raise `height=1400` in app.py.

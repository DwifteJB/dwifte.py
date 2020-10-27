print("Removing files except config")
rm -r -f *.py *.txt *.sh cogs data *.md app.json update.json
git clone https://github.com/DwifteJB/dwifte.py temp
rm -f temp/config.json
mv temp/* ./

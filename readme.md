# Setup instructions

1. Turn on mysql server
2. Setup database and tables by running `music_store/db/create_db.py`
```
pip install -r requirements.txt
cd db/
python create_db.py
```
3. Go back to projects root directory and install node dependencies.
```
cd ..
cd music_app/
npm install
```

4. You can start the server by running :
```
node app.js
```

5. Access the web page from http://localhost:3000

# Screenshots
![Homepage](https://raw.githubusercontent.com/alella/music_store/master/screenshots/scrotIt0MR.png)
![search](https://raw.githubusercontent.com/alella/music_store/master/screenshots/scrotV3Urf.png)

# Accounts
**Admin**  
username: `admin`  
password: `admin1234`

**test user**  
username: `user`  
password: `user1234`

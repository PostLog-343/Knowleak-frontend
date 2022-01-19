import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCgXEuWZT2h3it6HiWJDaqBOvlDwex5kvo",
  "authDomain": "knowleak-2d7a7.firebaseapp.com",
  "databaseURL": "https://knowleak-2d7a7-default-rtdb.firebaseio.com",
  "projectId": "knowleak-2d7a7",
  "storageBucket": "knowleak-2d7a7.appspot.com",
  "messagingSenderId": "274559070657",
  "appId": "1:274559070657:web:e1f19f431690782c17bf40",
  "measurementId": "G-PZ1HH9M194"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

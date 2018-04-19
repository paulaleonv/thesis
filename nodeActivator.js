// connect to db
var firebase = require("firebase/app");
require("firebase/auth");
require("firebase/database");
require("firebase/firestore");
require("firebase/messaging");
require("firebase/functions");

// Leave out Storage
//require("firebase/storage");

// Initialize Firebase
const config = {
  apiKey: "AIzaSyCCMRS8jPtvNUy_w5dRqn2xsMZsOmP5SK4",
  authDomain: "dreamarchive-a89e5.firebaseapp.com",
  databaseURL: "https://dreamarchive-a89e5.firebaseio.com",
  projectId: "dreamarchive-a89e5",
  storageBucket: "dreamarchive-a89e5.appspot.com",
  messagingSenderId: "138872739434"
};


//OJO:
firebase.initializeApp(config);
var database = firebase.database();
// let ref = database.ref('newUserDreamsDB');
//why is thus testDB working?
const ref = database.ref('testDB');
console.log("is this database connecting")
ref.on('value', gotData, errData);

// ref.on('value', gotData, errData);

function errData(err) {
  console.log("error!");
  console.log(err);
}

function gotData(data){
  console.log(data.val())

}

// // will be using this somehow
// // Retrieve new posts as they are added to our database

// ref.on("child_added", function(snapshot, prevChildKey) {
//   var newPost = snapshot.val();
//   console.log("Author: " + newPost.author);
//   console.log("Title: " + newPost.title);
//   console.log("Previous Post ID: " + prevChildKey);
// });
//

// execute video gen script wth specific tag

// const { spawn } = require('child_process');
// const ls = spawn('python', ['script_merge_connected.py', tagname]);
//
// ls.stdout.on('data', (data) => {
//   console.log(`stdout: ${data}`);
// });
//
// ls.stderr.on('data', (data) => {
//   console.log(`stderr: ${data}`);
// });
//
// ls.on('close', (code) => {
//   console.log(`child process exited with code ${code}`);
// });

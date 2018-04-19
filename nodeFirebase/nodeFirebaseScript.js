
var firebase = require('firebase');
var firebase = require('firebase/app');
require('firebase/auth');
require('firebase/database');

const { spawn } = require('child_process');


const config = {
  apiKey: "AIzaSyCCMRS8jPtvNUy_w5dRqn2xsMZsOmP5SK4",
  authDomain: "dreamarchive-a89e5.firebaseapp.com",
  databaseURL: "https://dreamarchive-a89e5.firebaseio.com",
  projectId: "dreamarchive-a89e5",
  storageBucket: "dreamarchive-a89e5.appspot.com",
  messagingSenderId: "138872739434"
};
var app = firebase.initializeApp(config);


// we are now conected to firebase and need to create a reference to the exact point in the database from where we want data )depens on you db structure

function makePythonVideo(tag){
  const ls = spawn('python', ['pythonActivator.py', tag]);
  //
   ls.stdout.on('data', (data) => {
     console.log(`stdout: ${data}`);
   });
  //
   ls.stderr.on('data', (data) => {
     console.log(`stderr: ${data}`);
   });
  //
   ls.on('close', (code) => {
     console.log(`child process exited with code ${code}`);
   });
}

// somthing like this:
// var adaRef = firebase.database().ref("users/ada");


// with that reference we can then use firebases functions to retireve database
//
// the functions we are interested in are something like

// let ref = database.ref('newUserDreamsDB');
var ref = firebase.database().ref("testDB");

// this function gives us  all in the database once, then nothing else ONCE
 // ref.once("value")
 //   .then(function(snapshot) {
 //     console.log(snapshot.val());
 //   });

// ... to get data once (eg all daata in the beginning)

// and something like this


// orginal function that gives us every data point once in the begginen and then fires for each new child child added
 // ref.on("child_added", function(snapshot, prevChildKey) {
 //   var newPost = snapshot.val();
 //   console.log("body: " + newPost.body);
 //   console.log("title: " + newPost.title);
 //   console.log("tags:" + newPost.tag);
 //   console.log("id " + prevChildKey);
 // });



let durationOfDataWeDontWantToProcess = 6000; // milliseconds
let timeAtStart = new Date();

function cleanPunctuation (c) {
  return c.replace(/[^A-Za-z0-9_]/g," ");
}
function getWordsInDreamAsCSVstring(dream){
  let array = cleanPunctuation(dream).split(" ");
  array = array.filter(function(word){return word.length > 0});
  return array.join(",")

}




ref.on("child_added", function(snapshot, prevChildKey) {
   console.log("got a datapoint");
   let currentTime = new Date();
   if(currentTime - timeAtStart < durationOfDataWeDontWantToProcess){

     console.log("----->I bet this is old data!!")
     // we wouldnt want to make a new video for this old datapoint
   }else{
     console.log("THIS MUS BE NEWWWWWWWWWWW");
     // here we would tell python to create  video
     var newPost = snapshot.val();

     console.log("body: " + newPost.body);
     console.log("title: " + newPost.title);
     console.log("tags:" + newPost.tag);
     console.log("id " + prevChildKey);

     wordsInDream = getWordsInDreamAsCSVstring(newPost.body)

     makePythonVideo(wordsInDream)

   }
 });


// //
//
//
// // Test for the existence of certain keys within a DataSnapshot
// var ref = firebase.database().ref("newUserDreamsDB/testDB");
// ref.once("value")
//   .then(function(snapshot) {
//     var dreamBody1 = snapshot.child("testDB").val(); // {first:"Ada",last:"Lovelace"}
//     var title1 = snapshot.child("title").val(); // "Ada"
//     var tags1 = snapshot.child("tag").val(); // "Lovelace"
//     console.log("Dream body: " + tags1);
//     console.log("Dream title: " + dreamBody1);
//     console.log("Dream tags:" + title1);
//
//
//   });
//
//




//
// ... to create a event listener for any new data point thats added.
// inside this callback function we would run the python script from this node script using a technique like:

// create a sketch of words in movement
//the words comes from the json file "tags"
//if clicked its the word activates the python video program

var tagWords = [];
var videosTag;
var allWords;

function preload() {
     videosTag = loadJSON("videosWater.json", showTagWords);
     console.log("is tagwords loading?");
  	 console.log("videosTag:" + videosTag);
//just with the videos that are BEGGINING, get the tags

}


function setup() {

  createCanvas(windowWidth, windowHeight);
  //showTagWords();

}

function draw() {

    //background (100,100,100);
  	//opacity(30);
}

function showTagWords() {

  var tagWords2 = videosTag.videos[0].tags;

  //console.log("number of videos: " + videosTag.videos.length);

  //for (i=0; i<videosTag.length[i].tags; i++) {


  // iterate over all the videos
  for (var i = 0; i < videosTag.videos.length; i++) {

    console.log("i" + i);
    console.log ("videotag" + videosTag.videos[i].id)
    console.log ("videotag" + videosTag.videos[i].sequencePosition.length)
    // for every video iterate over all the sequencePositions
    for (var j = 0; j < videosTag.videos[i].sequencePosition.length; j++) {

      //check if this sequencePosition is a beginning
      if (videosTag.videos[i].sequencePosition[j] == "beggining") {
        console.log("beginning!!");
        text(videosTag.videos[i].tags[0], 20,20, 20,20);
//      } else {
        //console.log("not beginning: " + videosTag.videos.sequencePosition[j])
      } //en of for loop3
    } //end of for loop2

  } //end of for loop1



  //fill(200,0,0);
	//textSize(22);
	//textFont('Avenir');
  //text(i, 30, 20, 20, 30);
 // }

 // fill(200,0,0);
//	textSize(22);
//	textFont('Avenir');
//  text(tagWords2, 30, 20, 20, 30);
//  console.log("tagWords:" + tagWords);
  //console.log("testing2");

}
//end of functionshowTagWords ()


//showTagWords ();

//create a function to connect with the program

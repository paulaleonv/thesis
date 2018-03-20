// create a sketch of words in movement
//the words comes from the json file "tags"
//if clicked its the word activates the

var words = [];
var videosTag;
var allWords;

function preload() {
     videosTag = loadJSON("videosWater.json")
     console.log("is tagwords loading?");
  	 console.log(videosTag);
//just with the videos that are BEGGINING, get the tags

}
function setup() {
  createCanvas(windowWidth, windowHeight);

  showTagWords ();
}


function showTagWords () {
  var tagWords = videosTag.videos[6].tags;
  //var tagWords2 = videosTag.videos[i].tags;

  for (i=0; i<tagWords.length[i]; i++) {
    console.log(tagwords2);
    text(i, 100, 50, 50, 50);
    console.log("qué esta pasando aquí");
  }

  fill(200,0,0);
	textSize(22);
	textFont('Avenir');
  text(tagWords, 30, 20, 20, 30);
  console.log(tagWords);
  console.log("testing2");
}

 console.log("testing");
//showTagWords ();

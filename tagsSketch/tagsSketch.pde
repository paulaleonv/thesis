JSONArray json;
//JSONObject json;
//JSONArray values;
float videos;

String[] words;
String[] begginingTags;

void setup() {
  //no se como cargarlo, si como json array o como json object. como array me dice que necesita [
  json = loadJSONArray("videos.json");
  println("is the json loading!");
  size(1080, 800, P3D);
  //fullScreen(P3D);
  noStroke();
  textFont(createFont("Avenir Next Condensed", 22));
  textAlign(LEFT);

  frameRate(30);

}
//end of setup

//function to select all the tag words in videos.json that in "sequencePosition" has "beggining"
//create space between the words, take out "," and distribute them in space.
void showTagWords() {
 
  //iniciación de for loop y funcion.
  
}


//funtion to connect sketch with the python program
void clickedWord() {
 
  
}
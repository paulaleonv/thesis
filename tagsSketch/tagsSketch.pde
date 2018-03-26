

//empty array to store the tags of all of the videos
//that are a beginning
//String[] beginningTags;
StringList beginningTags = new StringList();

//declare json object
JSONObject json;

//example numbers inside of the json object
String[] exampleNumbers = {"example0", "example1"};

String[] videos;

void setup() {
  //no se como cargarlo, si como json array o como json object. como array me dice que necesita [
  //load the json file
  json = loadJSONObject("videos.json");
  println("is the json loading!");
  //println(json);

  //retrieve the videos json array
  JSONArray videos = json.getJSONArray("videos");
  //println(videos);

  //iterate over the array
  for (int i = 0; i < videos.size(); i++) { 
    //retrieve every json object inside of the array
    //println(videos.getJSONObject(i));

    //println(videos.getJSONObject(i).getJSONArray("sequencePosition"));

    //iterate every sequencePosition of every video
    for (int j = 0; j < videos.getJSONObject(i).getJSONArray("sequencePosition").size(); j++) {
      //println(videos.getJSONObject(i).getJSONArray("sequencePosition").getString(j));

      //check if any of the sequenceposition tags inside of every video are beginning
      if (videos.getJSONObject(i).getJSONArray("sequencePosition").getString(j).equals("beginning")) {
        //add all of the tags of this video to the beginningTags array
        //println(videos.getJSONObject(i).getJSONArray("tags"));
        for (int k = 0; k < videos.getJSONObject(i).getJSONArray("tags").size(); k++) {
          println(videos.getJSONObject(i).getJSONArray("tags").getString(k));

          //just add the tag if the tag is not already in the StringList beginningTags
          //the first one just gets added
          //THIS LAST PART DOES NOT WORK
          //if (beginningTags.size() == 0) {
          //  beginningTags.append(videos.getJSONObject(i).getJSONArray("tags").getString(k));
          //} else {
          //  for (int m = 0; m < beginningTags.size(); m++) {
          //    if (!beginningTags.get(m).equals(videos.getJSONObject(i).getJSONArray("tags").getString(k))) {
          //      beginningTags.append(videos.getJSONObject(i).getJSONArray("tags").getString(k));
          //    }
          //  }
          //}
        }
      }
    }
  }


  println(beginningTags.size());

  size(1080, 800, P3D);
  //fullScreen(P3D);
  noStroke();
  textFont(createFont("Avenir Next Condensed", 22));
  textAlign(LEFT);

  frameRate(30);
  //retrieve each example inside of examples
  //JSONObject testVideo = videos[0].getJSONObject("tags");
  //println(testVideo);

  //String[] tags = videos.getString("tags");
  //String exampleString1 = example1.getString("exampleString");
  //String exampleString0 = videos.getString("tags");
  //String exampleString1 = example1.getString("exampleString");
  //println(tags);
};
//end of setup


void draw() {
};

















//function to select all the tag words in videos.json that in "sequencePosition" has "beginning"
//create space between the words, take out "," and distribute them in space.
void showTagWords() {

  //iniciacion de for loop y function.
};


//function to connect sketch with the python program
void clickedWord() {
}
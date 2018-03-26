
//texts to display
String[] poem = new String[8];

//numberLines has the same length as the poem array
//in this case, there are seven items
int[] numberLines = {3, 12, 15, 12, 10, 20, 2, 1};

String words = " ";

//maximum number of files
int maxNumberFiles = 5000;
String initialInputFile = "private/currentInput";
String currentInputFile = initialInputFile + ".txt";

String[] files = new String[2];

//speeds of movement of texts
float[] speeds = new float[7];
//there are seven speed increments
float[] speedDeltas = {-0.9,-0.009, -0.01, 0.007, 0.009, 0.03, -0.013};

int fontinc = 0;



//PVector array for translate
PVector[] translations = new PVector[8];
//PVector array for rotation
PVector[] rotations = new PVector[8];
//array for colors
color[] colors = new color[8];
//array for positions
PVector[] positions = new PVector[8];


void setup() {

  size(1080, 800, P3D);
  //fullScreen(P3D);
  noStroke();

  textFont(createFont("Avenir Next Condensed", 22));
  textAlign(LEFT);

  frameRate(30);
   
  files[0] = "private/dreams_curation.txt";
  files[1] = currentInputFile;

  // setting up the matched sentences of dreams, through markov


  //initialize poems to be a single space character
  for (int i = 0; i < poem.length; i++) {
    poem[i] = (" ");
  }
  setupPosition();
  setupTranslation();
  setupRotation();
  setupColor();
}

void draw() {

  //reset hasLoaded so that every
  //4 mins it is false again
  // so that setupMarkov() runs again

  //check if we need to reset
  if (millis() - lastReset > deltaMinutes * 60 * 1000) {
    lastReset = millis();
    hasLoaded = false;
    println("resetted");
  }

  setupMarkov();

  //black background
  background(0);

  lights();

  ////draw the poems
  //for (int i = 0; i < poem.length; i++) {
  for (int i = 0; i < 7; i++) {
    pushMatrix();
    //translate
    translate(translations[i].x, translations[i].y, translations[i].z);
    //rotateX
    rotateX(rotations[i].x);
    //rotateY
    rotateY(rotations[i].y);
    //rotateZ
    rotateZ(rotations[i].z);
    //translate(-width, -height, 0);
    //fill
    fill(colors[i]);
    //textFont
    //textFont(createFont("Avenir Next Condensed", 12));
    //text
    //text(poem[i], positions[i].x, positions[i].y*-speeds[i], positions[i].z, 500);
    
    //OJO CON ESTA LINEA, PREGUNTARLE A AARON 
    text(poem[i], width/2-width/3, 30*-speeds[i], 500, 500);

    popMatrix();
  }
  
  
  ////Draw text to the center of the screen
  ////Incrementing velocity for the rotation of the cube and sphere
  for (int i = 0; i < speeds.length; i++) {
    speeds[i] += speedDeltas[i];
  }

  fontinc++;

  
}

void setupTranslation() {
  //curated sentences / top centered, not readable 
  translations[0] = new PVector(width/7, -height*11.5, 0);
  //rigth low corner
  //translations[0] = new PVector(width, height/5, 0);
  //user sentences/ blue, top, centered
  translations[1] = new PVector(width/6, 0, 0);
  //centered low
  //list of 12 verbs , yellow, left top corner
  translations[2] = new PVector(-width/3, - height/1.8, 0);
  //left low corner
  translations[3] = new PVector(width/1.9, height+500, 0);
  //left buttom corner, grey, nouns 6x4 poem
  translations[4] = new PVector(-300, height/1.5+135, 0);
//adjectives list, buttom centered, adjectives list 24
  translations[5] = new PVector(width/3.6, height/1.2+150, 0);
 // 
  //translations[6] = new PVector(width/1.5, -400, 0);
  translations[6] = new PVector(width,-height, 0);
  translations[7] = new PVector(width/2, height/2+500, 0);
}

void setupMarkov() {
  if (!hasLoaded) {
    if (! ( markov0.ready() && markov1.ready() &&markov2.ready() )) {
      hasLoaded = true;
      return;
    }

    setupPosition();
    setupTranslation();
    setupRotation();
    setupColor();
    
    pickLastFile();

    //reset speeds
    for (int i = 0; i < speeds.length; i++) {
      speeds[i] = 0;
    }

    //PODRÍAMOS HACER UN RESET TRANSLATIONS? 
    x = 50;
    y = 50;

    ///////////
    //poem[0,1]
    ///////////

    //poem0 and poem1 are the long ones
    //todo: poem0 is from one file, poem1 is from a different file
    //poem0 is with curated previous texts
    poem[0] = RiTa.join(markov0.generateSentences(numberLines[0]), " ");
    //poem1 is with input from users
    poem[1] = RiTa.join(markov1.generateSentences(numberLines[1]), " ");
    //Poem[6] is the input from users 
    poem[6] = RiTa.join(markov2.generateSentences(numberLines[6]), " ");
    
    String[] lines = loadStrings(currentInputFile);
    String placeHolder = "";
    for (int i = 0; i < lines.length; i++) {
      placeHolder = trim(placeHolder) + trim(lines[i]);
    }
    //make a list of all the words in the file

    String[] lineList = splitTokens(placeHolder, ". ");

    ///////////
    //poem[2,3]
    ///////////
    
    //poem2 is a list of 24 verbs
    //poem3 is 6 lines of 4 verbs each
    //load the files

    //create new string list
    String[] verbs = new String[1];
    verbs[0] = " ";
    for (int i = 0; i < lineList.length; i++) {
      if (RiTa.isVerb(lineList[i])) {
        boolean isRepeated = false;
        for (int j = 0; j < verbs.length; j++) {
          if (lineList[i].equals(verbs[j])) {
            isRepeated = true;
          }
        }
        if (!isRepeated) {
          verbs = append(verbs, lineList[i]);
        }
      }
    }

    //we take 24 random ones
     int randomVerbsNumber = 24;
    //int randomVerbsNumber1 = 12;
    //int randomVerbsNumber2 = 24;
    String[] randomVerbs2 = new String[randomVerbsNumber];
    String[] randomVerbs3 = new String[randomVerbsNumber];

    //pick the random 24 verbs
    for (int i = 0; i < randomVerbs2.length; i++) {
      int auxIndex = int(random(verbs.length));
      randomVerbs2[i] = verbs[auxIndex];
      randomVerbs3[i] = verbs[auxIndex];
    }

    //construct poem2
    poem[2] = "";
    for (int i = 0; i < 12; i++) {
      poem[2] = poem[2] + randomVerbs2[i] + "\n";
    }

    //construct poem3
    poem[3] = "" ;
    //create the six lines
    for (int i = 0; i < 4; i++) {
      //create a line
      for (int j = 0; j < 4; j++) {
        poem[3] = poem[3] + randomVerbs3[4*i+j] + " ";
      }
      poem[3] = poem[3] + "\n";
    }


    /////////
    //poem[4]
    /////////

    //poem4 is made out of nouns or adverbs
    //use lineList
    String[] nouns = new String[1];
    nouns[0] = " ";
    for (int i = 0; i < lineList.length; i++) {
      if (RiTa.isNoun(lineList[i])) {
        boolean isRepeated = false;
        for (int j = 0; j < nouns.length; j++) {
          if (lineList[i].equals(nouns[j])) {
            isRepeated = true;
          }
        }
        if (!isRepeated) {
          nouns = append(nouns, lineList[i]);
        }
      }
    }

    //we take 24 random nouns
    int randomNounsNumber = 24;
    String[] randomNouns = new String[randomNounsNumber];

    //pick the random 24 nouns
    for (int i = 0; i < randomNouns.length; i++) {
      int auxIndex = int(random(nouns.length));
      randomNouns[i] = trim(nouns[auxIndex]);
    }
    //construct poem4
    poem[4] = "" ;
    //create the six lines
    for (int i = 0; i < 6; i++) {
      //create a line
      for (int j = 0; j < 4; j++) {
        poem[4] = poem[4] + randomNouns[4*i+j] + " ";
      }
      poem[4] = poem[4] + "\n";
    }
    print(poem[4]); 


/*
 /////////
    //poem[4] TEST FOR ADVERBS
    /////////
  //poem4 is made out of adverbs
    //use lineList
    String[] adverbs = new String[1];
    adverbs[0] = " ";
    for (int i = 0; i < lineList.length; i++) {
      if (RiTa.isAdverb(lineList[i])) {
        boolean isRepeated = false;
        for (int j = 0; j < adverbs.length; j++) {
          if (lineList[i].equals(adverbs[j])) {
            isRepeated = true;
          }
        }
        if (!isRepeated) {
          adverbs = append(adverbs, lineList[i]);
        }
      }
    }

    //we take 24 random nouns
    int randomAdverbsNumber = 24;
    String[] randomAdverbs = new String[randomAdverbsNumber];

    //pick the random 24 nouns
    for (int i = 0; i < randomAdverbs.length; i++) {
      int auxIndex = int(random(adverbs.length));
      randomAdverbs[i] = trim(adverbs[auxIndex]);
    }
    //construct poem4
    poem[4] = "" ;
    //create the six lines
    for (int i = 0; i < 6; i++) {
      //create a line
      for (int j = 0; j < 4; j++) {
        poem[4] = poem[4] + randomAdverbs[4*i+j] + " ";
      }
      poem[4] = poem[4] + "\n";
    }
    print(poem[4]); 


*/





    /////////
    //poem[5]
    /////////

    //poem5 is made out of adjectives
    //use lineList
    String[] adjectives = new String[1];
    //OJO QUE CAMBIE AQUI NOUND POR ADJECTIVES PARA PROBAR
    //nouns[0] = " ";
     adjectives[0] = " ";
    for (int i = 0; i < lineList.length; i++) {
      if (RiTa.isAdjective(lineList[i])) {
        boolean isRepeated = false;
        for (int j = 0; j < adjectives.length; j++) {
          if (lineList[i].equals(adjectives[j])) {
            isRepeated = true;
          }
        }
        if (!isRepeated) {
          adjectives = append(adjectives, lineList[i]);
        }
      }
    }

    //we take 24 random nouns
    int randomAdjectivesNumber = 24;
    String[] randomAdjectives = new String[randomAdjectivesNumber];

    //pick the random 24 nouns
    for (int i = 0; i < randomAdjectives.length; i++) {
      int auxIndex = int(random(adjectives.length));
      randomAdjectives[i] = trim(adjectives[auxIndex]);
    }
    //construct poem5
    poem[5] = "" ;
    for (int i = 0; i < 24; i++) {
      poem[5] = poem[5] + randomAdjectives[i] + "\n";
    }


    hasLoaded = true;
  }
}

void setupRotation() {
  rotations[0] = new PVector(radians(-30 + speeds[0]), 0, 0);
  rotations[1] = new PVector(radians(45 - speeds[5]), 0, 0);
  rotations[2] = new PVector(radians(18 * speeds[2]), radians(40), radians(-40));
  rotations[3] = new PVector(radians(65), 0, 0);
  rotations[4] = new PVector(radians(55), radians(30),radians(30));
  rotations[5] = new PVector(radians(-30), radians(30), radians(30));
  //rotations[6] = new PVector(radians(35 + speeds[6]), radians(5), radians(50));
  rotations[6] = new PVector(radians(15 + speeds[6]), radians(10), radians(45));
  rotations[7] = new PVector(0, 0, 0);
}

void setupColor() {
  colors[0] = color(130, 130, 130);
  colors[1] = color(13, 91, 126);
  colors[2] = color(0, 49, 105);
  colors[3] = color(85, 211, 216);
  colors[4] = color(100, 100, 100);
  colors[5] = color(6, 107, 130);
  colors[6] = color(180,180,180);
  colors[7] = color(255, 0, 0);
}

void setupPosition() {
  //poem in the rigth low corner
  positions[0] = new PVector(0, 0, 0);
  //positions[0] = new PVector(width/2, height * speeds[5], 300);
  //poem (red for now//I want to change it´s direction)
  positions[1] = new PVector(0, 0, 0);
  positions[2] = new PVector(0, 0, 0);
  //peom inleft low corner
  positions[3] = new PVector(0, 800, 0);
  //poem in right left corner
  positions[4] = new PVector(0, 0, 0);
  positions[5] = new PVector(0, 0, 0);
  positions[6] = new PVector(0, 0, 0);
  positions[7] = new PVector(255,0,0);
}

void pickLastFile() {
  
  int counter = 1;
  
  //while (counter < maxNumberFiles ){
  //  String aux = initialInputFile + char(' ') + "(" + counter + ")" +  ".txt";
  //  println(aux);
  //  File f = new File(aux);
  //  if (f.exists()) {
  //    currentInputFile = aux;
  //  }
  //  else {
  //    println("picked: " + counter);
  //    files[1] = currentInputFile;
  //    return; 
  //  }
  //  counter++;
  //}
  
  
  while (counter < maxNumberFiles ){
    String aux = initialInputFile + char(' ') + "(" + counter + ")" +  ".txt";
    println(aux);
    if (loadStrings(aux) != null) {
      currentInputFile = aux;
      counter++;
    }
    else {
      println("picked: " + currentInputFile);
      files[1] = currentInputFile;
      return; 
    }
  }
}
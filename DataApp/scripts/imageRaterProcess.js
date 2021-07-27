//Slider Values
var slider = document.getElementById("catRateSlider");
var output = document.getElementById("sliderVal");
output.innerHTML = slider.value;

slider.oninput = function displaySlider() {
  output.innerHTML = this.value;
}

function displaySlider() {
    output.innerHTML = '5';
  }

var obj_csv = {
    size:0,
    dataFile:[]
};
 
function readFile(input) {
    console.log(input)
    if (input.files && input.files[0]) {
        let reader = new FileReader();
            reader.readAsBinaryString(input.files[0]);
        reader.onload = function (e) {
            console.log(e);
            obj_csv.size = e.total;
            obj_csv.dataFile = e.target.result
            console.log(obj_csv.dataFile)
            parseData(obj_csv.dataFile)                
        }
    }
}

let csvData = [];

function parseData(data){    
    let lbreak = data.split("\n");
    lbreak.forEach(res => {
        csvData.push(res.split(","));
    });
    console.table(csvData);
    findNextImage()
    loadNextImage()
}

// Get image
let foundImage = '';
i=1
function findNextImage(){    
    var found = false;    
    while (!found){
        if (csvData[i][2] == 'None'){
            found = true;
            foundImage = csvData[i][1];
        } else{
            i = i+1;
            if (i>=csvData.length){
                console.log('All Images Rated in file');
            }
        }
    }
}

// Load image
function loadNextImage(){
    var image = document.querySelector('#catImage');
    var downloadingImage = new Image();
    downloadingImage.onload = function(){
        image.src = this.src;   
    };
    downloadingImage.src = foundImage;
}

//Submit Rating
// Execute a function when the user releases a key on the keyboard
document.addEventListener("keyup", function(event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.key === 'Enter' || event.key === ' ') {
      // Cancel the default action, if needed
      event.preventDefault();
      // Trigger the button element with a click
      document.getElementById("Submit").click();
    }
  });
function memeClicked(){
    var imageType = 'meme';
    submitRating()
}
function notACatClicked(){
    var imageType = 'notCat';
    submitRating()
}
function submitRating(){
    var imageType = '';
    if (imageType == ''){
        imageType = 'cat';
    }
    var imageData = document.querySelector('.dataContainer');
    csvData[i][2] = imageData.querySelector('#catRateSlider').value;
    imageData.querySelector('#catRateSlider').value = '5'
    displaySlider()
    var colours = '';
    var colourOptions = imageData.getElementsByClassName('colourOptionsContainer')[0].children;
    for (var j = 0; j < colourOptions.length; j++) {
        if (colourOptions[j].classList[2] == 'checked'){
            if (j+1 == colourOptions.length){
                colours = colours + "-" + imageData.querySelector('.other input[type=text]').value;
            }else{
                colours = colours + "-" + colourOptions[j].classList[0];
            }            
            colourOptions[j].classList.toggle('checked')
        }
    } 
    csvData[i][3] = colours;
    csvData[i][4] = imageType;
    findNextImage()
    loadNextImage()
}

function export_csv(){
    let csv = '';
    csvData.forEach( array => {
        csv += array.join(',')+"\n";
    });
  
    let data = new Blob([csv], { type: 'text/csv' });  
    let csvUrl = URL.createObjectURL(data);
  
    let hiddenElement = document.createElement('a');
    hiddenElement.href = csvUrl;
    hiddenElement.target = '_blank';
    hiddenElement.download = 'CatPicURLs' + '.csv';
    hiddenElement.click();
  }
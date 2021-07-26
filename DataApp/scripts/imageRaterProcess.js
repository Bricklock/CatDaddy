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
function findNextImage(){
    var found = false;
    var i = 1;
    while (!found){
        if (csvData[1][2] == 'None\r'){
            found = true;
            foundImage = csvData[1][1];
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

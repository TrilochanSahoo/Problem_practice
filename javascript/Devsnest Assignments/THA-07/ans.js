// Q-1 - Write a JavaScript program to list the properties of a JavaScript object. Sample object: var student = { name : "David Rayy", sclass : "VI", rollno : 12 }
var student = {
    name : "David Rayy",
    sclass : "VI",
    rollno : 12
}
// console.log(Object.keys(student))

// Q-2 - Write a JavaScript program to delete the rollno property from the following object. Also print the object before or after deleting the property.
// console.log(student)
// delete student.rollno
// console.log(student)

// Q-3 - Write a JavaScript program to get the length of a JavaScript object. 
function size(obj){
    let size = 0
    for (key in obj){
        if(obj.hasOwnProperty(key)){
            size = size+1
        }
    }
    return size
}
// console.log(size(student))

// Q-4 - Write a JavaScript program to display the reading status (i.e. display book name, author name and reading status) of the following books. var library = [ { author: 'Bill Gates', title: 'The Road Ahead', readingStatus: true }, { author: 'Steve Jobs', title: 'Walter Isaacson', readingStatus: true }, { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', readingStatus: false }]

var library = [ { 
        author: 'Bill Gates',
        title: 'The Road Ahead', 
        readingStatus: true 
    }, 
    {   
        author: 'Steve Jobs', 
        title: 'Walter Isaacson', 
        readingStatus: true 
    }, 
    { 
        author: 'Suzanne Collins',
        title: 'Mockingjay: The Final Book of The Hunger Games', 
        readingStatus: false 
    }]

for (item in library){
    // console.log("Book Name : "+library[item].title)
    // console.log("Author Name : "+library[item].author)
    // console.log("Reading Status : "+library[item].readingStatus)
} 

// Q-5 - Write a JavaScript program to get the volume of a Cylinder with four decimal places using object classes. Volume of a cylinder : V = πr2h where r is the radius and h is the height of the cylinder.
var cylinder = {
    r : 23,
    h : 54
}
cylinder.volume = (Math.PI*cylinder.r*2*cylinder.h).toFixed(4)
// console.log(cylinder.volume)

// Q-6 -  Write a JavaScript program to sort an array of JavaScript objects.  Sample Object : var library = [ { title: 'The Road Ahead', author: 'Bill Gates', libraryID: 1254 }, { title: 'Walter Isaacson', author: 'Steve Jobs', libraryID: 4264 }, { title: 'Mockingjay: The Final Book of The Hunger Games', author: 'Suzanne Collins', libraryID: 3245 }]; Expected Output: [[object Object] { author: "Walter Isaacson", libraryID: 4264, title: "Steve Jobs" }, [object Object] { author: "Suzanne Collins", libraryID: 3245, title: "Mockingjay: The Final Book of The Hunger Games" }, [object Object] { author: "The Road Ahead", libraryID: 1254, title: "Bill Gates" }]

var library = [{ 
    title: 'The Road Ahead', 
    author: 'Bill Gates', 
    libraryID: 1254 
},{ 
    title: 'Walter Isaacson', 
    author: 'Steve Jobs', 
    libraryID: 4264 
},{ 
    title: 'Mockingjay: The Final Book of The Hunger Games', 
    author: 'Suzanne Collins', 
    libraryID: 3245 
}]

let ordered = []
let lib =[],i=0

for (item of library){
    ordered.push(Object.keys(item).sort().reduce((obj, key)=>{
        obj[key] = item[key]
        return obj
    },{}))
    // console.log(ordered)
    lib.push(item.libraryID)
}
lib.sort((a,b)=>{
    return b-a
})
for (num of lib){
    for( item of ordered){
        if(item.libraryID===num){
            library[i]=item
        }
    }
    i+=1
}
console.log(library)
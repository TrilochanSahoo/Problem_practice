// Q - union and intersection of two sorted array 
var userInput1 = prompt("Enter first array : ")
var userInput2 = prompt("Enter second array : ")
let arr1 = userInput1.split(",")
for (let i = 0;i<arr1.length;i++){
    arr1[i] = parseInt(arr1[i])
}
document.write(arr1)
console.log(arr1)
let arr2 = userInput2.split(",")
for (let i = 0;i<arr2.length;i++){
    arr2[i] = parseInt(arr2[i])
}
document.write(arr2)
console.log(arr2)


// union 
let unionArr = []
arr1.forEach(function(element){
    if(!(unionArr.indexOf(element)!==-1)){
        unionArr.push(element)
    }
})
arr2.forEach(function(element){
    if(!(unionArr.indexOf(element)!==-1)){
        unionArr.push(element)
    }
})
// document.write(unionArr)
console.log(unionArr)


// intersection 
let intersectionArr = []
arr1.forEach(function(element){
    arr2.forEach(function(ele){
        if(element==ele){
            intersectionArr.push(element)
        }
    })
})
console.log(intersectionArr)


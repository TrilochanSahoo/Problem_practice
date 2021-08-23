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
let i,j = 0
while((i != arr1.length) || (j != arr2.length)){
    if(arr1[i]<arr2[j]){
        unionArr.push(arr1[i])
        i++
    }else if(arr1[i]==arr2[j]){
        unionArr.push(arr1[i])
        i++
        j++
    }else{
        unionArr.push(arr2[j])
        j++
    }
}
document.write(unionArr)
console.log(unionArr)

// intersection 
let intersectionArr = []
i,j = 0
while((i != arr1.length) || (j != arr2.length)){
    if(arr1[i]==arr2[j]){
        intersectionArr.push(arr1)
    }
    i++
    j++
}
console.log(intersectionArr)


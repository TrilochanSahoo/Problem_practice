// Q - cyclically rotate an array by one 
var userInput = prompt("Enter array : ")
let arr = userInput.split(",")
for (let i = 0;i<arr.length;i++){
    arr[i] = parseInt(arr[i])
}
console.log(arr)
console.log(arr.length)

function rotate(arr,length){
    let temp = arr[length-1]
    for(let i = length - 1 ; i > 0 ; i--){
        arr[i]=arr[i-1]
    }
    arr[0] = temp
    return arr
}
console.log(rotate(arr,arr.length))
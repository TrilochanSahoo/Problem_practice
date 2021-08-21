var userInput = prompt("Enter an array of numbers : ")
let arr, min, max
arr = userInput.split(",")
console.log(arr)
for (i in arr){
    arr[i] = parseInt(arr[i])
}

console.log(arr)

if(arr[0]>arr[1]){
    min = arr[1]
    max = arr[0]
}else{
    min = arr[0]
    max = arr[1]
}
for (let i=2;i<arr.length;i++){
    if(arr[i]<min){
        min = arr[i]
    }
    else if(arr[i]>max){
        max = arr[i]
    }
}
console.log("max is :"+max)
console.log("min is :"+min)

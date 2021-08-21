var userInput = prompt("Enter an array :")
let arr=[]
for (i of userInput){
    arr.push(i)
}
console.log(arr)

let start=0,end=arr.length-1

for (let i=0;i<arr.length/2;i++){
    let temp = 0
    if(end<start){
        break
    }
    else{
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start++
        end--
    }
}

console.log(arr)
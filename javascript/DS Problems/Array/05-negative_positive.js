// Q- move negative integer to one side and positive to one side 

var userInput = prompt("Enter array")
let arr = userInput.split(",")
// console.log(arr)
for (let i = 0;i<arr.length;i++){
    arr[i] = parseInt(arr[i])
}
// console.log(arr)

function arrange(arr){
    let j = 0
    for(let i = 0 ; i < arr.length ; i++){
        if(arr[i]<0){
            if(i != j){
                let temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            }
            j++
        }
    }
    document.write(arr)
}

arrange(arr)
// Q - minimize the maximize difference heights

var userInput = prompt("Enter array : ")
var k = parseInt(prompt("Enter k value : "))
let arr = userInput.split(",")
for (let i = 0;i<arr.length;i++){
    arr[i] = parseInt(arr[i])
}

function getMinDiff(arr,k){
    let n = arr.length
    // console.log(arr)
    let diff = arr[n-1]-arr[0]
    let minimum = arr[0] + k
    let maximum = arr[n-1] - k
    let temp = 0
    if(minimum>maximum){
        temp = maximum
        maximum = minimum
        minimum = temp
    }

    for (let i=1;i<arr.length-1;i++){
        let difference = arr[i]-k
        let sum = arr[i] + k
        if(difference>=minimum || sum<=maximum){
            continue
        }
        if(maximum-difference <= sum-minimum){
            minimum = difference
        }
        else{
            maximum = sum
        }
    }
    return Math.min(diff,maximum-minimum)
}

console.log(getMinDiff(arr,k))
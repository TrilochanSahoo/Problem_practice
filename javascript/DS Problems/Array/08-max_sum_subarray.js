// Q - Largest sum contiguous subarray (Kadane's Algorithm)
var userInput = prompt("Enter array : ")
let arr = userInput.split(",")
for (let i = 0;i<arr.length;i++){
    arr[i] = parseInt(arr[i])
}

console.log(arr)

function maxSubArray(arr){
    let current_max = arr[0]
    let max_so_far = arr[0]
    for (let i = 1; i < arr.length; i++) {
        current_max = Math.max(arr[i],(current_max+arr[i]))
        console.log(current_max)
        max_so_far = Math.max(max_so_far,current_max)
        console.log(max_so_far)
    }
    return max_so_far
}

console.log(maxSubArray(arr))
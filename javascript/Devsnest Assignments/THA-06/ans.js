// Q-1
input1 = "w3resourse"
input2 = [1, 2, 4, 0]

// console.log(Array.isArray(input1))
// console.log(Array.isArray(input2))

// Q-2
// console.log([1, 2, 6, 0].slice())
// console.log([1, 2, [4, 0]].slice())

// Q-3
function first(arr,para){
    let temp = []
    for(var i = 0;i<para;i++){
        if(arr[i]===undefined){
        }else{
            temp.push(arr[i])
        }
    }
    return temp
}


// console.log([7,9,0,-2].shift())
// console.log([[], 3].shift())
// console.log(first([7,9,0,-2],3))
// console.log(first([7,9,0,-2],6))
// console.log(first([7,9,0,-2],-3))

// Q-4
var myColor = ["Red", "Green", "White", "Black"]
// console.log(myColor.join(" "))
// console.log(myColor.join(","))
// console.log(myColor.join("+"))

// Q-5
function maximum_times(arr){
    let temp = [...new Set(arr)]
    let maxList = []
    for(let i=0;i<temp.length;i++){
        let count = 0
        for(let j=0;j<arr.length;j++){
            if(temp[i]==arr[j]){
                count+=1
            }
        }
        maxList.push(count)
    }
    var flag=maxList.indexOf(Math.max(...maxList))
    console.log("maximum times "+temp[flag]+" is present"+maxList[flag])
    
}

var samp = [3,'a','a','a',2,3,'a',3,'a',2,4,9,3]
maximum_times(samp)
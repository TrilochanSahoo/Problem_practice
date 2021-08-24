// stack example- word is a palindrome word or not 

var letters = []
var word = "racecar"
var revWord = ""

for(var i = 0; i<word.length;i++){
    letters.push(word[i])
}

for(var i = 0 ; i<word.length;i++){
    revWord = revWord+ letters.pop()
}

if(word === revWord){
    console.log(word+"is a palindrome word.")
}
else{
    console.log(word+"is not a palindrome word.")
}
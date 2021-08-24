var Stack = function(){
    this.storage = []
    this.count = 0

    // push element into the array 
    this.push = function(value){
        this.storage[this.count] = value
        this.count++
    }

    // remove element from the last 
    this.pop = function(){
        if(this.count==0){
            return undefined
        }
        this.count--
        var result = this.storage[this.count]
        delete this.storage[this.count]
        return result
    }

    this.size = function(){
        return this.count
    }

    // last Element in the array 
    this.peek = function(){
        return this.storage[this.count-1]
    }
}

var myStack = new Stack()
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.push(7)
myStack.push(3)
console.log(myStack.storage)
myStack.pop()
myStack.pop()
console.log(myStack.storage)
console.log(myStack.peek())
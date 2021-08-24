// set = array having no duplicate element 
function mySet(){
    var storage = []

    // check element is present or not 
    this.has = function(element){
        return (storage.indexOf(element)!==-1) 
    }

    // return Array element 
    this.value = function(){
        return storage
    }

    // add element to the array 
    this.add = function (element){
        if(!this.has(element)){
            storage.push(element)
            return true
        }
        return false
    }

    // delete an element in the Array 
    this.remove = function(element){
        if(this.has(element)){
            storage.splice(storage.indexOf(element),1)
            return true
        }
        return false
    }

    // union of two array 
    this.union = function(otherSet){
        var unionSet = new mySet()
        var firstSet = this.value()
        var secondSet = otherSet.value()
        firstSet.forEach(function(element){
            unionSet.add(element)
        })
        secondSet.forEach(function(element){
            unionSet.add(element)
        })
        return unionSet
    }

    // intersection of two array 
    this.intersection = function(otherSet){
        var intersectionSet = new mySet()
        var firstSet = this.value()
        firstSet.forEach(function(element){
            if(otherSet.has(element)){
                intersectionSet.add(element)
            }
        })
        return intersectionSet
    }

    // difference of two array 
    this.difference = function(otherSet){
        var differenceSet = new mySet()
        var firstSet = this.value()
        firstSet.forEach(function(element){
            if(!otherSet.has(element)){
                differenceSet.add(element)
            }
        })
        return differenceSet
    }

    // subset 
    this.subSet = function(otherSet){
        var firstSet = this.value()
        return firstSet.every(function(element){
            return otherSet.has(element) 
        })
    }
}

var setA = new mySet()
var setB = new mySet()

setA.add(2)
setA.add(4)
setB.add(1)
setB.add(4)
setB.add(3)
setB.add(1)
setB.add(2)
console.log(setA.value())
console.log(setB.value())
console.log(setA.subSet(setB))
console.log(setA.intersection(setB).value())
console.log(setB.difference(setA).value())
console.log(setA.union(setB).value())
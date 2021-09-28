const seats = document.querySelectorAll('.seat')
const selected = document.querySelector('.selected')
const remaining = document.querySelector('.remaining')

for (let i=0;i<seats.length;i++){
    seats[i].addEventListener('click',()=>{
        console.log("clicked")
        if(seats[i].classList.contains('active')){
            seats[i].classList.remove('active')
            // console.log(selected.innerText)
            selected.innerText = Number(selected.innerText)-1
            remaining.innerText = Number(remaining.innerText)+1
        }
        else{
            seats[i].classList.add('active')
            // seats[i].innerText = i+1  
            selected.innerText = Number(selected.innerText)+1
            remaining.innerText = Number(remaining.innerText)-1
        }
    })
}
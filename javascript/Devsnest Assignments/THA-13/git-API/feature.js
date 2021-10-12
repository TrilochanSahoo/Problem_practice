const btn = document.getElementById('btn')
const userInput = document.getElementById('userInput')
const section = document.querySelector(".section")

const getData = async (userInput)=>{
    const res = await fetch(`https://api.github.com/users/${userInput}/followers`)
    const data = await res.json()
    return data
}

btn.addEventListener('click', async ()=>{
    let res = getData(userInput.value)
    let user = await res
    let html = ""
    user.map((data)=>{
        // console.log(data.login)
        // // console.log(data.avatar_url)
        // console.log(data.repos_url)
        html += `<div class="card" style="width: 18rem;">
            <img src="${data.avatar_url}" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">${data.login}</h5>
              <a href="${data.repos_url}" class="btn btn-primary">Go to Profile</a>
            </div>
          </div>`
    })
    section.innerHTML = html
    console.log(user)
})
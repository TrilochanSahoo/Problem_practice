var url = "https://opentdb.com/api.php?amount=1";

const questionTitle = document.querySelector('.question_title')
const nextQuestion = document.querySelector('.next')
const choices = document.querySelector('.choices')

const result = (btn)=>{
    let btns = choices.querySelectorAll('button')
    btns.forEach((btn)=>{
        btn.click()
    })
}

const createChoice = (choice, ans)=>{
    console.log(choice)
    const btn = document.createElement("button")
    btn.innerText = choice

    btn.addEventListener("click",()=>{
        if(choice === ans){
            btn.classList.add("correct")
            // if(btn.classList.contains("correct")){

            // }
        }else{
            btn.classList.add("wrong")
        }
        result(btn)
    })
    choices.appendChild(btn)

}
class question{
    constructor(question,answer,...opt){
        this.question = question
        this.answer = answer
        if(opt.length<4){
            this.opt1 = opt[0]
            this.opt2 = opt[1]
        }else{
            this.opt1 = opt[0]
            this.opt2 = opt[1]
            this.opt3 = opt[2]
            this.opt4 = opt[3]
        }
    }
    display(){
        questionTitle.innerHTML = `Q. ${this.question}`
        if(this.opt3===undefined){
            createChoice(this.opt1, this.answer)
            createChoice(this.opt2, this.answer)
        }else{
            createChoice(this.opt1, this.answer)
            createChoice(this.opt2, this.answer)
            createChoice(this.opt3, this.answer)
            createChoice(this.opt4, this.answer)
        }
    }
}
u
function shuffle(array) {
    var i = array.length,
        j = 0,
        temp
    while (i--) {
        j = Math.floor(Math.random() * (i+1))
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
    }
    return array
}

async function getApi(url){
    const res = await fetch(url)
    var data = await res.json()
    console.log(data.results)

    data.results.forEach(ques => {
        let choice = [ques.correct_answer,...ques.incorrect_answers]
        choice = shuffle(choice)
        // const que = new question(ques.question, ques.incorrect_answers[0], ques.incorrect_answers[1], ques.incorrect_answers[2], ques.correct_answer )
        const quiz = new question(ques.question, ques.correct_answer, choice[0],choice[1],choice[2],choice[3])
        quiz.display()
    });
}
nextQuestion.addEventListener('click',()=>{
    choices.innerHTML = ''
    getApi(url)
})

getApi(url)
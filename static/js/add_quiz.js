class NewQuiz{
    constructor() {
        this.quiz = {}
        this.question_count = 0
        this.div = document.getElementById("quiz")
    }

    save_text_question(idx){
        let question = document.getElementById(`question-${idx}`).value
        let answer = document.getElementById(`answer-${idx}`).value
        this.quiz[idx]['question'] = question
        this.quiz[idx]['answer'] = answer.toString(10)
        document.getElementById(`save-${idx}`).innerText = ""
    }

    save_choice_question(idx){
        let question = document.getElementById(`question-${idx}`).value
        let answer = document.getElementsByName(`answer-${idx}`)
        for(let i = 0; i<answer.length; i++){
            if (answer[i].checked) {
                this.quiz[idx]['answer'] = i.toString(10)
                this.quiz[idx]['question'] = question
                for(let j=0; j<this.quiz[idx]['choices'].length; j++) {
                    this.quiz[idx]['choices'][j] = document.getElementById(`${idx}-${j}`).value
                    document.getElementById(`save-${idx}`).innerText = ""
                }
                return
            }
        }
    }

    change_status(idx){
        document.getElementById(`save-${idx}`).innerText = "(NOT SAVED)"
    }

    add_option(idx){
        let HTML_code = `<div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text" id="basic-addon1">${this.quiz[idx]['choices'].length + 1}</span>
                              </div>
                              <input type="text" id="${idx}-${this.quiz[idx]['choices'].length}" class="form-control" placeholder="Enter your option" aria-describedby="basic-addon1" onchange="page.change_status(${idx})">
                              <div class="input-group-append">
                                  <div class="input-group-text">
                                    <input type="radio" name="answer-${idx}" class="" aria-label="Correct answer" value="${this.quiz[idx]['choices'].length}" onchange="page.change_status(${idx})">
                                  </div>
                              </div>
                        </div>`
        this.quiz[idx]['choices'].push("")
        let new_option = document.createElement('div')
        new_option.innerHTML = HTML_code
        document.getElementById(`options-${idx}`).append(new_option)
    }

    generate_text_question(){
        return `<div class="card" style="margin-top: 32px">
                    <div class="card-header">Question ${this.question_count + 1} <span id="save-${this.question_count}">(NOT SAVED)</span></div>
                    <div class="card-body">
                        <textarea class="form-control" rows="5" id="question-${this.question_count}" placeholder="Enter your question" onchange="page.change_status(${this.question_count})"></textarea>
                        <input type='text' id="answer-${this.question_count}" placeholder="Enter right answer for the question" class="form-control question-input" onchange="page.change_status(${this.question_count})">
                        <button type="button" class="btn btn-primary" onclick="page.save_text_question(${this.question_count})">Save</button>
                    </div>
                </div>`
    }

    generate_choice_question(){
        return `<div class="card" style="margin-top: 32px">
                    <div class="card-header">Question ${this.question_count + 1} <span id="save-${this.question_count}">(NOT SAVED)</span></div>
                    <div class="card-body">
                        <textarea class="form-control question-input" rows="5" id="question-${this.question_count}" placeholder="Enter your question" onchange="page.change_status(${this.question_count})"></textarea>
                        <div id="options-${this.question_count}"></div>
                        <button class="btn btn-primary" onclick="page.add_option(${this.question_count})">Add Option</button>
                        <button class="btn btn-primary" onclick="page.save_choice_question(${this.question_count})">Save</button>
                    </div>
                </div>`
    }

    add_question(){
        let selected_option = document.getElementById("questionSelector")
        let question_HTML = document.createElement('div')
        if (selected_option.value == 0){
            this.quiz[this.question_count] = {'type': '0'}
            question_HTML.innerHTML = this.generate_text_question()
            this.question_count++;
        } else if (selected_option.value == 1){
            this.quiz[this.question_count] = {'type': '1', 'choices': []}
            question_HTML.innerHTML = this.generate_choice_question()
            this.question_count++;
        }
        this.div.append(question_HTML)
    }

    post_data(url){
        $.ajax({
            type: "POST",
            url: url,
            data: JSON.stringify(this.quiz),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (url) {
               window.location.replace(url.url);
            },
            error: function (response) {
               alert(response.responseJSON.message);
            }
        });
    }
}

let page = new NewQuiz()


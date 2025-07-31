const send = document.getElementById('send');
let taskList = []

send.addEventListener('click', (e) => {
    const task = document.getElementById('task').value;
    const taskDescription = document.getElementById('taskDescription')
    task.innerHTML = 'Without tasks'
    taskList.push(task)
    console.log(taskList)

    if (task == '') {
        alert('Insert a value')
    } else {

        // Task container
        let taskDescriptionChild = document.createElement('li');

        taskDescription.appendChild(taskDescriptionChild)

        // Styles

        taskDescriptionChild.innerHTML = task;
        taskDescriptionChild.style.backgroundColor = '#000000',
        taskDescriptionChild.style.padding = '20px'
        taskDescriptionChild.style.margin = '10px'
        taskDescriptionChild.style.width = '50vw'


        // Task items
        

        let btnTaskDone = document.createElement('button');
        let btnTaskDelete = document.createElement('button');
        let doneText = document.createElement('p');
        taskDescriptionChild.appendChild(doneText)

        btnTaskDone.textContent = 'Done'
        btnTaskDelete.textContent = 'Delete'
        taskDescriptionChild.appendChild(btnTaskDone);
        taskDescriptionChild.appendChild(btnTaskDelete);

        btnTaskDone.addEventListener('click', (e) => {
            
            doneText.style.padding = '10px'
            doneText.style.backgroundColor = '#555555'
            doneText.style.marginTop = '20px'
            doneText.style.marginBottom = '30px'
            doneText.textContent = 'Done' 
            taskDescriptionChild.style.backgroundColor = '#0000006e'
        })

        // Styles

        btnTaskDone.style.marginLeft = '10px'
        btnTaskDone.style.marginRight = '5px'

        btnTaskDelete.style.marginLeft = '5px'
        btnTaskDelete.style.marginRight = '5px'

        btnTaskDelete.addEventListener('click', (e) => {
            taskDescription.removeChild(taskDescriptionChild)
            taskList.pop(task)
        })

    }
})
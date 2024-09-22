const archiveButtons = document.getElementsByClassName('archive-button');
const activityButtons = document.getElementsByClassName('change-activity-btn');

for(let i = 0; i < activityButtons.length; i++){
    activityButtons[i].addEventListener('change', e => {
        console.log(e.target.checked, e.target.id)
    })
}

for(let i = 0; i < archiveButtons.length; i++){
    archiveButtons[i].addEventListener('click', e => {
        console.log(e.target.id)
    })
}

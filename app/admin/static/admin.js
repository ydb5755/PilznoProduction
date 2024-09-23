const archiveButtons = document.getElementsByClassName('archive-button');
const activityButtons = document.getElementsByClassName('change-activity-btn');




function deactivateArchiveButtons(){
    for (let i = 0; i < archiveButtons.length; i++){
        archiveButtons[i].disabled=true;
    }
}
function activateArchiveButtons(){
    for (let i = 0; i < archiveButtons.length; i++){
        archiveButtons[i].disabled=false;
    }
}
function deactivateActiveStatusCheckboxes(){
    for (let i = 0; i < activityButtons.length; i++){
        activityButtons[i].disabled=true;
    }
}
function activateActiveStatusCheckboxes(){
    for (let i = 0; i < activityButtons.length; i++){
        activityButtons[i].disabled=false;
    }
}

async function updateActiveStatus(id, status) {
    deactivateActiveStatusCheckboxes()
    deactivateArchiveButtons()
    var result = await fetch(`/campaigns/update_active_status/${id}/${status}`, {method:'PUT'});
    var data = await result.json();
    if (status === true){
        status = 'True'
    } else {
        status = 'False'
    }
    document.getElementById(`${id}-active-status`).innerText = status;
    activateActiveStatusCheckboxes()
    activateArchiveButtons()
    
}

async function archiveCampaign(id){
    deactivateActiveStatusCheckboxes()
    deactivateArchiveButtons()
    var result = await fetch(`/campaigns/archive_campaign/${id}`, {method:'PUT'});
    var data = await result.json();
    document.getElementById(`${id}-row`).remove();
    activateActiveStatusCheckboxes()
    activateArchiveButtons()
}

document.addEventListener("DOMContentLoaded", (event) => {
    for(let i = 0; i < activityButtons.length; i++){
        activityButtons[i].addEventListener('change', e => {
            updateActiveStatus(parseInt(e.target.value), e.target.checked)
        })
    }
    for(let i = 0; i < archiveButtons.length; i++){
        archiveButtons[i].addEventListener('click', e => {
            archiveCampaign(parseInt(e.target.value))
        })
    }
  });

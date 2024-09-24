const archiveButtons = document.getElementsByClassName('archive-button');
const activityButtons = document.getElementsByClassName('change-activity-btn');
const adminButtons = document.getElementsByClassName('change-admin-btn');


function deactivateAdminButtons(){
    for (let i = 0; i < adminButtons.length; i++){
        adminButtons[i].disabled=true;
    }
}
function activateAdminButtons(){
    for (let i = 0; i < adminButtons.length; i++){
        adminButtons[i].disabled=false;
    }
}
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

function activateAllButtons(){
    activateAdminButtons()
    activateArchiveButtons()
    activateActiveStatusCheckboxes()
}
function deactivateAllButtons(){
    deactivateAdminButtons()
    deactivateArchiveButtons()
    deactivateActiveStatusCheckboxes()
}

async function updateActiveStatus(id, status) {
    deactivateAllButtons()
    var result = await fetch(`/campaigns/campaign_api/update_active_status/${id}/${status}`, {method:'PUT'});
    var data = await result.json();
    if (status === true){
        status = 'True'
    } else {
        status = 'False'
    }
    document.getElementById(`${id}-active-status`).innerText = status;
    activateAllButtons()
}

async function archiveCampaign(id){
    deactivateAllButtons()
    var result = await fetch(`/campaigns/campaign_api/archive_campaign/${id}`, {method:'PUT'});
    var data = await result.json();
    document.getElementById(`${id}-row`).remove();
    activateAllButtons()
}

async function updateAdminStatus(id, status) {
    deactivateAllButtons()
    var result = await fetch(`/users/users_api/update_admin_status/${id}/${status}`, {method:'PUT'});
    var data = await result.json();
    if (status === true){
        status = 'True'
    } else {
        status = 'False'
    }
    document.getElementById(`${id}-admin-status`).innerText = status;
    activateAllButtons()
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
    for(let i = 0; i < adminButtons.length; i++){
        adminButtons[i].addEventListener('change', e => {
            updateAdminStatus(parseInt(e.target.value), e.target.checked)
        })
    }
  });

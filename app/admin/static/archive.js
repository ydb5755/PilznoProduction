const unArchiveButtons = document.getElementsByClassName('unarchive-button');


function deactivateUnArchiveButtons(){
    for (let i = 0; i < unArchiveButtons.length; i++){
        unArchiveButtons[i].disabled=true;
    }
}
function activateUnArchiveButtons(){
    for (let i = 0; i < unArchiveButtons.length; i++){
        unArchiveButtons[i].disabled=false;
    }
}


async function unArchiveCampaign(id){
    deactivateUnArchiveButtons()
    var result = await fetch(`/campaigns/campaign_api/un_archive_campaign/${id}`, {method:'PUT'});
    var data = await result.json();
    document.getElementById(`${id}-row`).remove();
    activateUnArchiveButtons()
}


document.addEventListener("DOMContentLoaded", (event) => {
    for(let i = 0; i < unArchiveButtons.length; i++){
        unArchiveButtons[i].addEventListener('click', e => {
            unArchiveCampaign(parseInt(e.target.value))
        })
    }
  });
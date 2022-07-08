function ejecuteRequest(){
    var request = new XMLHttpRequest();
    // request.open('GET', '/static/js/ejample.json', false);  // `false` makes the request synchronous
    request.open('GET', '/sqlite', false);  // `false` makes the request synchronous
    request.send(null);

    
    console.log(request.responseText);
    
}

// var buttonRequest = document.getElementById('buttonRequest')
//     buttonRequest.addEventListener('click', ()=>{
//         alert('button request')
//         ejecuteRequest()
//     })



var div_loader = document.getElementById('div_loader')


function showMeLoaderGif(){
    div_loader.style.display = 'block'
}

function hideMeLoaderGif(){
    div_loader.style.display = 'none'
}
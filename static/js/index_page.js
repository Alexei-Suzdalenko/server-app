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
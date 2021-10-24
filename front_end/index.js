function grabQuote(){
  fetch('http://127.0.0.1:5000/ai-quotes', { 
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer' // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
  }).then(response => response.json())
  .then(data => {
      console.log(data)
      const obj = data;
      document.getElementById("1").innerHTML = obj.author;
      document.getElementById("2").innerHTML = obj.quote;
  });
}
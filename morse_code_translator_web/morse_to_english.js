function toEnglish() {
    // button click handler code
    //console.log("Hello World!");

     // Replace this URL with the actual URL of your Flask API endpoint
  const apiUrl = 'http://127.0.0.1:5000/api/morse_to_english';

  eng_txt=document.getElementById('userinput1');
  morse_code=document.getElementById('userinput2');

  invalid_chars2 = document.getElementById('invalid_chars2');
  invalid_chars1 = document.getElementById('invalid_chars1');

  errorMsg1 = document.querySelector('#invalid_chars1');
  errorMsg2 = document.querySelector('#invalid_chars2');

  // Data to be sent in the POST request
  const postData = {
    'user_input': morse_code.value,
    // Add more key-value pairs as needed
  };
  //console.log(invalid_chars);
  //console.log(errorMsg);
  //console.log(eng_txt);
  //console.log(morse_code);

  // Perform the POST request using the fetch API
  if (morse_code.value) {
  fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json', // Specify the content type as JSON
    },
    body: JSON.stringify(postData), // Convert data to JSON format
  })
  .then(response => response.json())
  .then(data => {
    
    //console.log('Success:', data);
    // Handle the response data here
    //console.log(data.result[0]);
    //errorMsg.parentElement.classList.add('to-morse');
    eng_txt.value = data.result[0];
    if (data.result[1].length) {
        //console.log(data.result[1]);
        //console.log(errorMsg);
        errorMsg2.parentElement.classList.add('erroR');
        invalid_chars2.innerHTML = "Invalid characters: ";
        for (const ch in data.result[1]) {
            invalid_chars2.innerHTML += data.result[1][ch] + " ";
        }
    }
    if (!data.result[1].length) {
        //console.log(data.result[1]);
        //console.log(errorMsg);
        errorMsg1.parentElement.classList.remove('erroR');
        errorMsg2.parentElement.classList.remove('erroR');
        invalid_chars1.innerHTML = "";
        invalid_chars2.innerHTML = "";
    }
    //errorMsg.parentElement.classList.add('to-morse');
    //invalid_chars.innerHTML = "testing";
  })
  .catch(error => {
    console.error('Error:', error);
    // Handle errors here
  });
    }
    else {
        errorMsg1.parentElement.classList.remove('erroR');
        errorMsg2.parentElement.classList.remove('erroR');
        invalid_chars1.innerHTML = "";
        invalid_chars2.innerHTML = "";
        eng_txt.value="";
    }
  } 
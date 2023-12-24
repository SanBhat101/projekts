function toMorse() {
    // button click handler code
    //console.log("Hello World!");

     // Replace this URL with the actual URL of your Flask API endpoint
  const apiUrl = 'http://127.0.0.1:5000/api/translate_to_morse';

  eng_txt=document.getElementById('userinput1');
  morse_code=document.getElementById('userinput2');

  invalid_chars = document.getElementById('invalid_chars');
  errorMsg = document.querySelector('#invalid_chars');

  // Data to be sent in the POST request
  const postData = {
    'user_input': document.getElementById('userinput1').value,
    // Add more key-value pairs as needed
  };
  //console.log(invalid_chars);
  //console.log(errorMsg);
  //console.log(eng_txt);
  //console.log(morse_code);

  // Perform the POST request using the fetch API
  if (eng_txt.value) {
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
    morse_code.value = data.result[0];
    if (data.result[1].length) {
        //console.log(data.result[1]);
        //console.log(errorMsg);
        errorMsg.parentElement.classList.add('to-Morse');
        invalid_chars.innerHTML = "Invalid characters: ";
        for (const ch in data.result[1]) {
            invalid_chars.innerHTML += data.result[1][ch] + " ";
        }
    }
    if (!data.result[1].length) {
        //console.log(data.result[1]);
        //console.log(errorMsg);
        errorMsg.parentElement.classList.remove('to-Morse');
        invalid_chars.innerHTML = "";
    }
    //errorMsg.parentElement.classList.add('to-morse');
    //invalid_chars.innerHTML = "testing";
  })
  .catch(error => {
    console.error('Error:', error);
    // Handle errors here
  });
    }
  } 
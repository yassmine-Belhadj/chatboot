const form = document.getElementById('userinput');
const chatlog = document.querySelector('.chatlog');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const input = document.getElementById('input').value;
  const response = generateResponse(input);
  displayResponse(response);
});

function generateResponse(input) {
  let response = '';
  if (input.includes('bonjour') || input.includes('salut')) {
    response = 'Bonjour ! Comment puis-je vous aider aujourd\'hui ?';
  } else if (input.includes('météo')) {
    response = 'Je ne suis pas capable de fournir les prévisions météo actuellement. Veuillez consulter une source météorologique en ligne.';
  } else if (input.includes('quel est ton nom') || input.includes('comment tu t\'appelles')) {
    response = 'Je m\'appelle Chatbot. Et vous ?';
  } else if (input.includes('merci')) {
    response = 'De rien ! N\'hésitez pas à me poser d\'autres questions.';
  } else {
    response = 'Je suis désolé, je ne suis pas capable de répondre à cette question. Veuillez essayer de reformuler votre question ou de la poser différemment.';
  }
  return response;
}

function displayResponse(response) {
  const message = document.createElement('p');
  message.textContent = response;
  chatlog.appendChild(message);
}

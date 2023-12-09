# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:56:12 2023

@author: 19108
"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Math Quiz</title>
</head>
<body>

<h1>Welcome to the Math Quiz!</h1>

<div id="quiz">
  <p id="question"></p>
  <input type="text" id="userAnswer" placeholder="Your answer">
  <button onclick="checkAnswer()">Submit</button>
  <p id="result"></p>
</div>

<script>
  function generateQuestion() {
    const num1 = Math.floor(Math.random() * 10) + 1;
    const num2 = Math.floor(Math.random() * 10) + 1;
    const operators = ['+', '-', '*', '/'];
    const operator = operators[Math.floor(Math.random() * operators.length)];
    let answer;

    switch (operator) {
      case '+':
        answer = num1 + num2;
        break;
      case '-':
        answer = num1 - num2;
        break;
      case '*':
        answer = num1 * num2;
        break;
      case '/':
        answer = num1 / num2;
        break;
    }

    return { question: `What is ${num1} ${operator} ${num2}?`, answer };
  }

  let correctAnswers = 0;
  const totalQuestions = 5;
  let currentQuestion = 0;

  function displayQuestion() {
    if (currentQuestion < totalQuestions) {
      const { question, answer } = generateQuestion();
      document.getElementById('question').textContent = question;

      document.getElementById('result').textContent = '';
      document.getElementById('userAnswer').value = '';

      document.getElementById('userAnswer').focus();

      currentQuestion++;
    } else {
      document.getElementById('quiz').innerHTML = `<p>You answered ${correctAnswers} out of ${totalQuestions} questions correctly.</p>`;
    }
  }

  function checkAnswer() {
    const userAnswer = parseFloat(document.getElementById('userAnswer').value);
    if (!isNaN(userAnswer)) {
      const { answer } = generateQuestion();

      if (userAnswer === answer) {
        document.getElementById('result').textContent = 'Correct!';
        correctAnswers++;
      } else {
        document.getElementById('result').textContent = `Sorry, the correct answer is ${answer}`;
      }

      displayQuestion();
    } else {
      document.getElementById('result').textContent = 'Invalid input. Please enter a number.';
    }
  }

  displayQuestion();
</script>

</body>
</html>

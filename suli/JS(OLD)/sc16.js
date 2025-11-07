
function isLeapYear() {
  var year = parseInt(prompt("Enter a year: "))
  document.write((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0);
};

function countA() {
  var text = prompt("Enter a text: ");
  let count = 0;
  for (let i = 0; i < text.length; i++) {
    if (text[i] === 'a' || text[i] === 'A') {
      count++;
    }
  }
  document.write(count);
};

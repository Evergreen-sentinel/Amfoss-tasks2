const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  function printStarPattern(n) {

    for (let i = 1; i <= n; i += 2) {
      let stars = '*'.repeat(i);
      let padding = ' '.repeat((n - i) / 2);
      console.log(padding + stars);
    }

    for (let i = n - 2; i >= 1; i -= 2) {
      let stars = '*'.repeat(i);
      let padding = ' '.repeat((n - i) / 2);
      console.log(padding + stars);
    }
  }
  
  readline.question('Enter a number: ', (num) => {
    let n = parseInt(num);
    printStarPattern(n);
    readline.close();
  });

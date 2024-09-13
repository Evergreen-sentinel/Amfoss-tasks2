const fs = require('fs');

function generateStarPattern(n) {
  let pattern = '';

  for (let i = 1; i <= n; i += 2) {
    let stars = '*'.repeat(i);
    let padding = ' '.repeat((n - i) / 2);
    pattern += padding + stars + '\n';
  }

  for (let i = n - 2; i >= 1; i -= 2) {
    let stars = '*'.repeat(i);
    let padding = ' '.repeat((n - i) / 2);
    pattern += padding + stars + '\n';
  }

  return pattern;
}

fs.readFile('input2.txt', 'utf8', (err, data) => {
  if (err) throw err;

  let n = parseInt(data.trim());
  let pattern = generateStarPattern(n);

  fs.writeFile('output2.txt', pattern, (err) => {
    if (err) throw err;
    console.log('The pattern has been saved to output2.txt');
  });
});

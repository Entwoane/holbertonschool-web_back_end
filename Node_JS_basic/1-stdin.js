process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

process.stdin.once('data', (input) => {
  const name = input.trim();
  console.log(`Your name is: ${name}`);
  process.stdin.end();
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});

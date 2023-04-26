#/usr/bin/node
const mode = require('fs');
const file = process.argv[2];

mode.readFile(file, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    process.stdout.write(data);
  }
});

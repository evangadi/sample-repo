const { log } = require('console')
let os = require('os')
// console.log(os);
let pla = os.freemem()
console.log(pla);
// let fs = require('fs')
// console.log(fs);
let pa = require('path')
let po = pa.parse(__filename)
console.log(po);


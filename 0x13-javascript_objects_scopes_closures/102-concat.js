#!/usr/bin/node

const fs = require('fs');
const { argv } = require('node:process');

const str1 = fs.readFileSync(argv[2], 'utf-8');
const str2 = fs.readFileSync(argv[3], 'utf-8');
const str3 = str1 + str2;

fs.writeFileSync(argv[4], str3);

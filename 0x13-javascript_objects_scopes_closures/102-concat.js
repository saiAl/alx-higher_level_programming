#!/usr/bin/node

const fs = require('fs');

const str1 = fs.readFileSync('fileA', 'utf-8');
const str2 = fs.readFileSync('fileB', 'utf-8');
const str3 = str1 + str2;

fs.writeFileSync('fileC', str3);

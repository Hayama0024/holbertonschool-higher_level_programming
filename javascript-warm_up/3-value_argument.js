#!/usr/bin/node

const arg = process.argv[2]; // 3番目の値（＝1番目の引数）

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}

// Complete the function so that it converts dash - delimited("kebab" case) & underscore - delimited("snake" case) words into "camel" casing.The first word within the output should be capitalized only if the original word was capitalized.

//     toCamelCase("the-stealth-warrior")
// // returns "theStealthWarrior"
// toCamelCase("The_stealth_warrior")
// // returns "TheStealthWarrior"

function toCamelCase(str) {
  str = str.split(/[-_]/);
  // if (str.includes("-")){
  //   str = str.split("-");
  // } else {
  //   str = str.split("_");
  // }

  for (let i = 1; i < str.length; i++) {
    str[i] = str[i][0].toUpperCase() + str[i].slice(1);
  }
  return str.join("");
}

console.log(toCamelCase("the-stealth-warrior"));
console.log(toCamelCase("The_stealth_warrior"));

const readline = require("readline");
const chalk = require("chalk");
const kontol = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
function bobok(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
const presser = String.raw`
╔═╗╔═╗╔═╗╔═╗
╚╗╚╝╔╝╚╗╚╝╔╝
─╚╗╔╝──╚╗╔╝╔╦═╗╔═══╦╗╔╗
─╔╝╚╗──╔╝╚╗╠╣╔╗╬══║║║║║
╔╝╔╗╚╗╔╝╔╗╚╣║║║║║══╣╚╝║
╚═╝╚═╝╚═╝╚═╩╩╝╚╩═══╩══╝  
`;
kontol.question("Ip nya apa Bego", function (ip) {
  kontol.question("Port Nya Masukin Juga Ajg ", function (port) {
    console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    console.log(chalk.red(presser));
    bobok(2000).then(() => {
      for (var i = 0; i < Infinity; i++) {
        console.log(`Mulai menyerang ${chalk.bold.red(`${ip}`)}, port kontol ${chalk.bold.cyan(`${port}`)}`);
      }
    });
  });
});  

ZX Teams Adick Adick
const readline = require('readline');
const rl = readline.createInterface({input : process.stdin, output : process.stdout});
rl.question(`Would you like to [A]be a youtuber or [B]be unemployed or [C]be a hardworking citizen or [D]a simp? (Be sure to answer in capitals)` , (option) => {
  rl.close();
  if (option == "A") {
    console.log(`Okay, loser hahaha lemme guess a commentary channel? Huh?`);
  }
  else if (option == "B") {
    console.log(`Yeah atleast you're not a commentary youtube channel..`)
  }
  else if (option == "C") {
    console.log(`You are so honorable kind sir may I be your wife?`);
  }
  else if (option == "D") {
    console.log(`In the wise words of a not-so-liked twitch streamer "Depression is stupid"`);
  }
  else {
    console.log(`Idk m8 as long as you're not a commentary channel in 2020 you're better off doing absolutely nothing`);
  }
});

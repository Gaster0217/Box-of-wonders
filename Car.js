car = function () {
  const ac_constant = 10;
  var speed;
  var distance;
  const readline = require('readline');
  const rl = readline.createInterface({input : process.stdin, output : process.stdout});
  rl.question("[A] accelerate, [B] slow down, [C] show speed, [D] Quit", (cp) => {
    if (cp == "A") {
      speed = i * 10;
      console.log("You just acclerated! You are now moving at, ", speed, " mpt");
      distance = distance + speed;
    }
    else if (cp == "B") {
      speed = i / 10;
      console.log("You slowed down! You are now moving at, ", speed, " mpt");
    }
    else if (cp == "C") {
      console.log("Your distance is ", distance, " meters and speed is", speed, " mpt");
    }
    else if (i == 25) {
      console.log("Fuel almost running out! Only 5 turns remaining...");
    }
    rl.close();
  });
}
car();
//I am sorry i didn't include a loop in the function, pls sir spare my life for my silly little forgetful nature.

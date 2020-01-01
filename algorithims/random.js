function die() {
    return Math.floor((Math.random() * 6) + 1);
}

function roll() {
    var sum = 0;
    var max = 0;
    var min = 0;
    var count = 0;
    var doubles = false;
    while (doubles != true) {
        var die1 = die();
        var die2 = die();
        if(die1 > max) {
            max = die1;
        }
        if(die2 > max) {
            max = die1;
        }
        if(die1 < min) {
            min = die1;
        }
        if(die2 <min) {
            min = die1;
        }
        sum += die1 + die2;
        count += 2;

        if (die1 == die2) {
            doubles = true;
        }
    }
    
}
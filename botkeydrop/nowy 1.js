function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function placeBet(amount){
    var coinsBefore = parseInt(document.getElementById('balance_p').innerText);
    document.getElementById('dice_amount').value = amount;
    document.getElementById('dice_play').click();
	sleep(2000)
    var coinsAfter = parseInt( document.getElementById('balance_p').innerText);
    if (coinsBefore < coinsAfter){
        return false
    }
    return true
}


var lose = 0;



function start() {

    setTimeout(function() {
		var bet = undefined;
		sleep(2000);
		if (lose < 4){
			var bet = placeBet(20);
		}
		if (bet != undefined){
			if (bet === true){
				lose = 0;
				start();
				return;
			}			
		}
		if (lose < 4){
			lose = lose + 1;
			start();
			return;
		}
		var amount = 200;
		var bet = placeBet(amount);
		if (bet === false){
			amount = amount * 2;
			start();
			return;
		}
		lose = 0;
		start();
		return;
    }, 2000);
}
start();
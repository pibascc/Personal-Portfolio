function clearResult() {
    let result = document.getElementById("main_result");
    let result_caption = document.getElementById("result_caption");
    let result_divisor = document.getElementById("result_divisor");
    result.innerHTML = "";
    result_caption.innerHTML = "";
    result_divisor.innerHTML = "";
}

function process() {
    let result = document.getElementById("main_result");
    let result_caption = document.getElementById("result_caption");
    let result_divisor = document.getElementById("result_divisor");                     
    let input = document.getElementById("number_input");
    let n = Number(input.value);
    let d = 2;
    if ((n.length != 0) && Number.isSafeInteger(n) && (n > 0)) {
        let l = Math.sqrt(n);
        if (n === 1) {
            result.innerHTML = "NO";
            result_caption.innerHTML = "It is NOT a PRIME number because it only has ONE factor";
        }
        else {
            let prime = true;           
            for (; d <= l; ++d) {
                if (n % d === 0) {
                    prime = false;
                    break;
                }
            }
            if (prime) {
                result.innerHTML = "YES";
                result_caption.innerHTML = "It is a PRIME number"
            }
            else {
                result.innerHTML = "NO";
                result_caption.innerHTML = "It is NOT a PRIME number and is divisible by:";
                result_divisor.innerHTML = String(d);
            }
        }
    }
    else {
        result.innerHTML = "ERROR"
        result_caption.innerHTML = "Invalid INPUT"
    }
}
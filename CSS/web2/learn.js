var first = document.getElementById('firstNumber');
var second =  document.getElementById('secondNumber');
var resultone = document.getElementById('result');
var buttton = document.getElementById('buttonClick');

function addNumbers(blahh){
    if(!first.value || !second.value){
        alert("Please enter any number first");
    } 
    else{
        var x = parseFloat(first.value);
        var y = parseFloat(second.value);
        var sum = x / y;
        var result = sum * 100;
        resultone.innerText = "Answer is " + result + " %";
        blahh.preventDefault();
    }
}
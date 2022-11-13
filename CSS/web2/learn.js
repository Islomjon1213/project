var firstNum = document.getElementById('fNumber');
var secondNum = document.getElementById('sNumber');
var resultone = document.getElementById('result');
var form = document.getElementById('forms');


form.addEventListener('submit', function(event){
    if(!firstNum.value || !secondNum.value){
        alert("Please enter any number");
    } else{
        var x = parseFloat(firstNum.value);
        var y = parseFloat(secondNum.value);

        var sum = x * y;
        // var sum = x - y;

        resultone.innerText = "Answer is " + sum;
        event.preventDefault();
    }
});
const num1 = 1;
const num2 = 1;
console.log('테스트', num1);

function solution(num1, num2) {
    let remainder = num1 % num2;

    console.log('remainder', remainder);
    
    return remainder;
}

solution(num1, num2); 
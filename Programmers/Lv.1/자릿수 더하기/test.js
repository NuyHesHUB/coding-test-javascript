function solution(n) {
    let num = n.toString().split('').map(Number);
    let initValue = 0;
    const sum = num.reduce((acc, cur) => acc + cur ,initValue);

    return sum;
}

console.log(solution(123));
console.log(solution(987));
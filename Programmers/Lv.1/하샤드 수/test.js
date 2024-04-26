function solution(x) {
    let str = x.toString().split('').map(Number);
    let init = 0;
    let sum = str.reduce((a,b) => a + b , init);
    const result = x%sum === 0 ? true : false;
    
    return result;
}

console.log(solution(10));
console.log(solution(12));
console.log(solution(11));
console.log(solution(13));
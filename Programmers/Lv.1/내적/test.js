function solution(a, b) {
    let result = [];
    let sum = 0;
    for (let i = 0; i < a.length; i++) {
        result.push(a[i] * b[i]);
    }
    result.forEach((item) => {
        sum += item
    }) 
    
    
    return sum;
} 

function solution(a, b) {
    let result = 0;
    for (let i = 0; i < a.length; i++) {
        result += a[i] * b[i];
    }
    
    return result;
} 

function solution(a, b) {
    return a.reduce((acc, cur, idx) => {
            return acc + cur * b[idx];
        }, 0);
} 

console.log(solution([1,2,3,4], [-3,-1,0,2]));
console.log(solution([1,2,3], [4,5,6]));
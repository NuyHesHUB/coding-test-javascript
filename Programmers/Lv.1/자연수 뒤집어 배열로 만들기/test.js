function solution(n) {
    let str = n.toString().split('').map(Number);
    return str.reverse();
}

console.log(solution(12345));
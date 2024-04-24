function solution(n) {
    let num = parseInt(n.toString().split('').sort((a,b) => b-a).join(''));
    return num;
}

console.log(solution(118372));
function solution(seoul) {
    const findKim = seoul.indexOf('Kim')
    return `김서방은 ${findKim}에 있다`;
}

console.log(solution(["Jane", "Kim"]));
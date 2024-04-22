function solution(n){
    let arry = [];
    let index = 1;
    let sum = 0;
    while (index <= n) {
        if (n % index === 0) arry.push(index)
        index++
    }
    arry.forEach((num) => {
        sum += num;
    })
    return sum;
}
console.log(solution(12));
console.log(solution(5));


// 다른 사람 풀이
function solution(num) {
    let sum = 0;
    for (let i = 1; i <= num; i++) {
        if (num % i === 0) sum += i
    }
    return sum
}

// 훨씬 간단해 보이고 효율적인 것 같다.
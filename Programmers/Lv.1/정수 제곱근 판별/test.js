function solution(n) {
    let sqrt = Math.sqrt(n);
    if (Number.isInteger(sqrt)) {
        return Math.pow(sqrt + 1, 2);
    } else {
        return -1;
    }
}

console.log(solution(121));
console.log(solution(3));

/*-------------------------------------*\
                문제 설명   
\*-------------------------------------*/

// Math.sqrt() 함수는 숫자의 제곱근을 반환합니다.
// Number.isInteger() 함수는 주어진 값이 정수인지 확인합니다.
// Math.pow() 함수는 첫 번째 인수를 두 번째 인수만큼 제곱한 값을 반환합니다.
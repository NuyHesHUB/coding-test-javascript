function solution(num) {
    let result = 0;
    for(let i=0; i<500; i++){
      if(num != 1) {
        num = num % 2 == 0 ? num / 2 : num * 3 + 1; 
      }
      else {
        return result = i;
      } 
    }
    return result = -1;
}

console.log(solution(6));
console.log(solution(16));
console.log(solution(626331));

// 다른사람 풀이1

function collatz(num) {
    var answer = 0;
    while(num !=1 && answer !=500){
        num%2==0 ? num = num/2 : num = num*3 +1;
    answer++;
  }
    return num == 1 ? answer : -1;
}
// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(collatz(6));

// 다른사람 풀이2

function collatz(num, count = 0) {
    return (num == 1) ? ((count >= 500) ? -1 : count) : collatz((num % 2 == 0) ? num / 2 : (num * 3) + 1, ++count);
}
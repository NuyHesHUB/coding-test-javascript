function solution(arr, divisor) {
  let result = [];
  
  for(let i=0;i<arr.length;i++){
      if(arr[i] % divisor === 0){
          result.push(arr[i])
      }
  }
  
  if (result.length === 0) {
      return [-1];
  }
  
  return result.sort((a, b) => a - b);
  
}

console.log(solution([5, 9, 7, 10],5));
console.log(solution([2, 36, 1, 3],1));
console.log(solution([3,2,6],10));

// 다른사람 풀이

function solution(arr, divisor) {
    var answer = arr.filter(v => v%divisor == 0);
    return answer.length == 0 ? [-1] : answer.sort((a,b) => a-b);
}
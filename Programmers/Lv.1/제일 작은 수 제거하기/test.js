function solution(arr) {
    let min = Math.min(...arr);
    if(arr.length>1){
      const newArr=arr.filter(v => v !== min);
      return newArr;
    }else{
      return [-1];
    }
}

console.log(solution(10));
console.log(solution(12));
console.log(solution(11));
console.log(solution(13));
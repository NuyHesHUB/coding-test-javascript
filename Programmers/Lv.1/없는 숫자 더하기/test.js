function solution(numbers) {
    let arr = [0,1,2,3,4,5,6,7,8,9];
    let sub = arr.filter(x=> !numbers.includes(x));
    
    return sub.reduce((a,c)=>a+c,0)
}

console.log(solution([1,2,3,4,6,7,8,0]));
console.log(solution([5,8,4,0,6,7,9]));
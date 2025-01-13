function solution(s) {
    const arr = [...s];
    
    if(arr.length % 2 !== 0) {
        return arr[(Math.floor(arr.length/2))]
    } else {
        return arr[(arr.length/2)-1] + arr[(arr.length/2)]
    }
}

console.log(solution("abcde"));
console.log(solution("qwer"));

// 4 일 때 2,3 번째
// 5 일 때 3번째
// 6 일 때 3,4번째  
// 7 일 때 4번째 
// 8 일 때 4,5번째 


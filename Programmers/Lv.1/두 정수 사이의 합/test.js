function solution(a, b) {
    let result=0;
    if(a<b){
        for(let i=a; i<=b; i++){
            result+=i;
        }
    } else {
        for(let i=b; i<=a; i++){
            result+=i;
        }
    }
    return result;
}

console.log(solution(3,5));
console.log(solution(3,3));
console.log(solution(5,3));
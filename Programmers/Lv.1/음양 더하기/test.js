function solution(absolutes, signs) {
    let arr = [...absolutes];  

    for(let i=0; i<arr.length; i++){
        if(!signs[i]){
            arr[i] *= -1;
        }
    }

    return arr.reduce((sum, val) => sum+val, 0);
  }

console.log(solution([4,7,12],[true,false,true]));
console.log(solution([1,2,3],[false,false,true]));


// 다른 사람 풀이
function solution(absolutes, signs) {
    return absolutes.reduce((acc, val, i) => acc + (val * (signs[i] ? 1 : -1)), 0);
}

// reduce와 삼항연산자를 사용해서 엄청간결하게 작성했다. reduce보다 for문이 성능이 더 좋다고는 하는데 알아봐야겠다.
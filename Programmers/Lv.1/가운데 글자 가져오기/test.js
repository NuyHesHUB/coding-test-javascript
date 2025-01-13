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

/* function solution(s) {
    return s.substr(Math.ceil(s.length / 2) - 1, s.length % 2 === 0 ? 2 : 1);
} */

/* function solution(s) {
    return s.length % 2 == 0 ? s.substr(s.length / 2 - 1, 2) : s.substr(Math.floor(s.length / 2), 1);
} */

/* function solution(s) {
    var length = s.length;
    var answer = '';

    if(!(s.length >0 && s.length<100)) {
        return;
    }

    if(length % 2 != 0) {
        answer += s.slice(length/2, length/2 +1);
    }else {
        answer += s.slice(length/2 -1, length/2 +1);
    }

    return answer;

}

var s = 'qwerty';
console.log(solution(s)); */
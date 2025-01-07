function solution(phone_number) {
    let phone = phone_number.split('');

    for(let i=0;i<phone.length-4;i++){
        phone[i]='*';
    }

    return phone.join('')
}

console.log(solution("01033334444"));
console.log(solution("027778888"));

// 다른 사람 풀이 1

function hide_numbers(s){
    return s.replace(/\d(?=\d{4})/g, "*");
}

console.log("결과 : " + hide_numbers('01033334444'));

// 다른 사람 풀이 2

function hide_numbers(s){
    var result = "*".repeat(s.length - 4) + s.slice(-4);
    return result;
}

console.log("결과 : " + hide_numbers('01033334444'));

  
// 다른 사람 풀이 3
const solution = n => [...n].fill("*",0,n.length-4).join("")
/*
//#2-0. 경고문 띄워보기
alert("hi");



//#2-1. 데이터 타입
//text는 ""혹은 '' 안에 기재



//2-2. 변수
console.log(); //= 콘솔에 값 출력

const a = 5;
const b = 2;

//이름짓는 방식
const myName = "sung min"; //자바스크립트 방식
const my_name = "sung min"; //파이썬 방식

console.log(a + b);
console.log(a * b);
console.log(a / b);
console.log("hello " + myName);



//2-3. 변수 지정 방식
//1. const - 상수, 재선언 금지, 값이 바뀔 수 없음.
const a = 5;  
const b = 2;

console.log(a + b);
console.log(a * b);
console.log(a / b);

//2. let - 재선언 금지, 값을 바꿀 수 있음
let myName = "sung min";

console.log("hello " + myName);

myName = "yuri";
console.log("your new name is " + myName)

//3.ver - 재선언 가능, 값을 바꿀 수 있음. 예전에 쓰던 변수. 지금은 const와 let으로 사용.
var friendsName = "coco";
console.log("your friend's name is " + friendsName);

var friendsName = "momo";
console.log("your new friend's name is " + friendsName);



//2-4. boolean
//true, false 는 값이 있음. null은 값이 없음.
const t = true;
const f = false;
const n = null;

//undefined - 변수에 값을 선언하지 않음 (정의 X)
let something;

console.log(t);
console.log(f);
console.log(n);
console.log(something);



//2-5. 배열
const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat"];

//Get Item from Array
console.log(daysOfWeek);
console.log(daysOfWeek[5]);

//Add one more day to the Array
daysOfWeek.push("sun");
console.log(daysOfWeek);
*/
// 1. 상수 객체
const animal = {
  type: "고양이",
  name: "나비",
  color: "black",
};

animal.age = 2; // 추가
animal.name = "까망이"; // 수정
delete animal.color; // 삭제

// 2. 메서드
// -> 값이 함수인 프로퍼티를 말함

const person = {
  name: "김민규",
  //메서드
  sayHi: function () {
    console.log("안녕하세요");
  },
};

person.sayHi();
person["sayHi"]();

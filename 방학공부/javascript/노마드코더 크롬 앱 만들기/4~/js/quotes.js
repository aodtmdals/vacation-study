const quotes = [
    {
        quotes : "대접받고 싶은 대로 남을 대접하라.",
        author : "영어 속담",
    },
    {
        quotes : "오랫동안 꿈을 그리는 사람은 마침내 그 꿈을 닮아간다.",
        author : "앙드레 말로",
    },
    {
        quotes : "변명 중에서도 가장 어리석고 못난 변명은 '시간이 없어서'라는 변명이다.",
        author : "토마스 에디슨",
    },
    {
        quotes : "여가를 활용하지 못하는 사람은 항상 여가 시간이 없다.",
        author : "서양 격언",
    },
    {
        quotes : "빛을 퍼뜨릴 수 있는 두 가지 방법이 있다. 촛불이 되거나 또는 그것을 비추는 거울이 되는 것이다.",
        author : "이디스 워튼",
    },
    {
        quotes : "세상은 고통으로 가득하지만 한편 그것을 이겨내는 일로도 가득차 있다.",
        author : "헬렌 켈러",
    },
    {
        quotes : "사랑은 두 사람이 마주 쳐다보는 것이 아니라 함께 같은 방향을 바라보는 것이다.",
        author : "생텍쥐페리",
    },
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const todaysQutes = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQutes.quotes;
author.innerText = todaysQutes.author;
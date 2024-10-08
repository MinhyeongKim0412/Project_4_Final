function toggleQuickMenu() {
    const menu = document.querySelector('.quick-menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}

function updateTime() {
    const currentTimeElement = document.getElementById('current-time');
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    currentTimeElement.textContent = `${hours}:${minutes}`;  // 시간:분 형식으로 표시
}

setInterval(updateTime, 1000);  // 매초마다 시간 업데이트
updateTime();  // 페이지 로드 시 시간 설정

// 방향키로 가로 스크롤을 제어하는 스크립트
document.addEventListener('keydown', function(event) {
    const gallery = document.querySelector('.gallery');
    if (event.key === 'ArrowRight') {
        gallery.scrollBy({ left: 200, behavior: 'smooth' }); // 오른쪽으로 스크롤
    } else if (event.key === 'ArrowLeft') {
        gallery.scrollBy({ left: -200, behavior: 'smooth' }); // 왼쪽으로 스크롤
    }
});

// 좌우 버튼 클릭 시 스크롤
document.querySelector('.nav-button.left').addEventListener('click', function() {
    const gallery = document.querySelector('.banner-inner');
    gallery.scrollBy({ left: -200, behavior: 'smooth' }); // 왼쪽으로 스크롤
});

document.querySelector('.nav-button.right').addEventListener('click', function() {
    const gallery = document.querySelector('.banner-inner');
    gallery.scrollBy({ left: 200, behavior: 'smooth' }); // 오른쪽으로 스크롤
});

// div사이즈 동적으로 구하기
const outer = document.querySelector('.outer');
const innerList = document.querySelector('.inner-list');
const inners = document.querySelectorAll('.inner');
let currentIndex = 0; // 현재 슬라이드 화면 인덱스

inners.forEach((inner) => {
    inner.style.width = `${outer.clientWidth}px`; // inner의 width를 모두 outer의 width로 만들기
});

innerList.style.width = `${outer.clientWidth * inners.length}px`; // innerList의 width를 inner의 width * inner의 개수로 만들기

// 버튼에 이벤트 등록하기
const buttonLeft = document.querySelector('.button-left');
const buttonRight = document.querySelector('.button-right');

buttonLeft.addEventListener('click', () => {
    currentIndex--;
    currentIndex = currentIndex < 0 ? 0 : currentIndex; // index값이 0보다 작아질 경우 0으로 변경
    innerList.style.marginLeft = `-${outer.clientWidth * currentIndex}px`; // index만큼 margin을 주어 옆으로 밀기
});

buttonRight.addEventListener('click', () => {
    currentIndex++;
    currentIndex = currentIndex >= inners.length ? inners.length - 1 : currentIndex; // index값이 inner의 총 개수보다 많아질 경우 마지막 인덱스값으로 변경
    innerList.style.marginLeft = `-${outer.clientWidth * currentIndex}px`; // index만큼 margin을 주어 옆으로 밀기
});

// 퀵 메뉴 토글 함수
function toggleQuickMenu() {
    const menu = document.querySelector('.quick-menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}

// 현재 시간 업데이트 함수
function updateTime() {
    const currentTimeElement = document.getElementById('current-time');
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    currentTimeElement.textContent = `${hours}:${minutes}`;  // 시간:분 형식으로 표시
}

setInterval(updateTime, 1000);  // 매초마다 시간 업데이트
updateTime();  // 페이지 로드 시 시간 설정

// 슬라이드 배너 관련 코드
document.addEventListener('DOMContentLoaded', () => {
    const outer = document.querySelector('.outer');
    const innerList = document.querySelector('.inner-list');
    const inners = document.querySelectorAll('.inner');
    let currentIndex = 0; // 현재 슬라이드 화면 인덱스

    // 각 슬라이드의 폭을 동적으로 설정
    inners.forEach((inner) => {
        inner.style.width = `${outer.clientWidth}px`; // inner의 width를 모두 outer의 width로 만들기
    });

    // 전체 리스트의 폭 설정
    innerList.style.width = `${outer.clientWidth * inners.length}px`;

    // 슬라이드 이동 함수
    function moveSlide(direction) {
        currentIndex += direction;
    
        // 인덱스 범위 조정
        if (currentIndex < 0) {
            currentIndex = inners.length - 1; // 마지막 슬라이드로 이동
        } else if (currentIndex >= inners.length) {
            currentIndex = 0; // 첫 번째 슬라이드로 이동
        }
    
        // 슬라이드 이동
        innerList.style.transform = `translateX(-${currentIndex * outer.clientWidth}px)`;
    }

    // 자동 슬라이드 기능
    let autoSlideInterval = setInterval(() => moveSlide(1), 3000); // 3초마다 다음 슬라이드로 이동

    // 좌우 버튼 클릭 시 슬라이드 이동
    document.querySelector('.nav-button.left').addEventListener('click', () => {
        clearInterval(autoSlideInterval); // 자동 슬라이드 일시 중지
        moveSlide(-1); // 왼쪽으로 슬라이드 이동
    });

    document.querySelector('.nav-button.right').addEventListener('click', () => {
        clearInterval(autoSlideInterval); // 자동 슬라이드 일시 중지
        moveSlide(1); // 오른쪽으로 슬라이드 이동
    });

    // 방향키로 가로 스크롤을 제어하는 스크립트
    document.addEventListener('keydown', function(event) {
        if (event.key === 'ArrowRight') {
            clearInterval(autoSlideInterval); // 자동 슬라이드 일시 중지
            moveSlide(1); // 오른쪽으로 슬라이드 이동
        } else if (event.key === 'ArrowLeft') {
            clearInterval(autoSlideInterval); // 자동 슬라이드 일시 중지
            moveSlide(-1); // 왼쪽으로 슬라이드 이동
        }
    });
});

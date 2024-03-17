// 페이지 URL 정의
const standardPageUrl = "http://localhost:8088/TeamProject1/standard.html";

// 평가기준 페이지 연결 함수 정의
function linkStandardPage() {
    const standardPageLink = document.getElementById("standardPageLink");
    standardPageLink.href = standardPageUrl;
}

function goToRankPage() {
    window.location.href = "http://localhost:8088/TeamProject1/rank.html";
}

// "보러가기" 버튼에 클릭 이벤트 추가
document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".btn-lg");
    buttons.forEach(button => {
        if (button.innerText === "보러가기") {
            button.addEventListener("click", goToRankPage);
        }
    });
});
// 페이지 로드 시 평가기준 페이지 컨트롤러 연결 실행
window.onload = linkStandardPage;

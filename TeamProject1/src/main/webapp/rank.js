// 페이지 URL 정의
const rankPageUrl = "http://localhost:8088/TeamProject1/rank.html";

// 랭크 페이지 연결 함수 정의
function linkRankPage() {
    const rankPageLink1 = document.getElementById("rankPageLink1");
    const rankPageLink2 = document.getElementById("rankPageLink2");
    const rankPageLink3 = document.getElementById("rankPageLink3");
    rankPageLink1.href = rankPageUrl;
    rankPageLink2.href = rankPageUrl;
    rankPageLink3.href = rankPageUrl;
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
// 페이지 로드 시 랭크 페이지 컨트롤러 연결 실행
window.onload = linkRankPage;
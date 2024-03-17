// 페이지 URL 정의
const mainPageUrl = "http://localhost:8088/TeamProject1/main.html";
const rankPageUrl = "http://localhost:8088/TeamProject1/rank.html";
const pagelinkPageUrl = "http://localhost:8088/TeamProject1/pagelink.html";
const standardPageUrl = "http://localhost:8088/TeamProject1/standard.html";

// 컨트롤러 연결 함수 정의
function linkControllersToPages() {
    // 메인 페이지 연결
    const mainPageLink = document.getElementById("mainPageLink");
    mainPageLink.href = mainPageUrl;

    // 랭크 페이지 연결
    const rankPageLink1 = document.getElementById("rankPageLink1");
    rankPageLink1.href = rankPageUrl;
    const rankPageLink2 = document.getElementById("rankPageLink2");
    rankPageLink2.href = rankPageUrl;
    const rankPageLink3 = document.getElementById("rankPageLink3");
    rankPageLink3.href = rankPageUrl;

    // 페이지링크 페이지 연결
    const pagelinkPageLink = document.getElementById("pagelinkPageLink");
    pagelinkPageLink.href = pagelinkPageUrl;

    // 평가기준 페이지 연결
    const standardPageLink = document.getElementById("standardPageLink");
    standardPageLink.href = standardPageUrl;
}

// 페이지 로드 시 컨트롤러 연결 실행
window.onload = linkControllersToPages;

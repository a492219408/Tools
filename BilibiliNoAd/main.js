document.querySelectorAll(".bili-video-card.is-rcmd>.bili-video-card__wrap.__scale-wrap>a").forEach((node) => {
    let target = node.getAttribute("data-target-url");
    if (typeof (target) === "string" && !target.match(/www\.bilibili\.com/g)) {
        let biliVideoCardNode = node.parentNode.parentNode;
        if (biliVideoCardNode.parentNode.className === "feed-card") {
            biliVideoCardNode.parentNode.remove();
        } else {
            biliVideoCardNode.remove();
        }
    }
});

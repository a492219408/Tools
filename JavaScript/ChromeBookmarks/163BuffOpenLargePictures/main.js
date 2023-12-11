let imgNodeList = document.querySelectorAll("a[data-inspecturl]");
if (typeof buffFalg === "undefined" && imgNodeList.length > 0) {
    buffFalg = true;
    imgNodeList.forEach((x) => {
        window.open(x.getAttribute("data-inspecturl"))
    });
} else {
    if (location.href.match("page_num")) {
        location.href.split("#")[1].split("&").forEach((x) => {
            let y = x.split("=");
            if (y[0] === "page_num") {
                location.href = location.href.replaceAll(/(.*page_num=).*?(?=&|$)(.*)/g, "$1$2") + (++y[1]);
            }
        });
    } else {
        let href = location.href;
        if (!location.href.match("#")) {
            href += "#";
        } else {
            href += "&";
        }
        href += "page_num=2";
        location.href = href;
    }
    delete buffFalg;
}

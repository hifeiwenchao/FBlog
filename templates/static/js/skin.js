/* Style Switcher by Paul Sowden, see A List Apart: http://www.alistapart.com/articles/alternate/ */

function setActiveStyleSheet(title) {
    let i, a, main;
    for(i=0; (a = document.getElementsByTagName("link")[i]); i++) {
    if(a.getAttribute("rel").indexOf("style") !== -1 && a.getAttribute("title")) {
      a.disabled = a.getAttribute("title") !== title;
    }
  }
}

function getActiveStyleSheet() {
    let i, a;
    for(i=0; (a = document.getElementsByTagName("link")[i]); i++) {
    if(a.getAttribute("rel").indexOf("style") !== -1 && a.getAttribute("title") && !a.disabled) return a.getAttribute("title");
  }
  return null;
}

function getPreferredStyleSheet() {
    let i, a;
    for(i=0; (a = document.getElementsByTagName("link")[i]); i++) {
    if(a.getAttribute("rel").indexOf("style") !== -1
       && a.getAttribute("rel").indexOf("alt") === -1
       && a.getAttribute("title")
       ) return a.getAttribute("title");
  }
  return null;
}

function createCookie(name,value,days) {
  let expires;
    if (days) {
      let date = new Date();
      date.setTime(date.getTime()+(days*24*60*60*1000));
        expires = "; expires=" + date.toGMTString();
    }
  else expires = "";
  document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
    let nameEQ = name + "=";
    let ca = document.cookie.split(';');
    for(let i=0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0)===' ') c = c.substring(1,c.length);
    if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length,c.length);
  }
  return null;
}

window.onload = function(e) {
    let cookie = readCookie("style");
    let title = cookie ? cookie : getPreferredStyleSheet();
    setActiveStyleSheet(title);
}

window.onunload = function(e) {
    let title = getActiveStyleSheet();
    createCookie("style", title, 365);
}

let cookie = readCookie("style");
let title = cookie ? cookie : getPreferredStyleSheet();
setActiveStyleSheet(title);

$(function(){
    H_qqServer={};
    H_qqServer.clickOpenServer = function () {
        $('.skin-btn-open').click(function(){
            $('.skin-btn').animate({
                right: '-50'
            },400);
            $('.skin-content').animate({
                right: '0',
                opacity: 'show'
            }, 800 );
        });
        $('.skin-close').click(function(){
            $('.skin-btn').animate({
                right: '-7px',
                opacity: 'show'
            },400);
            $('.skin-content').animate({
                right: '-250',
                opacity: 'show'
            }, 800 );
        });
    };
    H_qqServer.run= function () {
        this.clickOpenServer();
    };
    H_qqServer.run();
});
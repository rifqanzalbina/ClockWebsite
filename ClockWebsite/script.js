function updateClock() {
    const currentTime = new Date();
    const hours = currentTime.getHours();
    const minutes = currentTime.getMinutes();
    const seconds = currentTime.getSeconds();

    const timeString = `${formatTime(hours)}:${formatTime(minutes)}:${formatTime(seconds)}`;

    document.getElementById("time").textContent = timeString;
}

function formatTime(time) {
    return time < 10 ? `0${time}` : time;
}

setInterval(updateClock, 1000);

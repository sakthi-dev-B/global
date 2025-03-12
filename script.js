function updateDateTime() {
    const now = new Date();

    const date = now.toLocaleDateString();

    const time = now.toLocaleTimeString();

    document.getElementById("date").textContent = "Date: " + date;
    document.getElementById("time").textContent = "Time: " + time;
}

setInterval(updateDateTime, 1000);

updateDateTime();

document.getElementById("year").textContent = new Date().getFullYear();

let index = 0;
        function moveSlide() {
            const slides = document.querySelectorAll(".slide");
            index = (index + 1) % slides.length;
            document.querySelector(".slider").style.transform = `translateX(-${index * 100}%)`;
        }
        setInterval(moveSlide, 1000);
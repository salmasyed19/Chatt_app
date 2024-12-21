function openCamera() {
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        const video = document.createElement('video');
        video.srcObject = stream;
        video.play();
        document.body.appendChild(video);
    })
    .catch(function(error) {
        console.error("Error accessing camera", error);
    });
}

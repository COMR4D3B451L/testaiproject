function globalMethods() {
    return {
      enterLine(text) {
        const chatBody = document.getElementById("response-box")
        const newElement = document.createElement("span");
        const br = document.createElement("br");

        newElement.innerHTML = `<span class='text-red-700'>You:</span> ${text}`;
        chatBody.appendChild(newElement);
        chatBody.appendChild(br);
      },
    };
  }
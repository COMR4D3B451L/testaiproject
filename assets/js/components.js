function globalMethods() {
    return {
      enterLine(text) {
        const chatBody = document.getElementById("response-box")
        const newElement = document.createElement("span");

        newElement.innerHTML = `You: ${text}`;
        newElement.classList.add('bg-slate-100', 'py-2', 'rounded-xl', 'mb-2', 'px-4', 'flex');
        chatBody.appendChild(newElement);
      },
      focusInput(el) {
        el.focus();
        document.addEventListener('htmx:afterSwap', function (event) {
          el.value = '';
        });
      },
      scrollToBottom(el) {
        document.addEventListener('htmx:afterSwap', function (event) {
          el.scrollTop = el.scrollHeight;
        });
      },
    };
  }
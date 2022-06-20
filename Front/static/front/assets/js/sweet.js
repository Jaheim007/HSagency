htmx.on("showMessage", (event) => {
    Swal.fire({
        icon: event.detail.icon,
        title: event.detail.title,
        text: event.detail.message,
    })
})
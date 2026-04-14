document.addEventListener("DOMContentLoaded", function () {

    const forms = document.querySelectorAll("form");

    forms.forEach(function(form) {
        form.addEventListener("submit", function(e) {
            e.preventDefault();
            alert("Form Submitted Successfully ✅");
        });
    });

});

var modal = document.querySelector(".modal");
var openModalLinks = document.querySelectorAll(".open-modal-link");
var closeBtn = document.querySelector(".close");
var form = document.querySelector("#meal-plan-form");
var dayInput = form.querySelector("input[name='day']");
var categoryInput = form.querySelector("input[name='category']");

openModalLinks.forEach(function(link) {
    link.addEventListener("click", function(event) {
        event.preventDefault();
        var day = link.dataset.day;
        var category = link.dataset.category;

        // Set the values of the hidden fields
        dayInput.value = day;
        categoryInput.value = category;

        modal.style.display = "block";
    });
});

closeBtn.addEventListener("click", function() {
    modal.style.display = "none";
});

window.addEventListener("click", function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});

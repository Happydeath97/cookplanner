const modal = document.querySelector(".modal");
const openModalLinks = document.querySelectorAll(".open-modal-link");
const closeBtn = document.querySelector(".close");
const form = document.querySelector("#meal-plan-form");
const dayInput = form.querySelector("input[name='day']");
const categoryInput = form.querySelector("input[name='category']");

openModalLinks.forEach(function(link) {
    link.addEventListener("click", function(event) {
        event.preventDefault();
        const day = link.dataset.day;
        const category = link.dataset.category;

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

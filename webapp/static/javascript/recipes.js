const sButton = document.getElementById("selectIngredient");
const sInputField = document.getElementById("ingredients");
const hInputField = document.getElementById("selectedIngredients");
const sItemsContainer = document.getElementById("selectedIngredientsContainer");
const arrayOfSelectedI = [];

// Add an event listener to the input field
sInputField.addEventListener('keydown', function(event) {
  if (event.keyCode === 13) { // Check if Enter key (key code 13) is pressed
    event.preventDefault(); // Prevent the default form submission behavior
    sButton.click(); // Programmatically trigger a click event on the Select button
  }
});

function jinjaArrayConstructor() {
    const arr = []; // Initialize an empty array to store the content

    // Select all div elements with class "passing-value"
    const divs = document.querySelectorAll('.passing-value');
    // Loop through the selected divs and append their content to the array
    divs.forEach((div) => {
        arr.push(div.textContent); // Append the content of the div to the array
    });


    return arr; // Return the array with the content
}
const jinjaArr = jinjaArrayConstructor();


$(function () {
    // Initialize autocomplete on the input field
    $("#ingredients").autocomplete({
        source: jinjaArr,
        // Specify other options as needed
    });
});

// Function to update the selected ingredients container
function updateSelectedIngredients() {
    sItemsContainer.innerHTML = ""; // Clear the container

    // Iterate through arrayOfSelectedI and create a div for each selected ingredient
    arrayOfSelectedI.forEach((ingredient, index) => {
        const div = document.createElement("div");
        div.className = "sItem-container";

        // Create a text node with the ingredient
        const ingredientText = document.createTextNode(ingredient);
        div.appendChild(ingredientText);

        // Create a button to remove the ingredient
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "X";
        deleteButton.className = "sItem-button";
        deleteButton.addEventListener("click", () => {
            // Remove the ingredient from the array
            arrayOfSelectedI.splice(index, 1);

            // Update the selected ingredients container
            updateSelectedIngredients();
            hInputField.value = arrayOfSelectedI.join('&');
        });

        div.appendChild(deleteButton);
        sItemsContainer.appendChild(div);
    });
}


// Attach a click event handler to the sButton
sButton.addEventListener("click", function (event) {
    event.preventDefault(); // Prevent the form submission (if it's inside a form)

    // Get the current content of hInputField and sInputField
    const selectedIngredient = sInputField.value.trim();
    // Check if sInputField is not empty
    if (selectedIngredient !== "" && !arrayOfSelectedI.includes(selectedIngredient)) {
        arrayOfSelectedI.push(selectedIngredient);
        // Clear the sInputField for the next ingredient
        sInputField.value = "";

        hInputField.value = arrayOfSelectedI.join('&');
        updateSelectedIngredients();
    }
});
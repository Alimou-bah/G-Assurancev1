document.addEventListener("DOMContentLoaded", function () {
  const deleteButton = document.getElementById("deleteButton");
  const confirmationDialog = document.getElementById("confirmationDialog");
  const confirmYes = document.getElementById("confirmYes");
  const confirmNo = document.getElementById("confirmNo"); // Bouton pour annuler la suppression

  deleteButton.addEventListener("click", function () {
    confirmationDialog.style.display = "flex";
  });

  confirmYes.addEventListener("click", function () {
    // Ajoutez ici la logique de suppression de l'élément
    confirmationDialog.style.display = "none";
    alert("Élément supprimé.");
  });

  confirmNo.addEventListener("click", function () {
    confirmationDialog.style.display = "none";
  });

  // Fermer la boîte de dialogue si l'utilisateur clique en dehors de celle-ci
  window.addEventListener("click", function (event) {
    if (event.target === confirmationDialog) {
      confirmationDialog.style.display = "none";
    }
  });
});

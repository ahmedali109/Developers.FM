document.querySelectorAll(".tab-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    document
      .querySelectorAll(".tab-btn")
      .forEach((b) => b.classList.remove("active"));
    document
      .querySelectorAll(".tab-content")
      .forEach((c) => c.classList.remove("active"));

    btn.classList.add("active");
    const tabId = btn.getAttribute("data-tab");
    document.getElementById(tabId).classList.add("active");
  });
});

const modal = document.getElementById("questionModal");
const openModalBtns = document.querySelectorAll(".btn-ask-question");
const closeModalBtn = document.getElementById("closeModalBtn");
const cancelBtn = document.getElementById("cancelBtn");
const receiverSelect = document.querySelector('select[name="receiver"]');

// Handle all Ask Question buttons
openModalBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    modal.classList.add("active");
    document.body.style.overflow = "hidden";
    // Reset the dropdown when opening from other sections
    if (receiverSelect && !btn.getAttribute("data-user-id")) {
      receiverSelect.value = "";
    }
  });
});

// Handle Ask buttons on user cards
document.querySelectorAll(".btn-ask-user").forEach((btn) => {
  btn.addEventListener("click", () => {
    const userId = btn.getAttribute("data-user-id");
    const userName = btn.getAttribute("data-user-name");

    // Set the selected user in the dropdown
    if (receiverSelect) {
      receiverSelect.value = userId;
    }

    // Open the modal
    modal.classList.add("active");
    document.body.style.overflow = "hidden";
  });
});

const closeModal = () => {
  modal.classList.remove("active");
  document.body.style.overflow = "auto";
};

closeModalBtn.addEventListener("click", closeModal);
cancelBtn.addEventListener("click", closeModal);

modal.addEventListener("click", (e) => {
  if (e.target === modal) {
    closeModal();
  }
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && modal.classList.contains("active")) {
    closeModal();
  }
});

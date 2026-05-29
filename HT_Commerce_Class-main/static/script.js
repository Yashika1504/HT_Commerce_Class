  window.onload = function () {
    if (!sessionStorage.getItem('announcementShown')) {
      setTimeout(() => {
        document.getElementById('announcement-banner').classList.add('active');
        sessionStorage.setItem('announcementShown', 'true');
      }, 800);
    }
  };

  function closeAnnouncement() {
    document.getElementById('announcement-banner').classList.remove('active');
  }

//  JavaScript for Modal
        function openModal(image) {
            var modal = document.getElementById("imageModal");
            var modalImg = document.getElementById("modalImage");

            modal.style.display = "flex";
            modalImg.src = image.src;
        }

        function closeModal() {
            document.getElementById("imageModal").style.display = "none";
        }

// JavaScript for Counter Animation
  document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll('.counter');
    counters.forEach(counter => {
      const updateCount = () => {
        const target = +counter.getAttribute('data-count');
        const count = +counter.innerText;
        const speed = 20;
        const increment = target / speed;

        if (count < target) {
          counter.innerText = Math.ceil(count + increment);
          setTimeout(updateCount, 40);
        } else {
          counter.innerText = target;
        }
      };
      updateCount();
    });
  });

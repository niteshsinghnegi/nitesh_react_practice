const url = "https://kontests.net/api/v1/all";

// HTML se container select
const cardContainer = document.getElementById("cardContainer");

// Loading message
cardContainer.innerHTML = `
  <div class="col-12">
    <h4 class="text-center">Loading contests...</h4>
  </div>
`;

// Fetch API
fetch(url)
  .then((response) => response.json())
  .then((data) => {
    let html = "";

    data.forEach((contest) => {
      html += `
        <div class="col-md-4 mb-4">
          <div class="card h-100 shadow-sm">
            <div class="card-body">
              <h5 class="card-title">${contest.name}</h5>

              <p class="card-text">
                <strong>Platform:</strong> ${contest.site}<br>
                <strong>Start:</strong> ${contest.start_time}<br>
                <strong>End:</strong> ${contest.end_time}
              </p>

              <a href="${contest.url}" 
                 target="_blank" 
                 class="btn btn-primary btn-sm">
                Visit Contest
              </a>
            </div>
          </div>
        </div>
      `;
    });

    // Cards inject into HTML
    cardContainer.innerHTML = html;
  })
  .catch((error) => {
    cardContainer.innerHTML = `
      <div class="col-12">
        <h4 class="text-danger text-center">
          Failed to load contests
        </h4>
      </div>
    `;
    console.error(error);
  });

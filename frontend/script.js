function showTab(tabName, btn) {

    document.querySelectorAll(".tab-content").forEach(tab => {
        tab.style.display = "none";
    });

    document.querySelectorAll(".tab").forEach(button => {
        button.classList.remove("active");
    });

    document.getElementById(tabName).style.display = "block";
    btn.classList.add("active");
}


async function analyze() {

    const username = document.getElementById("username").value.trim();

    if (!username) {
        alert("Please enter a GitHub username.");
        return;
    }

    document.getElementById("result").style.display = "none";

    const loader = document.getElementById("loader");
    const loadingText = document.getElementById("loading-text");

    loader.style.display = "block";

    try {

        loadingText.innerText = "🔍 Analyzing GitHub Profile...";

        // ----------------------------
        // SUMMARY
        // ----------------------------

        const summaryResponse = await fetch("analyze-summary",{

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                github_username: username
            })

        });

        const summaryData = await summaryResponse.json();

        if (!summaryResponse.ok) {
            throw new Error(summaryData.detail);
        }


        loadingText.innerText = "🤖 Preparing Interview Questions...";


        // ----------------------------
        // INTERVIEW
        // ----------------------------

        const interviewResponse = await fetch("/generate-interview", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                summary: summaryData.summary
            })

        });

        const interviewData = await interviewResponse.json();

        if (!interviewResponse.ok) {
            throw new Error(interviewData.detail);
        }

        loader.style.display = "none";
        document.getElementById("result").style.display = "block";


        // ----------------------------
        // SUMMARY
        // ----------------------------

        document.getElementById("summary").innerHTML = `

        <div class="card">

        ${marked.parse(summaryData.summary)}

        </div>

        `;


        // ----------------------------
        // PROJECTS
        // ----------------------------

        const projectRegex = /# 📂 Top Projects([\s\S]*?)(# ⭐|$)/;

        const projectMatch = summaryData.summary.match(projectRegex);

        document.getElementById("projects").innerHTML = `

        <div class="card">

        <h2>📂 Top Projects</h2>

        ${projectMatch
            ? marked.parse(projectMatch[1])
            : "<p>Projects information unavailable.</p>"}

        </div>

        `;


        // ----------------------------
        // INTERVIEW
        // ----------------------------

        document.getElementById("interview").innerHTML = `

        <div class="card">

        ${marked.parse(interviewData.interview)}

        </div>

        `;

    }

    catch (error) {

        loader.style.display = "none";

        document.getElementById("result").style.display = "block";

        document.getElementById("summary").innerHTML = `

        <div class="card">

        <h2>❌ Error</h2>

        <p>${error.message}</p>

        </div>

        `;

    }

}
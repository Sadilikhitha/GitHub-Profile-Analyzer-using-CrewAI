async function analyze() {

    const username = document.getElementById("username").value.trim();

    if (!username) {
        alert("Please enter a GitHub username.");
        return;
    }

    const loader = document.getElementById("loader");
    const output = document.getElementById("output");
    const loadingText = document.getElementById("loading-text");

    output.innerHTML = "";
    loader.style.display = "block";

    const messages = [
        "🔍 Connecting to GitHub...",
        "📂 Fetching repositories...",
        "🧠 Analyzing projects and technologies...",
        "📊 Extracting developer skills...",
        "📝 Generating developer summary...",
        "🤖 Writing technical blog...",
        "✨ Finalizing results..."
    ];

    let i = 0;

    const animation = setInterval(() => {

        loadingText.innerText = messages[i];

        if (i < messages.length - 1) {
            i++;
        }

    }, 1500);

    try {

        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                github_username: username
            })
        });

        const data = await response.json();

        clearInterval(animation);
        loader.style.display = "none";

        console.log(data);

        if (data.result) {

            output.innerHTML = marked.parse(data.result);

        } else {

            output.innerHTML = `
                <div style="
                    background:#fff3cd;
                    color:#856404;
                    border:1px solid #ffeeba;
                    padding:20px;
                    border-radius:10px;
                ">
                    <h3>⚠️ AI Analysis Failed</h3>
                    <p>${data.error || data.detail || "Unknown error occurred."}</p>
                </div>
            `;

        }

    } catch (error) {

        clearInterval(animation);
        loader.style.display = "none";

        console.error(error);

        output.innerHTML = `
            <div style="
                background:#fee2e2;
                color:#b91c1c;
                border:1px solid #fecaca;
                padding:20px;
                border-radius:10px;
            ">
                <h3>❌ Connection Error</h3>
                <p>Unable to connect to the FastAPI backend.</p>
            </div>
        `;

    }

}
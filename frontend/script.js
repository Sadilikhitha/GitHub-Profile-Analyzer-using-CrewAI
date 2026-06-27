async function analyze() {

    const username = document.getElementById("username").value;
    
    const response = await fetch("/analyze",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            github_username:username
        })
    });

    const data = await response.json();

    document.getElementById("output").innerHTML = marked.parse(data.result);
}
async function callAPI() {
    const inputText = document.getElementById("inputText").value;
    const taskType = document.getElementById("taskType").value;

    const response = await fetch("http://localhost:8080/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            task_type: taskType,
            input_text: inputText
        })
    });

    const data = await response.json();

    document.getElementById("output").innerText =
        JSON.stringify(data, null, 2);
}
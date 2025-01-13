import React, { useState } from "react";

const App = () => {
  const [url, setUrl] = useState("");
  const [response, setResponse] = useState("");

  const handleSearch = async () => {
    try {
      const res = await fetch("http://127.0.0.1:5000/process-url", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
      });
      const data = await res.json();
      setResponse(data.message);
    } catch (error) {
      console.error("Error:", error);
      setResponse("Error occurred while processing the URL.");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>URL Processor</h1>
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter the URL of the product page"
        style={{ width: "300px", marginRight: "10px", padding: "5px" }}
      />
      <button onClick={handleSearch} style={{ padding: "5px 10px" }}>
        Search
      </button>
      {response && <p style={{ marginTop: "20px" }}>{response}</p>}
    </div>
  );
};

export default App;

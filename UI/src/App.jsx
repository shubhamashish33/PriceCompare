import React, { useState } from "react";

const App = () => {
  const [url, setUrl] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    try {
      const res = await fetch("http://localhost:8000/process-url", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
      });
      const result = await res.json();

      if (res.ok) {
        setData(result.data);
        setError("");
      } else {
        setError(result.detail || "Error occurred while processing the URL.");
        setData(null);
      }
    } catch (err) {
      console.error("Error:", err);
      setError("Error occurred while processing the URL.");
      setData(null);
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

      {error && <p style={{ color: "red", marginTop: "20px" }}>{error}</p>}

      {data && (
        <div style={{ display: "flex", gap: "20px", marginTop: "20px" }}>
          {/* Flipkart Card */}
          {data.Flipkart && (
            <div
              style={{
                border: "1px solid #ccc",
                padding: "10px",
                borderRadius: "5px",
                width: "300px",
                boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
              }}
            >
              <h2>Flipkart</h2>
              <p><strong>Title:</strong> {data.Flipkart.Title}</p>
              <p><strong>Price:</strong> ₹{data.Flipkart.Price}</p>
              <a
                href={data.Flipkart.FlipkartLink}
                target="_blank"
                rel="noopener noreferrer"
                style={{ color: "blue" }}
              >
                View on Flipkart
              </a>
            </div>
          )}

          {/* Amazon Card */}
          {data.Amazon && (
            <div
              style={{
                border: "1px solid #ccc",
                padding: "10px",
                borderRadius: "5px",
                width: "300px",
                boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
              }}
            >
              <h2>Amazon</h2>
              <p><strong>Title:</strong> {data.Amazon.Title}</p>
              <p><strong>Price:</strong> ₹{data.Amazon.Price}</p>
              <a
                href={data.Amazon.AmazonLink}
                target="_blank"
                rel="noopener noreferrer"
                style={{ color: "blue" }}
              >
                View on Amazon
              </a>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default App;

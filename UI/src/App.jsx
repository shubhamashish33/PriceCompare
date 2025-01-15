import React, { useState } from "react";

const App = () => {
  const [url, setUrl] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);
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
    } finally {
      setLoading(false);
    }
  };
  const formatCurrency = (value) => {
    return new Intl.NumberFormat('en-IN', { // Use 'en-IN' for Indian numbering format
      style: 'currency',
      currency: 'INR', // You can change this to 'USD', 'EUR', etc., based on your requirement
      maximumFractionDigits: 0, // No decimals
    }).format(value);
  };
  

  return (
    <div className="container">
      <h1 className="title">Price Comparison</h1>
      <div className="searchbox">
        <input
          type="text"
          className="inptBox"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter the URL of the product"
        />
        <button className="btn" onClick={handleSearch}>
          Search
        </button>
      </div>

      {error && <p style={{ color: "red", marginTop: "20px" }}>{error}</p>}

      <div
        className={`card-container ${data ? "expanded" : ""}`}
      >
        {data &&
          Object.keys(data).map((key) => (
            <div className="cards" key={key}>
              <h2 className="card-header">{key}</h2>
              <p className="card-title"><strong>Title:</strong> {data[key].Title}</p>
              <p><strong>Price:</strong> {formatCurrency(data[key].Price)}</p>
              <a className="link"
                href={data[key][`${key}Link`]}
                target="_blank"
                rel="noopener noreferrer"
                style={{ color: "blue" }}
              >
                View on {key} <i class="fa-solid fa-up-right-from-square"></i>
              </a>
            </div>
          ))}
      </div>

      {loading && (
        <div className="loader-popup">
          <div className="loader"></div>
        </div>
      )}
    </div>
  );
};

export default App;

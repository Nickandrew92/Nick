
// Import necessary libraries
import React, { useState } from 'react';

// Define the main component
const CruiseSearchForm = () => {
  // Define state variables
  const [startDateRangeBeginning, setStartDateRangeBeginning] = useState('');
  const [startDateRangeEnd, setStartDateRangeEnd] = useState('');
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    // Construct the request payload
    const payload = {
      start_date_range_beginning: startDateRangeBeginning,
      start_date_range_end: startDateRangeEnd,
    };

    try {
      // Make the API call
      const response = await fetch('http://localhost:5000/widgety-cruise-search', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="cruise-search-form">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="startDateRangeBeginning">Start Date Range Beginning:</label>
          <input
            type="date"
            id="startDateRangeBeginning"
            value={startDateRangeBeginning}
            onChange={(e) => setStartDateRangeBeginning(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="startDateRangeEnd">Start Date Range End:</label>
          <input
            type="date"
            id="startDateRangeEnd"
            value={startDateRangeEnd}
            onChange={(e) => setStartDateRangeEnd(e.target.value)}
            required
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Loading...' : 'Search'}
        </button>
      </form>
      {results && (
        <div className="results">
          <h2>Search Results:</h2>
          <pre>{JSON.stringify(results, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default CruiseSearchForm;

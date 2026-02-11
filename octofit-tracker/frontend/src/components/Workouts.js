import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container mt-4"><p>Loading workouts...</p></div>;
  if (error) return <div className="container mt-4"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">Workouts</h2>
        <button className="btn btn-primary">Create Workout</button>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th>Workout Name</th>
              <th>Description</th>
              <th>Difficulty</th>
              <th>Duration (min)</th>
              <th>Category</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map(workout => (
              <tr key={workout.id}>
                <td><strong>{workout.name}</strong></td>
                <td>{workout.description}</td>
                <td>
                  {workout.difficulty && (
                    <span className={`badge bg-${workout.difficulty === 'Easy' ? 'success' : workout.difficulty === 'Medium' ? 'warning text-dark' : 'danger'}`}>
                      {workout.difficulty}
                    </span>
                  )}
                </td>
                <td>{workout.duration || '-'}</td>
                <td>{workout.category || '-'}</td>
                <td>
                  <button className="btn btn-sm btn-outline-primary me-1">View</button>
                  <button className="btn btn-sm btn-outline-success">Start</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {workouts.length === 0 && <div className="alert alert-info">No workouts found.</div>}
    </div>
  );
}

export default Workouts;

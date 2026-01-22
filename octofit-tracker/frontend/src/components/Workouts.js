import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts - Fetching from API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts - Raw API response:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts - Processed data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-2">Loading workouts...</p>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="alert alert-danger" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p>{error}</p>
      </div>
    </div>
  );

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">💪 Workout Suggestions</h2>
        <button className="btn btn-info">
          <i className="bi bi-arrow-clockwise me-2"></i>Refresh Suggestions
        </button>
      </div>
      {workouts.length === 0 ? (
        <div className="empty-state">
          <p className="lead">No workout suggestions found.</p>
          <p className="text-muted">Check back later for personalized workout recommendations!</p>
        </div>
      ) : (
        <div className="row">
          {workouts.map((workout, index) => {
            let difficultyColor = 'bg-secondary';
            if (workout.difficulty_level === 'Easy') difficultyColor = 'bg-success';
            else if (workout.difficulty_level === 'Medium') difficultyColor = 'bg-warning text-dark';
            else if (workout.difficulty_level === 'Hard') difficultyColor = 'bg-danger';
            
            return (
              <div key={workout.id || index} className="col-md-6 col-lg-4 mb-4">
                <div className="card h-100">
                  <div className="card-body d-flex flex-column">
                    <h5 className="card-title">{workout.name}</h5>
                    <div className="mb-3">
                      <span className={`badge ${difficultyColor} me-2`}>{workout.difficulty_level}</span>
                      <span className="badge bg-secondary">{workout.workout_type}</span>
                    </div>
                    {workout.description && (
                      <p className="card-text flex-grow-1">{workout.description}</p>
                    )}
                    <hr />
                    <div className="d-flex justify-content-between align-items-center mb-2">
                      <span className="text-muted">Duration</span>
                      <span><strong>{workout.duration} min</strong></span>
                    </div>
                    <div className="d-flex justify-content-between align-items-center mb-3">
                      <span className="text-muted">Est. Calories</span>
                      <span className="badge bg-success">{workout.estimated_calories} cal</span>
                    </div>
                    <div className="d-grid gap-2">
                      <button className="btn btn-primary">Start Workout</button>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default Workouts;

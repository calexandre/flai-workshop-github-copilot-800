import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Teams - Fetching from API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams - Raw API response:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams - Processed data:', teamsData);
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Teams - Error fetching data:', error);
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
        <p className="mt-2">Loading teams...</p>
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
        <h2 className="mb-0">👥 Teams</h2>
        <button className="btn btn-primary">
          <i className="bi bi-plus-circle me-2"></i>Create Team
        </button>
      </div>
      {teams.length === 0 ? (
        <div className="empty-state">
          <p className="lead">No teams found.</p>
          <p className="text-muted">Create a team to start competing together!</p>
        </div>
      ) : (
        <div className="row">
          {teams.map((team, index) => (
            <div key={team.id || index} className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">{team.name}</h5>
                  <p className="card-text flex-grow-1">
                    {team.description || 'No description available'}
                  </p>
                  <hr />
                  <div className="d-flex justify-content-between align-items-center mb-3">
                    <span className="text-muted">Members</span>
                    <span className="badge bg-info">{team.member_count || team.members?.length || 0}</span>
                  </div>
                  <div className="d-flex justify-content-between align-items-center mb-3">
                    <span className="text-muted">Total Points</span>
                    <span className="badge bg-success">{team.total_points || 0}</span>
                  </div>
                  <div className="d-grid gap-2">
                    <button className="btn btn-outline-primary btn-sm">View Details</button>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Teams;

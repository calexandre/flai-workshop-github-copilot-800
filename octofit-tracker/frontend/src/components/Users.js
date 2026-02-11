import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
    console.log('Users API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Users fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        setUsers(Array.isArray(usersData) ? usersData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching users:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container mt-4"><p>Loading users...</p></div>;
  if (error) return <div className="container mt-4"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <div className="row">
        {users.map(user => (
          <div key={user.id} className="col-md-6 mb-3">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{user.username}</h5>
                <p className="card-text">Email: {user.email}</p>
                {user.first_name && <p className="card-text">Name: {user.first_name} {user.last_name}</p>}
                {user.profile && (
                  <>
                    {user.profile.age && <p className="card-text">Age: {user.profile.age}</p>}
                    {user.profile.weight && <p className="card-text">Weight: {user.profile.weight} kg</p>}
                    {user.profile.height && <p className="card-text">Height: {user.profile.height} cm</p>}
                  </>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
      {users.length === 0 && <p>No users found.</p>}
    </div>
  );
}

export default Users;

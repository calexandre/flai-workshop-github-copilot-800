import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand d-flex align-items-center" to="/">
            <img src="/octofitapp-small.png" alt="OctoFit Logo" height="40" className="me-2" />
            <span>OctoFit Tracker</span>
          </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container-fluid">
        <Routes>
          <Route path="/" element={
            <div className="container mt-4">
              <div className="text-center mb-5">
                <h1 className="display-4 fw-bold mb-3">Welcome to OctoFit Tracker</h1>
                <p className="lead">Track your fitness activities, compete with teams, and achieve your goals!</p>
              </div>
              
              <div className="row g-4">
                <div className="col-md-4">
                  <div className="card h-100 text-center">
                    <div className="card-body">
                      <h3 className="card-title">📊 Activities</h3>
                      <p className="card-text">Log and track your daily fitness activities</p>
                      <Link to="/activities" className="btn btn-primary">View Activities</Link>
                    </div>
                  </div>
                </div>
                
                <div className="col-md-4">
                  <div className="card h-100 text-center">
                    <div className="card-body">
                      <h3 className="card-title">🏆 Leaderboard</h3>
                      <p className="card-text">Compete and see who's leading the pack</p>
                      <Link to="/leaderboard" className="btn btn-success">View Leaderboard</Link>
                    </div>
                  </div>
                </div>
                
                <div className="col-md-4">
                  <div className="card h-100 text-center">
                    <div className="card-body">
                      <h3 className="card-title">👥 Teams</h3>
                      <p className="card-text">Join teams and achieve fitness goals together</p>
                      <Link to="/teams" className="btn btn-info">View Teams</Link>
                    </div>
                  </div>
                </div>
              </div>
              
              <div className="row g-4 mt-2">
                <div className="col-md-6">
                  <div className="card h-100 text-center">
                    <div className="card-body">
                      <h3 className="card-title">👤 Users</h3>
                      <p className="card-text">Browse community members and their profiles</p>
                      <Link to="/users" className="btn btn-secondary">View Users</Link>
                    </div>
                  </div>
                </div>
                
                <div className="col-md-6">
                  <div className="card h-100 text-center">
                    <div className="card-body">
                      <h3 className="card-title">💪 Workouts</h3>
                      <p className="card-text">Discover personalized workout suggestions</p>
                      <Link to="/workouts" className="btn btn-warning">View Workouts</Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;

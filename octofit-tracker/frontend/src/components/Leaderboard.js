import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('https://ominous-space-funicular-jqgwr57pqqjhqjj7-8000.app.github.dev/leaderboard')
//    fetch('https://ominous-space-funicular-jqgwr57pqqjhqjj7-8000.app.github.dev/api/leaderboard/')
      .then(response => response.json())
      .then(data => setLeaderboard(data));
  }, []);

  return (
    <div>
      <h1 className="text-center">Leaderboard</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Score</th>
            <th>User ID</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map(entry => (
            <tr key={entry.id}>
              <td>{entry.id}</td>
              <td>{entry.name}</td>
              <td>{entry.score}</td>
              <td>{entry.user_id}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Leaderboard;

```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      const response = await axios.get('/api/users');
      setUsers(response.data);
    };

    fetchUsers();
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
```
```jsx
import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const switchMode = () => setIsLogin(!isLogin);

  const submitHandler = async (e) => {
    e.preventDefault();
    const authData = { username, password };
    let url = 'http://localhost:5000/login';
    if (!isLogin) {
      url = 'http://localhost:5000/register';
    }
    try {
      const response = await axios.post(url, authData);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>{isLogin ? 'Login' : 'Register'}</h1>
      <form onSubmit={submitHandler}>
        <input
          type="text"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
          value={username}
        />
        <input
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
          value={password}
        />
        <button type="submit">{isLogin ? 'Login' : 'Register'}</button>
      </form>
      <button onClick={switchMode}>
        Switch to {isLogin ? 'Register' : 'Login'}
      </button>
    </div>
  );
};

export default App;
```
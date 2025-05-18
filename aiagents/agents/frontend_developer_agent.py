from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step
from aiagents.utils.file_writer import write_react_file


class FrontendDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="FrontendDeveloperAgent", role="Frontend Code Generator")

    @log_progress_step("FrontendDeveloperAgent", "Generating React frontend code")
    def execute(self, prompt: str) -> dict:
        """
        Generates basic React.js frontend code from the prompt.
        This agent focuses on generating App.jsx and one example component.
        """
        # Basic React layout
        app_code = """\
import React from 'react';
import Header from './components/Header';

function App() {
  return (
    <div className="App">
      <Header />
      <h1>Welcome to the AI-generated App</h1>
    </div>
  );
}

export default App;
"""

        header_code = """\
import React from 'react';

function Header() {
  return (
    <header style={{ padding: '1rem', background: '#f5f5f5' }}>
      <h2>Header Section</h2>
    </header>
  );
}

export default Header;
"""

        # Define the output structure
        files = {
            "output/client/src/App.jsx": app_code,
            "output/client/src/components/Header.jsx": header_code,
        }

        for path, content in files.items():
            write_react_file(path, content)

        self.remember("frontend_files", list(files.keys()))
        return {"generated_files": list(files.keys())}

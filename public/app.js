document.addEventListener('DOMContentLoaded', () => {
  // Theme toggle functionality
  const themeToggle = document.querySelector('.theme-toggle md-icon-button');
  const themeIcon = document.querySelector('.theme-toggle md-icon');
  
  themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    const isDarkMode = document.body.classList.contains('dark-theme');
    themeIcon.textContent = isDarkMode ? 'light_mode' : 'dark_mode';
  });
  
  // API integration
  const generateBtn = document.getElementById('generate-btn');
  const topicField = document.getElementById('topic');
  const useAdkCheckbox = document.getElementById('use-adk');
  const resultField = document.getElementById('result');
  
  generateBtn.addEventListener('click', async () => {
    const topic = topicField.value.trim();
    
    if (!topic) {
      alert('Please enter a topic');
      return;
    }
    
    // Show loading state
    generateBtn.disabled = true;
    resultField.value = 'Loading...';
    
    try {
      const response = await fetch('/api/playground', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          topic,
          use_adk: useAdkCheckbox.checked
        })
      });
      
      const data = await response.json();
      
      // Display the result
      if (data.error) {
        resultField.value = `Error: ${data.error}`;
      } else if (data.report) {
        resultField.value = data.report;
      } else if (data.result) {
        resultField.value = data.result;
      } else {
        resultField.value = 'Received response with unknown format';
      }
    } catch (error) {
      resultField.value = `Error: ${error.message}`;
      console.error('API request failed:', error);
    } finally {
      generateBtn.disabled = false;
    }
  });
  
  // Tab navigation
  const tabs = document.querySelector('md-tabs');
  tabs.addEventListener('change', (e) => {
    console.log(`Selected tab: ${e.target.activeTabIndex}`);
    // Implement tab navigation logic here
  });
  
  // GitHub button
  const githubButton = document.querySelector('md-outlined-button');
  githubButton.addEventListener('click', () => {
    window.open('https://github.com/groupthinking/mcp-tools-extension', '_blank');
  });
  
  // Get Started button
  const getStartedButton = document.querySelector('md-filled-button');
  getStartedButton.addEventListener('click', () => {
    const playgroundSection = document.querySelector('.playground');
    playgroundSection.scrollIntoView({ behavior: 'smooth' });
  });
  
  // Learn More buttons
  const learnMoreButtons = document.querySelectorAll('.card-actions md-text-button');
  
  learnMoreButtons.forEach((button, index) => {
    button.addEventListener('click', () => {
      const topics = [
        'MCP (Model Context Protocol) is an open standard for connecting AI systems with external context.',
        'Google ADK (Agent Development Kit) provides tools for building AI agents with Gemini models.',
        'Our integration is containerized with Docker for easy deployment in any environment.'
      ];
      
      alert(topics[index]);
    });
  });
}); 
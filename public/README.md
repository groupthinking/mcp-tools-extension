# MCP-ADK Integration Frontend

This directory contains the frontend for the MCP-ADK Integration project, built using Material Web components.

## Design

The frontend is designed to match the Material Web design system (https://material-web.dev/), using Material Design 3 components and theming.

## Features

- Modern, responsive UI using Material Web components
- Light/dark theme toggle
- Integration with the MCP-ADK backend API
- Interactive playground for testing the integration
- Material Design 3 color system

## Components Used

- Buttons (filled, outlined, text)
- Cards
- Text fields
- Checkboxes
- Tabs
- Icons and icon buttons

## Setup

The frontend is served by the Express backend and automatically built with the TypeScript project.

## Development

To make changes to the frontend:

1. Edit the files in the `public` directory
2. Run `npm run dev` to start the development server
3. Access the frontend at http://localhost:5000

## Structure

- `index.html` - Main HTML structure
- `styles.css` - CSS styling with Material Design tokens
- `app.js` - Frontend JavaScript functionality
- `site.webmanifest` - Progressive Web App manifest 
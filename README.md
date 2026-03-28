# Voice Recorder Web Application

A modern web application that allows users to record voice recordings directly from their browser or upload existing audio files. Built with React for the frontend and Express.js for the backend.

## Features

- **Voice Recording**: Record audio directly from your browser using the Web Audio API
- **File Upload**: Upload existing audio files (MP3, WAV, OGG, M4A, FLAC)
- **Drag & Drop**: Intuitive drag-and-drop interface for file uploads
- **Audio Preview**: Play back recordings before uploading
- **File Management**: View and manage all uploaded recordings
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Timer**: Shows recording duration while recording

## Tech Stack

### Frontend
- React 18
- HTML5 & CSS3
- Axios for HTTP requests
- Web Audio API for recording

### Backend
- Node.js
- Express.js
- Multer for file uploads
- CORS for cross-origin requests

## Installation

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Setup

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Install server dependencies**:
   ```bash
   npm install
   ```

3. **Install client dependencies**:
   ```bash
   npm run install-client
   ```

4. **Start the application**:
   - For development (runs both server and client):
     ```bash
     npm run dev
     ```
   - Or run them separately:
     ```bash
     # Start the backend server
     npm run server
     
     # In another terminal, start the frontend
     npm run client
     ```

5. **Open your browser** and navigate to `http://localhost:3000`

## Usage

### Recording Audio
1. Click the "Start Recording" button
2. Grant microphone permissions when prompted
3. Record your audio (timer will show duration)
4. Click "Stop Recording" when finished
5. Preview your recording in the audio player
6. Click "Upload Recording" to save it

### Uploading Files
1. Click on the upload area or drag and drop an audio file
2. Select an audio file from your device
3. The file will automatically upload
4. View all uploaded files in the "Uploaded Recordings" section

### Managing Recordings
- All recordings are stored in the `uploads` directory on the server
- You can play any uploaded recording directly from the interface
- File information includes name, size, and upload timestamp

## API Endpoints

### `POST /api/upload`
Upload an audio file
- **Body**: FormData with 'audio' field
- **Response**: JSON with file information

### `GET /api/files`
Get list of all uploaded files
- **Response**: Array of file objects with metadata

### `GET /uploads/:filename`
Serve uploaded audio files

## File Structure

```
voice-recorder-app/
├── server.js              # Express server
├── package.json           # Server dependencies
├── uploads/               # Uploaded audio files (auto-created)
├── client/
│   ├── public/
│   │   └── index.html     # HTML template
│   ├── src/
│   │   ├── App.js         # Main React component
│   │   ├── App.css        # Application styles
│   │   ├── index.js       # React entry point
│   │   └── index.css      # Global styles
│   └── package.json       # Client dependencies
└── README.md              # This file
```

## Future Enhancements

- **API Integration**: Connect to external speech-to-text or audio processing APIs
- **User Authentication**: Add user accounts and private recording storage
- **Audio Editing**: Basic audio editing capabilities (trim, crop, effects)
- **Cloud Storage**: Integration with cloud storage services (AWS S3, Google Cloud)
- **Real-time Transcription**: Live speech-to-text during recording
- **Voice Notes**: Add text notes and tags to recordings
- **Sharing**: Generate shareable links for recordings

## Troubleshooting

### Microphone Access
- Ensure you grant microphone permissions when prompted
- Check browser settings if microphone access is blocked
- Use HTTPS in production for microphone access

### File Upload Issues
- Check file size limit (50MB by default)
- Ensure file format is supported (audio files only)
- Verify server has write permissions for uploads directory

### Development Issues
- Make sure ports 3000 and 5000 are available
- Check Node.js version compatibility
- Clear browser cache if experiencing UI issues

## License

MIT License

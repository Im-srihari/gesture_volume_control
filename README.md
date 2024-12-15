# Gesture Volume Controller

A Python-based application that allows you to control your system's volume using hand gestures captured through your webcam. This project combines computer vision and hand tracking to create an intuitive way to adjust volume settings without touching your device.

## Project Components

### 1. Hand Tracking Module (`hand_tracking.py`)
- Custom-built hand tracking class using MediaPipe
- Features:
  - Real-time hand detection
  - Multi-hand support (up to 2 hands)
  - Landmark detection and drawing
  - FPS monitoring
  - Configurable detection parameters

### 2. Volume Controller (`volume_controller.py`)
- Main application that uses hand tracking for volume control
- Features:
  - Real-time volume adjustment
  - Visual feedback system
  - System volume integration
  - Distance-based control mechanism

## Prerequisites

- Python 3.x
- Required libraries:
  ```
  opencv-python
  mediapipe
  numpy
  pycaw
  comtypes
  ```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/gesture-volume-controller.git
cd gesture-volume-controller
```

2. Install the required packages:
```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

## Usage

1. Run the volume controller:
```bash
python volume_controller.py
```

2. Hand Gesture Controls:
   - Show your palm to the camera
   - Pinch your thumb and index finger together for minimum volume
   - Spread them apart to increase volume
   - The distance between fingers controls the volume level
   - Visual feedback shows:
     - Blue line: Current finger distance
     - Green circle: Minimum volume indicator
     - Red circles: Maximum volume indicator

## Technical Details

### Hand Tracking Module
- Uses MediaPipe's hand detection model
- Provides landmark detection for 21 hand points
- Configurable parameters:
  - `mode`: Static/Dynamic detection
  - `max_hands`: Number of hands to detect
  - `detection_confidence`: Minimum detection confidence threshold
  - `track_confidence`: Minimum tracking confidence threshold

### Volume Controller
- Maps finger distance to volume range
- Uses pycaw for Windows audio control
- Real-time volume adjustment with visual feedback
- FPS counter for performance monitoring

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- MediaPipe for hand tracking solutions
- Pycaw for Windows audio control
- OpenCV community for computer vision tools

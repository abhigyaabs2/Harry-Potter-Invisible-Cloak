# 🪄 Harry Potter Invisible Cloak

Transform yourself into a wizard with this OpenCV-powered invisible cloak effect! Using computer vision and color detection, this project recreates the magical invisibility cloak from Harry Potter using just a webcam and a colored t-shirt.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-v4.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- **Real-time invisibility effect** using your webcam
- **Multiple color support** - works with red, blue, green, and yellow clothing
- **Advanced skin tone filtering** to avoid detecting your face/hands
- **Adaptive color detection** with multiple ranges for consistent results
- **Interactive controls** for background recalibration and mask visualization
- **Optimized for dark green t-shirts** with enhanced processing

## 🎯 How It Works

The invisible cloak uses computer vision techniques:

1. **Background Subtraction**: Captures a clean background when you're not in frame
2. **Color Detection**: Identifies your colored t-shirt using HSV color space
3. **Mask Creation**: Creates a mask of the detected cloth areas
4. **Image Replacement**: Replaces cloth pixels with corresponding background pixels
5. **Real-time Processing**: Applies the effect live through your webcam

## 🚀 Quick Start

### Prerequisites

```bash
pip install opencv-python numpy
```

### Installation

1. Clone this repository:
```bash
git clone [https://github.com/yourusername/invisible-cloak.git](https://github.com/abhigyaabs2/Harry-Potter-Invisible-Cloak)
cd invisible-cloak
```

2. Run the script:
```bash
python invisible_cloak.py
```

### Usage

1. **Choose option 1**: Test your camera setup
2. **Choose option 2**: Calibrate color detection for your specific t-shirt
3. **Choose option 3**: Start the invisible cloak effect!

## 🎮 Controls

| Key | Action |
|-----|--------|
| `q` | Quit the application |
| `c` | Recalibrate background |
| `m` | Toggle mask visualization |

## 🎨 Supported Colors

The script works best with these t-shirt colors:

- **🔴 Red**: Excellent detection, works in most lighting
- **🔵 Blue**: Very reliable, good contrast with skin
- **🟢 Green**: Good results, optimized for dark green
- **🟡 Yellow**: Works well with proper lighting

## 📋 Step-by-Step Guide

### 1. Setup Phase
- Position yourself in front of your webcam
- Ensure good, even lighting
- Have your colored t-shirt ready

### 2. Background Capture
- **Step completely out of frame** when prompted
- Keep the camera steady during capture
- Wait for "Background captured!" message

### 3. Cloak Effect
- Enter the frame wearing/holding your colored t-shirt
- **Stretch the t-shirt** to cover areas you want invisible
- **Move slowly** for best results
- Use the mask view (`m` key) to check detection

## 🛠️ Troubleshooting

### Common Issues

**Problem**: Cloth not being detected
- **Solution**: Use the color calibration feature (option 2)
- **Tip**: Ensure good lighting and stretch the cloth flat

**Problem**: Skin being made invisible instead of cloth
- **Solution**: The script has built-in skin tone filtering
- **Tip**: Use a cloth color that contrasts well with your skin

**Problem**: Inconsistent detection
- **Solution**: Move slowly and maintain consistent lighting
- **Tip**: Face the camera directly for best results

**Problem**: Parts of t-shirt still visible
- **Solution**: Use the enhanced processing for dark colors
- **Tip**: Try a brighter colored t-shirt if possible

### Optimization Tips

1. **Lighting**: Use bright, even lighting without harsh shadows
2. **Background**: Choose a simple, static background
3. **Movement**: Move slowly and deliberately
4. **Cloth**: Use solid colors without patterns or logos
5. **Camera**: Keep the camera steady and at eye level

## 🔧 Customization

### Adjusting Color Detection

To optimize for your specific t-shirt color, modify the HSV ranges in the code:

```python
# For your specific green shade
lower_green = np.array([YOUR_H_MIN, YOUR_S_MIN, YOUR_V_MIN])
upper_green = np.array([YOUR_H_MAX, YOUR_S_MAX, YOUR_V_MAX])
```

Use the color calibration tool to find these values!

### Adding New Colors

To add support for new colors:

1. Find the HSV range using the calibration tool
2. Add the color detection in the main loop
3. Update the mask creation logic

## 📱 System Requirements

- **Python 3.7+**
- **OpenCV 4.0+**
- **NumPy**
- **Webcam** (built-in or external)
- **Good lighting conditions**

## 🎪 Demo Tips

For the best "magical" effect:

- **Dramatic reveals**: Start without the t-shirt, then put it on
- **Partial invisibility**: Cover only parts of your body
- **Object invisibility**: Make objects "disappear" by wrapping them
- **Multiple people**: Take turns with the cloak effect

## 🐛 Known Limitations

- Works best with solid, bright colors
- Requires consistent lighting
- May struggle with very dark or very light colors
- Performance depends on camera quality and lighting conditions

## 🤝 Contributing

Feel free to contribute improvements:

- Better color detection algorithms
- Support for multiple simultaneous colors
- Performance optimizations
- Additional filter effects

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the magical world of Harry Potter
- Built using OpenCV computer vision library
- Thanks to the open-source community for computer vision resources


**Enjoy your magical invisibility powers! 🧙‍♂️✨**

For questions or issues, please open an issue on GitHub or check the troubleshooting section above.

#!/usr/bin/env python
# coding: utf-8

# In[12]:


import cv2
import numpy as np
import time

def create_invisible_cloak():

    
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    
    # Camera properties for better quality
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # Allowing camera to warm up
    time.sleep(2)
    
    # Capturing the background for a few seconds
    print("Setting up background. Please move out of the frame!")
    print("Background capture will start in 3 seconds...")
    time.sleep(3)
    
    background = None
    for i in range(30):
        ret, frame = cap.read()
        if ret:
            background = frame
        print(f"Capturing background... {i+1}/30")
        time.sleep(0.1)
    
    print("Background captured! You can now enter the frame with your cloak.")
    print("Press 'q' to quit, 'c' to recalibrate background, 'm' to show mask")
    print("Use a bright, solid-colored cloth for best results!")
    
    show_mask = False
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Flipping the frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        background_flipped = cv2.flip(background, 1)
        
        # Converting to HSV color space for better color detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # DARK GREEN T-SHIRT detection with adaptive thresholds
        # Multiple green ranges to catch different lighting conditions
        lower_green1 = np.array([35, 40, 20])   # Very dark green
        upper_green1 = np.array([85, 255, 180])
        lower_green2 = np.array([30, 60, 30])   # Medium dark green
        upper_green2 = np.array([90, 255, 200])
        lower_green3 = np.array([40, 80, 40])   # Brighter areas of dark green
        upper_green3 = np.array([80, 255, 220])
        
        # Create multiple masks and combine them
        mask1 = cv2.inRange(hsv, lower_green1, upper_green1)
        mask2 = cv2.inRange(hsv, lower_green2, upper_green2)
        mask3 = cv2.inRange(hsv, lower_green3, upper_green3)
        mask = cv2.bitwise_or(mask1, cv2.bitwise_or(mask2, mask3))
        
        # Enhanced skin tone filtering with multiple ranges
        lower_skin1 = np.array([0, 20, 70])    # Light skin
        upper_skin1 = np.array([20, 150, 255])
        lower_skin2 = np.array([0, 10, 60])    # Very light skin
        upper_skin2 = np.array([25, 80, 200])
        lower_skin3 = np.array([10, 30, 80])   # Medium skin
        upper_skin3 = np.array([25, 120, 220])
        
        skin_mask1 = cv2.inRange(hsv, lower_skin1, upper_skin1)
        skin_mask2 = cv2.inRange(hsv, lower_skin2, upper_skin2)
        skin_mask3 = cv2.inRange(hsv, lower_skin3, upper_skin3)
        skin_mask = cv2.bitwise_or(skin_mask1, cv2.bitwise_or(skin_mask2, skin_mask3))
        
       
        mask = cv2.bitwise_and(mask, cv2.bitwise_not(skin_mask))
        
       
        kernel_large = np.ones((9, 9), np.uint8)
        kernel_small = np.ones((5, 5), np.uint8)
        
       
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_large, iterations=4)
        
       
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_small, iterations=2)
        
      
        mask = cv2.dilate(mask, kernel_large, iterations=3)
        
        
        mask = cv2.medianBlur(mask, 25)  
        mask = cv2.GaussianBlur(mask, (15, 15), 0)  
        
       
        _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
        
        # Create inverse mask
        mask_inv = cv2.bitwise_not(mask)
        
        # Apply the masks
        res1 = cv2.bitwise_and(background_flipped, background_flipped, mask=mask)
        res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
        
        # Combine the results to create the invisible effect
        final_output = cv2.add(res1, res2)
        
        # Show mask for debugging if requested
        if show_mask:
            cv2.imshow('Mask (White = Detected Cloth)', mask)
        
        # Display the result
        cv2.imshow('Invisible Cloak', final_output)
        cv2.imshow('Original Frame', frame)
        
        # Handle key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            print("Recalibrating background...")
            print("Please move out of the frame!")
            time.sleep(2)
            for i in range(30):
                ret, frame = cap.read()
                if ret:
                    background = frame
            print("Background recalibrated!")
        elif key == ord('m'):
            show_mask = not show_mask
            if not show_mask:
                cv2.destroyWindow('Mask (White = Detected Cloth)')
            print(f"Mask display: {'ON' if show_mask else 'OFF'}")
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()

def test_camera():
    """Test if camera is working properly"""
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return False
    
    print("Camera test - press 'q' to quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
        
        cv2.imshow('Camera Test', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return True

def color_calibration():
    """
    Helper function to calibrate the color range for your specific cloth.
    Use this to find the best HSV values for your cloak color.
    """
    cap = cv2.VideoCapture(0)
    
    # Create trackbars for HSV adjustment
    cv2.namedWindow('Color Calibration')
    cv2.createTrackbar('H Min', 'Color Calibration', 0, 179, lambda x: None)
    cv2.createTrackbar('S Min', 'Color Calibration', 50, 255, lambda x: None)
    cv2.createTrackbar('V Min', 'Color Calibration', 50, 255, lambda x: None)
    cv2.createTrackbar('H Max', 'Color Calibration', 10, 179, lambda x: None)
    cv2.createTrackbar('S Max', 'Color Calibration', 255, 255, lambda x: None)
    cv2.createTrackbar('V Max', 'Color Calibration', 255, 255, lambda x: None)
    
    print("Adjust the trackbars to isolate your cloak color.")
    print("Press 'q' when you're satisfied with the color detection.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Get trackbar values
        h_min = cv2.getTrackbarPos('H Min', 'Color Calibration')
        s_min = cv2.getTrackbarPos('S Min', 'Color Calibration')
        v_min = cv2.getTrackbarPos('V Min', 'Color Calibration')
        h_max = cv2.getTrackbarPos('H Max', 'Color Calibration')
        s_max = cv2.getTrackbarPos('S Max', 'Color Calibration')
        v_max = cv2.getTrackbarPos('V Max', 'Color Calibration')
        
        # Create mask with current values
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(hsv, lower, upper)
        
        # Show original and mask
        cv2.imshow('Original', frame)
        cv2.imshow('Mask', mask)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print(f"Final HSV values:")
            print(f"Lower: [{h_min}, {s_min}, {v_min}]")
            print(f"Upper: [{h_max}, {s_max}, {v_max}]")
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("=== Harry Potter Invisible Cloak ===")
    print("Choose an option:")
    print("1. Test camera")
    print("2. Calibrate cloak color")
    print("3. Start invisible cloak effect")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        test_camera()
    elif choice == "2":
        color_calibration()
    elif choice == "3":
        create_invisible_cloak()
    else:
        print("Invalid choice. Running invisible cloak effect...")
        create_invisible_cloak()


# In[ ]:





# ### 

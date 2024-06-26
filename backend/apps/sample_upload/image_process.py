import cv2
import numpy as np




def analyze_colors(filepath):
    # Load the image
    image = cv2.imread(filepath)

    # Check if image is loaded
    if image is None:
        print(filepath)
        raise FileNotFoundError(f"Image at path {filepath} not found")

    # Resize the image for easier processing
    scale_percent = 50
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # Convert to grayscale and apply Gaussian blur
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges and perform morphological closing
    edges = cv2.Canny(blurred, 50, 150)
    kernel = np.ones((5, 5), np.uint8)
    morph = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Find contours and the largest one
    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        raise ValueError("No contours found in the image")

    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Crop the bottom 25% of the detected strip
    crop_bottom = int(h * 0.25)
    detected_strip_cropped = resized_image[y:y+h-crop_bottom, x:x+w]

    # Stretch vertically to a height of 800 pixels
    target_height = 800
    stretch_ratio = target_height / detected_strip_cropped.shape[0]
    detected_strip_stretched = cv2.resize(detected_strip_cropped, None, fx=1, fy=stretch_ratio, interpolation=cv2.INTER_LINEAR)

    # Crop 40% from the sides
    crop_percent = 40
    crop_pixels = int(detected_strip_stretched.shape[1] * crop_percent / 100)
    cropped_strip = detected_strip_stretched[:, crop_pixels:-crop_pixels]

    # Resize to a height of 800 pixels
    final_strip = cv2.resize(cropped_strip, (detected_strip_stretched.shape[1], target_height), interpolation=cv2.INTER_LINEAR)

    # Define the segment height and margin
    margin_top = final_strip.shape[0] // 20
    segment_height = (250) // 10  # 10 segments with margins

    start_y = margin_top
    average_colors = []

    # Iterate over 10 segments
    for i in range(10):
        end_y = start_y + segment_height
        
        top_pad = 5 if i > 0 else 0
        bottom_pad = 5 if i < 9 else 0
        segment_top = start_y + top_pad
        segment_bottom = end_y - bottom_pad

        segment = final_strip[segment_top:segment_bottom, :]
        average_segment_color = np.mean(segment, axis=(0, 1)).astype(int)
        average_colors.append(average_segment_color)

        # Draw rectangle for visualization (optional)
        cv2.rectangle(final_strip, (0, segment_top), (final_strip.shape[1], segment_bottom), (0, 255, 0), 2)

        start_y = end_y + margin_top  # Move to next segment

    # Define labels for the segments
    labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
    rgb_values = {}

    for i, color_value in enumerate(average_colors):
        # Convert BGR to RGB and store
        rgb_values[labels[i]] = color_value.tolist()[::-1]

    return rgb_values


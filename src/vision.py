def get_obstacle_grid():
    import cv2
    import numpy as np

    ROWS = 20
    COLS = 20

    # Load image manually
    frame = cv2.imread("image/layout.png")

    if frame is None:
        print("Image not found!")
        return None

    frame = cv2.resize(frame, (COLS, ROWS))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

    # Save processed image
    cv2.imwrite("outputs/obstacle_map.png", thresh)

    grid = []

    for i in range(ROWS):
        row = []
        for j in range(COLS):
            if thresh[i][j] > 0:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)

    return grid
import cv2
from cameras.camera_manager import init_cameras
from detection.board_loader import load_board_overlays

cam20, cam16, cam15 = init_cameras()
overlays = load_board_overlays()

while True:
    f20 = cam20.read()
    f16 = cam16.read()
    f15 = cam15.read()

    if f20 is not None:
        cv2.imshow("20", overlays["20"].draw(f20))
    if f16 is not None:
        cv2.imshow("16", overlays["16"].draw(f16))
    if f15 is not None:
        cv2.imshow("15", overlays["15"].draw(f15))

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam20.release()
cam16.release()
cam15.release()
cv2.destroyAllWindows()

import cv2
import time
import os


while True:
    ip_kamera = input("Cammera IP>")
    rtsp_url = f"rtsp://{ip_kamera}"
    cap = cv2.VideoCapture(rtsp_url)
    
    if cap.isOpened():
        print(f"Connected to {ip_kamera}")
        break
    else:
        print(f"ERROR: Could not connect to {ip_kamera}")
        time.sleep(3)
        os.system("cls")

while True:
    # Odczytanie klatki z kamery
    ret, frame = cap.read()

    # Sprawdzenie, czy klatka została poprawnie odczytana
    if not ret:
        print("error: failed to capture image")
        input("Press any key to try again...")
        break

    # Zmniejszenie rozmiaru klatki o 50%
    frame = cv2.resize(frame, None, fx=0.75, fy=0.75)

    # Wyświetlenie klatki
    cv2.imshow(f"IP: {ip_kamera}", frame)

    # Przerwanie pętli po naciśnięciu klawisza 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zwolnienie zasobów
cap.release()
cv2.destroyAllWindows()

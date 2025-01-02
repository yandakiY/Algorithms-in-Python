import cv2

# Charger l'image originale en niveaux de gris
image_originale = cv2.imread('profil.png', cv2.IMREAD_GRAYSCALE)

# Détecter les contours avec le filtre de Canny
contours = cv2.Canny(image_originale, 100, 200)

# Afficher les contours sous forme d'image dessinée
cv2.imshow('Image Dessinée', contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

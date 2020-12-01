# Pixels</h1>

### Description</h3>
Vous devez compter le nombre pixels NON noir.

Format: Hero{nombre}

### Solution</h3>

On dispose d'une image png qui contient des pixels de plusieurs couleurs. 
Le but est de compter tous les pixels noirs.

Evidemment cela ne se fait pas à la main; donc voici mon script ultra compact utilisant le module `cv2`.

```python
import cv2
image = cv2.imread("image.png", 0)
print(cv2.countNonZero(image))
```

Le flag est donc `Hero{41229}`

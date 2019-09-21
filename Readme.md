## Size of an image

```print(image.shape)```

## Black and White
``` cv2.imread('image', 0)```

## Color image
``` cv2.imread('image',3) ```

## Display image till user press any key
```
    cv2.imshow("Saijal Shakya", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

## Display image for 2000ms
```cv2.waitKey(2000)```

## Resize Image
```
    cv2.resize (image, (200,200))
```

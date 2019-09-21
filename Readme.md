- Python OpenCV stores image in numpy array :bowtie:


## Size of an image

```print(image.shape)```

## Black and White
``` cv2.imread('image', 0)```

## Color image
``` cv2.imread('image',3) ```

## Display image till user press any key
```
    cv2.imshow("Title of the window", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

## Display image for 2000ms
```cv2.waitKey(2000)```

## Resize Image
```
    cv2.resize (image, (200,200))
```

## Double the size of an image
```
    resize = cv2.resize(image, (int(image.shape[1]*2), int(image.shape[0]*2)))
```

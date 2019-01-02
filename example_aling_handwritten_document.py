# -*- coding: utf-8 -*-
from pyjaya.clasic import JayaClasic
from pyjaya.utils import FloatRange
import numpy as np
from PIL import Image
from skimage import feature


def function(solution):
    # opening the image and converting it to grayscale
    img = Image.open('static/handwritten_document.bmp').convert('L')
    a = img.rotate(solution[0])
    # converting a to an ndarray
    a = np.asarray(a)
    # performing Canny edge filter
    array = feature.canny(a, sigma=3.0).astype(int)
    image_canny = Image.fromarray(array, mode='L')
    cant = []
    for i in range(image_canny.size[1]):
        cant.append(sum(array[i, :]))
    cant.sort()
    return sum(cant[-200:])/200.0


def main():
    print("RUN: JayaClasic")
    listVars = [FloatRange(0.0, 180.0)]
    jc = JayaClasic(5, listVars, function)
    jc.toMaximize()
    result = jc.run(5)
    print(result)
    print("--------------------------------------------------------------")
    img = Image.open(
        'static/handwritten_document.bmp'
    ).convert('L').rotate(result['best_solution']).show()


if __name__ == '__main__':
    main()

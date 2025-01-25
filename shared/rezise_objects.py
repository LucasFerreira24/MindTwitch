from pygame import transform


def rezise_objects(image, screen_size: tuple, screen_reference: tuple, image_size: tuple = None):
    if image_size:
        object_width, object_height = image_size
    else:
        object_width, object_height = image.get_size()

    new_width =  int(object_width * screen_size[0] / screen_reference[0])
    new_heght =  int(object_height * screen_size[0] / screen_reference[0])

    return transform.scale(image, (new_width, new_heght))
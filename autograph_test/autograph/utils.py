import json

try:
    from PIL import Image, ImageDraw, ImageOps
except ImportError:
    import Image
    import ImageDraw
    import ImageOps

RESIZE = 5  # For SuperSampling
IMAGE_BORDER_SIZE = RESIZE
IMAGE_BORDER_FILL = "#A0A0A0"
SIGNATURE_WIDTH = 400
SIGNATURE_HEIGHT = 200


def redrawAutograph(json_string, height=SIGNATURE_HEIGHT, width=SIGNATURE_WIDTH, im_border_size=IMAGE_BORDER_SIZE,
                    im_border_fill=IMAGE_BORDER_FILL):
    """
    Generate Autograph based on lines.
    Anti-aliasing by using super-sampling technique.
    """
    try:
        drawing = json.loads(json_string)
    except Exception, e:
        raise Exception(e.args)
    else:
        im = Image.new("RGBA", (width*RESIZE, height*RESIZE), "#FFF")
        draw = ImageDraw.Draw(im)
        try:
            for line in drawing['lines']:
                draw.line(list(tuple([point[0]*RESIZE, point[1]*RESIZE]) for point in line),
                          fill="#000", width=RESIZE*2)
        except Exception, e:
            raise Exception(e.args)
        finally:
            del draw
        im = ImageOps.expand(im, border=im_border_size, fill=im_border_fill)
        im.thumbnail((width, height), Image.ANTIALIAS)
        return im
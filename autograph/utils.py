import json

try:
    from PIL import Image, ImageDraw, ImageOps
except ImportError:
    import Image
    import ImageDraw
    import ImageOps

RESIZE = 5  # For SuperSampling
IMAGE_FORMAT = "PNG"
IMAGE_BORDER_SIZE = RESIZE
IMAGE_BORDER_FILL = "#A0A0A0"
IMAGE_OUTPUT_DIR = ""
IMAGE_OUTPUT_NAME = "signature.png"
SIGNATURE_WIDTH = 400
SIGNATURE_HEIGHT = 200


def redrawSignature(json_string, height=SIGNATURE_HEIGHT, width=SIGNATURE_WIDTH, im_format=IMAGE_FORMAT,
                    im_output_dir=IMAGE_OUTPUT_DIR, im_output_name=IMAGE_OUTPUT_NAME,
                    im_border_size=IMAGE_BORDER_SIZE, im_border_fill=IMAGE_BORDER_FILL):
    """
    Generate Signature based on lines.
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
        im.save("%s%s" % (im_output_dir, im_output_name), im_format)
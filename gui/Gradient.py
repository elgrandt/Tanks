#Edicion 1
#Cree la funcion FillGradient que te colorea cualquier surface con colores degradados

import pygame

def FillGradient(Surface, Color1, Color2, Rect=None, Vertical=True, Forward=True):
    """fill a surface with a Color pattern
    Parameters:
    Color1 -> starting Color
    Color2 -> final Color
    Rect -> area to fill; default is surface's rect
    Vertical -> True=vertical; False=horizontal
    Forward -> True=forward; False=reverse
    """
    
    if Rect is None: Rect = Surface.get_rect()
    x1,x2 = Rect.left, Rect.right
    y1,y2 = Rect.top, Rect.bottom
    if Vertical: h = y2-y1
    else:        h = x2-x1
    if Forward: a, b = Color1, Color2
    else:       b, a = Color1, Color2
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pygame.draw.line
    if Vertical:
        for line in range(y1,y2):
            Color1 = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(Surface, Color1, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            Color1 = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(Surface, Color1, (col,y1), (col,y2))
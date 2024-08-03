"""
四角形の計算を行うモジュール
"""

def calc_rectangle_area(width, height):
    """
    四角形の面積を計算する

    Args:
        width : 幅
        height : 高さ

    Returns:
        面積

    """
    return width * height

def calc_rectangle_perimeter(width, height):
    """
    四角形の周囲の長さを計算する

    Args:
        width : 幅
        height : 高さ

    Returns:
        周囲の長さ

    """
    return 2 * (width + height)
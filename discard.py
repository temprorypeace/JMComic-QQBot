import os
import glob
import img2pdf
from PIL import Image

def images_to_pdf(image_folder, output_pdf, sort_by='name'):
    """
    将文件夹中的图片转换为PDF文件
    
    参数:
    image_folder: 图片文件夹路径
    output_pdf: 输出的PDF文件路径
    sort_by: 图片排序方式 ('name'按文件名, 'date'按修改时间)
    """
    # 获取图片文件列表
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.gif', '*.tiff']
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(image_folder, ext), recursive=True))
    
    if not image_files:
        print("未找到图片文件!")
        return
    
    # 根据选择的方式排序
    if sort_by == 'name':
        image_files.sort()
    elif sort_by == 'date':
        image_files.sort(key=os.path.getmtime)
    elif sort_by == 'natural':
        # 自然排序 (例如: img1, img2, ..., img10)
        import re
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        image_files.sort(key=alphanum_key)
    
    # 验证图片完整性
    valid_images = []
    for img_path in image_files:
        try:
            with Image.open(img_path) as img:
                img.verify()  # 验证图片是否完整
            valid_images.append(img_path)
            print(f"验证通过: {os.path.basename(img_path)}")
        except Exception as e:
            print(f"跳过损坏图片: {os.path.basename(img_path)} - {str(e)}")
    
    if not valid_images:
        print("没有有效的图片可转换!")
        return
    
    # 使用img2pdf创建PDF
    try:
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(valid_images))
        print(f"成功创建PDF: {output_pdf}")
        print(f"共转换 {len(valid_images)} 张图片")
        print(f"PDF文件大小: {os.path.getsize(output_pdf)/1024/1024:.2f} MB")
    except Exception as e:
        print(f"创建PDF失败: {str(e)}")
        # 尝试删除可能不完整的PDF文件
        if os.path.exists(output_pdf):
            os.remove(output_pdf)

if __name__ == "__main__":
    # 配置参数
    IMAGE_FOLDER = r"D:/Study/PythonAutomation/JMComic/images"  # 替换为你的图片文件夹路径
    OUTPUT_PDF = r"D:/Study/PythonAutomation/JMComic/output.pdf"  # 输出PDF文件路径
    SORT_METHOD = 'natural'  # 排序方式: 'name', 'date', 'natural'(自然排序)
    
    # 检查文件夹是否存在
    if not os.path.exists(IMAGE_FOLDER):
        print(f"错误: 图片文件夹不存在 - {IMAGE_FOLDER}")
    else:
        # 执行转换
        images_to_pdf(IMAGE_FOLDER, OUTPUT_PDF, SORT_METHOD)
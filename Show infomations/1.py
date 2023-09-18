from astropy.io import fits
import matplotlib.pyplot as plt


hdul = fits.open('your_file.fit')  # 打开一个.fits文件
header = hdul[0].header
print(header)
data = hdul[0].data
hdul.close()


print(image_data.shape)  # 打印数据的形状（行数和列数）
print(image_data)  # 打印数据的内容



plt.imshow(image_data, cmap='gray')  # 使用灰度颜色映射显示图像
plt.colorbar()  # 添加颜色条
plt.show()  # 显示图像

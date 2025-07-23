import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# ====== 画像読み込み ======
img = cv2.imread("data/70.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# reshape（各ピクセルをベクトルに）
pixel_data = img_rgb.reshape((-1, 3))

# ====== KMeansクラスタリング ======
n_colors = 15
kmeans = KMeans(n_clusters=n_colors, random_state=0, n_init="auto")
labels = kmeans.fit_predict(pixel_data)
palette = np.uint8(kmeans.cluster_centers_)

# ====== ラベルごとの代表色に置き換え ======
segmented_img = palette[labels].reshape(img_rgb.shape)

# ====== 結果表示 ======
# plt.figure(figsize=(12, 2))
# plt.imshow(segmented_img)
# plt.axis("off")
# plt.title(f"Color quantized to {n_colors} colors")
# plt.show()

# 保存
cv2.imwrite("tmp/70.png", cv2.cvtColor(segmented_img, cv2.COLOR_RGB2BGR))

import cv2
import numpy as np
import matplotlib.pyplot as plt

# def crop_and_save_image(image, x1, y1, x2, y2, output_path):
#     """
#     画像の指定された座標部分を切り取って保存する

#     Args:
#         image: OpenCV/numpy形式の画像データ
#         x1: 切り取り開始x座標
#         y1: 切り取り開始y座標 
#         x2: 切り取り終了x座標
#         y2: 切り取り終了y座標
#         output_path: 保存先のパス
#     """
#     cropped = image[y1:y2, x1:x2]
#     cv2.imwrite(output_path, cropped)


def read_image(file_path):
    # 画像読み込み
    img = cv2.imread(file_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb

def count_same_color_range(img):
    # ======= パラメータ =======
    line_count = 7  # 平均する行数（例：中心±3行）
    threshold = 100  # 色が「同じ」とみなすRGB距離（小さいほど厳しい）

    # ======= 行の平均色を計算 =======
    h, w, _ = img.shape
    center_y = h // 2
    half = line_count // 2
    row_range = img[center_y - half : center_y + half + 1, :, :]  # shape: (line_count, width, 3)
    row_avg = np.mean(row_range, axis=0).astype(np.uint8)  # shape: (width, 3)

    # ======= 連続色をカウント =======
    color_segments = []
    prev_color = tuple(row_avg[0])
    count = 1

    for pixel in row_avg[1:]:
        curr_color = tuple(pixel)
        dist = np.linalg.norm(np.array(curr_color) - np.array(prev_color))
        # print(f"dist: {dist}")
        # print(f"curr_color: {curr_color}")
        if dist < threshold:
            count += 1
        else:
            color_segments.append((prev_color, count))
            prev_color = curr_color
            count = 1

    # 最後の色も追加
    color_segments.append((prev_color, count))

    # ======= 結果表示 =======
    for i, (color, count) in enumerate(color_segments):
        print(f"{i+1}: 色RGB {color}, 長さ: {count} px")

    import matplotlib.patches as patches

    fig, ax = plt.subplots(figsize=(12, 1))
    x = 0
    for color, width in color_segments:
        rgb = tuple(np.array(color) / 255)
        rect = patches.Rectangle((x, 0), width, 1, facecolor=rgb)
        ax.add_patch(rect)
        x += width
    ax.set_xlim(0, w)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    print("Hello from read_voting_percentage_from_image!")
    # img = read_image('data/age_group_voting.png')
    img = read_image('tmp/70.png')
    # TODO: cut image for each age
    # TODO: sharpe each image
    # crop_and_save_image(img, 75, 19, 400, 22, 'tmp/test.png')
    count_same_color_range(img)
    # TODO: to json

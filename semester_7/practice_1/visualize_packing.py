import matplotlib.pyplot as plt


def visualize_disk_usage(
    best_ind: list[int], files: list[int], disk_capacity: int
) -> None:
    """
    Визуализирует загрузку каждого диска в лучшем решении.

    :param best_ind: список — назначение файлов на диски
    :param files: массив размеров файлов (в гигабайтах)
    :param disk_capacity: ёмкость диска (в гигабайтах)
    """
    disk_usage = {}
    for file_idx, disk in enumerate(best_ind):
        disk_usage[disk] = disk_usage.get(disk, 0) + files[file_idx]

    disk_ids = sorted(disk_usage.keys())
    used_space = [disk_usage[d] for d in disk_ids]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(disk_ids, used_space, color="skyblue", edgecolor="black")
    plt.axhline(
        disk_capacity, color="red", linestyle="--", linewidth=2, label="Ёмкость диска"
    )

    plt.title("Загрузка дисков в лучшем решении", fontsize=14)
    plt.xlabel("Номер диска", fontsize=12)
    plt.ylabel("Использовано, ГБ", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.7)

    for bar, val in zip(bars, used_space):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            val + 2,
            f"{val:.1f}",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.show()

import numpy as np
import matplotlib.pyplot as plt

def parallel_approximation(missile_pos, target_pos, target_vel, time_step):
    # 计算导弹和目标之间的向量
    target_to_missile = missile_pos - target_pos
    target_to_missile_normalized = target_to_missile / np.linalg.norm(target_to_missile)

    # 计算新的导弹位置
    missile_vel = target_vel + target_to_missile_normalized * np.linalg.norm(target_vel)
    new_missile_pos = missile_pos + missile_vel * time_step
    
    return new_missile_pos

# 初始化
missile_pos = np.array([0, 0], dtype=float)
target_pos = np.array([100, 100], dtype=float)
target_vel = np.array([1, -1], dtype=float)
time_step = 0.1

# 模拟
positions = [missile_pos.copy()]
for _ in range(100000):
    missile_pos = parallel_approximation(missile_pos, target_pos, target_vel, time_step)
    positions.append(missile_pos.copy())

# 绘图
positions = np.array(positions)
plt.plot(positions[:, 0], positions[:, 1], label='Missile Path')
plt.scatter(*target_pos, color='red', label='Target')
plt.title('Parallel Approximation')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.axis('equal')
plt.grid()
plt.show()
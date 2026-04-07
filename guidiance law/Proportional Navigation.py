import numpy as np
import matplotlib.pyplot as plt

def proportional_navigation(missile_pos, target_pos, target_vel, gain=3, time_step=0.1):
    # 计算目标与导弹之间的相对位置
    relative_pos = target_pos - missile_pos
    distance = np.linalg.norm(relative_pos)
    
    # 计算目标的预期位置
    target_future_pos = target_pos + target_vel * time_step
    
    # 计算所需的航向
    desired_heading = np.arctan2(target_future_pos[1] - missile_pos[1], target_future_pos[0] - missile_pos[0])
    
    # 更新导弹位置
    missile_vel = np.array([np.cos(desired_heading), np.sin(desired_heading)]) * 1  # 固定速度
    new_missile_pos = missile_pos + missile_vel * time_step
    
    return new_missile_pos

# 初始化
missile_pos = np.array([0, 0], dtype=float)
target_pos = np.array([100, 100], dtype=float)
target_vel = np.array([1, -1], dtype=float)

# 模拟
positions = [missile_pos.copy()]
for _ in range(10000):
    missile_pos = proportional_navigation(missile_pos, target_pos, target_vel)
    positions.append(missile_pos.copy())

# 绘图
positions = np.array(positions)
plt.plot(positions[:, 0], positions[:, 1], label='Missile Path')
plt.scatter(*target_pos, color='red', label='Target')
plt.title('Proportional Navigation')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.axis('equal')
plt.grid()
plt.show()
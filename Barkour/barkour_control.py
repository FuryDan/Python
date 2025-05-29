import mujoco
import numpy as np
import time
import math

# Инициализация модели и данных
model = mujoco.MjModel.from_xml_path('D:\VSCode\Barkour\barkour.xml')
data = mujoco.MjData(model)
viewer = mujoco.viewer.launch_passive(model, data)

# Параметры управления
PHASE_OFFSETS = [0, np.pi/2, np.pi, 3*np.pi/2]  # Для каждой ноги
SPEED = 2.5
JUMP_DURATION = 0.3

class GaitController:
    def __init__(self):
        self.phase = 0.0
        self.last_jump_time = 0.0
        
    def update(self, dt, base_pos):
        self.phase += dt * SPEED
        obstacle = self.detect_obstacle(base_pos)
        
        ctrl = np.zeros(model.nu)
        if obstacle == 'jump' and (time.time() - self.last_jump_time) > 1.0:
            ctrl = self.jump_action()
            self.last_jump_time = time.time()
        else:
            ctrl = self.trotting_gait(obstacle)
        
        return ctrl
    
    def trotting_gait(self, obstacle_type):
        angles = np.zeros(model.nu)
        amp_hip = np.deg2rad(50)
        amp_knee = np.deg2rad(70)
        
        # Параметры адаптации
        if obstacle_type == 'poles':
            amp_hip *= 1.3
            freq = 1.2
        elif obstacle_type == 'a_frame':
            amp_knee *= 1.4
            freq = 0.8
        else:
            freq = 1.0
        
        for i in range(4):
            phase = self.phase + PHASE_OFFSETS[i]
            
            # Тазобедренный сустав (синусоида)
            angles[i*2] = np.sin(phase * freq) * amp_hip
            
            # Коленный сустав (косинусоида со смещением)
            angles[i*2+1] = (np.cos(phase * freq) * amp_knee) - amp_knee/2
            
        return angles
    
    def jump_action(self):
        return np.array([-1.5, 3.0, -1.5, 3.0, -1.5, 3.0, -1.5, 3.0])
    
    def detect_obstacle(self, pos):
        x = pos[0]
        if x < -1.0: return 'start'
        elif -1.0 <= x < 0.5: return 'poles'
        elif 0.5 <= x < 1.8: return 'a_frame'
        elif 1.8 <= x < 2.5: return 'jump'
        else: return 'finish'

# Основной цикл
controller = GaitController()
start_time = time.time()

try:
    while True:
        dt = model.opt.timestep
        base_pos = data.body('base').xpos
        
        data.ctrl[:] = controller.update(dt, base_pos)
        
        mujoco.mj_step(model, data)
        viewer.sync()
        
        # Проверка завершения
        if base_pos[0] > 3.2:
            print("Course completed!")
            break
            
        time.sleep(0.001)

except KeyboardInterrupt:
    pass
finally:
    viewer.close()
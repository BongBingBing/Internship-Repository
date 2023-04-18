import numpy as np
import h5py
import matplotlib.pyplot as plt
import PeukerFile as PF

NUM_JOINTS = 6

def read_data(fname):
    hf = h5py.File(fname, 'r')
    print(list(hf.keys()))
    js = hf.get('joint_state_info')
    joint_pos = np.array(js.get('joint_positions'))
    joint_time = np.array(js.get('joint_time'))
    
    newPos,Inds = PF.DouglasPeuckerPoints2(joint_pos, num_points=100)
    
    time = joint_time[:, 0] + joint_time[:, 1] * (10.0**-9)
    js_fig, (ax1, ax2) = plt.subplots(2, 1)
    js_fig.suptitle('Joints')
    for i in range(NUM_JOINTS):
        ax1.plot(time, joint_pos[:, i], label= 'joint' + str(i))
    ax1.legend()
    for i in range(NUM_JOINTS):
        ax2.plot(time[Inds], newPos[:, i], label= 'joint' + str(i))
    ax2.legend()
        
    ax1.set_ylabel('positions (rad)')
    ax2.set_ylabel('positions (rad)')
    plt.show()
    
    


    
def main():
    filename = 'C:\\Users\\andyb\\OneDrive\\Área de Trabalho\\Internship\\VS Code\\recorded_demo_2023-03-15_15_18_02.h5'#raw_input('Enter the filename of the .h5 demo: ')
    read_data(filename)

if __name__ == '__main__':
  main()

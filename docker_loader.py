import os

os.system("docker load < /SLAM-Hive/slam_hive_algos/vins-fusion-mono-imu/image.tar")
while True:
    # image_check = client.images.get("slam-hive-algorithm:orb-slam3-ros-stereo-inertial")
    ret = os.popen("docker images | grep vins-fusion-mono-imu")
    if ret.read() != '':
        break
os.mkdir("/SLAM-Hive/slam_hive_algos/vins-fusion-mono-imu/docker_loader_finish")

print("------ successful ------")

### Build the VINS-Fusion by Dockerfile
Firstly, git clone the algorithm Dockerfile repository to your computer, then:
```
cd vins-fusion-stereo-imu
./install.sh
```
You can check whether the image is successfully built as follows:
```
docker images
```
you can see:
```
slam-hive-algorithm vins-fusion-stereo-imu [IMAGE ID] [CREATED] [SIZE]
```

For source code, we just change the places where used to save trajectory and mapping result files.

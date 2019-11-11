# OpenVino Headpose

以Openvino Sample中的pyrhon/Objectdetection 及Intel中兩個Pre-train model 進行實作
face-detection-retail-0005
head-pose-estimation-adas-0001

## 相關環境
* OpenVino 2019R3.1(2019R3 在製作Docker 上有點問題)
* Python 3.5.2
python 相關套件可參考 requirement.txt 輸入
```
pip install -r requirements.txt
```
即可安裝相關套件

## Doocker
可利用Dockerfile 進行Docker 環境的快速建制，輸入下列指令可build docker image。<Imagename> 為自定義的名字
```
docker build . -t <Imagename>
```

Dockerfile所建制的為使用CPU進行inference的環境
可輸入下面參數啟動 
* --device=/dev/video0 為要mount webcam路徑此為筆電預設，如筆電加裝修改後面數字即可
```
docker run -ti -d --device=/dev/video0  <Imagename> bash
```
```
docker exec -ti <container> bash
```

## inference
進入後要啟動環境
```
source /opt/intel/openvino/bin/setupvars.sh 
```
目前使用python直接參數後面會修正成ini
暫時由server傳送 angle 字串，收到後會回傳 angle_p_fc,angle_r_fc,angle_y_fc 這裡可以在討論
以 , 號區分
啟動指令如下,需注意由於我們使用模型需要cpu_extension lib 在openvino 的路徑如下 /opt/intel/openvino/inference_engine/lib/intel64 根據CPU選擇指令集, 在將路徑輸入在-l 之後
```
python3 HeadPose.py -m <face detection xml path> -m_hp <head pose xml path> -l /opt/intel/openvino/inference_engine/lib/intel64/libcpu_extension_avx2.so 
```


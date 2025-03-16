# xBD Building Semantic Segmentation

이 저장소는 **xBD** 데이터를 활용하여 건물(building)의 semantic segmentation을 수행하는 딥러닝 모델 구현 코드를 포함합니다.  
본 프로젝트는 데이터 전처리, 모델 학습, 평가 및 추론까지 전체 파이프라인을 제공합니다.

## 목차

- [xBD Building Semantic Segmentation](#xbd-building-semantic-segmentation)
  - [목차](#목차)
  - [프로젝트 개요](#프로젝트-개요)
  - [특징](#특징)
  - [요구사항](#요구사항)
  - [설치 방법](#설치-방법)
  - [데이터셋](#데이터셋)
  - [사용 방법](#사용-방법)
  - [결과](#결과)
  - [기여 방법](#기여-방법)
  - [라이선스](#라이선스)
  - [참고 자료](#참고-자료)

## 프로젝트 개요

이 프로젝트는 xBD 데이터셋을 활용하여 건물 영역을 정확하게 분할하는 semantic segmentation 모델을 구현합니다.  
모델은 딥러닝 기반 네트워크(Pytorch/TensorFlow 등)를 사용하며, 다양한 전처리 및 데이터 증강 기법을 적용하여 학습 성능을 향상시키고자 합니다.

## 특징

- **End-to-End Pipeline:** 데이터 전처리부터 모델 학습, 평가, 추론까지 전체 워크플로우 제공
- **모듈화 설계:** 각 모듈(데이터 로더, 모델, 학습 스크립트 등)이 독립적으로 구성되어 확장이 용이함
- **사용자 친화적 구성:** 구성 파일(config.yaml 등)을 통한 하이퍼파라미터 및 경로 설정
- **GPU 지원:** CUDA 지원을 통해 빠른 학습 환경 제공

## 요구사항

- Python 3.8 이상
- PyTorch (또는 사용 중인 딥러닝 프레임워크)
- CUDA (GPU 사용 시)
- 기타 Python 라이브러리: numpy, opencv-python, albumentations, matplotlib 등  
  *(자세한 내용은 `requirements.txt` 참조)*

## 설치 방법

1. 저장소 클론:
   ```bash
   git clone https://github.com/seunghyeokleeme/xBD_building_segmentation.git
   cd xBD_building_segmentation
   ```

2. 가상환경 생성 및 활성화 (선택 사항):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```

## 데이터셋

xBD 데이터셋을 사용합니다. 데이터셋은 다음과 같이 구성되어야 합니다:

```
datasets/
├── train/
│   ├── images/
│   └── targets/
├── hold/
│   ├── images/
│   └── targets/
└── test/
    └── images/
    └── targets/
```

- **다운로드:** 
  1. xBD 데이터셋은 [xBD 공식 페이지](https://xview2.org)에서 다운로드하여 재난 전 데이터셋만 활용합니다.


## 사용 방법

1. datasets 압축 해제 (1024 x 1024) 및 재난 전 데이터셋 활용
  ```bash
  python3 ./data_read.py
  python3 ./copy_pre_disatser_images.py
  ```

2. 1024 x 1024 -> 4개의 512 x 512 crop
  ```bash
  python3 ./crop.py --datasets_dir="./datasets" \
--save_dir="./datasets_512"
  ```

3. tensorboard 실행
  ```bash
  tensorboard --logdir='./log'
  ```

4. TRAIN
```bash
python3 ./train.py \
--lr 1e-3 --batch_size 12 --num_epoch 50 \
--data_dir "./datasets_512" \
--ckpt_dir "./checkpoint_v1" \
--log_dir "./log/exp1" \
--result_dir "./results_v1" \
--mode "train" \
--train_continue "off"
```

5. TEST
```bash
python3 ./train.py \
--lr 1e-3 --batch_size 12 --num_epoch 50 \
--data_dir "./datasets_512" \
--ckpt_dir "./checkpoint_v1" \
--log_dir "./log/exp1" \
--result_dir "./results_v1" \
--mode "test" \
--train_continue "off"
```

6. EVAL
```bash
python3 ./eval.py \
--result_dir "./results_v1" \
--out_fp "./localization_metrics.json"
```

7. INFERENCE
```bash
python3 ./inference.py \
--lr 1e-3 --batch_size 4 \
--data_dir "./inference_datasets" \
--ckpt_dir "./checkpoint" \
--result_dir "./inference_results"
```

## 결과

![실험 사진1](./results/result1.png)
![실험 사진2](./results/result2.png)

| Parameter         | 실험 1                | 실험 2 |
|-------------------|---------------------|--------|
| Image Size        | 512 x 512 4 crop    | -      |
| Learning Rate     | 1.0000e-03          | -      |
| Batch Size        | 12                  | -      |
| Number of Epoch   | 24                  | -      |
| Model             | U-net               | -      |
| Loss              | nn.BCEWithLogitsLoss| -      |
| Precision         | 0.8861              | -      |
| Recall            | 0.8263              | -      |
| F1 Score          | 0.8552              | -      |
| Accuracy          | 0.9834              | -      |
| IoU               | 0.7470              | -      |


## 기여 방법

1. 저장소를 Fork 합니다.
2. 새로운 브랜치를 생성 (`git checkout -b feature/YourFeature`).
3. 코드를 수정 및 개선합니다.
4. 변경사항을 커밋 (`git commit -m 'Add some feature'`).
5. 원격 저장소에 Push (`git push origin feature/YourFeature`).
6. Pull Request를 생성합니다.

## 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE) 하에 배포됩니다.

## 참고 자료

- [xBD 공식 페이지](https://xview2.org)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Unet: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597)

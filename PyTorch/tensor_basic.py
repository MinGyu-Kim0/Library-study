import torch

# 1. PyTorch의 구성요소
# torch: 메인 네임스페이스, 텐서 등의 다양한 수학 함수가 포함

# torch.autograd: 자동 미분 기능을 제공하는 라이브러리 

# torch.nn: 신경망 구축을 위한 데이터 구조나 레이어 등의 라이브러리

# torch.multiprocessing: 병렬처리 기능을 제공하는 라이브러리

# torch.iptim: SGD(Stochastic Gradient Descent)를 중심으로 한 파라미터 최적화 알고리즘 제공

# torch.utils: 데이터 조작 등 유티리티 기능 제공 

# torch.onnx: ONNX(Open Neural Netwrok Exchange), 서로 다른 프레임워크 간의 모델을 공유할 때 사용

# 2. Tensor(다차원)
# 데이터 표현을 위한 기본 구조로 텐서(tensor)를 사용

# 텐서는 데이터를 담기위한 컨테이너로서 일반적으로 수치형 데이터를 저장

# 넘파이의 ndarray와 유사

# GPU를 사용한 연산 가속 가능

# 3. 텐서 초기화와 데이터 타입 

# 초기화되지 않은 텐서
x = torch.empty(4, 2) # tensor([[1.0421e-25, 8.7721e-43],
print(x)              #         [0.0000e+00, 0.0000e+00],
                      #         [0.0000e+00, 0.0000e+00],
                      #         [0.0000e+00, 0.0000e+00]])

# 무작위로 초기화된 텐서
x = torch.rand(4, 2)# tensor([[0.2203, 0.2103],
print(x)            #         [0.9538, 0.4828],
                    #         [0.5633, 0.2542],
                    #         [0.4415, 0.8477]])

# 데이터 타입(dtype)이 long이고, 0으로 채워진 텐서
x = torch.zeros(4, 2, dtype=torch.long) # tensor([[1.0421e-25, 8.7721e-43],
print(x)                                #         [0, 0],
                                        #         [0, 0],
                                        #         [0, 0]])

# 사용자가 입력한 값으로 텐서 초기화
x = torch.tensor([3, 2.3]) # tensor([3.0000, 2.3000])
print(x)

# 2 x 4 크기, double 타입, 1로 채워진 텐서
x = x.new_ones(2, 4, dtype=torch.double) # tensor([[1., 1., 1., 1.],
print(x)                                 #         [1., 1., 1., 1.]], dtype=torch.float64)

# x와 같은 크기, float 타입, 무작위로 채워진 텐서
x = torch.randn_like(x, dtype=torch.float) # 기존의 텐서 모양과 같지만 데이터 타입은 float으로 지정 
print(x)                                   # tensor([[-1.6308,  0.4237, -1.4537, -0.6048],
                                                   # [ 0.0099,  0.5399,  0.3143, -0.1571]]) float형

# 텐서의 크기 계산
print(x.size()) # torch.Size([2, 4])
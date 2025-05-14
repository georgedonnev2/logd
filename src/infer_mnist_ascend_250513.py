#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
昇腾NPU版MNIST推理脚本 - 详细注释版
功能：加载训练好的模型进行手写数字识别
"""

import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image  # 图像处理库
import os

# ==================== 设备检测 ====================
try:
    import torch_npu
    NPU_AVAILABLE = True
except ImportError:
    NPU_AVAILABLE = False
    print("[警告] torch_npu模块未找到，将使用CPU推理")

device = torch.device("npu:0" if NPU_AVAILABLE else "cpu")
print(f"当前推理设备: {device}")

# ==================== 网络结构定义 ====================
# 注意：必须与训练时完全一致
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = torch.relu(x)
        x = self.conv2(x)
        x = torch.relu(x)
        x = torch.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = torch.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        return torch.log_softmax(x, dim=1)

# ==================== 模型加载函数 ====================
def load_model(model_path):
    """
    加载预训练模型
    参数:
        model_path: 模型文件路径
    返回:
        加载好的模型
    """
    # 初始化模型结构
    model = Net().to(device)
    
    # 加载模型参数（自动匹配设备）
    model.load_state_dict(
        torch.load(model_path, map_location=device)
    )
    
    # 设置为评估模式（关闭dropout等）
    model.eval()
    
    print(f"模型已从 {model_path} 加载")
    return model

# ==================== 图像预处理 ====================
def preprocess_image(image_path):
    """
    预处理输入图像
    参数:
        image_path: 图像文件路径
    返回:
        预处理后的4D tensor (1xCxHxW)
    """
    # 定义与训练时相同的预处理流程
    transform = transforms.Compose([
        transforms.Grayscale(),       # 转换为灰度图
        transforms.Resize((28, 28)),  # 调整大小
        transforms.ToTensor(),       # 转为Tensor并归一化到[0,1]
        transforms.Normalize((0.1307,), (0.3081,))  # 标准化
    ])
    
    try:
        # 打开图像文件
        img = Image.open(image_path)
        
        # 应用预处理并添加batch维度
        # unsqueeze(0)将3D tensor (CxHxW) 转为4D (1xCxHxW)
        return transform(img).unsqueeze(0).to(device)
    except Exception as e:
        print(f"图像加载失败: {str(e)}")
        return None

# ==================== 推理函数 ====================
def predict(model, image_tensor):
    """
    执行推理
    参数:
        model: 加载的模型
        image_tensor: 预处理后的图像tensor
    返回:
        预测结果 (0-9)
    """
    if image_tensor is None:
        return -1  # 错误代码
    
    with torch.no_grad():  # 关闭梯度计算以节省内存
        output = model(image_tensor)
        # 返回概率最大的类别
        return output.argmax(dim=1).item()

# ==================== 主函数 ====================
if __name__ == '__main__':
    # 初始化模型
    model = load_model('mnist_model_e5.pth')
    
    # 待预测图像路径
    test_image = 'test.png'
    
    # 检查图像是否存在
    if not os.path.exists(test_image):
        print(f"错误：测试图像 {test_image} 不存在")
        print("请准备一个28x28左右的手写数字图片，命名为test.png")
        exit(1)
    
    # 预处理图像
    print("\n正在预处理图像...")
    input_tensor = preprocess_image(test_image)
    
    if input_tensor is not None:
        # 执行推理
        print("正在进行推理...")
        prediction = predict(model, input_tensor)
        
        # 输出结果
        print("\n===== 识别结果 =====")
        print(f"预测数字: {prediction}")
        
        # 可视化结果
        digit_art = [
            " _ \n| |\n|_|",  # 0
            "   \n  |\n  |",   # 1
            " _ \n _|\n|_ ",   # 2
            " _ \n _|\n _|",   # 3
            "   \n|_|\n  |",   # 4
            " _ \n|_ \n _|",   # 5
            " _ \n|_ \n|_|",   # 6
            " _ \n  |\n  |",   # 7
            " _ \n|_|\n|_|",   # 8
            " _ \n|_|\n _|"    # 9
        ]
        
        if 0 <= prediction <= 9:
            print(f"\nASCII表示:\n{digit_art[prediction]}")
        else:
            print("无效预测结果")
    else:
        print("图像预处理失败，请检查输入图像")
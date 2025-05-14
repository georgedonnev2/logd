#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
昇腾NPU版MNIST训练脚本 - 详细注释版
功能：使用PyTorch+NPU训练手写数字识别模型
"""

# ==================== 导入模块 ====================
import os
import torch
import torch.nn as nn  # 神经网络基础模块
import torch.optim as optim  # 优化器模块
from torchvision import datasets, transforms  # 视觉数据集和预处理
from torch.utils.data import DataLoader  # 数据加载器
import time

# 尝试导入NPU支持库
try:
    import torch_npu  # 昇腾NPU的PyTorch适配库

    NPU_AVAILABLE = True
except ImportError:
    NPU_AVAILABLE = False
    print("[警告] torch_npu模块未找到，将回退到CPU训练")

# ==================== 设备配置 ====================
# 说明：自动检测NPU可用性，优先使用NPU
device = torch.device("npu:0" if NPU_AVAILABLE else "cpu")
print(f"当前训练设备: {device}")


# ==================== 神经网络定义 ====================
class Net(nn.Module):
    """
    MNIST分类网络结构
    网络架构：
    输入(1x28x28) -> Conv2d(32) -> ReLU -> Conv2d(64) -> ReLU
    -> MaxPool -> Dropout -> Flatten -> FC(128) -> ReLU -> Dropout -> FC(10)
    """

    def __init__(self):
        super(Net, self).__init__()
        # 第一卷积层：1个输入通道，32个输出通道，3x3卷积核，步长1
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1)
        # 第二卷积层：32输入通道，64输出通道
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1)
        # Dropout层：训练时随机丢弃神经元防止过拟合
        self.dropout1 = nn.Dropout2d(0.25)  # 25%丢弃率
        self.dropout2 = nn.Dropout2d(0.5)  # 50%丢弃率
        # 全连接层：9216=64*12*12（经过两次卷积和池化后的特征图大小）
        self.fc1 = nn.Linear(9216, 128)  # 9216->128维
        self.fc2 = nn.Linear(128, 10)  # 128->10类输出

    def forward(self, x):
        """前向传播过程"""
        # 卷积层1 + ReLU激活
        x = self.conv1(x)
        x = torch.relu(x)

        # 卷积层2 + ReLU激活
        x = self.conv2(x)
        x = torch.relu(x)

        # 最大池化层（2x2窗口）
        x = torch.max_pool2d(x, 2)

        # 随机丢弃部分神经元
        x = self.dropout1(x)

        # 展平多维特征图为一维向量
        x = torch.flatten(x, 1)

        # 全连接层 + ReLU激活
        x = self.fc1(x)
        x = torch.relu(x)

        # 最终丢弃层
        x = self.dropout2(x)

        # 输出层（10类对数概率）
        x = self.fc2(x)
        return torch.log_softmax(x, dim=1)  # 使用log_softmax便于计算NLLLoss


# ==================== 数据预处理 ====================
# MNIST标准化参数（全局均值0.1307，标准差0.3081）
transform = transforms.Compose(
    [
        transforms.ToTensor(),  # PIL图像转Tensor（0-255 -> 0-1）
        transforms.Normalize((0.1307,), (0.3081,)),  # 标准化： (x - mean) / std
    ]
)

# ==================== 数据加载 ====================
# 下载并加载MNIST训练集
train_dataset = datasets.MNIST(
    root="./data",  # 数据集存储路径
    train=True,  # 加载训练集
    download=True,  # 如果不存在则下载
    transform=transform,  # 应用定义的数据变换
)

# 创建数据加载器
train_loader = DataLoader(
    dataset=train_dataset,
    batch_size=64,  # 每批64张图像
    shuffle=True,  # 打乱数据顺序
    num_workers=4,  # 使用4个子进程加载数据
    pin_memory=True,  # 锁页内存，加速数据传输到GPU/NPU
)

# ==================== 模型初始化 ====================
model = Net().to(device)  # 实例化模型并移动到指定设备

# 损失函数：负对数似然损失（配合log_softmax输出）
criterion = nn.NLLLoss().to(device)

# 优化器：Adam优化器，学习率0.001
optimizer = optim.Adam(
    params=model.parameters(), lr=0.001, betas=(0.9, 0.999)  # 动量参数
)


# ==================== 训练函数 ====================
def train(epoch):
    """训练单个epoch"""
    model.train()  # 设置模型为训练模式（启用dropout等）

    start_train = time.perf_counter()

    for batch_idx, (data, target) in enumerate(train_loader):
        # 将数据移动到NPU/CPU
        data, target = data.to(device), target.to(device)

        # 梯度清零（防止梯度累积）
        optimizer.zero_grad()

        # 前向传播
        output = model(data)

        # 计算损失
        loss = criterion(output, target)

        # 反向传播
        loss.backward()

        # 参数更新
        optimizer.step()

        # 每100个batch打印训练进度
        # if batch_idx % 100 == 0:
        if batch_idx % 10 == 0:
            current_samples = batch_idx * len(data)
            total_samples = len(train_loader.dataset)
            progress = 100.0 * batch_idx / len(train_loader)

            end_train = time.perf_counter()

            print(
                f"Epoch: {epoch:2d} [{current_samples:6d}/{total_samples}"
                f" ({progress:.0f}%)]  Loss: {loss.item():.6f}"
                f" elapsed_time: {end_train - start_train:.4f} secs"
            )


# ==================== 主训练循环 ====================
if __name__ == "__main__":
    print("===== MNIST训练开始 =====")
    print(f"使用设备: {device}")
    print(f"训练样本数: {len(train_dataset)}")
    print(f"批量大小: {train_loader.batch_size}")
    print(f"总迭代次数: {len(train_loader)}次/epoch")

    # 训练10个epoch
    # for epoch in range(1, 11):

    start_train = time.perf_counter()

    for epoch in range(1, 1 + 5):
        train(epoch)

        end_train = time.perf_counter()
        print(f"total_elapsed_time: {end_train - start_train:.4f} 秒")  # 保留4位小数

    # 保存训练好的模型
    model_path = "mnist_model_e5.pth"
    torch.save(model.state_dict(), model_path)
    print(f"\n训练完成！模型已保存到 {model_path}")

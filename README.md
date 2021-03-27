# Video-Stitching-for-Linear-Camera-Arrays
复现Video Stitching for Linear Camera Arrays

# 下载数据集


# 训练网络

# CARLA for dataset generation
- download software

option1: download softwares for windows 10 from following link, and unzip them.
>链接：https://pan.baidu.com/s/1itOuasnq40xLMFZGJ4iT8Q 
提取码：j1un 

option2: download softwares for ubuntu 18.04 from following link, and unzip them.
>链接：https://pan.baidu.com/s/1ZnTj8bWMRo3tn9D3E2wqwQ 
提取码：31ys 

option3: find more resource from [CARLA](https://github.com/carla-simulator/carla/releases)

- install required packages

    ○ 建立虚拟环境(optional)
    
        § virtualenv  carla  --python==python37
        
    ○ 启动虚拟环境(optional)
    
        § carla\script\activate
        
    ○ 安装package
    
        § pip install --user pygame numpy -I https::/pypi.tuna.tsinghua.edu.cn/simple
        
- 下载项目代码
    
- 生成dataset

    ○ 启动虚拟环境
    
       § carla\script\activate 

    ○ 启动server
        
        § cd <directory of CARLA software>
        
        § CARLA_0.9.11\WindowsNoEditor\CarlaUE4.exe
        
    ○ 生成dataset
    
        § cd <code folder>/PythonAPI
        
        § python  .\generate_dataset.py #generate video dataset
        
     dataset can be found under folder, 'PythonAPI/output/'
        
        

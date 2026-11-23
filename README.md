# 二分查找 vs 哈希查找：可视化对比演示

> 《计算机与专业基础研讨》课程期末大作业 · 6 人小组协作
>
> **选题：二分查找 vs 哈希查找的可视化**

## 一、项目简介

本项目是一个桌面演示程序，用 Python + Tkinter 把两种经典查找算法的完整执行过程「放慢」并画出来，帮助初学者直观理解两者的差异：

- **二分查找**：在有序数组上反复折半，用 `lo / hi / mid` 三个指针展示区间收缩过程，直到命中或区间为空。
- **哈希查找**：用取模散列把关键字映射到桶里，用链地址法处理冲突，展示一次查找经过哪些槽位、比较了几次。

两侧并排运行，同一组数据、同一个目标值，**比较次数实时计数**，最后给出对比结论。

## 二、团队成员

| 姓名 | GitHub | 组内角色 | 负责模块 |
|---|---|---|---|
| 刘硕 | [@favor177](https://github.com/favor177) | 组长 / 项目经理 | `src/main.py`、README、PR 审查与合并 |
| 赵森森 | [@yuhuyuyuqun](https://github.com/yuhuyuyuqun) | 界面开发 | `src/ui_layout.py` |
| 侯果果 | [@houguoguo1106](https://github.com/houguoguo1106) | 算法 · 二分查找 | `src/algo_binary.py` |
| 刘红瑶 | [@liu666code](https://github.com/liu666code) | 算法 · 哈希查找 | `src/algo_hash.py` |
| 吴馨瑜 | [@WXY-codes-rgb](https://github.com/WXY-codes-rgb) | 可视化渲染 | `src/render.py` |
| 张谨洋 | [@pingjingdenaiwa](https://github.com/pingjingdenaiwa) | 测试与文档 | `tests/`、设计文档 |

## 三、安装与运行

（程序完成后补充，形如：）

```bash
git clone https://github.com/favor177/Binary-vs-Hash-Search.git
cd Binary-vs-Hash-Search
python src/main.py
```

## 四、目录结构

```
.
├── README.md                             本文件
├── Project_Requirements_and_Design.md    项目需求与设计文档
├── AI_Prompts_Log.md                     AI 辅助编程记录
├── LICENSE                               开源协议
├── docs/                                 补充文档与图片
│   ├── images/                           截图与示意图
│   ├── screenshots/                      冲突解决等过程证据
│   └── archive/                          文档历史版本
├── src/                                  源代码
│   ├── main.py                           入口与窗口装配
│   ├── ui_layout.py                      界面布局与控件
│   ├── algo_binary.py                    二分查找（输出步骤序列）
│   ├── algo_hash.py                      哈希查找（输出步骤序列）
│   └── render.py                         Canvas 绘制与动画
└── tests/                                测试用例
```

## 五、Git 协作记录

（项目进行中补充：分支列表、关键提交、冲突解决记录）

## 六、贡献者名单

| 成员 | 贡献内容 |
|---|---|
| 刘硕 | 项目初始化、接口契约、主程序装配、PR 审查与合并 |
| 赵森森 | 界面布局与控件 |
| 侯果果 | 二分查找算法与步骤记录 |
| 刘红瑶 | 哈希表、散列函数与冲突链 |
| 吴馨瑜 | Canvas 绘制与动画渲染 |
| 张谨洋 | 测试用例、需求文档、AI 交互记录整理 |

## 七、开源协议

本项目采用 MIT License，详见 [LICENSE](LICENSE)。
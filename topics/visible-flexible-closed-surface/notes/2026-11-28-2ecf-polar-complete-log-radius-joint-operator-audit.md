# 全 Cartesian 与 C2 log-radius 设计的完整 J/JT/正规跨块：实际小核检查

本条是一个独立的 **新 g 设计消费者**，不是原固定 g 链的改进结论，也不是已有 R165/R170/R183/R186 少参数径向设计定理的重述。目标生产空间保留当前 87×147=12789 个 Cartesian 自由度，再增添与同一 physical quintic 共用支撑的 87 个 log-radius 自由度。本条实际付款的是 120+8=128 列的小核；生产 12876 列和非线性接受数均仍为零。

## 1. 数学源、端迹与全部参数依赖

使用完整原 position source、原 a0 及源端口。令

    X(s,u;z,alpha) = X_source(s,u) + W_z(s,u),
    h(s;alpha) = sum_i B_i(s) alpha_i,
    a(s;alpha) = a0(s) exp(h(s;alpha)).

位置源和 W 均不依赖 alpha。B 是全 physical clamped quintic；在 c 和 S 每端省略最外三列。因此 h,h',h'' 端迹为零，a,a',a'' 与原端口严格相同（数学样条层面），在外部沿用原 a0。对任意有限实 alpha，a>0。内部重复节点重数至多三，h 为 C2。新目标的两个径向导数完整为

    a'  = exp(h) (a0' + a0 h'),
    a'' = exp(h) (a0'' + 2 a0' h' + a0 (h'' + h'^2)).

本消费者的全部 14 行是原 13 行加原 q=2 reciprocal-area 行。设 E=|Xs|²、F=Xs·Xu、G=|Xu|²，原 metric 原始向量 m=(E−1,sqrt(2)F/a,G/a²−1)。固定 z 时

    d_h m = (0,−m_1,−2(m_2+1)).

实际原 metric residual 带 quartic amplification；代码调用原 point.metric_apply(d_h m)，完整包含 amplification 的导数，再乘原固定 sqrt(weight)。绝不能只将 F/a 和 G/a² 的分母求导而忽略 amplification。

面积比 sigma=|Xs×Xu|/a。原 active q=2 residual 为 sqrt(weight) max((0.5/sigma)²−1,0)，故其 alpha 方向为

    d_h r_area = 2 sqrt(weight) (0.5/sigma)²  [active].

在 inactive 区为零；原 hinge 处继承原消费者的分支约定。本实核有340个实际 active 点，因而检查并非全 inactive 退化测试。

原 curvature 使用 X 的真实第一、第二基本形式，原 geometry 使用物理 X，故在固定 z 下均无 target a 依赖。所有物理节点、角节点、ds/S quadrature、两组各半权重、metric/curvature/geometry 常数、area strength=1、area threshold=.5、point guides、空间基和 recipe 常数均固定，不依赖 alpha。这里没有另外的 Codazzi 或 a'/a'' residual；导数 a',a'' 仍在目标定义和端迹中完整保存。增量 H2 damping 对 z 使用原频率块，对 alpha 使用同 physical k=0 径向 H2 块；它不作为绝对 h 或绝对位置场的目标罚项。

因此改变 alpha 确实改变 g。后续必须先选定并冻结最终 alpha，再在该单一新 g 上做加密/收敛论证；此处的设计下降不能作为原固定 g 收敛。

## 2. 实际小核，而非生产场替身

来自完整原205径点 prepared 的实际33个径点；取原128角每8个的16角、原192角每8个的24角；真实 source 六jet和 a0 三jet均来自原缓存，不做位置投影或另造模拟数据。小基为 radial J=8、Fourier M=2 的完整 XYZ 基：120位置列+8径向列，共128列。两组共有1320点，**每点完整14行，共18480行**。

z 为固定随机非零120参数，alpha_i=.017 sin(i+.31) 非零；报告完整保存 z、alpha、basis、节点、角节点、全部权重、point config 和 area 定义。小核检查只证该消费者实现与完整数学线性化一致，不把小核算成12789生产求解。

## 3. 实际独立对照

完整 JVP、JT 都使用物理系数（interleaved radial row 含147个XYZ通道和1个alpha通道）。正规矩阵保留原完整 XYZ 块、每个 Cartesian-alpha 跨块以及全部 alpha-alpha 块。小核显式逐列形成 J，形成 J^T J + lambda S (lambda=.003)，与实际带状 Cholesky 装配和解对比；生产实现不显式形成完整 J。

| 实际量 | 结果 |
|---|---:|
| XYZ JVP central FD (epsilon=1e−6) | 1.7959165914e−10 |
| alpha JVP central FD (epsilon=1e−6) | 2.6776129026e−10 |
| 联合 JVP central FD (epsilon=1e−6) | 8.6131799072e−11 |
| 三方向最大伴随相对差 | 1.8858183129e−15 |
| 完整正规矩阵相对 Frobenius 差 | 2.9169892260e−16 |
| Cartesian-alpha 跨块相对差 | 3.0134809889e−16 |
| alpha-alpha 块相对差 | 2.8709963342e−16 |
| 真实完整物理正规方程相对残差 | 6.7721890594e−16 |
| 带状解相对独立 dense solve 差 | 6.7104002969e−15 |

额外 epsilon=1e−7,1e−8 检查完整保存在报告；误差随舍入放大，没有将差分当严格区间证书。跨块 Frobenius 范数32.40645654、alpha 块17.42344262，均实际非零。

独立 OS 进程自然 exit=0，外部5.481924114秒，peak child RSS128160KiB；消费者内部5.055259257秒。非线性步数0、生产步数0、连续证界0。

## 4. 入口与身份

源码：`2ecf-polar-log-radius-operator.py`、`2ecf-polar-log-radius-local-check.py`。报告/日志/OS回执：`polar-log-radius-local-check.json`、`.log`、`-exit.json`（原始工作目录；不是把工作目录路径当公开输入）。

运行命令（W为本会话工作目录，S为仓库课题 scripts）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 -u "$W/2ecf-polar-log-radius-local-check.py" --scripts "$S" --prepared "$W/polar-c2-extended-prepared.json" --output "$W/polar-log-radius-local-check.json"
```

需先按已登记的完整前缀生产入口重建原 prepared/源缓存；本条没有声称此临时缓存永久存在。主仓库只需提交入口、数学定义、实跑命令及哈希记录，不提交大数组。

| 文件 | SHA256 |
|---|---|
| `2ecf-polar-log-radius-operator.py` | `f44226464ba3cad0f2c69f7bd9b7d86befa9a311d7ec268e0d81e7a19f36b17c` |
| `2ecf-polar-log-radius-local-check.py` | `bd3b9595bb9aeb30a59929a41fbc373281545fe94e96e1c12744c619ed8fe291` |
| `polar-log-radius-local-check.json` | `7f3d82a5cf943e54174e3076b83362c38ab1065b58a6aaf0e91713b8b84df5d5` |
| `polar-log-radius-local-check-exit.json` | `edf9d8eafa18840f2d9ac2649264e465f1de4a6e8165ccb54cd5370fd52bb324` |
| `polar-log-radius-local-check.log` | `05fea29c4c3faed40ca2d240df4cee6b7abace6742cb372e59d46517893751a9` |
| `polar-c2-extended-prepared.json` | `e8803bd9fd40c5e1edb298af42ed3b78585ebb02914e4aee26cf75a79daf8a03` |

本条未声称 whole closed、全时 reach、固定 g 加密或课题完成。G10 固定 g 支仍继续；新设计消费者的下一项是实际12876列全14行大场。

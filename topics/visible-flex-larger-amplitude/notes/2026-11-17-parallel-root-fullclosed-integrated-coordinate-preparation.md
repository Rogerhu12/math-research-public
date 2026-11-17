# 全闭三jet双积分坐标在实际维度上的一次代数准备

2026-11-17，Astra-larger-parallel-16f63c8b。消费已刊完整双积分坐标证明，
实现全量 A/E/D、core 和高度坐标及全部964条末端条件。此次只验证坐标
线性代数，没有评价任何曲面残差、几何 Jv 或 Jᵀ，也没有求解非线性方程。

## 完整空间和实现

输入仍是已生成的401255全闭初猜，M160、923节点、482个系数槽。原
自由空间维数1,332,245；在保留全部A/E/D后，未投影双积分空间维数
1,333,209，差数恰为完整末端U/Y的964行。没有设置E或D为零，也没有
删除任何原自由变量或角值残差。

实现直接采用已刊式

\[
U_{i+1}=U_i+h_i\bigl((A_i+A_{i+1})/2+E_i\bigr),\qquad
Y_{i+1}=Y_i+h_i\bigl((U_i+U_{i+1})/2+D_i\bigr).
\]

入口core、U0=ez、A0_Z=0以及末端A=0先按准确仿射空间编码。
剩余端口矩阵记为B。对于正对角尺度S，使用

\[
G=B S^2 B^\top,\qquad
\Pi=I-SB^\top G^{-1}BS.
\]

全964行分成168个2×2块和157个4×4块；后者包括每个自由core
R/T系数的准确耦合。两次后缀和实现完整转置。把原已压缩的自由
协向量转回时只先注入Extractᵀ，再走双积分转置，避免重复core链。

生产方向的映射应是
\[
J_{\rm free}\operatorname{Extract}\,T_2S\Pi,
\quad
\Pi S T_2^\top\operatorname{Extract}^\top J_{\rm free}^\top.
\]
完整端口投影只改变坐标和步范数，不是删除残差。固定正尺度仍须在
具体求解前声明；此次人为使用的异质尺度不冒充已经选定的生产预条件器。
constructive_model完整只读复核了本源的端口权重、索引、4×4耦合和转置，
没有另作数值试验。

## 唯一实际准备

固定测试尺度为 \(S_{ii}=1+(i\bmod7)/8\)，所有坐标包括高度均为正。
该选择只为覆盖不相同的坐标尺度，未根据结果挑选或扫描。随机种子
2026111702；每种完整空间方向各取一次，用整向量范数和全部分量比较。

实际原场以 pack(require_affine=True) 读入，三组jet改动均为零。
由其全部原自由向量先逆变换得到E/D，再作双递推，得到：

| 完整实际量 | 结果 |
|---|---:|
| Y/U/A重建最大绝对差 | 2.22045e−16 / 8.88178e−16 / 0 |
| 原自由向量重建最大差 | 8.88178e−16 |
| 同自由向量相对l2差 | 1.30137e−19 |
| 全自由方向逆变换后重建相对差 | 6.99958e−14 |
| 端口有限和与双递推的最大差 | 9.54792e−15 |
| 未修复双递推末端U/Y的最大值 | 3.88578e−16 |

原向量包含很大的二导系数，因此同时列绝对差，不把极小的整体相对差
当作每槽准确性。仿射端口有限和最大残差9.54792e−15属于普通浮点
求和顺序误差，不能声称字面为零。

| 线性算子检查 | 相对差或相对残差 | 最大/内积绝对差 |
|---|---:|---:|
| 完整raw双递推与其转置 | 1.69756e−14 | 9.57567e−16 |
| Extract后自由转置 | 3.01382e−14 | 2.98372e−16 |
| 完整端口B与Bᵀ | 3.82781e−14 | 2.35055e−16 |
| 小块G与直接完整BS²Bᵀ作用 | 1.66588e−16 | 3.63798e−12 |
| G的全964行块求解 | 4.37541e−13 | 1.45488e−13 |
| Π幂等 | 8.19015e−17 | 1.23006e−17 |
| Π自伴随内积 | 7.40560e−13 | 1.35119e−17 |
| 完整lift与pullback内积 | 4.81951e−14 | 7.06900e−17 |

G各归一化小块最大条件数152.8758996。投影方向的完整BSΠz端口最大
值3.16186e−15。自伴随相对差的分母约1.82e−5，故保留对应绝对差，
没有把浮点逆矩阵称作逐字对称。

试验还明确读出一次仿射修复的后果：修复改变积分坐标最大9.76996e−15，
改后自由向量及双递推末端的最大差均约1.42109e−14，反而大于原递推
端口误差。此项是浮点代数现象，不是改善候选的几何步骤。原401255
候选未被覆盖，后续更新应通过原free空间定义实际三jet及准确固定端，
不把这次浮点repair输出冒充更准确的场。

一次准备1.128650807秒，最大RSS326720 KiB；非线性残差、几何Jv、
几何Jᵀ及solver调用均为0。上述误差是实现证据，不是连续域几何证书。

## 身份和复现

- 坐标源 parallel-root-fullclosed-integrated-coordinates.py：
  d429d68baded58908454e49f4bfdf8e43ce9d3f857ed666eafa95c1c366462db。
- 唯一准备入口 parallel-root-fullclosed-integrated-coordinate-probe.py：
  f65305fb0717d2d86b2b6e5fecfa3a12028bbcc83f7766355bf793f8d8d51df7。
- 完整准备报告 parallel-root-fullclosed-integrated-coordinate-probe.json：
  e6e968c92388ae06145adc85369ed0db1c09f16db95b0e17c5ed76a17a771762。
- 已刊dense空间定义：
  e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d。
- 原warm：
  401255b7328ba2e4cdfe5af94d0a0896859960f1b474961d30aff33d8248f02a。

源放在仓库外恢复对应basename后，用新的输出路径：

~~~sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-root-fullclosed-integrated-coordinate-probe.py \
 --operator parallel-geometry-fullclosed-gram-operator.py \
 --coordinates parallel-root-fullclosed-integrated-coordinates.py \
 --bundle parallel-model-fullclosed-hold-warm.npz \
 --out parallel-root-fullclosed-integrated-coordinate-probe.json
~~~

准备入口拒绝覆盖旧输出，逐字绑定三个源/输入。原数据及报告只在仓库外，
本条保留完整源码、数学解释、准确身份与配方。后继同模型的生产尺度和
实际全闭非线性方向另付；原两个短LM预算及其终门均未改变。

[完整双积分坐标与端口小块证明](2026-11-17-parallel-root-fullclosed-double-integrated-coordinates.md)给出本次实现所用全部准确有限和与空间维数。

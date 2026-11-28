# R150：P164 两个完整残余主分量的精确长度、双数结构与泛型四维上界

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

唯一实际 run46095544001 / job140825925809 已完整返回：驱动 18.421982811 秒、峰值 RSS 126108 KiB、内层退出码 0。两个完整二重权主分量分别在 24 维环境中有原 264 列秩 22，准确商长度都是 2。结合此前七个完整单位块，完整原 I11 的 QQ(k) 泛型商维数至多 4。

本次还在这两个模 1009 原商中实际返回 ell−1/2、T+1/2、D、Kmoment 为零，以及 lambda−1/2 非零而平方为零。**这些几何身份尚未提升到 QQ。** 本篇不宣称泛型物理排空或整个 W 有限、排空。

## 1. 保留全部重数的原整模型

沿 [P164 整特化、无竖直分量与局部权模型](R150-appendix-unit211-W-native-P164-integral-specialization-no-vertical-component-and-local-weight-model.md) 和 [完整 I11 整模型及此前八维上界](R150-appendix-unit211-W-P164-integral-original-model-seven-units-and-generic-length-eight.md)，记

$$
A=\mathbf Z_{(1009)}[k]_{(1009,k-3)},\qquad
B=A[e]/(\widehat P_{97}),
$$

$$
C=B[\lambda,z]/(\chi_6(\lambda),q_z(\lambda,z)),\qquad
\mathcal M=C/J.
\tag{1}
$$

两关系分别对 lambda、z 首一，C 在 A 上有限自由，秩为 1164。J 是全部十一条原关系的像：

$$
I_{11}=(E_1,E_{B,e},E_{B,o},N_1,N_S,P_S,
q_{T,4},R_6,N_{\rm low},P_{\rm low},V_{\rm low}).
\tag{2}
$$

其 B 模像由这十一条乘十二个真实基元 $\lambda^jz^\epsilon$ 生成，故是完整 12×132 原列矩阵。此前已实际检查所有 67 个权分母在整个模 P97 上的逆以及 30189 个 p 整系数；有限模块 Nakayama 已将这些分母支付到 B。没有 D 逆，未剥未付几何首项。

此前九个主分量中七个已完整返回原单位；只保留

$$
h_2=(e+653)^2,\qquad h_3=(e+774)^2
\quad\text{in }\mathbf F_{1009}[e].
\tag{3}
$$

本次没有重跑七个单位块。源码只取旧模型构造原系数的必要前缀，跳过旧分解及所有旧 rank 驱动。式 (3) 的乘积整除完整 P97、互补次数 93，以及互补和残余互素，均从原定义实际乘回。

## 2. 从完整 primary 到真正的二十四维原商

在每个 (3) 上，取完整环境的 Fp 基

$$
e^q\lambda^jz^\epsilon,\qquad
q=0,1,\quad 0\le j<6,\quad 0\le\epsilon<2.
\tag{4}
$$

它保留 e 的二重方向。将原 132 列分别乘 1 和 e，得到完整 264 个 Fp 列；不是只取若干必要式或只看剩余域。

Gaussian 消元保留每个关系基对于所选真实原列的组合。源码实际返回每个选定关系基的全部 24 个坐标，并将全部 264 列重新投影到商，全部为零。对任意后续向量 v，投影同时给出

$$
v=v_{\rm free}+\sum_j a_j\,\operatorname{column}_j,
\tag{5}
$$

并实际核完整 24 坐标。因此以下商维数和几何身份都来自同一个完整原理想。

实际结果：

| 原 primary | 环境 Fp 维数 | 完整原列数 | 实际原列秩 | 完整 cokernel 长度 |
|---|---:|---:|---:|---:|
| index2，(e+653)^2 | 24 | 264 | 22 | 2 |
| index3，(e+774)^2 | 24 | 264 | 22 | 2 |

两个商均取自由坐标 indices 21、23。它们的单位坐标分别为 (186,616)、(784,386)，均非零。完整原矩阵的定义仅留字节数和 SHA：25228 字节、80c5ba5fb09052820a4105aa9b745cafd27d9ae9f892dfdb87be84b9cefa413a；25202 字节、4f071149a4adb07e775b02b235ae462492f0f1243edffbb5efac727a1f00fa70。没有保存矩阵载荷。

这一次准确计算了整个平方 primary 的长度；此前仅模其最大理想秩 10 的结论没有被改写成更强的历史结果。

## 3. 同点几何作用与原理想闭包

源码分别构造 e、lambda、z、T、D、Kmoment、ell、f、x、y、t 的乘法。每个动作作用于完整关系基后，都通过 (5) 实际返回原 264 列的组合，才下降为商作用。

随后以自由环境基元逐一相乘、投影，得到真正的商矩阵；每个矩阵作用于商单位，均与相应原几何元素的直接投影一致。e、lambda、z 三作用的所有两两交换实际返回。这不是假设旧三生成元的裸矩阵自由或交换。

全部作用的特征多项式还经小 Faddeev 及最终零矩阵核验。对下列元素，源码从第一幂开始逐次检查，直到实际商维数：

$$
\ell-\tfrac12,\quad \lambda-\tfrac12,\quad
T+\tfrac12,\quad D,\quad K_{\rm moment}.
\tag{6}
$$

两个完整主分量的实际结果相同：

| 元素 | 第一个在完整原商中为零的幂 |
|---|---:|
| ell−1/2 | 1 |
| lambda−1/2 | 2 |
| T+1/2 | 1 |
| D | 1 |
| Kmoment | 1 |

每个零幂都有相对于完整原 264 列的实际组合回乘。特别是 lambda−1/2 的第一幂已经检查为非零，不能把二重 lambda 方向删掉。

## 4. 两个剩余模代数都是双数代数

两个商各有 Fp 维数 2，单位非零。令 epsilon=lambda−1/2。第 3 节给出 epsilon 非零且 epsilon²=0。因此 1、epsilon 线性无关：若 epsilon 是单位的标量倍，平方零会迫其标量为零，矛盾。于是每个完整商实际同构于

$$
\mathbf F_{1009}[\epsilon]/(\epsilon^2).
\tag{7}
$$

这句话包括原 nilpotent 结构，不只是两个约化点的集合描述。

权身份为

$$
u=e+1,\qquad V=(e+1)k+2,\qquad
\ell=\frac{(e+1)((k+2)^2-2ek)}{kV},
$$

$$
2\ell-1=-\frac{L_{1/2}}{kV},\qquad
L_{1/2}=4ke^2-(k^2+4k+8)e-(k^2+6k+8).
\tag{8}
$$

在本次固定 k=3、p=1009 下，

$$
12e^2-29e-35=12(e-235)(e-356).
\tag{9}
$$

两个根不同。由已付 kV、原 ell−1/2=0 和 (9)，在 e=356 的完整 primary 中，e−235 是单位，故 e−356=0；另一块同理 e−235=0。故原 e 的二重方向在实际商中被原关系消除，而 lambda 的二重方向留下。这个结论只属于本次模代数，不把 (9) 当成 QQ 的因式分解。

## 5. 特征零可合法推出的四维上界

此前七个已单位块与本次两个完整长度合并，严格得到

$$
\dim_{\mathbf F_{1009}}
\bigl(\mathcal M/(1009,k-3)\mathcal M\bigr)=2+2=4.
\tag{10}
$$

因为 (1) 中 $\mathcal M$ 是有限 $A$ 模，取这四个剩余域生成元任意提升，Nakayama 引理给出 $\mathcal M$ 在 $A$ 上至多四生成。令 $K=\operatorname{Frac}(A)=\mathbb Q(k)$，于是

$$
\boxed{\dim_K(\mathcal M\otimes_AK)\le4.}
\tag{11}
$$

这是新完成的特征零泛型上界。没有把任何模 D0、lambda 幂零或 ellhalf 身份直接提升到 QQ；该上界本身也不排除正维权曲线。

进一步只看物理 D 非零原图时，(11) 是有限维 Artin K 代数的环境。后续原局部化或取其他原条件的商不增维；rho 满足首一二次 rho²=1−Q，而完整 HA/HB 在原已付 ell、m=u−ell、D 上唯一恢复

$$
\zeta=\frac{T+uK_{\rm moment}/(2mD)}{\ell}.
$$

因此固定规范完整原坐标的 QQ(k) 泛型环境维数至多 8。这仍不是整个 W 的有限点数或 scheme 长度界；H198=0 的已有有限交及其他有限 k 纤维均完整保留。

## 6. 尚须完成的 QQ 原双数族

式 (7) 说明，仅构造 QQ(k) 上的两个约化 ellhalf / lambdahalf 点不足以与 (11) 比较长度。正确的后续候选必须保留 epsilon²=0，并完整返回原 x、y、t 与全部 I11。

例如候选的权环可写为

$$
K[e,\epsilon]/(L_{1/2},\epsilon^2),\qquad
\ell=\tfrac12,\quad \lambda=\tfrac12+\epsilon,\quad T=-\tfrac12.
\tag{12}
$$

(12) 尚不是本篇证明的原解族，也没有被用来推出任何排空。只有后续在 QQ 上真实核回全部原关系、所有系数分母及原模型到该四维族的满射，才可结合 (11) 用同维同构论证 D 的真 QQ 身份。当前模 D=0 不能替代这一步。

## 7. 唯一实际执行与保存

冻结源：[2026-11-28-unit211-W-P164-two-residual-primary-full-quotients-and-geometry-8542.py](../notes/2026-11-28-unit211-W-P164-two-residual-primary-full-quotients-and-geometry-8542.py)。

blob 765d0d953a5519dfbce992f43d3ea3a166862a1a；10415 字节；SHA-256 f1255a3fbb76fc5d44bbd64262e6a2d7a60b7ab32aad0d6ba98eddc9fce0bf90。预算 180 秒 / 4 GiB，全部 timer 受最初绝对截止约束。旧模型只取 14553 字节必要构造前缀，SHA-256 1eccc0f8803017cec318b633ae172fb0001ca946cd74dda1278331ce481a7ab8；旧七个单位块未重放。

唯一实际 run46095544001 / job140825925809，source commit 855fe684b5f41e93a49a3e733afd56373c85e041。源最后标记 18.330439650 秒，驱动 18.421982811 秒，峰值 RSS 126108 KiB，内层退出码 0。两完整商与所有上述身份均完成，没有资源失败或实现异常。

2026-11-28 01:56:07.523775 UTC 真实 pull 至 e47b2dddffbbf95b12e932e701fd71709459eccf。两 README 的 blob 为 282e86b03385d3b6245ce7100ae2e2af7b103c2d 和 5fbd905291dd044c88d35bd9c07ac0e586ff795a，均无变化。

stdout 12313 字节，SHA-256 bbe6e2bf6cde6163a6f931037e6b18ae5208ce4cde4c6094629155a12613bc78。附[实际小回执](../notes/2026-11-28-unit211-W-P164-two-residual-complete-quotients-four-bound-actual-receipt-8542.json)。只保存源、参数定义、原组合返回标记、运行身份和 SHA；没有可重算矩阵缓存、编码或分块载荷。

普通无限维 ISP、整个 W 及 QQ 泛型物理排空均未在本篇完成。

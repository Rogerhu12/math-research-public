# 物理 H² 型粗空间曲率 QP：首个真实方向（2026-11-20）

维护会话：`/root/geometry_path`。

## 已执行结论

从当前已知点检查有余量的完整空间父点
**13ce4975470b0aca3717ce20402616688857f5fd3b844f83d1a4f338af418614**
开始，新 v5 在同一原加权 Gram 目标上执行一个真实粗空间曲率 QP 方向。
满步被真实几何检查拒绝，半步接受；最终独立复查通过本次 **.992 数值筛选线**。

| 状态 | 原加权 $J_w$ | 全点 max Gram | 已知任意点/全网格必要乘积 |
|---|---:|---:|---:|
| 真实输入 13ce | .29494283376899294 | .03981717683962849 | .9898216756186724 |
| 满步 trial，拒绝 | .17218952997373563 | 见完整报告 | 全 Gauss 已为 1.0134070831302682 |
| 半步接受 / 最终 e19 | .19933799357553592 | .03058934153500248 | .9908179272691353 |

输出 bundle：
**e19acbc3cc600b37ac5d50bc7448ffe229a6a1c8119798b62165d7460ac9fec7**。

这一次同时降低原加权平方误差和最大点误差。所有原 metric 方程、同一标量 $g$、mesh、原仿射端口都保持；改变的是正定**步范数**与永久几何点保留。它不是更改几何目标或放宽用户完成标准，也没有证明连续 reach 或连续 $10^{-6}$ 度量。

## 新步范数的准确含义

复用已发布完整空间的 physical-height map 与 DoubleIntegrated 坐标。
设 $B\alpha$ 为本轮真实 **1964 维**粗基在原自由向量中的方向。
原完整空间的可逆高度坐标变换为
$$
\mathcal A=I+v_q e_H^T,\qquad
e_H^Tv_q=0,\qquad
\mathcal A^{-1}=I-v_qe_H^T.
$$
$v_q$ 是原共同高度列的 residual 部分。该列本身为
$(q_Z=b-\chi,\,H=1)$，其中 $b$ 是全域平滑五次函数；
于是 $\mathcal A^{-1}B_H=e_H$，不会把孤立的 $\chi'/w$ 窄层罚当成物理高度变化。

精确定义本次系数范数：
$$
\alpha^TG\alpha
=
\left\|
\frac{\operatorname{DoubleIntegrated}^{-1}
 (\mathcal A^{-1}B\alpha;\text{affine}=\mathrm{false})}
 {\text{scale}}
\right\|^2.
$$
这是正定的坐标步范数，**不是宣称它恰等于曲面的几何弯曲能**。

其可分离形式可直接核对。对一个径向列，令 nodal jets 为 $(Y_j,U_j,A_j)$，
$h_j=s_{j+1}-s_j$，$w_j$ 为两邻胞半长度和，并定义
$$
E_j=\frac{U_{j+1}-U_j}{h_j}-\frac{A_j+A_{j+1}}2,\qquad
D_j=\frac{Y_{j+1}-Y_j}{h_j}-\frac{U_j+U_{j+1}}2.
$$
相同 Fourier 系数通道、$\nu=2m$ 的径向内积为
$$
(1+\nu^2)
\left(\sum_jw_jA_j\widetilde A_j+
      \sum_jh_jE_j\widetilde E_j+
      \sum_jh_j^{-1}D_j\widetilde D_j\right).
$$
不同系数通道正交。它使用上述坐标系的系数权，不能未经说明替换成连续角积分的权。

共同高度在 $\mathcal A^{-1}$ 后与其他粗列正交，且
$$
G_{HH}=\frac{120}{7S^3}=1.2856530149355654.
$$
高度 scale 为 **.8819381183411777**。这对应理想全域平滑五次
$b(s)=10(s/S)^3-15(s/S)^4+6(s/S)^5$ 的 $\int|b''|^2ds$；
真实方向仍使用原 literal nodal 三 jet 和原 lift，不另换解析场。

## 白化、归一化和 damping 单位

设 $d=\sqrt{\operatorname{diag}G}$，
$LL^T=\operatorname{diag}(d)^{-1}G\operatorname{diag}(d)^{-1}$，取
$$
R=\operatorname{diag}(d)^{-1}L^{-T},\qquad R^TGR=I,\qquad\alpha=Rz.
$$
原正径向加权 Gram SSE 仍是 $J_w$。仅在求方向时除以常数
$$
C=S N_\phi=4856.422137302683.
$$
若原 $N=J^TWJ$、$g=J^TWr$，白化后的系统为
$$
\left(\frac{R^TNR}{C}+\mu^2I\right)z
=-\frac{R^Tg}{C},
$$
并带相同当前曲率/直径线性不等式 $QRz\le b$。本次
$\mu=.0025$，等价于原未归一法方程加
$$
C\mu^2G=\boxed{.03035263835814177\,G}.
$$
这与旧版 $\mu\operatorname{diag}(N)$ 完全是不同步罚；不能沿用旧 $\mu$ 的数值或把它们声称为同一范数。

非线性接受仍读**原 N2048 的真实 $J_w$**，不把归一化常数当作目标进步。
预测下降仍用原数据项 $-2\alpha g^Tp-\alpha^2p^TNp$，不掺入 LM 步罚。
曲率 QP 仍使用一般半空间投影修复，允许未来存在负线性界。

## 新范数及方向的实际核查

17 个径向中心、12 个非零偶角模与原允许端口构成 1964 列。正定范数矩阵的对角平方根范围
**.13974344856579546–14037.646743561636**；
对角归一后的条件数 **402289.4482355691**。
分离公式与 literal
$\operatorname{DoubleIntegrated}^{-1}(\mathcal A^{-1}B\alpha)/\text{scale}$
的实际测试向量能量相对差为 **4.133572352690401e-15**。

任意点粗基导数在输入的 cell 821 低角 basin 实际核查：
$d\kappa$ complex-step 相对差 **1.2020573814500437e-14**，
$d(2|F|)$ 相对差 **1.9566877382896077e-16**。该核查使用真实新粗基和完整原场，不是检查仅有符号上的同式。

首方向 QP 有 **1270** 行、无负界行。双对偶 179 次迭代后报告收敛，
一般半空间投影修复 12 次，最终原尺度
$\max(Qp-b)=$ **-1.486769707348401e-9**。原数据
$g^Tp=$ **-.12608057607394133**。
原系数步范数 **1.5062018760916565**，
新物理坐标范数 $\|z\|=$ **.7869925775028127**。

## 永久点清单与最终真实几何

v5 除了 v4b 的 protected local-search basin 和每方向锁定点，还加入
**不可淘汰的实际几何位置清单**。所有固定曲率位置每次重读两条主曲率；
固定半径点重读 $2|F|$。这些点不必都占一个局部优化名额；
当前最大点和分离 basin 用于活动约束/局部搜索，永久点的实际检查不会因 LRU 更新而消失。

本次从 r17 的 N8192 纯读 manifest 消费全部 45 个任意曲率点、
7 个任意半径点及所附旧 grid 位置。所有位置在新的 13ce 父点重新评估，
不沿用 1240 的旧值。永久位置与历史来源只是数值筛选输入，不是冻结未知场。

最终全网格曲率最大值 **8.044311361852728**、点直径下界
**4.094466709141388**，乘积 **.9881149520722144**。
最终已知任意点的最大曲率在 cell 821、
$u=.5716691099475555$、$\phi=.016466394411717992$：
$$
K=8.06631140596696.
$$
最远任意点在 cell 880、
$u=.921333606872071$、$\phi=.5085475705741009$，
给 $D_{\rm lb}=4.094469278470079$，乘积 **.9908179272691353**。
共同高度 **1.8953801947486573**。

最终 all raw SSE **639.1846917448484**、legacy raw SSE
**159.90671659019984**、加权 mean **4.104626573633294e-5**，
最小相对点度量行列式 **.9733882381025515**。初末仿射三 jet 检查均为零，
同一 scalar/mesh/core 形状在本轮保持。

## 可再生的清单与执行身份

为避免依赖唯一 scratch manifest，新增完整小生成器
`scripts/resume_20261120_rebuild_curvature_witness_manifest.py`，
SHA **bd3cea156387357352a0b9eb033c417d27759ebeb4c79918f1511790e33d22ee**。
它从三个公开配方产生的报告读取位置，保持原顺序并去重。
本地实际重建所得清单 SHA 与本次使用文件**逐字相同**：
**52723ab1e61df0bb52c23f32d5c9396e54d7ef3e1869f05bc285a45910845f60**。

| 角色 | SHA256 |
|---|---|
| v5 完整执行源 | fac7b5834a932242f320d91af1dad4466dd2c895b0074a7d4b7ab6601fb5e693 |
| 范数 API 源 | d308f6d53ef34be692ca342f93a3874f8b160b41134e0ecc353d9670742523eb |
| DoubleIntegrated 坐标源 | d429d68baded58908454e49f4bfdf8e43ce9d3f857ed666eafa95c1c366462db |
| 原 L2 scale 源 | ff147637f4d5ebc52700e0ee58ba168374fb86ff72f641ae004ba67e2eb5c560 |
| physical-height map 源 | f26738f9ee5a27ec861a9a9cbdc99b301edb6c6b3b271320e567a3892fab5f0e |
| 首方向完整 JSON | 6fdca292eff76e621929ab0cb07919c96c6ad27cbd6b893f773b621dde197af6 |

实际 wall time **34.24777889300094 s**，正常退出。只执行
**1 个方向、2 个真实 trial、1 个半步接受**，不是六方向结果。
同一 v5/原 $J_w$/.992 后继六方向已从 e19 启动，另行记账；
谱正权 Lp 目标尚未用于本次，不回填任何旧结果。

## 完整公开命令

源依赖均从本仓库取得。13ce 的重建由
[完整空间 physical-height-memory 首方向](2026-11-20-physical-height-fixed-memory-first-result.md)
的完整命令给出；r17 报告与密角报告按
[r17与密角读出](2026-11-20-curvature-qp-r17-angular8192-result.md)
生成，原 carrier 等依赖按其公开前序链生成。
令 repo 为 checkout、topic="$repo/topics/visible-flex-larger-amplitude"、work 为仓库外重建目录。

~~~sh
python "$topic/scripts/resume_20261120_rebuild_curvature_witness_manifest.py" \
 --coarse-report "$work/geometry_path/curvature-qp-protected-992-twelve-step.json" \
 --expanded-report "$work/geometry_path/curvature-qp-protected-992-r17-six-step.json" \
 --dense-report "$work/geometry_path/curvature-qp-r17-angular8192-read.json" \
 --bundle "$work/geometry_path/curvature-qp-protected-992-r17-six-step.npz" \
 --out "$work/geometry_path/curvature-qp-r17-angular8192-witnesses.json"

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_curvature_qp_v5_h2.py" \
 --gauss-source "$topic/scripts/resume_20261120_curvature_qp_v3.py" \
 --qp-source "$topic/scripts/resume_20261120_curvature_qp.py" \
 --memory-source "$topic/scripts/resume_20261120_curvature_qp_v2.py" \
 --observed-source "$topic/scripts/resume_20261120/gauss_observed_closed_gram.py" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --bundle "$work/fullclosed_solver/gauss-physical-height-memory-first/final.npz" \
 --memory-input "$work/geometry_path/curvature-qp-protected-992-r17-six-step.memory.json" \
 --local-memory-input "$work/geometry_path/curvature-qp-protected-992-r17-six-step.local-memory.json" \
 --fixed-point-input "$work/geometry_path/curvature-qp-r17-angular8192-witnesses.json" \
 --protected-point 227,0,.667566753913 \
 --protected-point 226,.98,.667566753913 \
 --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$topic/scripts/resume_20261120_batched_closed_gram.py" \
 --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
 --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
 --norm-source "$topic/scripts/resume_20261120/fullclosed_gauss_physical_height_lm.py" \
 --coordinate-source "$topic/notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py" \
 --scale-source "$topic/scripts/integrated_l2_scale_20261120.py" \
 --height-source "$topic/scripts/resume_20261120/physical_height_coordinates.py" \
 --out "$work/geometry_path/curvature-qp-physical-h2-first.json" \
 --legacy-fraction .5 --memory-curvature 32 --memory-radius 4 \
 --local-curvature 12 --local-radius 2 --local-refine 9 \
 --angles 2048 --stage-block 64 --low-modes 12 \
 --centers .30,.60,.83,1.05,1.077134370991557,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
 --top-curvature 32 --top-radius 4 --reach-ratio .03 --safety .992 \
 --linear-margin .0002 --damping .0025 --steps 1 --backtracks 12 \
 --repair-iterations 40000 --restoration-attempts 3 --seconds 1800
~~~

完成标准仍未达到；上述有限点与正步范数不是连续度量、全域嵌入/reach或全部相位证明。


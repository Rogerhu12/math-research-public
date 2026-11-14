# 正帽真实无限角能量的 Wiener 快路

2026-11-12，接 R88 的物理 N4 边界、N16/P2 内部 trial/flux。
同一准确显式对称对象仍为 δ5；本方法没有重做 Newton，也不更换图。

## 1. 完整原函数界

令 \(B_j=\sum_k|\partial_r^j\beta_k|\)、
\(G_j=\sum_k|\partial_r^j\gamma_k|\)，所有系数先在准确共同样条
span 上作有向求值。真实角频率为 \(4k\)，故
\(\|\sum b_k\sin4k\theta\|_W\le\sum|b_k|\)。用非负系数的
Taylor majorants
\(B(t)=\sum_{j=0}^2B_jt^j/j!\)、\(G(t)=\sum_{j=0}^2G_jt^j/j!\)。
真实切向差的三个分量由
\[
 d_x=\cosh G\sinh B,\quad
 d_y=(\cosh G-1)+(\cosh B-1)+(\cosh G-1)(\cosh B-1),
 \quad d_z=\sinh G                                             \tag{1}
\]
逐系数控制。横向旋转原函数的完整 Fourier multiplier 行范数不超过
1；竖直零均值原函数在 \(4\mathbb Z\setminus\{0\}\) 上不超过 1/4。
因此单位原函数的每个横向分量由 \(d_h=d_x+d_y\) 控制，竖直由
\(d_z/4\) 控制。径向零模另有更强的界 \(d_y\)，并非线性的相位界。
这包含全部无限角模，没有采样误差或未付的 Fourier 截断。

沿用缩放恒等式 \(u=LP+P'\)、\(u'=L'P+LP'+P''\)。记对应 majorant
为 \(U_h,U_z,U'_h,U'_z\)，径向零模为 \(U_0,U'_0\)。真实归一 mean
能量修正 e,e′ 满足
\[
 |e|\le2|L|U_0+2U_h^2+U_z^2,
\]
\[
 |e'|\le2|L'|U_0+2|L|U'_0+2(2U_hU'_h+U_zU'_z).             \tag{2}
\]
将 (2) 放进已证明的准确 K 公式，再以同一真实 \(L,C,a,Z\) 和
完整切向/原函数界评价 \(D_2,M_2,W_2,H_1,F_z\)，得到 B 与 B⁻¹ 的
**所有实角**系数区间。所有实际分母与正曲率都必须通过；较大的
包裹只导致此快路拒绝，不被解释为真实系数失去正性。

`fourfold_phase_cap_wiener_box.py` 实现上述公式。其小角网格只因
共用 scalar 输入类而被初始化；实际能量证明没有调用任何角 FFT。

## 2. 准确有限 Gram 积分

在一个真实共同 span 与一个 FE 单元的交上，选准确常数矩阵中心
\(B_c=\left(\begin{smallmatrix}a_c&b_c\\b_c&c_c\end{smallmatrix}\right)\)。
设真实系数离中心的完整区间半径为 \(\epsilon_a,\epsilon_b,
\epsilon_c\)。对全部 10 个输入列，同时取 \(X=V_r,Y=V_\theta\)
或 dual 的 \(X=p,Y=q\)。完整 Fourier Parseval 给有限 Gram 矩阵
\[
 I_{XX}=\int X^*X\,dr,\quad
 I_{XY}=\int(X^*Y+Y^*X)\,dr,\quad I_{YY}=\int Y^*Y\,dr.
\]
P2 的每个 integrand 径向 degree 至多 4，真实 GL3 对它准确；根/权
不确定性、所有复矩阵运算和所选 dyadic 中心仍有向支付。没有把浮点
Gauss 节点或普通 BLAS 结果当准确积分。令 \(J_X=\operatorname{tr}I_{XX}\)、
\(J_Y=\operatorname{tr}I_{YY}\)，则整个能量矩阵的算子范数费用为
\[
 \epsilon_aJ_X+2\epsilon_b\sqrt{J_XJ_Y}+\epsilon_cJ_Y.       \tag{3}
\]
这是全输入列的 Frobenius/Parseval 上界，不仅是某一列的能量误差。
式 (3) 同时支付真实无限角扰动和整个实径向区间的系数变化。

在 r≈1.3025、1.8025 的完整宽约 0.0025 span 上，实际最大主/dual
误差密度分别小于 \(2.337\,10^{-5}\)、\(5.272\,10^{-6}\)。r≈0.8025
给 \(5.338\,10^{-4}\)，故没有通过首次 \(10^{-4}\) 探针门；原失败
报告保留。后续外 body cover 以 \(10^{-3}\) 为逐段接受上限，最终费用
相加使用各段实际报告值。内侧误差不能因此转授。

## 3. 自然 graft 与真无限尾已经实际完成

`fourfold_phase_cap_graft_tail_energy.py` 直接按 R71/R74 相同公式，从
δ5 在 r=3 的准确四阶入口构造自然权 C4 graft；其半径、归一相位、
高度积分的定义都未更换。高度用准确正斜率积分的包络，不需要把一个
浮点高度积分视为真值。同一 frozen graft 的 origin/direction、长度
1/8、构造源码与真尾参数包含都被核实。

真实区间 \([3,25/8]\) 已由 37 个闭区间完整覆盖。全部角模依 (1)、
(2) 支付，主与 dual 能量矩阵的累计算子误差分别小于
\[
 8.074\,10^{-7},\qquad8.072\,10^{-7}.                     \tag{4}
\]
CPU 8.69 秒，实际 wall 90.86 秒。报告在
`data/cap_physical4_energy/graft_and_true_tail.json.gz`。

右端非零模另用 R74 的实际 \(\gamma_{4|k|}\) 和准确有向倒数积分
\[
 U_R^*\Gamma_HU_R,\qquad p_R^*\Gamma_H^{-1}p_R.
\]
N16 的全部保存模均保留；这两项各自包含参数盒、Γ 误差、舍入和
选中心的费用，均小于 \(9.29\,10^{-37}\)。regular 均值作为单独
\(\xi,\lambda\) 迹保留，未赋予虚构 \(\gamma_0\)。同一报告保存
完整准确有限边界矩阵 \(T(g,h)=L(j_g,h)\)，供 R88 的 Loewner
上下界及中心公式使用。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_graft_tail_energy.py \
  --out data/cap_physical4_energy/graft_and_true_tail.json.gz
```

## 4. 有界缓存与连续 body 重放

每个真实 common span 都单独处理，不能把近重合但不相同的二进制
knots 合并。每换 span 就释放旧 raw/scalar germ 缓存；只在内存保留
当前 FE 的矩阵。每个完成 FE 写独立 gzip 报告，再用小 manifest
登记其 SHA。恢复时比对实际对象、trial NPZ、源码/依赖、准确区间。

第一 runner 实际完成 FE20、21，即约 [0.8,0.9] 的准确 dyadic 区间。
随后在下一单元开头主动 Ctrl-C，退出 130；保留旧 partial，不称其
余区间已完成。第二 runner 从 FE22 另目录续算，改变的只是标量
多项式乘法的实现：逐标量双循环改成按同一 i 顺序的有向整行更新。
每个目标系数的加法次序不变，未使用未支付的浮点 convolution。
一个实际共同 span 上所有多项式端点逐位相等，完整 form 球也相同；
CPU set_cell 从 0.285 秒减至 0.089 秒。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_wiener_cover.py \
  --start-element 20 --stop-element 22 --error-per-length 1/1000 \
  --out-dir data/cap_physical4_energy/body_wiener_0800_3000

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_wiener_cover_v2.py \
  --start-element 22 --stop-element 64 --error-per-length 1/1000 \
  --out-dir data/cap_physical4_energy/body_wiener_0900_3000_vector
```

第一条以已经完成的相同单元报告作严格身份检查后恢复，不会将旧
覆盖到 FE64 的未完成 manifest 当证书。第二条当前仍在持续运行；
完成范围只由每个实际 FE 报告决定。自然 graft 的完成也不意味着
body、完整 cap Schur 或最终无限维逆已经完成。

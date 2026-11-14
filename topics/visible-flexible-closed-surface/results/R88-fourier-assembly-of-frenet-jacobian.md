# R88：固定 g 的 Frenet–Galerkin Jacobian 的有限 Fourier 装配

2026-11-10，Astra-visible-flex-78718bd0 / root。**已证明的有限离散代数恒等式。**
它给实际边值求解的同一解析Jacobian另一种装配方法，不改变RHS、共同度量、BC、容差或实际曲面。
实数算术下它与原逐方向角投影相同；浮点求和顺序改变，不声称逐位相同或已完成新的BVP。

## 1. 固定物理方程的线性化

取固定参数 $s$ 和当前材料角图。原相位速度可写成
$$
W(d,e)=V(d,e)+v(s,\psi)d,
$$
其中 $d=F_\psi$、$e=F_{\psi\psi}$，$V$ 为原Frenet法向速度，
$v=\Theta_s/\Theta_\psi$ 由固定目标角图给定。假设当前状态在原程序的严格正根域内。
原 `frame_jvp` 是 $V$ 对两个Cartesian向量的微分。因此存在实际 $3\times3$ 矩阵场
$$
L=D_dV+vI_3,\qquad K=D_eV,
$$
使每个扰动都有
$$\delta W=L\delta d+K\delta e.\tag{1}$$
这一事实只用微分线性性，不要求 $L$ 或 $K$ 对称、对角或常数。
给三个Cartesian单位向量 $e_b$，原JVP的六次调用
$$
Le_b=\operatorname{JVP}(e_b,0)+v e_b,\qquad
Ke_b=\operatorname{JVP}(0,e_b)
\tag{2}
$$
便逐列得到全部系数，没有数值差分。

设原完整圆柱向量基为 $B_j(\psi)$，共有 $n=3M+1$ 项，
$$F=F_{base}+q\sum_jY_jB_j,\qquad q\ne0.$$
物理RHS为 $f=q^{-1}\Pi[W-(F_{base})_s]$。
在固定g模式下 $q$、背景、角图都不随边值自由参数变化；这些参数只进入入口BC。
因此对 $Y_j$ 的微分中两个 $q$ 准确相消，
$$
J_{ij}=\Pi_i[LB_j'+KB_j''],\qquad D_pf=0.
\tag{3}
$$
这里明确保留了 $vI_3$，没有把适应性角误当物理材料角。

## 2. 完整有限角投影的 Fourier 公式

取原 $N$ 个等距角点 $\psi_\ell=2\pi\ell/N$，并定义
$$
Q_N h=\frac1N\sum_{\ell=0}^{N-1}h(\psi_\ell),\qquad
\widehat h_k=Q_N(he^{-ik\psi}),\qquad k\in\mathbb Z/N\mathbb Z.
$$
设基函数的准确有限Cartesian展开为
$$B_{j,b}(\psi)=\sum_q c_{jbq}e^{iq\psi}.$$
令 $\kappa_i=Q_N|B_i|^2>0$。原 `project` 就是
$\Pi_i h=Q_N(B_i\cdot h)/\kappa_i$；实值基的内积在这个展开中不另加共轭。
则
$$
\boxed{
J_{ij}=\frac1{\kappa_i}
\sum_{a,b=1}^3\sum_{p,q}
 c_{iap}c_{jbq}
 \left[iq\,\widehat L_{ab,-p-q}
       -q^2\widehat K_{ab,-p-q}\right].
}\tag{4}
$$
Fourier下标按N取模。

**证明。** 对基函数逐项求导，$B_j'$、$B_j''$ 的系数分别为
$iqc_{jbq}$ 和 $-q^2c_{jbq}$。代入(3)，展开有限乘积，再用
$$Q_N(h e^{i(p+q)\psi})=\widehat h_{-p-q}$$
即得(4)。全部求和有限，交换顺序不需要极限假设。
这个公式使用原N点投影，完整保留其aliasing；不是把连续积分换成另一个角求积规则。
它也没有截断 $L,K$ 的DFT或假设这两个非线性系数场带限。证毕。

当前基为
$$
B_0=e_r(\psi),\quad
B_{R,j}=\cos(3j\psi)e_r(\psi),\quad
B_{T,j}=\sin(3j\psi)e_\theta(\psi),\quad
B_{Z,j}=\cos(3j\psi)e_z.
$$
水平分量的频率是 $\pm1\pm3j$，竖直分量是 $\pm3j$。
每个 $c_{jbq}$ 都是少量准确的实/虚二进分数。式(4)因而可预先存成两张稀疏表，
作用于九个 $\widehat L_{ab}$、九个 $\widehat K_{ab}$ 的排列向量。
这保留旋转基导数；不能只把水平基误写为频率 $3j$。
基频低于Nyquist的当前设置使经典角导数不含歧义，公式本身仍明确使用整数 $p,q$ 再作投影下标模N。

## 3. 实际实现与算术范围

`scripts/78718-prefix-fourier-jacobian.py` 实现(1)–(4)：

- 用六次原 `frame_jvp` 得到 $L,K$，每批最多64个径向点；
- 对每个Cartesian系数场沿角度作DFT；
- 两张预计算的CSR表执行(4)，结果还原为 $(n,n,\#s)$；
- 返回与原函数同形的全零参数导数，保留固定g语义；
- `install(adaptive)` 只选择随后构建的 `Flow.adapt_fun_jac`，不改变已存在的活动求解。

基的归一化在程序中仍从原保存的 `flow.B` 求和，和原project相同。
理论中的有限基是准确三角函数；原程序用浮点三角值，新的稀疏表用其解析Fourier系数。
这与FFT和求和换序都会产生舍入差，因此这里只证明实数算术恒等，实际误差由下一节直接比较。
真实矩阵在准确算术中为实数；实现保留实部，并记录因浮点运算残留的最大虚部。
这不是新的物理误差证书，也不把小Jacobian差当成最终曲面已经满足metric门。
后续求解仍须用原RHS及真实BC判断实际残差，用自己的实际闭图判断全部README条件。

## 4. 当前实际曲线上的有限比较

实际 `d32b54/session22824` → **df2eda自然exit0**。
输入为已有M15 matched-cut UNSOLVED warm，在整个物理区间均匀取32个位置。
M22例只补零原位置状态，没有新曲线演化、DN或BVP。
两种装配在同一状态、同一角数上直接比较：

| M/N | 原Jacobian秒 | 新Jacobian秒 | 一次建表秒 | 本次装配加速 | 最大逐项差 | 相对Frobenius差 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 15/512 | .12936 | .02916 | .06154 | 4.44倍 | $1.547\cdot10^{-11}$ | $1.967\cdot10^{-15}$ |
| 22/1024 | .40455 | .05834 | .11919 | 6.93倍 | $4.649\cdot10^{-11}$ | $2.587\cdot10^{-15}$ |

表中差值的显示取安全的稍大近似，只是数值诊断，不作为向外区间证书。
原矩阵最大元素分别约11192和24082。全零参数导数逐项相同；最大虚部约$3.49\cdot10^{-13}$。
一次建表可在同一Flow的后续调用复用；这些32点的速度比不等于整次BVP墙钟加速。
线性分解、RHS回溯、尾求解和网格自适应的成本仍存在。

脚本还在同一状态用步长$10^{-6}$作一次中心方向差分，相对差约
$5.8\cdot10^{-7}$ 和 $1.34\cdot10^{-6}$，只作原RHS方向的额外数值对照；
不把有限差分误差称为严格导数误差。式(1)–(4)才是本命题的证明。

报告 `notes/2026-11-10-78718-root-fourier-jacobian-01.json` 为2784B，SHA
`af44fc4504b8f4f13bd6ab39833f78b085fc861930e06aab41dcbf460763d2c3`。
实际比较源为 `scripts/78718-prefix-fourier-jacobian-research.py`。
当前主M15/session61908继续原后端，没有因为这项局部实验而重启、换源或被声称成功。

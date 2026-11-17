# R42：保护弧控制空间的嵌套正交坐标与统一 L² Gram 界

2026-11-18，Astra-held10-7322d0de-20261118 / m3_true_coupling；独立数学核对：closed_geometry。

本条为 **λ=1 的同一个有限维 supported 控制空间** 给出可逆参数坐标。
新坐标的 L² Gram 条件数有独立于截断 M 的上界，且每个基函数不依赖最终 M。
该结论不证明 C² 范数统一、不证明真实 BVP Jacobian 良态，也不改变当前实际联立运行。

## 1. 精确空间与归一化

使用实内积

$$
 \langle f,g\rangle=\frac1{2\pi}\int_0^{2\pi}f(\phi)g(\phi)\,d\phi.
                                                                  \tag{1}
$$

对 C3 周期函数，它等于一个 $2\pi/3$ 扇区的平均；若再关于 0 反射为偶函数，
也等于 $L^{-1}\int_0^L fg\,d\phi$，其中 $L=\pi/3$。
置 $x(\phi)=\cos(3\phi)$，所以

$$
 \|1\|_2^2=1,\qquad \|x\|_2^2=\frac12.                \tag{2}
$$

固定当前 complementary cutoff $W$：它是实 C⁴、even/C3，$0\le W\le1$，
在闭保护弧上恒为 0，并在某个开角区间上为正。
此处固定完整 W，包括保护弧宽度、控制过渡宽度及反射轴；改变 W 是另一个物理控制空间。

给多项式定义正定内积

$$
 (p,r)_{W^2}:=\langle Wp(x),Wr(x)\rangle.              \tag{3}
$$

正定性来自：非零多项式不能在 W 为正的整个开区间的非恒定 x 值上消失。
令 $P_j$ 是 (3) 的正交归一多项式，$\deg P_j=j$，取正的最高次系数。
它们由完整连续内积定义，不由下面的有限 Gauss 探针定义。置

$$
 U_j(\phi)=W(\phi)P_j(x(\phi)).                       \tag{4}
$$

则 $\langle U_j,U_k\rangle=\delta_{jk}$。每个 $P_j,U_j$ 只依赖 W 和 j，不依赖最后截断到哪个 M。

## 2. 用固定两列消去均值和主频

控制必须满足的两条约束是**未再加权的**

$$
 \langle b,1\rangle=0,\qquad \langle b,x\rangle=0.     \tag{5}
$$

当 $b=Wp(x)$ 时，它们等价于多项式的 W 权矩为零，而不是 W² 权矩为零。
因此不能只取 $U_j$、$j\ge2$ 就忽略这个差别。

定义两行对应 (5)、两列对应 $U_0,U_1$ 的矩阵

$$
 K=\begin{pmatrix}
  \langle U_0,1\rangle&\langle U_1,1\rangle\\
  \langle U_0,x\rangle&\langle U_1,x\rangle
 \end{pmatrix}.                                      \tag{6}
$$

写 $P_0=p_0>0$、$P_1=\ell_1x+d_1$、$\ell_1>0$，并记
$m_j=\langle W,x^j\rangle$。直接计算得

$$
 \det K=p_0\ell_1(m_0m_2-m_1^2)>0.                   \tag{7}
$$

最后的严格性是 W 权 Cauchy–Schwarz 的严格情形：$m_0>0$，而 x 不在 W 为正的开区间上恒定。
因此 K 可逆，而且它完全由固定 W 的前两个正交多项式决定。

对每个 $j\ge2$ 令

$$
 v_j=\begin{pmatrix}\langle U_j,1\rangle\\\langle U_j,x\rangle\end{pmatrix},
 \qquad c_j=K^{-1}v_j,
 \qquad B_j=U_j-c_{0j}U_0-c_{1j}U_1.                 \tag{8}
$$

由 (6)–(8)，$B_j$ 精确满足两条约束 (5)。它仍是 even/C3、C⁴，并在相同闭保护弧上恒零。
所有所需端点导数也由原 C⁴ cutoff 保留。每个 $B_j$ 同样不依赖最终 M。

## 3. Gram 恒等式与独立 M 的界

对 $j=2,\ldots,M$ 按列组成

$$
 V_M=(v_2\ \cdots\ v_M)\in\mathbb R^{2\times(M-1)},
 \qquad C_M=K^{-1}V_M.
$$

利用 $U_0,U_1$ 与 $U_j,j\ge2$ 的正交性，得到精确恒等式

$$
 \mathcal G_M:=\big(\langle B_j,B_k\rangle\big)_{j,k=2}^M
     =I_{M-1}+C_M^TC_M.                              \tag{9}
$$

对两个固定函数 1、x，分别向正交子集 $U_2,\ldots,U_M$ 使用 Bessel 不等式：

$$
 \sum_{j=2}^M|\langle U_j,1\rangle|^2\le1,
 \qquad
 \sum_{j=2}^M|\langle U_j,x\rangle|^2\le\frac12.
$$

这里无需 $U_j$ 在整个 L² 上完备；仅有这个正交子集便足够。于是

$$
 \|V_M\|_F^2\le\frac32,\qquad
 \|C_M\|_2^2\le\|K^{-1}\|_2^2\|V_M\|_F^2
                 \le\frac32\|K^{-1}\|_2^2.           \tag{10}
$$

综合 (9)–(10)，对每个 M≥2 和任意实向量 z，

$$
 \boxed{\quad
 \|z\|_{\ell^2}^2\le
   \left\|\sum_{j=2}^M z_jB_j\right\|_2^2
  \le\left(1+\frac32\|K^{-1}\|_2^2\right)\|z\|_{\ell^2}^2.
 \quad}                                               \tag{11}
$$

因此 $\lambda_{\min}(\mathcal G_M)\ge1$、
$\kappa_2(\mathcal G_M)\le1+(3/2)\|K^{-1}\|_2^2$，右侧独立于 M。
这个一般定理是严格结论；下面的浮点 K 数值不是它的严格数值上界。

## 4. 与原 raw finite span 完全相同

定义

$$
 \mathcal Y_M=\{p\in\mathbb R[x]:\deg p\le M,
   \ \langle Wp,1\rangle=\langle Wp,x\rangle=0\}.
$$

由 $m_0m_2-m_1^2>0$，这两条线性约束在次数≤M的空间上独立，故
$\dim\mathcal Y_M=M-1$。式 (8) 除去 W 后是
$P_j-c_{0j}P_0-c_{1j}P_1$，其次数恰为 j、最高次系数非零，且属于 $\mathcal Y_M$。
按最高次数消元，这 M−1 个多项式线性无关，因而构成 $\mathcal Y_M$ 的一组基。

原 raw λ=1 控制是

$$
 W\,[T_j(x)-\Pi_W T_j(x)],\qquad j=2,\ldots,M,        \tag{12}
$$

其中 $T_j(\cos\theta)=\cos(j\theta)$，$\Pi_W$ 是 W 权下向
$\operatorname{span}\{1,x\}$ 的投影。其 W 权 2×2 Gram 同样由上述严格方差保证可逆。
式 (12) 除去 W 后也属于 $\mathcal Y_M$、次数恰为 j、最高次系数非零，因此是同一多项式空间的另一组基。

乘 W 在多项式空间上是单射：若 $Wp=0$，在 W 为正的开区间上 p 为零，所以 p 恒为零。
因此

$$
 \operatorname{span}\{B_2,\ldots,B_M\}
   =\operatorname{span}\{W(T_j-\Pi_WT_j):2\le j\le M\},  \tag{13}
$$

而两组有限控制坐标之间的线性变换唯一且可逆。完整 q、主圆化核及 W 固定后，
正确变换全部控制坐标会保留同一个完整核心函数；不是物理同伦。
同时每列独立于 M，故新坐标中 append 0 精确保留原控制函数，适合定义真正嵌套的固定 g 精化。

这项等价性只在 λ=1 如此陈述。若沿 λ<1 只替换 compact 部分而保留原 cosine 部分不作相同变换，
会改变原同伦路径；不能凭 (13) 声称沿途 BVP 或度量相同。

## 5. 一个隔离的有限数值探针

[screen_supported_orthogonal_coordinates.py](../scripts/resume_m3/screen_supported_orthogonal_coordinates.py)
用每个非零分段 512 点 Gauss 求积形成候选三项递推系数；它没有改生产核心库或正在运行的 λ=1 BVP。
实际输入为完整 M16 的十五 c，取 a=.21、bc=.4。结果为：

| 有限检查 | 数值 |
|---|---:|
| $U$ Gram 与单位阵的最大差 | `5.339001132474361e-16` |
| 两条约束残差 | `4.9291811816043127e-17` |
| 新 Gram 与 $I+C^TC$ 的最大差 | `6.938893903907228e-16` |
| 新 Gram 最小/最大特征值 | `.9999999999999977` / `2.061367482987432` |
| 新 Gram 条件数 | `2.061367482987437` |
| $\|K^{-1}\|_2$ 的浮点值 | `2.935310280896174` |
| 将该浮点值代入一般上界 | `13.924069667702167`，**非严格数值上界** |
| 旧 raw 物理 L² 采样矩阵条件数 | `760819.3741088586` |
| 旧 raw 物理 L² Gram 条件数（由 SVD 平方计算） | `5.788461200193954e11` |

旧代码另报的 `1.5533225210953648e10` 是 W 权高矩 Schur 的条件数，
与这里实际控制函数的 W² 物理 L² Gram 是不同矩阵，不能混写。

把同一实际十五 c 变成该有限候选坐标后，在 2049 个比较点的支撑函数 0/1/2 阶 jet 差分别不超过
`3.2526065174565133e-19`、`8.565197162635485e-18`、`4.458239333260394e-16`；
控制曲率差也不超过最后一数。精确 finite span 等价由第4节证明，不能由这些样本反推。

命令、源码和输出 SHA-256 见
[supported_orthogonal_coordinates_execution.json](../scripts/resume_m3/supported_orthogonal_coordinates_execution.json)。
连续正交多项式及连续两矩的具体生产系数还需相应包围；当前 Gauss 系数不自动升级为精确系数。

## 6. 在本课题中的用途与边界

式 (11) 仅控制控制函数本身的 L² 坐标，不能控制角导数、C² 范数、正性余量或全 metric。
也不能从小 Gram 条件数推出实际投影 Frenet 方程、边界条件或 tail DN 的 Jacobian 良态。
在真正用于求解之前，需要完成稳定递推/导数/原始函数的生产实现、连续系数定义及必要的参数链式法则；
原 rho/Frenet/D/S/A、尾 `2e-9`、完整 metric 和几何门全部继续保留。

本条给出了一个保持端点有限函数空间的可算坐标方案，并没有把旧失败态变成接受态，
也没有在 C⁴ 空间中宣称任意 supported 函数均属于某个有限或无限参数像。

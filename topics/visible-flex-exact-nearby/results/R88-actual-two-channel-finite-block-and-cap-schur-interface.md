# R88：真实双通道有限块、完整均值帽 Schur 与有向系数入口

2026-11-12，reproduce-newton。

**状态：已构造并实际计算新的完整双通道有限模型；实际无限图的若干
径向点 Fourier 系数及真无限尾低模 DN 已有向支付。径向传播、有限
帽 Galerkin 与最终无限维 Schur 的误差仍须另付。** 本篇不以 principal
返回替代完整算子，也不把旧 metric Newton 的 Schur 列移作本篇低块。

当前点是准确显式对称仿射对象
\(\delta_5=-7789843107295549/4611686018427387904\)。真尾数据在
已登记公共盒 \(|\delta-\delta_5|\le1/2500000\) 上成立。下面的浮点
核心和帽实验只在中心点计算；不把它们升级为整个参数盒的结果。

## 1. 物理系数与穿过腰圈的零阶项

沿用 [R37](R37-fixed-type-metric-defect-newton-interface.md) 的物理
散度算子。记
\[
 X=F_r,\quad T_1=F_\theta,\quad
 c_*=T_1\times X,\quad G=c_*\cdot c_*,\quad
 R_2=F\cdot F,\quad S=F\cdot c_*,
\]
\[
 L_*=c_*\cdot F_{rr},\quad M_*=c_*\cdot F_{r\theta},\quad
 N_*=c_*\cdot F_{\theta\theta},\qquad h_*=R_2/S^2.
\]
在同一真实核心，\(S>0,N_*<0\)。不引入正 height 除法便有
\[
 a=-N_*h_*,\quad b=M_*h_*,\quad c=-L_*h_*,\quad
 \widehat c=-\frac{M_*^2+K_0G^2}{N_*}h_*,\quad
 \omega=c-\widehat c.                                      \tag{88.1}
\]
这些是 R37 的原始材料密度，未将其乘以变化的 \(\zeta^2\) 后偷换
为另一个散度算子。

令 \(u=F/|F|\)。原零阶项可完全用二 jet 计算：
\[
 d=\sum_{j=1}^3(\nabla u_j)^T\mathsf A\nabla u_j
 =\frac1{R_2}\left[
 a\left(X^2-\frac{(F\cdot X)^2}{R_2}\right)
 +2b\left(X\cdot T_1-\frac{(F\cdot X)(F\cdot T_1)}{R_2}\right)
 +c\left(T_1^2-\frac{(F\cdot T_1)^2}{R_2}\right)\right].       \tag{88.2}
\]
证明是将真实 \(Pu_j=0\) 乘以 \(u_j\) 求和，用
\(\sum u_j^2=1\)、\(\sum u_j\nabla u_j=0\)。这保留原真实零阶项，
不由目标曲率猜一个势。

取已支付的贯穿腰圈函数
\[
 \ell=\partial_\theta\log(F_z/r)-\tfrac12\partial_\theta\log R_2.
\]
当 \(r\ne0\) 时等于 \(F_{z,\theta}/F_z-(F\cdot F_\theta)/R_2\)；
在 \(r=0\) 的准确值是
\(F_{z,r\theta}/F_{z,r}-(F\cdot F_\theta)/R_2\)。显式奇偶性及
已证 \(F_z/r>0\) 支持此可去奇性，而非将一个小浮点量看成零。
R37 的完整修正于是为
\[
 \widehat P w=\partial_r(aw_r+bw_\theta)
 +\partial_\theta(bw_r+\widehat c w_\theta)
 +\left[d+(\omega\ell)_\theta+\omega\ell^2\right]w.           \tag{88.3}
\]
保存 \(\tau=d+\omega\ell^2\)、\(\sigma=\omega\ell\)，在 Fourier
系数层准确取 \(\widehat d_l=\tau_l+4il\sigma_l\)。因此无需用空间
有限差分计算 \((\omega\ell)_\theta\)。在腰圈始终没有除以
\(Y_z=F_z/|F|\)。

## 2. 先投影再消元的完整双通道系统

固定 \(k=-N,\ldots,N\)，物理频率为 \(4k\)，并置
\(D=\operatorname{diag}(4ik)\)。对任意真实系数 \(q\)，令
\((M_q)_{kj}=q_{k-j}\)，保持全部 lag \(|k-j|\le2N\)。写
\[
 A=M_a,\quad B=M_b,\quad C=M_{\widehat c},\quad H=M_{\widehat d}.
\]
有限 Galerkin 方程使用
\[
 p=A w_r+B D w,\qquad
 p_r+D B w_r+D C D w+H w=f_N.                               \tag{88.4}
\]
这里必须先投影 \(a\)，再逆有限 \(A\)；直接投影点乘的 \(a^{-1}\)
定义的是另一个有限系统。完整真实 \(a\ge a_*>0\) 给
\(A\ge a_*I\)。消元得到
\[
 \frac d{dr}\binom wp=
 \begin{pmatrix}
 -A^{-1}BD&A^{-1}\\
 DBA^{-1}BD-DCD-H&-DBA^{-1}
 \end{pmatrix}\binom wp+\binom0{f_N}.                       \tag{88.5}
\]
所有零模都在两条通道中，普通源的均值同样保留。实系数使
\(A,B,C,H\) 自伴，\(D^*=-D\)，故对
\(J=\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)\)
有准确 \(\mathcal F^*J+J\mathcal F=0\)。真实有限径向传播保持这个
通量。数值残差小只是诊断，不替代连续传播误差界。

显式径向对称性给 \(a,\widehat c,\widehat d\) 偶、\(b\) 奇。
若 \(T_+\) 从 0 传到 \(c\)，\(R=\operatorname{diag}(I,-I)\)，则
\[
 T(-c,c)=T_+R T_+^{-1}R.                                    \tag{88.6}
\]
这是本篇完整有限算子的两迹恒等式，与 R77 的标量主返回平方恒等式
用途不同。没有角 involution，也没有删除反向通道。

若 \(T=\left(\begin{smallmatrix}T_{11}&T_{12}\\T_{21}&T_{22}\end{smallmatrix}\right)\)
且 \(T_{12}\) 可逆，其两端物理高度到向外通量 \((-p_-,p_+)\) 的矩阵是
\[
 \Lambda_{\rm core,N}=
 \begin{pmatrix}
 T_{12}^{-1}T_{11}&-T_{12}^{-1}\\
 T_{21}-T_{22}T_{12}^{-1}T_{11}&T_{22}T_{12}^{-1}
 \end{pmatrix}.                                            \tag{88.7}
\]
在 Dirichlet 共振处应保留 (88.5) 的两通道；不能强行使用 (88.7)。

## 3. 已实际支付的有限系数，而非有限 primitive 替代

`scripts/fourfold_phase_core_low_coefficients.py` 使用准确仿射 native
样条、完整 primitive 误差和已付同对象复图表。它先计算真实实轴
角节点球，再对每个 scalar Fourier lag 付完整梯形混叠费。
若归一角 \(x=4\theta\) 的外带宽为 \(s\)，全带模数为 \(M\)，
角节点数为 \(Q\)，则 \(|l|<Q/2\) 的费用为
\[
 M\frac{e^{-s(Q-|l|)}+e^{-s(Q+|l|)}}{1-e^{-sQ}}.              \tag{88.8}
\]
真正无限 primitive 的误差先进入节点和外带模数；没有只对截断
primitive 付 (88.8)。逆矩阵与 (88.5) 全部在 Arb 复球矩阵中执行。

直接宽复矩形求 \(1/N_*\) 在腰点曾拒绝。本版使用同一完整复图表
的实际 \(|N_*|\)、\(\Re S\)、\(\Re R_2\) 正下界来付商模数。
这些下界绑定 origin、direction、准确参数包含、整个实核心与
物理 \(1/64\) 角带，不把区间包裹的失败解释为真实零点。

实际完成 \(N=4\)、Q=1024、primitive Q=512，在
\(r=0,1/8,61/256\) 三点的全部 18×18 generator：

| 实际半径 | 连续实角上的 \(a\) 安全下界 |
|---|---:|
| 0 | 0.23741541429409909 |
| 1/8 | 0.39717917511890021 |
| 61/256 | 0.58487961387246956 |

报告 `notes/2026-11-12-actual-core-low-coefficients-M4.json` 保存每个
真实系数球、全部矩阵元、外带模数和对象哈希。此处尚未覆盖两点
之间的径向传播，不能把三个点合称整个核心证书。

重放：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_core_low_coefficients.py --modes 4 \
  --out notes/2026-11-12-actual-core-low-coefficients-M4.json
```

## 4. 首批完整核心有限传播诊断

`scripts/fourfold_phase_core_low_block.py` 在同一 δ5 上读取真正
R37 系数，正侧逐 174 个实际共同样条 span 积分，再用 (88.6)。
有限 radial primitive 的统一网格评价改用准确 Fourier folding
的浮点 FFT；角 jet 仍用真实单位切向公式。三个径向点的六个
二 jet 与原逐点 evaluator 独立比较，最大差小于 \(2.45\,10^{-15}\)。
原慢 evaluator 的首轮被主动终止，退出码 130，没有保存或声称
完成结果。当前两次完整运行如下：

| N | 两通道维数 | CPU 秒 | 半核心通量缺陷 | 核心 DN 自伴缺陷 | DN 均值到非均值耦合 norm |
|---:|---:|---:|---:|---:|---:|
| 2 | 10 | 13.92 | 2.19e−14 | 4.57e−14 | 1.32129 |
| 4 | 18 | 14.16 | 2.89e−13 | 1.92e−12 | 1.37640 |

核心切口为 \(r=\pm1/4\)。两次最小有限 DN 奇异值分别约
0.00913 和 0.01065。它们属于这些具体 Galerkin 核心模型，未接
真实帽和无限高频 Schur；因此不构成最终低块可逆性结论。
均值耦合为一阶量，实际显示删均值会改变此系统。

完整两通道传播和 DN 矩阵在各自同名前缀 NPZ 中保存。程序每
20 个 span 保存 partial checkpoint；最终报告绑定源与对象。

随后把这三个点的浮点 generator 与第 3 节的真球直接比较，结果
**没有全部包含**。不包含项都在左下块，最大中心差分别为
\(2.22\,10^{-9},3.39\,10^{-9},4.31\,10^{-9}\)。独立纯 Arb
`AffineBallTarget` 的三个真实 K 球全部与 fast directed 核相交；
浮点 K 与纯 Arb 中心差分别约
\(-5.09\,10^{-12},4.38\,10^{-12},8.47\,10^{-12}\)。直接逐
scalar jet 对照显示 SciPy 二阶半径导数差达 \(1.46\,10^{-11}\)，
第三阶差达 \(1.40\,10^{-8}\)。这里 K 的误差经 \(DCD\) 的
\((4N)^2\) 因子放大，解释了上述左下块差异。小自伴/通量缺陷
并不检测这种自伴系数误差。

此发现不改变第 3 节独立 native 真实系数球；也没有人为扩大球
来包含一个本来不受证书约束的浮点评价。重放源
`fourfold_phase_core_native_diagnostic.py` 和报告
`notes/2026-11-12-core-native-diagnostic-replay.json` 同时保存
失败项、完整 scalar 比较及纯 Arb 对照，早期两个 inline 诊断
报告保留原字节。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_core_low_block.py --modes 4 \
  --out notes/2026-11-12-actual-core-low-block-M4.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_core_native_diagnostic.py \
  --out notes/2026-11-12-core-native-diagnostic-replay.json
```

## 5. 真无限尾有限端口

R74 的真实外尾给每个物理 \(m=4|k|\ne0\)
\[
 \gamma_m^0=\frac{1+4m\omega/A_0}{A_0+4\omega/m},\qquad
 A_0=4\omega+a_*^2/z_*.
\]
准确第四模有 \(\gamma_4=\gamma_4^0\)。其它模保留
\[
 |\gamma_m-\gamma_m^0|\le m2^{42}e^{-2m\omega B}<m2^{-100}.   \tag{88.9}
\]
`scripts/fourfold_phase_finite_tail_DN.py` 检查完整 R74 realization、
同一 graft、真实参数包含和 barrier 长度，再有向输出各低模。
它没有将 \(\gamma_m\) 直接设为稳定线。

当前已完成 \(|k|\le8\)，例如 \(\gamma_4\) 包在约
\([0.68439109\pm3.08\,10^{-9}]\)。这些球主要反映实际入口的
参数盒，完整精确有向端点保存在报告。

在 form 中延拓 \(\Gamma_H1=0\) 仍须同时保留 regular mean
输入 \(\xi\) 与输出 \(\lambda\)；这不是一个自由 mean 边界条件。
尾的普通源也不包含在齐次 \(\gamma_m\) 中，须按 R74 的实际
源/contact 行相加。

```bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_finite_tail_DN.py --modes 8 \
  --out notes/2026-11-12-actual-finite-tail-DN-M8.json
```

## 6. 完整正帽有限 Schur 的可运行接口

在正帽取真实 \(Y=Y_z>0\)、\(w=YU\)。同一修正满足
\[
 Y\widehat P(YU)=\operatorname{div}(\mathsf B\nabla U),\qquad
 \mathsf B=Y^2\widehat{\mathsf A}.
\]
其系数可不经 \(|F|\) 除法写成
\[
 \mathsf B_{11}=-F_z^2N_*/S^2,\quad
 \mathsf B_{12}=F_z^2M_*/S^2,\quad
 \mathsf B_{22}=-F_z^2(M_*^2+K_0G^2)/(N_*S^2).               \tag{88.10}
\]
使用物理角上的正 form
\[
 b(U,V)=\int_{1/4}^{25/8}\!\langle\mathsf B\nabla U,\nabla V\rangle dr
             +\langle\Gamma_HU(25/8),V(25/8)\rangle.        \tag{88.11}
\]
在 \([1/4,3]\) 用同一真实 body，在 \([3,25/8]\) 使用 R71/R74
的自然权 C4 graft，外面接 (88.9)。不在 r=3 人工设置边界。

取连续径向 P1 基和全部 \(k=-N,\ldots,N\) Fourier 基。对径向
基 \(\phi_i,\phi_j\)，准确弱矩阵 integrand 为
\[
 \phi_i'\phi_j'A_B+\phi_i'\phi_j B_BD
       -\phi_i\phi_j'DB_B-\phi_i\phi_jD C_BD.              \tag{88.12}
\]
完整矩阵按径向节点为 block tridiagonal。先消去全部内部节点，
再仅消去 regular 端非零角模，保留
\[
 (U_{\rm left,k})_{|k|\le N}\oplus\xi
       \longmapsto(p_{\rm left,k})_{|k|\le N}\oplus\lambda.\tag{88.13}
\]
这是一个真正的有限 Schur 运算，regular 的均值通量没有消去。
若有限矩阵块写成 \(K_{bb},K_{bi},K_{ii}\)，则
\(S=K_{bb}-K_{bi}K_{ii}^{-1}K_{ib}\)。普通弱源 \(g\) 的完整
有效负荷是 \(g_b-K_{bi}K_{ii}^{-1}g_i\)，contact 为
\(S U_b-(g_b-K_{bi}K_{ii}^{-1}g_i)\)；源符号仍须由
\(Y\widehat P(YU)\) 的实际方程换入，不设为零。

源 `scripts/fourfold_phase_cap_low_schur.py` 已实现这个模型。它对
小半径 body 先在真实切向层减去圆模，再计算 E 与 K 的小修正，
避免将两个很大的背景曲率项相减。当前积分与线性代数是浮点，
所以其报告显式标 `rigorous_cap_DN=false`；尾球取中点只定义此
有限模型，球半径另存，不与准确真尾混同。

Fourier 系数均用平均角内积。若改用 R74 的
\(\phi_0=(2\pi)^{-1/2}\)，输入和输出的全部 Fourier 坐标同乘
\(\sqrt{2\pi}\)，矩阵不变；非齐次 mean 数值则须一起换算。

已实际完成 \(N=4\) 的 72 个径向单元模型：16 个内帽单元、48 个
body 单元与 8 个 graft 单元。求积在所有实际共同样条节点处分段，
但不因极近的二进制 knot 人工增添极短 FE 未知量。4 点 Gauss 共
调用 5400 个实际系数点，CPU 25.27 秒。10×10 增广 DN 的自伴缺陷
为 \(2.99\,10^{-16}\)，共同常数向量的残差为
\(3.74\,10^{-15}\)。regular mean 输出对左端常数输入约为
\(-0.01492414598\)，确实不是可删的零行。完整未知量、radial
block 矩阵和增广 Schur 均在同名 NPZ 中保存。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_low_schur.py --modes 4 --radial-elements 48 \
  --out notes/2026-11-12-actual-cap-low-Schur-M4.json
```

## 7. 物理接线与尚欠的真正低块

在正核心右界，令 \(p_w=aw_r+bw_\theta\)、
\(p_Y=aY_r+bY_\theta\)。同一帽的向外 grounded conormal 准确为
\[
 U=Y^{-1}w,\qquad p_{g,\rm cap}=-(Yp_w-wp_Y).             \tag{88.14}
\]
两个 multiplication 都是完整角算子。不能把有限
\(\Pi_N M_Y\Pi_N\) 的逆当作 \(\Pi_N M_{Y^{-1}}\Pi_N\)，也不能忽略
它们产生的高模式。随后才接 R83 的实际角、高度、动量与
\(L_1/2\) shear，再接 R53 的共同根剪切。R85 的 root 零模及
regular 有限端口继续存在。

`fourfold_phase_low_feedback.py` 已将两个上述帽和实际核心有限 DN
按此物理规则接成 20×20 系统，其中 18 个两侧低频高度与 2 个
regular mean 输入/通量全部保留。左帽选正 height \(-Y_z\)，右帽
选 \(Y_z\)；全局竖直平移因此对应两侧 grounded 常数的符号
\((-1,+1)\)，regular 常数同样取此符号。当前有限系统的这个
平移向量残差为 \(6.08\,10^{-4}\)，不是准确零。加此 gauge 行列
后的浮点逆范数约 63.025。

接线 multiplication 也展示不能免费忽略的高模：在这次有限
采样中，\(|l|>8\) 的 \(Y\) 系数绝对和约 \(4.63\,10^{-5}\)，
\(Yp_Y\) 系数绝对和约 0.1062。二者都是当前有限 FFT 的诊断，
不是无限尾界，但已足以排除“低块只保对角接线”的做法。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_low_feedback.py \
  --out notes/2026-11-12-actual-low-feedback-M4.json
```

最终目标低块是同一个全频算子在已付高切 N 下的准确
\(A_{LL}-A_{LH}A_{HH}^{-1}A_{HL}\)。本篇的 \(N=2,4\) 只是实际
有限入口与成本/结构诊断，尚未由 R53/R85 总余项指定为最终高切。
它们也没有支付有限径向近似、帽全域投影、接线高模和真正
普通源的全部误差。当前可继续直接使用的是 (88.1)–(88.14)
及已保存的真实有限系数和端口数据，而非一个未经验证的最终逆。

## 8. 不依赖一般逆大常数的帽互补能量界

下面给同一个完整正帽 DN 的可直接计算上下界，未将帽的非均值
高模解设为零。令 \(g=(U(c,\cdot),\xi)\)，其中左端迹是给定
有限 Fourier 多项式，regular 端只有均值 \(\xi\) 固定。对任意
满足这些 Dirichlet 数据的 \(H^1\) 试函数 \(V\)，真 DN 的二次型
是能量最小值，故
\[
 \langle Sg,g\rangle\le
 E(V)=\int \nabla V^*\mathsf B\nabla V
           +\langle\Gamma_H V_R^\perp,V_R^\perp\rangle.   \tag{88.15}
\]
这里除 \(\xi\) 外的 regular 模式均自由；试函数可以取第 6 节的
有限解，但其准确系数与真正积分误差须明确支付。

另选任意真实 \(H(\mathrm{div})\) 通量 \(j=(p,q)\)，满足
\(p_r+q_\theta=0\)，并记
\[
 L(j,g)=-\langle p_L,g_L\rangle+\overline{p_0}\xi,
 \qquad
 D(j)=\int j^*\mathsf B^{-1}j
       +\langle\Gamma_H^{-1}p_R^\perp,p_R^\perp\rangle.     \tag{88.16}
\]
角平均 \(p_0\) 沿径向为常数，\(\Gamma_H^{-1}\) 只作用于非零模。
分部积分和配方给对每个 admissible \(V\) 的准确恒等式
\[
 E(V)-2\Re L(j,g)+D(j)
 =\int(\nabla V-\mathsf B^{-1}j)^*\mathsf B
                 (\nabla V-\mathsf B^{-1}j)
  +\|\Gamma_H^{1/2}V_R^\perp+
                 \Gamma_H^{-1/2}p_R^\perp\|^2\ge0.        \tag{88.17}
\]
因此 \(2\Re L-D\le\langle Sg,g\rangle\le E(V)\)。这对
完整角算子成立；没有使用有限 Galerkin 解等于真解的假设，也不
乘以 R74 一般源解的较大逆常数。

有限通量空间可直接选
\[
 p_k(r)\text{ 为连续 P1},\quad
 q_k=-p_k'/(4ik)\quad(k\ne0),\qquad
 p_0\text{ 为全局常数},\quad q_0\text{ 为逐单元常数}.    \tag{88.18}
\]
它在分布意义下准确散度为零：\(p\) 没有径向跳跃，切向通量的
径向跳跃不进入散度。regular mean 的形式没有改动。
若 \(D=j^*H_Dj\)、\(L=j^*L_Dg\)，最大化有限通量参数给
\[
 L_D^*H_D^{-1}L_D\ \le S\ \le S_{\rm trial}.                \tag{88.19}
\]
从而只要对两个有限能量矩阵付有向积分和求逆误差，就能证某个
真实有限输入块的帽 DN 包络。它尚不等于核心/帽全频反馈的
\(A_{LL}-A_{LH}A_{HH}^{-1}A_{HL}\)；两者的任务不可混同。

新源 `fourfold_phase_cap_complementary_energy.py` 实现 (88.18)–
(88.19)。它沿用原 primal 的实际网格、对象和 tail 数据，重新
计算真实物理 form 的逆矩阵系数；当前运行仍是浮点求积候选，
不会仅凭正的能量差把它称为有向证书。

第一轮实际 \(N=4\) 同网格共有 657 个 flux 未知量，CPU 24.89 秒。
得到的浮点上、下矩阵差为半正定至舍入层，最大特征值约 0.08882；
共同常数输入的 dual 输出准确为零。这个差尚不够当前反馈约
63 的逆尺度，明确保留为需要收紧的量。它包含 radial 与帽内部
角空间的限制，不能只凭增加 core 截断 N 把它宣布消失。完整
finite flux 系数和两个边界矩阵均在同名前缀 NPZ 中保存。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_complementary_energy.py \
  --out notes/2026-11-12-actual-cap-complementary-energy-M4.json
```

非齐次源也可保留在同一恒等式中。若物理 grounded 方程为
\(\operatorname{div}(\mathsf B\nabla U)=f\)，取
\(\operatorname{div}j=f\)，并将能量改为
\(E(V)+2\Re\int\overline f V\)。分部积分的源项恰好抵消，
(88.17) 原式右端仍成立。由一个真实 particular flux 加有限的
散度零通量即可形成含源的二次/一次有效负荷；若只近似满足散度
方程，剩余项 \(2\Re\langle f-\operatorname{div}j,V\rangle\)
必须另付。本篇实际数值仅做零源矩阵，没有声称该非齐次费用已付。

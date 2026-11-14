# R90：前缀圆柱 Fourier 基的 FFT 恒等式与实际加速

状态：**已证明的有限角节点代数恒等式及明确误差分解。** 本稿支持当前同 g 高模前缀的 `values/project` 加速；不改变 Frenet 方程、warp、节点数、保留模式或边界条件。FFT 与旧逐项表求和有不同的舍入顺序，不能声称它们逐 bit 相同；本文也没有给 SciPy 实现冒充一个未计算的严格舍入证书。

作者：Astra-visible-flex-78718bd0，`/root/geometric_closure`，2026-11-10。实际加速实现与计时由 `numerical_recovery` 完成；本结果只用于后续选择的新 Flow，不改正在运行的 M15 源。

## 1. 当前实际基与离散变换约定

源 `curve_stable_prefix_bvp.py::CylindricalPrefix.basis` 的状态顺序为

$$
C=(R_0,R_1,\ldots,R_M,T_1,\ldots,T_M,Z_1,\ldots,Z_M).
$$

令 $k_j=mj$，当前 $m=3$，并取 $\psi_l=2\pi l/N$。对应曲线扰动是

$$
X(\psi)=R(\psi)e_r(\psi)+T(\psi)e_\theta(\psi)+Z(\psi)e_z,
\tag{1}
$$

$$
R=R_0+\sum_{j=1}^M R_j\cos(k_j\psi),\quad
T=\sum_{j=1}^M T_j\sin(k_j\psi),\quad
Z=\sum_{j=1}^M Z_j\cos(k_j\psi).
\tag{2}
$$

以下有限 DFT 使用不缩放的正变换

$$
\widehat f_k=\sum_{l=0}^{N-1}f_l e^{-2\pi ikl/N},\qquad
f_l=\frac1N\sum_{k=0}^{N-1}\widehat f_k e^{2\pi ikl/N}.
\tag{3}
$$

要求 $mM+1<N/2$，于是所用圆柱和 Cartesian 频率都不触及 Nyquist。实际前缀的节点选择满足更强的 $N\ge8(mM+1)$。节点数不必被 $m$ 整除。

## 2. 实 Fourier 合成及一、二阶角导数

对任意实三角多项式
$f=a_0+\sum_{0<k<N/2}(a_k\cos k\psi+b_k\sin k\psi)$，实逆 FFT 的非负频谱应填成

$$
\widehat f_0=Na_0,\qquad
\widehat f_k=\frac N2(a_k-i b_k),\qquad
\widehat f_{N/2}=0.
\tag{4}
$$

其余未使用频率置零，负频率由共轭对称补齐。代入 (3)，正负两项之和恰为 $a_k\cos k\psi+b_k\sin k\psi$，证明 (4) 在所有节点精确合成原多项式。无须在径向常数上错误地再乘 $1/2$。

实际新实现选择 `scipy.fft.irfft(..., norm='forward')`，使逆变换不再乘 $1/N$；因此代码填入的是 $a_0$ 和 $(a_k-i b_k)/2$，即 (4) 全部除以 N。正向投影仍用 `rfft(..., norm='backward')` 的未缩放变换 (3)。这两处约定共同给出上述同一个合成/投影，不能在代码已选择未缩放逆变换后再乘一次 N。

利用 $e_r'=e_\theta$、$e_\theta'=-e_r$，直接对 (1) 求导：

$$
X_\psi=(R'-T)e_r+(R+T')e_\theta+Z'e_z,
\tag{5}
$$

$$
X_{\psi\psi}=(R''-R-2T')e_r+(2R'+T''-T)e_\theta+Z''e_z.
\tag{6}
$$

因此三个局部分量的 FFT 输入可以直接按下表生成。

| 角导数阶数 | 径向分量 | 切向分量 | 竖直分量 |
|---|---|---|---|
| 0 | $R_0+\sum R_j\cos k_j\psi$ | $\sum T_j\sin k_j\psi$ | $\sum Z_j\cos k_j\psi$ |
| 1 | $-\sum(k_jR_j+T_j)\sin k_j\psi$ | $R_0+\sum(R_j+k_jT_j)\cos k_j\psi$ | $-\sum k_jZ_j\sin k_j\psi$ |
| 2 | $-R_0-\sum((k_j^2+1)R_j+2k_jT_j)\cos k_j\psi$ | $-\sum(2k_jR_j+(k_j^2+1)T_j)\sin k_j\psi$ | $-\sum k_j^2Z_j\cos k_j\psi$ |

最后逐节点乘 $e_r,e_\theta,e_z$ 得 Cartesian 输出。这正是原 `B/B1/B2` 的逐列公式。旋转并没有截掉任何 Cartesian 频率：水平复坐标为 $(R+iT)e^{i\psi}$，所以保留的频率是 $1\pm k_j$，另有常数径向项产生的频率1。把圆柱系数的最大频率 $mM$ 误当成 Cartesian 截止频率会丢失其中一支；上述算法没有这样做。

## 3. 原有限节点投影的 FFT 表达

给定任意实 Cartesian 节点数组 $F_l$，先逐点旋回

$$
f^R_l=F_l\cdot e_r(\psi_l),\qquad
f^T_l=F_l\cdot e_\theta(\psi_l),\qquad f^Z_l=F_{l,z}.
\tag{7}
$$

保留原基列各自的正分母

$$
n_a=\sum_l|B_a(\psi_l)|^2.
\tag{8}
$$

若正变换采用 (3)，原 `CylindricalPrefix.project` 的各分量恰为

$$
\begin{aligned}
(\Pi F)_0&=\operatorname{Re}\widehat f^R_0/n_0,\\
(\Pi F)_{R_j}&=\operatorname{Re}\widehat f^R_{k_j}/n_{R_j},\\
(\Pi F)_{T_j}&=-\operatorname{Im}\widehat f^T_{k_j}/n_{T_j},\\
(\Pi F)_{Z_j}&=\operatorname{Re}\widehat f^Z_{k_j}/n_{Z_j}.
\end{aligned}
\tag{9}
$$

证明：$\operatorname{Re}\widehat f_k=\sum_l f_l\cos(k\psi_l)$，$-\operatorname{Im}\widehat f_k=\sum_l f_l\sin(k\psi_l)$；再用 (7) 展开点积即可。对于理想实数三角基，(8) 分别是 $N$ 和 $N/2$。实际新实现仍保留旧 binary 基表所算的分母，不用理想值覆盖它们。

此式对任意节点数组成立，不要求非线性向量场本身带限。原 N 点投影的 aliasing 因而仍属于同一个有限节点模型；FFT 不删除也不新增一个“连续 Fourier 投影精确”的承诺。

实际实现也处理以 `B1/B2` 作为分母基的调用。为完整写出其数学含义，记
$C_{R,k}=\operatorname{Re}\widehat f^R_k$、$S_{R,k}=-\operatorname{Im}\widehat f^R_k$，T、Z 同理。以下列出各投影的分子；每列除以所用阶数的原 $\sum_l|B^{(h)}_a|^2$。

| 所用基 | 常数径向列 | $R_j$ 列 | $T_j$ 列 | $Z_j$ 列 |
|---|---|---|---|---|
| $B^{(0)}$ | $C_{R,0}$ | $C_{R,k}$ | $S_{T,k}$ | $C_{Z,k}$ |
| $B^{(1)}$ | $C_{T,0}$ | $-kS_{R,k}+C_{T,k}$ | $-S_{R,k}+kC_{T,k}$ | $-kS_{Z,k}$ |
| $B^{(2)}$ | $-C_{R,0}$ | $-(k^2+1)C_{R,k}-2kS_{T,k}$ | $-2kC_{R,k}-(k^2+1)S_{T,k}$ | $-k^2C_{Z,k}$ |

表中 $k=k_j$。证明是将第2节逐列的一、二阶基与 F 点乘，再应用 (3) 的余弦/正弦求和公式。这里的 `project(F,B1)` 本来就不是 `project(F,B)` 的角导数；它是原程序对另一组列分别取点积再除列范数的同一操作。未声称导数基之间在有限节点内正交。

## 4. 复杂输入必须保持复线性

旧 `values/project` 的基表为实数，故对复输入 $A+iB$ 应满足

$$
\mathcal T(A+iB)=\mathcal T(A)+i\mathcal T(B),
\tag{10}
$$

其中 $\mathcal T$ 表示合成或投影的实线性映射。因此最直接的实现是把输入实、虚部各自送入实 FFT 路径，再按 (10) 合并。对合成，不能将任意复系数当成一个实函数的共轭对称频谱交给 `irfft`。对投影，也不能将复数组的单次 FFT 后直接取实部当作复余弦系数：那会混合或丢失需要保留的虚部。

这一拆分对 `complex-step` 尤其必要。输入 $A+i\varepsilon B$ 时，虚支 FFT 只处理尺度为 $\varepsilon$ 的实数组，不会把实支尺度为1的 FFT 舍入残差带入虚部后再除以 $\varepsilon$。在当前 Frenet 正根分支内，后续点乘采用双线性而非 Hermitian 形式，正平方根有局部解析延拓；所以该复线性 FFT 包装仍可用于

$$
\varepsilon^{-1}\operatorname{Im}f(A+i\varepsilon B)
=Df(A)B+O(\varepsilon^2).
$$

这只是解析恒等式和正确数据通道；实际浮点误差仍由所用实支计算决定。根域判定在邻域内不触发时不影响该局部延拓。

## 5. binary 基表与 FFT 根之间的误差在哪里

旧代码先以 binary64 网格计算 `sin/cos`，再形成及保存 Cartesian 基表。新实现可复用原保存的 binary $e_r,e_\theta$，但 FFT 的内部旋转根、乘加和求和树仍与旧逐列求和不同。

令 $B^{(h)}_{a,l}$ 是旧保存的第 $h$ 阶基表。令 $\widetilde B^{(h)}_{a,l}$ 表示“用 (4) 的理想 DFT 进行局部合成，再以指定的保存旋转向量旋转”的精确算术结果。定义

$$
\epsilon^{(h)}_a=\max_l
|\widetilde B^{(h)}_{a,l}-B^{(h)}_{a,l}|.
$$

那么在尚未计入变换自身舍入时，合成的准确差满足

$$
\max_l\left|\sum_a C_a
(\widetilde B^{(h)}_{a,l}-B^{(h)}_{a,l})\right|
\le\sum_a|C_a|\epsilon^{(h)}_a.
\tag{11}
$$

保持同一分母 (8) 后，投影的准确差满足

$$
|\widetilde\Pi_aF-\Pi_aF|
\le \frac1{n_a}\sum_l |F_l|
|\widetilde B^{(0)}_{a,l}-B^{(0)}_{a,l}|.
\tag{12}
$$

这些由三角不等式立即得到，并对复输入同样成立。实际运行还需加上两条求值路径各自的乘加/FFT 舍入项。因此“同一有限数学变换”不等于“用原 binary 表定义的算子逐 bit 相同”。本稿没有通过未证明的 libm/FFT 正确舍入假设把 (11)–(12) 变成一个特定数值上界；实际 callback 和 Jacobian 的差由相应运行报告如实给出。

同理，`float128/complex256` 是当前 NumPy/SciPy 平台的类型名称。数值代理实际检查为 `np.finfo(np.longdouble).nmant=63`，即含首位的64位二进有效精度，不能按 IEEE binary128 的112位小数尾数（113位有效精度）解释。保留扩展精度的目标是避免无意降回 binary64，而非宣称获得了四倍精度或全流程严格误差证书。

## 6. 对实际 Frenet 速度的局部误差传递

这里给出一个可直接使用的数学范围，说明小基表差如何传入同一非线性方程。令 $d=X_\psi$、$c=X_{\psi\psi}$，$\lambda=|d|$、$T=d/\lambda$，
$v=(I-TT^T)c$、$n=|v|$、$N=v/n$、$\kappa=n/\lambda^2$。固定背景 $\mu=a'/a$，令 $\alpha=-\mu/\kappa$、$\beta=\sqrt{1-\alpha^2}$，$V=\alpha N+\beta(T\times N)$。

在连接两份实输入 $(d,c)$ 的线段上，若统一有
$\lambda\ge\lambda_*>0$、$n\ge n_*>0$、$|\alpha|\le A<1$、$|c|\le C_*$，并取 $0<b_*\le\sqrt{1-A^2}$，则对 chart 速度 $W=V+b\,d$（同一个已固定平流系数 $b$）有

$$
|\Delta W|\le K_1|\Delta d|+K_2|\Delta c|,
\tag{13}
$$

$$
K_2=\frac{A/b_*+A+1}{n_*},\qquad
K_1=\frac{K_2C_*}{\lambda_*}
 +\frac{2A/b_*+1}{\lambda_*}+|b|.
\tag{14}
$$

证明：$|\delta T|\le|\delta d|/\lambda$。因 $T\cdot\delta T=0$，正交投影的微分 $\delta(TT^T)$ 的算子范数正是 $|\delta T|$，故
$|\delta v|\le|\delta c|+|c||\delta d|/\lambda$。
接着 $|\delta N|\le|\delta v|/n$、
$|\delta\kappa|/\kappa\le|\delta v|/n+2|\delta d|/\lambda$。
由 $N\perp T\times N$ 和 $\delta\beta=-\alpha\delta\alpha/\beta$，
$|\delta\alpha N+\delta\beta(T\times N)|=|\delta\alpha|/\beta$。
其余标架变化至多 $(|\alpha|+\beta)|\delta N|+\beta|\delta T|$。
代入上述界、使用 $\beta\le1$，再加 $|b||\delta d|$ 并沿线段积分，得 (13)–(14)。

此界的正根间隙属于给定输入的条件，不从一次 dtype 检查自动得到。原 profile 与 `geo/frame` 的背景、warp 和正根选择保持不变，故需要比较的是同一函数的求值差。

## 7. 实现适用范围

FFT 快路径应只识别已注册的 Cartesian 圆柱 `B/B1/B2` 及其具体 N；`velocity_s` 和审计可传其他 N，旧 `local_basis` 又采用不同的局部分量约定，不能仅凭形状相似就自动套用。未识别的表仍可使用原求和路径。

在相同 M/N 的有限模型中，合成和投影的主量级从逐节点、逐模式乘加转为每批三个 FFT 及节点旋转，即由 $O(MN)$ 转为 $O(N\log N+M)$。实际加速比例取决于批量、dtype 和下游 Jacobian；应引用实际计时，而非从这个算术量级预言整次 BVP 的墙时。新的高模真正联解、完整 metric 及闭曲面指标仍使用它们自己的实际结果。

## 8. 已完成的实际 callback 比较

实现为 [78718-prefix-long-fourier-transforms.py](../scripts/78718-prefix-long-fourier-transforms.py)，SHA256
`d3b1b13bf8bb7806ce1358cc4314e14e9e5801701c5857deb2b3c38fe2c1385b`。
它仅对新 Flow 实例挂接 `values/project/basis`，用表对象身份识别已注册的具体 N 及阶数；旧局部基、复制表或未知表保留原 fallback。原 `geo/frame`、背景和 warp 代码保持原调用。

实际比较程序为 [78718-prefix-long-fourier-research.py](../scripts/78718-prefix-long-fourier-research.py)，SHA256
`5187ae70cb3306c60fd96bcc6b679e703788eda214a90a9dddc558616591b6d8`。
它读取原 M15 `UNSOLVED` matched-cut warm（SHA256 `cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc`），取32个实际物理 s 点；M22 行是同一保存曲线的零补系数，只用于比较函数调用。每项计时重复5次取中位数，0 BVP、0 DN、0 新曲线。

| M / N | RHS 原 / FFT 秒 | RHS 加速 | `velocity_s` 原 / FFT 秒 | 加速 |
|---|---:|---:|---:|---:|
| 15 / 512 | .05361185 / .01454101 | 3.687 倍 | .09526571 / .02923939 | 3.258 倍 |
| 22 / 1024 | .13303373 / .02711745 | 4.906 倍 | .17329667 / .05410310 | 3.203 倍 |

RHS 最大绝对差分别约 $1.051\cdot10^{-14}$ 和 $9.856\cdot10^{-15}$。
对 $\varepsilon=10^{-25}$ 的 complex-step，方向结果的相对二范数差分别约 $1.806\cdot10^{-15}$、$2.369\cdot10^{-15}$；方向量本身较大，其最大绝对差分别约 $1.83\cdot10^{-12}$、$4.60\cdot10^{-12}$，故这里准确区分绝对与相对误差。
三个阶数 `B/B1/B2` 均实际比较过；原长实输出仍是 `float128`，长复输出仍是 `complex256`，原样本的未知表 fallback 逐字相同。
`B1` 投影在本选定场上接近零，最大绝对差约 $2\cdot10^{-17}$，其相对数可能约1；未用相对数掩盖这一零尺度问题。

这些是此次有限输入的浮点比较，并非所有可能输入的数值误差上界，也没有预言真实高 M 联解的收敛或 metric。相应数学控制的输入范围由第5、6节明确列出。

实际工具回执为 **3b97b5/session34280 → 0ea332 自然 exit0**。报告
[2026-11-10-78718-numerical-prefix-long-fourier-benchmark-01.json](../notes/2026-11-10-78718-numerical-prefix-long-fourier-benchmark-01.json)
为8391 B，SHA256 `ccdc1a2a2ca63eb88d50ee593c7b3fc7ef0acc8cbac2570f783fdd6263bc6db0`。本结果按根 README §13 直接登记，不以另一次重复运行或独立审查为前提。

# 纯乘积张量提升和的核：精确递归与尚未闭合的角度问题

日期：2026-11-12。本文研究的是近邻模型，不是把它当成原 odometer 的对数。负责人：文献/张量子代理；不改变主问题状态。

**2026-11-13 历史对齐。** [R113 主稿](../results/R113-pure-tail-dominance-and-carry-obstructions.md)已经证明纯线性的统一相对尾 $\le1/2$、临界吸收和几何 $(3-\sqrt5)/2$ 范围。root 与 central 已在早期提交 `69d4d5d2a8299f0c93e623fa2d0b5220ef5dbf4c` 核到完全相同主稿 blob `cf5737de87299090f3a5cc3892a2cd1f5f147c33`。本稿 §§12、14 的纯线性部分只算完整复核，不计新增结论；§§13、14 的算子单位版本和纯二次例作为该方法的具体展开保留，不外推实际 carry。R113 两个附录的完整图核反例和单个 carry 无相对图界也继续适用。

## 1. 对象及表示必须分清

令

$$
 H=L^2(\{0,1\}^{\mathbb N},\mu),\qquad
 \mu=\bigotimes_{j\ge0}(\tfrac12,\tfrac12),
$$

并以局部正交基 $e_0=\sqrt2\,1_{\{b=0\}}$、$e_1=\sqrt2\,1_{\{b=1\}}$ 写
$E_j=e_{10}^{(j)}$。无限张量的参考向量是
$+=(e_0+e_1)/\sqrt2=1$，不是有限因子的迹向量。取正数
$\delta_j\in\ell^1$，特别关心

$$
 \delta_j=\frac{2}{(j+2)^2+1}\asymp(j+2)^{-2},\qquad
 B=\sum_{j\ge0}\delta_jE_j.
$$

该级数范数收敛，$E_iE_j=E_jE_i$ 且 $E_j^2=0$。有限首段和幂零，其余和的范数趋零，故 $B$ 拟幂零：对固定首段 $H_m$、尾部 $C_m$，因二者交换且 $H_m^{m+1}=0$，谱移位公式或有限二项展开给 $r(B)\le r(C_m)\le\|C_m\|\to0$。

实际算子是 R43 的

$$
 L=\sum_j[\log(I+N_j)-\log(I+r_jN_j)],
 \quad N_j=A^{2^j}/\|A^{2^j}\|,
$$

其首项接近 $\sum\delta_jE_j$，但
$N_j^2=\eta_jN_{j+1}\ne0$。因此下文利用 $E_j^2=0$ 的精确张量等式不能直接替换成实际 $L$ 的等式。

Tucci 的 *Some quasinilpotent generators of the hyperfinite II$_1$ factor*，arXiv:0708.1968v1，2007-08-14，Theorem 4.4（PDF 印刷页 14）证明几何系数的迹表示模型单射、稠密值域。其决定性步骤是对核投影使用有限因子的忠实归一化迹，得到 $\gamma_n=(\gamma_{n+1}+\gamma_{n-1})/2$，再用 $0\le\gamma_n\le1$。本表示的向量态 $\langle\cdot1,1\rangle$ 不是迹，不能照搬该等式。原文：[arXiv PDF](https://arxiv.org/pdf/0708.1968)。

## 2. 单位拆分与所有广义核的精确图公式

设 $C=\sum_{j\ge1}\delta_jE_j$，$a=\delta_0>0$，按第 0 位的 $e_0,e_1$ 拆分，则

$$
 B=\begin{pmatrix}C&0\\aI&C\end{pmatrix},\qquad
 B^k=\begin{pmatrix}C^k&0\\kaC^{k-1}&C^k\end{pmatrix}.
$$

记 $K_k(C)=\ker C^k$，$K_0(C)=\{0\}$。直接求解两行方程给出

$$
 \ker B^k
 =\{(-Cy/(ka)+z,y):y\in K_{k+1}(C),\ z\in K_{k-1}(C)\}. \tag{2.1}
$$

证明的逆向也明确：若 $(x,y)\in\ker B^k$，第二行乘 $C$ 后由第一行得 $C^{k+1}y=0$；置 $z=x+Cy/(ka)$，第二行即 $C^{k-1}z=0$。反向代入两行即可。

特别地，

$$
 \ker B=\{(-Cy/a,y):y\in\ker C^2\}. \tag{2.2}
$$

因此 $B$ 有非零核当且仅当 $C$ 有非零核，但不能把式 (2.2) 简写为 $\ker B=e_1\otimes\ker C$；$\ker C^2$ 中的一阶广义核也会进入图。

拆掉前 $m$ 位，设 $H_m=\sum_{j<m}\delta_jE_j$、$C_m=\sum_{j\ge m}\delta_jE_j$。因 $H_m$ 与 $C_m$ 交换，若 $Bf=0$，则

$$
 C_m^q f=(-H_m)^qf,\qquad C_m^{m+1}f=0. \tag{2.3}
$$

这正是不能直接用一阶尾核角度证明总核为零的原因：需要控制的广义核阶数随 $m$ 增长。

## 3. 只需排除核中非零均值，但仍须真正证明

**引理。** $\ker B=\{0\}$ 当且仅当 $\ker B\perp1$。

只有反向需要说明。$B$ 与每个 $E_j$ 交换，故 $K=\ker B$ 对每个有限乘积 $E_F=\prod_{j\in F}E_j$ 不变。若 $K\perp1$，则对 $f\in K$，

$$
 \langle f,E_F^*1\rangle=\langle E_Ff,1\rangle=0.
$$

而 $E_F^*1=\prod_{j\in F}1_{\{b_j=0\}}$，这些函数的线性张成包含全部柱集示性函数（对 $b_j=1$ 使用 $1-1_{\{b_j=0\}}$ 展开），在 $H$ 中稠密，所以 $f=0$。

等价地，只须证明 $1\in\overline{\operatorname{Ran}B^*}$。不过这只是目标的精确化，并未自动提供所需逼近向量。

全位互补变换 $Jf((b_j))=f((1-b_j))$ 是本表示内的酉自伴算子，满足 $J1=1$、$JE_jJ=E_j^*$，从而 $JBJ=B^*$。因此本纯模型中单射与稠密值域等价；这里使用的是具体酉对称性，不是有限迹。

## 4. 尾核的均值界，以及强标量化

令 $r_j=(-1)^{b_j}$ 为 Walsh 一阶向量，并记

$$
 s_m=\sum_{j\ge m}\delta_j,\qquad
 q_m^2=\sum_{j\ge m}\delta_j^2.
$$

局部计算给出

$$
 E_j1=(1-r_j)/2,\qquad E_j^*1=(1+r_j)/2,
$$

故

$$
 C_m^*1=\frac{s_m}{2}1+\frac12\sum_{j\ge m}\delta_jr_j. \tag{4.1}
$$

若 $g\in\ker C_m$，与式 (4.1) 取内积并用 Walsh 正交性即得

$$
 |\langle g,1\rangle|\le\frac{q_m}{s_m}\|g\|. \tag{4.2}
$$

对 $\delta_j\sim c j^{-2}$，

$$
 s_m\sim c/m,\qquad q_m^2\sim c^2/(3m^3),
 \qquad q_m/s_m\sim(3m)^{-1/2}. \tag{4.3}
$$

而且

$$
 C_m/s_m\longrightarrow I/2\quad\text{强收敛}. \tag{4.4}
$$

证明：对只依赖前 $M$ 位的柱函数 $h$，当 $m>M$ 时
$C_mh=h\otimes C_m1$，故
$\|(C_m/s_m-I/2)h\|=(q_m/(2s_m))\|h\|\to0$。
又 $\|C_m/s_m\|\le1$，用柱函数的稠密性推广到所有 $h\in H$。

若 $\delta_j$ 单调下降，还有更强的范数上界

$$
 \|C_m\|\le\frac{s_m+\delta_m}{2}. \tag{4.5}
$$

以下给出所需有限维估计的完整证明。$S_n=\sum_{j=1}^nE_j$ 在计算基按 1 的数量分层；从第 $r$ 层到第 $r+1$ 层的矩阵每列有 $n-r$ 个 1、每行有 $r+1$ 个 1。由矩阵 $\ell^1$、$\ell^\infty$ 范数的插值或直接加权 Cauchy–Schwarz，块范数至多 $\sqrt{(n-r)(r+1)}\le(n+1)/2$，故 $\|S_n\|\le(n+1)/2$。现按层分解

$$
 C_m=\sum_{n\ge1}(\delta_{m+n-1}-\delta_{m+n})
       \sum_{j=m}^{m+n-1}E_j.
$$

因为系数非负且
$\sum_{n\ge1}n(\delta_{m+n-1}-\delta_{m+n})=s_m$，该级数绝对范数收敛；三角不等式给出式 (4.5)。结合式 (4.4)，对平方衰减系数有 $\|C_m/s_m\|\to1/2$。

**限制。** 在 $\ker B$ 上，式 (2.3) 只说明这些强趋于 $I/2$ 的尾算子具有越来越高的幂零阶数。均匀有界的幂零算子可以强逼近非零标量；不能仅凭式 (4.4) 和式 (2.3) 得到矛盾。

## 5. 条件期望的精确残差

设 $P_m$ 为前 $m$ 位的条件期望，$f_m=P_mf$。对 $j\ge m$，

$$
 P_mE_jf=\tfrac12P_mf+\tfrac12P_m(r_jf).
$$

因此 $Bf=0$ 蕴含

$$
 (H_m+s_m/2)f_m
 =-\tfrac12\sum_{j\ge m}\delta_jP_m(r_jf). \tag{5.1}
$$

子空间 $\{h\,r_j:h\in P_mH\}$ 随 $j\ge m$ 两两正交，且均正交于 $P_mH$。故 Bessel 不等式和 Cauchy–Schwarz 给出

$$
 \sum_{j\ge m}\|P_m(r_jf)\|^2\le\|f-f_m\|^2,
$$

$$
 \|(H_m+s_m/2)f_m\|
 \le\frac{q_m}{2}\|f-f_m\|. \tag{5.2}
$$

$H_m+s_m/2$ 虽然在有限首段上可逆，其逆范数随 $m$ 可非常大。不能无依据地断言任意 $L^2$ 向量的条件期望误差足以抵消这个增长。

对任意柱函数 $h\in P_mH$ 还有精确范数公式

$$
 \|Bh\|^2
 =\|(H_m+s_m/2)h\|^2+\frac{q_m^2}{4}\|h\|^2. \tag{5.3}
$$

这是因为 $Bh=(H_m+s_m/2)h-\tfrac12h\sum_{j\ge m}\delta_jr_j$，两项正交。它证明每个固定柱空间上有正下界，但该下界 $q_m/2$ 趋零，仍不等于全空间单射证明。

一种可明确检查但失败的逼近是
$g_m=(H_m^*+s_m/2)^{-1}1$，因为

$$
 \|B^*g_m-1\|=(q_m/2)\|g_m\|.
$$

平方系数 $\delta_j=(j+2)^{-2}$ 的有限精确三角解数值显示该残差已经从 $m=10$ 的约 $85.6$ 增长到 $m=20$ 的约 $2.18\times10^6$。这里只把它作为该具体逼近没有给出收敛证据的记录，不用有限数值证明任何无限维否定命题。

## 6. 广义核角度所缺的恰当不等式

记

$$
 \gamma_k(C)=\|P_{K_k(C)}1\|^2,
 \quad V_k=K_k(C)\ominus K_{k-1}(C),
 \quad W_k=K_{k+1}(C)\ominus K_k(C).
$$

令

$$
 T_k=P_{V_k}C|_{W_k},\qquad
 v_k=P_{V_k}1,\quad w_k=P_{W_k}1,
 \qquad t=(ka)^{-1}.
$$

由于 $C K_k\subset K_{k-1}$，式 (2.1) 经正交拆分，成为第一分量的 $K_{k-1}$、第二分量的 $K_k$，以及图
$\{(-tT_ky,y):y\in W_k\}$ 的正交直和。标准图投影计算因此给出精确式

$$
 \gamma_k(aE_0+C)=\frac12\gamma_{k-1}(C)
 +\frac12\gamma_k(C)
 +\frac12\left\|(I+t^2T_k^*T_k)^{-1/2}
             (w_k-tT_k^*v_k)\right\|^2. \tag{6.1}
$$

这里 $1$ 在第 0 位的两分量都是尾部常数向量除以 $\sqrt2$。图的参数映射 $y\mapsto(-tT_ky,y)$ 的 Gram 算子为 $I+t^2T_k^*T_k$，故式 (6.1) 不使用有限维或有限迹。

特别地，当 $a\to\infty$ 时，

$$
 \gamma_k(aE_0+C)\to
 \frac12(\gamma_{k+1}(C)+\gamma_{k-1}(C)). \tag{6.2}
$$

若能对实际各尾部证明

$$
 \left\|(I+t^2T_k^*T_k)^{-1/2}
 (w_k-tT_k^*v_k)\right\|\le\|w_k\|, \tag{6.3}
$$

就有

$$
 \gamma_k(aE_0+C)\le
 \tfrac12(\gamma_{k+1}(C)+\gamma_{k-1}(C)). \tag{6.4}
$$

依次拆前 $m$ 位，并以 $\gamma_0=0$、$0\le\gamma_k\le1$ 结束，右边将被从位置 $k$ 出发、在 0 吸收的对称简单随机游走存活 $m$ 步的概率控制。对固定 $k$ 该概率趋零（反射原理或二项式公式），因而足以证明 $\gamma_1(B)=0$，再由第 3 节得 $\ker B=0$。

**尚未证明的是式 (6.3)，不是随机游走步骤。** 数值试验提示对有限正系数张量和、且新拆系数 $a$ 不小于其余单个系数时可能成立；它不能对任意正 $a$ 无条件使用。例如 3 位有限和，取 $a=1$、两个尾系数均为 $5$、$k=2$。$B^2$ 从一阶计算层到三阶层的行向量正比于 $(5,1,1)$，所以该层常数的核投影平方范数为 $3-49/27=32/27$，二、三阶层的总贡献为 $4$，零阶贡献为 $0$。故 $\gamma_2(B)=(4+32/27)/8=35/54$；尾部等权两位和满足 $\gamma_3(C)=1$、$\gamma_1(C)=1/4$，式 (6.4) 右侧为 $5/8$。差值为 $5/216>0$，所以无最大系数条件的版本为假。即使有限维最大系数版本得到证明，还须证明相应无限尾部版本或有一致近零谱控制；范数收敛不能自动交换核投影。

## 7. 有限截断核与计算的限度

对 $B_m=\sum_{j<m}\delta_jE_j$，计算基按集合 $S\subset\{0,\ldots,m-1\}$ 标记。第 $r$ 层到第 $r+1$ 层的块为

$$
 X_r[U,V]=
 \begin{cases}\delta_j,&U=V\cup\{j\},\\0,&\text{其他。}\end{cases}
$$

于是

$$
 \|P_{\ker B_m}1\|^2
 =2^{-m}\sum_{r=0}^m\|P_{\ker X_r}\mathbf1_r\|^2. \tag{7.1}
$$

更高幂块也有完全显式的矩阵：若 $|U|-|V|=k$，则
$B_m^k[U,V]=k!\prod_{j\in U\setminus V}\delta_j$ 当 $V\subset U$，其余为零。这避免把浮点 SVD 的近零奇异值误当成无限维核。

作为探索记录，$\delta_j=(j+2)^{-2}$ 时，式 (7.1) 的数值依次为：

| $m$ | $\|P_{\ker B_m}1\|^2$ |
|---:|---:|
| 1 | 0.5000000000 |
| 2 | 0.3144329897 |
| 3 | 0.2151714636 |
| 4 | 0.1574732893 |
| 5 | 0.1193894628 |
| 6 | 0.0929733339 |
| 7 | 0.0737283386 |
| 8 | 0.0593026742 |
| 9 | 0.0482213973 |

等权情形可精确求出 $\|P_{\ker B_m}1\|^2=2^{-m}$：常数参考向量属于完全对称张量子空间，$B_m$ 在其中是单一长度 $m+1$ 的提升链，其核是计算基的全 1 向量。一般正权时不能套用这个等式。

上述有限核角度下降，不足以推出无限 $B$ 的核为零。$B_m\to B$ 为范数收敛，但核投影在 0 不连续；实际核向量的前段切片只给式 (2.3) 的尾部广义核。

## 8. 连续函数类可排除，但不是一般 $L^2$ 结论

**命题。** 若每个 $\delta_j>0$，则 $\ker B\cap C(\{0,1\}^{\mathbb N})=\{0\}$。

证明：$B$ 保持连续函数，因级数一致收敛，且

$$
 (Bf)(b)=\sum_j\delta_jb_jf(b\text{ 的第 }j\text{ 位改为 }0).
$$

若 $Bf=0$ 几乎处处，则连续性和乘积测度的全支撑给出处处为零。在只有有限个 1 的点 $1_S$ 上，方程为

$$
 \sum_{j\in S}\delta_j f(1_{S\setminus\{j\}})=0. \tag{8.1}
$$

固定 $r\ge0$，取任意含所考察 $r$ 元集合的有限坐标集 $F$，并增大到 $|F|>2r$。式 (8.1) 说明第 $r$ 层函数属于这个有限 Boolean 提升矩阵的核。该矩阵在 $r<|F|/2$ 时单射：先用可逆对角矩阵 $D e_S=(\prod_{j\in S}\delta_j)e_S$ 化为等权提升 $U$；等权下降 $U^*$ 满足第 $r$ 层的交换关系

$$
 U^*U-UU^*=(|F|-2r)I.
$$

于是 $Ug=0$ 时 $0=\|U^*g\|^2+(|F|-2r)\|g\|^2$，故 $g=0$。因此 $f(1_S)=0$ 对所有有限 $S$ 成立。这些点在乘积拓扑中稠密，连续性推出 $f=0$。

本论证取了特定点的值；不能对任意 $L^2$ 等价类直接使用。实际 $L$ 的连续核排除已由 R43 完成，因此本节不是新的实际核结论。

## 9. 有限迹表示的递推可推广到任意非零可和系数

本节给出一个确实闭合、但仍属于有限迹表示的结论。取抽象二进制 UHF 代数的归一化迹 $\tau$，在其迹 GNS 表示的有限因子中考虑同一范数收敛元素 $B$。假设所有 $\delta_j\ne0$；本节不要求正实数或几何系数。

对第 $m$ 个尾因子记

$$
 \alpha_{m,k}=\tau_m(P_{\ker C_m^k}),\qquad
 \alpha_{m,0}=0.
$$

式 (2.1) 仍成立。该闭图子空间与
$K_{k-1}(C_{m+1})\oplus K_{k+1}(C_{m+1})$ 有有界、可逆的参数对应；其参数算子的极分解给出因子内两个投影的 Murray–von Neumann 等价。因此归一化迹满足

$$
 \alpha_{m,k}=\frac12\bigl(\alpha_{m+1,k-1}
                      +\alpha_{m+1,k+1}\bigr),\qquad k\ge1. \tag{9.1}
$$

这里系数 $k\delta_m$ 仅改变图，不改变图投影的迹。也可由第 6 节的正交图拆分直接验证：图投影与其参数空间投影等价，而第一位的归一化迹提供因子 $1/2$。

将式 (9.1) 迭代 $n$ 次，令 $S_n$ 为从 $k\ge1$ 出发、到达 0 即吸收的简单对称随机游走，得到

$$
 0\le\alpha_{0,k}
 =\mathbb E_k[\alpha_{n,S_n};\ \tau_0>n]
 \le\mathbb P_k(\tau_0>n). \tag{9.2}
$$

右边趋零。例如反射原理将未吸收的位置概率写成两个相差 $2k$ 的二项式概率之差，求和后只余至多 $2k$ 个中间二项式项，每项 $O(n^{-1/2})$。因此 $\alpha_{0,k}=0$。忠实性给 $\ker B^k=0$，特别 $\ker B=0$；有限因子的极分解又给 $\tau(P_{\ker B^*})=\tau(P_{\ker B})=0$，故值域稠密。

这把 Tucci Theorem 4.4 的几何自相似递推改成了逐尾部递推。但它仍不证明第 1 节的纯乘积表示中零核：抽象同一 C* 元素在不同表示中的 0 特征投影可以不同。

## 10. 一个足以合法跨表示的有限矩阵不等式

以下是尚未证明的具体有限维不等式，不登记为结论。对正权有限提升和 $B_m$，令 $\omega_m(X)=\langle X1,1\rangle$、$\tau_m(X)=2^{-m}\operatorname{Tr}X$。考虑

$$
 \omega_m\!\left(\frac{\varepsilon}{B_m^*B_m+\varepsilon I}\right)
 \le
 \tau_m\!\left(\frac{\varepsilon}{B_m^*B_m+\varepsilon I}\right),
 \qquad\varepsilon>0. \tag{10.1}
$$

**条件命题。** 若式 (10.1) 对所有有限正系数张量和成立，则所有全正非零可和系数的纯乘积模型 $B$ 单射。

证明：先固定 $\varepsilon>0$，因 $B_m\to B$ 范数收敛，连续函数演算给两侧正则化逆的范数收敛。因此式 (10.1) 先传到抽象 UHF 元素上的两个连续状态 $\omega_+$ 和 $\tau$。再令 $\varepsilon\downarrow0$，各自表示中的谱定理给

$$
 \|P_{\ker B\text{（纯表示）}}1\|^2
 \le \tau(P_{\ker B\text{（迹表示）}})=0,
$$

最后用第 3 节的均值判据。这里的极限次序合法，因为在取核投影以前已经固定正则化参数并使用范数连续性。

有限正权 Boolean 提升块的数值探索没有发现式 (10.1) 的反例（至 9 位；不同正系数和正则化参数），但数值不是证明。一般非负矩阵没有这种状态比较：例如两个正行向量 $(1,\epsilon,0)$、$(1,0,\epsilon)$ 的 Gram 矩阵，其核方向正比于 $(-\epsilon,1,1)$；当 $\epsilon>0$ 很小时，该核的全 1 向量投影平方范数大于核维数。因此不能仅凭矩阵条目非负就断言式 (10.1)，必须使用完整 Boolean 提升矩阵的特殊结构。

还检查了真实压缩二次型而非 $B_m$ 自身的核。由式 (5.3)，

$$
 P_mB^*BP_m=(H_m+s_m/2)^*(H_m+s_m/2)+q_m^2I/4.
$$

对 $\delta_j=(j+2)^{-2}$，在 $\varepsilon=q_m^2/4$ 时，有限柱空间内计算的
$\varepsilon\langle(P_mB^*BP_m+\varepsilon)^{-1}1,1\rangle$
从 $m=2$ 的约 $0.03064$ 降到 $m=16$ 的约 $0.003689$。这没有产生可用于构造非零核的正下界，也不能单凭该沿对角线的数值下降判定极限核为零：一般核向量的柱逼近速度可能慢于所选 $\varepsilon$ 尺度。

## 11. 当前缺口与可搬运部分

对于第 1 节所关心的一般正可和、特别平方尾系数，本文前 11 节没有证明纯模型 $B$ 在全 $L^2$ 上单射，也没有构造其非零核向量。下节复核 R113 已覆盖的相对尾子类，并展开算子单位版本；两者均未决定实际 $L$、$D$ 或 $A$ 的普通不变子空间。

已严格得到的工具是：全部广义核的 Schur 图、均值判据、尾部一阶角度、强标量化及尖锐量级范数界、条件期望残差、广义核角度的精确算子公式，以及迹表示任意非零可和系数的逐尾部零核证明。需要继续推进的具体缺口为式 (6.3)、式 (10.1)，或者从式 (5.1) 推出足以控制有限首段逆增长的真实核正则性。

这些结果转到实际 $L$ 时须重新计算所有进位项；特别是式 (2.1)、式 (2.3) 中的有限首段幂零、以及第 3 节对所有局部 $E_j$ 的交换性，在实际 $L$ 中都没有未经证明的精确对应。

## 12. 复核一个较弱充分条件：可和相对尾与广义核随机游走

2026-11-13 补充；作者 Astra-ISP-0c017065，AI-assisted，GPT-6 Astra Pro。

本节继续使用第 1 节的纯乘积 Haar 表示，参考向量为每位的
$(e_0+e_1)/\sqrt2$。证明不使用有限因子迹，也不删除实际模型的 carry；
结论仅针对这里明确给出的纯张量算子。

### 12.1 定理及量词

允许非零复系数 $a_j$，假设
$$
\sum_{j\ge0}|a_j|<\infty,\qquad a_j\ne0.
$$
在第 $j$ 位起始的尾部 Haar 空间 $H_j$ 上定义
$$
C_j=\sum_{i\ge j}a_iE_i,\qquad
\varepsilon_j=\frac{\|C_{j+1}\|}{|a_j|}.
$$
其中 $C_{j+1}$ 在 $H_j=\mathbb C^2\otimes H_{j+1}$ 上张量恒等。
假设
$$
\boxed{\sum_{j\ge0}\varepsilon_j<\infty.}
\tag{12.1}
$$
一个只依赖系数的充分条件是
$$
\sum_{j\ge0}\frac{\sum_{i>j}|a_i|}{|a_j|}<\infty.
\tag{12.2}
$$

**结论。** 对每个 $j\ge0$ 和每个固定整数 $k\ge1$，
$C_j^k$ 单射且值域稠密。这里不声称其在任意未知不变子空间内都有稠密值域。

### 12.2 保持原参考向量的图角度上界

记
$$
K_{j,k}=\ker C_j^k,\quad K_{j,0}=0,\qquad
\gamma_{j,k}=\|P_{K_{j,k}}\Omega_j\|^2,\quad \gamma_{j,0}=0.
$$
所有 $0\le\gamma_{j,k}\le1$。

固定 $j,k$，令 $C=C_{j+1}$、$a=a_j$，并写
$$
E=\ker C^{k+1},\quad F=\ker C^{k-1},\qquad
A=\frac1{ka}(I-P_F)C|_E.
$$
由 $CE\subset\ker C^k$ 以及 $F\subset\ker C^k\subset E$，
$$
\operatorname{Ran}A\subset \ker C^k\ominus F\subset E,
\qquad \|A\|\le\varepsilon_j/k.
\tag{12.3}
$$
这里 $E,F$ 均为闭子空间，不需要 $C$ 的值域闭合。

第 2 节的准确两行核公式，吸收 $Cy/(ka)$ 的 $F$ 分量以后，给出
$$
\boxed{
K_{j,k}=\{(-Ay+z,y):y\in E,\ z\in F\}.
}
\tag{12.4}
$$
且 $Ay\perp z$，所以
$$
\|(-Ay+z,y)\|^2
=\|y\|^2+\|Ay\|^2+\|z\|^2
\ge\|y\|^2+\|z\|^2.
\tag{12.5}
$$

原参考向量的两个分量确实相同：
$\Omega_j=(\Omega_{j+1},\Omega_{j+1})/\sqrt2$。
因此，对 (12.4) 中的向量配对并用 (12.5)，其在核上的投影平方范数满足
$$
\gamma_{j,k}
\le\frac12
\left(\|P_E\Omega_{j+1}-A^*\Omega_{j+1}\|^2
+\|P_F\Omega_{j+1}\|^2\right).
\tag{12.6}
$$
在此式中 $A:E\to H_{j+1}$，所以 $A^*$ 的值已在 $E$。
又由 $\operatorname{Ran}A\subset E$ 得
$A^*\Omega_{j+1}=A^*P_E\Omega_{j+1}$，故
$$
\boxed{
\gamma_{j,k}
\le\frac12\left[
(1+\varepsilon_j/k)^2\gamma_{j+1,k+1}
+\gamma_{j+1,k-1}\right]
\le(1+\varepsilon_j)^2
\frac{\gamma_{j+1,k+1}+\gamma_{j+1,k-1}}2.
}
\tag{12.7}
$$

这不是第 6 节尚未证明的无损角度不等式 (6.3)。
本节完整保留每一步的乘法损失，靠 (12.1) 支付其无限乘积。

### 12.3 吸收游走与真正零核

令 $S_N$ 为从 $k\ge1$ 出发、在 0 吸收的对称简单随机游走，
$\tau_0$ 为首次到 0 的时间。将 (12.7) 逐尾部迭代 $N$ 次，
并在 0 使用 $\gamma_{j,0}=0$，得到
$$
\begin{aligned}
0\le\gamma_{j,k}
&\le
\prod_{r=j}^{j+N-1}(1+\varepsilon_r)^2\,
\mathbb E_k[
\gamma_{j+N,S_N};\ \tau_0>N]\\
&\le
\exp\!\left(2\sum_{r\ge j}\varepsilon_r\right)
\mathbb P_k(\tau_0>N).
\end{aligned}
\tag{12.8}
$$
前面的常数有限且与 $N$ 无关。

为完整说明最后的极限，固定整数 $L>k$。游走在有限区间
$\{0,\ldots,L\}$ 内几乎必然到达某个端点：
每连续 $L$ 步都有至少 $2^{-L}$ 的条件概率达到端点。
到达 $L$ 先于 0 的概率由有限差分方程
$p_i=(p_{i-1}+p_{i+1})/2$、$p_0=0,p_L=1$
准确为 $k/L$。所以永不到 0 的概率至多 $k/L$；
让 $L\to\infty$，即得
$\mathbb P_k(\tau_0>N)\to0$。
由 (12.8)，
$$
\boxed{\gamma_{j,k}=0\quad(j\ge0,\ k\ge1).}
\tag{12.9}
$$

还需把真空角度零转为完整零核，而不是停在一列。
$C_j^k$ 与每个尾部有限乘积 $E_F$ 交换。
若 $f\in K_{j,k}$，则 $E_Ff\in K_{j,k}$，故
$$
\langle f,E_F^*\Omega_j\rangle
=\langle E_Ff,\Omega_j\rangle=0.
$$
这些 $E_F^*\Omega_j$ 的线性张成包含所有尾部柱函数，因而稠密。
所以 $f=0$。

最后令 $J$ 为所有尾位互补的酉算子，$K$ 为逐点复共轭，
$\mathcal C=JK$ 为反酉对合。则
$$
\mathcal C C_j\mathcal C=C_j^*.
$$
单射性遂给 $\ker(C_j^*)^k=0$，等价于 $C_j^k$ 值域稠密。
这一步对复系数同样有效，不使用有限迹。

### 12.4 明确覆盖的系数与仍未覆盖的模型

若
$$
a_j=e^{-\beta j^\alpha},\qquad \beta>0,\quad\alpha>1,
$$
则对充分大的 $j$，凸性给
$$
\frac{\sum_{i>j}a_i}{a_j}
\le
\frac{
e^{-\beta((j+1)^\alpha-j^\alpha)}
}{
1-e^{-\beta\alpha(j+1)^{\alpha-1}}
}
\le C_{\alpha,\beta}e^{-\beta\alpha j^{\alpha-1}}.
\tag{12.10}
$$
最后一项可和，故满足 (12.2)。
任意复相位不会改变这个充分条件。

这个相对尾可和子类已经被 R113 的更强主定理覆盖；此处只补完整乘法损失的直接验证。
平方尾 $a_j\asymp j^{-2}$ 的相对尾量级为 $j$，不满足本条件；
几何系数的相对尾也不趋零，本节的可和论证不覆盖它们；第 14 节另付其中一部分。
更一般的原 (6.3)、(10.1) 仍未证明。

本节不能直接用于实际 $N_j=E_j+\eta_jE_j^*N_{j+1}$：
carry 使第一位不再具有 (12.4) 的精确两行核图，
且实际核不自动对全部纯 $E_F$ 不变。
对联合二次行，第一位非对角块也不再是标量 $a_jI$；
若改用算子单位 $B_j$，必须另付
$B_j^{-1}C_{j+1}$ 在相应广义核上的真实费用。
因此没有由本节推出原迟首二次核、边界 $N=M$ 或普通 ISP 的结论。

## 13. 同一 Haar 图论证的算子非对角块版本

2026-11-13 同次补充；本节仍只处理准确纯张量拆分。

### 13.1 逐尾部的算子单位准则

设尾部算子族 $T_j$ 在原 Haar 张量分解中准确满足
$$
T_j=
\begin{pmatrix}
T_{j+1}&0\\
V_j&T_{j+1}
\end{pmatrix},
\tag{13.1}
$$
其中 $V_j$ 有界可逆且与 $T_{j+1}$ 交换。
还假设每个 $T_j$ 与所有其尾位上的 $E_i$ 交换。
若从某个 $J$ 起
$$
\boxed{
\sum_{j\ge J}\|V_j^{-1}T_{j+1}\|<\infty,
}
\tag{13.2}
$$
则 $T_J$ 单射；对所有 $j<J$，若 (13.1) 仍成立，即使这些早期
$V_j$ 不可逆，也有 $T_j$ 单射。

证明完全保持算子次序。置 $U=T_{j+1}$。
交换性给
$$
T_j^k=
\begin{pmatrix}
U^k&0\\
kV_jU^{k-1}&U^k
\end{pmatrix},
$$
并且
$$
\ker T_j^k
=
\{(-k^{-1}V_j^{-1}Uy+z,y):
y\in\ker U^{k+1},\ z\in\ker U^{k-1}\}.
\tag{13.3}
$$
逆向求解时，先由第二行再作用 $U$ 得 $U^{k+1}y=0$，
然后用 $V_j^{-1}$ 解出
$x+k^{-1}V_j^{-1}Uy\in\ker U^{k-1}$。
所有交换步骤都在同一个尾部空间进行。

令 $E=\ker U^{k+1}$、$F=\ker U^{k-1}$，
$$
A=k^{-1}(I-P_F)V_j^{-1}U|_E.
$$
由于 $V_j^{-1}$ 与 $U$ 交换，
$$
\operatorname{Ran}A\subset\ker U^k\ominus F\subset E,\qquad
\|A\|\le k^{-1}\|V_j^{-1}U\|.
$$
因此第 12 节的投影估计和吸收游走逐字适用，
给每个 $k$ 的真空核角度为零。
与所有 $E_i$ 的交换性及原真空伴随循环性给 $\ker T_J^k=0$。

对早期有限个头，若 $U$ 单射，则 (13.1) 的第一行迫 $x=0$，
第二行再迫 $y=0$，不需要 $V_j$ 可逆。
这证明结论。若相应族另满足原反酉对称
$\mathcal C T_j\mathcal C=T_j^*$，则也有稠密值域。

### 13.2 一个明确的纯二次范围

定义真正的纯提升和
$$
P_{a,j}=\sum_{i\ge j}a_iE_i,\qquad
P_{c,j}=\sum_{i\ge j}c_iE_i,\qquad
T_j=4P_{a,j}^2-2P_{c,j},
\tag{13.4}
$$
其中
$$
a_i=e^{-\beta i^\alpha},\quad
c_i=a_i^\kappa\mathbf1_{i>j_0},\qquad
\alpha>1,\ \beta>0,\ 0<\kappa\le2.
\tag{13.5}
$$
因为 $E_j^2=0$，准确第一位拆分为 (13.1)，其中
$$
\boxed{V_j=8a_jP_{a,j+1}-2c_jI.}
\tag{13.6}
$$
这个式子不含实际 carry，也不将实际 $Q_j^2$ 当成零。

对充分大的 $j>j_0$，记
$$
A_j=\sum_{i>j}a_i,\qquad C_j^{\rm coef}=\sum_{i>j}a_i^\kappa.
$$
由 (12.10) 及其 $\kappa\beta$ 版本，
$$
A_j/a_j\le C e^{-\beta\alpha j^{\alpha-1}},
\qquad
C_j^{\rm coef}/a_j^\kappa
\le C_\kappa e^{-\kappa\beta\alpha j^{\alpha-1}}.
\tag{13.7}
$$
由于 $a_j\le1$ 且 $2-\kappa\ge0$，
$$
\frac{4a_j\|P_{a,j+1}\|}{c_j}
\le4a_j^{2-\kappa}(A_j/a_j)\longrightarrow0.
$$
从而充分大 $j$ 时，(13.6) 中的标量主项可用范数 Neumann 级数，
得到
$$
\|V_j^{-1}\|\le c_j^{-1}.
\tag{13.8}
$$
于是
$$
\begin{aligned}
\|V_j^{-1}T_{j+1}\|
&\le
\frac{4A_j^2+2C_j^{\rm coef}}{a_j^\kappa}\\
&=
4a_j^{2-\kappa}(A_j/a_j)^2
+2C_j^{\rm coef}/a_j^\kappa .
\end{aligned}
\tag{13.9}
$$
右侧由 (13.7) 可和，(13.2) 得证。
每个 $T_j$ 与全部纯尾位 $E_i$ 交换；原反酉对称也保持 (13.4)。
因此这里的纯二次 $T_0$ 单射且值域稠密，全部固定正整数幂同样如此。
最初 $c_j=0$ 的有限个位置仅使用 §13.1 的三角回传，不伪造其单位逆。

当 $\kappa>2$ 时，(13.8) 的标量主导估计不再由上述条件保证；
$V_j^{-1}T_{j+1}$ 的实际费用需要重新证明。
本节的图预算没有证明这一更危险范围；后续 §15 改用精确局部幂零导子，已将纯模型范围补全。仍不把纯结论搬到原实际
$X^2-B_0+Y$。第 12 节末尾关于 carry、核图和未知限制的界限继续保留。

## 14. R113 吸收链的复核及算子单位表述

本节完整复核 R113 的准确正交图和吸收链，并在第 13 节的算子单位形式下保留同一证明。纯线性范围不是本轮新增结论。

### 14.1 准则

对第 12 节的纯线性族，只需存在 $J$ 和一个固定数
$0\le\varepsilon\le1/2$，使
$$
\|C_{j+1}\|/|a_j|\le\varepsilon\qquad(j\ge J).
\tag{14.1}
$$
则所有 $C_j$ 单射且值域稠密。

对第 13 节的准确三角族，同样可以把 (13.2) 替换成
$$
\|V_j^{-1}T_{j+1}\|\le\varepsilon\le1/2
\qquad(j\ge J).
\tag{14.2}
$$
其余假设保持：晚期 $V_j$ 是与 $T_{j+1}$ 交换的有界单位，
每个 $T_j$ 与全部尾位 $E_i$ 交换；
早期有限个非对角块只需保持原三角式。
结论为全部 $T_j$ 单射；稠密值域仍按原反酉对称假设取得。
$1/2$ 包括在已证范围内，不声称这个阈值对算子族必要或最优。

### 14.2 相邻核质量给真正的概率转移

采用第 13 节符号；纯线性情形就是 $V_j=a_jI$。
固定 $j,k$，令
$$
U=T_{j+1},\quad F=\ker U^{k-1},\quad G=\ker U^k,\quad
E=\ker U^{k+1},
$$
$$
V=G\ominus F,\quad W=E\ominus G,\qquad
A=k^{-1}(I-P_F)V_j^{-1}U|_E.
$$
因 $V_j^{-1}$ 与 $U$ 交换，
$A|_G=0$、$\operatorname{Ran}A\subset V$，且
$$
\|A|_W\|\le\varepsilon/k.
\tag{14.3}
$$
故核图分成三个正交部分：
第一分量的 $F$、第二分量的 $G$，以及
$\{(-Ay,y):y\in W\}$。

记 $\gamma_k=\|P_{\ker U^k}\Omega_{j+1}\|^2$，
$\Delta_k=\gamma_k-\gamma_{k-1}\ge0$，
$v=P_V\Omega_{j+1}$、$w=P_W\Omega_{j+1}$。
真实图投影的 Gram 矩阵是 $I_W+A^*A$，于是
$$
\gamma_{j,k}
=\frac{\gamma_{k-1}+\gamma_k}{2}
+\frac12\left\|
(I_W+A^*A)^{-1/2}(w-A^*v)
\right\|^2.
\tag{14.4}
$$
此处 $A^*$ 按 $A:W\to V$ 理解；
没有把完整图中的别的分量藏进这个记号。

由 $(I+A^*A)^{-1/2}$ 为收缩、(14.3) 及
$2\sqrt{\Delta_k\Delta_{k+1}}\le\Delta_k+\Delta_{k+1}$，
$$
\begin{aligned}
\gamma_{j,k}
&\le
\frac{\gamma_{k+1}+\gamma_{k-1}}2
+\frac{\varepsilon}{k}
 \sqrt{\Delta_k\Delta_{k+1}}
+\frac{\varepsilon^2}{2k^2}\Delta_k\\
&\le
p_+(k)\gamma_{k+1}
+p_0(k)\gamma_k
+p_-(k)\gamma_{k-1},
\end{aligned}
\tag{14.5}
$$
其中
$$
\boxed{
p_+(k)=\frac12+\frac{\varepsilon}{2k},\quad
p_0(k)=\frac{\varepsilon^2}{2k^2},\quad
p_-(k)=\frac12-\frac{\varepsilon}{2k}
                     -\frac{\varepsilon^2}{2k^2}.
}
\tag{14.6}
$$
三者之和准确为 1。
对 $k\ge1$ 和 $0\le\varepsilon\le1/2$，
$p_-(k)\ge1/8$，其余两者也非负。
因此 (14.5) 给真正的概率转移，不再积累第 12 节的逐步乘法损失。
在 0 令链吸收，并仍使用 $\gamma_{j,0}=0$。

### 14.3 包括端点的吸收证明

令 $\mathsf P$ 为 (14.6) 定义的齐次 Markov 转移矩阵。
系数 $\varepsilon$ 对所有 $j\ge J$ 固定，
所以 (14.5) 逐步迭代给
$$
0\le\gamma_{j,k}
\le(\mathsf P^N\gamma_{j+N,\cdot})(k)
\le\mathbb P_k(\tau_0>N).
\tag{14.7}
$$

下面证明右侧趋零，包括 $\varepsilon=1/2$。
置
$$
r_0=1,\qquad
r_n=\prod_{k=1}^n\frac{p_-(k)}{p_+(k)}.
$$
对大 $k$，
$$
\log\frac{p_-(k)}{p_+(k)}
=
\log\frac{1-\varepsilon/k-\varepsilon^2/k^2}
          {1+\varepsilon/k}
=-\frac{2\varepsilon}{k}+O(k^{-2}).
$$
所有早期因子均严格为正，故存在常数 $c,C>0$，使
$$
c(n+1)^{-2\varepsilon}\le r_n
\le C(n+1)^{-2\varepsilon}.
\tag{14.8}
$$
当 $2\varepsilon\le1$ 时，
$\sum_{n\ge0}r_n=\infty$。

固定 $L>k$。链在有限区间内几乎必然达到端点：
连续向下的 $L$ 步已有至少 $8^{-L}$ 的条件概率到达 0。
在到达 0 以前先到 $L$ 的概率解有限差分方程；保持项消去后，
相邻差满足
$d_{i+1}=(p_-(i)/p_+(i))d_i$。
由端点条件准确得到
$$
\mathbb P_k(\tau_L<\tau_0)
=
\frac{\sum_{i=0}^{k-1}r_i}
     {\sum_{i=0}^{L-1}r_i}
\longrightarrow0\qquad(L\to\infty).
\tag{14.9}
$$
若链永不到 0，则它必在到 0 之前到达每个有限的 $L$；
因此 (14.9) 迫该事件概率为零。
由 (14.7)，所有 $j\ge J,k\ge1$ 的真空核角度都为零。

随后仍按第 12、13 节使用 $E_F$ 的伴随循环性、
早期有限三角回传和原反酉对称，得到上述完整结论。
没有从有限矩阵核投影的范数连续性取极限，也没有使用迹维数。

### 14.4 R113 已覆盖的几何纯线性行及范围

第 12 节的可和条件当然保证晚期 (14.1)，
但 (14.1) 还允许相对尾不趋零。

例如正几何行 $a_j=r^j$、$0<r<1$。
第 4 节已经证明的单调系数范数上界给
$$
\frac{\|C_{j+1}\|}{a_j}
\le
\frac{r(2-r)}{2(1-r)}.
$$
因此
$$
\boxed{
0<r\le\frac{3-\sqrt5}{2}
}
\tag{14.10}
$$
都满足 (14.1)，其纯 Haar 提升和单射且值域稠密。
这是在当前纯乘积参考向量上直接得到的结论，
没有把 Tucci 的有限迹结论转移到这个表示。

第 13 节的超指数纯二次子类继续成立；
更一般的算子单位族可直接检查 (14.2)。
原平方尾、其余几何比率及 $\kappa>2$ 的纯二次不由本节的相对尾准则处理；后续 §15 已另行关闭全部可和纯线性/纯二次范围。实际 carry 模型及实际迟首二次仍开。

## 15. 纯模型的单位偏导、局部幂零导子与全可和行排核

2026-11-13 新补充。作者：normal_complex；central_review 独立核验主证明。只在原 Haar plus 纯乘积表示中工作。本节不删除实际算子中的进位，也不把纯结论运输到实际 $X^2-B_0+Y$。

### 15.1 与已有结论的扣重及准确结论

[R113](../results/R113-pure-tail-dominance-and-carry-obstructions.md) 已证明晚期相对尾范数不超过 $1/2$ 的纯线性范围，包含所列几何比率；本笔记 §12、§14 对该范围只是同步复核。§13 的算子单位图法需要另付
$\|V_j^{-1}T_{j+1}\|$，其纯二次例只处理 $0<\kappa\le2$。

以下改用两个同时成立的纯模型事实：每个固定有限头测试被充分高阶导子精确杀死；无穷多个位上的单位偏导给任意固定阶的强导子单位。所用逆的范数可以很大，因为其乘到的局部余项准确为零。没有把这些逆的费用声明为可供实际迁移的预算。

令
$$
H=L^2(\{0,1\}^{\mathbb N},\mu),\qquad
\Omega=1,\qquad
E_j=|e_1\rangle\langle e_0|_j,
$$
其中 $\mu$ 为等权乘积测度，局部参考向量为
$\Omega_+=(e_0+e_1)/\sqrt2$。所以
$$
E_j^2=0,\qquad [E_i,E_j]=0,\qquad \|E_j\|=1.
$$
系数可以任意复数，不要求按大小重排后与物理位一致。

**定理。**

1. 若 $a\in\ell^1(\mathbb C)$ 有无穷多个非零项，则
   $P_a=\sum_j a_jE_j$ 单射且值域稠密。
2. 若 $a,c\in\ell^1(\mathbb C)$，且 $c$ 有无穷多个非零项，则
   $T=4P_a^2-2P_c$ 单射且值域稠密。
3. 若 $c$ 仅有有限个非零项而 $a$ 有无穷多个非零项，第二个结论仍成立。

以上算子的全部正整数幂也单射且值域稠密。特别，§13 的
$a_j=e^{-\beta j^\alpha}$、$c_j=a_j^\kappa\mathbf1_{j>j_0}$ 在所有
$\alpha,\beta,\kappa>0$ 下满足本定理，不再要求 $\kappa\le2$ 或 $\alpha>1$。

### 15.2 有界纯尾和拟幂零，单位逆合法

每个纯提升和 $P_a$ 都由 $\ell^1$ 假设在算子范数中收敛。任取有限头，写
$$
P_a=H_m+R_m,\qquad
H_m=\sum_{j<m}a_jE_j,\qquad
R_m=\sum_{j\ge m}a_jE_j.
$$
$H_m^{m+1}=0$，且 $H_m$ 与 $R_m$ 交换。若 $|\lambda|>\|R_m\|$，则
$R_m-\lambda I$ 可逆，而
$$
P_a-\lambda I
=(R_m-\lambda I)
\left[I+(R_m-\lambda I)^{-1}H_m\right]
$$
的第二因子是恒等加一个幂零算子，故也可逆。因此
$$
\sigma(P_a)\subseteq\{|\lambda|\le\|R_m\|\}
$$
对所有 $m$ 成立。由 $\|R_m\|\to0$ 得 $\sigma(P_a)=\{0\}$。
同一论证适用于删除任意一个或有限多个位后的和。

固定一个满足 $c_j\ne0$ 的位置。写
$$
P_a=a_jE_j+P_{a,\ne j},\qquad
P_c=c_jE_j+P_{c,\ne j}.
$$
纯平方零给准确分解
$$
T=T_{\ne j}+E_jV_j,\qquad
T_{\ne j}=4P_{a,\ne j}^2-2P_{c,\ne j},\qquad
V_j=8a_jP_{a,\ne j}-2c_jI.
\tag{15.1}
$$
$V_j$ 与 $T$、$E_j$、$E_j^*$ 均交换。因为
$\sigma(8a_jP_{a,\ne j})=\{0\}$ 且 $c_j\ne0$，$V_j$ 是真实有界单位。这里使用谱可逆性，没有假设其非标量部分的范数小于 $2|c_j|$。

### 15.3 精确双导子，不交换不同位置的逆因子

记 $\delta=\operatorname{ad}_T$，即 $\delta(W)=TW-WT$。
局部矩阵计算给
$$
[E_j,[E_j,E_j^*]]=-2E_j,\qquad
[E_j,[E_j,[E_j,E_j^*]]]=0.
$$
在 (15.1) 中，$T_{\ne j}$ 与 $E_j^*$ 及 $V_j$ 交换，因此
$$
\delta^2(E_j^*)=-2E_jV_j^2,\qquad
\delta^3(E_j^*)=0.
$$
定义
$$
W_j=E_j^*V_j^{-2}.
$$
因为 $\delta(V_j^{-2})=0$，有
$$
\boxed{\delta^2(W_j)=-2E_j,\qquad \delta^3(W_j)=0.}
\tag{15.2}
$$

固定一个 $r$ 元集 $F$，按位索引递增次序取有序乘积
$$
W_F=\prod_{j\in F}^{\longrightarrow}W_j.
$$
不同 $W_j$ 不必交换。高阶 Leibniz 公式仍适用：总阶 $2r$ 中每个因子至多可分配两阶，所以只有全部分配两阶的项留下。由 (15.2)，
$$
\boxed{
\delta^{2r}(W_F)
=\frac{(2r)!}{(2!)^r}\prod_{j\in F}(-2E_j)
=(-1)^r(2r)!\,E_F,
\quad E_F=\prod_{j\in F}E_j.
}
\tag{15.3}
$$
这一步没有把 $E_i^*$ 与含其他位的 $V_j^{-2}$ 互换。

### 15.4 任意固定阶的真实强导子单位

$r$ 先任意固定。由于 $c$ 有无穷多个非零项，对每个 $N$ 可选 $N$ 个两两不交的 $r$ 元集合
$$
F_{N,1},\ldots,F_{N,N}
\subseteq\{j\ge N:c_j\ne0\}.
$$
置
$$
U_{N,r}
=\frac{(-1)^r2^r}{N(2r)!}
\sum_{\ell=1}^N W_{F_{N,\ell}}.
$$
这是每个 $N$ 上实际有界的算子；不声称它们的范数一致有界。
由 (15.3)
$$
\boxed{
\delta^{2r}(U_{N,r})
=\frac{2^r}{N}\sum_{\ell=1}^N E_{F_{N,\ell}}
=:R_{N,r}.
}
\tag{15.4}
$$
右侧范数至多 $2^r$，不含 $V_j^{-1}$ 的费用。

对一个固定有限头向量 $x$，充分大 $N$ 时所有选中位均在该头之外。局部计算为
$$
\langle E_F\Omega,\Omega\rangle=2^{-r},
\qquad
\|E_F\Omega\|^2=2^{-r}.
$$
不同 $F_{N,\ell}$ 的非真空波动正交。因此准确有
$$
\|(R_{N,r}-I)x\|^2
=\frac{2^r-1}{N}\|x\|^2.
\tag{15.5}
$$
有限头向量稠密，且 $\|R_{N,r}\|\le2^r$。故
$$
\boxed{\delta^{2r}(U_{N,r})\longrightarrow I\quad\text{强收敛}.}
\tag{15.6}
$$
$r$ 在此极限中固定；没有把 $r$ 随 $N$ 增长的情形纳入 (15.6)。

### 15.5 任何固定头测试的高阶导子准确为零

令 $D$ 为作用在前 $m$ 个物理位上的任意矩阵，张量上尾恒等。
把纯和分成头与尾：
$$
P_a=P_{a,<m}+P_{a,\ge m},\qquad
P_c=P_{c,<m}+P_{c,\ge m}.
$$
于是
$$
T=T_{\ge m}+S_m,
$$
$$
T_{\ge m}=4P_{a,\ge m}^2-2P_{c,\ge m},\qquad
S_m=4P_{a,<m}^2+8P_{a,<m}P_{a,\ge m}-2P_{c,<m}.
\tag{15.7}
$$
$T_{\ge m}$ 与 $D$、$S_m$ 都交换。$S_m$ 的每个单项至少含一个头位 $E_j$。所有这些头位平方零且交换，所以
$$
S_m^{m+1}=0.
$$
由交换导子的二项式，$\operatorname{ad}_{T_{\ge m}}D=0$ 给
$\delta^k(D)=\operatorname{ad}_{S_m}^k(D)$。再展开
$$
\operatorname{ad}_{S_m}^{2m+1}(D)
=\sum_{k=0}^{2m+1}
(-1)^k\binom{2m+1}{k}
S_m^{2m+1-k}DS_m^k.
$$
每项至少有一侧幂次不小于 $m+1$，故
$$
\boxed{\delta^{2m+1}(D)=0.}
\tag{15.8}
$$
这是准确算子等式，不是小范数估计；尾系数仍完整保留在 (15.7) 中。

### 15.6 从局部全配对排除原纯核

定义本表示内的反线性等距对合
$$
(\mathcal Cf)((b_j)_j)=\overline{f((1-b_j)_j)}.
$$
全位互补保持乘积测度，且固定 $\Omega$，所以此 $\mathcal C$ 在原 plus 表示内合法。它满足
$$
T^*=\mathcal C T\mathcal C,\qquad
B(x,y)=\langle x,\mathcal Cy\rangle,\qquad
B(Tx,y)=B(x,Ty).
$$
任意复系数均相容；没有使用一个未实现的无限相位酉。

取 $f,g\in\ker T$。对任意有界 $D,U$ 及整数 $n\ge0$，逐次把导子移过 $B$，有
$$
\boxed{
B(D\delta^n(U)f,g)
=(-1)^n B(\delta^n(D)Uf,g).
}
\tag{15.9}
$$
具体地，$B(\delta(Z)f,g)=0$ 对任意有界 $Z$ 成立；应用
$\delta(D\delta^{n-1}U)=\delta(D)\delta^{n-1}U+D\delta^nU$
并归纳即得 (15.9)。

对固定的 $m$ 头矩阵 $D$，选一个固定 $r>m$。
由 (15.8)，$\delta^{2r}(D)=0$。于是每个 $N$ 均有
$$
B(D\delta^{2r}(U_{N,r})f,g)=0.
$$
使用 (15.6) 的强极限，得到
$$
\boxed{B(Df,g)=0\quad\text{对所有有限头矩阵 }D.}
\tag{15.10}
$$

为自含地说明 (15.10) 迫核为零，反设 $0\ne f\in\ker T$，取 $g=f$。令 $\Pi_m$ 是前 $m$ 位条件期望，也就是头空间张量尾真空的投影。则 $\Pi_m\to I$ 强，且与 $\mathcal C$ 交换。选一个范数为一的头矩阵 $D_m$，把非零向量 $\Pi_m f$ 的单位化送到 $\Pi_m\mathcal Cf$ 的单位化。该局部矩阵与 $\Pi_m$ 交换，因此
$$
\begin{aligned}
B(D_mf,f)
&=\langle D_mf,\mathcal Cf\rangle\\
&=\|\Pi_mf\|\,\|\Pi_m\mathcal Cf\|
+\langle D_m(I-\Pi_m)f,(I-\Pi_m)\mathcal Cf\rangle.
\end{aligned}
$$
第二项的模至多
$\|(I-\Pi_m)f\|\,\|(I-\Pi_m)\mathcal Cf\|$，趋于零；
第一项趋于 $\|f\|^2>0$。这与 (15.10) 矛盾，故 $\ker T=0$。

由 $T^*=\mathcal C T\mathcal C$，也有 $\ker T^*=0$，即 $T$ 值域稠密。单射性与稠密值域逐次传到全部正整数幂。

### 15.7 纯线性与有限辅助支撑的补全

纯线性 $P_a$ 的证明是同一构造的特例：对每个 $a_j\ne0$，(15.1) 的偏导单位直接为 $V_j=a_jI$；(15.2)—(15.6) 全部成立。固定头拆分则用
$$
P_a=P_{a,\ge m}+P_{a,<m},\qquad P_{a,<m}^{m+1}=0.
$$
所以 (15.8)—(15.10) 同样给零核及稠密值域。这里覆盖任意有无穷非零项的复 $\ell^1$ 行，包括 R113 条件不成立的几何行或其他行；不用一个迹表示的核投影递推。

若 $c$ 有限支撑而 $a$ 有无限支撑，选一个有限头包含全部 $\operatorname{supp}c$。在该头的物理基中，$4P_a^2-2P_c$ 是有限的三角算子矩阵，每个对角块均为
$$
4P_{a,\ge m}^2.
$$
尾 $P_{a,\ge m}$ 由刚证的纯线性结论单射，其平方也单射。从三角方程的第一行起逐行消去，整个矩阵单射；反酉对称再给稠密值域。

如果 $a,c$ 都有限支撑，则 $T$ 只作用在一个有限纯头的零常数幂零代数中。非零这样的 $T$ 有非零核，故本节的无限尾条件有实际内容。

### 15.8 实际模型仍缺的步骤

本节没有支付任何原 $N_j,Q_j$ 的进位迁移。

实际模型中，固定有限物理头的幂零性质不会在原全空间上保持：
(15.8) 一般不再等于零。即使 $U_{N,r}$ 每个有界且其导子输出可逼近单位，也不能删除
$$
B((\operatorname{ad}_T^{2r}D)U_{N,r}f,g).
$$
它可能同时含真实进位、未知核和巨大逆因子的成本。

[R236 固定阶广义核附录](../results/R236-appendix-fixed-order-double-commutators-and-generalized-kernel-isotropy.md) 已在其原实际普通 Bell 范围内付固定阶强导子单位及全局等向性；它明确没有付任意局部 $D$ 的等向性。本节新用的是纯模型精确局部幂零，所以不外推那个实际附录，也不混用两稿不同的算子范围。

因此本节关闭纯二次 $\kappa>2$ 及上述更一般纯可和范围，原实际迟首核、普通正常见证及允许误差的实际真空原像仍须继续处理。

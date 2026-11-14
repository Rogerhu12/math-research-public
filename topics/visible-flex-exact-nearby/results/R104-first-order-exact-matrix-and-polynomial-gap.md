# R104：一阶准确矩阵正规化、全频多项式除数与完整强逆接口

2026-11-12，constructive-route。

**状态：完整证明的算子接口及已经执行的实际标量算术。**
R101 已支付同一实际 principal 返回的圆共轭，R102 已支付其完整首相位算术。
本篇把 R46 的一阶反馈式直接化为多项式对角模型
$1+e^{2\pi i\alpha j}(1+i\beta/j)$，保留全部有限输入列、跨锥块、
均值、增广列及普通源。只需同一个固定权上的 $4/3$ 阶强余项；
不要求 R40 的三阶余项或二阶符号输入，也不使用指数算子共轭。

实际 $\alpha,\beta$ 的全频对角界已付，13 个整数/有理门全部通过。
当前完整反馈系数的角向乘子范数、整网强余项常数和实际有限 Schur
逆仍未给出数值；本篇没有把这些条件写成已经通过的 PDE 逆，更不是
课题 README 的闭曲面族完成证书。

## 1. 同一角标度、固定权和实际输入

本篇 $x$ 是 R100/R102 的 $2\pi$ 标签角，$j$ 是其整数 Fourier 频率。
所有物理角频率换算、root 周期常数及 Maslov 号，须在取得以下实际式时
已经准确支付，不能把 $j$ 静默换成物理 $4j$。

先在正频率空间 $j\ge1$ 证明。令
$$
D e_j=j e_j,\qquad U f(x)=f(x+\omega),\qquad
\omega=2\pi\alpha,\qquad T_v=\Pi_+M_v\Pi_+ .
\tag{104.1}
$$
允许固定权
$W_j=e^{\rho\varpi(|j|)}$，其中 $\rho\ge0$，$\varpi$ 非负、递增、
次可加且 $\varpi(0)=0$。定义
$$
\|u\|_{s,\rho}^2=\sum_{j\ge1}\langle j\rangle^{2s}W_j^2|u_j|^2,
\qquad
M_{s,\rho}(v)=2^{|s|/2}\sum_l
 \langle l\rangle^{|s|}W_l|v_l| .
\tag{104.2}
$$
当 $\rho=0$，这正是 R46 的 Sobolev/乘子口径。Peetre 不等式及
$W_j/W_k\le W_{j-k}$ 给
$\|T_v:H^s_\rho\to H^s_\rho\|\le M_{s,\rho}(v)$。
以下略去 $\rho$，始终是同一个权；带宽损失不冒充平滑阶数。

固定 $S\ge0$。假设**实际完整反馈**已在同一 frame 写成
$$
\mathcal A=I+U(I+iB)+R,\qquad B=T_bD^{-1},\qquad
b\ \text{实},\quad \langle b\rangle=\beta,
\tag{104.3}
$$
并已支付
$$
B_*\ge M_{S+2}(b),\qquad
R_*\ge\sup_{|s|\le S}\|R:H^s_\rho\to H^{s+4/3}_\rho\|,
\qquad M_{S+3}(b-\beta)<\infty .
\tag{104.4}
$$
$R$ 是完整强矩阵余项，不是逐列渐近。多个幅度支、负频率及均值的
处理见 §5；不能先删掉这些块，再把剩余部分称为 (104.3)。

R100 的准确连分数给
$$
|1-e^{-il\omega}|>\frac2{5|l|}\quad(l\ne0).
\tag{104.5}
$$
逐模解
$$
a-a_-=\beta-b,\qquad a_-(x)=a(x-\omega),\qquad\langle a\rangle=0.
\tag{104.6}
$$
因此
$$
a_l=-\frac{b_l}{1-e^{-il\omega}}\quad(l\ne0),\qquad
a\ \text{实},\qquad
A_*\ge M_{S+2}(a)
\quad\text{可取}\quad
A_*=\frac52 M_{S+3}(b-\beta).
\tag{104.7}
$$
最后一个常数保守：$|l|\le\langle l\rangle$，而 (104.2) 的两个
$2^{s/2}$ 因子还可节省 $\sqrt2$。这里不要求 $A_*$ 或 $B_*$ 小。

## 2. 有限低列留下的准确共轭

取整数
$$
N_0\ge1,\qquad A_*/N_0\le\tfrac12,\qquad
P_0=1_{j\ge N_0},\quad P_{0L}=I-P_0,
$$
$$
C=T_aD^{-1}P_0,\qquad \mathcal T=I+iC .
\tag{104.8}
$$
对全部 $|r|\le S+2$，
$$
\|C\|_{H^r_\rho\to H^r_\rho}\le A_*/N_0\le\tfrac12,
\qquad
\|\mathcal T\|\le\tfrac32,\qquad
\|\mathcal T^{-1}\|\le2 .
\tag{104.9}
$$
逆是收敛的有界算子 Neumann 级数。$\mathcal T$ 不声称酉；
它是有明确双向范数的准确坐标变化。低输入 $j<N_0$ 上
$\mathcal T=\mathcal T^{-1}=I$，高输入产生的低输出仍保留。

定义
$$
\mathcal D=I+U(I+i\beta D^{-1}),\qquad
F_0=iU T_{b-\beta}D^{-1}P_{0L},
$$
$$
E_2=-UBC+\beta CUD^{-1}.
\tag{104.10}
$$
则有不含形式符号余差的完整恒等式
$$
\boxed{\quad
\mathcal A\mathcal T-\mathcal T\mathcal D
   =F_0+E_2+R\mathcal T ,
\quad}
\tag{104.11}
$$
从而
$$
\boxed{\quad
\widetilde{\mathcal A}:=\mathcal T^{-1}\mathcal A\mathcal T
=\mathcal D+\widetilde F_0+\widetilde E_2+\widetilde R,
\quad
(\widetilde F_0,\widetilde E_2,\widetilde R)
=(\mathcal T^{-1}F_0,\mathcal T^{-1}E_2,
  \mathcal T^{-1}R\mathcal T).
\quad}
\tag{104.12}
$$

**证明。** $U^{-1}T_aU=T_{a_-}$，$U,D^{-1},P_0$ 彼此交换。
展开左侧的一阶项为
$$
iU\{C-U^{-1}CU+B-\beta D^{-1}\}
 =iU T_{b-\beta}D^{-1}(I-P_0)=F_0 .
$$
二次项准确是 $-UBC+\beta CUD^{-1}$。余下只有 $R\mathcal T$。
没有把 $T_bT_a$ 换成 $T_{ba}$，也没有交换 $D^{-1}$ 与乘子；
所以完整 Toeplitz/Hankel 矩阵及全部 ordering 都在 (104.11) 中。$\square$

因为 $\|D^{-1}:H^r_\rho\to H^{r+1}_\rho\|\le\sqrt2$，
逐次使用 (104.2) 给，对于 $|s|\le S$，
$$
\|E_2:H^s_\rho\to H^{s+2}_\rho\|
 \le2M_{s+2}(b)M_{s+1}(a)+2|\beta|M_{s+2}(a)
 \le2A_*(B_*+|\beta|).
$$
结合 (104.9)，得到完整强常数
$$
\boxed{\quad
K_2:=4A_*(B_*+|\beta|),\qquad K_{4/3}:=3R_*,
$$
$$
\|\widetilde E_2:s\to s+2\|\le K_2,\qquad
\|\widetilde R:s\to s+4/3\|\le K_{4/3}.
\quad}
\tag{104.13}
$$
这里只在 $|r|\le S+2$ 使用 $\mathcal T^{\pm1}$，在 $|s|\le S$
使用 $R$，没有暗加一个未给出的 $R$ 导数窗口。

$F_0$ 是有限**输入**秩，绝不等于有限 Fourier 矩阵。
其全部高输出仍在 (104.12) 中。当 $N_0=1$ 时它为零；否则
$$
\|\widetilde F_0:H^s_\rho\to H^{s+2}_\rho\|
\le2N_0M_{s+2}(b-\beta).
\tag{104.14}
$$
这里 $D^{-1}P_{0L}$ 的两阶增益范数为
$\max_{1\le j<N_0}(j+j^{-1})\le N_0$。
后文高切 $N\ge N_0$ 时 $\widetilde F_0P_{\ge N}=0$；
这个事实允许把它放在真实有限块接线中，而不把其大范数加到高块收缩费。

## 3. 实际多项式对角：所有频率都已支付

沿用 R102 的准确目标
$$
1323907691653283951\,\alpha^2
-1460270480137213085\,\alpha
+402669666587037055=0
$$
的较小根。实际整个 $\Delta_5$ 参数盒已证
$$
37.00989598323246<\beta<37.04013657837160 .
\tag{104.15}
$$
本节使用保存的准确有理端点，不把这些显示小数当计算输入。

记
$$
d_j=1+e^{i\omega j}(1+i\beta/j),\qquad j\ge1.
$$
**全频结论为**
$$
\boxed{\quad |d_j|>\frac7{110j}\quad(j\ge1).\quad}
\tag{104.16}
$$

若 $1\le j\le499$，逆三角不等式给
$$
j|d_j|\ge\sqrt{j^2+\beta^2}-j>1,
\tag{104.17}
$$
因为 $\beta>37$ 且 $37^2=1369>2\cdot499+1=999$。
因此这批低模不需要另外的逐频相位计算。

若 $j\ge500$，对 $t\ge0$，
$$
0\le t-\arctan t=\int_0^t\frac{u^2}{1+u^2}du\le t^3/3 .
$$
于是
$$
j|\arctan(\beta/j)-\beta/j|
<\frac{(371/10)^3}{3\cdot500^2}
=\frac{51064811}{750000000}<\frac7{100}.
\tag{104.18}
$$
R102 的全部正频率 $17/100$ scaled 相位间隙因此留下大于 $1/10$，
并给
$$
|1+e^{i(\omega j+\arctan(\beta/j))}|>\frac1{5\pi j}.
\tag{104.19}
$$
设 $r_j=\sqrt{1+\beta^2/j^2}\ge1$。准确恒等式
$$
|1+r_je^{it}|^2=(r_j-1)^2+r_j|1+e^{it}|^2
$$
说明 (104.19) 也是 $|d_j|$ 的下界。R102 已保存的 Machin
有理包络给 $\pi<22/7$，故得 (104.16)。

这是直接对多项式对角的证明；没有先替换为 $e^{i\beta/j}$，
所以不额外引入 $\beta^2/(2j^2)$ 的模型误差。负锥若为同一实算子的
准确共轭块，其对角是 $\overline{d_j}$，下界完全相同。
不同常相位或不同首平均的其他块，须另给实际除数门。

## 4. 真高块与全部有限 Schur 接线

取整数 $N\ge N_0$，$P_H=1_{j\ge N}$。置
$$
c=\frac7{110},\qquad
\kappa_N=\frac1c\left(\frac{K_2}{N}
                           +\frac{K_{4/3}}{N^{1/3}}\right).
\tag{104.20}
$$
当真实常数满足 $\kappa_N\le1/2$，完整高块
$$
A_{HH}=P_H\widetilde{\mathcal A}P_H
=P_H(\mathcal D+\widetilde E_2+\widetilde R)P_H
$$
在每个已付 $|s|\le S$ 有唯一逆，
$$
\boxed{\quad
\|A_{HH}^{-1}:P_HH^{s+1}_\rho\to P_HH^s_\rho\|
\le \frac{2}{c}=\frac{220}{7}.
\quad}
\tag{104.21}
$$

**证明。** (104.16) 给 $|d_j^{-1}|<j/c$。所以
$$
\|\mathcal D^{-1}P_H
(\widetilde E_2+\widetilde R)P_H\|_{H^s_\rho\to H^s_\rho}
\le\kappa_N .
$$
这利用真实输出投影的
$j/\langle j\rangle^2\le N^{-1}$ 和
$j/\langle j\rangle^{4/3}\le N^{-1/3}$；不是按单列估计猜出的矩阵范数。
Neumann 逆得到 (104.21)。准确源空间是 $P_HH^{s+1}_\rho$，
定义域为
$$
\mathcal G_s=\{u\in P_HH^s_\rho:A_{HH}u\in P_HH^{s+1}_\rho\}
$$
的图范数空间；不声称 $A_{HH}$ 把整个 $H^s$ 都映入 $H^{s+1}$。
齐次核在整个 $P_HH^s_\rho$ 上也为零。$\square$

一个仅用有理数的保守充分选择是
$$
N_0=\max(1,\lceil2A_*\rceil),\qquad
N\ge\max\left\{N_0,
 \left\lceil\frac{4K_2}{c}\right\rceil,
 \left\lceil\left(\frac{4K_{4/3}}{c}\right)^3\right\rceil\right\}.
\tag{104.22}
$$
它把两个收缩项分别压到 $1/4$。当前没有代入虚构的 $A_*,B_*,R_*$；
完整源中的可执行函数只在传入实际准确有理上界后给条件 cutoff。

令 $L$ 包括全部 $j<N$、均值、核规范、真实参数/兼容增广变量。
把 (104.12) 的**整个实际算子**分成 $L/H$ 四块。特别
$\widetilde F_0$ 的所有高输出仍属于 $A_{HL}$，不能投掉。
有限输入列进入 $A_{HH}^{-1}$ 所需的 $H^{s+1}$ norm，须由实际列及其尾支付；
(104.14) 已支付 $F_0$ 的这部分，但不替代其他增广列的独立费用。

完整有限条件是
$$
\mathcal S_N=A_{LL}-A_{LH}A_{HH}^{-1}A_{HL}
\tag{104.23}
$$
的实际逆，或在已指定核规范/兼容条件上的实际增广逆。
若这一步也已付，则令 $f'=\mathcal T^{-1}f$，
$$
u_L=\mathcal S_N^{-1}
   (f'_L-A_{LH}A_{HH}^{-1}f'_H),\qquad
u_H=A_{HH}^{-1}(f'_H-A_{HL}u_L),\qquad z=\mathcal T u .
\tag{104.24}
$$
这保留全部有限列、高低反馈和有符号源项。
归一化高逆常数 (104.21) 还应与实际有限逆及 (104.9) 的
源变换 $\le2$、解重建 $\le3/2$ 一起放入最终 PDE/非线性预算。

## 5. 多锥、均值、普通源及不能省的假设

对有限多个已给定的标量主锥，逐锥使用 $\mathcal T$；共轭负锥使用
其准确复共轭变换，在均值和有限增广空间上取恒等。
实际跨锥、跨幅度支余项全部放入同一个矩阵 $R$，其
$R_*$ 是整个直和 Hilbert 空间上的强范数上界；不能以每一块
各自 $\le R_*$ 就免费推得全矩阵也 $\le R_*$。
对已付矩阵 norm 上界，(104.9)、(104.13) 原样成立。

若某两个主支之间仍有未经消除的一阶矩阵值耦合，它不是本定理的
$4/3$ 阶余项。本篇不把非交换矩阵同调冒充逐标量同调。
未知 Maslov 常相位、不同 rotation、缺失 mean 行或未支付的端口
Schur，也不能藏进 $R$。

R46 (6.12) 的普通源是同一个真实 Cauchy 积分
$$
f_{\rm amp}=\mathscr F(x)^{-1}
 \int_y^x\mathcal T_{\rm Cauchy}(x,r)(0,f(r))^t\,dr .
\tag{104.25}
$$
这是 R46 的局部物理 cut 幅度。令 $\mathcal J_{\rm wire}$ 为从该局部
幅度到本篇已经共轭的归一标签/frame 的真实源注入，包含 $x=4\eta$
尺度、完整 $\mathscr G_H$ 和实际端口操作，并支付其该档 norm
$K_{{\rm wire},s+1}$。(104.24) 的 $f$ 必须是已经这样接线的右端，
不能把局部 $f_{\rm amp}$ 与它无费等同。为了使用 (104.21)，应付
$
\|\mathcal T^{-1}\mathcal J_{\rm wire}f_{\rm amp}\|_{H^{s+1}}
\le 2K_{{\rm wire},s+1} I_{s+1}(x)\mathfrak E_{s+1}
       \int\|f(r)\|_{H^{s+1/2}}\,dr .
\tag{104.26}
$
这里显示的是 $\rho=0$ 的源界；若选 $\rho>0$，须另付同一固定权的
真实源估计，不能从有限阶光滑能量自动升级。式 (104.26) 明确包含高逆的
一阶损失；$K_{{\rm wire},s+1}$ 不能默认为 1。若原源有 divergence、contact 或
边界结构，仍须先使用其实际源重建；不能仅改名成 (104.25)。
正侧 Ai 源、帽尾源、mean 兼容和参数列也按其实际有限/无限输出
进入同一 (104.23)–(104.24)。

## 6. 当前实际输入从哪里来

R46 (9.1) 正是目标输入形状；R101 的 principal 圆共轭必须以 R46
(3.11)、(7.3) 的完整通量 frame 实施。其首系数平均按 R46 (9.2)
和 R50 固定材料有限部保持为本题已经认证的 $\beta$。
非均值首系数并未由这个平均积分自动给出。

严格负区每段的真实输入角系数是 R46 (5.7)
$$
\widehat h_\sigma(x,\eta)=
 \int_{x_0}^x\frac{\mathcal F}{2\mu}
 (r,\Theta_\sigma(r,\eta))\,\Theta_{\sigma,\eta}(r,\eta)\,dr .
\tag{104.27}
$$
完整 $b$ 由这些段、R43 的实际 collar 首 Dyson 系数、全部端口
一阶变换经 R46 (7.3) 加合产生。为使用 (104.7)，须对这一完整
同一对象支付 $M_{S+3}(b-\beta)$；仅有 $\beta$ 或 principal ODE
的端点图不能提供它。

R99 的 $b_{\rm root}=(v_1\circ H^{-1})/3$ 是实际 canonical root
势的系数，和 (104.3) 的反馈相位 $b$ 不是同一个量。
R99 的 17 个 root Cauchy 乘子、完整 $v_1$ 及 frame 证书可给
R43/R46 真实 collar 接线的输入，仍须经过有限 collar/严格区传播。
R92/R97 的 canonical/physical 低列与全尾可接 (104.23)，但不替代
整个低 Schur 的逆。R103 的 primal/dual 正帽门亦须以其真实
paired-source 合同接回；本篇没有取消这些门。

相较 R40，本接口消除了“必须先取得 $p_2$、三阶强余项以及
$e^{2Q}$ 共轭费用”的额外要求。留下的准确合同为：

1. 同一固定权、同一实际窗口的完整式 (104.3)，含正确的常相位、
   mean/cross/source 及其 full frame；
2. 完整 $M_{S+3}(b-\beta)$、$M_{S+2}(b)$ 和 $R_*$，代入
   (104.13)、(104.20)；
3. 全部有限低列、兼容及参数高尾的实际 Schur 逆；
4. 将该强逆接入 R37 非线性修正与真实闭帽、固定开握持、可见位移、
   非全等和 reach 预算。

这些要求仍是本课题 open 的实际工作，不因标量对角除数已全频通过
而自动成立。

## 7. 已执行的有限算术与重放

源：
[scripts/fourfold_polynomial_diagonal_and_cutoff_exact.mjs](../scripts/fourfold_polynomial_diagonal_and_cutoff_exact.mjs)

报告：
[notes/2026-11-12-R104-polynomial-diagonal.json](../notes/2026-11-12-R104-polynomial-diagonal.json)

从课题根目录运行：
~~~sh
node scripts/fourfold_polynomial_diagonal_and_cutoff_exact.mjs \
  --out notes/2026-11-12-R104-polynomial-diagonal.json
~~~

源逐 UTF8 SHA256 核对 R102 报告和实际 $\beta$ 包，使用完整 BigInt
约分有理数执行 13 个门，包含同对象/同参数区间、较小根、低频
平方不等式、全部高频 atan 费用和准确 $\pi<22/7$。
本次在 functions.exec 的 V8 内实际执行同一纯函数；
native CLI 因执行器不可用尚未运行，报告明确区分两者。
没有新增几何或 ODE 计算。

可选 --bounds 指向包含准确有理字符串 a_bound、b_bound、
beta_abs_bound、remainder_four_thirds_bound 的 JSON。它计算
(104.22)；这些输入须是已经独立支付的实际有限窗口上界。
当前报告没有调用这一可选门，也不输出伪造的实际 cutoff。

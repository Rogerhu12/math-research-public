# R43：真实 Airy 传播的首个逆频率相位与 4/3 阶余项

2026-11-12，independent-audit。

**状态：本篇证明同一个实际 canonical simple-turn 负侧传播的
首阶符号，不是最终全域反馈的相位证书。** 第一项真实 Dyson
积分的同向对角部分给一个明确的实射线积分；根部与反向支的剩余
都是 $4/3$ 阶平滑。用 R42 的真实二次 Dyson 余项把这个首阶
计算升级到准确传播。证明含均值和全 Fourier 矩阵，不只给单列
渐近式，也不要求势的振幅小。

真实正组件的 Ai defect、边界 shear、严格负区和全网接线仍须
与同一个对象匹配。本文末尾写出它们的精确接口，避免把这里的
单根射线积分直接称为 R34 所需的完整 $\beta$。

## 1. 实际输入、权与主结论

沿用 [R39](R39-finite-component-airy-transfer-input.md) 与
[R42](R42-integrable-airy-dyson-and-flux-frame.md)：
$$
U_{\xi\xi}-\xi U_{\phi\phi}+VU=f,
\quad 0\le\xi\le\delta\le1,\quad q=2\pi/\ell,
\quad z'=\mathcal Kz+\Gamma_f.
\tag{1.1}
$$
$F_*$、$D_\pm$、$c$ 及均值列均保持原定义。$V$ 为实际实势，
现在额外供应它的一阶径向导数以及所需有限角范数。
令
$$
v_l=\sup_{0\le\xi\le\delta}|V_l(\xi)|,
\quad v_l^{(1)}=\sup_{0\le\xi\le\delta}|\partial_\xi V_l(\xi)|,
\quad w_l=v_l+v_l^{(1)}.
\tag{1.2}
$$

先可取无权空间 $E_s$。更一般地，若实际 canonical 势已经支付
权 $W_\rho(j)=e^{\rho\omega(|j|)}$，其中 $\omega$ 非负、递增、
次可加且 $\omega(0)=0$，定义
$$
\|u\|_{s,\rho}^2=\sum_j\langle j\rangle^{2s}W_\rho(j)^2|u_j|^2,
\quad E_{s,\rho}=(H^s_\rho)^2,
$$
$$
M_{r,\rho}(V)=2^{|r|/2}\sum_l\langle l\rangle^{|r|}
                       e^{|\rho|\omega(|l|)}v_l.
\tag{1.3}
$$
这包括直接 log 权，但“实际 canonical 势已支付该权”是额外输入；
本篇不从固定 root、有限角 Fourier 或 C4 径向样条自动推出它。
负权空间按 R41 的有界 Fourier 延拓理解。

写 $D e_j=|j|e_j$，在均值上定义 $D^{-1/2}e_0=0$。
令 $\Pi_\varepsilon$ 为 $\varepsilon j>0$ 的正、负频率投影，
$\varepsilon\in\{+1,-1\}$；幅度支另用 $\sigma\in\{+1,-1\}$。
定义四个真实实函数
$$
\boxed{\quad
a_{\sigma\varepsilon}(\phi)
=\frac1{2q}\int_0^\delta\frac{
 V\bigl(\xi,\phi-\sigma\varepsilon\tau(\xi)\bigr)}{\sqrt\xi}
                  d\xi,
\qquad \tau(\xi)=\frac23\xi^{3/2}.
\quad}
\tag{1.4}
$$
以及准确自伴的标量算子
$$
A_\sigma=\sum_{\varepsilon=\pm1}
 \Pi_\varepsilon D^{-1/2}M_{a_{\sigma\varepsilon}}
                         D^{-1/2}\Pi_\varepsilon,
\qquad
B=i\operatorname{diag}(A_+,-A_-).
\tag{1.5}
$$
$M_a$ 是完整乘法；投影与 $D^{-1/2}$ 的顺序按 (1.5) 固定。
$B^*=-B$，且与 $J=\operatorname{diag}(I,-I)$ 交换，所以
$e^B$ 同时是准确普通酉及 $J$-酉算子。

为列出余项，设
$$
\begin{aligned}
C_q={}&4(50\pi+5)q^{-4/3}
       +150\pi\max\{1,q^{-2/3}\}+3q^{-1},\\
\mathcal W_{s,\rho}(V)={}&
2^{|s+4/3|/2}\sum_l
 \langle l\rangle^{|s+4/3|+4/3}
             e^{|\rho|\omega(|l|)}w_l.
\end{aligned}
\tag{1.6}
$$
令
$$
K_s^{(0)}=100\pi\max(1,2^{1/3}q^{-2/3})M_{s+1/3,\rho}(V),
$$
$$
B_s^{(1)}=100\pi\max(1,\sqrt2/q)M_{s+1/2,\rho}(V),
\qquad
A_s^{(1)}=\frac{\sqrt{2\delta}}qM_{s+1/2,\rho}(V).
\tag{1.7}
$$
在所用有限窗口满足 R39 的实际 collar 门及
$\delta\max K_s^{(0)}\le1/10$。若只要求无权结论，取 $\rho=0$。

**定理 1.1。** 准确齐次传播满足
$$
\boxed{\quad C(\delta,0)=I+B+R_{4/3},\quad}
\tag{1.8}
$$
其中
$$
\|R_{4/3}:E_{s,\rho}\to E_{s+4/3,\rho}\|
\le 2C_q\mathcal W_{s,\rho}(V)
       +2e^{1/10}\delta B_s^{(1)}B_{s+1}^{(1)}.
\tag{1.9}
$$
也有准确分解
$$
\boxed{\quad C(\delta,0)=e^B+\widehat R_{4/3},\quad}
\tag{1.10}
$$
右端余项 norm 不超过 (1.9) 再加
$$
\frac12e^{A_{s+2}^{(1)}}A_s^{(1)}A_{s+1}^{(1)}.
\tag{1.11}
$$
这里 $e^B$ 不是实际传播的替代品：$\widehat R_{4/3}$ 被明确保留。
均值的实际传播和所有跨符号耦合也没有被设为零；它们在声明的
完整余项中按实际有限范数携带，后续有限低块仍须真实处理。

## 2. 带余项的单个 Airy 振荡式

令 $Y_\sigma(t)=\operatorname{Bi}(-t)+i\sigma\operatorname{Ai}(-t)$，
$t>0$。标准 Airy 首项及其导数给
$$
t^{1/4}Y_\sigma(t)
\sim\pi^{-1/2}e^{i\sigma(\frac23t^{3/2}+\pi/4)}
\quad(t\to\infty).
\tag{2.1}
$$
这里只使用首项的极限和一阶导数极限，来源为 NIST DLMF
[9.7.9–9.7.12](https://dlmf.nist.gov/9.7#ii)。以下误差界独立
从常微分方程导出，不把未给余项的渐近符号当作全区间估计。

置 $\eta=\tfrac23t^{3/2}$、$Z=t^{1/4}Y_\sigma(t)$。
R39 的准确变换给
$$
Z''+Z=-\frac5{36\eta^2}Z.
$$
用 (2.1) 在无穷远的实际振荡条件，变常数公式为
$$
Z(\eta)=\pi^{-1/2}e^{i\sigma(\eta+\pi/4)}
-\int_\eta^\infty\sin(s-\eta)\frac5{36s^2}Z(s)ds.
\tag{2.2}
$$
R39 的能量界先保证 $Z$ 有界，因此积分绝对收敛；终端
Volterra 逐次积分又给
$$
\left|Z(\eta)-\pi^{-1/2}e^{i\sigma(\eta+\pi/4)}\right|
\le\pi^{-1/2}\left(e^{5/(36\eta)}-1\right).
\tag{2.3}
$$
对 $t\ge1$，$5/(36\eta)\le5/24$，并且
$e^{5/24}\le(1-5/24)^{-1}=24/19<4/3$，所以
$$
\boxed{\quad
\left|Y_\sigma(t)-\frac{t^{-1/4}}{\sqrt\pi}
 e^{i\sigma(\frac23t^{3/2}+\pi/4)}\right|
\le\frac5{18\sqrt\pi}\,t^{-7/4}.
\quad}
\tag{2.4}
$$

对非零物理频率 $\lambda=q|j|$，写
$$
d_\sigma(\xi,j)=\frac c{\sqrt\pi}\lambda^{-1/2}\xi^{-1/4}
 e^{i\sigma(\lambda\tau(\xi)+\pi/4)}.
\tag{2.5}
$$
由 (2.4)，在 $\xi\lambda^{2/3}\ge1$ 有
$$
|D_\sigma-d_\sigma|
\le\frac5{18\lambda\xi^{3/2}}|d_\sigma|,
\qquad |D_\sigma|\le2|d_\sigma|.
\tag{2.6}
$$
根附近则仍使用 R39 的全轴界
$|D_\sigma|\le10c\lambda^{-1/3}$。不能把 (2.5) 的奇异振幅
直接延伸到根当作真实 Cauchy 列。

## 3. 第一项真实 Dyson 矩阵及根层费用

第一项是准确算子
$$
T_1=\int_0^\delta\mathcal K(\xi)d\xi.
$$
从 R39 的完整 source inverse，逐项得到
$$
(\mathcal K_{\sigma\tau})_{kj}
=\frac{i\sigma\pi}{2c^2}
        D_{-\sigma}(\xi,k)V_{k-j}(\xi)D_\tau(\xi,j).
\tag{3.1}
$$
这个符号同时固定了后面相位的正负，不由特征图猜测。

先令 $j,k\ne0$，记
$\lambda_* = q\min(|j|,|k|)$。把积分切在
$a=\min(\delta,\lambda_*^{-2/3})$。根区的真实乘积积分至多
$$
\frac\pi{2c^2}\int_0^a|D_{-\sigma}(k)D_\tau(j)|d\xi
\le50\pi\lambda_*^{-4/3}.
\tag{3.2}
$$
把两个 $D$ 改成两个 $d$ 后，根区对应的绝对积分至多
$\lambda_*^{-4/3}$。

若 $a<\delta$，在余下区间用 (2.6)，得到
$$
|D_{-\sigma}(k)D_\tau(j)-d_{-\sigma}(k)d_\tau(j)|
\le\frac{5c^2}{6\pi}\lambda_*^{-2}\xi^{-2}.
$$
乘 $\pi/(2c^2)$ 并积分，费用至多
$\tfrac5{12}\lambda_*^{-4/3}$。因此，对每个 Fourier lag $l=k-j$，
把 (3.1) 的完整积分替换成 (2.5) 的振荡乘积所引入的误差满足
$$
\boxed{\quad
|\mathrm{error}_{\sigma\tau;kj}|
\le(50\pi+2)\lambda_*^{-4/3}v_l.
\quad}
\tag{3.3}
$$
这里没有假定 $\lambda_*>1$；小频率若使整个 collar 位于根层，
(3.2) 已单独覆盖。

## 4. 同向项给出真实射线积分

若 $\tau=\sigma$ 且 $j,k$ 同号 $\varepsilon$，两个首项的
Maslov 常数相消，并且
$$
\frac{i\sigma\pi}{2c^2}d_{-\sigma}(k)d_\sigma(j)
=\frac{i\sigma}{2q\sqrt{|k||j|}}\xi^{-1/2}
                  e^{-i\sigma\varepsilon q(k-j)\tau(\xi)}.
\tag{4.1}
$$
积分后正是
$$
\frac{i\sigma}{\sqrt{|k||j|}}
                      (a_{\sigma\varepsilon})_{k-j}.
\tag{4.2}
$$
这就是 (1.5) 的准确对称 ordering。由于 $V$ 为实数，(1.4)
为实函数，$A_\sigma$ 真自伴；没有把一个左符号的近似自伴性
当成准确通量。

特别，四个积分的角平均相同：
$$
\langle a_{\sigma\varepsilon}\rangle
=\frac1{2q}\int_0^\delta\xi^{-1/2}\langle V(\xi,\cdot)\rangle d\xi.
\tag{4.3}
$$
这是该实际 canonical frame 的单根贡献。主返回的进一步变角、
严格负区传播、另一根和 boundary frame 都还会影响完整相位，
所以 (4.3) 目前不能直接充当全网的 $\beta$。

## 5. 反向项的 4/3 阶界

若 $\tau=-\sigma$，首项乘积的相位含
$\Lambda\tau(\xi)$，其中
$\Lambda=q(|j|+|k|)\ge2\lambda_*$。只需估计
$$
I_l(\Lambda)=\int_0^\delta \xi^{-1/2}V_l(\xi)
                               e^{\pm i\Lambda\tau(\xi)}d\xi.
$$
准确有
$$
\boxed{\quad |I_l(\Lambda)|
\le\Lambda^{-1/3}(5v_l+v_l^{(1)}).\quad}
\tag{5.1}
$$

**证明。** 若 $\delta\le\Lambda^{-2/3}$，绝对积分就不超过
$2\Lambda^{-1/3}v_l$。否则在 $a=\Lambda^{-2/3}$ 切开。
根区给同样的 $2\Lambda^{-1/3}v_l$。在 $[a,\delta]$ 使用
$\partial_\xi e^{\pm i\Lambda\tau}=\pm i\Lambda\sqrt\xi\,
e^{\pm i\Lambda\tau}$ 作一次积分分部。两个端点至多给
$2\Lambda^{-1/3}v_l$，微分 $\xi^{-1}$ 给
$\Lambda^{-1/3}v_l$，其余项给
$$
\frac{v_l^{(1)}}\Lambda\log(\delta\Lambda^{2/3})
\le\Lambda^{-1/3}v_l^{(1)}.
$$
最后一步中 $\Lambda>1$，$\delta\le1$，且
$(2/3)\log\Lambda\le\Lambda^{2/3}$。证毕。

振荡乘积的前因子绝对值为 $1/(2\sqrt{\lambda_j\lambda_k})$。
因此由 (5.1) 其积分至多
$3\lambda_*^{-4/3}w_l$。与 (3.3) 合并，反向支满足
$$
|(T_1)_{\sigma,-\sigma;kj}|
\le(50\pi+5)\lambda_*^{-4/3}w_l.
\tag{5.2}
$$
这一步用的是实际 $\partial_\xi V$，不是把一个仅有连续势的
振荡积分默认升级到该阶数。

## 6. 从全矩阵到强算子界：含均值及不同比例频率

称 $j,k$ 为可比同号对，若二者非零、同号，且
$|j|/2\le|k|\le2|j|$。这时
$$
\lambda_*^{-4/3}
\le4q^{-4/3}\langle j\rangle^{-4/3}.
\tag{6.1}
$$
所以 (3.3)、(4.2)、(5.2) 已给这些对的余项界。

对于其余对，$l=k-j$ 满足
$\langle j\rangle^{4/3}\le3\langle l\rangle^{4/3}$。
包括 $j=0$ 或 $k=0$。原完整 Airy 列满足统一逐元界
$$
|D_\sigma(\xi,j)|\le10c\max(1,q^{-1/3}),
\quad 0\le\xi\le\delta\le1,
$$
因此
$$
|(T_1)_{\sigma\tau;kj}|
\le50\pi\max(1,q^{-2/3})\delta v_l.
\tag{6.2}
$$
在这类对上，模型 (1.5) 若非零，其元的绝对值也至多
$\sqrt\delta\,q^{-1}v_l$。所以所有完整矩阵元统一满足
$$
\boxed{\quad
|(T_1-B)_{\sigma\tau;kj}|
\le C_q\langle l\rangle^{4/3}w_l
                         \langle j\rangle^{-4/3}.
\quad}
\tag{6.3}
$$
这解释了为何 mean 和 cross-sign 项确实可以进入本篇有限强余项：
它们各自的实际源系数仍存在，费用由同一个 $w_l$ 支付。

由
$$
\frac{\langle k\rangle^{s+4/3}}{\langle j\rangle^{s+4/3}}
\le2^{|s+4/3|/2}\langle k-j\rangle^{|s+4/3|},
\qquad
\frac{W_\rho(k)}{W_\rho(j)}
\le e^{|\rho|\omega(|k-j|)},
$$
离散 Young 不等式对每个幅度 block 给
$C_q\mathcal W_{s,\rho}$；两个输入、输出支的直和再给因子 $2$。
于是
$$
\boxed{\quad
\|T_1-B:E_{s,\rho}\to E_{s+4/3,\rho}\|
\le2C_q\mathcal W_{s,\rho}(V).\quad}
\tag{6.4}
$$
这是完整矩阵 norm，不是由每列 norm 推断 $\ell^2$ 有界。
无权 $\mathcal W$ 可由 R39(4.3) 同一积分分部，以有限实际角
导数上界计算；同时要对 $\partial_\xi V$ 支付相应导数。

## 7. 精确传播、真酉近似与首个左符号

R42 的证明在 (1.3) 的已付权中逐字成立：$D_\pm$ 与权交换，
中间乘法用 $M_{r,\rho}$。特别在 $N=1$ 时，
$$
\|C-I-T_1:E_{s,\rho}\to E_{s+2,\rho}\|
\le2e^{1/10}\delta B_s^{(1)}B_{s+1}^{(1)}.
\tag{7.1}
$$
嵌入到 $E_{s+4/3,\rho}$ 并与 (6.4) 合并，证明 (1.8)–(1.9)。

由 (1.4)，
$M_{r,\rho}(a_{\sigma\varepsilon})
\le\sqrt\delta\,q^{-1}M_{r,\rho}(V)$。
每个 $D^{-1/2}$ 在非零频率上增益 $1/2$ 的 norm 至多
$2^{1/4}$，所以
$$
\|B:E_{s,\rho}\to E_{s+1,\rho}\|\le A_s^{(1)}.
\tag{7.2}
$$
两 cones 各自正交，取最大值而非额外求和。
有界算子的准确积分余项
$$
e^B-I-B=\int_0^1(1-t)e^{tB}B^2dt
$$
遂给 (1.11)，从而证明 (1.10)。无权 $E_0$ 上 $e^B$ 准确酉；
高 Sobolev 或正权上的指数费用仍须保留。

若后续采用 R40 的左符号约定，在每个固定 cone 上可写
$$
\Pi_\varepsilon D^{-1/2}M_aD^{-1/2}\Pi_\varepsilon
=\Pi_\varepsilon M_a\Pi_\varepsilon D^{-1}
                         +\text{二阶平滑项},
\tag{7.3}
$$
这个式子的完整同 cone 矩阵误差为
$$
a_{k-j}\left(|k|^{-1/2}|j|^{-1/2}-|j|^{-1}\right).
$$
对 $jk>0$，准确有
$$
\left||k|^{-1/2}|j|^{-1/2}-|j|^{-1}\right|
=\frac{||k|-|j||}{|j|\sqrt{|k|}(\sqrt{|k|}+\sqrt{|j|})}
\le\frac{|k-j|}{|j|^{3/2}|k|^{1/2}}.
$$
乘上 $H^s\to H^{s+2}$ 权后，用
$\langle n\rangle\le\sqrt2|n|$ 对 $n\ne0$，以及
$|k|/|j|,|j|/|k|\le1+|k-j|$，即可得到例如
$$
\|\text{(7.3)误差}\|_{H^s_\rho\to H^{s+2}_\rho}
\le2^{(|s|+2)/2}\sum_l
 (1+|l|)^{|s|+3}e^{|\rho|\omega(|l|)}|a_l|.
\tag{7.4}
$$
所以首个逆频率系数确实是 $i\sigma a_{\sigma\varepsilon}$；
ordering 的差属于已经列明的更高阶，不能改动该首阶系数。

## 8. 普通源仍使用实际传播

完整解保持 R39/R42 的准确公式
$$
z(\delta)=\bigl(e^B+\widehat R_{4/3}\bigr)z(0)
       +\int_0^\delta C(\delta,t)\Gamma_f(t)dt.
\tag{8.1}
$$
式中 ordinary source 不是 $e^B$ 的一个随意近似。若要将源也
替成有限 Dyson 段，直接使用 R42(3.2) 的真实双 Cauchy 槽误差。
物理 source 的 Jacobian、height、divergence 附加项，以及根与
strict cut 的 normal shear 全部沿用 R39 §7。

本篇没有自动给出随几何变化的导数。只对固定 canonical 圆与
坐标中的 $V$ 变化，(1.4) 可直接线性求导；圆长、root map 或
physical source 也变化时，其实际贡献和导数损失仍按 R42 §5
一起验证。

## 9. 正侧 Ai、完整 DN 与最终相位的实际接口

在根的正侧写 $y=-\xi>0$。自由衰减列
$$
u_A=c\lambda^{-1/3}\operatorname{Ai}(y\lambda^{2/3})
$$
在根满足
$$
u_A=(D_+-D_-)/(2i),\qquad
\partial_\xi u_A=-c\lambda^{1/3}\operatorname{Ai}'(0).
\tag{9.1}
$$
所以在本文同一个完整 Airy frame 中，理想 Ai 图确实是
$z_-=-z_+$，非零频率的 normalized DN 确实是 $c_AI$。
这只固定理想图及符号，并未将实际正组件替成它。

实际验证应使用同一个 full 正组件 Green 算子 $G$、Poisson
算子 $\mathcal H$ 与完整 source contact $\mathcal K_E$。
设实际正侧有限 Taylor/cutoff Ai 试解为 $\mathcal Q_A$，本端
height 为 $A_A$，另一端 height 为零，完整本端 conormal 为
$C_A$，实际 residual 为 $f_A=P\mathcal Q_A$。则真实 Dirichlet
唯一性给准确恒等式
$$
\mathcal H_{(A_Ah,0)}=\mathcal Q_Ah-Gf_Ah,
\qquad
C_A-\Lambda_{ii}A_A=(\mathcal K_E)_i f_A.
\tag{9.2}
$$
另一端 flux 也由同一个 $\mathcal K_E f_A$ 给出，不能删除。
contact 的完整式为
$$
\langle h,\mathcal K_E f\rangle
=\mathfrak e(\mathcal E h,Gf)-\langle\mathcal E h,f\rangle;
\tag{9.3}
$$
只有两项一起才是正确 conormal。

若实际 canonical boundary 表示、normal shear 和有限强 source
界已经证明
$$
f_A:H^s\to L^2H^{s+2/3},\qquad
(\mathcal K_E)_i:L^2H^t\to H^{t+1/3},
\tag{9.4}
$$
那么 (9.2) 的 defect 增益一整阶。还须确认实际 root normal
shear 已准确扣除，试解的非零频率根迹**精确**为
$$
A_A=c\operatorname{Ai}(0)\Gamma^{-1/3},\qquad
C_A=-c\operatorname{Ai}'(0)\Gamma^{1/3},
$$
或另行支付这些根迹差的相应 $4/3$ 阶 normalized 费用；只有
一个未标余项的主项并不够。满足这一门后，左右再作
$\Gamma^{-1/3}$，即可得到所有 root 端口的
$$
\Gamma^{-1/3}\Lambda_{\rm can}\Gamma^{-1/3}
=c_AI+R_{4/3}
\tag{9.5}
$$
相应本端及 cross 结论。这里 $\Gamma e_j=q|j|e_j$ 对
$j\ne0$，其 mean 取一个明确正值；mean/cross 的实际有限列仍保留。
如果一个端点是 regular elliptic cut，其 trace 和归一化按 R36
的 $1/2$ 阶槽另外处理，不能把该端也直接写成 $c_AI$。
实际 Robin 逆须由 R35 证明的同一个 full realization 提供，
再把 (9.5) 变成真实 Cayley 的 $-I+R_{4/3}$，不能仅凭图的
isotropy 声称 onto。

(9.4) 尤其不能只引用一个较弱的 $H^{t-1/3}$ contact 界后宣称
仍有 $4/3$ 阶；其内部 subelliptic 正则及物理 source 换元必须
实际支付。普通有限阶正侧 jet 延拓可使用，不需要去解一个未经
支付的椭圆 Cauchy 问题；但它的残差、角 norm 与两端 shear
仍是输入证书。

因此本文已把负侧 root collar 的首个真实相位及余项支付出来。
还必须把两个 root 的实际正侧响应、严格负区首阶传递、真实
返回共轭和全部组件相接，才能识别完整 scalar feedback 中的
$\phi_0,\beta$。R34 的危险格以及真实有限低块在那之后使用。

## 10. 精度选择与未完成的全域门

若完整接线确实能在同一个实际 frame 中保留 $4/3$ 阶余项，
而完整对角除数有 $\kappa/|j|$ 下界，则余项经该逆后仍增益
$1/3$。按 R41 进行两次一般角图变换时各损 $\varepsilon$，
选择 $0<\varepsilon<1/6$ 仍保严格正增益，可以在实际高切上
吸收。高切以外的完整低块、source、核规范及多个帽的相对
刚体条件全部仍须验证。

这解释了首阶路线为何可能比先构造任意高阶 classical symbol
更省实际正则预算。它不是低幅度或低模式截断论证：这里的
(1.8)–(1.10) 都是全频率准确算子加有强 norm 的余项。但本题
当前候选尚未自动满足正侧、strict bulk、完整反馈及非线性
收敛的全部输入，故本篇仍不满足 README 的完成标准。

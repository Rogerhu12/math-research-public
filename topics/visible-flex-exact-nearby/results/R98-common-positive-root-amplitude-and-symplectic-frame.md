# R98：共同正化根振幅、准确辛框架与有限增广

2026-11-12，visible-exact-astra-f6a2。

**状态：已证明。** 本篇给出同一个真实 canonical 根空间上的准确辛变换，
并对平方根、逆平方根及其与 Airy 三分之一次幂的交换给出强范数。
实际 R99 与第9节的 $v_0$ 重算表支付了 $\delta_5\pm10^{-9}$ 族的正性、交换常数和小的根比较余项。
本篇不把根矩阵恒等式当作已经支付的完整帽反射、外切面匹配或全反馈逆。

关键用途是把正、负两侧共有的 $v_1/(3\lambda^2)$ 根振幅吸收入同一正算子；
它不再作为两个互不相关的二阶误差分别收费。有限低频、根均值、
regular 端口的均值与通量，以及有限列的完整高频尾均保留。

## 1. 同一个角空间和频率约定

令 canonical 根角为 $\phi\in\mathbb R/(\ell\mathbb Z)$，
$q=2\pi/\ell$。本文只用四重对称空间，采用其正交归一基
$e_k(\phi)=\ell^{-1/2}\exp(4iqk\phi)$，$k\in\mathbb Z$。
定义
$$
 \lambda_k=4q|k|\quad(k\ne0),\qquad \lambda_0=1,\qquad
 \Gamma e_k=\lambda_ke_k,\qquad
 \|u\|_{\mathcal H^s}=\|\Gamma^su\|_{L^2(d\phi)}.                 \tag{98.1}
$$
这是本篇所有算子范数的测度和标度；不是物理 $\theta$ Fourier 投影。
在本实际族 $4q>1$，故与通常含均值的 Sobolev 范数等价，转换时仍须保留
$q$ 和根角 Jacobian。

取整数 $K\ge0$，置
$$
 P_h=1_{\{|k|>K\}},\qquad E=I-P_h,\qquad d=2K+1,\qquad
 \Lambda=4q_-(K+1).                                           \tag{98.2}
$$
其中 $0<q_-\le q\le q_+$。令 $v=v_0$、$b=v_1/3$ 为**真实 canonical**
根势及其第一法向导数的三分之一，都是实函数。定义
$$
 P=P_h\Gamma^{-1}M_v\Gamma^{-1}P_h,\qquad
 D=P_h\Gamma^{-1}M_b\Gamma^{-1}P_h,\qquad W=I+D.                \tag{98.3}
$$
$P,D$ 都在同一个 $L^2(d\phi)$ 上自伴，且在 $E$ 上为零。
特别，$W$ 在所有低模（包括均值）上准确等于恒等。

## 2. 由完整 Wiener 和得到的强范数

记
$$
 R_l=1+\frac{|l|}{K+1},\quad
 M_a(t)=\sum_{l\in\mathbb Z}|a_l|R_l^t,\quad
 L_a(t)=\sum_{l\in\mathbb Z}|l|\,|a_l|R_l^t,\qquad t\ge0.        \tag{98.4}
$$
Fourier 系数包括常数项和全部正负 lag。对任意 $s\in\mathbb R$，
$$
 \|D\|_{\mathcal H^s\to\mathcal H^s}
       \le m_s:=\frac{M_b(|s|)}{\Lambda^2},                    \tag{98.5}
$$
$$
 \|P_h\Gamma^{-1}M_a\Gamma^{-1}P_h\|
       _{\mathcal H^s\to\mathcal H^{s+2}}
       \le M_a(|s+1|).                                       \tag{98.6}
$$
证明：若 $|j|,|k|>K$，$l=k-j$，则
$\lambda_k/\lambda_j$ 及其倒数都不超过 $R_l$。
逐 lag 的加权矩阵条目由(98.4)控制，再用移位在 $\ell^2$ 上等距和
绝对求和。这里没有逐列估计到算子估计的未经支付的转换。

准确排序误差
$$
 E_a=P_h[M_a,\Gamma^{-1}]\Gamma^{-1}P_h
$$
满足
$$
 \|E_a\|_{\mathcal H^s\to\mathcal H^{s+3}}
       \le 4q_+L_a(|s|+2).                                  \tag{98.7}
$$
事实上其 $(k,j)$ 条目为
$a_l(\lambda_k-\lambda_j)/(\lambda_k\lambda_j^2)$。
加权三阶后出现
$(\lambda_k/\lambda_j)^{s+2}(\lambda_k-\lambda_j)$，
而 $|\lambda_k-\lambda_j|\le4q_+|l|$。因此(98.7)在同号和异号块上同时成立。

## 3. 实际正性与函数演算

若 $m_0<1$，则
$$
 (1-m_0)I\le W\le(1+m_0)I.                                  \tag{98.8}
$$
定义准确正算子 $A=W^{1/2}$。若某窗口中的 $m_s<1$，
二项式级数在相应 $\mathcal H^s$ 的有界算子范数中收敛，并给
$$
 \|A\|_{\mathcal H^s}\le2-\sqrt{1-m_s},\quad
 \|A^{-1}\|_{\mathcal H^s}\le(1-m_s)^{-1/2},\quad
 \|A-I\|_{\mathcal H^s}\le1-\sqrt{1-m_s}.                     \tag{98.9}
$$
这些级数与 $L^2$ 谱函数演算相同：先在三角多项式上用同一个幂级数，
再由稠密性延拓。负窗口亦由同一绝对矩阵和成立，不把 $H^s$ 上的
非自伴共轭算子错误当成 $L^2$ 正算子。

设 $\mathfrak C_r(T)=\Gamma^{-r}T\Gamma^r-T$。完整三阶交换界为
$$
 \|\mathfrak C_r(D)\|_{\mathcal H^s\to\mathcal H^{s+3}}
 \le B_{s,r}:=4q_+|r|L_b(|s|+|r|+2).                         \tag{98.10}
$$
证明用
$$
 |x^r-1|\le |r|\,|\log x|\max(x^r,1),\qquad
 |\log(\lambda_j/\lambda_k)|
 \le\frac{|\lambda_j-\lambda_k|}{\min(\lambda_j,\lambda_k)}.
$$
加权后的剩余比值至多 $R_l^{|s|+|r|+2}$。$r=0$ 时两侧均为零。
这是一个全矩阵界，未删掉输出均值；事实上该交换算子在低空间准确为零。

若
$$
 m=\max\{m_s,m_{s+3+r}\}<1,
$$
则
$$
 \boxed{\ 
 \|\mathfrak C_r(A)\|_{s\to s+3}
       \le\frac{B_{s,r}}{2\sqrt{1-m}},\qquad
 \|\mathfrak C_r(A^{-1})\|_{s\to s+3}
       \le\frac{B_{s,r}}{2(1-m)^{3/2}}.\ }                    \tag{98.11}
$$
写 $T=\Gamma^{-r}D\Gamma^r$，则
$T^n-D^n=\sum_{i=0}^{n-1}T^i(T-D)D^{n-1-i}$。
在 $s\to s+3$ 上左乘的 $T$ 范数为 $m_{s+3+r}$，
右乘的 $D$ 范数为 $m_s$，故每项的和不超过 $nm^{n-1}B_{s,r}$。
对 $\sqrt{1+x}$ 与 $(1+x)^{-1/2}$ 的绝对二项式系数求导，正好得到
(98.11)。这也逐项说明了有限损失窗口在哪里，而非只说“交换低一阶”。

## 4. 准确的共同辛变换

在完整 Cauchy Hilbert 空间 $L^2(d\phi)\oplus L^2(d\phi)$ 上置
$$
 \mathbb J=\frac1i\begin{pmatrix}0&I\\-I&0\end{pmatrix},\qquad
 \mathscr T=
 \begin{pmatrix}I&P\\0&I\end{pmatrix}
 \begin{pmatrix}A^{-1}&0\\0&A\end{pmatrix}.                   \tag{98.12}
$$
则
$$
 \boxed{\qquad \mathscr T^*\mathbb J\mathscr T=\mathbb J.\qquad} \tag{98.13}
$$
上三角因子使用 $P=P^*$，对角因子使用 $A=A^*>0$ 和
$A^{-1}A=AA^{-1}=I$，分别直接相乘即得。可逆性和 onto 同时成立。
在任意已支付的有限 Sobolev 窗口，其范数由(98.6)、(98.9)给出。
regular 端口的 $(\xi,\lambda)$ 两个真实有限槽可直和附加恒等辛块；
该操作不删除其与根槽的真实 DN 耦合。

准确辛性不是说任意物理半密度拉回在普通 $L^2$ 上酉。
R99 的实际物理 Cauchy 矩阵仍带 $Y_0'$、height、$Y$ 和 $\pi_Y$；
必须按其真实边界测度及共轭密度接入(98.12)。

## 5. 两侧实际试解在根处共有同一振幅

对非零输入频率，R53 的负侧校正试解满足
$$
 (u,p)_{\rm app}(0)=
 \begin{pmatrix}I&S_v\\0&I+S_b\end{pmatrix}(u,p)_{\rm free}(0),
 \qquad S_a=M_a\Gamma^{-2}\Pi_{\ne0}.                         \tag{98.14}
$$
这里 $p=\partial_\xi u$ 是完整第二 Cauchy 槽。
由 $B(0)=-v$、$B_\xi(0)=-v_1/3$、
$C(0)=C_\xi(0)=0$ 和
$p_{\rm free}=-c\lambda^{1/3}Y_\sigma'(0)$ 直接得到(98.14)。

正侧用 $y=-\xi$，第二槽仍取 $p=-\partial_yu$。
R53 的 $B_+=-v+(v_1/3)y$ 与 $C_+=(v_\phi/2)y^2$，以及
R87 物理多项式在根处准确相同的 $B,B_y,C,C_y$ jets，
给出**相同**的(98.14)，而不是相反的 $S_b$。
因此该振幅有真实的双侧来源。

令
$$
 F_a=S_a-P_hS_aP_h=ES_a+P_hS_aE.
$$
它的秩至多 $2d$，而 $F_a$ 的列一般具有无限高频尾。
由(98.7)准确有
$$
 S_a=P_h\Gamma^{-1}M_a\Gamma^{-1}P_h+E_a+F_a.
$$
于是
$$
 \boxed{\ 
 \begin{pmatrix}I&S_v\\0&I+S_b\end{pmatrix}
 =\mathscr T\begin{pmatrix}A&0\\0&A\end{pmatrix}
 +\begin{pmatrix}0&E_v-PD\\0&E_b\end{pmatrix}
 +\begin{pmatrix}0&F_v\\0&F_b\end{pmatrix}.\ }                 \tag{98.15}
$$
这是完整算子恒等式；不是主符号相等。
$PD$ 还有明确四阶界
$$
 \|PD\|_{s\to s+4}\le M_v(|s+3|)M_b(|s+1|).                 \tag{98.16}
$$
低频差量必须在(98.15)的 $S_a$ 层处理。不能先对两个不同的全算子
取平方根，再把平方根之差无证明地称为有限秩。

R53 核心均值列原本取真实自由列，所以 $\Pi_{\ne0}$ 正确地使它不受
$S_a$ 修改。若正帽试解按 R96 把均值输入设为零，该实际有限列与比较
均值列之差要另附到有限增广；它不影响(98.15)的无限高块，也不许可
删除均值的真实方程。两个根和 regular 端口均按这一约定保全。

## 6. Airy balanced frame 及明确阶数

令
$$
 a=\operatorname{Ai}(0)>0,\qquad b_A=-\operatorname{Ai}'(0)>0,\qquad
 c=\sqrt{a/b_A}.
$$
在非零频率上完整自由根 frame 是
$$
 F_A=
 \begin{pmatrix}\Gamma^{-1/3}&0\\0&\Gamma^{1/3}\end{pmatrix}C_A,\quad
 C_A=c\begin{pmatrix}
 a(\sqrt3+i)&a(\sqrt3-i)\\
 -b_A(\sqrt3-i)&-b_A(\sqrt3+i)
 \end{pmatrix}.                                             \tag{98.17}
$$
$\operatorname{Bi}(0)=\sqrt3a$、
$\operatorname{Bi}'(0)=\sqrt3b_A$、$2\sqrt3ab_A=1/\pi$ 给
$$
 \det C_A=-2ic^2/\pi,\qquad
 F_A^*\mathbb JF_A=(2c^2/\pi)\operatorname{diag}(I,-I).        \tag{98.18}
$$
均值使用 R39 的 $c(1+i\sigma\xi/\pi)$，其根矩阵
$C_0=c\left(\begin{smallmatrix}1&1\\i/\pi&-i/\pi\end{smallmatrix}\right)$
具有相同的通量常数。由于 $A$ 在所有低频上准确等于恒等，
这个真实均值块与 $A$ 的交换准确为零。

在 $F_A$ 的 balanced 标度中，$E_v$ 的上右角增益为 $7/3$，
$PD$ 的上右角增益为 $10/3$，$E_b$ 对角增益为 $3$。
例如
$$
 \|\Gamma^{1/3}E_v\Gamma^{1/3}\|_{s\to s+7/3}
 \le4q_+L_v(|s-1/3|+2),                                    \tag{98.19}
$$
而 $PD$ 若统一按 $7/3$ 记，其费用可取
$$
 \Lambda^{-1}M_v(|s+8/3|)M_b(|s+2/3|).                       \tag{98.20}
$$
这些余项输出仍位于 $P_h$，故使用 $\Lambda^{-1}$ 合法；
同样可用 $\Lambda^{-2/3}$ 将 $E_b$ 的三阶嵌入 $7/3$。

共同振幅与自由 frame 的交换准确为
$$
 F_A^{-1}\operatorname{diag}(A,A)F_A-\operatorname{diag}(A,A)
 =C_A^{-1}\operatorname{diag}(\mathfrak C_{-1/3}(A),
                              \mathfrak C_{1/3}(A))C_A.      \tag{98.21}
$$
所以它增益三阶，强界不超过 $\|C_A^{-1}\|\|C_A\|$ 乘以两项
(98.11)的最大值。逆振幅亦然。具体可用
$$
 \|C_A^{-1}\|\|C_A\|
 \le \frac{2(a^2+b_A^2)}{\sqrt3ab_A}<3,                       \tag{98.22}
$$
由上述 Gamma 初值直接验证。均值块在(98.21)为零；
若需要整个自由 frame 的粗条件数，连同均值可安全取 $4$。

正帽的主关系 $a_{\rm out}=-a_{\rm in}$ 同时乘同一个 $A$ 后不变。
这句话仅说明共同振幅不改变主关系。真实余项仍须包含(98.15)、
(98.21)、正侧完整源/contact、负侧强传播余项和外切面匹配。

## 7. 已支付的实际数值窗口

这里使用实际重算文件
[ci-canonical-v1-scaled-Wiener-summary](../notes/2026-11-12-ci-canonical-v1-scaled-Wiener-summary.json)，
其完整报告 SHA256 为
$c736ccff24d8cacc607d5a8f016f66b72a2565112e989ea01e4078c5dc9e1ae6$，
源 SHA256 为
$2d5ee3ff7a16008cdbeeb760b455ce53b0d919c7f7db3ee8d3883828bd5269c4$。
原计算 run 43299719198 的算术成功、发布失败；发布恢复
run 43300446121 准确重用其 artifact 后成功保存。不是由旧摘要拼回报告。

对象为相同准确 affine $\delta_5\pm10^{-9}$ 族：
$$
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 9.720962901467<q<9.720962905773.
$$
报告已经将物理 $v_1$ 经**真实** $H$ 变到 canonical 角，支付了
名义角误差、完整系数 $L^2$ 误差和无限解析尾。表内 Fourier 和已除以3，
所以恰为本篇 $b=v_1/3$ 的(98.4)；不能用物理 Fourier 表替代。

下表全为向外取整后的真实上界。$m_4$ 同时控制全部 $|s|\le4$。

|$K$|$m_0$ 上界|$m_4$ 上界|$L_b(3)$ 上界|$L_b(4)$ 上界|
|---:|---:|---:|---:|---:|
|52|0.163013|0.562317|87527296|4802358382|
|64|0.108380|0.228680|48192638|2157953223|
|96|0.048667|0.060448|15171956|454610095|
|128|0.027517|0.029866|6791922|151874059|
|192|0.012293|0.012564|2298192|33160033|
|256|0.006933|0.007000|1136112|11589197|

特别取 $K=256$，则 $W\ge0.993067I$，并可在所有 $|s|\le4$ 使用
$$
 \|A\|_{\mathcal H^s}<1.004,\qquad
 \|A^{-1}\|_{\mathcal H^s}<1.004,\qquad
 \|A-I\|_{\mathcal H^s}<0.004.                               \tag{98.23}
$$
对 $s=0,r=\pm1/3$，(98.10)只需 $L_b(7/3)\le L_b(3)$；
$q_+<10$ 和 $m<0.007$ 给安全整数界
$$
 \|\mathfrak C_{\pm1/3}(A)\|_{0\to3}<7\,610\,000,\qquad
 \|\mathfrak C_{\pm1/3}(A^{-1})\|_{0\to3}<7\,670\,000.         \tag{98.24}
$$
例如第一项的精确可算表达是
$40(1136112)/(6\sqrt{0.993})$。
乘(98.22)后，Airy frame 中两项均小于 $23\,010\,000$。
这是三阶增益常数；作为仅作用于 $P_h$ 的 $L^2$ 误差，可再除以
$\Lambda^3$，这里 $\Lambda>4(9.72)(257)>9992$。
它不是 $2.3\times10^7$ 的无增益误差。

$K=256$ 只是本篇方便的根幅度切分，不强迫整个物理帽或全部反馈矩阵
采用该截断。$E$ 的真实列可按 R92/R97 保持有限增广并带完整高尾。
(98.19)中的 $v_0$ 一阶 Wiener 矩不能混用 $v_1$ 表。现可直接从
[actual-root-v0-complex-strip](../notes/2026-11-12-actual-root-v0-complex-strip.md)
的完整较宽族证书支付一个保守实际界。其 canonical 归一化角
$\psi=q\phi$ 的条带宽度大于 $.0009097245839404$，
$|v_0|<6004.148324$。安全取 $V_*=6005$、$u_*=9/10000$、
$r=2500/2509$，则
$
 |v_l|\le V_*e^{-4u_*|l|}\le V_*r^{|l|}.                     \tag{98.25}
$
令 $S_j(r)=\sum_{n\ge1}n^jr^n=(r\partial_r)^j[r/(1-r)]$。
全部都是显式正有理函数，故对整数 $p\ge0$
$
 M_v(p)\le V_*\left[1+2\sum_{j=0}^p
          {p\choose j}(K+1)^{-j}S_j(r)\right],\quad
 L_v(p)\le2V_*\sum_{j=0}^p{p\choose j}(K+1)^{-j}S_{j+1}(r).
                                                               \tag{98.26}
$
$K=256$ 时准确有理运算向上取整给：

|$p$|$M_v(p)$ 上界|$L_v(p)$ 上界|
|---:|---:|---:|
|0|3342117|930033642|
|1|6960925|2944101309|
|2|18416572|11500616502|
|3|63166052|54936011898|
|4|276924853|314998997028|

因此(98.7)、(98.16)、(98.19)–(98.20)的实际费用也全部有限且明确。
例如 $s=0$ 的(98.19)可用 $2197440475920$。
该保守解析模界很大，不能称为 $K=256$ 上的小余项。
该界在最初版本中指出了实际有限谱这一改进方向。第9节现已支付完整实际
canonical 系数及全尾，大幅缩小 $v_0$ 的一阶矩；保留本表作为有效的粗界记录。

## 8. 与完整强反馈的准确接口

将(98.15)代入实际两侧 trial Cauchy 矩阵，再用(98.21)把共同 $A$
移到 incoming/outgoing 两个相同的振幅槽，可得到：
一个准确保通量的共同 frame、同侧共同正振幅、明确 $7/3$ 或三阶的
根余项，以及有限秩增广。所有恒等式均在同一 $L^2(d\phi)$
和同一含均值的 balanced frame 中成立。

要由此得到真实反射及全反馈强逆，还必须把以下真实量接入：
正帽完整 scalar/weak-flux 源的 paired 估计及外端 Wronskian；
负组件全部传播和普通源；第9节根比较之外的完整 source/contact；
有限低块及增广列的真实可逆性。这些是独立的实际算子输入，
本篇的正性、辛性和函数演算不代付它们。

R96 的细领口自由截断费用很大，故优先按同一 paired Wronskian
重组并保留外端真实 DN/regular 项。不能把其两个大源项各自估计后，
再凭共同振幅的正性宣布完整反馈已小。


## 9. 实际 $v_0$ 的有限系数、完整尾与更小的根排序费

本节替换第7节最后那张粗解析模表在实际计算中的使用，保留该表作为
先前有效但过大的界。对象、真实角和参数盒均未改变。
新完整报告
[ci-canonical-v0-scaled-Wiener](../notes/2026-11-12-ci-canonical-v0-scaled-Wiener.json)
的 SHA256 为
$3709417eec2b87e21f81f83c05dc83e113fd881984ea2e7de6678cbafe85db68$；
[小表](../notes/2026-11-12-ci-canonical-v0-scaled-Wiener-summary.json)
的 SHA256 为
$66112956b245389aa38c3d07244685ad31c29f7aae0575b8986bf80b54459ce8$。
算法和完整费用见
[actual-v0-and-common-root-budget](../notes/2026-11-12-actual-v0-and-common-root-budget.md)。

先在准确物理有限参考中写 $v_0=5050+(v_0-5050)$。
对余项做同一真实角图的逆映射、完整节点误差、DFT 和解析 alias；
然后只在 canonical 零系数加入**准确整数**5050，并支付保存该系数
的舍入。这不改变实际几何。真余项的 canonical 复模小于467.112549，
真逆角条带大于0.0018609264148；比较、节点和投影的总系数
$\ell^2$ 误差小于 $1.872673\,10^{-5}$。对任意保留点 $J$，
完整矩由下式支付：
$$
 \sum_{|l|\le J}|c_l||l|^\nu R_l^p+
 \epsilon\left(\sum_{|l|\le J}|l|^{2\nu}R_l^{2p}\right)^{1/2}
 +2M\sum_{l>J}l^\nu R_l^p e^{-4ul},\qquad \nu=0,1.          \tag{98.27}
$$
常数5050已经在 $c_0$ 内；最后一项只需真余项的模。
$\nu=1$ 时零系数准确不贡献费用。每个 $J$ 的界都包含所有 Fourier
系数，选择其中较小者不删除尾。因而(98.27)是(98.4)的全矩界。

实际有向结果的安全整数表为：

|$K$|$M_v(3)$|$L_v(3)$|$M_b(1)$|$L_b(3)$|
|---:|---:|---:|---:|---:|
|64|5314|148981|694529|48192638|
|128|5218|22139|693436|6791922|
|256|5192|4520|692884|1136112|

所有表项都是严格上界，$b$ 两列使用第7节的完整实际报告。
例如 $K=256$ 的 $L_v(3)$ 从粗表的 $5.49\,10^{10}$ 降为4520；
这是实际有限谱和全尾的改善，不是舍弃高 lag。

### 9.1. 同一个波空间上的准确分解

令 $\mathcal G=\operatorname{diag}(\Gamma^{1/3},\Gamma^{-1/3})$，
$\overline{\mathscr T}=\mathcal G\mathscr T\mathcal G^{-1}$，
$\mathcal A=\operatorname{diag}(A,A)$，并记(98.14)左侧矩阵为
$\mathscr T_{\rm app}$。定义
$$
 \mathcal R_h=
 F_A^{-1}\mathscr T^{-1}
 \begin{pmatrix}0&E_v-PD\\0&E_b\end{pmatrix}F_A
 +F_A^{-1}\mathcal A F_A-\mathcal A,\qquad
 \mathcal F=
 F_A^{-1}\mathscr T^{-1}
 \begin{pmatrix}0&F_v\\0&F_b\end{pmatrix}F_A.                 \tag{98.28}
$$
于是准确有
$$
 \boxed{\quad
  (\mathscr T F_A)^{-1}\mathscr T_{\rm app}F_A
       =\mathcal A+\mathcal R_h+\mathcal F .
       \quad}                                               \tag{98.29}
$$
左右都在同一个含均值的 $L^2(d\phi)\oplus L^2(d\phi)$ 上。
$\mathcal R_h$ 的输入、输出都在 $P_h\oplus P_h$；
$\mathcal F$ 是有限秩算子而不是有限 Fourier 矩阵。
regular 的 $(\xi,\lambda)$ 两槽可以直和附加，真实 DN 交叉项仍归入
完整反馈方程。

在 $\mathcal H^{7/3}\oplus\mathcal H^{7/3}$ 上有
$$
 \|\overline{\mathscr T}^{-1}\|
 \le t_K:=(1-m_4)^{-1/2}
          \left(1+\frac{M_v(3)}{\Lambda^{4/3}}\right).        \tag{98.30}
$$
证明：$\mathcal G\operatorname{diag}(A,A^{-1})\mathcal G^{-1}$
只需 $A,A^{-1}$ 的 $8/3$、$2$ 窗口，均由 $m_4$ 控制。
逆剪切的上右角是
$-\Gamma^{-2/3}P_hM_vP_h\Gamma^{-2/3}$，其同阶范数由
$M_v(7/3)/\Lambda^{4/3}\le M_v(3)/\Lambda^{4/3}$ 控制。
三角矩阵的范数不超过1加该上右角的范数。

取
$$
 C_K=\frac{2q_+L_b(3)}{3\sqrt{1-m_4}},
$$
则(98.11)、(98.19)–(98.22)逐项给
$$
 \boxed{\begin{split}
 \|\mathcal R_h\|_{\mathcal H^0\oplus\mathcal H^0
                    \to\mathcal H^{7/3}\oplus\mathcal H^{7/3}}
 &\le \mathcal K_K,\\
 \mathcal K_K
 &=3t_K\left[
    4q_+L_v(3)+\frac{M_v(3)M_b(1)}{\Lambda}
       +\frac{4q_+L_b(3)}{\Lambda^{2/3}}\right]
       +\frac{3C_K}{\Lambda^{2/3}},\\
 \|\mathcal R_h\|_{L^2\oplus L^2}
 &\le \mathcal K_K/\Lambda^{7/3}.
 \end{split}}                                               \tag{98.31}
$$
各项的窗口如下。$E_v$ 作用于输入 $\mathcal H^{-1/3}$，
再左乘 $\Gamma^{1/3}$，需 $L_v(7/3)\le L_v(3)$。
$PD$ 在相同上下三分之一次幂之间增益 $10/3$，需
$M_v(8/3)M_b(2/3)\le M_v(3)M_b(1)$，再付 $\Lambda^{-1}$。
下对角 $E_b$ 增益3，需 $L_b(7/3)$，再付 $\Lambda^{-2/3}$。
共同振幅的 Airy 交换亦增益3，费用为 $3C_K$。
这些算子都保持高空间，故最后的嵌入因子合法。
数值3仅用于非零高频上的 $C_A$；真实均值块不产生交换费用。

### 9.2. 完整实际界与可逆的根比较高块

[准确有理预算程序](../scripts/fourfold_phase_common_root_budget.py)
先核两张完整小表的 SHA、准确 affine 对象及频率身份，再用
Python 标准库 Fraction 解析有向小数球。
程序不以浮点数比较任何最终不等式。
实际
[预算报告](../notes/2026-11-12-actual-common-root-high-remainder.json)
支付：

|$K$|$\|\mathcal R_h\|_{0\to7/3}$ 上界|$\|\mathcal R_h\|_{0\to0}$ 上界|$\|(\mathcal A+\mathcal R_h)^{-1}\|_{0\to0}$ 上界|
|---:|---:|---:|---:|
|64|77000000|0.88|16|
|128|8700000|0.021|1.04|
|256|2100000|0.001|1.006|

其中第三列使用**完整**强界除以真实高频下界，不是将增益忽略后
再次估计。$K=128,256$ 的实际有理结果还分别小于
$0.020182714085$ 和 $0.000941293201$。

为使各小数都可直接核对，证明中可只用以下有理数：

|$K$|$\Lambda>L$|$L^{1/3}>r$|$m_4<\mu$|$t_K<t$|$C_K<C$|
|---:|---:|---:|---:|---:|---:|
|64|2527|13.61|0.229|1.316|366000000|
|128|5015|17.11|0.03|1.08|46000000|
|256|9992|21.53|0.007|1.03|7610000|

例如检查 $r^3<L$、$a_i^2(1-\mu)>1$ 和
$a_i(1+M_v(3)/(Lr))<t$ 即支付(98.30)，其中
$a_i=1.139,1.016,1.004$；检查
$(20L_b(3)/(3C))^2<1-\mu$ 即支付 $C_K<C$。
把 $\Lambda$ 的负幂分别换成 $L^{-1},r^{-2},(L^2r)^{-1}$
后，(98.31)的所有运算都是准确有理数。

最后一列还使用 $L^2$ 正性。$K=64$ 可用实际
$m_0<0.10838$，故 $A>0.944I$；另外两行可用
$A>0.984I$、$A>0.996I$。以第三列为误差，
Neumann 级数给该逆界。例如
$(0.944-0.88)16>1$、
$(0.984-0.021)1.04>1$、
$(0.996-0.001)1.006>1$。
低空间上 $\mathcal A+\mathcal R_h$ 准确等于恒等。
这是一个真实可用的根比较逆，尚不包含完整帽或负区传播。

### 9.3. 可直接接入有限 Schur 的增广列

用 $\mathcal E:\mathbb C^d\to E L^2$ 表示准确低 Fourier 注入，
$J_1,J_2$ 表示两槽注入。对 $(a,r)=(v,1),(b,2)$，(98.28)
的有限项可写成下列两个秩至多 $d$ 的积：
$$
 \begin{split}
 U_{a,0}&=F_A^{-1}\mathscr T^{-1}J_r\mathcal E,
 &V_{a,0}&=\mathcal E^*S_aJ_2^*F_A,\\
 U_{a,1}&=F_A^{-1}\mathscr T^{-1}J_rP_hS_a\mathcal E,
 &V_{a,1}&=\mathcal E^*J_2^*F_A .
 \end{split}                                                \tag{98.32}
$$
将四组列并排、四组行上下堆叠，就准确得到
$\mathcal F=UV$，秩至多 $4d=4(2K+1)$。
这里的 $P_hS_a\mathcal E$ 和后续 $\mathscr T^{-1}$ 的作用均保留
**全部**高输出尾。低行 $\mathcal E^*S_a$ 也对完整高输入作用。
这套表示可直接保留为有限增广，而不能裁成某个物理 Fourier 低块。

令 $\mathcal L_0=\mathcal A+\mathcal R_h$。在此根比较问题内，
完整(98.29)可逆当且仅当有限矩阵
$$
 I+V\mathcal L_0^{-1}U                                      \tag{98.33}
$$
可逆；若可逆，标准消元准确给
$$
 (\mathcal L_0+UV)^{-1}
 =\mathcal L_0^{-1}
 -\mathcal L_0^{-1}U(I+V\mathcal L_0^{-1}U)^{-1}
       V\mathcal L_0^{-1}.                                 \tag{98.34}
$$
公式由代入线性方程并设 $z=Vx$ 直接证明，不含谱截断近似。
本篇没有宣称(98.33)已付有限矩阵逆。若正帽 trial 的均值列取零，
与真实自由均值的差另附秩至多2的列；regular 的均值/通量和
另一个根的全部数据也仍须进入全系统。

因此本节真正关闭的是 $v_0$ 大排序费和共同根 frame 的高块门。
R96 的正帽 paired source、外端匹配、负区强传播及全反馈有限
Schur 仍是独立任务，不能从根比较的逆直接升级得到。

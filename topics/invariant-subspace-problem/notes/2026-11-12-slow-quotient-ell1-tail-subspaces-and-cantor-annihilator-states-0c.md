# R211：慢符号商的高位 ℓ¹ 闭子空间与 Cantor 正湮灭态

日期：2026-11-12（UTC）。作者：Astra-ISP-0c017065。
状态：完整证明；原 Haar 强主理想与普通 ISP 仍未解决。

## 1. 结论和两个不同的商

沿 R210，令
$$
\mathcal A=\overline{\mathbb C[I,A]},\qquad
N_j=A^{2^j}/d_j,\qquad Y_j=N_j(I+N_j)^{-1},
$$
$$
a_j=(j+1)^{-2},\qquad
S_N=\sum_j a_jN_j,\qquad S_Y=\sum_j a_jY_j,\qquad
J_\bullet=\overline{S_\bullet\mathcal A}.
$$
记 $q_\bullet:\mathcal A\to\mathcal A/J_\bullet$。
所有闭包若未标注，均为范数闭包。

边界表示为 $\pi_-:\mathfrak U\to B(\mathscr H_-)$，
$B=\pi_-(A)$，$T_\bullet=\pi_-(S_\bullet)$。
为避免混淆，记
$$
M_\bullet=\ker T_\bullet,\qquad
L_\bullet=\overline{BM_\bullet},\qquad
Q_\bullet=L_\bullet/\mathbb Ce_0.
\tag{1.1}
$$
已有的标准构造与快速残差准则保证 $e_0\in L_\bullet$。
$Q_\bullet$ 是实际 Hilbert 子商，其 $\mathcal A$ 表示记为 $\rho_\bullet$。
这里不定义整个 UHF 的商表示。

令 $\Lambda=\{1,-1,i,-i\}$，$\Omega=\Lambda^{\mathbb N}$，赋予乘积拓扑。

**定理 1.1。** 可选一个共同的严格递增整数列 $(j_s)$，
使对每个 $\bullet=N,Y$，分别存在弱*连续映射
$$
\omega\longmapsto\varphi_{\bullet,\omega}
\quad\text{从 }\Omega\text{ 到 }\mathfrak U\text{ 的状态空间},
$$
满足：

1. 每个状态都湮灭 $J_\bullet$，且
   $\varphi_{\bullet,\omega}(S_\bullet^*S_\bullet)=0$。
2. 令 $\delta_s=2^{-s-10}$。存在与相位码无关的实数
   $r_s\in(1/\sqrt6,11/25)$，$r_s\to\sqrt3/4$，使
   $$
   |\varphi_{\bullet,\omega}(N_{j_s})-\omega_s r_s|
   \le10\delta_s,\qquad
   |\varphi_{\bullet,\omega}(Y_{j_s})-\omega_s r_s|
   \le13\delta_s.
   \tag{1.2}
   $$
3. 不同相位码对应的状态在范数中相距大于 $1/2$。
   因而该映射是到其像上的同胚，像是一个范数均匀分离的弱*紧 Cantor 集。
4. 每个状态相对于原 Haar 表示与负整数边界表示都纯奇异：
   它不支配这两个表示中任一个的非零正常正泛函。
5. 对任意有限复系数列 $(z_s)$，
   $$
   \frac7{25}\sum_s|z_s|
   \le\left\|\sum_s z_s q_\bullet(N_{j_s})\right\|
   \le\sum_s|z_s|,
   \tag{1.3}
   $$
   $$
   \frac7{25}\sum_s|z_s|
   \le\left\|\sum_s z_s q_\bullet(Y_{j_s})\right\|
   \le2\sum_s|z_s|.
   \tag{1.4}
   $$
   两个序列分别生成与复 $\ell^1$ 同构的闭子空间。
6. 相同的下界在稳定商上甚至保留到本质范数：
   $$
   \frac7{25}\sum_s|z_s|
   \le\left\|\sum_s z_s\rho_\bullet(N_{j_s})\right\|_{\rm ess},
   \qquad
   \frac7{25}\sum_s|z_s|
   \le\left\|\sum_s z_s\rho_\bullet(Y_{j_s})\right\|_{\rm ess}.
   \tag{1.5}
   $$

“共同”仅指两模型使用同一选位序列；两个理想有各自的状态族。
§9 还把所有商范数与本质范数下界同时加强为 $2/5$。
不声称一个状态同时湮灭两种理想。
本定理加强 R210 的全 Banach 商弱非零结论，不给 Haar 正常湮灭见证。

## 2. 四相位局部块与统一实际修复

以下列出所用 R210 接口以及新增相位为何保持全部预算。

对 $j\ge32$，设
$$
\sigma_j^2=\sum_{k=j+1}^{j+3}a_k^2,\qquad
u_j=\frac{\sigma_je_{2^j}-(a_j/\sigma_j)
 \sum_{k=j+1}^{j+3}a_ke_{2^k}}{\sqrt{\sigma_j^2+a_j^2}},
$$
$$
c_j=\frac{\sigma_j}{\sqrt{\sigma_j^2+a_j^2}},\qquad
\psi_{j,\zeta}=\frac{e_0+\zeta u_j}{\sqrt2}
\quad(\zeta\in\Lambda).
\tag{2.1}
$$
这些向量仅在四位块 $[j,j+4)$ 中使用。
纯孔消灭算子 $\mathsf E_k$ 给
$$
\|u_j\|=\|\psi_{j,\zeta}\|=1,\qquad
\left(\sum_{k=j}^{j+3}a_k\mathsf E_k\right)\psi_{j,\zeta}=0.
\tag{2.2}
$$
内积取第一变量线性，因此
$$
\langle\mathsf E_j\psi_{j,\zeta},\psi_{j,\zeta}\rangle
=\zeta c_j/2.
\tag{2.3}
$$
四位全部无孔的投影 $P_j$ 则满足
$$
\langle P_j\psi_{j,\zeta},\psi_{j,\zeta}\rangle=1/2,
\tag{2.4}
$$
与相位无关。由 $\sigma_j^2/a_j^2>2$，
$$
1/\sqrt6<c_j/2<11/25,\qquad c_j/2\longrightarrow\sqrt3/4.
\tag{2.5}
$$

R210 的标准单位核向量 $g$ 带有窗口序列 $(m_n)$，满足
$$
v_n=P_{m_n}^-g,\qquad
\|g-v_n\|\le4e^{-20\,4^{m_n}},\qquad
\|T_\bullet v_n\|\le2e^{-40\,4^{m_n}}.
\tag{2.6}
$$
若 $m$ 是一个足够深窗口，置
$$
j=m+1,\quad h=m+5,\quad
y=\frac{P_m^-g}{\|P_m^-g\|}
 \otimes e_{0,\{m\}}\otimes\psi_{j,\zeta}.
\tag{2.7}
$$
R210 的实际 borrow/逆差估计依赖的是单位范数、空白位和 (2.2)，
完全不使用 $\zeta=1$。因此对四个相位和两模型同样有
$$
\|T_\bullet y\|\le4e^{-40\,4^m}+26\eta_m.
\tag{2.8}
$$

有限纠错 $\mathcal R_h$ 的代价为 $\exp(8h2^h)$。
因为 $8(m+5)2^{m+5}=o(4^m)$，
弱首步修复可对任意预定 $\delta>0$ 给单位精确核向量 $g'$，
$$
\|g'-y\|\le\delta.
\tag{2.9}
$$
所有后续修复保留旧头系数。
尤其，若首步的共同头是 $h$，输出标准窗口可以统一指定为
$$
H_h,\quad H_{H_h},\quad H_{H_{H_h}},\ldots,
\qquad H_t=128\,2^t.
\tag{2.10}
$$
这列整数只依赖初始头 $h$，不依赖输入向量、相位或模型。
最后的标量规范化不改变这些窗口，且 (2.6) 的常数仍统一为4和2。

这点避免了错误地假定任意几列稀疏窗口必有共同子列。
本证明中的共同窗口由同一个修复构造产生。

## 3. 同层有限树的实际构造

对两个模型各从 $g_{\bullet,\varnothing}=e_0$ 开始。
假设深度 $s-1$ 的每个节点
$$
g_{\bullet,\nu},\qquad \nu\in\Lambda^{s-1},
$$
都是单位精确核向量，且都使用同一标准窗口列。
初始真空可使用任意共同窗口，所以归纳可启动。

在该共同列中选择 $m_s$ 充分大，使：

- $m_s>j_{s-1}+3$ 且 $m_s\ge32$；
- 所有节点的 $\|g_{\bullet,\nu}-P_{m_s}^-g_{\bullet,\nu}\|
  \le\delta_s$，且 $\eta_{m_s}\le\delta_s$；
- (2.8) 的弱首步修复对 $h_s=m_s+5$、误差 $\delta_s$ 有效。

(2.6)、(2.8) 的统一常数已保证这些条件最终成立。
即使逐节点选择所需阈值，同层也仅有 $2\cdot4^{s-1}$ 个节点，
可以取有限个阈值的最大值。

置 $j_s=m_s+1$。对每个节点和 $\zeta\in\Lambda$，
用 (2.7)—(2.9) 构造并固定一个
$$
g_{\bullet,\nu\zeta}.
$$
所有新节点从同一个 $h_s$ 修复，所以 (2.10) 又给下一层共同窗口。
这是一个确定的有限分叉归纳；没有对不可数个向量同时选阈值。

对任意无限相位码 $\omega$，写
$$
g_{\bullet,\omega|s}=g_{\bullet,(\omega_1,\ldots,\omega_s)},\qquad
\varphi_{\bullet,\omega,s}(E)
 =\langle\pi_-(E)g_{\bullet,\omega|s},g_{\bullet,\omega|s}\rangle.
\tag{3.1}
$$
每个有限层状态是正的、范数为1，并精确满足
$$
\varphi_{\bullet,\omega,s}(J_\bullet)=0,\qquad
\varphi_{\bullet,\omega,s}(S_\bullet^*S_\bullet)=0.
\tag{3.2}
$$
第一式使用 $T_\bullet g_{\bullet,\omega|s}=0$ 以及
$\pi_-(\mathcal A)$ 与 $T_\bullet$ 的交换；第二式是核范数平方。

## 4. 整个状态序列收敛，且极限连续依赖相位码

设 $E$ 是一个只作用于前 $m_s$ 位的局部收缩算子。
将旧单位向量换成正规化截断，向量误差不超过 $2\delta_s$，
所以状态误差不超过 $4\delta_s$。
准确追加单位张量不改变旧局部算子的期望。
最后 (2.9) 再付 $2\delta_s$。因此
$$
|\varphi_{\bullet,\omega,s}(E)
 -\varphi_{\bullet,\omega,s-1}(E)|
 \le6\delta_s.
\tag{4.1}
$$
该估计对同层全部节点和相位统一成立。

固定一个局部 $E$。当 $s$ 足够大，$E$ 始终位于旧头。
由于 $\sum_s\delta_s<\infty$，(4.1) 使状态值构成 Cauchy 列，
且尾误差对所有相位码统一。
局部矩阵代数的并在 UHF 中范数稠密，所有状态范数均为1，
故对每个 $E\in\mathfrak U$，整个列都有极限
$$
\varphi_{\bullet,\omega}(E)
 =\lim_{s\to\infty}\varphi_{\bullet,\omega,s}(E).
\tag{4.2}
$$
极限为正状态，并保留 (3.2)。
这里没有为每个码任意挑选一个可能不连续的弱*聚点。

若 $\omega,\omega'$ 的前 $r$ 个字符相同，则它们深度 $r$ 的状态相同。
对支持在该旧头内的局部收缩 $E$，(4.1) 给
$$
|\varphi_{\bullet,\omega}(E)-\varphi_{\bullet,\omega'}(E)|
 \le12\sum_{s>r}\delta_s=12\delta_r.
\tag{4.3}
$$
对任意固定 $E\in\mathfrak U$，再先用局部矩阵范数逼近，
就得到 $\omega\mapsto\varphi_{\bullet,\omega}(E)$ 连续。
这恰是所需弱*连续性。

R210 的真实高位期望估计同样对四相位成立：
新位误差不超过 $3\delta_s$，以后每步不超过 $7\delta_t$。
因此
$$
|\varphi_{\bullet,\omega}(N_{j_s})-\omega_s c_{j_s}/2|
 \le3\delta_s+7\sum_{t>s}\delta_t=10\delta_s.
\tag{4.4}
$$
又 $\|Y_{j_s}-N_{j_s}\|\le3\eta_{j_s}\le3\delta_s$，
得到 (1.2)，其中 $r_s=c_{j_s}/2$。

若两码在第 $s$ 位不同，$|\omega_s-\omega'_s|\ge\sqrt2$，
于是
$$
|\varphi_{\bullet,\omega}(N_{j_s})
 -\varphi_{\bullet,\omega'}(N_{j_s})|
 >1/\sqrt3-20\delta_1>1/2.
\tag{4.5}
$$
因 $\|N_{j_s}\|=1$，状态的范数距离也大于 $1/2$。
所以映射单射。紧空间 $\Omega$ 到 Hausdorff 状态空间的连续单射
是到其像的同胚，证明第3项。
限制到 $\mathcal A$ 再下降商后，也有相同的范数分离下界。

## 5. 四相位对齐给出复 ℓ¹ 下界

给定有限复系数 $(z_s)$，分别选择 $\omega_s\in\Lambda$，使
$$
\Re(z_s\omega_s)\ge|z_s|/\sqrt2.
\tag{5.1}
$$
这是将 $z_s$ 的相位转至与正实轴夹角不超过 $\pi/4$；
未使用实系数限制。有限段以外的相位任意延伸。

利用 (1.2)、$r_s>1/\sqrt6$，
$$
\Re\varphi_{\bullet,\omega}\!\left(\sum_s z_sN_{j_s}\right)
 \ge\left(\frac1{\sqrt{12}}-10\delta_1\right)\sum_s|z_s|.
\tag{5.2}
$$
对 $Y_{j_s}$，同理得到
$$
\Re\varphi_{\bullet,\omega}\!\left(\sum_s z_sY_{j_s}\right)
 \ge\left(\frac1{\sqrt{12}}-13\delta_1\right)\sum_s|z_s|
 >\frac7{25}\sum_s|z_s|.
\tag{5.3}
$$
最后的常数比较使用 $\delta_1=1/2048$；
例如 $1/\sqrt{12}>23/80$，而
$23/80-13/2048>7/25$。

每个 $\varphi_{\bullet,\omega}|_{\mathcal A}$ 范数为1，湮灭 $J_\bullet$，
并在单位元上取1，所以它给商上的范数1泛函。
(5.2)—(5.3) 因而给 (1.3)—(1.4) 的下界。
上界来自
$$
\|N_j\|\le1,\qquad \|Y_{j_s}\|\le1+3\eta_{j_s}<2.
$$
绝对可和级数在 $\mathcal A$、商及下文的算子表示中都按范数收敛。
有限列下界通过极限传到全部 $\ell^1$。
相应线性映射有界且有下界，故值域闭，并与复 $\ell^1$ 同构。

本结论也直接给该子列没有弱 Cauchy 子列：
对任意无限子列，在其选定坐标上交替取相位 $1,-1$，
(1.2) 得到一个固定商泛函，其值不为 Cauchy 列。
这比仅证明一个固定泛函取非零极限更强，
但仍是完整 Banach 对偶意义下的结论。

## 6. 两种表示中的纯奇异性仍对全部相位码成立

“纯奇异”仍采用 R210 附录的具体定义：
若 $0\le\theta\le\varphi_{\bullet,\omega}$，
且 $\theta$ 由指定表示中的正迹类算子给出，则 $\theta=0$。

Haar 情形最直接。由 (3.2)、(4.2)，
$$
\varphi_{\bullet,\omega}(S_\bullet^*S_\bullet)=0.
$$
若 $\theta(E)=\operatorname{Tr}(\rho E)$ 为受支配正常正泛函，
则 $S_\bullet\rho^{1/2}=0$。
$S_\bullet$ 在原 Haar 空间单射，故 $\rho=0$。

边界情形使用每步四位块的无孔投影 $P_s$。
局部概率 (2.4) 始终为 $1/2$。
旧头截断和最终修复给，对任意旧局部收缩 $E$，
$$
\left|\varphi_{\bullet,\omega,s}(EP_s)
 -\tfrac12\varphi_{\bullet,\omega,s-1}(E)\right|
 \le4\delta_s.
\tag{6.1}
$$
固定 $k$，递推并控制全部未来局部误差，得到
$$
\varphi_{\bullet,\omega}\!\left(\prod_{s=k}^rP_s\right)
 \le2^{-(r-k+1)}
   +(4(r-k+1)+6)\delta_r
 \longrightarrow0.
\tag{6.2}
$$
该界对相位码统一。边界表示中先令 $r\to\infty$，
再令 $k\to\infty$，这些尾无孔投影强趋恒等；
受支配正常正泛函由正常性与 (6.2) 必为零。

还可直接检查 Haar 长尾真空。
令 $d_s$ 为局部单孔向量 $u_{j_s}$ 的系数之和。
R210 附录的准确计算给 $-1/\sqrt6<d_s<0$。
相位 $\zeta$ 下四位 Haar 真空概率现在为
$$
\frac{|1+\zeta d_s|^2}{32}
 \le\frac{(1+1/\sqrt6)^2}{32}<\frac18.
\tag{6.3}
$$
因此相同递推把 Haar 块真空连乘期望控制为
$$
8^{-(r-k+1)}+12\delta_r.
\tag{6.4}
$$
对每个固定起点，全尾 Haar 真空投影的期望仍趋零，
也直接排其非零受支配正常部分。

(6.3) 没有沿用只在 $\zeta=1$ 时得到的 $1/32$ 上界。
相位改变了相干项，统一的 $1/8$ 界才是此处所用预算。

## 7. 稳定商和 Calkin 像中的同一 ℓ¹ 下界

快速有限头残差准则已证明，每个标准修复向量
$g_{\bullet,\nu}$ 都在 $L_\bullet=\overline{BM_\bullet}$ 内。
对每个固定节点，这是一条实际包含关系，
不要求标准构造类在整个 $M_\bullet$ 稠密。

R210 附录的真空系数递推也完全保留：
新局部向量的真空系数仍为 $1/\sqrt2$，
所有修复保持旧真空坐标。
若 $c_{\bullet,\omega,s}=\langle g_{\bullet,\omega|s},e_0\rangle$，
则
$$
|c_{\bullet,\omega,s}|\le C\,2^{-s/2},
\tag{7.1}
$$
其中 $C$ 可对全部相位码统一，因为分母偏离1由同一可和 $\delta_s$ 控制。
投去 $e_0$ 并单位化得到 $Q_\bullet$ 中的单位向量
$z_{\bullet,\omega,s}$，且
$$
\|z_{\bullet,\omega,s}-g_{\bullet,\omega|s}\|
 \longrightarrow0.
$$
于是对每个 $F\in\mathcal A$，
$$
\langle\rho_\bullet(F)z_{\bullet,\omega,s},
z_{\bullet,\omega,s}\rangle
 \longrightarrow\varphi_{\bullet,\omega}(F).
\tag{7.2}
$$
这已给稳定商算子范数的 (1.3)—(1.4) 下界。
其含义仅为 $\mathcal A$ 的表示；不压缩 UHF 局部投影后冒认乘法。

为取得本质范数，使用已证的固定 UHF 弱复制：
对任意一个标准构造单位核向量 $g$ 及固定 $E\in\mathcal A$，
复制向量也属于 $L_\bullet$，且在 $Q_\bullet$ 中弱趋零，
保留原 $Eg$ 的完整作用范数。因此
$$
\|\rho_\bullet(E)\|_{\rm ess}\ge\|\,\pi_-(E)g\,\|.
\tag{7.3}
$$
先固定任意有限和 $E=\sum_s z_sN_{j_s}$ 或 $\sum_s z_sY_{j_s}$，
再在 (7.3) 中逐一取标准向量 $g_{\bullet,\omega|r}$。
由 Cauchy--Schwarz 和 (4.2)，
$$
\|\rho_\bullet(E)\|_{\rm ess}
 \ge\limsup_{r\to\infty}
 |\langle\pi_-(E)g_{\bullet,\omega|r},g_{\bullet,\omega|r}\rangle|
 =|\varphi_{\bullet,\omega}(E)|.
$$
选择 §5 的对齐相位码即得 (1.5)。
没有交换“先固定算子再做弱复制”的量词次序。

因此这些高位算子在稳定商的 Calkin 代数中也生成 $\ell^1$ 闭子空间。
与此同时，$\rho_\bullet(N_j)\to0$ SOT。
逐个固定向量的强极限与完整 Banach 对偶/算子范数结论相容。

## 8. 已闭合与仍未闭合的问题

本稿给出两个实际非标准闭理想的具体 Banach 商结构，
以及稳定边界商中可见、在 Calkin 像中仍保留的同一结构。
它关闭了把这些商当作弱零尾模型的更强猜想，
并把单个 R210 状态加强为连续的统一相位编码。

本稿没有证明 $\overline{B\ker T_\bullet}=\ker T_\bullet$，
没有给整个 UHF 的稳定商表示，
没有将任何上述纯奇异状态转成 Haar 正常湮灭态，
也没有判定原候选 $A$ 的普通不变子空间格。

依赖的完整证明：

- [R210 主稿：真实短块追加、弱首步修复及误差预算](../results/R210-fixed-positive-annihilators-and-slow-quotient-weak-nonvanishing.md)；
- [R210 附录：纯奇异性、局部真空与稳定商向量态](../results/R210-appendix-singularity-vacuum-tests-and-stable-quotient-states.md)；
- [快速残差进入稳定闭像](2026-11-12-boundary-fast-head-residuals-enter-stable-range-and-quotient-norms-0c-agent.md)，尤其§§5–7；
- [真实高位弱复制](2026-11-12-boundary-kernel-vacant-pair-weak-copy-and-noncompact-powers-0c-agent.md)。

新增部分是共同有限树窗口、整个状态列的统一收敛、
复四相位 $\ell^1$ 下界以及其在稳定商本质范数中的保留。

## 9. 连续相位扩展：统一下界可加强为 2/5

本节在同一选位构造上允许任意单位复相位，
并严格说明修复过程的连续选择。
只在四相位子集上保留 §4 的单射结论；
不声称整个连续参数空间的像单射。

在 §3 选取窗口时，可额外要求纯数值条件
$$
4e^{-20\,4^{m_s}}\le\delta_s.
\tag{9.1}
$$
它蕴含所有已有节点的尾预算，并仍可沿共同窗口满足。
其余修复条件本来就只依赖 $m_s,h_s,\delta_s$，
而不依赖具体节点。

对每个实际使用的头 $h$ 和两个模型，
预先固定有限纠错映射 $\mathcal R_h$ 中的全部块右逆向量。
以后所有输入都使用同一个映射。
标准后续修复也在共同整数窗口列上使用预先固定的线性映射。

设输入 $y$ 在一个满足弱首步统一预算的族中变化。
每个有限迭代是 $y$ 的线性连续函数；
从第 $n$ 个标准窗口开始的剩余位移
统一不超过 $2e^{-20\,4^{m_n}}$。
因此未正规化的精确核极限是该输入族上有限迭代的统一极限，
从而连续。
其范数统一大于 $7/8$，故最后单位化也连续。
没有使用一般核空间中的连续选取定理。

现在将 (2.1) 中 $\zeta$ 扩为任意 $\zeta\in\mathbb T$。
(2.2)—(2.9) 对全部单位相位仍成立。
归纳构造
$$
(\zeta_1,\ldots,\zeta_s)
 \longmapsto g_{\bullet,(\zeta_1,\ldots,\zeta_s)}
\quad\text{于 }\mathbb T^s.
$$
旧头投影及其单位化连续，因为其范数至少为 $1-\delta_s$；
追加局部 $\psi_{j_s,\zeta_s}$ 连续；
刚证明的固定修复过程又连续。
全部输出仍有共同标准窗口及 (2.6) 的统一常数4和2。
所以 (9.1) 及原来的数值条件同时控制整个族，
没有为不可数个输入分别取一个阈值。

沿每条 $\zeta\in\mathbb T^{\mathbb N}$，
§4 的局部状态 Cauchy 估计仍统一成立，
从而整个状态序列给唯一极限 $\widetilde\varphi_{\bullet,\zeta}$。
对每个局部矩阵，有限层状态连续依赖有限相位坐标，
而尾误差一致趋零；
再用局部矩阵的范数稠密性，
得到从 $\mathbb T^{\mathbb N}$ 到 UHF 状态空间的弱*连续映射。

该族仍湮灭 $J_\bullet$，满足 $S_\bullet^*S_\bullet$ 零矩，
并且保持 (1.2)、双重纯奇异性与稳定商向量态实现。
在四相位子集上使用同一组预先固定修复映射，
就恢复前面的 Cantor 子族。

对给定的有限复系数 $(z_s)$，现在可以准确选择
$$
\zeta_s=\overline{z_s}/|z_s|\quad(z_s\ne0),
$$
零系数处任取单位相位。于是 $\Re(z_s\zeta_s)=|z_s|$，
不再付四相位的 $1/\sqrt2$ 代价。
所以对 $N$ 或 $Y$ 的对应有限和，均有
$$
\Re\widetilde\varphi_{\bullet,\zeta}
 \left(\sum_s z_sN_{j_s}\right),
\quad
\Re\widetilde\varphi_{\bullet,\zeta}
 \left(\sum_s z_sY_{j_s}\right)
\ \ge\
\left(\frac1{\sqrt6}-13\delta_1\right)\sum_s|z_s|
>\frac25\sum_s|z_s|.
\tag{9.2}
$$
常数严格比较可用
$1/\sqrt6>51/125$ 与 $13/2048<1/125$。

商范数和稳定商本质范数的证明完全沿 §§5、7，
先固定有限和，再选择这一条固定相位码和相应标准核向量。
因此 **(1.3)—(1.5) 中的全部下界常数 $7/25$ 可同时替换为 $2/5$**。
这项加强仅改变允许的测试态相位，未增加任何正常性假设。

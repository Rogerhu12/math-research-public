# R263 — 普通完整中央桥梁、三种真实 Cartier 相位及原乘法卷积缺项

日期：2026-11-13。**状态：以下普通测度规范、两个保质量的完整桥梁、正密度素数子类上的三相位、全卷积恒等式及固定二十四次非零缺项均已证明。尚未从三条完整中央零推出该乘法缺项的消失，也没有据此证明主目标。**

本篇在普通素数处工作，不能把 R245/R246 的惰性参考中心值一搬过来。
三条来源始终取 R243/R244 的原归一
$$
A=A_{17}(2z)/16,\qquad B=A_{34}(z),\qquad H=A_{136}(z),\qquad
A,B,H=z^4+O(z^8).
\tag{1}
$$
对应的实际曲线参数分别是
$$
E_{17}:y^2=x^3-17x,\quad
E_{34}:y^2=x^3-34^2x,\quad
E_{136}:y^2=x^3-136x.
\tag{2}
$$
特别，第二条曲线的四次扭曲参数是 $34^2$，不是 $34$。

## 1. 一个共同的普通 Amice 规范

设 $p\equiv1\pmod4$，$p\ge13$，删去以下论证中出现的固定有限坏素数集。
选定 $\mathbb Q(i)\hookrightarrow\mathbb Q_p$，令
$$
b_D=\psi_D(\bar{\mathfrak p})\in\mathbb Z_p^\times,\qquad
\pi_D=p/b_D,\qquad D\in\{0,8,17,34,136\}.
$$
下标 $0$ 表示 $y^2=x^3-x$；下标 $34$ 仍按 (2) 解释。
记 $\mathcal O=\widehat{\mathbb Z_p^{\rm ur}}$，选实际整正式同构
$$
\beta_0:\widehat{\mathbb G}_m\longrightarrow\widehat E_0,\qquad
\beta_0^*\omega_0=\Omega_0\frac{dT}{1+T},\quad \Omega_0\in\mathcal O^\times.
\tag{3}
$$
这里的 $\Omega_0$ 是普通正式周期。原复周期只在 R246 的有限 theta 算子定义中使用。

对本篇实际函数 $G$，令 $\nu_G$ 的 Amice 变换为
$$
\mathcal A_G(T)=G\bigl(\Omega_0\log(1+T)\bigr).
\tag{4}
$$
(4) 通过 $G(\log_{E_0}t)$ 的整椭圆正式级数与 $\beta_0$ 的复合读取。
它不许可把 $p$ 挠点的正式对数代成零后再代入复解析函数。

R51 的正式 $\sigma$ 整性、R115/R243 的实际多项式，证明
$$
\nu_A,\nu_B,\nu_H,\nu_{S_8},\nu_\vartheta
\quad\hbox{均为有界整测度},\qquad
S_8=-y\vartheta\sigma^3,\quad S_8(0)=\vartheta(0)=1.
\tag{5}
$$
各个有限分母都只需加入一个固定坏集合。对 $S_8$，也可直接用
$S_8=t\vartheta^4$、$t^2=1-x^{-2}$、$t(0)=1$ 核实 (5)。

共同尺度的比较是真正的正式群比较。若曲线方程为
$y^2=x^3-\Delta x$，选 $\eta^4=\Delta$，则
$$
I_\eta(x,y)=(x/\eta^2,y/\eta^3),\qquad
I_\eta^*\omega_0=\eta\omega_\Delta,\qquad
\Omega_0=\eta\Omega_\Delta.
\tag{6}
$$
常数项一的参考按 $G_\Delta(z)=G(\eta z)$ 运输；首项 $z^4$ 的截面按
$G_\Delta(z)=\Delta^{-1}G(\eta z)$ 运输。其测度分别等于原共同测度、
或原共同测度乘 $\Delta^{-1}$。这些固定单位不改变中央消失。
此外 (1) 的第一列还有准确的 $2$ 倍缩放及 $1/16$。
没有把 $\eta\notin\mathbb Z_p$ 错当作 $\mathbb G_m$ 的整数乘法。

置 $d=p-1$，定义完整变换
$$
M_G(u)=\langle\nu_G,K_u\rangle,\qquad
K_u(x)={\bf1}_{\mathbb Z_p^\times}(x)\langle x\rangle^{du}.
\tag{7}
$$
它与原 Iwasawa 变量的关系是 $T_{\rm Iw}=(1+p)^{du}-1$。
因此其中央导数非零与原导数非零等价。

对任意 $\lambda\in\mathbb Z_p^\times$，Amice 复合给
$\nu_{G(\lambda z)}=[\lambda]_*\nu_G$，从而准确有
$$
\boxed{M_{G(\lambda z)}(u)=(\lambda^d)^uM_G(u).}
\tag{8}
$$
$[\lambda]_*$ 表示加法群上的乘法缩放。式 (8) 保留了 $u=0$ 的真实质量。

### 1.1 对数伴随仍有完整普通变换

令 $F=S_8^{17}$、$V_8=F'/F$，取 R245 的固定 $C_*$。
在正式圆盘中，$F$ 是整单位，$V_8$ 及其导数的 Amice 变换有界。
若 $r(T)\in1+T\mathcal O[[T]]$，则
$$
\log r(T)=\sum_{n\ge1}\ell_nT^n,\qquad
|\ell_n|_p\le n.
\tag{9}
$$
这是把 $\log(1+v)=\sum_{j\ge1}(-1)^{j+1}v^j/j$ 逐系数展开得到的：
第 $n$ 项只用 $j\le n$，且 $|1/j|_p\le n$。
因此 $C_*$ 给一个阶至多一的分布；它可以作用于所有局部解析函数，特别是 $K_u$ 及其 $u$ 导数。
算子 $\Omega_0^{-1}(1+T)\partial_T$ 与乘一个有界 Amice 级数保持这种多项式增长。

R246 中 $\mathcal V$ 的实际有限平移，作用于 $C_*(2z)$ 时也合法。
其平移点是 $(4a\pm1)P+(4b\pm1)Q$ 型的原 theta 点；
代入 $2z$ 后的两个周期坐标均为奇数除以八，故不落在
$r=(x-1)/(x+1)$ 的零极二挠点。固定坏集合之外，移位后的有理单位
可写成 $r(P)(1+Tq(T))$，其中 $q\in\mathcal O[[T]]$、$r(P)$ 为代数单位。
取实际 $\log_p r(P)$，余下系数仍满足 (9)。
这保留移位对数的常数与线性项；没有沿用惰性情形的二阶零或 Gauss 界。

## 2. 实际普通半平方及两个参考的质量

对 (2) 的三个真实有限 theta 向量，R46 的比较证明在普通处给
$$
\mathscr K_{D,p}(u)=c_{D,p}\,U_{D,p}(u)M_D(u)^2,\qquad
c_{D,p}\ne0,\quad U_{D,p}(0)=1,\quad U_{D,p}\text{ 为解析单位}.
\tag{10}
$$
这里 $\mathscr K$ 是该曲线自己的完整 Katz 反圆分支；$M_D$ 取 (7)
中相应的原列，固定列单位由 (6) 支付。

说明第三条曲线在这里所需的新普通接口。R239/R243 已认定其全权
Yang 向量及实系数平方，且原导子为 $f_{136}=136$。对所有 $4\mid m$，
$2m+1\equiv1\pmod8$，有限角色及导子不变。
Katz 插值中两处普通 Euler 因子准确相同，均为
$$
E_D(m)=1-\frac{\pi_D^m}{b_D^{m+1}}.
\tag{11}
$$
原 theta 平方于是给整个 $\mathbb Z_p$ 上矩的平方乘 $E_D(m)^2$。
取 $m=m_0+(p-1)p^n$，必要时再乘一个固定的二幂消去有限尺度的 tame 部分。
非单位矩及 $E_D(m)-1$ 的误差赋值趋于无穷；单位矩则趋于 (7)。
解析恒等定理得到 (10)。这正是 R46 的密权证明，保留同一正式周期、
两个阶乘、原始导子和全部有限常数。

普通 Selmer 比较也确实适用于第三条曲线。三个 ray class 度分别为
$$
[K(f_{17}):K]=256,\quad [K(f_{34}):K]=512,\quad
[K(f_{136}):K]=2048,\qquad
f_{17}=34(1+i), f_{34}=68, f_{136}=136.
\tag{12}
$$
这由类数一的公式 $Nf\prod_{\mathfrak l\mid f}(1-N\mathfrak l^{-1})/4$ 直接计算。
它们与奇 $p$ 互素。三条曲线的准确秩均为二；已有 CM parity 给正根数。
R40 所核 Perrin–Riou V.8 及 Agboola–Howard Theorem 2.4.17(1)
于是给完整 Selmer 余秩下界
$$
2\le s_{D,p}\le\operatorname{ord}_{u=0}\mathscr K_{D,p}
=2\operatorname{ord}_{u=0}M_D.
\tag{13}
$$
相关 CM 扭点层对 $K$ 阿贝尔，满足该 Perrin–Riou 定理使用的两处局部
Leopoldt 条件，见 R40 §3；此处没有另加高度非退化或 Sha 有限假设。
因此
$$
\boxed{M_A(0)=M_B(0)=M_H(0)=0,\qquad
M_D'(0)\ne0\ \Longrightarrow\ \Sha(E_D/\mathbb Q)[p^\infty]\text{ 有限}.}
\tag{14}
$$
对旧两条曲线已有更强的充要条件；本篇对第三条仅需 (14)。

现在定义**实际**参考质量
$$
m_8=M_{S_8}(0),\qquad m_\theta=M_\vartheta(0).
$$
有准确等式
$$
\boxed{m_8^2=(1-b_8^{-1})^2,\qquad
m_\theta^2=(1-b_0^{-1})^2.}
\tag{15}
$$
证明是在同一完整 theta/Katz 比较中同时读取权零和密正权极限。
参考的整体零次矩都是一；权零插值给固定平方常数乘
$(1-b_D^{-1})^2$，密正权极限给**同一个**固定平方常数乘 $m_D^2$。
该常数非零，故相消。$E_0$ 的参考常数为 $1/4$，见 R60 及其参考笔记；
$E_8$ 的原 rank-zero 向量和非零权零平方已在 R245 §1 及原 E8 参考笔记证明。
$\vartheta(2z)$ 与 $\vartheta(z)$ 的质量由 (8) 相同，故没有额外的二倍尺度。

两条参考曲线都有有理二挠点，故 $a_p$ 为偶数；$p\ge13$ 时
$|a_p|\le2\sqrt p<p-1$，于是 $a_p\not\equiv1\pmod p$。
因 $b_D\equiv a_p\pmod p$，(15) 给
$$
\boxed{m_8,m_\theta\in\overline{\mathbb Q}\cap\mathcal O^\times.}
\tag{16}
$$
它们分别是 $(1-b_D^{-1})$ 的实际带符号值。符号由原 Amice 测度确定；
下文保留 $m_D$，不逐个选择符号，不把它们置成一。
此证明也没有从正权矩擅自删除参考的潜在原点原子。

## 3. 两个保质量、保全部连接的普通完整桥梁

沿用 R245/R246 的实际常数与算子
$$
\alpha=4+i,\quad\bar\alpha=4-i,\quad
a=-\frac{14548243}{4370281080},\qquad
\nabla_8=\partial_z-V_8,\qquad
\nabla_8^2C_*=H-a\frac{S_8(\alpha z)-S_8(\bar\alpha z)}{2i}.
\tag{17}
$$
记
$$
J_8=M_{S_8},\quad J_\theta=M_\vartheta,\quad
D_o(u)=\frac{(\alpha^d)^u-(\bar\alpha^d)^u}{2i},\quad
C_o(u)=\frac{(\alpha^d)^u+(\bar\alpha^d)^u}{2}.
$$
由于 $p\ne17$ 且 $i\in\mathbb Z_p$，(8) 可准确应用于 $\alpha,\bar\alpha$。
于是
$$
\boxed{M_H(u)-\Phi_o(u)=aD_o(u)J_8(u),\qquad
\Phi_o(u)=M_{\nabla_8^2C_*}(u).}
\tag{18}
$$
普通处的因子是 $\alpha^{p-1}$；其中没有惰性规范的除 $17$。

为明确 (18) 的全部转置，令 $\mu=\nu_{V_8}$、$\xi=\nu_{C_*}$。
普通微分满足 $\nu_{G'}=\Omega_0^{-1}x\nu_G$，函数乘法对应
**加法卷积**。因此准确有
$$
\begin{aligned}
\Phi_o(u)={}&\Omega_0^{-2}\langle\xi,y^2K_u(y)\rangle\\
&-\Omega_0^{-1}\langle\mu\otimes\xi,(x+2y)K_u(x+y)\rangle\\
&+\langle\mu\otimes\mu\otimes\xi,K_u(x+y+z)\rangle.
\end{aligned}
\tag{19}
$$
所有和的单位条件与全部 tame 因子都在 $K_u$ 内。
式 (19) 不把卷积和的对数拆成各因子对数。

令 $C_2=C_*(2z)$、$F_2=F(2z)$、$\nabla_2=\partial_z-F_2'/F_2$，定义
$$
\Psi_o(u)=\tfrac14M_{\mathcal V\nabla_2^2C_2}(u),\qquad q_4=4^d.
$$
R246 的原源恒等式 $\mathcal V H(2z)=iA_{17}(4z)/22$ 与
$\mathcal V N_I=-iO_R$ 给
$$
\boxed{\Psi_o(u)=ia\,q_4^uC_o(u)J_\theta(u)
             +\frac i{22}q_4^uM_{A_{17}}(u).}
\tag{20}
$$
它可逐平移展开而不丢交换差。若 $\mathcal V=\sum_s k_s\mathcal T_s$，
置 $C_s=\mathcal T_sC_2$、$F_s=\mathcal T_sF_2$、$W_s=F_s'/F_s$，则
$$
\mathcal V\nabla_2^2C_2
=\sum_s k_s\{C_s''-2W_sC_s'+(W_s^2-W_s')C_s\}.
\tag{21}
$$
式 (19) 对每个 $(W_s,C_s)$ 逐项应用，再乘 $k_s/4$，就是 (20) 的完整普通转置。
$W_s$ 包括原 theta 平移的线性指数；$C_s$ 包括真实移位后的对数及其常数。

由 (16) 可在原点邻域定义
$$
\widehat\Psi_o(u)=\frac{\Psi_o(u)}{ia\,q_4^uJ_\theta(u)}
=C_o(u)+\frac{M_{A_{17}}(u)}{22aJ_\theta(u)}.
\tag{22}
$$
若三条原完整普通中央导数都消失，则 (8)、(14)、(18)、(22) 给
$$
\boxed{\frac{\Phi_o'(0)}{m_8}
=-\frac{a(p-1)}{2i}\log_p\frac{4+i}{4-i},\qquad
\widehat\Psi_o'(0)=\frac{p-1}{2}\log_p17.}
\tag{23}
$$
这两个量均非零，且由 Brumer 的 $p$ 进对数定理在 $\overline{\mathbb Q}$ 上线性无关。
所需乘法独立性可直接核实：在 $4+i$、$4-i$ 两素位取赋值，
$17^m((4+i)/(4-i))^n$ 为根单位迫 $m+n=m-n=0$。
式 (23) 仍是两个实际伴随行的非零值；尚无已证关系使它们在三中央零下相依。

## 4. 全 Euler 分布及一个特征零三相位算子

对 (1) 的三条原测度，有完整、未作 tame 平均的关系
$$
\boxed{\nu_D|_{p\mathbb Z_p}=b_D^{-1}[p/b_D^2]_*\nu_D.}
\tag{24}
$$
证明沿 R63 的全部 tame 分支论证，下面列明对新来源仍需的步骤。
$i$ 不变性只留下 $4\mid j$ 的分支。原有限向量在所有
$m\equiv j\pmod{p-1}$、$4\mid m$ 上不变，故全 ray Katz 插值与密权比较给
$$
\left(\int_{\mathbb Z_p^\times}x^m\,d\nu_D\right)^2
=(1-b_D^{-1}(p/b_D^2)^m)^2
 \left(\int_{\mathbb Z_p}x^m\,d\nu_D\right)^2.
$$
按 R63 的乘法环带变换取平方根：其目标为整域，单位环带上两测度本来相同，
所以正号是统一的；差只能支撑于零。非平凡 tame 分支先乘 $x^j$，
小球质量趋零及该 tame 特征排除原点项；平凡分支用 (14) 和
$A(0)=B(0)=H(0)=0$ 排除原点项。合成全部分支即 (24)。
这个证明使用三条曲线各自的 $b_D$。

对任意测度定义真正的抽取算子
$$
\psi_p\mu=(x\mapsto x/p)_*(\mu|_{p\mathbb Z_p}),\qquad
\boxed{T_p=b_{17}[b_0^2]_*\psi_p.}
\tag{25}
$$
四次扭曲给 $b_D/b_0\in\mu_4$；$[i]_*\nu_D=\nu_D$。
故 (24) 的缩放 $b_D^{-2}$ 可准确换成共同 $b_0^{-2}$，从而
$$
\boxed{T_p\nu_A=\nu_A,\qquad
T_p\nu_B=(b_{17}/b_{34})\nu_B,\qquad
T_p\nu_H=(b_{17}/b_{136})\nu_H.}
\tag{26}
$$
这是特征零的完整测度等式，尚未取模 $p$。

写 $\chi_2=b_{E_2}/b_0$、$\chi_{17}=b_{17}/b_0$，统一采用
$b_{E_\Delta}/b_0=\chi_4(\Delta)$ 的四次特征约定。
真正的三个参数 (2) 给 (26) 的相位
$$
\boxed{(1,\chi_2^{-2}\chi_{17}^{-1},\chi_2^{-3})
       =(1,\chi_2^2\chi_{17}^{-1},\chi_2).}
\tag{27}
$$
若四次特征用倒数规范，全部相位一同共轭，结论不变。

### 4.1 三相位互异的准确正密度子类

取
$$
\chi_2=\epsilon\in\{i,-i\},\qquad \chi_{17}=-\epsilon.
\tag{28}
$$
它迫 $p\equiv5\pmod8$，而 (27) 变成
$$
(1,-\epsilon,\epsilon).
\tag{29}
$$
这是 $K(\sqrt[4]2,\sqrt[4]{17})/K$ 的一个共轭对 Frobenius 条件。
两个 Kummer 类在 $K^\times/K^{\times4}$ 中独立：在 $17$ 上方任一素位取赋值
先迫 $17$ 的指数为零模四；随后 $2^a$ 为四次幂迫 $a=0\pmod4$。
最后一句对奇 $a$ 可由 $1+i$ 处的赋值排除，对 $a=2$ 则由 $2$ 非 $K$ 中的平方排除。
因此扩张在 $K$ 上次数十六，(28) 非空；其两元素在 $\mathbb Q$ 上组成共轭稳定集合。
Chebotarev 给正密度的有理素数，删去固定坏集合仍无穷。

在该子类上，$T_p^j$ 作用于三个原生成元的首项矩阵为
$$
\begin{pmatrix}1&1&1\\1&-\epsilon&\epsilon\\1&-1&-1\end{pmatrix},\qquad
\det=4\epsilon\in\mathcal O^\times.
\tag{30}
$$
式 (30) 是三个线性特征方向；没有断言 $T_p$ 保持乘法。

### 4.2 同一算子的几何 Cartier 版本

在剩余域中令 $\mathscr G(t)=G(\log_{E_0}t)$。
共同正式同构满足
$\beta_0^{\sigma^{-1}}=\beta_0\circ[b_0]$、
$\Omega_0^{\sigma^{-1}}=b_0\Omega_0$，如 R63 §3。
Cartier 在 Amice 坐标先作 $\psi_p$ 再作系数 $\sigma^{-1}$。
由 (24) 得
$$
\mathcal C(\mathscr G_D\omega_0)
=\frac{b_0}{b_D}\,
\mathscr G_D([b_0/b_D^2]t)\omega_0
=\frac{b_0}{b_D}\,
\mathscr G_D([b_0^{-1}]t)\omega_0.
\tag{31}
$$
这里的正式乘法保留完整 $\mathbb Z_p$ 整数，并非只保留其一次项。
因此
$$
\mathcal U_p(\mathscr G)
=\frac{b_{17}}{b_0}\left(\frac{\mathcal C(\mathscr G\omega_0)}{\omega_0}\right)
\circ[b_0]
\tag{32}
$$
是 (25) 在原 $\mathbb F_p$ 系数函数上的约化。式 (27)–(30) 原样适用。

## 5. 原乘法列中缺少的项：准确的余类卷积公式

以下 $*$ 始终为**加法卷积**。对 $0\le a<p$ 定义
$$
\mu_a=(x\mapsto(x-a)/p)_*(\mu|_{a+p\mathbb Z_p}),
$$
令 $\tau_c$ 表示加法平移 $x\mapsto x+c$。直接按两个加数的剩余类拆分有
$$
\boxed{\psi_p(\mu*\nu)=\mu_0*\nu_0+
\sum_{a=1}^{p-1}(\tau_1)_*(\mu_a*\nu_{p-a}).}
\tag{33}
$$
$\tau_1$ 是真实 carry；不是乘法缩放 $[1]$。

更一般，对 $\ell$ 个因子有
$$
\psi_p(\mu_1*\cdots*\mu_\ell)
=\mathop{\sum_{0\le a_j<p}}_{\sum a_j\equiv0\ (p)}
 (\tau_{\sum a_j/p})_*
 (\mu_{1,a_1}*\cdots*\mu_{\ell,a_\ell}).
\tag{34}
$$
证明是在每个直积余类上写 $x_j=a_j+py_j$；和除以 $p$ 后就是
$\sum y_j+\sum a_j/p$。各余类互不重叠，故这不是近似式。

记 (34) 中除去全部 $a_j=0$ 一项后的和为 $\operatorname{Off}$。
若 $P$ 是齐次 $\ell$ 次多项式，把各单项式的这些和按原系数相加，记为
$\operatorname{Off}_P(\nu_A,\nu_B,\nu_H)$。于是
$$
\psi_p P(\nu_A,\nu_B,\nu_H)
=P(\psi_p\nu_A,\psi_p\nu_B,\psi_p\nu_H)+\operatorname{Off}_P.
\tag{35}
$$
在 $T_p$ 规范下，两个主项之间还必须保留次数因子 $b_{17}^{1-\ell}$。
只在三条一次来源上知道 (26)，不足以删除 (35) 的最后一项。

## 6. 固定二十四次原关系的缺项确实非零，且返回原有限来源

R244 的完整原关系是本原整齐次多项式
$$
\Phi(A,B,H)=0,\qquad \deg\Phi=24.
\tag{36}
$$
仍取 R243/R244 的三个 primitive 角多项式 $a(t),b(t),h(t)$。
它们次数为 $23,23,24$，在 $t=1$ 都等于 $1/5$；无穷点像是 $[0:0:1]$。
本篇固定有理计算给
$$
\gcd_{\mathbb Q[t]}(a^2+b^2,h^2-b^2)=1.
\tag{37}
$$
为给出可重算的整证书，置 $A_*=5a,B_*=5b,H_*=55h$，令
$f,g$ 分别为 $A_*^2+B_*^2$ 与 $H_*^2-121B_*^2$ 的本原部分。
随文 JSON 保存完整整数多项式 $U,V$，满足
$$
Uf+Vg=N,\qquad
N=1076842389698789525286775008137294437105950760118094106143909478400.
\tag{38}
$$
这证明原项目曲线不含 $[1:-i:i]$ 及其共轭；有限点由 (37)，无穷点由上述像排除。
删去 R244 的固定好约化集合及 $N$ 的素因子，模 $p$ 同样成立。

因此在 (28) 的素数子类上，原有限次数二十四列
$$
P_\epsilon=\Phi(A,-\epsilon B,\epsilon H)
\tag{39}
$$
满足
$$
\boxed{[z^{96}]P_\epsilon=\Phi(1,-\epsilon,\epsilon)\in\mathcal O^\times.}
\tag{40}
$$
特别它在原商源 $\mathscr E_{24}$ 中 primitive 且不为零。
没有除去共同径向载体；其真实首阶是 $z^{96}$，原 charge 是二十四倍。

将 (35) 应用于 (36)，再用 (26)，得到一个更强的准确缺项恒等式：
$$
\boxed{
b_{17}[b_0^2]_*\operatorname{Off}_\Phi
=-b_{17}^{-23}\nu_{P_\epsilon}.
}
\tag{41}
$$
证明中 $\Phi(\psi_p\nu_A,\psi_p\nu_B,\psi_p\nu_H)
=b_{17}^{-24}[b_0^{-2}]_*\nu_{P_\epsilon}$。
所以 (41) 保留了全部缩放与二十四次的常数幂。
它表明这个具体非零余类卷积组合确实在支付共同目标自同构后返回原有限来源，
其次数为二十四，不必引入一个任意环境函数。

等价地，(32) 对原零关系的作用为零，而先对三个生成元分别作 (32) 再代入
$\Phi$，得到 (39) 的非零列。这是实际 Cartier 不乘法的一个原源内证书。

## 7. 完整中央零给出的内容与尚未得到的关系

式 (24) 迭代后，三条测度的每个非零环带均有
$$
\nu_D|_{p^n\mathbb Z_p^\times}
=b_D^{-n}[ (p/b_D^2)^n ]_*\bigl(\nu_D|_{\mathbb Z_p^\times}\bigr).
\tag{42}
$$
故三条完整中央零确实迫所有这些环带的质量及归一对数矩为零：
$$
\int_{p^n\mathbb Z_p^\times}1\,d\nu_D=0,\qquad
\int_{p^n\mathbb Z_p^\times}\log_p(x/p^n)\,d\nu_D=0.
\tag{43}
$$
第二式的换元多出 $-2n\log_p b_D$ 乘质量，恰由第一式消去。
所以 (43) 保留了三零的真实全精度内容，未把它弱化成首层测试。

但是 (43) 不逐个指定非零加法余类的测度 $\nu_{D,a}$。
特别，(34) 中对 $\log_p(\sum y_j+\sum a_j/p)$ 的积分不是 (43) 的线性组合。
式 (41) 虽然已经把一个关键组合放回原 $\mathscr E_{24}$，还没有证明
三中央零迫其 Mellin 导数为零，更没有证明其整条测度为零。
首项单位 (40) 也不等于中央 Mellin 导数非零。

因此，若以“只有有限个 good $p$”反设继续，(14) 允许对几乎全部普通及惰性
素数使用三条完整零；在 (28) 这个实际普通子类，还可使用 (23)、(26)、(41)、(43)。
新的确切接口是原非零余类卷积在这些完整零约束下的作用。
把 $T_p$ 当成源代数自同态，或把一次来源的零扩成整个乘法理想，都会直接丢失 (41) 的非零项。

## 8. 证书与一手引用

- [固定精确脚本](../scripts/check-three-source-ordinary-cartier-defect.py) 与
  [完整 Bézout 证书](../scripts/check-three-source-ordinary-cartier-defect.json)。
  脚本只读取 R243 已认证的三个多项式，执行有理 Euclid 运算；没有扫描目标素数。
- A. Agboola、B. Howard，*Anticyclotomic Iwasawa theory of CM elliptic curves*，
  Ann. Inst. Fourier 56 (2006), 1001–1048，Theorems 2.1.1、2.4.17；
  [原刊全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
- B. Perrin–Riou，*Arithmétique des courbes elliptiques et théorie d'Iwasawa*，
  Mémoires SMF 17 (1984)，V.8、V.17；
  [原刊全文](https://www.numdam.org/article/MSMF_1984_2_17__1_0.pdf)。
  本篇对具体原曲线的条件核验见 (12)–(14)，完整 Selmer 比较沿用 R40，
  没有只用 Mordell–Weil 高度替代整个 Selmer 群。
- 全权平方使用 Yang 1997 的原有限向量，具体原归一与证明已分别保存于
  R51、R115、R239/R243；两个实际 log 伴随与有限运输使用 R245、R246。

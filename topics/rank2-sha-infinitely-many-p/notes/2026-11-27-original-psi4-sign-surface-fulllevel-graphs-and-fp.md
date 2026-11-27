# 原 psi4 的 sign 双盖模曲面、严格最高投影与实际图的 fp 公式

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**状态：本文给出新的实际模曲面、完整模形式来源、严格 Chow
最高投影及全部 degree17 图的 proper finite-polynomial 公式。
它不从局部 Hom 或一个正权锚推出中央权斜率非零。**
新源的有限函数、degree102 多项式、两条三挠 Weyl 词及绝对
raw 归一，使用已经发布的
[psi4 来源笔记](2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)，
特别其§10。两个 completion 与 canonical 斜率的纯解析恒等式
使用[单参数 Newton 笔记](2026-11-27-original-psi4-double-slot-newton-and-canonical-slope.md)；
那里§6的几何条件不因本篇一个非零正权系数而自动消失。

## 1. 原 cubic 模曲线与真实 sign cover 的纤维积

始终用原 Tate3 曲面
$$
 y^2+xy+ty=x^3,\qquad
 \omega_t=\frac{dx}{2y+x+t},\qquad D=t(1-27t).
 \tag{1}
$$
原 R991 的 fine 模群和基曲线是
$$
 \Gamma=\{\gamma\in\Gamma_1(3):
 b-c/3\equiv0\pmod3\},\qquad B:v^3=D.
$$
在完整2级上，三个非零2挠点的置换群是
$\mathrm{GL}_2(\mathbf F_2)=S_3$。
取 $A_3$ 商，即真正 sign 双盖。完成平方后，2挠三次式是
$x^3+(x+t)^2/4$；其判别式为
$$
 \operatorname{disc}\!\left(x^3+\frac{(x+t)^2}{4}\right)
 =\frac{t^3(1-27t)}{16}.
$$
因此该双盖的函数域是 $\mathbf Q(t)(\sqrt D)$。
它与原 cubic 层 $v^3=D$ 的纤维积正规化为
$$
 \boxed{\quad C:s^6=t(1-27t),\qquad v=s^2,\qquad
 V=1-54t,\quad V^2=1-108s^6.\quad}
 \tag{2}
$$
相应光滑射影相对极小椭圆曲面记为 $\mathcal T\to C$，
纤维仍是(1)。所以 $C\to X_1(3)$ 的次数是6；
$C\to B$ 才是 sign 双盖。没有把 $C$ 误称为全 full2 曲线：
完整2级先保留，(2)是它的 $A_3$ 商与原9级层的纤维积。

等价地，实际经典群是
$$
 \Gamma'=\Gamma\cap
 \ker\bigl(\mathrm{SL}_2(\mathbf Z)\longrightarrow
       \mathrm{SL}_2(\mathbf F_2)\xrightarrow{\mathrm{sgn}}\{\pm1\}\bigr).
 \tag{3}
$$
原 $\Gamma$ 没有椭圆稳定子，也没有负抛物 lift；
(3)继承这两点。因此(2)所用的是原正 universal family，
没有额外二次扭曲的 starred 纤维。

双盖 $C\to B$ 仅在原两 cusp 分歧。
原 $I_9,I_3$ 因而变为 $I_{18},I_6$；原好纤维的逆像仍好。
Riemann--Hurwitz 给 $g(C)=2$，纤维 Euler 数为24，故
$$
 \chi(\mathcal O_{\mathcal T})=2,\qquad
 q(\mathcal T)=2,\qquad p_g(\mathcal T)=3,\qquad b_2=30.
 \tag{4}
$$
这里 $q=g(C)$ 可由椭圆曲面公式或 Leray 与负次数
$L^{-1}$ 的 $H^0=0$ 得到，不依赖尚未知的 MW 点。

零截面、纤维、两奇异纤维的非恒等分量已经给
$2+17+5=24$ 个独立 NS 类。
而 $h^{1,1}=30-2\cdot3=24$，所以特征零恰有
$$
 \rho=24,\qquad \operatorname{rank}MW=0,\qquad
 \dim H^2_{\rm tr}=6.
 \tag{5}
$$
这些是原模型上的完整维数计算，不假定另一个 K3 或纯动机逆。

## 2. 三个二形式、有限甲板与两个无穷点

定义真正的几何自同构
$$
 \sigma_2:(s,V,x,y)\longmapsto(-s,V,x,y),\qquad
 \tau_0:(s,V,x,y)\longmapsto(\omega^2s,V,x,y).
 \tag{6}
$$
两者分别为 sign 甲板及原 $v\mapsto\omega v$ 的 order3 lift，
它们交换。这里 $\tau_0$ 保持2级取向；后文 degree17 后读出的
9级操作不应预先叫作 $\tau_0$。

由 $6s^5ds=Vdt$，全二形式的一个基是
$$
 \boxed{\quad
 \Omega_4=\frac{dt}{s^5}\wedge\omega_t
       =6\frac{ds}{V}\wedge\omega_t,\qquad
 s\Omega_4,\qquad s^2\Omega_4.
 \quad}
 \tag{7}
$$
验证正规性须包括两无穷点。令 $z=v/t=s^2/t$、$r=1/t$；
同原好模型有
$$
 Y^2+zXY+(r-27)Y=X^3,\qquad
 \omega_t=z\,\omega_{\min}.
 \tag{8}
$$
在(2)的两个无穷点用 $u=1/s$，有
$V\sim\pm6\delta u^{-3}$、$z\sim\pm3\delta u$，其中同一符号
按 $t=(1-V)/54$ 配对。因此
$(ds/V)\wedge\omega_t$ 在两点各恰有二阶零；
乘以 $s,s^2$ 后零阶分别为1、0。
在有限光滑处及两个半稳定 cusp，(7)同样正规。
三个形式线性独立，结合(4)即是全基。

在该基上，实际 pull 特征为
$$
\begin{array}{c|ccc}
 &\Omega_4&s\Omega_4&s^2\Omega_4\\ \hline
 \sigma_2^*&-1&+1&-1\\
 \tau_0^*&\omega^2&\omega&1 .
\end{array}
\tag{9}
$$
特别 sign 且非平凡3型的全纯线只有 $\Omega_4$。
它与旧 $S$ 的全纯线 $s\Omega_4=\Omega_S$ 不同；
两者的 $\tau_0$ 特征确实相反。

## 3. 完整 q 展开锁定同一 f4 来源

本节的 $q=e^{2\pi i\tau}$ 明确是 R991(30)的
$t=1/27$ 宽度1 Tate cusp。沿原
$$
 u_0=729\left(\frac{\eta(3\tau)}{\eta(\tau)}\right)^{12},
 \qquad t=\frac1{u_0+27}
$$
有 $D=q+\cdots$。在(2)选唯一首项1的支
$$
 s=q^{1/6}+\cdots.
 \tag{10}
$$
$t=0$ 的原 Tate cusp 宽度3，那里是 $s\sim q_{\rm Tate}^{1/18}$；
并未用它替代(10)。

令 $f_4=\theta(\psi_4^2)=\sum a_nq^n$ 为来源笔记的实际
weight3、level108 新形式，$a_1=1$。
以下从其同一有限向量证明整个函数等式，而非从首项猜测。

在2处，归一新向量 $W_2^0$ 的 $K_0(4)$ 特征平凡。
共轭
$$
 \operatorname{diag}(2,1)K_0(4)
      \operatorname{diag}(2,1)^{-1}=K(2)
$$
给 $\pi_2(\operatorname{diag}(2,1))W_2^0$ 的 $K(2)$ 不变性。
$\pi_{4,2}^{K(2)}$ 正是实际 $S_3$ sign 一维类型。
乘 $2^{3/2}$ 后，它的 Kirillov 函数在
$2^{-1}\mathbf Z_2^\times$ 上为 $2^{3/2}$，其余为零。

在3处，取来源笔记(5)的真实 $\theta$ projector，
作用于 $\pi_3(\operatorname{diag}(3,1))W_3^0$，再乘 $3^{3/2}$。
按全局 $\Psi_3(1/3)=\omega^{-1}$，所得 $w^+$ 的 Kirillov
支撑为 $-1/3+\mathbf Z_3$，常数为 $3^{3/2}$；
它的完整延拓是 $D_3\mapsto i$。
这个事实沿 R991 的 compact induction 与 R1006(9)--(11)
证明，不省略243项投影。

在其余有限位取同一标准球。
因 $\psi_4^2$ 在2、3分歧，$a_n=0$ 若 $2\mid n$ 或 $3\mid n$；
对其余非零 $a_n$，CM 理想范数强迫 $n\equiv1\pmod3$。
故全部非零指标都是 $n\equiv1\pmod6$。
将上述真实有限 Whittaker 函数逐项代入全局展开：
可留下的有理指标恰是 $n/6$，
3处条件是 $n/6\in-1/3+\mathbf Z_3$，
2处条件是 $n$ 为奇数。
两个归一因子 $2^{3/2}3^{3/2}$ 与无穷 Whittaker 的尺度相消，
每个留下的系数仍恰为同一个 $a_n$。因此 identity 经典分量
**逐项**等于
$$
                         h_4(\tau)=f_4(\tau/6).
 \tag{11}
$$

该 tensor 的经典角色是
$\mathrm{sgn}_2(\gamma)\theta_3(\gamma)^{-1}$；
其核包含(3)。在 $T:\tau\mapsto\tau+1$ 上，2处是 $-1$，
3处右字符是 $\omega$，所以经典字符为
$-\omega^2=e^{\pi i/3}$。这正是(10)的 $s$，不是旧
$f_{27}(\tau/3)$ 的 $\omega$。
分开读取两个部分，$w^+$ 已在 identity 分量出现，
本次标准 torus 接合不应再插入旧的 $h$。

由(9)，这个全角色在 $H^{2,0}$ 中的空间一维，(11)属于它。
原 R997(24)的 Tate 微分规范在同一宽度1 cusp 给
$\omega_t$ 的原 $\delta$ 因子，而
$dt/s^5=-q^{1/6}dq/q+\cdots$。
所以所有系数、模型及实际微分同时固定为
$$
 \boxed{\qquad f_{\Omega_4}=-\delta\, f_4(\tau/6).\qquad}
 \tag{12}
$$
它也给出精确函数恒等式
$f_4(\tau/6)=f_{27}(\tau/3)/s(\tau)$。
这里一维性仅在已经证明(11)的完整向量及其角色后用于定比例；
不是只凭 CM 无穷型或秩二纯实现认来源。

模曲面的标准 Betti--étale 比较与(11)于是识别该
rank2 summand 为 $\operatorname{AI}(\widehat{\psi_4^2})$，
保2、3处全部局部型。没有使用未经证明的 Chow 比较。

## 4. 严格 Chow 最高投影

用 Kahn--Murre--Pedrini 的同一 $t_2$ 函子与有理系数。
有限自同构(6)在 $t_2(\mathcal T)$ 上给真正的对应；
其群关系在 Chow 层成立，而非只在 realization 中成立。
置
$$
 e_{\rm sign}=\frac{1-\sigma_2^*}{2},\qquad
 e_3=\frac{2-\tau_0^*-\tau_0^{2*}}3,\qquad
 M_4=e_{\rm sign}e_3\,t_2(\mathcal T).
 \tag{13}
$$
两幂等元交换且自伴。(5)、(9)给 $M_4$ 的 realization 恰为
$\Omega_4$ 与其共轭两线，没有遗漏额外 $(1,1)$ 部分。
使用 $t_2$ 的函子性是在其已定义的 Chow 对象上作组合；
不对一个任取的全层 Murre projector作未经证明的平均。

在 $M_4$ 上令
$$
 f=1+2\tau_0^* .
$$
因 $1+\tau_0^*+\tau_0^{2*}=0$，且转置为逆自同构，
$$
 f^2=-3,\qquad f^\dagger=-f,\qquad
 f\Omega_4=-\delta\Omega_4.
 \tag{14}
$$
取源 $A=A_4:y^2=x^3+4$、$\omega_A=dx/(2y)$，
令 $e_A=\pi_1(A)$、$g=[\delta]^*$。
原真正 CM 对应给 $g^2=-3,g^\dagger=-g$、
$g\omega_A=\delta\omega_A$。
于是
$$
 P_{\rm high}=\frac12\left(1+\frac{f\otimes g}{3}\right)
 \tag{15}
$$
是自伴严格 Chow 幂等元。
更精确地置
$$
 e_S^\pm=\frac12(1\mp f/\delta),\qquad
 e_A^\pm=\frac12(1\pm g/\delta),\qquad
 P_\pm=e_S^\pm\otimes e_A^\pm .
 \tag{16}
$$
则 $P_++P_-=P_{\rm high}$、$P_-^t=P_+$，
而 $P_+(\Omega_4\omega_A)=\Omega_4\omega_A$。

在实际 cycle/push 上，
$$
 \tau_{0,*}|_{e_S^-}=\omega^2,\qquad
 [\omega]_{A,*}|_{e_A^-}=\omega.
 \tag{17}
$$
第一个式子由 $e_S^-$ 选 $\tau_0^*=\omega$ 再取逆得到；
第二个是原 $[\delta]^*$ 在 Picard/cycle 上为对偶同源的
同一规范，见 R1043(25)--(26)。
因此(17)不能由经典 $T$ 字符直接替代。

令 $\chi_{4,p}$ 是 $T_pA_4$ 的原算术 CM 角色。
由(11)和 $H^1(A)$ 的对偶，$P_-$ 在 $H^3(2)$ 中并作
$e_{\eta_k}$ 后准确给
$$
 V_{k,p}^{\rm new}=
 \eta_k^{-1}\chi_{4,p}^{\,3}\varepsilon_p^{-1}
 =\widehat{\lambda_k}\,\varepsilon_p^{-1},
 \qquad \lambda_k=\psi_4^4/\psi_k .
 \tag{18}
$$
这保完整新 $\eta_k=\psi_k/\psi_4$。
混合部分包含原 $\beta_k$；尤其 $\beta_1=\psi_{17}$ 的
Selmer 不可用旧 R998 的 $\beta_{27,j}$ 消失结论删除。
本篇用(15)--(16)的严格对应自行剥离最高部分。

## 5. 真实 CM 基点、所有核与有限域

全局固定一个有限 Galois 扩张 $L/K$，
包含 $A_4[306]$、三个 $H_k=K(\eta_k)$ 以及规范商图。
各 $H_k/K$ 为阶6的实际角色域，未用旧十八阶域替换。
可令 $L$ 为这些有限域的 Galois 合成；之后不随 $p$ 换源。

标准 torus 与 $w^+$ 的有限3接合是
$$
 g=P=\begin{pmatrix}1&-1\\1&1\end{pmatrix}.
$$
须从 Hsieh§4.1、§4.4的定义直接读取级点：
$\eta_g(e_i)=p_\tau(e_i g')$，$g'=\det(g)g^{-1}$。
所以把两点堆成列时是 $g'(\tau,1)^T$，而不是将点的横排
再直接右乘 $g'$。本次
$$
 \boxed{\quad
 \beta_9=((1+\omega)u_9,(1-\omega)u_9)^T,\qquad
 g'=\begin{pmatrix}1&1\\-1&1\end{pmatrix}.
 \quad}
 \tag{19}
$$
旧 $Ph$ 的 $g'$ 对称，故此区分不改变旧 R1006 的基；
新 $P$ 不对称，必须逐项使用(19)。

第二个3挠点仍在 $\ker[\delta]$，所以原 $t$ 点为 $\infty$。
它在(2)有两个 sign 取向。固定 $u_2=(-\sqrt[3]{4},0)$
及 $(u_2,\omega u_2)$ 的实际 full2 基；其有序根的
Vandermonde固定其中一个取向，另一个由任一 transposition
给出。无需任取一个新的六次根作为源。

对于全部十八个 cyclic17 核 $C\subset A[17]$，
取规范商 $\lambda_C:A\to A/C$，把2级、9级沿它运输，
再忘到(2)，得到 $b_C$ 与实际同源
$$
                     \varphi_C:A\longrightarrow\mathcal T_{b_C}.
 \tag{20}
$$
所有图 degree17。商微分按
$\varphi_C^*\omega_{\varphi_C}=\omega_A$ 固定；若在原模型中
$\varphi_C^*\omega_t=c_C\omega_A$，便用 $\omega_t/c_C$。
不把 degree17 同源当作能自然运输靶 full17 级；
17数据就是这十八个核与原 toric 权。

令 $c_k(C)$ 为来源笔记(6)的全部权，采用同一
$C=\bar uC_0$ 标号及 idèle 角色。
原 $\chi_{k,17}(\omega)=1$，但它在整个十八项商上非平凡。
定义
$$
 \Delta_C=\Gamma_{\varphi_C}
   -17(\mathcal T_{b_C}\times O_A)-(O_{b_C}\times A),\qquad
 Z_k^{\rm raw}=\sum_Cc_k(C)\Delta_C .
 \tag{21}
$$
同一式定义另一 sign 取向的图。

$H^1(\mathcal T)=\pi^*H^1(C)$，因为截面给单射且两边维数均4。
因此其向任何纤维的 restriction 为零；对偶 Gysin 同样为零。
正如 R997(4)--(6)，(21)减掉两个外 Künneth 项后，
剩余纤维 $H^1\otimes H^1$ 的全局循环类也为零。
所以每一条 $\Delta_C$ 已同调零，AJ 在施最高投影前就定义。

完整 full2 sign 词、全十八核重编号、degree17 的
Weil pairing 分量及两个 CM 标量，详见第6节。
其中先施纯三阶谱与源端 $e_A^-$，不含 sign；再施 sign
才选出最高线。其结论准确为
$$
 e_{\rm sgn}Z_k=\frac12(Z_k-\sigma_{2,*}Z_k),
 \tag{22}
$$
其中没有省略十八项，$\frac12$ 来自 $3/6$。
据此定义同一个固定循环
$$
 Y_k=P_-\,e_{\eta_k}\operatorname{Cor}_{L/H_k}
                         e_{\rm sgn}Z_k^{\rm raw},\qquad
 e_{\eta_k}=\frac16\sum_{\gamma\in\operatorname{Gal}(H_k/K)}
                         \eta_k(\gamma)^{-1}\gamma .
 \tag{23}
$$
所有 Galois 作用于几何而固定外系数。
$P_-$、有限图、规范零截面与整个 projector word 均按实际
模问题运输；没有把某一完整 trace 留作球向量。

## 6. Full2 图词的完整次序与绝对系数

本节在真正 full2/full9 cover 上先作三阶谱投影，
不预先假定 sign。原 R1029§6 的完整2挠谱盖可以直接使用：
$$
 \widetilde C:\ 4H^3=A^6-1,\qquad
 r(A,H)=(\omega A,\omega H),\qquad
 j(A,H)=(A^{-1},-H/A^2).
 \tag{A0}
$$
其到(2)的明确映射为
$$
 s=\frac{H}{\delta A},\qquad
 V=\frac{A^6+1}{2A^3}.
$$
代入 $4H^3=A^6-1$ 即得 $V^2=1-108s^6$。
$r$ 固定 $s,V$，$j$ 给 $s\mapsto-s$。
而 $\tau_0$ 在全层是 $(A,H)\mapsto(A,\omega^2H)$，
与 $r,j$ 都交换。故下面各个有限对应是在同一实际
全2曲面上定义的，不依赖已经施加 sign 的结论。
沿 $A_3$ 商推图时，单条源图映到(20)的同一图；
下面 $3/6$ 的全部重数已经显式保留。

### 6.1 级结构与全部核

固定同一个有限域 $L$，包含 $A[306]$ 及下面规范商同源。
新的 identity 经典分量是 $f_4(\tau/6)$。其3处已是
$w^+$，所以标准 torus 的有限矩阵是 $g=P$，不再是旧
$P h$。Hsieh 的级结构定义为
$\eta_g(e_i)=p_\tau(e_i g')$，故把两个点堆成列时必须用
$g'(\tau,1)^T$，其中 $g'=\det(g)g^{-1}$。于是
$$
 g=P=\begin{pmatrix}1&-1\\1&1\end{pmatrix},\qquad
 g'=\begin{pmatrix}1&1\\-1&1\end{pmatrix},\qquad
 \boldsymbol\beta_9=((1+\omega)u_9,(1-\omega)u_9)^T.
 \tag{A1}
$$
旧 $P h$ 的 $g'$ 恰好对称，因此这一行列区别不改变
R1006 的旧基；本次 $P$ 不对称，必须使用上述实际定义。
列向量的每一行记录相应点的像，所以
$$
 [\omega]\boldsymbol\beta_9
 =M_\omega\boldsymbol\beta_9,\qquad
 M_\omega=
 \begin{pmatrix}4&4\\6&4\end{pmatrix}\pmod9.
 \tag{A2}
$$
直接核法是
$\omega(1+\omega)=-(1+\omega)/2-(1-\omega)/2$、
$\omega(1-\omega)=3(1+\omega)/2-(1-\omega)/2$。
因而原 $I^+$ 的 $b-c$ 是 $4-2=2\bmod3$，
读为 $\omega^2$。
这与横排同一基右乘 $M_\omega^T$ 是同一关系；
不能把转置矩阵另塞进同一 $I^+$ 而保留角色不变。
经典 deck 的对应沿 R1043(20)--(21)，本次 $P$ 及
$w^+$ 的区别则必须按(A1)重付。

源 full2 基取 $\boldsymbol\beta_2=(u_2,\omega u_2)^T$。
其 CM 单位矩阵可以取
$$
 r=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
 s=\begin{pmatrix}0&1\\1&0\end{pmatrix}
 \quad\text{于 }\mathrm{GL}_2(\mathbf F_2).
 \tag{A3}
$$
于是 $r^3=s^2=1,\ srs=r^{-1}$，且 sign 在
$\langle r\rangle$ 上为1、在 $s$ 上为负。
CRT 使 $d_r,d_s$ 只改2级，$d_9$ 只改9级。

令 $\mathcal C$ 为 $A[17]$ 的十八个循环子群。
对每个 $C$ 使用真实商
$$
 \lambda_C:A\longrightarrow A_C=A/C.
$$
因17素于18，$\lambda_C$ 把源的2级与9级基同构地送到靶。
这里**没有**把 $A[17]$ 沿 degree17 同源输送为靶的 full17 基；
17处的数据就是 $\mathcal C$ 的全部核标签和原 toric 系数。

取原 $k=1,3,5$ 的 $\chi_{k,17}$，保持其实际
$\mathbf P^1(\mathbf F_{17})$ 规范。写 $c_k(C)$ 为原十八项权。
因原单位表为 $u^{48k}$，有
$$
 \chi_{k,17}(\omega)=1,\qquad c_k(\omega C)=c_k(C).
 \tag{A4}
$$
所有十八项都保留；(A4)并不把另外十七个核任意删去。

### 6.2 真实同源图：先重编号，再合全和

存在由源 $[\omega]$ 诱导的规范同构
$$
 j_C:A_C\longrightarrow A_{\omega C},\qquad
 j_C\lambda_C=\lambda_{\omega C}[\omega].
 \tag{A5}
$$
这不是把 $\omega$ 当作固定靶 $A_C$ 的整自同构：
一般 $A_C$ 只有 conductor17 的 CM order。

记 $b_C$ 为含所运输2级、9级的实际靶模点，
$\Gamma_C$ 为 $\lambda_C$ 在 universal surface 与 $A$
乘积中的图。$j_C$ 把 $A_C$ 的级基送到
$(d_r d_9)$ 作用后的 $A_{\omega C}$ 级基。
因而，返回原标记对象使用 $j_C^{-1}$，对每个 $P\in A$ 有
$$
 j_C^{-1}\lambda_{\omega C}(P)=\lambda_C(\omega^{-1}P).
$$
重新以 $P=\omega Q$ 参数化图，得到严格等式
$$
 (d_r d_9\times1)_*\Gamma_{\omega C}
       =(1\times[\omega])_*\Gamma_C .
 \tag{A6}
$$
这一步同时保留基点、纤维同构与源 CM 作用。

将图改成原修正图
$$
 \Delta_C=\Gamma_C
    -17(S_{b_C}\times O_A)-(O_{b_C}\times A)
$$
不改变(A6)：规范商同构、甲板作用及源 $[\omega]$
均保持零截面，相应纤维也按 $C\mapsto\omega C$ 重编号。

置
$$
 Z_k^{\rm raw}=\sum_{C\in\mathcal C}c_k(C)\Delta_C.
$$
仅在这份**完整和**上使用(A4)，才得到
$$
 \boxed{\quad
 (d_r d_9)_* Z_k^{\rm raw}=[\omega]_{A,*}Z_k^{\rm raw},
 \qquad
 d_{r,*}Z_k^{\rm raw}=d_{9,*}^{-1}[\omega]_{A,*}Z_k^{\rm raw}.
 \quad}
 \tag{A7}
$$
所以先前形式上的“17 deck”在此准确地由核标签的置换支付，
不是一个不存在的靶17级自然推前。

### 6.3 先作三阶谱，再作 sign

令 $\tau_0$ 表示原 $v\mapsto\omega v$ 在新的 full2
sign 曲面上的 order3 lift。若 sign 双盖用
$$
 s_0^2=v,\qquad s_0^6=t(1-27t)
$$
表示，则保持2级 sign 的该 lift 是
$\tau_0:s_0\mapsto\omega^2s_0$。
它不是下面 degree17 靶上直接读得的 $d_9$。

源(A1)的 Weil pairing 指数为 $+2$，degree17 后变成
$34\equiv1\pmod3$。因此分量归一化 $D_{34}$ 在模3
不再反转(A2)已经读出的逆字符。R1043(20)--(21)的同一
几何列基规则准确给出
$$
                       d_9=\tau_0^{-1}.
 \tag{A8}
$$
特别，这里的逆号来自新(A2)的 $b-c=2$，不是旧基
经 $-34$ 分量产生的逆号。原 degree34 输入的旧
$P h$、旧基及 $-68$ 不应搬来。

这里必须在施加 full2 sign **以前**取三阶谱。先在实际
full2/full9 cover 的
$e_{\tau_0\ne1}t_2$ 上使用有限对应幂等元
$$
 Q_\tau=\frac{1+\omega^2\tau_0^*+\omega(\tau_0^*)^2}{3}.
$$
它选 $\tau_0^*=\omega$，还没有施加 $e_{\rm sgn}$，
也不把所得整块称为新的最高线。具体地，在
$V^2=1-108s_0^6$ 的实际形式中，令
$$
 \Omega_0=(ds_0/V)\wedge\omega_{\rm fib},\qquad
 \Omega_1=s_0(ds_0/V)\wedge\omega_{\rm fib}.
$$
则 $\tau_0^*\Omega_0=\omega^2\Omega_0$、
$\tau_0^*\Omega_1=\omega\Omega_1$。因此 $Q_\tau$ 保留
anti-$\Omega_0$ 和 holomorphic $\Omega_1$ 两个伙伴；
不能在此先删除后者。

对 order3 自同构，cycle push 是相应 pull 的逆。
所以这一**未作 sign 投影**的有限幂等元严格给出
$$
 \tau_{0,*}\big|_{Q_\tau}=\omega^2,\qquad
 [\omega]_{A,*}\big|_{e_A^-}=\omega .
 \tag{A9}
$$
第一式由有限对应多项式本身成立，不借最高线已经选出的
假设。第二式沿 R995(18)、R1043(25)--(26)的
原 $e_A^-=(1-[\delta]^*/\delta)/2$ 约定：
它在实际点或 cycle 的 push 上选 $+\delta$，故选 $\omega$；
不能把 H1 pull 的共轭特征代入(A7)。

令 $P_0$ 表示在上述 $e_{\tau_0\ne1}t_2$ 上的
$Q_\tau$ 与源端 $e_A^-$。完整3处 compact 词及其余有限
权仍按原顺序保留；此处只把与 full2 作用交换的这两个
谱投影先实施，**不把 $e_{\rm sgn}$ 放进 $P_0$**。
在 $Z_k=P_0Z_k^{\rm raw}$ 上，由(A8)--(A9)，
$$
 d_{9,*}^{-1}[\omega]_{A,*}
       =\omega^2\omega=1.
$$
因此(A7)先准确给出
$$
                             d_{r,*}Z_k=Z_k .
 \tag{A10}
$$
这个 $C_3$ 不变性在 sign 之前取得。它同时保留新
$P$ 基与 degree17 分量、三阶谱及源曲线 CM push；
不使用旧 degree34 的相位或任何最高 Selmer 分量消失。

### 6.4 六项 sign 平均与取向差

整个 full2 projector是
$$
 e_{\rm sgn}=\frac16\sum_{g\in\mathrm{GL}_2(\mathbf F_2)}
                         {\rm sgn}(g)d_{g,*}.
$$
由(A3)，
$$
 e_{\rm sgn}
  =\frac16(1+d_r+d_r^2)(1-d_s).
$$
(A10)及 $rs=sr^{-1}$ 说明 $Z_k,d_sZ_k$ 都在 $C_3$
不变部分。因此
$$
 \boxed{\qquad
                   e_{\rm sgn}Z_k
                    =\frac12\bigl(Z_k-d_{s,*}Z_k\bigr).
 \qquad}
 \tag{A11}
$$
此时才沿 $A_3=\langle r\rangle$ 商返回上述双盖，并以
$e_{\rm sgn}$ 选真正的
$M_4=e_{\rm sgn}e_{\tau_0\ne1}t_2$ 分量。
双盖反射 $s_0\mapsto-s_0$ 在 $\Omega_0$ 上为负、
在 $\Omega_1$ 上为正，所以(A11)删除前段仍保留的
$\Omega_1$ 伙伴，留下原最高所需的 anti-$\Omega_0$
与源端 $e_A^-$ 组合。这是实际有限 sign 投影的结果，
不借一个旧 Hodge 分量或其 Selmer 群为零。

绝对系数是 $3/6=1/2$；没有另除一个3，也没有从旧三条
degree2商借一个重数。

任一 transposition都是 $r^a s r^{-a}$。由(A10)，
$$
 d_{r^a s r^{-a},*}Z_k=d_{s,*}Z_k .
$$
故(A11)不依赖在三个 transpositions 中选哪一个。
两个项是原 full2 模问题的两个取向；$s$ 不是源 CM
自同构，不能把第二项再识别为第一项或其一个任意标量倍。

上述等式在完整 $L$ 上逐图成立。CM 单位
$[\omega]$ 在 $K$ 上定义，与全部实际 Galois 共轭相容。
Galois 改变 full2 基时至多共轭 $r,s$，而
$e_{\rm sgn}$ 是 $S_3$ 的中心幂等元，(A11)在 C3 不变
部分也不依赖所选 $s$。因此可以原样施以
$$
                         e_{\eta_k}\operatorname{Cor}_{L/H_k}
$$
以及原的其它有限投影；原 Artin 分母只出现它本来的那一次。
这里没有新增一个任取的 $\eta_k(\omega)$，也没有把
17处核权同 Artin projector 混为一项。


## 7. 惰性目标素数处的同一固定图

令 $p\equiv2\pmod3$，排除固定的 $2,3,17$、
所用数域/图/系数的分母及固定光滑模型的有限坏集。
本节不需要旧 R1014 的 $p>q_0$，因为没有使用旧新增 NS
或最短截面的整格结论。取 $K_p=\mathbf Q_{p^2}$，
并固定原 $K$ 嵌入。以下 $F=\varphi^2$ 是未 Tate 扭曲的
晶体 $p^2$-Frobenius。

源 $A_4$ 的完整 Hecke 角色给
$\psi_4((p))=-p$，不是从另一条三次扭曲中借来的 primary
规范。故算术 Frobenius 在 $A_4[N]$ 上为 $[-p]$，
对所有 $N\mid306$ 同时成立。它固定全部十八个 cyclic17
核，在 full2 上为恒等，并在9级上是标量 $-p\equiv1\bmod3$。
该标量在原完整 GL 模群中：$b=c=0$、$a=d=1\bmod3$，
determinant $p^2$ 正是 Weil pairing 的同一变化。
因此它也保持(2)的 sign 取向及 cubic 根。
各同源及其相同模问题的表达在本局部定义于 $K_p$；
全部几何 Galois 共轭同样如此。
这里没有要求原 full306 挠点本身全在 $K_p$。

同时
$$
 \eta_k((p))=\psi_k((p))/\psi_4((p))=1.
 \tag{24}
$$
三个实际椭圆曲线都在该惰性好素数处有平方 Frobenius $[-p]$，
所以(24)保的是完整有限角色，不只是一个残余单位值。

由(11)--(12)的同一模形式实现，在 $M_4$ 上的 Hecke
多项式为 $X^2-p^2$，源 $A_4$ 的为 $X^2+p$。因此
$$
 F|M_{4,\rm cris}=p^2,\qquad
 F|H^1_{\rm cris}(A_4)=-p,\qquad
 F|M_4\otimes H^1(A_4)=-p^3.
 \tag{25}
$$
(18)的真实 $H^3(2)$ 最高线与 Artin twist 上，相应归一化
算子为 $-p^{-1}$。两个 Tate 指数为 $(2,-1)$，
所以 $D_{\rm dR}/\mathrm{Fil}^0$ 是系数域上的一维空间；
$D_{\rm cris}^{\varphi=1}=0$。
Bloch--Kato 基本正合列于是给同一个局部同构
$$
 \exp_{\rm BK}:D_{\rm dR}(V_{k,p}^{\rm new})/\mathrm{Fil}^0
                    \xrightarrow{\ \sim\ }H_f^1(K_p,V_{k,p}^{\rm new}).
 \tag{26}
$$
好模型上实际图的 AJ 位于 $H_f^1$。
(26)仅把此新局部类与其标量等价；没有将它冒充原 rank2
椭圆曲线的 canonical 首导数。

## 8. 新图的 proper fp 原函数及完整杯积

在新 $\mathcal T$ 的 functorial Čech--rigid/de Rham
mapping fibre 中取
$$
 P_T(X)=1-X/p^2,\qquad
 \widetilde\Omega_4=(\Omega_4,\Xi_{4,p}),\qquad
 d\Xi_{4,p}=(1-p^{-2}F)\Omega_4 .
 \tag{27}
$$
这是 $H^2_{\rm fp}(\mathcal T,2)$ 的 lift。
$\Xi_{4,p}$ 是总次数1 cochain，包括1形式、交叠函数和
Frobenius 比较同伦；不声称全曲面有一个全局 Frobenius lift。
存在性来自(25)，因为 $P_T(F)$ 杀掉同一个全纯上同调类。

对于每个实际光滑纤维 $\mathcal T_b$，
令 $\xi_{b,p}$ 是(27)的导出 restriction 的闭
$H^1_{\rm dR}(\mathcal T_b)$ 类。
$\Omega_4$ 限制到曲线为零，故它闭。
若更换(27)，差来自 $H^1(\mathcal T)$；
而 $H^1(\mathcal T)=\pi^*H^1(C)$ 在每个纤维上限制零。
所以 $\xi_{b,p}$ 不含一个任意的水平纤维常数。
更换局部 Frobenius lift 时也必须随同更换比较同伦。

Besser 的 proper 正合列中，注入
$\boldsymbol i$ 在固定多项式模型是 $P_T(F)$。
同源靶的 $H^1$ 上 $F=-p$，因此
$$
 \boldsymbol i^{-1}
       (\widetilde\Omega_4|_{\mathcal T_b})
       =\frac{p}{p+1}\,\xi_{b,p}.
 \tag{28}
$$
此处 Hodge 参数是2，而
$\mathrm{Fil}^2H^1_{\rm dR}(\mathcal T_b)=0$，
所以等式在全 $H^1$ 中成立；随后杯积才只读模
$\mathrm{Fil}^1$ 的商。

在曲线因子取 $H^1_{\rm fp}(A,0)$ 中 $\omega_A$ 的唯一 lift，
其多项式为 $P_A(X)=1+X/p$。
两个参数 $2+0=2$ 正是 codimension2 AJ 的测试次数。
该 $n=0$ lift 限制到 $O_A$ 为零，不另挑常数。

对(21)每条真实 degree17 图，投影公式和 proper fp 杯积给
$$
 \boxed{\quad
 \operatorname{AJ}_p(\Delta_C)(\Omega_4\omega_A)
 =\frac{p}{p+1}
       \left\langle\varphi_C^*\xi_{b_C,p},\omega_A\right\rangle_A .
 \quad}
 \tag{29}
$$
两修正项的贡献严格为零：曲线 lift 在 $O_A$ 的限制为零，
而 $\widetilde\Omega_4$ 向点的 degree2 限制也为零。
degree17 仍完整在 $\Delta_C$ 和真实 pullback 中。

可用同一卷积直接核(29)的符号：
$$
 (P_T*P_A)(X)=1+X/p^3,\qquad
 1+\frac{T_1T_2}{p^3}
   =-\frac{T_2}{p}\left(1-\frac{T_1}{p^2}\right)
       +\left(1+\frac{T_2}{p}\right).
 \tag{30}
$$
所以杯积分子的总 cochain 为
$-p^{-1}\Xi_{4,p}\wedge F\omega_A+\Omega_4\wedge G_p$。
限制到图后第二项为零，第一项在上同调中是
$\varphi_C^*\xi_{b_C,p}\wedge\omega_A$。
trace 前仍要除以 $(P_T*P_A)(p^2)=1+1/p$，
准确得到(29)。不能把这个分子直接改名 AJ。

用 $\epsilon=+,-$ 标记两种 full2 取向，
并将 $\varphi_{C,-}$ 定义为实际 transposition 后的同源图。
令
$$
\begin{split}
 \mathcal I^{\rm new}_{k,p}
  =\frac1{12}\sum_{\sigma\in\operatorname{Gal}(H_k/K)}
      \eta_k(\sigma)^{-1}
   \sum_{\gamma\in\operatorname{Gal}(L/H_k)}
   \sum_{C\in\mathcal C}c_k(C)\,
 \Big(&
 \langle(\sigma\gamma\varphi_{C,+})^*
              \xi_{\sigma\gamma b_{C,+},p},\omega_A\rangle\\
 -&\langle(\sigma\gamma\varphi_{C,-})^*
              \xi_{\sigma\gamma b_{C,-},p},\omega_A\rangle
 \Big).
\end{split}
\tag{31}
$$
$1/12$ 恰是原 $1/6$ Artin projector 与真实 $1/2$ sign；
不是把 full9 的有限向量再任意平均一次。
先在全层施纯 $\tau_0$ 谱投影的各项也按第6节保留；
在(31)中将它移到测试线时作用为恒等。
外系数在几何 Galois 作用下固定，所有十八核和全部
$\gamma$ 重数都保留。

由于 $P_-^t=P_+$ 且 $P_+(\Omega_4\omega_A)=\Omega_4\omega_A$，
(23)、(29)给真正的新循环公式
$$
 \boxed{\qquad
 \operatorname{AJ}_p(Y_k)(\Omega_4\omega_A)
       =\frac{p}{p+1}\,\mathcal I^{\rm new}_{k,p}.
 \qquad}
 \tag{32}
$$
若按指定 Artin de Rham 基下降，仍须乘同一
$a_{k,p}^{-1}$；它不改变 $p/(p+1)$。
这里的 $a_{k,p}$ 属于新 $\eta_k$，
不借旧十八阶来源的 $\sqrt{17}$ 规范。

## 9. 真实后继接口与未预付的非零

(32)是新的 fixed-cycle 局部公式，适用于上述全部好惰性 $p$。
它不使用旧54图的三个 degree2商、旧最短截面 $Q_p$、
旧 NS 判别式或旧 $\beta_{27,j}$ 的 Selmer 消失。
本篇也没有把新源的 $n=4$ 非零当作(32)或其某个权导数非零。

后继 Kriz/fixed-base $p^2$ 权族须使用本篇同一个
$\pi_4$ 向量、(19)基、十八核与两取向、(16)最高投影，
以及来源笔记§10的绝对幅度。
它所要消费的纯解析源已经准确为
$$
                 -3q_\delta^{-v}K_{-,k}(v)J_{S_k}(v),
 \qquad v=(p-1)u,\quad n=(p^2-1)u-2 .
 \tag{33}
$$
对 canonical $k=1$，$J_S(0)=0$，
指定 $u$-斜率含完整因子
$-3(p-1)K_{-,1}(0)J_S'(0)$。
把实际几何族与(33)相认时仍须支付同一局部/公共因子；
不能用旧 full54 的名字代替新有限图。
即使有这种相认，$J_S'(0)$ 在无穷多个不同 $p$ 非零
也仍是需要继续解决的实质门槛。

### 原始来源及本篇的实际使用范围

- R991§6、R997§§2--5：原 cubic 模曲线、Tate3 好模型、
  Betti--étale 比较、原微分的 cusp 规范及修正图的 AJ。
- R1029§6：原2挠完整 $S_3$ 谱盖；
  第6节显示其到(2)的准确代数坐标。
- R995：$t_2$ 的严格对应和 CM 转置约定。
  本篇(13)--(16)另用自己的有限甲板直接构造投影，
  未把旧曲面的三同源对应无理由搬来。
- Hsieh, *Special values of anticyclotomic Rankin--Selberg
  L-functions*, Documenta Math.19 (2014)，
  §§4.1、4.4 的 $\eta_g(e_i)=p_\tau(e_i g')$，
  §5.1 的几何模形式与 Whittaker 归一；
  https://content.ems.press/assets/public/full-texts/serials/dm/19/8965392/online/10.4171-dm-462.pdf 。
- Besser (2016)，(2.1)、(2.5)、(2.7) 的 proper fp 正合列、杯积和注入规范；
  以及 R1049§§2--4 已逐项核读的同一 proper Čech 实现。
  本篇按(25)--(32)对新 $\mathcal T/A_4$ 重新给出全部算子，
  不将一个 affine 公式直接套到 proper 曲面。

本篇没有新增数学程序运行；所有恒等式均由所写模型、有限
对应和已指明原定理证明。

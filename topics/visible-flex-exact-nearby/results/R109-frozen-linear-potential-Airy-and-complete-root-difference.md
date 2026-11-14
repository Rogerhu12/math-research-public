# R109：准确线性势 Airy 试解、真实根差与完整流余项

2026-11-12，independent-audit。

**状态：试解、完整残差、根范数比较及实际系数预算已证明。**
本篇精确吸收根处的常数势和线性势，消去这两项造成的径向近似误差。
使用 R99 的完整真实 Fourier 数据，34 个准确有理数门已实际执行。
它不是完整帽反射或反馈逆；尚未取得新的全领口残差积分。
所有低输出、均值、真实 height/Piola、主矩阵误差和 cutoff 均明确保留。

## 1. 同一个实际算子与逐输入列定义

参数域、真实根、canonical 周期及归一与 R108 相同：
$$
 |\delta-\delta_5|\le10^{-9},\quad
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 \phi\in\mathbb R/((2\pi/q)\mathbb Z).
 \tag{109.1}
$$
真实四重频率为 $4qk$。写 $j\ne0$，
$\lambda=4q|j|$、$\epsilon=\operatorname{sgn}j$。
在已给真实图中，完整 canonical 算子为
$$
 P_*=-\operatorname{div}\big((C_0+E)\nabla\big)+V,\qquad
 C_0=\operatorname{diag}(1,y),\qquad
 V(0,\phi)=-v_0(\phi),\quad V_y(0,\phi)=v_1(\phi).
 \tag{109.2}
$$
选 R96 的真实归一 height 时 $E_{11}=0$。选根匹配四次 height 时
$E_{11}$ 一般非零，必须保留。本篇假设实际图/height 的根匹配已满足
$E_{ab}(0)=\partial_yE_{ab}(0)=0$；R103 给出了这个准确根条件。
不把根 jets 当作全宽领口的误差界。

对每个输入列，定义
$$
 a_j(\phi)=\big(\lambda^2+v_1(\phi)\big)^{1/3},\qquad
 Z_j(y,\phi)=a_j(\phi)y-\frac{v_0(\phi)}{a_j(\phi)^2},
 \tag{109.3}
$$
取正实立方根。令
$$
 U_j^{\rm lin}
   =c\lambda^{-1/3}e^{i\epsilon\lambda\phi}
                  \operatorname{Ai}(Z_j),\qquad
 c=\sqrt{\operatorname{Ai}(0)/[-\operatorname{Ai}'(0)]}.
 \tag{109.4}
$$
这是逐输入的完整符号定义。$\lambda$ 始终是该输入频率；(109.3)
**不是**对非交换算子 $\Gamma^2+M_{v_1}$ 作函数演算。
每个系数乘法在左，输入频率乘子在右。

实际 R99 数据严格给，在 $|j|>64$ 时
$$
 |v_1|<2076981,\qquad \lambda>2527,\qquad
 \|v_1\|/\lambda^2<1/2.
 \tag{109.5}
$$
故 $a_j$ 在全部实际参数和实角上严格正。
下文更强的 scaled Wiener 门也全部通过。

本篇只改变所选高输入列。$|j|\le K$ 的全部真实输入列（含 $j=0$、
regular 均值及通量）保留在有限增广系统中；没有用(109.3)替代其实际方程。
输出的均值和低行则始终由下文完整误差界保留。

## 2. 径向方程和根残差准确为零

令 $F_j=c\lambda^{-1/3}\operatorname{Ai}(Z_j)$。
由于 $a_j$ 不依赖 $y$，Airy 方程直接给
$$
 (F_j)_{yy}
  =a_j^2Z_jF_j
  =(\lambda^2y-v_0+yv_1)F_j.
 \tag{109.6}
$$
因此对 $P_0=-\partial_y^2-y\partial_\phi^2+V$，
$$
 P_0U_j^{\rm lin}
 =e^{i\epsilon\lambda\phi}
 \left[(V+v_0-yv_1)F_j
        -2i\epsilon\lambda y(F_j)_\phi-y(F_j)_{\phi\phi}\right].
 \tag{109.7}
$$
在 $V+v_0-yv_1=y^2V_2$ 的真实可去意义下，右侧的每项都带 $y$。
结合(109.2)的根匹配条件，
$$
 (P_*U_j^{\rm lin})(0,\phi)=0.
 \tag{109.8}
$$
这里无需另加固定 $y^2$ completion。
新试解的根两迹与原 R53 试解不同，差额必须支付，不能原样沿用旧根矩阵。

全部 angular 系数导数可直接按真实乘法计算：
$$
 \begin{split}
 a_\phi&=\frac{(v_1)_\phi}{3a^2},\\
 a_{\phi\phi}&=\frac{(v_1)_{\phi\phi}}{3a^2}
                   -\frac{2(v_1)_\phi^2}{9a^5},\\
 Z_\phi&=y a_\phi-\frac{(v_0)_\phi}{a^2}
                          +\frac{2v_0a_\phi}{a^3},\\
 Z_{\phi\phi}&=y a_{\phi\phi}-\frac{(v_0)_{\phi\phi}}{a^2}
 +\frac{4(v_0)_\phi a_\phi}{a^3}
 +\frac{2v_0a_{\phi\phi}}{a^3}
 -\frac{6v_0a_\phi^2}{a^4}.
 \end{split}
 \tag{109.9}
$$
例如
$$
 (F_j)_\phi=c\lambda^{-1/3}\operatorname{Ai}'(Z)Z_\phi,\quad
 (F_j)_{\phi\phi}=c\lambda^{-1/3}
   [Z\operatorname{Ai}(Z)Z_\phi^2+\operatorname{Ai}'(Z)Z_{\phi\phi}].
 \tag{109.10}
$$
因此根可去商可以按(109.7)直接计算，而不对两个大近似根值相减后除以 $y$。

## 3. 完整 $E$ 和截断项

对 $U=e^{i\epsilon\lambda\phi}F$，
$-\operatorname{div}(E\nabla U)=e^{i\epsilon\lambda\phi}\mathcal E_\lambda F$，
其中准确为
$$
 \begin{split}
 \mathcal E_\lambda F={}&-E_{11}F_{yy}
 -(E_{11,y}+E_{12,\phi})F_y
 -2E_{12}(F_{y\phi}+i\epsilon\lambda F_y)\\
 &-(E_{12,y}+E_{22,\phi})(F_\phi+i\epsilon\lambda F)\\
 &-E_{22}(F_{\phi\phi}+2i\epsilon\lambda F_\phi-\lambda^2F).
 \end{split}
 \tag{109.11}
$$
特别是 $E_{11}$ 及其导数没有省略。对只依赖 $y$ 的真实 cutoff $\chi$，
$$
 \begin{split}
 P_*(\chi U)={}&\chi P_*U
 -2\chi'[(1+E_{11})U_y+E_{12}U_\phi]\\
 &-\big[(1+E_{11})\chi''+
                   (E_{11,y}+E_{12,\phi})\chi'\big]U .
 \end{split}
 \tag{109.12}
$$
$\chi=1$ 于根附近、$\chi=\chi'=0$ 于外端附近时，新试解在根仍满足
(109.8)，而完整 grounded primal/dual 可按 R108 零延拓到同一真实帽。
外端真实 Robin 形式仍在同一能量空间；它的 mismatch 在该紧支对上为准确零。

若 $v=\tau_*\chi U$，则真实 grounded residual 是
$$
 f=\operatorname{div}(A\nabla v)
        =-\tau_*^{-1}P_*(\chi U).
 \tag{109.13}
$$
改变 height 必须同步使用(109.13)，并支付新的 $\tau_*^{-1}$ 及其角导。
不能将 R108 的 $2.257$ 或 $\tau^{-1}$ 原数值转授到未认证的宽图。

## 4. 完整 Banach 符号预算与根差

记
$$
 \|b\|_{K,s}=\sum_{\ell\in\mathbb Z}
       \left(1+\frac{|\ell|}{K+1}\right)^s|\widehat b_\ell|,
       \qquad s\ge0.
 \tag{109.14}
$$
其权满足次乘性，故是含单位的 Banach 代数。
R99 的真实表包含完整 Fourier 误差和无限尾，并对同一个实际族统一有效。

对每个 $K=64,128,256$，取报告中严格频率下界 $\Lambda$ 和
严格立方根下界 $l<\Lambda^{1/3}$。令
$$
 V_s>\|v_0\|_{K,s},\quad W_s>\|v_1\|_{K,s},\quad
 t_s=W_s/\Lambda^2,\quad
 u_s<(1-t_s)^{1/3},\quad
 S_s=\frac{V_s}{\Lambda l\,u_s^2}.
 \tag{109.15}
$$
实际 $s=0,1,3$ 的九行均给 $t_s<1/2,S_s<1/4$。

写 $x=v_1/\lambda^2$、$z_0=-v_0/\lambda^{4/3}$。
真正的根参数是 $z=z_0(1+x)^{-2/3}$。
binomial 的完整绝对系数和给
$$
 \begin{gathered}
 \|(1+x)^{-2/3}-1\|\le(1-t_s)^{-2/3}-1\le u_s^{-2}-1,\\
 \|(1+x)^{1/3}\|\le2-(1-t_s)^{1/3}\le2-u_s,\\
 \|(1+x)^{1/3}-1-x/3\|
       \le1-t_s/3-(1-t_s)^{1/3}\le1-t_s/3-u_s.
 \end{gathered}
 \tag{109.16}
$$
这里不是以列范数的上确界替代完整矩阵范数。每个解析幂展开先按
固定的乘积 $v_0^p v_1^r$ 和输入的负幂展开，再把它们的非负 Fourier
卷积上界相加，得到对全部输入 $j$ 同时有效的一个 lag 包络。
因此可用真正的行列 Schur/Young 界，合法交换的是非负收敛级数。

令 $A_0=\operatorname{Ai}(0)$、$A_1=\operatorname{Ai}'(0)$。
R96/R103 已付 $cA_0<27/50$、$c|A_1|<39/100$。
定义非负系数
$$
 a_0=27/50,\quad a_1=39/100,\quad a_2=0,\quad
 a_n=\frac{a_{n-3}}{n(n-1)}\quad(n\ge3)
 \tag{109.17}
$$
及
$$
 T_0(S)=\sum_{n\ge3}a_nS^n,\qquad
 T_1(S)=\sum_{n\ge3}n a_nS^{n-1}.
 \tag{109.18}
$$
这是完整 Airy entire 函数的绝对 Taylor majorant，不截掉高阶项。

设 $\Delta U_0,\Delta U_y$ 是(109.4)减去 R53 canonical 试解的两根迹。
逐输入右侧平衡后，准确得到以下完整符号上界：
$$
 \begin{split}
 E_{v,s}&=\frac{39}{100}\frac{V_s}{\Lambda l}(u_s^{-2}-1)
                      +T_0(S_s),\\
 E_{p,s}&=\frac{39}{100}(1-t_s/3-u_s)
                      +(2-u_s)T_1(S_s).
 \end{split}
 \tag{109.19}
$$
即 $\Delta U_0\Gamma^{1/3}$ 的公共 lag 包络由 $E_{v,s}$ 控制，
$\Delta U_y\Gamma^{-1/3}$ 的由 $E_{p,s}$ 控制。
这是乘法在左、输入频率在右的准确排序。

## 5. 真实根范数、全部低输出和均值

为了明确每一个有限槽，定义
$$
 \bar\Gamma e_k=
 \begin{cases}4q|k|e_k,&k\ne0,\\ e_0,&k=0.\end{cases}
 \qquad
 \mathcal D=\operatorname{diag}(\bar\Gamma^{1/3},\bar\Gamma^{-1/3}).
 \tag{109.20}
$$
本节只是这个指定对角根范数；它不是物理 Cauchy 矩阵或完整辛 frame 的逆。

令 $P_H$ 为 canonical $|k|>K$。
对高输入、高输出，
$|\lambda_n/\lambda_j|^{1/3}$ 和 $|\lambda_j/\lambda_n|^{1/3}$
都不超过 $(1+|n-j|/(K+1))^{1/3}$。
因此 $s=1$ 的已付包络给
$$
 \|P_H\mathcal D(\Delta U_0,\Delta U_y)^TP_H\|
                  \le\sqrt{E_{v,1}^2+E_{p,1}^2}.
 \tag{109.21}
$$
高度一槽的相同界保全部输出仍成立。
通量槽的低输出必须另外支付。所有 $E_p$ 的 Taylor 单项至少带
$\lambda^{-8/3}$；故乘以 $\lambda^{1/3}$ 后，对所有 $\lambda\ge\Lambda$
仍由 $\Lambda^{1/3}E_{p,0}$ 控制。又 $\bar\Gamma^{-1/3}\le I$，从而
$$
 \|\mathcal D(\Delta U_0,\Delta U_y)^TP_H\|
        \le\sqrt{E_{v,1}^2+\Lambda^{2/3}E_{p,0}^2}.
 \tag{109.22}
$$
均值和所有低输出都包括在此式，而非假设它们无耦合。

更强的高→高 $H^0\to H^{8/3}$ 费为
$$
 \Lambda^{8/3}\sqrt{E_{v,3}^2+E_{p,3}^2}.
 \tag{109.23}
$$
证明：值差的每个单项至少衰减 $\lambda^{-10/3}$，通量差至少
$\lambda^{-8/3}$；加左侧 $H^{8/3}$ 后需的 lag 权分别至多为3和 $7/3$，
故 $s=3$ 够用。低输出的完整有限行仍通过(109.22)保留，不把(109.23)
错误转授为已经删除低行的全空间逆。

真实根均值也随试解改变。R108 的 $h_1=e_\phi/\tau_0$、
$h_2=e_\phi\mu/\tau_0$ 给
$$
 |\Delta m|\le
 .831\,\Lambda^{1/3}E_{p,0}
 +(.831)(24.940215)\,\Lambda^{-1/3}E_{v,0}.
 \tag{109.24}
$$
这直接用全部根列，不要求其均值为零。原 R108 的均值费应加(109.24)。

## 6. 实际执行的完整表

四个输入报告的准确 SHA、九个 $s$ 行、完整 entire 尾、34 门及输出均在
`notes/2026-11-12-R109-frozen-linear-Airy-root-budget.json`。
来源是实际 v0、v1 全 Fourier 表、共同根报告和已原生完成的 R108 报告。
纯 BigInt 核已在 JavaScript 执行器实际运行；Node 读盘入口尚未运行。
不把两者混写。每次正有理数运算向上取30位十进制，根在24位夹取；
所有误差方向在源码中明确。

| $K$ | 平衡高→高根差 | 平衡高→全部输出根差 | 高→高 $H^{8/3}$ 费 |
|---:|---:|---:|---:|
|64|.026156185854|.250652314757|33424502|
|128|.002053845754|.025339941933|15356214|
|256|.000226820608|.003938254452|10555589|

| $K$ | 原完整均值费 | 新根差的均值费 | 新完整均值费 |
|---:|---:|---:|---:|
|64|.083628975067|.235628466137|.319257441203|
|128|.044138082420|.022738891555|.066876973974|
|256|.025473398447|.003399550210|.028872948656|

程序保留均值的 $\bar\Gamma_0=1$，没有只用高→高表来掩盖低输出。
在接 R98/R99 时，还须把这些差乘上**同一个真实**根 frame/height/flux
的已付范数；本表没有把该乘数设为1。

完整 Taylor 尾的实现如下。计算到 $N=24$ 后，对两个非零 residue class
分别取第一个未留项 $n$。后续三步比值不超过
$$
 \frac{S^3}{(n+3)(n+2)}\quad\hbox{和值级数},\qquad
 \frac{S^3}{n(n+2)}\quad\hbox{和导数级数}.
 \tag{109.25}
$$
它们都严格小于1，后续分母递增，所以首遗漏项除以 $1-r$ 给完整尾。
向上舍入的有限系数和幂只增加此界。

## 7. 正轴衰减与完整 source 阶数

这里给可用于下一实际积分的明确支配式，不把有限 jets 的存在当作已付数值。
由已过的门，置 $z=y\lambda^{2/3}$，真实参数满足
$$
 Z\in[3z/4-1/4,\;6z/5+1/4].
 \tag{109.26}
$$
R96 已证明实际 Airy 支的正性、正轴衰减及其初值。
这些性质还给一个简短自证估计。对 $x>0$，
$g=\operatorname{Ai}'(x)+\sqrt x\,\operatorname{Ai}(x)$ 满足
$g'=\sqrt x\,g+\operatorname{Ai}(x)/(2\sqrt x)$。
若某点 $g>0$，积分因子使 $g$ 此后至少指数增长，与 R96 的衰减矛盾。
故 $g\le0$，并得到
$$
 c\operatorname{Ai}(x)\le(27/50)e^{-2x^{3/2}/3}\quad(x\ge0).
 \tag{109.27}
$$
又 $c|\operatorname{Ai}'(x)|=\int_x^\infty t\,c\operatorname{Ai}(t)dt$。
对 $x\ge1$，用 $u=t^{3/2}$ 及 $u^{1/3}$ 的切线凹上界，
积分不超过 $(81/100)\sqrt x\,e^{-2x^{3/2}/3}$。
在 $[-1/4,0]$ 上，一阶系统的 $\ell^1$ 范数给
$c(|\operatorname{Ai}|+|\operatorname{Ai}'|)<(.54+.39)e^{1/4}<1.24$；
在 $[0,1]$ 上由正性和单调性更小。
结合(109.26)，可统一使用
$$
 c|\operatorname{Ai}(Z)|,\ c|\operatorname{Ai}'(Z)|
 \le4(1+z)^{1/2}e^{-z^{3/2}/(3\sqrt2)},\qquad z\ge0.
 \tag{109.28}
$$
对 $z\le1$ 上式显然大于上述紧区间界；
对 $z\ge1$，$Z\ge z/2$，$Z\le3z/2$，分别应用正轴界；
若此时 $Z<1$ 则 $z<2$，仍用紧区间界即可。

所有更高 Airy 导数都由准确的多项式递推
$$
 P_0=1,\ Q_0=0,\quad
 P_{r+1}=P_r'+ZQ_r,\quad Q_{r+1}=P_r+Q_r',
 \quad \operatorname{Ai}^{(r)}=P_r\operatorname{Ai}+Q_r\operatorname{Ai}'
 \tag{109.29}
$$
控制。配合(109.9)，所有需要的有限角导数可写成明确的正系数 majorant。

在有足够实际有限角导数的图内，设 $V+v_0-yv_1=y^2V_2$，
$E_{ab}=O(y^5)$ 且相应的一阶径向导为 $O(y^4)$。
由 $y=\lambda^{-2/3}z$ 及 $L^2_y$ 的 $\lambda^{-1/3}$ 因子：

- $y^2V_2F$ 的最坏 source gain 为2。
- $2\lambda yF_\phi$ 的最坏 gain 为 $5/3$。
- $yF_{\phi\phi}$ 的最坏 gain 为 $8/3$。
- 完整(109.11)中 $E_{11}$、$E_{12}$、$E_{22}$ 项的最坏 gain
  分别至少为 $8/3,7/3,2$。

这包含 root shift 和 slope 的全部角变化；没有将 $a_j$ 当成角常数。
若每一项系数的三阶角导也有同样有限 $L^2_y$ majorant，
三次 Fourier 分部给 lag 衰减 $(1+|\ell|)^{-3}$；
左侧 $H^{5/3}$ 至多增加 $(1+|\ell|)^{5/3}$，其余和可求，
故得到真正的全矩阵 $H^0\to L^2_yH^{5/3}$ 强界。
若换成更弱系数空间，则须另证对应的乘法/矩阵估计，不能略去。

所有实际积分常数均可化为有限多项式及
$$
 \int_0^\infty z^m e^{-b z^{3/2}}dz
 =\frac23 b^{-2(m+1)/3}\Gamma\!\left(\frac{2(m+1)}3\right),\quad m>-1.
 \tag{109.30}
$$
cutoff 支撑离根时，(109.28)给其完整指数尾；但是窄 cutoff 的真实常数
可能很大，必须用(109.12)真正计算，不能只凭阶数称它可忽略。

当前 C4 样条跨径向 knot 后，混合坐标的高角 jets 并非免费存在。
本节的矩阵阶数定理明确以上述实际有限导数为输入；R109 的真实根预算
只使用已付根 scalar span 和完整根 Fourier 表，不替未计算的宽域授予正则性。
需要时可直接在物理变量分段、使用弱源，或另付相应有限 Sobolev 乘法界。

## 8. 全输出 inverse-derivative 流：直接保住一个高频因子

R108 的完整 stream 可以进一步使用输入高频，而不删除任何低输出。
令 $Q=T_{q_j(\phi)}$ 是全列符号算子，$Q^{[1]}=T_{\partial_\phi q_j}$，
$D=\partial_\phi$，$D^{-1}$ 在非零模上定义、在均值上为0。
对无均值输入准确有
$$
 \boxed{\quad
 D^{-1}\Pi Q=\Pi QD^{-1}-D^{-1}\Pi Q^{[1]}D^{-1},\qquad
 P_0Q=-P_0Q^{[1]}D^{-1}.
 \quad}
 \tag{109.31}
$$
证明仅用 $DQ=QD+Q^{[1]}$ 和 $D^{-1}D=\Pi$，故允许真实输入频率相关符号。
$Q^{[1]}$ 只微分系数，不把输入平面波的 $i\epsilon\lambda$ 错算进去。

若完整公共 lag 包络分别给 $\|Q\|\le M_0$、$\|Q^{[1]}\|\le M_1$，
则在 $|j|>K$，
$$
 \|D^{-1}\Pi QP_H\|
 \le\Lambda^{-1}[M_0+(4q)^{-1}M_1],\qquad
 \|P_0QP_H\|\le\Lambda^{-1}M_1.
 \tag{109.32}
$$
这里 $D^{-1}$ 的低输出费用完整留下；绝无假设 $P_HQ=QP_H$。

令 $Q(y)$ 是(109.13)除以 $y$ 的**完整**残差算子，
$M_0(y),M_1(y)$ 是上述真正系数 lag 包络，包括 $\tau_*^{-1}$ 和 cutoff。
若同一真实 canonical collar 满足
$A^{-1}\le L\,\operatorname{diag}(1,y^{-1})$，R108 的精确流于是给
$$
 \begin{split}
 \mathcal R\le{}&\sqrt{LH}\,\|m_{\rm new}\|\\
 &+\frac{\sqrt L}{\Lambda}
 \left[
  \int_0^H\left(\int_0^y sM_1(s)ds\right)^2dy
 +\int_0^H y\big(M_0(y)+(4q)^{-1}M_1(y)\big)^2dy
 \right]^{1/2}.
 \end{split}
 \tag{109.33}
$$
这允许直接利用真实 Airy 衰减，而不先把整区间换成最大值。
均值列使用(109.24)后的新费用；regular、Robin 和外区仍按 R108 同一个
紧支 primal/dual 对处理。

(109.33)省的是角流中的真实输入逆频率。它既没有压缩体内方程，
也不把完整 gap 改成只含 PDE residual 的局部数值。
目前新 $M_0(y),M_1(y)$ 和宽图 $L$ 尚未实际连续积分；这些是接强反馈
仍要继续支付的真正输入。

## 9. 可重放文件与未完成范围

源为 `scripts/fourfold_phase_frozen_linear_airy_root_budget.mjs`。
源和报告记录了四个准确输入、全部输出、真实执行环境和源 SHA；
Node 入口可独立读取原文件重放全部34门。第一次不舍入的实验算术调用未返回
结果后被终止；本报告来自随后实际通过的有向有限小数有理数实现，不沿用失败调用。

已付的是实际根差和可用的完整 source/stream 恒等式。
尚未付的是新的全领口系数积分、真实外端/低高网络和全空间强反馈逆。
所有实际规范变化都通过 R99 的完整 Cauchy 矩阵接线，而非只匹配主符号。

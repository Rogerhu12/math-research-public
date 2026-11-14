# R30：明确 Diophantine 返回数、全频除数与参数归一化

2026-11-12，visible-flex-exact-nearby / independent-audit。

**状态：已证明的中间结论。** 本文给两个明确二次无理返回数，支付
旋转的 $I-T$ 和反周期 $I+T$ 的全频一阶损失逆。较强选择的两个逆
常数分别为 $5/4$、$5$。此外，在明确的 Fourier--Wiener 解析范数中，
本文完整证明带一个平移反项的圆周共轭收敛门，并写出实际几何参数
消去反项所需的横截公式。

这些结果还不是原始等距 PDE 的逆。实际候选的特征返回图、完整传输
幅度、非线性源空间、转折接线和边界图尚须识别；本结果没有把径向
作用量或数值近似返回数当成那些输入已经完成。

## 1. 角变量约定与两个可调目标

圆周坐标使用 $x\pmod{2\pi}$，令
$$
T_\alpha u(x)=u(x+\alpha),\qquad
\alpha=2\pi\rho.
$$
对于径向标量主符号
$\xi_s^2-V(s)\xi_\theta^2$ 的正势腔，一次往返的材料角增量（选定
方向后）为 $2J$，其中 $J=\int_{V>0}\sqrt V\,ds$。
这是由特征方程 $d\theta/ds=\pm\sqrt V$ 直接积分得到的。
在四重商角 $x=4\theta$ 中，返回角为 $8J$，所以径向对应为
$$
\rho=\frac{4J}{\pi}\pmod1.
\tag{1.1}
$$
真正非径向返回数必须另行确定；(1.1) 不被当成其定义或证明。

第一个便于整数范数证明的目标为
$$
\rho_0=\frac{4+\sqrt6}{11},\qquad
J_0^{\rm irr}=\frac{\pi(4+\sqrt6)}{44}.
\tag{1.2}
$$
第二个具有更好全频常数的目标为
$$
\boxed{\quad
\rho_\sharp=[0;1,1,2,2,1,1,3,\overline1]
=\frac{8165-\sqrt5}{13918},\qquad
J_\sharp=\frac{\pi\rho_\sharp}{4}.
\quad}
\tag{1.3}
$$
作参数探索时，
$\rho_\sharp\approx .586489720651$、$J_\sharp\approx .460627949451$。
它接近旧近似图曾报告的 $J\approx .4606$；这些小数仅供选目标，
不是当前候选的认证值，也不要求把有限幅作用量拉回 R25 的径向
$11\pi/89$。

## 2. 第一个目标的完整整数范数证明

记 $\|t\|_{\mathbb Z}=\operatorname{dist}(t,\mathbb Z)$。
对 $k\ne0$，取 $j$ 为 $k\rho_0$ 的最近整数，令
$$
z=11(k\rho_0-j)=4k+k\sqrt6-11j.
$$
其代数范数
$(4k-11j)^2-6k^2$ 为非零整数。由 $|z|\le11/2$，
$$
|z|\ge\frac1{|z-2k\sqrt6|}
\ge\frac1{11/2+2\sqrt6|k|}
>\frac2{21|k|}.
$$
因此
$$
\|k\rho_0\|_{\mathbb Z}>\frac2{231|k|}.
\tag{2.1}
$$
对最近半整数，写 $l$ 为奇整数，使
$|2k\rho_0-l|\le1$。令
$z=11(2k\rho_0-l)=8k+2k\sqrt6-11l$。
其范数同样是非零整数，且 $|z|\le11$，所以
$$
|z|\ge\frac1{11+4\sqrt6|k|}>
\frac1{21|k|}.
$$
于是
$$
\operatorname{dist}(k\rho_0,\mathbb Z+1/2)>
\frac1{462|k|}.
\tag{2.2}
$$
利用 $2\sin(\pi t)\ge4t$ 于 $0\le t\le1/2$，得到
$$
|e^{2\pi ik\rho_0}-1|>\frac8{231|k|},\qquad
|e^{2\pi ik\rho_0}+1|>\frac2{231|k|}.
\tag{2.3}
$$
这是所有整数频率的证明，不是有限小分母扫描。

## 3. 有界部分商目标及强常数 $5/4$、$5$

令 $\phi=(1+\sqrt5)/2$。前缀的连续分数矩阵给
$$
\rho_\sharp=\frac{61\phi+17}{104\phi+29}
=\frac{8165-\sqrt5}{13918}.
$$
所以它的全部部分商不超过 $3$。

这里所用的初等逼近事实是：若无理数的全部部分商不超过 $A$，则
对所有非零整数 $k$，
$$
\|k\rho\|_{\mathbb Z}>\frac1{(A+2)|k|}.
\tag{3.1}
$$
为说明常数来源，设 $p_j/q_j$ 为收敛分数。
完全商公式给
$$
|q_j\rho-p_j|
=\frac1{q_j\rho_{j+1}+q_{j-1}}
>\frac1{q_{j+1}+q_j}.
$$
其中 $\rho_{j+1}<a_{j+1}+1$。
选择 $j$ 使 $q_j\le |k|<q_{j+1}$；收敛分数的第二类最佳逼近性质
给 $\|k\rho\|_{\mathbb Z}\ge |q_j\rho-p_j|$。
这个性质也由相邻收敛分数的行列式为 $\pm1$ 直接得到：把候选整数对
写成这两个基向量的整系数组合，若分母小于下一收敛分母而误差更小，
两个交错误差的符号迫使组合系数至少达到下一部分商，产生矛盾。
最后
$q_{j+1}+q_j\le(A+2)q_j\le(A+2)|k|$，即得 (3.1)。
最初两个分母相等时取最大的相应 $j$，结论不变。

应用 $A=3$，再对 $2k$ 使用同一结论，得到
$$
\boxed{\quad
\|k\rho_\sharp\|_{\mathbb Z}>\frac1{5|k|},\qquad
\operatorname{dist}(k\rho_\sharp,\mathbb Z+1/2)>
\frac1{20|k|}.
\quad}
\tag{3.2}
$$
第二式由
$\operatorname{dist}(2k\rho_\sharp,2\mathbb Z+1)
\ge\|2k\rho_\sharp\|_{\mathbb Z}$ 得到。
因此对 $\alpha_\sharp=2\pi\rho_\sharp$，
$$
\boxed{\quad
|e^{ik\alpha_\sharp}-1|>\frac4{5|k|},\qquad
|e^{ik\alpha_\sharp}+1|>\frac1{5|k|}.
\quad}
\tag{3.3}
$$

对整数 $s\ge0$，取
$\|u\|_{H^s}^2=\sum_{j=0}^s\|\partial_x^ju\|_2^2$。
逐模除法给
$$
\boxed{\begin{aligned}
\|(T_{\alpha_\sharp}-I)^{-1}g\|_{H^s}
&\le\frac54\|g\|_{H^{s+1}}
&&(\langle g\rangle=0,\ \langle u\rangle=0),\\
\|(I+T_{\alpha_\sharp})^{-1}g\|_{H^s}
&\le5\|g\|_{H^{s+1}}.
\end{aligned}}
\tag{3.4}
$$
$I+T$ 的均值模除以 $2$，已包含在第二行常数中。
一般实 Sobolev 阶使用通常 Fourier 权也得到相同的一阶损失；
本文后面的显式复合常数使用整数阶。

## 4. 已有真实共轭时的范数转移

设真实保向微分同胚 $F$ 与旋转满足
$$
F\circ H=H\circ R_{\alpha_\sharp},
\tag{4.1}
$$
其中 $H$ 是真实光滑保向圆周微分同胚。
纯复合算子 $P_Hu=u\circ H$ 满足
$P_HT_F=T_{\alpha_\sharp}P_H$。
所以
$$
(I\pm T_F)^{-1}
=P_{H^{-1}}(I\pm T_{\alpha_\sharp})^{-1}P_H.
\tag{4.2}
$$
负号时要求 $\langle g\circ H\rangle=0$，并在同一共轭坐标固定均值。

以下给可由有限导数界直接计算的常数，避免隐藏复合损失。
记 $m_H=\inf H'>0$，$B_{j,l}$ 为链式法则的部分 Bell 多项式，
并约定 $B_{0,0}=1$、$B_{j,0}=0$（$j>0$）。置
$$
C_s(H)=m_H^{-1/2}
\left(\sum_{j=0}^s\sum_{l=0}^j
\|B_{j,l}(H',\ldots,H^{(j-l+1)})\|_\infty^2\right)^{1/2}.
\tag{4.3}
$$
逐阶链式法则和 $dy=H'(x)\,dx$ 给
$\|P_H\|_{H^s\to H^s}\le C_s(H)$。
因此 (3.4) 在实际坐标中的常数分别为
$$
\frac54C_s(H^{-1})C_{s+1}(H),\qquad
5C_s(H^{-1})C_{s+1}(H).
\tag{4.4}
$$

若实际主传输是半密度
$U_Fu=\sqrt{F'}\,u\circ F$，则使用酉 pullback
$U_Hu=\sqrt{H'}\,u\circ H$；仍有
$U_HU_F=T_{\alpha_\sharp}U_H$。
对一个乘法函数 $a$，定义显式 Leibniz 矩阵常数
$$
M_s(a)=\left(\sum_{j=0}^s\sum_{l=0}^j
\binom jl^2\|a^{(j-l)}\|_\infty^2\right)^{1/2},\qquad
D_s(H)=M_s(\sqrt{H'})C_s(H).
$$
则实际半密度传输的两逆常数分别至多
$$
\frac54D_s(H^{-1})D_{s+1}(H),\qquad
5D_s(H^{-1})D_{s+1}(H).
\tag{4.5}
$$
负号的兼容是 $\langle U_Hg\rangle=0$。
实际传输若还有额外幅度或低阶项，必须另付；(4.5) 没有将它们删除。

## 5. 一个完整的解析反项共轭定理

下面给可直接核验的充分条件，不只引用定性共轭定理。
使用周期 Fourier--Wiener 范数
$$
\|f\|_s=\sum_{k\in\mathbb Z}|f_k|e^{s|k|}.
\tag{5.1}
$$
它是 Banach 代数，实平移等距，且
$$
\|f'\|_{s-\delta}\le\frac1{e\delta}\|f\|_s,\qquad
\|f\circ(\operatorname{id}+h)\|_r\le\|f\|_{r+\|h\|_r}
\tag{5.2}
$$
只要右端有定义。第二式由逐个 $e^{ik(x+h)}$ 的幂级数和代数性质得到。
由 (3.3)，零均值同调方程有
$$
\|(T_{\alpha_\sharp}-I)^{-1}g\|_{s-\delta}
\le\frac5{4e\delta}\|g\|_s.
\tag{5.3}
$$

设 $F(x)=x+\alpha_\sharp+f(x)$ 为实解析保向圆周微分同胚的提升，
$\|F''\|_S=\|f''\|_S\le B$。
给一个近似共轭 $H_0(x)=x+h_0(x)$ 和实常数 $\lambda_0$。
假设
$$
\|h_0'\|_{s_0}\le\frac18,\qquad
E_0(x)=F(H_0(x))+\lambda_0-H_0(x+\alpha_\sharp),
\qquad \|E_0\|_{s_0}\le\varepsilon_0.
$$
选择 $0<\delta_0<s_0/4$，置
$$
C=2+\frac{25}{8}B.
$$
若满足明确门
$$
\boxed{\quad
\varepsilon_0\le\frac{\delta_0^2}{32C},\qquad
S>s_0+\|h_0\|_{s_0}+\frac{3\varepsilon_0}{\delta_0},
\quad}
\tag{5.4}
$$
则存在真实解析共轭 $H_\infty=x+h_\infty$ 和实反项
$\lambda_\infty$，满足
$$
F\circ H_\infty+\lambda_\infty
=H_\infty\circ R_{\alpha_\sharp},
\tag{5.5}
$$
其解析宽度至少 $s_\infty=s_0-4\delta_0>0$，并且
$$
\boxed{\begin{aligned}
\|H_\infty-H_0\|_{s_\infty}
&\le3\varepsilon_0/\delta_0,\\
\|H_\infty'-H_0'\|_{s_\infty}
&\le4\varepsilon_0/\delta_0^2,\\
|\lambda_\infty-\lambda_0|&\le3\varepsilon_0.
\end{aligned}}
\tag{5.6}
$$
特别 $H_\infty'>0$ 于实轴，是真正圆周微分同胚。
定理为 $F+\lambda_\infty$ 给共轭；除非实际参数步骤另证
$\lambda_\infty=0$，不能把它冒称为未经改变的 $F$ 已有共轭。

## 6. 自动约化和一次修正的完整常数

设某步 $H=x+h$、$\|h'\|_s\le1/4$、误差 $\|E\|_s\le\varepsilon$。
记 $H'_R(x)=H'(x+\alpha_\sharp)$、$b=1/H'_R$，则
$$
\|b\|_s\le4/3,\qquad |\langle b\rangle|\ge2/3.
$$
取
$$
\Delta\lambda=-\frac{\langle bE\rangle}{\langle b\rangle},
\qquad
w_R-w=b(E+\Delta\lambda),\qquad\langle w\rangle=0,
\qquad
\Delta H=H'w.
\tag{6.1}
$$
右端均值准确为零，且
$$
|\Delta\lambda|\le2\varepsilon,\qquad
\|b(E+\Delta\lambda)\|_s\le4\varepsilon.
$$
由 (5.3) 和 $5/e<2$，
$$
\|w\|_{s-\delta}<2\varepsilon/\delta,\qquad
\|\Delta H\|_{s-\delta}\le\frac52\varepsilon/\delta.
\tag{6.2}
$$
对 $w$ 和 $H'$ 再花一个 $\delta$ 的 Cauchy 宽度，
$$
\|(\Delta H)'\|_{s-2\delta}
\le3\varepsilon/\delta^2.
\tag{6.3}
$$
其中两项分别由
$\|H''\|\|w\|\le\varepsilon/(2\delta^2)$ 和
$\|H'\|\|w'\|\le5\varepsilon/(2\delta^2)$ 给出。

对误差恒等式求导得
$$
F'(H)H'-H'_R=E'.
$$
所以 (6.1) 代入后新的误差准确是
$$
E_{\rm new}
=E'w+
\bigl[F(H+\Delta H)-F(H)-F'(H)\Delta H\bigr].
\tag{6.4}
$$
那个变系数余项是 $E'w$，因而二次小；没有把任意非径向 PDE 的主系数
变动宣称为同样可约化。
只要 $H+t\Delta H$ 的复域位于 $F$ 的允许域，(5.2) 和 Taylor 积分给
$$
\boxed{\quad
\|E_{\rm new}\|_{s-2\delta}
\le\left(2+\frac{25B}{8}\right)
\frac{\varepsilon^2}{\delta^2}
=C\frac{\varepsilon^2}{\delta^2}.
\quad}
\tag{6.5}
$$

## 7. 收敛、域和所有迭代费用

取
$$
\delta_j=2^{-j}\delta_0,\qquad
s_j=s_0-2\sum_{i<j}\delta_i,\qquad
q_0=\frac{4C\varepsilon_0}{\delta_0^2}\le\frac18.
$$
若 $q_j=4C\varepsilon_j/\delta_j^2$，(6.5) 给
$q_{j+1}\le q_j^2$，故
$$
\varepsilon_j
\le\varepsilon_0\,4^{-j}q_0^{\,2^j-1}.
\tag{7.1}
$$
由 $2^j-1\ge j$，(6.2)--(6.3) 的修正可求和：
$$
\sum_j\|\Delta H_j\|
\le\frac{5\varepsilon_0}{2\delta_0}
\sum_j2^{-j}q_0^{\,2^j-1}
<\frac{3\varepsilon_0}{\delta_0},
$$
$$
\sum_j\|(\Delta H_j)'\|
\le\frac{3\varepsilon_0}{\delta_0^2}
\sum_jq_0^{\,2^j-1}
<\frac{4\varepsilon_0}{\delta_0^2},
$$
$$
\sum_j|\Delta\lambda_j|
\le2\varepsilon_0\sum_j4^{-j}q_0^{\,2^j-1}
<3\varepsilon_0.
\tag{7.2}
$$
所有范数取各步更小的共同域。
由 (5.4)，导数总改变量不超过 $1/(8C)\le1/16$，加初始 $1/8$
仍小于 $1/4$。这保持了第 6 节的逆导数门。
域总改变量由第一行控制，(5.4) 的第二条使每个实际复合
$F(H_j+t\Delta H_j)$ 合法，故没有未经支付的解析域减少。

(7.1) 使误差趋零，(7.2) 使共轭和反项在 $s_\infty>0$ 上收敛。
代入连续的解析复合得到 (5.5)--(5.6)。
实数据的实性在每步保持，且
$\|h_\infty'\|\le3/16<1$，因此实轴上 $H_\infty$ 保向且次数一。
紧圆周上的解析反函数定理给其真实解析逆。

若需要第 4 节的具体有限阶共轭范数，由最终解析宽度和 (5.6) 可取
$$
\|h_\infty^{(r)}\|_\infty
\le\left(\frac{r}{e s_\infty}\right)^r
\left(\|h_0\|_{s_0}+\frac{3\varepsilon_0}{\delta_0}\right).
$$
逆映射导数再由 $H_\infty\circ H_\infty^{-1}=\operatorname{id}$ 的链式
法则递推，分母使用 $H_\infty'\ge13/16$；这是有限、明确的运算，
可代回 (4.3)--(4.5)。

## 8. 真实几何参数如何消去反项

反项 $\lambda$ 是圆周共轭计算的一个输出，不是已授权改变几何方程
的自由常数。若实际返回图来自参数族 $F_a$，应对同一目标
$\alpha_\sharp$ 构造
$$
F_a(H_a(x))+\lambda(a)=H_a(x+\alpha_\sharp)
\tag{8.1}
$$
并真正找到 $\lambda(a)=0$ 的参数。

对可微的真实解族，令 $\dot H=H'w$ 并对 (8.1) 求导；平均同调方程
给准确公式
$$
\boxed{\quad
\lambda'(a)=-
\frac{\left\langle
(\partial_aF_a)(H_a)/H_a'(x+\alpha_\sharp)
\right\rangle}
{\left\langle1/H_a'(x+\alpha_\sharp)\right\rangle}.
\quad}
\tag{8.2}
$$
例如若实际 $\partial_aF_a(H_a(x))\ge\tau>0$ 于实轴，则正权平均
直接给 $\lambda'(a)\le-\tau$。
更一般地，分子非零的已认证下界已足够；没有必要要求点态同号。
也可用两个实际参数端点的反项异号及连续性来定位零点。

在零点处 (8.1) 才给未经平移的真实返回图的共轭，随后第 4 节才对
它给全频传输逆。
若恰能独立证明实际 $F_a$ 的旋转数为 $\rho_\sharp$，反项也必为零：
当 $\lambda>0$ 时，(8.1) 在 $H_a$ 坐标下使 $F_a$ 每步位移严格小于
$\alpha_\sharp$，且差至少 $\lambda/\sup H_a'$；故其旋转数严格较小。
$\lambda<0$ 同理较大。这个论证不把一个浮点旋转数当成准确等式。

## 9. 对本题的使用界限及文献对应

现在已给出的输入输出是：

- 明确的无理目标和全部频率除数；
- 已有真实共轭后的纯复合/半密度逆，含真实有限导数费用；
- 一个带反项的完整解析共轭收敛门；
- 用实际几何参数消去反项的准确横截条件。

尚未获得的实际输入包括候选的返回图 $F_a$、其复域及解析误差、
实际参数对返回图的导数、转折处传输的准确幅度，以及将该传输问题
与完整等距 PDE、固定帽和无限尾之间对应的双向估计。
因此本文不把 $I+T$ 可逆直接升级为 PDE 可逆或主课题完成。

自动约化思路与 Jordi-Lluís Figueras、Àlex Haro、Alejandro Luque，
*Effective bounds for the measure of rotations*，Nonlinearity 33 (2020)，
Theorem 3.1 及其证明中的参数同调步骤相对应。
该原文为一般参数族提供更广的后验定理；本文 §5--7 的常数是在
上述 Wiener 范数、特定目标和单平移反项下独立逐项证明的简化门，
不引用该文尚未在本题付清的常数。
原文：[作者机构存档](https://diposit.ub.edu/server/api/core/bitstreams/9ee43039-37e7-410e-9117-893bcf91b300/content)，
[arXiv:1806.05517](https://arxiv.org/abs/1806.05517)。


## 10. 适配其它实际作用量的有界部分商版本

上述两个具体数值不是唯一允许的目标。若最新候选给出另一可调的
返回数区间，可选一个完全包含于该区间的有限连续分数柱，再把尾部
接成 $\overline1$。所得数仍为明确二次无理数。其全部部分商的最大值
$A$ 由有限前缀和 $1$ 直接算出，故没有不确定的 Diophantine 常数。
柱包含关系可以用相邻收敛分数的有理端点严格判断。

设 $D=A+2$。第 3 节的相同证明给
$$
\|(T_\alpha-I)^{-1}\|_{H^{s+1}\to H^s}\le D/4,\qquad
\|(I+T_\alpha)^{-1}\|_{H^{s+1}\to H^s}\le D.
\tag{10.1}
$$
负号仍须零均值。
第 5--7 节也有完全一致的一般版本：取
$$
C_D=\frac{2D}{5}+\frac{D^2B}{8},\qquad
\varepsilon_0\le\frac{\delta_0^2}{32C_D},
$$
$$
S>s_0+\|h_0\|_{s_0}
+\frac{3D}{5}\frac{\varepsilon_0}{\delta_0}.
\tag{10.2}
$$
则得到真实反项共轭，且
$$
\|H_\infty-H_0\|\le
\frac{3D}{5}\frac{\varepsilon_0}{\delta_0},\qquad
\|H_\infty'-H_0'\|\le
\frac{4D}{5}\frac{\varepsilon_0}{\delta_0^2},\qquad
|\lambda_\infty-\lambda_0|\le3\varepsilon_0.
\tag{10.3}
$$
证明只需把 (6.2)--(6.5) 换成
$$
\|w\|\le\frac{2D}{5}\frac{\varepsilon}{\delta},\quad
\|\Delta H\|\le\frac D2\frac{\varepsilon}{\delta},\quad
\|(\Delta H)'\|\le\frac{3D}{5}\frac{\varepsilon}{\delta^2},\quad
\|E_{\rm new}\|\le C_D\varepsilon^2/\delta^2.
$$
第一式用 $1/e<2/5$。相同 $q_0\le1/8$ 求和给 (10.3)，且
$C_D\ge2D/5$ 保持总导数改变量不超过 $1/16$。
在 $A=3,D=5$ 时恰恢复前面全部具体常数。

这个版本允许针对同一个实际候选重新选择目标，而非强迫其作用量
回到早期参考值。真正的参数区间、实际返回图和反项零点仍须由本题
几何求解器提供；连续分数选择不替代这些步骤。

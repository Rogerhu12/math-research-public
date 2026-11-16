# R440：零阶零第三核的完整消-self 核、十六点实际控制与全部根的五列余商

日期：2026-11-16。**原式纸面推导；未执行新的研究代码、profile、积分、零点、矩阵或科学测试。**

[R438](R438-constant-tail-S-responses-and-fifteen-joint-actual-mirror-fluxes.md) 已从 P/S 常尾支路得到十八个 formal self 方向和同一库十五个实际镜点。原零阶零第三核还有三条非恒尾组合；它们在每一个实际 $A_f=0$ 点上准确消掉有序 suffix，而同包 self 不为零。

本稿一次列全这一 universal 消-self 核及其完整 self 像，得到二十一个 formal current 方向。第三条新组合把同一镜对库的实际可控组扩大到十一左点加五右点。更重要的是：清掉这十六行以后，本明确模块对其余全部真实根只剩五条具体原成本列。本稿给出这五列和原目标的准确残差比较，不把 formal 维数冒成全部实际根的满秩，也不把本模块的限制说成整个响应空间的障碍。

## 1. 记号与原尾分解

使用 [R432](R432-complete-zero-order-kernel-and-all-degenerate-point-response-matrices.md) 的原五维第三核
$$
Z_{c0}=\operatorname{span}\{\sigma,\tau_0,\tau_1,\tau_2,\tau_3\},
\quad A=6pt-2r^2,\quad p=u',\ r=u'',\ t=u'''.
$$
其 $a_\tau$ 为
$$
p^2,\quad A,\quad xA+2pr,\quad
x^2A+4xpr-4p^2,\quad x^3A+6x^2pr-4xp^2 .
\tag{1}
$$
全部是 R432 的原三槽算子；不只给一组猜测的局部系数。

原 E8 记作 P、R、S、L、U、V、T、Y，其中 $V=p_1,Y=p_2$。
按 [R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)(4)，P、S 的右包左尾为常数，另外六个的导数可准确取成
$$
E_j^s=(-R,-U,-T)_j,\qquad
E_j^t=(2L,2V,2Y)_j,\qquad 0\le j\le2.
\tag{2}
$$
对于真实三矩 $n=(n_0,n_1,n_2)$，
$$
p\,p_{E_j^s}(n)''-r\,p_{E_j^s}(n)'=rn_j,
$$
$$
p\,p_{E_j^t}(n)''-r\,p_{E_j^t}(n)'=(xr-p)n_j.
\tag{3}
$$
其中额外的真实常数尾仍保留，只是在(3)中被导数自然消掉。

R432 的原 current 为
$$
\int_{\ell_u}^x p\,[\mathcal B_E\tau(u^2,0)]''
=2a_\tau(pq_E''-rq_E'),\qquad q_E=\Phi_E(u,u).
\tag{4}
$$
其完整圆的同包及 suffix 两项均使用同一个(4)，不是分别改选积分常数。

## 2. 三个新组合：有序项在所有 A 根准确消失

定义三个真实原成本
$$
\boxed{
\begin{aligned}
\Xi_0&=4\mathcal B_L\tau_1+\mathcal B_R\tau_2,\\
\Xi_1&=4\mathcal B_V\tau_1+\mathcal B_U\tau_2,\\
\Xi_2&=4\mathcal B_Y\tau_1+\mathcal B_T\tau_2 .
\end{aligned}}
\tag{5}
$$
等价地，$\Xi_j=2\mathcal B_{E_j^t}\tau_1-\mathcal B_{E_j^s}\tau_2$。
由(1)—(3)，不先令 A 为零时，其尾乘子为
$$
2a_{\tau_1}(xr-p)-a_{\tau_2}r
=xA(xr-2p).
\tag{6}
$$
因此在**全部实际 A 根**，每个 $n_j$ 的右尾贡献为零。

对原圆
$$
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i,\quad
R_i=a_i^2-b_i^2,\quad T_i=a_i b_i
$$
以及真实
$n_{R,i}=\sum_{j>i}R_j\mu_j,\ n_{T,i}=\sum_{j>i}T_j\mu_j$，
(6)分别作用于这两组真实向量。故
$$
\boxed{
H_{d,i}(\Xi_j)=a_i^3R_i\,\zeta_j,\qquad
H_{e,i}(\Xi_j)=-a_i^3T_i\,\zeta_j,\qquad
C_i(\Xi_j)=0
}
\tag{7}
$$
在所有实际根成立；这里 $\zeta_j$ 是完整同包 current，下一节列出。

(6)还说明一个准确边界：本稿不宣这些 $\Xi_j$ 的 C 函数在任意非退化 x 都零。需要的是 R394 的全部内部 A 根行；在那里(7)没有余项。

原 $\tau\in Z_{c0}$ 的 whole-E 与自然身份给
$$
\Xi_j\in\mathcal R\cap\ker J^+ .
\tag{8}
$$
self 的外 collar 第二导数也零，因此这些列的 raw 与扣平台规范一致。一般 actual 目标的原平台项仍须保留。

## 3. 三个完整 self：原 J 项逐对相消

记
$$
P=J(r^2),\qquad S=J(xr^2),\qquad C=J(x^2r^2+2p^2),
\quad D_E=pq_E''-rq_E'.
$$
C 在本节是原二阶 primitive；不要与两通道消-self 向量混同。

直接由 R255 的完整式取导，并在 $pt=r^2/3$ 代入，得
$$
\begin{aligned}
D_L&=-\tfrac23ur^2+\tfrac16xpr^2+\tfrac12(xr-p)P,\\
D_R&=-\tfrac43pr^2+\tfrac13xr^3-rP,\\
D_V&=upr-xp^2r-\tfrac23xur^2+\tfrac{11}{12}x^2pr^2
-\tfrac1{12}x^3r^3+\tfrac12(xr-p)S,\\
D_U&=2p^2r-\tfrac{10}{3}xpr^2+\tfrac12x^2r^3-rS,\\
D_Y&=u^2r-2up^2+2xupr+xp^3-2x^2p^2r-\tfrac23x^2ur^2
+\tfrac76x^3pr^2-\tfrac1{12}x^4r^3+\tfrac12(xr-p)C,\\
D_T&=-2p^3+4xp^2r-\tfrac{10}{3}x^2pr^2+\tfrac13x^3r^3-rC.
\end{aligned}
\tag{9}
$$
比如 $q_V=-u^2/2+xup-x^2p^2/2-x^2S/4$、$q_Y=-xu^2+x^2up-x^3p^2/2-x^2C/4$；原 S、C 从未假紧。

式(4)—(5)现在给
$$
\zeta_j=8p\{2rD_{(L,V,Y)_j}+(xr-p)D_{(R,U,T)_j}\}.
\tag{10}
$$
每对的原 primitive 系数恰为 $r(xr-p)-(xr-p)r=0$。
完整结果是
$$
\boxed{
\begin{aligned}
\zeta_0={}&\tfrac83x^2pr^4-\tfrac{32}{3}xp^2r^3
+\tfrac{32}{3}p^3r^2-\tfrac{32}{3}upr^3,\\
\zeta_1={}&16up^2r^2-\tfrac{32}{3}xupr^3-16p^4r
+\tfrac{80}{3}xp^3r^2-16x^2p^2r^3+\tfrac83x^3pr^4,\\
\zeta_2={}&16u^2pr^2-32up^3r+16p^5-32xp^4r+32xup^2r^2\\
&+\tfrac{80}{3}x^2p^3r^2-\tfrac{32}{3}x^2upr^3
-\tfrac{32}{3}x^3p^2r^3+\tfrac43x^4pr^4 .
\end{aligned}}
\tag{11}
$$
所以这些是有完整原锚来源的全部 partial，而不是 principal 或未经核定的 local 截断。式(9)—(11)也允许 r 为零；没有除 r。

## 4. 原 c=0 标签中 universal 消-self 核已列全

这里的 universal 条件是：原 A 根的多项式 current 对所有自由 $(x,p,r)$、$p\ne0$ 和三矩变量 n 恒为零。它比一个已经固定库的有限 C 矩阵核更强；后者可能因实际 suffix、宽度及 jets 关系而更大。

$\tau_0$ 的八个 E 列在所有 A 根连 self 也盲，可以先模掉。余32个标签中，P/S 的八列因常尾自动消 C。每个矩的另外八列按 R432 的 $(s_0,t_0)=(r/p,xr/p-1)$ 乘积，准确给七个独立函数。其唯一关系正是
$$
2\,\tau_1\otimes E_j^t-\tau_2\otimes E_j^s.
\tag{12}
$$
原(2)的六套非恒尾按三个不同 $n_j$ 分开。因此这32个标签的 universal C 核恰由八条 P/S 列及三个(5)生成；不是只给若干足够的例子。

P/S 的十个原标签先模去两个 $\tau_0$ 盲列；余八条 current 有 R438 的一个关系，故其非盲 current 是七维。三个 $\zeta_j$ 再增加三维：
$\zeta_2$ 独有 $u^2pr^2$，$\zeta_1$ 独有 $up^2r^2$，$\zeta_0$ 的 $upr^3$ 不能由 P/S 列给出。

加入原 K 轨道，定义
$$
\boxed{\mathscr M_{21}=\mathscr M_{18}
+\operatorname{span}\{\Xi_0,\Xi_1,\Xi_2\}.}
\tag{13}
$$
先比较 K 的纯 $x^nr^5$，再按上述三个含 u 项及 R438 七列比较，得到二十一个独立原成本和二十一个 universal current 方向。
有限 jet 见证仍取 $p\ne0,t=r^2/(3p)$，四阶 jet 可另使 A 根简单。

式(13)完整描述的是 K 加上原 c=0 标签中 universal C 零的 self 像。
它不称整个 $\mathcal R\cap\ker E$ 已分类，也不将有限实际 C 核的额外关系删去。

## 5. 完整第四次镜差与新的实际第十六行

沿 R438 固定同一物理宽度、同一镜点对的
$$
s=p_*/r_*,\quad h_*=u_*/r_*,\quad
\kappa_*=-\tfrac83p_*r_*^4,\qquad p_*,r_*>0 .
$$
所有实际位置仍是 $x_j^\pm=\xi_j\pm b$，原不同中心不移动。

R435 的原生成式再取一次系数，给完整 K4 current
$$
\boxed{
\begin{aligned}
F_4={}&-896x^4r^5+3584x^2p^2r^3-448x^2ur^4\\
&-\tfrac{8960}{3}xp^3r^2-896xupr^3+512p^4r+896up^2r^2 .
\end{aligned}}
\tag{14}
$$
它也满足 $\partial_xF_4=-28F_3$；式(14)的原常项由生成式在 x=0 取得，不能从此导数关系丢掉。

令 $Q_4$ 是 K0…K4 的唯一固定实线性组合，使其**完整左侧多项式**等于 $\zeta_2^-(x)$。这是可逆五阶三角定义，不是只匹配 leading。
所有系数只依同一基点的 $(u_*,p_*,r_*)$；前两个为
$$
[K_4]Q_4=-s/672,\qquad [K_3]Q_4=-s^2/12 .
\tag{15}
$$
其余三项由(11)、R438(17)及(14)的全部二次、一次、常项依次精确确定。

为显式保原镜差，设
$C_*=(320/3)p_*^3r_*^2+32u_*p_*r_*^3$。
R438 给 $F_3^+-F_3^-=-2C_*$，而(14)给
$F_4^+-F_4^-=56C_*x$；K0…K2 镜差为零。
用这些完整身份及(15)，得到
$$
\boxed{
F_{\Xi_2-Q_4}^+(x)
=\kappa_*\left[
x^4+(20s^2-8h_*)x^2
-\left(\tfrac{10}{3}s^3+h_*s\right)x
+12h_*^2-22h_*s^2+\tfrac{56}{3}s^4
\right].
}
\tag{16}
$$
左侧则在整个对应族准确为零。式(16)包含所有低次和真常数。

取 R438 的 $L_0,\ldots,L_3$，其左值均零、右值为
$\kappa_*(1,2x,3x^2,3x^3)$。定义
$$
\boxed{
\begin{aligned}
L_4={}&\Xi_2-Q_4-\frac{20s^2-8h_*}{3}L_2
+\frac{10s^3/3+h_*s}{2}L_1\\
&-\left(12h_*^2-22h_*s^2+\tfrac{56}{3}s^4\right)L_0 .
\end{aligned}}
\tag{17}
$$
于是所有左对应点仍为零，全部右对应点准确为 $\kappa_*x^4$。

在原十一左对应点之外，选同一原库中五个不同副本的右镜点；已有十二完整 cell 足够。真实下块为
$$
\kappa_*\operatorname{diag}(\rho_j^5a^3R)
\bigl[1,\ 2x_j^+,\ 3(x_j^+)^2,\ 3(x_j^+)^3,\ (x_j^+)^4\bigr]_{j=1}^5.
$$
其行列式为
$$
\boxed{
18\kappa_*^5\prod_{j=1}^5(\rho_j^5a^3R)
\prod_{i<j}(x_j^+-x_i^+)\ne0 .}
\tag{18}
$$
连原 K0…K10 左上块，得到同一实际十六行矩阵。
原真实宽度、第五幅、$aR\ne0$、中心与右锚全保。没有新母条件、重新复制或自由移动某个 A 根。

## 6. 同一个实际截面及其范围

所有十六列都杀 $J^+$，也杀整个实际 A 根 C 向量。
因而与 R435/R438 相同，
$$
(J^+,\mathbf H_{16})(U)=J^+(U)\times\mathbb R^{16},\qquad
(J^+,\mathbf H_{16})(\mathcal R)=J^+(\mathcal R)\times\mathbb R^{16}.
\tag{19}
$$
原成本基与十六列形成固定增强基；新增 $\Xi_j$ 仍由原 E8/Z 真原型实现。
从起点把所有原型、保护芽、桥、共享真倒行、右锚、profiles 及查询点纳入同一合法窗口。

第一次实际商校正保全部 prototype 基准；第二次商校正的全部 H/C 代价也记录。内部整数先固定，最后一次有限 n 对
$n(a+Mt)+F(t,y)=y_{\rm resp}$
作统一紧目标 $C^1$ 收缩。Klein 继续先减 $V_{\rm base}$ 再除4。
因此有同一固定有限字的实际 $(J^+,\mathbf H_{16})$ 截面。

若其它 C 已按同一个实际联合接口支付，或已证明 R435 的共同响应等像条件，可同时保其它 C。没有该前提时不将两条独立实际路径拼接。
对于原完整 R/T 编码 cell 的首/末包，C 原来即由 E 因子化，故 $J^+=0,\mathbf H_{16}=0$ 支付选中十六点的两条 period 内部通量。

原 H* 的完整十六个查询值可通过(18)减去响应列，而保 $\lambda_+=1$。这只是同一有限组的 signed 核见证；其它根是否也能如此清，下一节给准确条件。

## 7. 全部同镜对副本的精确像

K 的左右多项式仍定义 R436 的真实输运 $\mathsf T$。
P/S 新列、$\Xi_0,\Xi_1,\Xi_2$ 的 left 次数分别至多3、2、3、4。
用完整 K0…K4 左基消去以后，右余式至多四次。
反过来 L0…L4 取得全部四次以下多项式。因此
$$
\boxed{
h^-(\xi)=P(\xi),\qquad
h^+(\xi)=\mathsf TP(\xi)+Q(\xi+b),\qquad
\deg P\le10,\quad\deg Q\le4 .
}
\tag{20}
$$
这里是 normalized self current，实际幅系数再乘回。
已有(18)的十六点时，整个这类对应族的 rank 恰16。

对该镜对更多副本，目标必须先满足同一个十次左多项式，且扣完整 $\mathsf T$ 后的右值必须来自同一个四次多项式。
这给本模块的准确全副本限制，不只是一个生成上界。

## 8. 支付十六行以后，原模块只余五条具体列

以下五条原成本在**整个所选镜对族**上均盲，不只杀已选十六点。
为避免把局部 monomial 当自由成本，先定义原成本代表：

- $\mathsf R=-45K_0/8$ 的 current 为 $r^5$；
- $\mathsf X=9K_1/16$ 的 current 为 $xr^5$；
- $\mathsf A=3J_\sigma/2$ 的 current 为 $p^2r^3$；
- $\mathsf B=3J_1/4$ 的 current 为 $pr^4$；
- $\mathsf B_1=3J_2/8+\mathsf A$ 的 current 为 $xpr^4$。

再令
$$
\bar J=3J_3/4,\qquad \bar W=3W_\sigma/2,\qquad \bar Z=3W_2/8,
$$
$$
\mathsf F=(\bar J-3\bar Z-10\bar W)/21,\quad
\mathsf E=(\bar J-3\bar Z-3\bar W)/7,\quad
\mathsf D=(3\bar J-2\bar Z-2\bar W)/7 .
\tag{21}
$$
其完整 currents 分别是 $p^3r^2,xp^2r^3,x^2pr^4$。
最后
$$
\mathsf G=(\mathsf D-4\mathsf E+4\mathsf F)/4-3\Xi_0/32
\tag{22}
$$
的 current 准确是 $upr^3$，由(11)直接得。

于是前四条为
$$
\begin{aligned}
\mathfrak b_0&=\mathsf A-s^2\mathsf R,&
F_{\mathfrak b_0}&=r^3(p^2-s^2r^2),\\
\mathfrak b_1&=\mathsf E-s^2\mathsf X,&
F_{\mathfrak b_1}&=xr^3(p^2-s^2r^2),\\
\mathfrak b_2&=\mathsf F-s^2\mathsf B,&
F_{\mathfrak b_2}&=pr^2(p^2-s^2r^2),\\
\mathfrak b_3&=\mathsf G-h_*\mathsf B,&
F_{\mathfrak b_3}&=pr^3(u-h_*r).
\end{aligned}
\tag{23}
$$
第五条完整成本取
$$
\boxed{
\begin{aligned}
\mathfrak b_4={}&\Xi_1-\tfrac23W_3-\tfrac7{18}s^2K_2
-\left(\tfrac{64}{3}s^2-\tfrac{32}{3}h_*\right)\mathsf B_1\\
&-\left(\tfrac{446}{27}h_*s^2-\tfrac{544}{27}s^4\right)\mathsf R .
\end{aligned}}
\tag{24}
$$
其 current 由(11)、R438(10)、原完整 K2 和(21)直接评价，不删任何项。
在 $u=h_*r,\ p=\pm sr$ 上：
$\Xi_1-\tfrac23W_3$ 的偶部是
$$
r^5\{16h_*s^2-16s^4-\tfrac{56}{9}s^2x^2\},
$$
奇部是
$$
r^5(\tfrac{64}{3}s^3-\tfrac{32}{3}h_*s)x.
$$
式(24)的后三项逐项恰消这两部，所以它也在全部镜对副本上盲。

五条 current 独立：$\mathfrak b_4$ 独有 $16up^2r^2$，再依次比较
$upr^3,p^3r^2,xp^2r^3,p^2r^3$。
由 $\dim\mathscr M_{21}=21$ 和(18)的 rank16，它们恰给原模块的整个镜对核，而非仅五个候选方向。

所有(21)—(24)的系数只由同一个参考 s、h* 固定。评价另一个宽度或另一个根时必须代入它的真实 jets，不重新选择这些系数。

## 9. 对全部真实根的准确目标比较

现在令 V 是同一库中一个实际 $J^+=0$ 成本，并假设其全部 C 已通过同一个联合接口清零。
原 $H_d,H_e$ 始终是完整 raw 积分；E 零使平台二次项零。即使要在一般 U 上扩展查询，也应先用 R435 的扣平台规范，不能静默删它。

对包 i 的任一实际根定义剩余 normalized 通道
$$
\eta_{i,\alpha}(V)=
\frac{R_iH_{d,i,\alpha}(V)-T_iH_{e,i,\alpha}(V)}
{a_i^3(R_i^2+T_i^2)} .
\tag{25}
$$
分母非零；允许 $R_i=0$，不能在全部根公式中擅除 R。
当 C=0，清(25)等价于两通道同时为零。
对本稿全部兼容列，$\eta_{i,\alpha}$ 就是其完整 current 在真实
$(x_{i,\alpha},u_i,p_i,r_i)$ 的值。

先用(18)的完整十六行逆矩阵消掉 V 的选中目标，得到唯一的
$V^\flat=V-W_{\rm core}$，其中 $W_{\rm core}$ 使用那十六条固定原列。
全部 J⁺、C 保持不变；$V^\flat$ 的原其它目标仍保所有同包历史和 ordered 尾。

构造一个明确五列矩阵
$$
\mathsf B_{(i,\alpha),j}
=F_{\mathfrak b_j}(x_{i,\alpha};u_i,p_i,r_i),
\qquad 0\le j\le4,
\tag{26}
$$
行遍历剩余全部实际根；不要求相同宽度或相同 cap 点。
由前节的完整核分类，
$$
\boxed{
\text{本模块可以在线性成本层清全部根}
\iff
\bigl(\eta_{i,\alpha}(V^\flat)\bigr)_{\rm rest}
\in\operatorname{im}\mathsf B .}
\tag{27}
$$
(26)是五条具体原成本的完整值，不只报告“至多五维”。
(27)的左边是同一个原 V 的真实积分残差，不用 whole natural self 零代替 cap 值。

两个可直接读取的边界为：

1. 若另一个实际 A 根有 $r=0$，(23)—(24)全部为零。因此在这个点
   $\eta(V^\flat)=0$ 是本模块不能再改的明确必要条件。
   本文不假定现有母必含这样的根。
2. 若一个其它根也满足 $u/r=h_*$、$p/r=\pm s$，则全部五列同样零；
   它的目标由核心十六行和真实物理 x 的(20)唯一预测，不能再给一个独立自由值。

对一般其它根，(26)准确保 $p^2-s^2r^2$、$u-h_*r$ 及第五完整余式。
任意行关系 $\ell\mathsf B=0$ 都给真实剩余条件
$\ell\,\eta(V^\flat)=0$。若不满足，只能宣当前明确 c=0/K 模块不足；
其它第三核、其它原响应或 actual 成本可能改变这个商，不能升级成主课题障碍。

最后，(27)首先是完整 signed 响应像判据。若要把全部其它根也升级为一个实际截面，还须在同一增强观察下核原响应等像/正字符及所有 prototype 基准，或取得对应完整实际联合入口。
不能因为存在一份线性修正，就把它拼接到冻结实际几何并宣全 period 已解。
本稿无条件的实际结论是第6节的同一个十六行截面；五列判据精确指出其后真正仍欠的原目标。

## 10. 已闭合与仍欠的范围

本稿已闭合原零阶零第三核中 universal C 零的全部 current 标签，保三条完整非恒尾组合、同包 primitive、真实 suffix 和物理坐标。它给二十一个 formal 方向、同一原库十六个实际内部点，以及其余全部根的明确五列余商。

它没有把 R434 的其它 whole-E 核结果提前并入，也没有把一般 actual self cap 化成只由这些 jets 决定。全部根的其它响应像、原完整 period 的仿射拼接/端点条件以及同相位十三行，仍按原真实对象和同一个实际基准继续。

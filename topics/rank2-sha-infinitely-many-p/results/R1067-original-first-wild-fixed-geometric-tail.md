# R1067 续证：原第三位尾的物理热卷积与两节点的 Frobenius

接续 [R1067 §§1--36](R1067-original-first-wild-rubin-native-euler-continuation.md)的(H1)--(H7)，记号及好素数从原文。
以下为原实际尾系数的纸面恒等式及边界 Frobenius 的计算。

## 37. 第三位尾的实际低热行及二阶原函数

沿用原 $v=B/A,\ \zeta=A/B$，所有分数幂在固定四盖 $t=x^4$ 取
$v^{1/4}=x(1+O(x^{12}))$ 的一致支。令
$$
 Q_{e,p}=(p+e-10)/4,\qquad
 \mathscr Y_e(v)=v^{e/4-4}\,y_e/A, \qquad
 \mathcal K_f(v)=A^{1/2}f .
$$
$Q_{5,p}=3m$、$Q_{11,p}=3m+3$；$\mathscr Y_e$ 只含 $v^3$ 的非负次幂，
因 $y_e\sim 32^\lambda t^{4-e/4}$ 且 $v=t(1+O(t^3))$。
原(H4)精确给
$$
 \boxed{\quad
 I_p\equiv k_p32^{p/12}
     [v^{Q_{e,p}}]\mathcal K_f(v)\mathscr Y_e(v)\pmod p .
 \quad}                                                        \tag{J1}
$$
证明先用 $ds=4x^3J dx$、$b=B/t$ 在固定四盖作特征零微分换元：
$$
 x^{-7}fJ b^{-5/2}y_e\,dx
   =\tfrac14 f B^{-5/2}y_e\,ds
   =-\tfrac14 (B^{1/2} f)(y_e/B)d\zeta
   =\tfrac14\mathcal K_f(v)(y_e/A) v^{-5/2}\,dv .
$$
(H4)取 $x^{p-1}$ 等于乘 $x^{-p}$ 后取留数。
在这一留数中，$x^{-p}$ 可模 $p$ 换为 $v^{-p/4}$，因为比为
$(v^{1/4}/x)^p$ 或其逆，该单位常数一、其余项从 $x^{12}$ 起；
在实用截窗模 $p$，其 $p$ 次幂首改正只可能在 $x^{12p}$。
所需项远小于此阶；$v/t$、$y_e$ 的实际有限整性分别由
(126)、(G6)和(H1)的单位分母给出。若双边高阶含 $p$ 分母，
此替换仅在原留数决定的有限窗使用。最后在 $v^{1/4}$ 变元取留数，
$dv/v$ 的 $x$-留数为四，正消去上式 $1/4$。
剩下的系数是 $[v^{p/4+3/2}]\mathcal K_f(v)y_e/A$，
即(J1)；所乘实际 $f$ 并没有消失。

这给明确的原物理低热卷积。令 $F_e=(D^2+a_{\rm GM})y_e$，则
$$
 \frac{d^2}{dv^2}(y_e/A)=A^3 F_e, \qquad
 F_e=\frac{D_e}{16}32^\lambda t^{2-e/4}L_e .
$$
第一式由 $dv=ds/A^2$ 和 $D^2A=-a_{\rm GM}A$ 两次求导。
$y_e/A$ 的初项次数 $4-e/4$ 不是 $0,1$，其全部次数同余模三，
故不含 $v^0,v^1$ 的积分常数。因此对 $0\le j\le Q_{e,p}$ 有
$$
 [v^j]\mathscr Y_e
 =\frac{D_e32^\lambda}
 {16(j+4-e/4)(j+3-e/4)}
 [v^j] A^3 (t/v)^{2-e/4}L_e .                              \tag{J2}
$$
$4j+16-e,4j+12-e$ 均为正数且在本窗小于 $2p$，
而它们模四均为 $-e$、与 $p\equiv e\bmod4$ 不同，
故所示两分母均为 $p$ 单位。
(120),(123)又给
$$
 [v^j]\mathcal K_f=\frac{D_z^{2j}S_1(0)}{68^j j!}.
$$
故(J1)是由 $0\le j\le Q_{e,p}\le(p+1)/4$ 的**同一原** $S_1$
实际物理热行与(J2)全部卷积产生的首层；它恰在(G10)的第三位出现。
两个边界类的非零只描述 $F_e$ 的来源，并不赋予此全卷积单位性。

## 38. 两个节点的定向分支与真实边界 Frobenius

本节计算边界上的实际算子，不将移动采样(J1)代成边界本征值。
两有理规范仍为 $E_+=e_0dx,E_-=(x^6/Y)e_0dx$。
在 $l=\pm\sqrt{-32}$ 处以 $x_{\rm ph}=x^2X_1$、
$y_{\rm ph}=x^3Y_1$ 得最小三次模型的特殊纤维
$$
 Y_1^2=X_1^3+6X_1+l=(X_1-a_l)^2(X_1+2a_l),\qquad
 a_l=-l/4, \qquad b_l^2=3a_l,\quad b_l^4=-18 .
$$
极小判据在此也直接可见：$c_4$ 为单位，原恒定非零判别式经尺度变换
产生 $\xi^{12}$ 因子，故为几何乘法约化。
归一化坐标 $v_1=Y_1/(X_1-a_l)$ 给
$$
 u_0=dX_1/(2Y_1)=\frac{dv_1}{v_1^2-b_l^2}
   =\frac1{2b_l}\,d\log q_{b_l},\qquad
 q_b=(v_1-b)/(v_1+b).                                       \tag{J3}
$$
两个节点分支由 $b$ 与 $-b$ 标记，$q_{-b}=q_b^{-1}$。
因此(H7)再取这个第二留数，把两边界线同构到有限 étale 代数
$\mathbf Q[b]/(b^4+18)$ 中的**奇函数**：
$$
 E_+\longmapsto -1/(2b),\qquad
 E_-\longmapsto -1/(2b l),\qquad l=-4b^2/3 .                \tag{J4}
$$
这里的箭头是物理 $u_0$ 的留数后再取(J3)的定向支。
它与局部 GM coinvariant 一致，一种直接核验如下。
$u_1=e_1/x$ 在最小三次模型的微分为 $X_1 u_0$，所以在节点分支
的留数是 $a_l$ 倍 $u_0$ 的留数。于是(J3)的泛函杀掉
$\operatorname{im}N_l=\langle u_0+(4/l)u_1\rangle$，因为
$1+4a_l/l=0$。它对 $u_0$ 非零，给该一维商的同构。
此核验未将 invariant line 误用作 coinvariant。

对每个原好 $p$，这个有限代数非分歧；令 $\sigma$ 为其特殊纤维
$b\mapsto b^p$ 的唯一非分歧 Frobenius 提升。
则在(J4)的归一中，边界微分的 Frobenius pullback 准确为
$$
 (F_{\rm bd}c)(b)=p^2 c(\sigma b) .                        \tag{J5}
$$
为核符号及两次 $p$，第一个参数是 $\xi$，其对数留数在
$\xi\mapsto\xi^p$ 下乘 $p$。第二个参数是(J3)的定向乘法坐标
$q_b$，在特殊纤维从源的 $b$ 到目标的 $\sigma b$ 时，
目标 $q_{\sigma b}$ 拉回为 $q_b^p$。在分裂乘法环面上
$q\mapsto q^p$ 是这个 Frobenius 的提升，故其 $d\log$ 类严格乘 $p$。
退化椭圆曲线的这一商就是环面定向线，已由上面的留数核验；
也可对照 J. Tate, *A review of non-Archimedean elliptic functions*
(1995), [作者全文](https://people.math.harvard.edu/~ctm/home/text/others/tate/tate-unif/tate-unif.pdf)
的乘法一致化。换成另一分支同时把 $q$ 取逆、对数留数取负，
这一符号已由奇函数的 $c(\sigma b)$ 计入。若局部参数另乘正则单位，
其 $d\log$ 不贡献当地对数留数。因此(J5)是在两个实际节点方向上
作用的 Frobenius；它也给§36经留数辨认的纯边界空间的算子。

具体取一个 $l$、$b=b_l$，另一点取 $b_{-l}=ib$。
记 $\epsilon=\sigma l/l=(\frac{-2}p)$ 及 $r=b/\sigma b$。
$r^2=\epsilon,\ r^4=1$。对有理规范的两线，(J4)--(J5)逐项给
$$
 \begin{array}{c|cc}
      &F_{\rm bd}E_+&F_{\rm bd}E_-\\ \hline
 p\equiv5\ (12) &p^2 r E_+&p^2\epsilon r E_-\\
 p\equiv11\ (12)&p^2 r l E_-&p^2\epsilon r E_+/l .
 \end{array}                                                   \tag{J6}
$$
这些等式指(J4)下的边界向量。第一行 $\sigma i=i$，
两 $l$ 上的 $b/\sigma b$ 相同。第二行 $\sigma i=-i$，
两 $l$ 上的该比相反，因此乘 $l$ 或 $1/l$ 于两线间互换；
因 $r^2=\epsilon$，在此行 $F_{\rm bd}^2=p^4 I$。
(H5)中使用带 $32^\lambda$ 的规范时须运输这些常数，
这两个常数未被默认为 Frobenius 固定。
(J6)完全确定的是边界算子，并非所选 $P$ 点 $y_e$ 原函数值的
Frobenius 方程，亦未把它称作完整 $I_p$ 或原 $J'(0)$ 的
Frobenius 特征值。原三位分子继续保留(G10),(J1)的整 $f$、
前缀、尾和各自系数。

## 39. 从同一 $E_-$ 的全球 Frobenius 差回到原 CM 规范原函数

令 $s_5=77\,32^{7/12}/4$、$s_{11}=5\,32^{1/12}/4$，
$E(5)=E_-,\ E(11)=E_+$，则(H5)为 $\Omega_e=s_e E(e)$。
在固定物理基中令
$$
 P_e(x)=s_e^{-1}\binom{D y_e(x)}{-y_e(x)},\qquad
 \upsilon_p=\begin{cases}
     \epsilon r,&e=5,\\
     \epsilon r/l,&e=11 .
 \end{cases}
$$
$P_e$ 按上述特征零选支计算；两分量除以 $s_e$ 后其实都在
$\mathbf Q[[x]]$，其协变导数为 $E(e)$。
(J6)的选择标记不影响 $\upsilon_p$：若换 $l$ 的符号，
第二种情形 $r$ 亦反号；第一种情形 $r$ 不变。
这些有理基的 Frobenius 矩阵系数在 $\mathbf Q_p$ 中，
因 $r^2=\epsilon$ 且 $\sigma(i)=\pm i$，或直接由(J4)有限
étale 代数的定义见之。

### 39.1 系数比较的范围与零处的规范

下面的全球比较只需在固定特征零曲面的一组好模型素数上使用。
这组比较可先于 $p$ 再删除一个有限集合；(J1)--(J6)及下一节
的逐系数手算不依赖这个额外删除。说明比较细节如下。

取固定 $C$ 上物理椭圆曲面的光滑射影极小正则模型 $S$，
记 $U=C-D_\infty$、$S_U=S|_U$。有限处是光滑椭圆族；
在两个无穷点的极小方程由§38给出 $c_4$ 为单位、判别式阶十二，
故两个几何坏纤维均为 $I_{12}$。在分裂节点切线的固定数域上
两条十二边形纤维构成严格正规交叉除子 $D_S$。
也可由节点的 $uv=\text{unit}\cdot\xi^{12}$ 模型作链式环面解消。
把这个**固定**光滑 proper 对及有限群作用铺开，
除有限个素数后得到相对光滑 proper、边界相对正规交叉的好模型。
取数域非分歧的好素数；下述物理 Frobenius 仍先从 $\mathbf Z_p$
构造再作相对标量比较。

在普通特征零相对 de Rham Leray 序列中，纤维 $[-1]^*$ 在
$R^0,R^2$ 为 $+1$，在 $R^1$ 为 $-1$。因而二阶的负特征部分
自然等于 $H^1_{\rm dR}(U,\mathcal E)$，没有异行微分可入或出。
后者由§36的对数复形计算：对每个正极阶 $n$ 的额外 principal
graded，$-nI+N_l$ 可逆，故允许任意亚纯极并不改变上同调。
$E_-,E_+$ 对应曲面上的 $e_0\wedge dx$ 乘 $x^6/Y,1$
（按统一纤维在前的约定）。对基上一形式取楔积杀掉选择相对微分
提升时的水平差；在有限光滑处给正则二形式。无穷处是一个正则
相对 dualizing 微分乘 $d\xi/\xi$。局部 $uv=\xi^{12}$ 中相对
dualizing 丛由 $du/u=-dv/v\bmod d\xi$ 生成，故二形式在
环面解消后为对数二形式。沿严格变换的节点三次曲线先取留数，
再在其归一化的两节点方向取留数，正是(J3)--(J4)。

这里可用**常系数**的光滑对比较。
A. Shiho, *Crystalline fundamental groups II: Log convergent cohomology
and rigid cohomology* (2002), [Cor. 2.3.8--2.3.9,
Th. 2.4.4(1), Cor. 2.4.13](https://www.ms.u-tokyo.ac.jp/journal/pdf/jms090101.pdf)，
在上述 proper、对数光滑、Zariski 型的特殊纤维及实际光滑对提升上，
把常系数 rigid 上同调辨认为提升的对数 de Rham 上同调：
光滑提升本身给计算管状邻域，proper GAGA 把解析对数复形的
超上同调识别为代数复形的。这里无需假设一个未证的
半权系数过收敛，亦无需 $C\to E_{16}$ 在 $x=0$ 为 étale。
比较对自动同构自然，并把几何 Frobenius 的边界作用送到两个
对数参数上的拉回。在分裂的边界正规交叉图，每个参数可取
$p$ 次幂作为对数提升，故双留数乘 $p^2$，并按(Frobenius作用于)
有限分支标记重新排列，准确为(J5)。由§36的两个特征维数及(H7),(J4)，
每个指定特征中的上同调类均由留数唯一检测。
特别在这个全球二阶负特征空间中，实际有
$$
                  F[E_-]=p^2\upsilon_p [E(e)].               \tag{K1}
$$
确实 $g,h$ 与 Frobenius 的自然性把源角送到其 $p$ 次幂角
（相对标量约定），即(J6)所示目标角；该角留数检测是单射。
这一步只在取得原受迫类的固定小曲面上进行。
(H4)的实际 $f$ 则随后仍从完整水平覆盖拉回。

在包含 $P_0=(x=0,Y=1)$ 的仿射图 $Y\ne0$ 上，取
$X\mapsto x^p$ 及§32.4的物理 Frobenius。
$Y$ 的 Hensel 公式在此也是 weak completion 上的提升：
平方根的非常数部分是 $p$ 倍的有界次数 Laurent 多项式，
其 $n$ 次幂的 $p$ 阶至少 $n$ 而次数至多线性增长。
在此图，提升的物理椭圆族是光滑 proper 的平面三次曲线。
对可提升光滑 proper 族的相对 rigid 直接像和变基，
可用 J.-Y. Étesse, *Images directes I*, JTNB **24** (2012),
[Th. 3.4.4](https://www.numdam.org/item/10.5802/jtnb.790.pdf)；
其相对 de Rham 模块即物理族的 $H^1$ 及 GM 连接，
几何 Frobenius 由直接像的自然拉回给出，限制于原盘即(F1)。
在此仿射 liftable 图的相对 de Rham 复形过滤里，
同样因 $[-1]^*$ 只在相对一次为负号，曲面二阶的负部
识别到带该 $H^1$ 系数的基曲线一次；
这是用严格邻域上的相对 de Rham 复形，再取过收敛极限的
同一 Leray 边项，且与几何拉回相容。在光滑仿射 dagger 图上，
基上一次类为零即一形式是某个全图过收敛截面的协变导数：
在仿射严格邻域用 coherent acyclicity，再取极限即得
由全局截面计算的两项复形。
所以(K1)限制给该图上的真实原函数 $T_p$：
$$
 \nabla T_p=W\varphi^*E_- -p^2\upsilon_p E(e).
$$
这里 $W$ 作用于系数，$\varphi^*$ 也拉回微分。
将原函数投到 $g$ 的指定目标特征即可。
此图 $g$ 稳定，所选 Frobenius 提升满足
$\varphi(\zeta_{12}x)=(\zeta_{12}x)^p=\zeta_{12}^p\varphi(x)$（即 $x\mapsto x^p$ 与
$g,g^p$ 相容）；物理族的 $W$ 服从相同的自然性。
该特征在 $P_0$ 为 $i$ 或 $-i$，而 $g$ 固定此点，作用于
物理纤维的两个特征为 $\zeta_{12}^{-4},\zeta_{12}^4$。
因此 $T_p(P_0)=0$。同特征的水平截面在此也必须为零，
由水平形式解唯一性给整支为零；这就选定了该原函数。
特征零形式 germ 中准确有
$$
 \boxed{\quad
 T_p(x)=W(x^4)P_5(x^p)-p^2\upsilon_p P_e(x).\quad}         \tag{K2}
$$
两侧协变导数相同，且因 $P_5(0)=P_e(0)=0$ 两侧同为零初值。
特别，全 $p$ 仅用同一实际源 $E_-$ 的全球 Frobenius 差；
未为两射线自由指定两个 primitive 常数。

由(H3)--(H5)的实际首项，
$$
 P_5(x)=\binom{x^7/7+O(x^{19})}{-4x^{11}/77+O(x^{23})}.
$$
故 $[W P_5(x^p)]_2$ 的首项准确为
$-p x^{7p}/(7u)$，其中 $u$ 是(F1)的物理 CM 单位。
由(K2)，第二分量在 $x^{<7p}$ 的特征零截窗内有
$T_{p,2}/p^2=\upsilon_p y_e/s_e$。
(H4)实际只需 $y_e$ 到 $x^{p-6}$，因为其余乘子
$x^{-7}fJb^{-5/2}$ 从 $x^5$ 起。因此得整个第三位尾的真实
过收敛原函数返回
$$
 I_p\equiv\frac{k_p32^{p/12}s_e}{\upsilon_p}
  [x^{p-1}]x^{-7}fJb^{-5/2}\frac{T_{p,2}}{p^2}\pmod p .
 \tag{K3}
$$
此处只使用已证整窗；没有声称该全图过收敛截面在整图上可整除 $p^2$。
$m$ 阶前缀、物理 $f$ 和(G10)的共同分子仍须一起消费。

## 40. $7p$ 的实际 Fermat 阶乘消去、整段共振及下一双分母

本节算式只用(F1),(F6),(H5),(J6)及(K2)的形式右端；
因此对原全部好 $p>211$ 均成立，不以§39的全球比较为整性假设。
记
$$
 k=(7p-16+e)/12,\qquad
 A_1=(28-e)/12,\quad B_1=(24-e)/12,\qquad n=(p-1)/2.
$$
$Z_e$ 的第 $j$ 系数为 $(j!)^2/((A_1)_j(B_1)_j)$。
$12i+28-e$ 首个 $p$ 的倍数为 $7p$，
$12i+24-e$ 首个为 $11p$，分别从模十二同余及正性可见。
故 $k$ 是 $Z_e$ 的首个含 $p$ 分母的指标，且该项恰有一位分母；
$y_e/s_e$ 的对应次数为 $7p$，前缀整。
因 $L_e(0)=1$，定义 $\ell_p=p[x^{7p}]y_e/s_e\bmod p$，得
$$
 \ell_p=
 \frac{4\cdot32^k}{7(12-e)\binom{(p-2)/3+k}{k}}
 =\frac1{7u\upsilon_p}\quad\text{于 }\mathbf F_p^\times.     \tag{K4}
$$
证明第一式：$A_1+k-1=7p/12$，$A_1\equiv1-k$、
$B_1\equiv2/3-k$。去掉此一个 $p$ 因子后
$(A_1)_{k-1}\equiv(-1)^{k-1}(k-1)!$、
$(B_1)_k\equiv(-1)^k(1/3)_k$，
又 $y_e/s_e=(4/D_e)x^{16-e}L_e Z_e$（自变量 $w=32x^{12}$）。
遂给 $-48 k32^k k!/(7D_e(1/3)_k)$，
用 $k\equiv(e-16)/12$、$1/3\equiv(p+1)/3$ 完成。

证明第二式时用(F6)前所得 $u\equiv-c_p$，
$c_p=\binom{n}{(p-2)/3}$。
写 $c_p/\binom{(p-2)/3+k}{k}=-G$ 模 $p$，则
$$
 G=\begin{cases}
   \displaystyle\binom n m/\binom{2m+1}m
       =(-1)^m4^{-m}(m+1)/(2m+1),&e=5,\\
   \displaystyle\binom n{m+1}/\binom{2m+2}{m+1}
       =(-1)^{m+1}4^{-m-1},&e=11 .
 \end{cases}
$$
确实 $((p-2)/3+k)!=(p-1-(m+1))!$，而 $k!$ 的 Wilson 互补
指标为 $5m+2$ 或 $5m+4$；互补两次的合符号均为负。
余式用 $\binom nj\equiv(-1)^j4^{-j}\binom{2j}j$。
因此只需 $4\,32^k G\upsilon_p/(12-e)=1$。
若 $e=5$，令 $s=2^{(p-1)/4}$，由 $m\equiv-5/12$
及 $s^4=1$，左侧为 $(-1)^m s^{-1}\upsilon_p$。
(J6)给 $r\equiv(-18)^{-(p-1)/4}=(-1)^m s^{-1}$，
因 $(3/p)=-1$；$\epsilon=(2/p)=s^2$，故等于一。
若 $e=11$，$b^{p-1}=(-18)^{3m+2}b^2$、
$b^2=-3l/4$ 给 $\upsilon_p\equiv\epsilon/(24(-18)^{3m+2})$。
左侧遂为 $-\epsilon\,2^{5(p-1)/2}/3^{(p-1)/2}=1$，
因 $(3/p)=1$、$\epsilon=-(2/p)$。这证完(K4)。

更强的消去在**整个**首分母段成立。令 $M=(p-2)/3$。
将 $Z_e$ 的 $k+h$ 项除以 $k$ 项，$0\le h\le M$ 时模 $p$ 为
$$
 \frac{((e-4)/12)_h^2}{(1)_h(2/3)_h}.
$$
这是因 $k+1\equiv(e-4)/12$、$A_1+k\equiv1$、
$B_1+k\equiv2/3$。乘 $L_e$ 后两射线都准确给(G6)的 $A$：
$e=11$ 使用 $A=(1-w)^{1/2}{}_2F_1(7/12,7/12;2/3;w)$。
因此 $p\,y_e/s_e$ 在 $x^{<11p+4}$ 窗的模 $p$ 级数为
$\ell_p x^{7p} A(x^4)$（其首段低于 $7p$ 为零）。
(F1)的 $W_{21}=-p A/u+O(x^{4p+4})$ 和(K4)现在准确给
$$
           [x^j]T_{p,2}\in p^2\mathcal O
                     \qquad(0\le j<11p+4).                 \tag{K5}
$$
在 $7p$ 起至该上限，$W P_5(x^p)$ 的第二分量在本窗只能来自
$W_{21} x^{7p}/7$；$W_{22}$ 乘 $P_{5,2}(x^p)$ 的最早项
恰是 $11p+4$。这样(K5)确使用完整 $A$ 行而非只消首项。

在下一格 $j=11p+4$，$h=M+1$ 产生第二个 $p$ 分母。
在 $Z_e$ 移位系数中新进入的因子
$B_1+k+M=11p/12$，在 $A$ 的超几何描述中相应的因子是
$2/3+M=p/3$，其余各因子模 $p$ 相同。
$e=11$ 的 Euler 前因子常数一，低于首双分母处的项乘 $p^2$
均消。故有真正两位首分母
$$
 p^2[x^{11p+4}]y_e/s_e
   \equiv\tfrac4{11}\ell_p\,p[t^{p+1}]A
   =-\frac{4u}{77\upsilon_p}\not\equiv0\pmod p .
 \tag{K6}
$$
用了(F6)及(K4)。另一方面 $W_{22}$ 乘
$-4x^{11p}/77$ 于该格的贡献准确为 $4u/77$；
$W_{21}$ 在原几何整格上整除 $p$。所以(K2)的第二分量在该格
至少整除 $p$，两个裸来源的单位首位真实相消。
此式未再给该格一次 $p$，也未从(K5)的长前缀推(G10)中合成后的
canonical 非零。

## 41. 第二共振的整段与底曲线上实际除两次 $p$ 的换提升

先不加固定模型例外，沿§40原全部好素数。设
$k_2=k+M+1=(11p-12+e)/12$、$j_2=11p+4$。
在 $Z_e$ 的 $k_2+h$ 项相对 $k_2$ 项的比中，上面两个参数
模 $p$ 均为 $e/12$，下面两个参数为 $4/3,1$。直到下一
共振之前分母均为单位。具体说 $0\le h<(2p-1)/3$，
$(4/3)_h$ 第一次失去单位是 $h=(2p-1)/3$。
此后对应的 $x$ 次数恰是 $19p$。当 $h=m+1$ 时，
分子齐来两个 $p$，并不妨碍将比值按整个窗模 $p$。
所以乘回整个 $L_e$、使用(G6),(K6)，得到
$$
 p^2y_e/s_e\equiv
 -\frac{4u}{77\upsilon_p}x^{11p+4} b(x^4)
          \pmod{p,\ x^{19p}},\qquad b=B/t.                   \tag{L1}
$$
低于 $j_2$ 的项已因至多一位分母全消。此处 $b$ 只在
$x^{<19p-j_2}$ 窗用到，所需 $(4/3)_h$ 均为单位。
在(K2)的物理端 $W_{21}$ 整除 $p$，$P_{5,1}(x^p)$ 至该窗
只有整的首项 $x^{7p}/7$；$W_{22}=-uB+O(x^{8p})$，
$P_{5,2}(x^p)$ 只用 $-4x^{11p}/77$。
这使整个 $[x^j]T_{p,2}$ 在 $j<19p$ 都整除 $p$，
而 $j<11p+4$ 已有(K5)的 $p^2$。
下面另以固定几何模型给两位整性，适用素数范围须另记。

### 41.1 固定对数椭圆晶体与两开

现取§39的固定良好铺开，再删除下述固定有限个素数。
用 $\mathcal C$ 表示固定曲线的光滑 proper 模型，$\mathcal D$
表示两条无穷截面（可先作固定数域的非分歧标量扩张）。
物理 $(\mathcal E,L,\nabla)$ 是固定代数对数格的整模型。
说明它携带这里需要的真 Frobenius。物理族可先取固定满
level $3$ 标记。这个有限 étale 标记盖在两 cusp 也能 étale
延长：在分裂几何节点的 Tate 参数 $q_{\rm Tate}$ 上，
$v_\xi(q_{\rm Tate})=12$；三除点由 $\mu_3,q_{\rm Tate}^{1/3}$
描述，后者为 $\xi^4$ 乘完备严格 Hensel 局部环中的单位。
所以特征零紧化的盖没有此处分歧；固定盖及映射可在再删有限
个素数后铺开。取满标记后的曲线到紧化 $X(3)$ 的模映射，
它由光滑处延拓（proper 曲线的赋值判据）；在两个有极 $j$ 值
的点落入 cusp，给相应的对数映射。涉及的标记群阶除 $48$。

A. Ogus, *F-crystals, Griffiths transversality, and the Hodge
decomposition*, Astérisque **221** (1994),
[§8.4 开头 pp. 175--176 及 (7.5.2),(7.5.3)](https://www.numdam.org/item/AST_1994__221__1_0.pdf)
对紧化模曲线上半稳定通用椭圆族明确给秩二、权一的 uniform
$F$--$T$-crystal，由该族的一次相对对数 crystalline 直接像得到。
其物理 de Rham 评价带对数 GM 和不变微分线。
在紧化曲线的模映射下拉回，且标记变化对物理族给自然同构，
故以 étale 下降得实际 $(\mathcal E,L)$ 上的晶体。
在特征零，这一拉回与原格在有限光滑处相同，在 cusp 两者均为
幂零留数对数延拓；§36已在 $u_0,u_1$ 中给出幂零留数。
两个固定代数延拓及 Hodge 线在特征零遂相等，所需同构及逆
均可在再删固定有限集合后铺开。这只使用通用晶体及其拉回，
允许四盖在 $x=0$ 的 Kodaira--Spencer 分歧。
对任一局部对数 Frobenius 提升 $\phi_i$，
所得 $W_i:\phi_i^*\mathcal E\to\mathcal E$ 整且
$W_i\phi_i^* L\subset p\mathcal E$；在光滑处就是§32的真晶体。
也可在整格已确定后，先在去 cusp 的稠密特殊纤维使用
(F1)的首列结论，再由向量丛模 $p$ 截面稠密消失知处处消失。

取确切两仿射 $U_*=\mathcal C-\mathcal D$、
$V=\mathcal C-\{Y=0\}$（后者含两个 cusp），作 $p$ 进完成。
其交为有限 $x$、$Y\ne0$ 图，$x$ 为 étale 坐标。
在 $U_*$ 上置
$$
 Q=Y^{2p}+32x^{12p}=1+pQ_1,\qquad
 \psi(x)=x^pQ^{-1/12},\quad \psi(Y)=Y^pQ^{-1/2}.
$$
这是该整完成环上的 Frobenius 提升，由同一分母消去方程可证。
在 $V$ 的有限部分用原 $\phi(x)=x^p$ 及对 $Y$ 的唯一 Hensel
提升。在无穷图 $\xi=1/x,z=Y/x^6$ 上，
$z^2=\xi^{12}-32,\ z\ne0$，取 $\phi(\xi)=\xi^p$，
再以 $z^p$ 为约化唯一提升 $z$。两者在交上相同；
$\xi^p$ 使它在两个 cusp 为对数提升。
所有幂级数均取模 $p$ 为一的单位根支或指定的 Hensel 支。
若系数已扩张，对完整系数用同一晶体标量约定。

### 41.2 两个 $p$ 在一形式和换提升原函数上的支付

记 $\alpha=E_-$，在交上 $\alpha=a\,dx$，
$a=(x^6/Y)e_0$。两个局部一形式
$W_i\phi_i^*\alpha/p^2$ 均整：系数在 Hodge 线，
而 $d\phi_i$ 和 $d\log\phi_i$（对数参数）各自给一位 $p$。
在交上写 $\delta=\phi(x)-\psi(x)$，
$\partial=\partial/\partial x$。两式相减的真正换提升原函数为
$$
 H_{\phi\psi}=
 \sum_{n\ge0}\frac{\delta^{n+1}}{(n+1)!}
      W_\psi\psi^*(\nabla_{\partial}^{\,n}a),\qquad
 \nabla H_{\phi\psi}=W_\phi\phi^*\alpha-W_\psi\psi^*\alpha.
                                                               \tag{L2}
$$
证明是在结晶 Taylor 同构中沿一维对角线积分。
逐项微分时，$\psi'(x)$ 与 $\delta'$ 项结合为
$\phi'(x)$ 乘端点 Taylor 级数，余下起点正是
$-\psi'(x)W_\psi\psi^*a$。这是两个实际 Frobenius
经平行移动的换提升，不是任选一个局部微分原函数。
也可对照 T. Tsuji, *Crystalline sheaves, syntomic cohomology and p-adic polylogarithms*,
[§§1--2 的晶体 Taylor 与 simplicial 计算](https://swc-math.github.io/dls/DLSTsuji2.pdf)。
在光滑交上 $\partial$ 与连接保整，$\delta\in p\mathcal O$。
$n=0$ 的第二个 $p$ 来自 $W_\psi\psi^*a\in p\mathcal E$；
$n\ge1$ 时 $(n+1)-v_p((n+1)!)\ge2$，且趋无穷，
$n\ge2$ 时此量至少三（本题 $p>211$）。故 $H_{\phi\psi}/p^2$ 整。
该积分可在交上的别的 étale 坐标中写出同一截面：
沿晶体 Taylor 对角线的形式原函数按起点零值唯一，换元保持
该值与端点；在 $p$ 进小对角线评价收敛。

这就给带 $\mathcal E$ 的整对数 de Rham Čech 一余循环，
一形式分量为上述两图的除后拉回，交分量为 $H_{\phi\psi}/p^2$。
两开交错 Čech 没有三重交条件。在有理化后它是
$F[\alpha]/p^2$；可用 Taylor 同构对两开拉回，交上从 $\psi$
到 $\phi$ 的路径积分就是从同一对角线抄回两端所需的 homotopy。
在 simplicial 的 Frobenius 计算中这正是其一次分量；
换提升时路径积分相加给 Čech coboundary。
所以(K1)准确给该类为 $\upsilon_p[E(e)]$。
也可从它在 cusp 对数图的双留数(J5)及§36的特征单射复核。

固定 proper 曲线上的两项代数对数复形
$[\mathcal E\xrightarrow{\nabla}\mathcal E\otimes\Omega^1(\log\mathcal D)]$
的超上同调在铺开环上为有限模：用两列 coherent 上同调谱
序列即可，不要求连接是 $\mathcal O$-线性的。再删固定有限
素数使其一次群无扭。平坦基变换及 proper 形式函数逐列给
本 $p$ 进完成上的同一群；有限仿射及其交的 coherent 无高阶
上同调，整完成 Čech 计算此复形。
故从上述余循环减 $\upsilon_p E(e)$ 后在**整**群中为零，
存在两图的整截面 $S_\psi,S_\phi$，满足
$$
 \nabla S_i=W_i\phi_i^*\alpha/p^2-\upsilon_p E(e),\qquad
 S_\phi-S_\psi=H_{\phi\psi}/p^2.                              \tag{L3}
$$
两提升与 $g,h$ 的相对 Frobenius 作用相容，两图亦稳定。
按规定的目标特征平均（群阶仅含 $2,3$），保持整和(L3)。
$P_0=(0,1)$ 处的 $g$ 特征比较与§39相同，给两截面皆为零。
从局部微分方程及零初值可知 $S_\phi=T_p/p^2$
为原(K2)全向量。这里指 $V$ 上的整 $p$ 进完成；(K2)原先的
过收敛截面与它在规范 germ 上相等。特别这组除固定有限例外
的素数在 $11p+4$ 及其后全部次数亦有第二位整性。
对§40全部原好素数，上述额外几何铺开的有限例外仍以(K5),(K6),(L1)为准。

## 42. 在整个分歧纤维和两个 cusp 支付极阶的原第三位输入

以横线记模 $p$，令 $M_p=(\overline{S_\phi})_2$ 为物理基底
第二分量。它在 $V$ 由上述完成的约化给代数正则截面分量。
在两 cusp 用 $u_0=xe_0,u_1=e_1/x$，于是
$S_{\phi,2} x$ 在各 cusp 正则，即 $M_p$ 各有至少一阶零。
在除去 cusp 的全仿射 $U_*$ 上，$S_\psi$ 原物理基正规。

为核分歧点成本，在 $x\ne0$ 的交用 $Y$ 作 étale 坐标；
$\alpha=a_Y dY,\quad a_Y=-x^{-5}e_0/192$，
因为 $dx=-Y\,dY/(192x^{11})$。令
$$
 D_Y=\overline{(\phi Y-\psi Y)/p}
     =\tfrac{\overline{Q_1}}2(Y^p-Y^{-p}).
$$
此式用 $\phi Y=Y^p(1-pQ_1/Y^{2p})^{1/2}$，
$\psi Y=Y^p(1+pQ_1)^{-1/2}$ 在二者均定义的图求首位。
(L2)--(L3)在此坐标约化为
$$
 \overline{S_\phi}-\overline{S_\psi}=
 D_Y\,\overline{W_\psi\psi^*a_Y/p}
       +\tfrac12 D_Y^2\,\overline{W_\psi\psi^*(\nabla_{\partial_Y}a_Y)}.
                                                               \tag{L4}
$$
$n\ge2$ 的项确已由(L2)估计消去。两个 $W$ 系数在所有 $Y=0$
处都正则，$D_Y$ 在十二个几何点各自至多 $p$ 阶极，
故 $M_p$ 在各点至多 $2p$ 阶极。此处允许
$\overline{Q_1}(Y=0)=0$，没有假设 Fermat 商为单位。

在有限仿射图 $Y^2=1-w,\ w=32x^{12}$ 上，(L3)的目标特征
给每个 $g$ 作用使第二标量分量乘 $\zeta_{12}^{16-e}$，
$h$ 作用使之为偶（$e=5$）或奇（$e=11$）。
这是把第二物理基 $e_1$ 的乘子从整个向量的特征除去得到。
有限处统一去极后，等价有
$$
 \boxed{\displaystyle
 M_p=x^{16-e} L_e(w)\,
     \frac{\Pi_{p,e}(w)}{(1-w)^p},\qquad
        \Pi_{p,e}\in k[w],\quad \deg\Pi_{p,e}\le p-1 .}       \tag{L5}
$$
确实以 $Y^{2p}$ 去极后的量在全仿射环有唯一
$A(x)+Y B(x)$ 写法，$h,g$ 迫其为上式所示的单一项。
在任一 cusp，$x^{16-e}L_e$ 恰有十一阶极；
由 $M_p$ 至少一阶零得 $11+12\deg\Pi_{p,e}-12p\le-1$。
$k$ 为原本完成处的剩余域，物理来源有理时即在 $\mathbf F_p$
下降。该多项式由任一分歧点处 $M_p$ 的整个 principal part
唯一决定：两候选差除去 $x^{16-e}L_e$ 后的分母为 $(1-w)^p$，
该点无极迫分子有 $(1-w)^p$ 因子（奇支的额外一个 $Y$ 不改变
所需的整数次幂），上述次数界迫差为零。

特别由 $\Pi/(1-w)^p=\Pi/(1-w^p)$，去掉
$x^{16-e}L_e$ 的规范第二分量在 $w$ 中的模 $p$ 系数逐 $p$ 格重复。
这是原几何差原函数的约化，而 $y_e$ 本身在(K4),(K6)有真分母。
以 $s_e$、$\upsilon_p$ 还原(K3)，就得
$$
 I_p\equiv
 \frac{k_p32^{p/12}s_e}{\upsilon_p}
 [x^{p-1}]\,x^{9-e} fJ b^{-5/2} L_e(w)\Pi_{p,e}(w)\pmod p .
                                                               \tag{L6}
$$
$(1-w^p)^{-1}$ 可在此窗取一，因为 $w^p=32^p x^{12p}$
而其余积分乘子在 $P_0$ 无极（$f$ 从 $x^{12}$ 起）。
$b=B/t$ 只在已付的低整窗使用。若需把此式写作代数 Cartier
提取，可在本窗把 $b^{-5/2}$ 换作
$(H/(C_0x^4))^{(p-5)/2}$：由(142)--(144)相同低窗内
$b\equiv H/(C_0x^4)$，右边指数多 $p/2$，常数一单位的平方根
的 $p$ 次幂模 $p$ 从 $x^p$ 前恒为一。
$f$ 仍是原冻结完整质量拉回，按原(134)亦是固定覆盖上的代数
函数（常数乘 $\Theta_f/\eta$）。(L6)进入(G10)时只替换其
真实 $I_p$，连同前缀及第二读者才能给原共同分子。

## 43. 从一个 $j=1728$ 分歧点重建全多项式并送入原共同第二位

沿用(L2)--(L6)的固定良好铺开素数。取一个分歧点
$x=x_0,\ Y=0,\ 32x_0^{12}=1$，令
$$
 v=Y^2=1-w,\quad x=x_0(1-v)^{1/12},\quad
 \rho=16-e,\quad d_5=0,\ d_{11}=1 .
$$
本节 $d_e$ 是 $L_e=Y^{d_e}$ 的奇偶，与原读者 $d=p+1$ 分开。
所有此处幂级数都在选点有限 étale 扩域中取常数一的支。
(L5)使这个单点的完整主部足够确定 $\Pi_{p,e}$；下文给出该主部
的纯有限公式，包含实际 Frobenius 的原始初值。

### 43.1 原晶体在分歧处所需的一列低窗

记 $G_\psi=(W_\psi e_0)_2/p$（$W_\psi$ 的列指目标基经拉回）。
$s'(Y)=ds/dY=J_*=-1/(48x^8)$，$a_{\rm GM}=-2x^4$。
设向量多项式 $Z_{<p}(Y)$ 由如下有限条件唯一决定：
$$
 \frac{dZ_{<p}}{dY}\equiv
 J_*\begin{pmatrix}0&a_{\rm GM}\\-1&0\end{pmatrix}Z_{<p}
          \pmod {Y^{p-1}},\qquad \deg Z_{<p}<p.               \tag{M1}
$$
第 $i+1$ 系数只除 $i+1$（$0\le i\le p-2$）。把
$H$、$DH$ 均按(F6)--(F12)的物理 Hasse 与物理 $D$ 在此图计算，
则确切初值为
$$
 Z_{<p}(0)=
 \begin{cases}
    (H(x_0,0)^{-1},\,0)^t,&e=5,\\
    (0,\,DH(x_0,0)^{-1})^t,&e=11 .
 \end{cases}                                                 \tag{M2}
$$
证明：在该点 $\psi(Y)=0$，且 $\psi(x_0)$ 为 $x_0^p$
剩余类在 $32X^{12}=1$ 中的唯一提升，即该有限标记的
Frobenius 像。源、目标物理椭圆纤维都是 $j=1728$，
$(X_{\rm ph},Y_{\rm ph})\mapsto(i^2 X_{\rm ph},i^3Y_{\rm ph})$
使 $e_0,e_1$ 特征为 $i^{-1},i$。Frobenius 自然性使
$W_\psi(0)$ 在 $p\equiv1\bmod4$ 为对角、在
$p\equiv3\bmod4$ 为反对角。这是实际几何 $W$ 的纤维；
杯积规范给 $\det W_\psi(0)=p$。
在光滑图上不同提升的 $W$ 模 $p$ 相同（晶体 Taylor 的
非常数项至少一位 $p$，适用于相同约化）。
(F12)中 $W_{22}=H,\ W_{12}=-DH\bmod p$ 与此行列式即给(M2)。
无需选择哪个抽象 CM Jacobi 单位作下一位提升。
例如 $H=[X^{p-1}](X^3+6x^4X+Y)^n,\ n=(p-1)/2$，
$n$ 偶时 $H(x_0,0)=\binom n{n/2}(6x_0^4)^{n/2}$；
$n$ 奇时 $H(x_0,0)=0$ 且
$$
 H_Y(x_0,0)=n\binom {n-1}{(n+1)/2}(6x_0^4)^{(n-3)/2}\ne0.
$$
上式 $Y$ 为底曲线参数；$x'(0)=0$，且 $D=J_*^{-1}\partial_Y$，
故(M2)两者均为真正单位。

由水平性，
$\nabla(W_\psi e_0/p)=W_\psi e_1\,\psi^*(ds)/p$。
$\partial_Y(\psi Y)/p$ 在整图的原点至少有 $p-1$ 阶零，
因 $\psi Y=Y^p(1+pQ_1)^{-1/2}$。
目标处 $J_*$ 正则，故(M1)准确给
$$
 \overline{G_\psi}\equiv (Z_{<p})_2\pmod {Y^p}.             \tag{M3}
$$
若 $e=11$，还可能形式上要求 $Y^p$ 的系数；它精确为零。
事实上 $h$ 使 $Y\mapsto-Y$、$e_0,e_1$ 分别乘 $i^{-1},i$，
并使 $\psi$ 与 $h^p$ 相容。由此
$G_\psi(-Y)=i^{-(p+1)}G_\psi(Y)$，在 $e=11$ 为偶，
在 $e=5$ 为奇。这个奇偶也可用 $J_*,a_{\rm GM}$ 为偶与(M2)
在已定低窗核验；额外 $Y^p$ 处使用真晶体对称性。

### 43.2 完全展开一个 branch 的两项

置 $q_c=(32^{1-p}-1)/p\bmod p$，在 $k[v]/(v^p)$ 中记
$$
 Q_c(v)=q_c-\sum_{n=1}^{p-1}\frac{v^n}{n}.
$$
因为 $pQ_1=v^p+32^{1-p}(1-v)^p-1$，且
$\binom p n(-1)^n/p\equiv-1/n$，故此即 $\overline{Q_1}$ 的整个
所需窗。在(L4)的第二分量中
$$
 \overline{(W_\psi\psi^*a_Y/p)_2}
   =-\frac{x^{-5p}}{192}\overline{G_\psi},\qquad
 \overline{(W_\psi\psi^*(\nabla_{\partial_Y}a_Y))_2}
   =\frac{x^{-13p}}{9216}H .
$$
第二式用 $a_Y=-x^{-5}e_0/192$、$ds/dY=-x^{-8}/48$；
导数的 $e_0$ 系数被 $W_\psi$ 模 $p$ 杀掉，$e_1$ 系数完整保留。
又 $D_Y=-\tfrac12 \overline{Q_1}Y^{-p}(1-Y^{2p})$。
所以 $\Pi(1-v)$ 就是下面在 $v^p$ 前截断的度 $<p$ 多项式：
$$
 \boxed{\displaystyle
 \Pi_{p,e}(1-v)=
 \left.
 x^{-\rho}\left\{
 \frac{Q_c(v)x_0^{-5p}}{384}\,Y^{p-d_e}(Z_{<p}(Y))_2
 +\frac{Q_c(v)^2x_0^{-13p}}{8\cdot9216}\,Y^{-d_e}H(x,Y)
 \right\}\right|_{v^{<p}} .}                                 \tag{M4}
$$
$Y^{-d_e}H$ 总是正则偶级数：其各单项式的 $Y$ 次数同余
$n\bmod2$，由 Hasse 的上式直接见到。第一项的偶性由(M3)给。
为逐精度核验，(L5)给
$\Pi(1-v)=x^{-\rho}Y^{2p-d_e}M_p$。
$S_{\psi,2}$ 在该点正则并带 $Y^{d_e}$（$h$ 的同一规定特征），
故其乘积整除 $Y^{2p}$。在剩下两项中
$1-Y^{2p}$ 及其平方可改为一，$x^{-5p},x^{-13p}$ 可分别
换为 $x_0^{-5p},x_0^{-13p}$，因 $x/x_0=1+O(Y^2)$。
当 $d_e=1$ 时第一项虽要求 $\overline{G_\psi}\bmod Y^{p+1}$，
唯一额外系数已由真奇偶杀掉。这证得(M4)，未把两个 $D_Y$
校正合并成单一端点或漏掉 $q_c$。

例如令 $d=d_e$，在原 $Y=0$ 点立即得
$$
 \Pi_{p,e}(1)=
 \frac{q_c^2\, [Y^d]H(x(Y),Y)}
      {8\cdot9216\,x_0^{13p+\rho}} .                         \tag{M5}
$$
其非零条件精确为 $q_c\ne0$。这个值使用全多项式的一个端点；
canonical 提取没有据此改成 Fermat 商条件。

### 43.3 返回实际冻结 $f$ 的两条分子

设 $\nu=(p+e-10)/12=m+(e-5)/6$，写(M4)为
$\sum_{i=0}^{p-1} c_{i,p}v^i$。在所有其余因子中保留同一实际
$f_*(w)$，令
$$
 K_e(w)=f_*(w)(1-w)^{-1/2}b(w)^{-5/2} L_e(w),\qquad
 \mathcal M_{i,p}(f)=
 \sum_{j=0}^{\nu}(-1)^{\nu-j}\binom i{\nu-j}[w^j]K_e(w).
$$
这些有限低系数亦可依(L6)把 $b^{-5/2}$ 换成真实 Hasse
$(H/(C_0t))^{(p-5)/2}$；所有原水平 $\gamma_a$ 保留。
因 $f$ 的三重 $t$ 零，$[w^0]K_e=0$。
在(L6)换 $w=32x^{12}$、用
$s_e=(D_e/4)32^{(12-e)/12}$ 后得到
$$
 I_p\equiv {\cal I}^{1728}_p:=
 \frac{k_pD_e32^{N/3}}{4\upsilon_p}
    \sum_{i=0}^{p-1}c_{i,p}\mathcal M_{i,p}(f)\pmod p.       \tag{M6}
$$
常数核验为
$p/12+(12-e)/12+\nu=(p+1)/6=N/3$。
所有 $c_{i,p}$ 由(M1),(M2),(M4)已定；右端无未定的
几何 Frobenius 系数。各标记 $x_0$ 的构造给同一 $\Pi$，
因为(L5)的全局来源固定。

于是当 $g_{1,p}\in p$，对原 $k=1,2$ 真有
$$
 \boxed{\displaystyle
 \frac{\mathcal U_1(\Xi_{k,p})}{p^2}\equiv
 k\gamma\mathsf a_p\left(\frac{E_N^0}{p^2}
                        -\tfrac32 {\cal I}^{1728}_p\right)
       -\mathsf b_p\frac{E_d^0}{p}\pmod p.}                 \tag{M7}
$$
两个前缀分别按(G8)--(G10)保留三位、两位，
实际尾由另一 CM 纤维的单一完整主部返回。
按(G4)，第一条 canonical 第二位取 $k=2$ 并乘 $\gamma^{-2}$；
第二条取 $k=1$ 并乘 $-\gamma^{-2}$。
(M5)与(M7)读取不同系数组合；(M7)的明确幂和尚未证明在
无穷原素数上非零。

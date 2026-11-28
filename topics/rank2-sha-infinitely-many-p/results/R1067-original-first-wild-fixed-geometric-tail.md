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

## 44. 原 $A$ 归一行的全局两位由一个分歧主部决定

在§§41--43的固定好模型上保留 $U_*,V,\phi,\psi$，记
$G_i=(W_i)_{21}/p,\ S_i=(W_i)_{22}$。
为免混淆，本节 $S_i$ 是矩阵条目；§41的整原函数仍写
$T_i/p^2$，其模 $p$ 第二分量记 $M_i$，其中 $M_\phi=M_p$。
所有矩阵均在原物理基 $e_0,e_1$ 中读。

在 $V$ 两 cusp 的框架是 $u_0=xe_0,\ u_1=e_1/x$。
$\phi^*u_0=x^p\phi^*e_0$ 和 Hodge 首列整除 $p$ 给
$x^{p+1}G_\phi$ 在两 cusp 都正则。物理 $g$ 的同质因子
$\lambda_g=\zeta_{12}^4$ 给
$G_\phi(\zeta_{12}x,Y)=\lambda_g^{-(p+1)}G_\phi(x,Y)=G_\phi(x,Y)$，
因为 $3\mid p+1$。故每个有限模 $p^r$ 的 $G_\phi$ 下降到
$Y$ 直线，唯一有可能出现的极在 $Y=0$，在 $Y=\infty$ 有零。
具体说，在 $Y\ne0$ 的有限图取 $\mu_{12}$ 不变元，
它是 $(\mathcal O/p^r)[Y,Y^{-1}]$，因为 $x^{12}=(1-Y^2)/32$。
其限制至两 cusp 的零阶排掉所有非负 $Y$ 次幂，包括常数。
故整个 $G_\phi\bmod p^r$ 就是在任一 $x=x_0,Y=0$ 点所取的
严格负 $Y$ 幂 principal part，降维和去常数均真实成立。

在该分歧处，按§43的 $J_*=-1/(48x^8)$ 把物理首列的换提升
Taylor 到两位。记 $\delta=\phi Y-\psi Y$，置
$$
 X_1=\frac{\delta}{p}\psi^*J_*+
             \frac{\delta^2}{2p}\psi^*(\partial_Y J_*).
$$
$\nabla_{\partial_Y} e_0=J_* e_1$，
$\nabla_{\partial_Y}^2 e_0=J_*' e_1-a_{\rm GM}J_*^2 e_0$。
最后一项另由 $W_\psi e_0\in p\mathcal E$ 提供一位；
阶数 $n\ge3$ 的 Taylor 项在除 $p$ 后仍整除 $p^2$。所以
$$
             G_\phi-G_\psi\equiv X_1 S_\psi\pmod{p^2}.
                                                               \tag{N1}
$$
所用 Laurent 系数全显式：
$$
 \frac{\delta}{p}\equiv
 \frac{Q_1}2(Y^p-Y^{-p})-
   \frac{pQ_1^2}{8}(Y^{-3p}+3Y^p)\pmod{p^2},\quad
 \psi^*J_*=-x^{-8p}Q^{2/3}/48 .
$$
$J_*'=-Y/(1152x^{20})$ 也在全分歧盘整。
因此 $X_1\bmod p$ 的极至多 $p$，$X_1\bmod p^2$ 的极至多 $3p$。

只需一个 $Y^{<p}$ 的两位单位提升，且其在物理 CM 本征线上的
第二位自由度从答案精确消失。取任一单位
$\Lambda$ 提升 $e=5$ 的 $H(x_0,0)$ 或 $e=11$ 的 $-DH(x_0,0)$。
用(M1)的同一矩阵，在 $(\mathcal O/p^2)[Y]/Y^p$ 的次数
$<p$ 多项式上解其递推（微分方程仅到 $Y^{p-1}$），
初值取 $(0,\Lambda)^t$ 或 $(\Lambda,0)^t$；记第二分量为 $Z^*$。
该列对应 $W_\psi e_1$，与(M1)--(M3)的除后首列不同。
证明是
$\nabla W_\psi e_1=-(\psi^*a_{\rm GM})W_\psi e_0\,\psi^*ds
 \in p^2\mathcal E\otimes\Omega^1$；在 CM 点两种初列的方向由
(M2)的同一 $i$ 作用固定。故存在常数 $\lambda\equiv1\bmod p$，
使 $Z^*=\lambda S_\psi\bmod(p^2,Y^p)$。全图仍有
$S_\psi\bmod p=H$。在所选分歧盘用特征零物理 Hasse 多项式作提升，
置
$$
 S^*(Y)=H(x(Y),Y)+[Z^*(Y)-H(x(Y),Y)]_{Y^{<p}},\qquad
 {\cal L}_p(Y)=\operatorname{pp}_{Y=0}(X_1 S^*(Y))\pmod{p^2}.
$$
$S^*-\lambda S_\psi$ 在整盘处处为 $p$ 倍，且其 $Y^{<p}$ 窗
模 $p^2$ 为零。由于 $X_1$ 的首位极至多 $p$，第二位极至多
$3p$ 而后者已乘 $p$，这些误差不改变严格负幂。
$G_\psi$ 在该点正则；用(N1)及前述降维唯一性即有
$$
 {\cal L}_p=\lambda G_\phi\pmod{p^2},\qquad
 U=\frac{G_\phi}{G_\phi(P_0)}
   \equiv U_{\rm br}(Y):=\frac{{\cal L}_p(Y)}{{\cal L}_p(1)}
                                       \pmod{p^2}.             \tag{N2}
$$
$G_\phi(P_0)=-1/u$ 是真正单位。因此没有未支付的 $j=1728$
第二位本征值，所选 $\Lambda$ 对归一比无影响。
在原 $N,d$ 两个读者的低窗，(F2)给 $U=A$。
$E_N$ 中 $U$ 的指数为 $p/2$：两单位模 $p^2$ 相同且
常数一，取该幂模 $p^3$ 也相同；$E_d$ 所需则只是模 $p^2$。
所以(N2)已经付足两条 canonical 在原 $A$ 因子所需的全部精度。

## 45. 原 $S=W_{22}$ 三位的 cusp 前缀与分歧尾恰好拼回

$\nabla_{\partial_Y}e_1=c e_0$，其中
$c=-a_{\rm GM}J_*=-1/(24x^4)$。与(M4)原受迫 $E_-=a_YdY$
的标量 $a_Y/e_0=-1/(192x^5)$ 比较，恰有
$c=8x(a_Y/e_0)$。在两提升间 Taylor 到 $p^3$，首项
$\delta(\psi^*c)W_\psi e_0$ 有两位，二阶
$\delta^2\psi^*(c' e_0+cJ_*e_1)/2$ 经 $W_\psi$ 后只有
$e_1$ 项可在第二位存活，三阶及以上消去。因此
$$
 \frac{S_\phi-S_\psi}{p^2}
 \equiv D_Y c^p \overline{G_\psi}
      +\tfrac12 D_Y^2(cJ_*)^p H
   =8 x^p(M_\phi-M_\psi)\pmod p .                            \tag{N3}
$$
右式恰是(L4)的两个真正换提升项同乘 $8x^p$，
没有额外的 Riccati 常数或自由选支。
故模 $p^3$ 的标量
$$
 S_\phi-8p^2 x^p M_\phi
$$
在交上等于 $S_\psi-8p^2x^pM_\psi$；$p^2M_i\bmod p^3$
为约化截面乘 $p^2$ 的规范意义。右端在 $U_*$ 全有限图正则，
左端在两个 cusp 有至多 $p-1$ 阶极：矩阵条目来自
$\phi^*u_1=x^{-p}\phi^*e_1$ 及 $x^{1-p} S_\phi$ 正则，
原函数项则来自(L5)的 $M_\phi$ 至少一阶零。

在有限图的全局正规函数环内，$g$ 的相对拉回给
$S_\phi(\zeta_{12}x)=\zeta_{12}^{4(p-1)}S_\phi(x)
=\zeta_{12}^{4}S_\phi(x)$，相同的特征也适用于
$x^p M_\phi$，因为 $p+16-e\equiv4\bmod12$。
$h$ 给 $S_\phi$ 标量特征 $i^{p-1}$，即 $e=5$ 偶、
$e=11$ 奇。于是上述合成的全局函数**整除** $t=x^4$，
其商形如 $L_e(w)Q_m(w)$。除 $x^4$ 后在两 cusp
极阶至多 $p-5$，即 $6d_e+12\deg Q_m\le p-5$，
所以 $\deg Q_m\le m$。这些次数界也适用于模 $p^3$ 的整模型：
在自由表示 $A(x)+YB(x)$ 中两个方向的首项由两个 cusp 的界
同时限制，固定特征又只留下其中一个方向。

在 $P_0$ 的特征零低窗 $S_\phi=-uB+O(t^{2p})$。
(L5)又使 $x^{p-4}M_\phi$ 从 $x^{p+12-e}=32^{-(m+1)}w^{m+1}$
阶起。因此前 $m+1$ 个 $w$ 系数准确为 $-u L_eP_m$
的同一前缀；$L_e$ 常数一，所以逐系数确定 $Q_m=-uP_m$。
这得**全 $V$ 上的矩阵等式**
$$
 \boxed{\displaystyle
 S_\phi\equiv -u\,t\,L_e(w)P_m(w)+8p^2 x^p M_\phi
                                     \pmod{p^3}.}             \tag{N4}
$$
作为规范检验，读 $S_\phi/t$ 的 $w^{m+1}$；
(K3)低窗给 $M_\phi=(4\upsilon_p/D_e)x^{16-e}L_e Z_e$。
(G7)同一系数给
$-u k_p32^{m+1}=32\upsilon_p/D_e\bmod p$。
因此(N4)的拼接首格不能再独立选择另一单位。
(N4)的多项式前缀保留(G8)的三位；全部非多项式校正由原
$M_\phi$ 的分歧主部给出。

令 $V_{\rm br}=
 L_eP_m-(8p^2/u)x^{p-4}M_\phi\bmod p^3$。
分数 $1/u$ 只在 $p^2$ 项中需要，取(F6)前的
$u\equiv-C_0\bmod p$ 即足。
由(M4)它是原固定分歧点的可写有理函数，且常数一。
由(N2),(N4)于原低窗分别归一 $U,V$，(F3)的完整输入现在为
$$
 \begin{aligned}
 \mathcal A_{N,p}&=
  [t^N]fJ\,U_{\rm br}^{p/2} V_{\rm br}^{-(p+3)/2}\pmod {p^3},\\
 \mathcal A_{d,p}&=
  [t^d]fJ\,U_{\rm br}^{p+1/2} V_{\rm br}^{-p-2}\pmod {p^2}.
 \end{aligned}                                                \tag{N5}
$$
两有理核均取常数一的正规幂；$x^{p-4}M_\phi$ 的 $x$ 次幂
属 $12\mathbf Z$，在所选 $P_0$ 盘内是 $w=32t^3$ 的函数。
原 $f$ 三重零使矩阵替换从未越过(F2)准确低窗。
在 $g_{1,p}\in p$ 时取任意同精度代表，原两条共同分子为
$$
 \frac{\mathcal U_1(\Xi_{k,p})}{p^2}
 \equiv k\gamma\mathsf a_p \frac{\mathcal A_{N,p}}{p^2}
       -\mathsf b_p\frac{\mathcal A_{d,p}}p
                                      \pmod p,\qquad k=1,2 .  \tag{N6}
$$
这里先以(N5)在所指精度整合，再在已有整性下除。
与(M7)相比，(N5)还把前缀中的 $A$ 与原 $S$ 的三位分别
完全还原到实际分歧主部及付清的 cusp 多项式。原水平 $f$、
$\mathsf a_p,\mathsf b_p,\gamma$ 及(G4)的两种符号均照旧。
(N6)所需的跨素数非零性仍待证明。

## 46. 原两条半权 theta 的全部同源 Fourier 行

本节固定 $M=68\cdot6^2$，限制至 $p\equiv-1\bmod M$ 且在前文所有固定好模型的素数。这是 Dirichlet 给出的无穷惰性子列。写 $d=p+1$，$N=d/2$，$h=N-1$，$\chi=(\,\cdot\,/p)$（零处取零），$\sigma=\chi(-1)=-1$，$\mathfrak G=\sum_{a\bmod p}\chi(a)\zeta_p^a$，所以 $\mathfrak G^2=\sigma p$。这一段不预置任何一个 $p$ 的 canonical 非零。

### 46.1 真实 Fourier 项和有限整矩阵

令 $F$ 分别为(134)的 $\Theta_f,\Theta_g$；全部原 $\gamma_a,\delta_b$ 仍在其内。置
\[
 \tau_j=(\tau+Mj)/p,\qquad W_j=F(\tau_j),\quad
 W_\infty=\epsilon\mathfrak G F(p\tau),\qquad
 \epsilon_f=\chi(M/68)=1,\quad
 \epsilon_g=\chi(M/4)=\chi(17)=1 .
 \tag{P1}
\]
最后的同号使用 $p\equiv-1\bmod17$ 和 $17\equiv1\bmod4$。对每个 $x\equiv a\bmod 34$ 或 $x\equiv b\bmod2$，有限 $j$ 处的相位分别为 $\zeta_p^{(M/68)jx^2}$ 或 $\zeta_p^{(M/4)jx^2}$。零频只由 $x=pz$ 贡献，对应 $a,b$ 换为 $p^{-1}a,p^{-1}b$。在本子列前者是 $-a$，后者是 $b$，而 $\vartheta_{34,-a}=\vartheta_{34,a}$，无须令 $\gamma_{-a}=\gamma_a$。

取 $v_j=(j,1)^t,\ v_\infty=(1,0)^t$，$C_{ij}=\chi(\det(v_i,v_j))$。所有 $\tau$ 上准确有
\[
 CW=\epsilon\sigma\mathfrak G W,\qquad C^2=\sigma p I .
 \tag{P2}
\]
确实在非零频 $k$ 上，$\sum_j\chi(i-j)\zeta_p^{jk}=\sigma\chi(k)\mathfrak G\zeta_p^{ik}$。常频项由 $C_{i\infty}=\sigma$ 配回，$\infty$ 行则是 $\sum W_j=p F(p\tau)$。用全部非零加性特征及常行、$\infty$ 行即得 $C^2$。所以(P2)也约束每个变形阶的整个向量。这里的 $C$ 是带两条指定同质向量的矩阵。

取一个 $\mathbf F_p$ 线性同构 $L:\mathbf F_p^2\to\mathbf F_{p^2}$（§47按物理角决定两个共轭选择之一），定一条标记线 $i_0$，缩放至 $L(v_{i_0})=1$。选 primitive $\lambda\in\mathbf F_{p^2}^{\times}$，$B=L^{-1}\lambda L$。若 $Bv_i=s_i v_{Bi}$，对标准向量置 $S e_i=\chi(s_i)e_{Bi}$。有
\[
 CS=-SC,\quad S^d=-I,\quad \xi=[\lambda^h]\quad
 (\operatorname{ord}\xi=2d).
\]
方括号表示非分歧环的 Teichmüller 提升。前一式由 $\chi(\det B)=-1$，第二式因 $B^d=(N\lambda)I$ 且 $N\lambda$ 是 $\mathbf F_p^\times$ 生成元。$B$ 在射影线上是一条 $d$ 循环。对奇数 $r\bmod2d$ 的特征基
\[
 e(r)=\sum_{k=0}^{d-1}\xi^{-rk}S^ke_{i_0}
\]
有 $Se(r)=\xi^re(r)$，且该基在当前位整可逆。故
\[
 Ce(r)=b_r e(r+d),\qquad b_r b_{r+d}=\sigma p .
 \tag{P3}
\]
这里 $b_r=\sum_{k=0}^{d-1}\xi^{-rk}\chi(\det(v_{i_0},B^kv_{i_0}))$，因为 $e(r+d)$ 的 $i_0$ 项为一。取 $\det(v_{i_0},v')=1$, $L(v')=\delta$。于是前述行列式为 $(\lambda^{kp}-\lambda^k)/(\delta^p-\delta)$。将其 $h$ 次幂展开，并用 $\sum_{k=0}^{d-1}(\bar\xi^{2j+1-r})^k$ 的正交性，得
\[
 \bar b_{2n+1}=
 \begin{cases}
 d(\delta^p-\delta)^{-h}(-1)^{h-n}\binom hn,&0\le n\le h,\\
 0,&h<n<d .
 \end{cases}                                                   \tag{P4}
\]
后一半由(P3)恰有一位 $p$。模 $p$ 的 $C$ 的核还有一个直接描述。$C_{ij}=\det(v_i,v_j)^h$ 是齐次 $h$ 次多项式的评值列。$(X-aY)^h$ 的二项式系数都非零，取 $h+1$ 个不同 $a$ 用 Vandermonde 即张成全部这样的多项式。评值在全部 $d=p+1$ 条线上单射。故 $\operatorname{im}\bar C$ 是整个次数 $h$ 的评值空间，维数 $h+1=N$，由(P2)亦等于 $\ker\bar C$。

## 47. 真实目标标记、有界整旋转参数和所有半权符号

### 47.1 原形变盘的框架及两条准确系数

在原 $j=0$ 点用 $t$ 盘，有限 étale 水平标记取原 $\widetilde P$；这里不取 $x^4=t$ 的分歧盘。源和目标用同一物理 $E_1:y_{\rm ph}^2=x_{\rm ph}^3+1$ 的 canonical CM lift。原 Gauss--Manin 基取 $e_0,e_1$，$\operatorname{Fil}^1=e_0$，以实际标定的两个水平基向量写 $e_0=A h_0+B h_1$。由 $A(0)=1,\ A'_s(0)=0,\ B(0)=0,\ B'_s(0)=1,\ dt/ds(0)=1$，$v=B/A$ 切线为一；Kodaira--Spencer 切线为同构。故在固定好位，$t$ 是此一致整形变盘的参数。可在有限非分歧扩域或其完备非分歧闭包证明，估值仍以 $v_p(p)=1$。

Serre--Tate 的形变等价将这张有素于 $p$ 标记的盘识别为原高度二形式群的有标记形变盘。特别 $\mu_{p^2-1}\subset\mathcal O_{\mathbf Q_{p^2}}^\times$ 通过改变特殊纤维的形式群标记在盘上整作用。它固定 canonical CM lift，因为该 lift 本身有全部这些形式群自同构。晶体与 Hodge 线的作用也整；水平 Betti 符号 $h_0,h_1$ 在此只表示取原 CM 值的水平晶体基，两个 CM 本征特征为 $a\mapsto a,\bar a$（顺序依嵌入）。因此 $v=B/A$ 按两者之商的阶 $d$ 特征 $\kappa$ 变换，切线同型也给此特征。这里用的是形式群和其晶体的局部作用，不把这些 $p$ 进单位说成整椭圆曲线的全局自同构。

对 $t$ 作 $\kappa$-Reynolds 投影，得到 $y=t+O(t^2)$。对 $e_0$ 作其纤维 CM 特征的 Reynolds 投影，得到 $\widetilde e_0=l(y)e_0,\ l(0)=1$；两次都只除 $p^2-1$。整性来自普遍形式群及其 Hodge 线上的整群作用；这里并未断言水平函数 $A,B$ 的全部系数整，原 $A$ 在 $d$ 次的 $p$ 分母仍保留。在坐标 $y$ 下群按 $y\mapsto\kappa(a)y$ 作用。按原水平基展开新 Hodge 框架，得到
\[
 \widetilde A=lA=\mathcal A(y^d),\qquad
 \widetilde B=lB=y\mathcal B(y^d),\qquad
 \mathcal A(0)=\mathcal B(0)=1 .                             \tag{P5}
\]
因为换 Hodge 框架后系数的特征分别为平凡和 $\kappa$。实际质量换成 $\widetilde f=l^{-1/2}f=\sum c_i y^i,\ \widetilde g=l^{-1/2}g$。取常数一的平方根；质量仍整，$\widetilde f$ 仍至少三重零，$\widetilde g(0)=1$。特征零下 $v=y+O(y^{d+1})$，且
\[
 \sqrt A f=\sqrt{\widetilde A}\,\widetilde f,\qquad
 [v^N]\sqrt A f=c_N=E_N,\qquad [v^d]\sqrt A f=c_d=E_d .     \tag{P6}
\]
后两式按 $t=t(v)$ 展开，等价于(123),(127)的 $\mathsf T_j f/j!$。$v/y-1$、$\widetilde A-1$ 从 $y^d$ 起；在 $d$ 次可能混入的常数项恰是 $\widetilde f(0)=0$。所以(P6)是原两精度前的准确等式。

### 47.2 在同一目标标记上对全部商统一读数

(P1)的有限分支以 $z\mapsto z$ 从 $\mathbf Z+\mathbf Z\tau$ 到 $\mathbf Z+\mathbf Z\tau_j$，无限分支以 $z\mapsto pz$ 到 $\mathbf Z+\mathbf Zp\tau$。标准 $M$-level 的推前标记相对于目标标准标记分别为 $D_f=\mathrm{diag}(1,p)$、$D_\infty=\mathrm{diag}(p,1)$：$Mj$ 不改变模 $M$ 标记。由于 $p\equiv-1\bmod M$，$D_\infty=-D_f$。将无限分支的同源取负。全部 $p+1$ 条带符号的同源遂以同一个 $D_f$ 运输标准基。

具体选源 canonical CM lift 的 $M$-标记，使其特殊纤维经相对 Frobenius 后恰为 $D_f$ 作用于**指定的原目标**标记。该选取存在且唯一，因为素于 $p$ 的标记上相对 Frobenius 为同构；其 Weil 配对因子正是 $\det D_f=p$。给定的该源标记可用复有向周期基实现，因 $\mathrm{SL}_2(\mathbf Z)\to\mathrm{SL}_2(\mathbf Z/M)$ 满射。所有商经其特殊纤维 quotient by $\ker(\mathrm{Fr})$ 的标记后，都落在上述原目标盘；无限处分支的取负也计入该识别。完整级杀掉目标的自同构歧义。

使用原半权质量时只需先下降三个乘积 $\Theta_f^2,\Theta_f\Theta_g,\Theta_g^2$ 和比值。它们属于实际双 unary 格的权一 Weil 表示：合并判别模后为偶 signature，level 整除 $68$。Strömberg, *Weil representations associated to finite quadratic modules*, Lemma 5.12 及其 $\epsilon_Q$ 的定义给 $\Gamma(68)$ 上恒等的此双格作用。故三个乘积在所选 $M$ 级及物理微分上准确读数；平方后的下降不需要一个未核的半权群分裂。未平方支由 $\widetilde g(0)=1$ 及下段全部相对符号固定；在原点 $g$ 是单位，$f/g$ 即三个乘积给的实际商。

将(P1)除去相同的源半周期常数（例如(134)的 $\lambda_s^{1/2}/\sqrt{2\pi}$）。若 $a_i$ 为实际带符号同源的微分拉回因子，则 $W_{f,i}^2=a_i f(t_i)^2,\ W_{g,i}^2=a_i g(t_i)^2,\ W_{f,i}W_{g,i}=a_i f(t_i)g(t_i)$，式中 $W$ 已除共同因子。有限分支的微分因子为 $\lambda_i/\lambda_s$。无限分支为 $-p\lambda_\infty/\lambda_s$，这恰是 $\mathfrak G^2\lambda_\infty/\lambda_s$。混合乘积又有 $\epsilon_f\epsilon_g=1$。这些等式是权一形式与同源的代数身份，故可在共同代数嵌入后比较 $p$ 进 germs；无需搬运复周期本身。换成(P5)的两个框架时，只须用新微分的拉回因子以及 $\widetilde f,\widetilde g$，共同源标量随之更换。

各条带标记同源在特殊纤维均为同一个相对 Frobenius，故在源、目标晶体水平框架间是同一个常矩阵。此由有标记的 Dieudonné 准同源的函子性给出，并非断言所有不同的特征零同源在固定椭圆曲线上相等。源、目标 $0$ 的 CM 作用把该矩阵置于反对角；原(F1),(F2)的相应非对角单位写 $u$（换相容源基也只改共同常数）。一般源参数下，Hodge 线比较给
\[
 \zeta(y_i):=\widetilde A(y_i)/\widetilde B(y_i)=Z,\qquad
 a_i=u\,\widetilde B(y_i)/\widetilde A_s .
 \tag{P7}
\]
$Z$ 为源 $v_s$ 的一个固定非零倍数，源 CM 时 $Z=0$。两式也可直接将两条 Hodge 线的水平坐标乘同一个反对角矩阵得到。此处 Gross--Hopkins, *The rigid analytic period mapping, Lubin--Tate space, and stable homotopy theory*, 主定理及其同源提升判据，和 André, *Period mappings and differential equations*, II, Lemmas 6.1.3,6.2.5，给标记晶体的水平平凡化及等变性。与原 $A,B$ 的相认由所选同一初值和水平解唯一性给出。

令 $y_*$ 为线 $i_0$ 的真实目标参数。则
\[
 v_p(y_*)=1/d,\qquad \mathfrak c=y_*^d,\quad v_p(\mathfrak c)=1,\qquad
 y_i=[L(v_i)^{p-1}]\,y_* .                                  \tag{P8}
\]
此处 $L$ 是源 $E_1[p]$ 的一维 $\mathbf F_{p^2}$ 结构所给的线性坐标，选取使 $L(v_{i_0})=1$；有限 $j$ 对应 $\langle(\tau+Mj)/p\rangle$，所以可将第一坐标基乘 $M$ 来使用(P1)的 $v_j$。证明角标：源 canonical 形式群的 $\mu_{p^2-1}$ 作用将商 $H$ 送至 $aH$；在特殊纤维标记后，目标作用由 $\mathrm{Fr}\,a\,\mathrm{Fr}^{-1}=\bar a$ 给出。目标的 $\kappa$ 是两嵌入之商，所以角标是 $a^{p-1}$ 或其逆。后一情形用 $L^p$ 作为 $L$ 即得(P8)。该论证在带标记形式群形变范畴进行，故只用素于 $p$ 标记来确定目标所在的盘。

为核实径向估值，canonical 源的形式群是未分歧二次域的 Lubin--Tate 群，非零 $p$ 挠点参数赋值 $1/(p^2-1)$。次数 $p$ 的商同源用其核的 Weierstrass 乘积给 $v_p(a_i)=1/d$。目标 $p$ 挠点中有 $p-1$ 个为不在核内的源 $p$ 挠点的像，其赋值为 $p/(p^2-1)$（乘积的每一项均为 $1/(p^2-1)$）。其余 $p^2-p$ 个来自 $[p]$ 像在非零核中的点，源赋值 $1/(p^2(p^2-1))$，商同源像赋值 $1/(p(p^2-1))$。故目标 $[p](T)$ 的 Newton 顶点 $(p,1/d)$，$T^p$ 系数有准确赋值 $1/d$。该系数模 $p$ 是 Hasse 乘整单位；(F6)的原 Hasse 在 $t=0$ 简单零。于是 $v_p(t_i)=1/d$，因 $y/t$ 为整单位也得(P8)。由(P7)和 $v_p(a_i)=1/d$ 有 $\mathcal B(\mathfrak c)$ 为单位。各目标参数因(P8)和 $y_*\ne0$ 互异；Wronskian 使 $\zeta'(y_i)\ne0$。

### 47.3 半权相对计号的唯一性

将(P7)的共同标量去掉。在 $Z=0$ 的分支，每个 $W_{g,i}$ 再除去同一个 $\sqrt{y_*\mathcal B(\mathfrak c)}$ 后，为 $\pm [L(v_i)]^h\,\widetilde g(y_i)$。$\widetilde g(y_i)\equiv1$ 模极大理想，故所有这些剩余值的平方为 $L(v_i)^{p-1}$。由(P2)且 $v_p(\mathfrak G)=1/2$，整个剩余向量属于 $\ker\bar C$。按§46.1它是某个齐次 $h$ 次 $P$ 在 $v_i$ 的评值。$P^2-L^{2h}$ 的次数 $2h=p-1$ 小于 $p+1$，而它在所有这些射影线上消失，故此多项式恒零，$P=\pm L^h$。奇特征保证在每条线上模极大理想的计号已唯一固定原来的 $\pm1$。所以只剩一个共同计号。混合乘积的准确等式说明同一支的 $f/g$ 恰等于 $\widetilde f/\widetilde g$，故两个原 theta 共用所确定的整套符号。近 $Z=0$ 各支的平方根通过该初值唯一延拓。

## 48. 两个指定 tame 分量的全部变形 jets 和原共同分子的三位径向式

令 $y(Z)$ 是(P7)在 $y_*$ 的逆支。写 $\ell_i=[L(v_i)^{p-1}]$。由(P5)的准确特征，另各支为 $y_i(Z)=\ell_i y(\ell_i Z)$。对 $0\le n<d$ 定义原整块
\[
 F_n(z)=\sum_{j\ge0}c_{n+jd} z^j,\qquad
 Q_n(Z)=y(Z)^n \left(\frac{y(Z)}{y_*}\right)^{1/2}
        \mathcal B(y(Z)^d)^{1/2}F_n(y(Z)^d).
\]
两个根在 $Z=0$ 取共同参考支。将(P7)的共同源因子去掉，以 $i=B^ki_0$ 编号。若 $B^kv_{i_0}=s_k v_i$，则 $[L(v_i)]^h=\xi^k\chi(s_k)$。因此 $W_{f,i}(Z)$ 准确是同一全支公共因子乘
\[
 \chi(s_k)\xi^k\sum_{n=0}^{d-1}\xi^{2nk} Q_n(\xi^{2k}Z).
\]
对 $Z^j$ 取系数，再用(P3)得全部真等式
\[
 [Z^j]Q_{n+N}
   ={b_{-2(n+j)-1}\over \epsilon\sigma\mathfrak G}
                    [Z^j]Q_n,\qquad 0\le n<N,\quad j\ge0 .
 \tag{P9}
\]
它们在移去公共源因子后取系数，该操作保持(P2)。此处 $\epsilon=1$，仍保留符号位置便于核对。尤其
\[
 F_N(\mathfrak c)=u_0 F_0(\mathfrak c),\qquad
 u_j={b_{-2j-1}\over\epsilon\sigma\mathfrak G\, y_*^N}
 \quad (0\le j\le2).
\]
$u_0,u_1,u_2$ 均为单位，且 $u_j/u_0=b_{d-1}/b_{d-2j-1}$。由(P4)分别为
\[
 u_1/u_0\equiv2,\qquad u_2/u_0\equiv8/3\pmod p .           \tag{P10}
\]
这些比来自非分歧环。$u_0$ 也可在完备非分歧扩域中取值：角标全轨道使 $\mathfrak c$ 被足够大的非分歧地基的惯性固定（准典范商遍历同一个驯轨道，$y$ 的系数取在该地基）；$(\mathfrak G y_*^N)^2=\sigma p\mathfrak c$，其除 $p^2$ 后开整单位平方根仅需非分歧扩域。以下亦可在共同有界值扩域作所指 $p^j$ 整除。

为支付径向微分的精度，置 $x=y^d/\mathfrak c$。有 Tate 代数的系数同余
\[
 \mathcal A(\mathfrak c x)\equiv1-x,\qquad
 \mathcal B(\mathfrak c x)\equiv1\pmod p.                    \tag{P11}
\]
确实(G6)在 $w$ 的 $k$ 次系数的每层 $p^b$ 估值贡献至少 $-1$：两个上参的命中次数各至少 $\lfloor k/p^b\rfloor$，一个下参至多多一次，另一分母是 $k!$。分母里正整数至多 $3k+1$，故在 $t^i,\ i=3k$，下界为 $-\lfloor\log_p(i+1)\rfloor$，亦适用于 $A$ 与 $B/t$。整旋转换元、整单位乘法保留该弱下界。$B/t$ 直到 $t^d$ 均整，因其第一可能 $p$ 分母须 $3k\ge2p-1$，故 $\mathcal B$ 在 $y^d$ 处也整。尺度 $\mathfrak c$ 后每个径向次数 $j\ge2$ 的估值至少 $j-\lfloor\log_p(jd+1)\rfloor\ge1$，且趋于无穷。$\mathcal A(\mathfrak c)=0$ 决定所余一次系数模 $p$ 是 $-1$。由此(P11)可逐次微分。

在 $x=1$ 取值，$Z=y_*^{-1}x^{-1/d}\mathcal A(\mathfrak c x)/\mathcal B(\mathfrak c x)$，故
\[
 {x_{ZZ}\over x_Z^2}=-{Z_{xx}\over Z_x}\equiv2/d\equiv2\pmod p .
\]
$Z_x$ 只在同一比中相消。写 $\kappa_n=(n+1/2)/d$；除去 $y_*^n$ 后各 $Q_n$ 为 $x^{\kappa_n}\mathcal B(\mathfrak cx)^{1/2}F_n(\mathfrak cx)$。一、二阶 $Z$ 微分在对等式两边分别除共同 $x_Z,x_Z^2$ 后成为 $\partial_x$ 和 $\partial_x^2+(x_{ZZ}/x_Z^2)\partial_x$。根的共同单位另可约掉。按(P11)在模 $p$ 的系数行，这两行分别为
\[
 D_1^{(n)}=\kappa_n F+\mathfrak c F',\qquad
 D_2^{(n)}=\kappa_n(\kappa_n+1)F+
       (2\kappa_n+2)\mathfrak c F'+\mathfrak c^2F'',         \tag{P12}
\]
其中 $F,F',F''$ 是 $F_n$ 在 $\mathfrak c$ 的普通导数值。第零行为 $F$；$\kappa_0\equiv1/2,\ \kappa_N\equiv1$。未约化的三行为整三角矩阵，对角均为一（变量取 $F,\mathfrak c F',\mathfrak c^2 F''$，并除共同 $\mathcal B^{1/2}$）。(P9)把 $N$ 块第 $j$ 行精确表为 $u_j$ 乘零块第 $j$ 行。

先因 $c_0=0$，零块前三个变量至少在 $p$，$N$ 块同样如此。模 $p^2$ 只需零、一行，$F_N(0)=F_N(\mathfrak c)-\mathfrak c F_N'(\mathfrak c)\bmod p^2$。由(P10),(P12)即得
\[
 E_N\equiv-u_0\mathfrak c E_d\pmod{p^2}.                    \tag{P13}
\]
现在假设原 $g_1\in p$。(128)给 $c_d=E_d\in p$，故 $F_0(\mathfrak c),\mathfrak c F_0'(\mathfrak c),\mathfrak c^2 F_0''(\mathfrak c)$ **全都在 $p^2$**，由上述三角性 $N$ 块亦然。在 $p^3$ 精度于是可使用(P10)--(P12)的全部模 $p$ 系数。整 Taylor 回 $x=0$ 给 $F_N(0)=F_N-\mathfrak c F_N'+\mathfrak c^2 F_N''/2\bmod p^3$，这在 $N$ 块等于 $3F_N-3D_1^{(N)}+D_2^{(N)}/2$。代入零块并保留全部三项，成为
\[
 u_0\{F_0-2\mathfrak c F_0'+\tfrac43\mathfrak c^2 F_0''\}
 \equiv-u_0\mathfrak c c_d-\tfrac13u_0\mathfrak c^2 c_{2d}
 \pmod{p^3}.
\]
由(P6)，所得同一物理行是
\[
 \boxed{E_N\equiv-u_0\mathfrak c E_d
                  -\tfrac13u_0\mathfrak c^2 c_{2d}\pmod{p^3}
 \qquad(g_1\in p).}                                         \tag{P14}
\]
$\mathfrak c/p$ 为单位。特别(N5)两个核的实际共同第二位满足
\[
 {\mathcal U_1(\Xi_{k,p})\over p^2}\equiv
 -\left(\mathsf b_p+k\gamma\mathsf a_p u_0{\mathfrak c\over p}\right)
       {E_d\over p}
 -{k\gamma\mathsf a_p u_0\over3}
       \left({\mathfrak c\over p}\right)^2 c_{2d}\pmod p,\quad k=1,2 .
 \tag{P15}
\]
这里 $c_{2d}$ 仍须用同一实际旋转框架和同一 $f$ 的整 Taylor 系数。$k=2$ 的行乘 $\gamma^{-2}$ 才是原 $j_1/p^2$。$k=1$ 保(G4)的另一符号。本推导未推断(P15)对无穷 $p$ 非零；$c_3$ 的非零在另一个 tame 分量，不替代 $c_{2d}$ 或 $E_d/p$。

一手文献入口：Strömberg 的判别模公式 [Lemma 5.12](https://arxiv.org/pdf/1108.0202)，Gross--Hopkins 的[原文](https://arxiv.org/pdf/math/9401220)，以及 André 的[晶体周期原文](https://arxiv.org/pdf/math/0203194)。本节所有有限矩阵、符号唯一性及三位系数由所示恒等式手证。


在原 g1 属于 p 的范围，(P14) 所用 c2d 模 p 亦不依所许的整旋转框架选择。若 $y'=y(1+a y^d+\cdots)$、新框架为原框架乘 $(1+b y^d+\cdots)$，则 $c_0=0$ 给 $c'_{2d}=c_{2d}-(da+b/2)c_d$。因 $c_d=E_d$ 属于 p，所指残值不变；物理整组合仍以(N5)及(P15)为定义。

## 49. 同一参考消去径向单位和原第四个物理权

仍取(P1)的无穷算术子列，$c_\sigma=[z^d]\log(\sigma(z)/z)$，$\gamma=34pc_\sigma$。为免与旋转系数混淆，写
\[
 \kappa=p[t^d]A\bmod p,\qquad
 E^{(g)}_r=[v^r]\sqrt A\,g,\qquad
 E^{(f)}_r=[v^r]\sqrt A\,f ,
\]
其中 $t=t(v)$。$E^{(f)}_N,E^{(f)}_d$ 正是 $E_N,E_d$，另记 $E^{(f)}_{2d}=E_{2d}$。以下不要求对任何局部 Jacobi 和选择额外首单位。

### 49.1 原 degree-two 参考读出三个规范常数

在(P5)置 $A_1=[y^d]\widetilde A,\ B_1=[y^d](\widetilde B/y)$。因 $A$ 在 $d$ 以前整，且 $y/t$、$l$ 都是常数一的整单位，$pA_1\equiv\kappa\bmod p$；由(G6)在 $d$ 处 $B_1$ 整。(P11)给
\[
 \mathfrak c/p\equiv-1/\kappa\pmod p .
 \tag{Q1}
\]
(P9)同样适用于原 $g$，且(P1)两来源的 $\epsilon$ 相同。$\widetilde g(0)=1$，$N<d$，故
\[
 u_0\equiv E^{(g)}_N=[y^N]\widetilde g\pmod p .
 \tag{Q2}
\]
原 degree-two theta 的热标度是 $4$。若 $\beta_i=[z^i](x\sigma^2)$，同(120),(123)有准确公式
\[
 E^{(g)}_r={(2r)!\over 4^r r!}\beta_{2r}.
\]
R614 的整窗口同样适用于此参考：$x z^2$ 在所需范围整，$\sigma/z$ 去掉原 Gaussian 后整，故其乘积在 $z^{2d}$ 以内整。写回 $\exp(2c_\sigma z^d)$，得到 $p\beta_d\equiv 2pc_\sigma$、$p^2\beta_{2d}\equiv(2pc_\sigma)^2/2\bmod p$。因此
\[
 u_0\equiv{(d!/p)(2pc_\sigma)\over4^N N!}\pmod p .
 \tag{Q3}
\]
有常数一时，(P6)在次数 $d$ 要增加 $A_1/2$：$v/y-1$ 从 $d$ 阶起，常数一自身的换元没有修正，而 $\sqrt{\widetilde A}$ 对常数一贡献 $A_1/2$。所以 $E_d^{(g)}=[y^d]\widetilde g+A_1/2$。另一面直接分块阶乘得
\[
 {(2d)!\over p\,d!}\equiv-4\pmod p
\]
（$p+2,\ldots,2p-1$ 模 $p$ 的乘积为 $-1$，$2p$ 给 $2$，$2p+1,2p+2$ 给 $2$）。故
\[
 {\kappa\over2}\equiv p E_d^{(g)}
 \equiv {-4\over4^d}\,{(2pc_\sigma)^2\over2}
 \equiv-{(pc_\sigma)^2\over2}\pmod p .
\]
于是 $\kappa=-(pc_\sigma)^2$ 是单位。从(127)还有
\[
 \mathsf b_p\equiv-68^2/4,\qquad
 \mathsf a_p u_0\equiv 17^N(2pc_\sigma),\qquad
 17^N\equiv17\chi(17)=17 .
\]
逐项代入(Q1)得到
\[
 \boxed{\quad \gamma\mathsf a_pu_0\,\mathfrak c/p
                 \equiv-\mathsf b_p\pmod p .\quad}            \tag{Q4}
\]
上述等式只约了原共同分子中实际乘 $p^2$ 的单位，未以近似值替代分子合成前的全部阶乘。

### 49.2 两位整组合与第四物理权

当原 $g_1\in p$，(P15)化成
\[
 {\mathcal U_1(\Xi_{k,p})\over p^2}
 \equiv(k-1)\mathsf b_p E_d/p
       -{k\mathsf b_p\over3\kappa}\,c_{2d}\pmod p.            \tag{Q5}
\]
(P5)也从该整系数回到物理热行。仅 $0\bmod d$ 分量参与 $[v^{2d}]$，且 $c_0=0$。用
\[
 y=v\{1+(A_1-B_1)v^d+O(v^{2d})\},
 \qquad \sqrt{\widetilde A}=1+(A_1/2)y^d+O(y^{2d})
\]
准确得到
\[
 E_{2d}=c_{2d}+\{(d+1/2)A_1-dB_1\}c_d
       ={(4d)!\over68^{2d}(2d)!}\alpha_{4d}.
\]
$E_d=c_d\in p$，从而 $E_{2d}$ 整，且
\[
 c_{2d}\equiv E_{2d}-\tfrac32\kappa E_d/p\pmod p .
\]
(130),(G4)的两个原行最终为
\[
 \boxed{\begin{aligned}
 j_1/p^2&\equiv {2\mathsf b_p\over\gamma^2}
             \left({E_d\over p}-{E_{2d}\over3\kappa}\right),\\
 j_2/p^2&\equiv {\mathsf b_p\over\gamma^2}
             \left({E_{2d}\over3\kappa}-{E_d\over2p}\right)
                       \pmod p .
 \end{aligned}}                                               \tag{Q6}
\]
因此该无穷子列上，真正 $j_1=0$ 要求 $E_d\in p$ 且
$E_{2d}\equiv3\kappa E_d/p\bmod p$，三个常数均已用固定原参考读定。
$E_{2d}$ 是 $4d$ 物理权，不能把它与 $2d$ 物理权 $E_d$ 混同。
完整 Gaussian Newton 也在这两个物理权中包含同样两位，故(Q6)不是额外独立坏条件；(P9)给出的则是原两个模函数在全部 $Z$ 变形阶的实际对应。仍需证明原第一种或第二种 canonical 单位在无穷个 $p$ 出现，或用更深 $J'(0)$ 证书。

## 50. $p\equiv137\bmod204$ 上的原 $\sqrt{-17}$ 普通子列

本节仍用原 $f,g,\widetilde P$、三乘积、物理热尺度 $68,4$ 及(127)的共同分子，保留§§29--45原固定水平覆盖和其各个已选择的局部支。另取
\[
 p\equiv137\bmod204,\quad M=68,\quad d=p+1,\quad N=d/2,\quad h=N-1.
\]
$137$ 与 $204$ 互素，故删去先前固定的有限坏集后仍有无穷个这种素数。此时 $p\equiv-1\bmod3$、$p\equiv1\bmod68$、$p\equiv5\bmod12$，所以物理 $j=0$ 仍超奇异，而 $\chi(-17)=1$，此即§31的 $K'=\mathbf Q(\sqrt{-17})$ 分裂子列。

辅助传输的 level $68$ 足以确定(P1)两个未平方 theta 的共同支。证明只用 $\Theta_f^2,\Theta_f\Theta_g,\Theta_g^2$ 的整权一双格下降。三种双格的判别模都是 even signature，level 整除 $68$，Strömberg Lemma 5.12 的 $\Gamma(68)$ 作用为恒等；固定冻结系数照旧。局部 $\widetilde g(0)=1$ 和(P2)校准所有平方根。故在此选择 $\tau_j=(\tau+68j)/p$，并不缩小原定义 $f,g$ 或固定权三 $\Phi_{f,g}$ 所在的覆盖。

有限相位分别为 $\zeta_p^{jx^2}$、$\zeta_p^{17jy^2}$。$p^{-1}a=a\bmod34$，参考的二标记同样固定。由 $\chi(17)=(p/17)=1$，得到
\[
 \epsilon_f=\epsilon_g=1,\qquad \sigma=\chi(-1)=1,\qquad
 W_\infty=\mathfrak G F(p\tau),\qquad \mathfrak G^2=p .
\]
于是用同一 $v_j,v_\infty,C$ 有 $CW=\mathfrak G W,\ C^2=pI$。有限和无限分支所运的 full level 矩阵现在都是单位，因为 $D_f=\operatorname{diag}(1,p)$、$D_\infty=\operatorname{diag}(p,1)$ 在模 $68$ 全为 $I$。选源 $M$-标记为指定原目标标记在相对 Frobenius 下的唯一逆像。这次无限同源按原复格取 $z\mapsto pz$，其微分因子为 $+p\lambda_\infty/\lambda_s$，正是 $\mathfrak G^2\lambda_\infty/\lambda_s$。相同的 $\epsilon_f\epsilon_g=1$ 同时给混合平方。因此全部带标记商都有同一特殊 Frobenius，不出现逐支未识别的 level 或相位。Reed--Solomon 核、$g(0)=1$ 和 $P^2-L^{2h}$ 的零数论证原样固定共同计号。

(P3)在此为 $b_rb_{r+d}=p$，(P4)仍给准确半数单位与半数一位 $p$。$\sigma$ 的改变已在
\[
 u_j=b_{-2j-1}/(\epsilon\sigma\mathfrak G y_*^N)
      =b_{-2j-1}/(\mathfrak G y_*^N)
\]
中保留；所用 $u_j/u_0$ 不变。(P5)--(P8)只用原 CM 域在 $p$ 的未分歧二次性、其 canonical lift 和原 Hasse 简单零，故整旋转框架、估值 $v_p(\mathfrak c)=1$、$c_N=E_N,c_d=E_d$ 均成立。在(G6)的估值核验本子列取 $e=5$，$B/t$ 在 $t^d$ 范围同样整。由此前的全变形证明，(P9)、(P13)--(P15)对这个 $\sigma=1$ 的实际 $u_0$ 全部成立。最后 $17^N\equiv17$，所以同一参考证明仍给
\[
 \kappa=p[t^d]A\equiv-(pc_\sigma)^2,\qquad
 \mathfrak c/p\equiv-1/\kappa,\qquad
 \gamma\mathsf a_pu_0\,\mathfrak c/p\equiv-\mathsf b_p\pmod p .
\]
特别当 $g_1\in p$，本子列也准确有
\[
 {j_1\over p^2}\equiv{2\mathsf b_p\over\gamma^2}
 \left({E_d\over p}-{E_{2d}\over3\kappa}\right),\qquad
 {j_2\over p^2}\equiv{\mathsf b_p\over\gamma^2}
 \left({E_{2d}\over3\kappa}-{E_d\over2p}\right)\pmod p,
 \qquad E_{2d}={(4d)!\over68^{2d}(2d)!}\alpha_{4d}.
\]
这里的 $K'$ 分裂性规定哪些原 harmonic 格点展开可以进一步使用；它本身没有推出这个中央差非零。

## 51. 全部变形阶的径向首剩余和实际无约束范围

用§§46--50任一条原子列，保留同一两块 $F_0(z),F_N(z)$。本节在一个共同的 $p$ 进整除阶同时读取(P9)的所有 $Z$ 阶。只谈已指明的共同首剩余；下一位可以携带此前落入 $\ker\bar C$ 的信息。

改用 $S=y_*Z,\ X=y/y_*,\ x=X^d$。取全部真逆支 $X_i(S)$，$X_i(0)=\ell_i$。由(P5),(P11)，每支在 $S=0$ 的缩放逆为整幂级数，且其约化满足
\[
 X_i^{p+1}+S X_i-1=0,\qquad X_i(0)=L(v_i)^{p-1}.
 \tag{R1}
\]
这里的整逆来自 $S=X^{-1}\mathcal A(\mathfrak c X^d)/\mathcal B(\mathfrak c X^d)$ 在各单位根处的单位导数。模 $p$ 的加法方程
\[
 Y^{p^2}+S Y^p-Y=0
\]
在 $S=0$ 各 $L(v_i)$ 处导数为 $-1$。故有唯一提升 $Y_i(S)$，$Y_i^{p-1}=X_i$。唯一性和方程的可加性使 $Y_i=Y(v_i)$、$Z_i=Y_i^p=Z(v_i)$ 都是 $v_i$ 的 $\mathbf F_p$ 线性形式（系数在剩余域的幂级数环）。此处 $Z_i$ 是线性形式，不再表示(P7)的参数。令 $D=Y(e_1)Z(e_2)-Z(e_1)Y(e_2)$，则 $D(0)\ne0$，且 $D^p=-D$，由此 $D=D(0)$ 恒定。§47的整套平方根在约化中恰给 $Y_i^h$。

设径向块 $F_0(\mathfrak c x),F_N(\mathfrak c x)$ 在有界闭 $x$ 盘同被 $p^r$ 整除，写
\[
 P(x)=p^{-r}F_0(\mathfrak c x)\bmod p,\qquad
 G(x)=p^{-r}F_N(\mathfrak c x)\bmod p .
\]
原 $c_i$ 整且 $v_p(\mathfrak c)=1$，两者是度至多 $r$ 的多项式。允许有一条剩余为零。为得到所有 $S$ 阶的条件，将(P9)恢复到整向量：令 $a_i$ 为§48关于 $Q_0$ 的带角项，$b_i$ 为关于 $Q_N$ 的带角项再除 $y_*^N$，公共因子照旧去掉。因(P3)，对每个系数的两对角位置同时有
\[
 C b=\eta a,\qquad C a=(\sigma p/\eta)b,\qquad
 \eta=\epsilon\sigma\mathfrak G/y_*^N\in\mathcal O^\times .
\]
这里的 $C$ 是固定 $p$ 的 Paley 矩阵，$a,b$ 已写成参数 $S$。约去共同的 $p^r$ 后，(P11)及确定的计号给
\[
 \bar a_i=Y_i^h P(X_i^d),\qquad
 \bar b_i=Y_i^h X_i^N G(X_i^d)=\frac{Z_i^N}{Y_i}G(1-SX_i).
 \tag{R2}
\]
特别在此共同剩余阶，全部 $S$ 系数都必须满足 $\bar C\bar b=\bar\eta\,\bar a,\ \bar C\bar a=0$；第二式也随第一式成立。下文解的是这两条准确剩余方程。

对 $1\le m\le2d-2$，(R1)全部根的幂和只有 $m=d$ 时非零，其值为 $1$。确实 $m<d-1$ 时由 Newton 恒等式为零，$m=d-1$ 时可能的系数是 $-(d-1)S=-pS=0$，$m=d$ 时为 $d=1$；更高至 $2d-2$ 用同一递推。计算(R2)的第 $i$ 行，
\[
 (\bar C\bar b)_i
 =D^{-h}Y_i^h\sum_j X_j^{N+1}(X_j-X_i)^h G(1-SX_j).
\]
其中 $Y_j^{h+N-1}=Y_j^{p-1}=X_j$，这给额外一次 $X_j$。若 $\deg G\le d-2$，所求各幂次数不超过 $d+\deg G\le2d-2$，只有 $d$ 次留下。置 $g_a=[T^a]G(1-T)$，有
\[
 (\bar C\bar b)_i=D^{-h}Y_i^h
        \sum_{a=0}^h(-1)^a\binom ha g_a(SX_i)^a .
\]
在 $S=0,G=1$ 对应 $e(d-1)$ 的第 $i_0$ 行给 $D^{-h}=\bar b_{d-1}$，而 $\eta=b_{d-1}u_0$。因 $SX_i$ 非恒定，故全部变形阶的共同首剩余准确等价于多项式身份
\[
 \boxed{\ P(1-T)=\bar u_0^{-1}
          \sum_{a=0}^h(-1)^a\binom ha [T^a]G(1-T)\,T^a.\ }   \tag{R3}
\]
这给次数 $\le h$ 的真正同构；若 $P=x^k,\ 0\le k\le h$，其唯一同次数解为
\[
 G=\bar u_0\sum_{a=0}^k\frac{\binom ka}{\binom ha}(1-x)^a.
\]
若 $h<r\le d-2$，(R3)的像是次数 $\le h$ 的全部多项式，核为 $(1-x)^{h+1}$ 的按 $r$ 次截取的倍数。故仅在径向首剩余的这个范围内，第一个核出现在 $h+1$ 次。

对原 canonical 坏 $j_1=0$，有 $g_1\in p,\ E_d\in p$。$P$ 块在闭盘整除 $p^2$。$N$ 块也在闭盘整除 $p^2$：$c_N=E_N\in p^2$，而 $F_N(\mathfrak c)=u_0F_0(\mathfrak c)\in p^2$ 进一步给 $c_{N+d}\in p$。取 $r=2$，记 $B=(\mathfrak c/p)^2 c_{2d}\bmod p$，由(Q5)的 $k=2$ 及(Q1)得
\[
 P(x)=B\,x(x-2/3),\qquad
 G(x)=\frac{\bar u_0 B}{3}(8x^2-8x+1).
 \tag{R4}
\]
后一式可直接用(R3)的 $k=1,2$ 核算。若 $B\ne0$，(Q5)也给 $j_2/p^2\ne0$。因此全部 $S$ 阶的这个共同首剩余确实容许非零的(R4)；缺口不能通过对同一首剩余再增加任意多的 $Z$ 阶解决。这不构造 $j_1=0$ 的原素数，也不为任意多项式解宣称存在实际特征零模形式提升。若利用下一位 $\sigma p/\eta$ 或更深几何约束，仍须保留其整提升和原水平质量。

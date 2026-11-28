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

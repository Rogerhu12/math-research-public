# R150：空谱锚、矩形次数点态多项式与任意指数权

主会话已全文核验；完整ISP仍未解决。研究原稿见[原稿](../notes/2026-11-12-empty-spectrum-anchor-rectangular-polynomial-cyclicity-0c.md)。


日期：2026-11-12（UTC）。作者：Astra-ISP-0c017065。预留 R150。

状态：以下定理及全部实际定义域步骤已给出完整证明。
使用 R125、R128、R134、R140、R144、R145 和 R147；
没有给任意高阶符号假设一个尚未构造的最大闭乘子。

## 1. 主定理

设
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
v=b_*+\sum_{j\ge0}b_j\chi_j,\qquad
w=c_*+\sum_{j\ge0}c_j\chi_j,
$$
三个系数列均属于 $\ell^2$。设 $u,v$ 均非常数，并记
$$
j_u=\min\{j:a_j\ne0\},\quad j_v=\min\{j:b_j\ne0\},\qquad
h_u=2^{j_u},\quad h=2^{j_v},\quad b=b_{j_v}\ne0.
$$
假设：

1. 第一阶闭乘子 $X=X_u$ 为空谱；
2. $h\le h_u$；
3. $F(U,V)\in\mathbb C[U,V]$ 的两个分别次数是 $p\ge1,m\ge1$，
   而角系数 $[U^pV^m]F$ 非零；
4. 令 $r(V)=[U^p]F(U,V)$，则 $\deg r=m$ 且
   $$
   \boxed{\gcd(r(V),r(V-2b))=1.}
   \tag{1.1}
   $$

**定理1.1。** 点态向量
$$
\boxed{F(u,v)e^w}
\tag{1.2}
$$
对实际 $A$ 循环。它属于 $H$，并且自动非零。
进一步，对每个 $\lambda\in\mathbb C$，
$$
\boxed{(F(u,v)-\lambda)e^w\ \text{循环}.}
\tag{1.3}
$$
指数在括号外；没有将它误写成 $F(u,v)e^w-\lambda$ 的无条件结论。
取 $w=0$ 后，全部 $F(u,v)-\lambda$ 均循环。

第一条有明确系数判据：R134/R138 证明，
$a\notin\ell^1$ 且存在 $\theta$ 使
$$
\sum_j\bigl(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\bigr)<\infty
$$
即保证空谱。允许常数项 $a_*$，以及任意重叠的 $a,b,c$ 支撑。

**推论1.2。** 任取 $\rho\in\mathbb C$、$p,m\ge1$，以及
$\deg s_i\le m$ 的任意 $s_0,\ldots,s_{p-1}$，则
$$
\boxed{
\left[u^p(v-\rho)^m+\sum_{i=0}^{p-1}u^i s_i(v)\right]e^w
\ \text{循环}.
}
\tag{1.4}
$$
因为 $(V-\rho)^m$ 与 $(V-\rho-2b)^m$ 互素。
低 $u$ 次数的全部系数均可任意选择，无小范数条件。

## 2. 空谱逆生成的真实局部 Banach 代数

记 $R=X^{-1}$。R134 已证明它是有界、单射、值域稠密且拟幂零的实际交换子：
$$
R\in\{A\}',\qquad r(R)=0.
\tag{2.1}
$$
不需要、也不声称 $R\in\mathcal A$。令
$$
\mathcal A_h=\overline{\mathbb C[I,A^h]}^{\|\cdot\|},\qquad
\mathcal B=\overline{\operatorname{alg}(\mathcal A_h,R)}^{\|\cdot\|}.
\tag{2.2}
$$
全部生成元属于交换的 $\{A\}'$，故 $\mathcal B$ 是实际有界交换
Banach 代数。它只有一个字符 $\chi_{\mathcal B}$：
任何字符限制到 $\mathcal A_h$ 必为唯一的常数字符，而
$$
|\varphi(R)|\le\lim_n\|R^n\|^{1/n}=0.
$$
这些值在生成元及其范数闭包上唯一决定字符；
存在性由复交换含幺 Banach 代数的极大理想定理给出。
因此
$$
\chi_{\mathcal B}(R)=0,\qquad
T\in\mathcal B,\ \chi_{\mathcal B}(T)\ne0
\ \Longrightarrow\ T\in\mathcal B^\times.
\tag{2.3}
$$

固定 dyadic $\zeta$，写 $\gamma=\gamma_\zeta$。
R125 的真实同域恒等式为
$$
\gamma X=X+D_u,\qquad D_u=A^{h_u}D_{u,0},
\tag{2.4}
$$
其中 $D_u$ 为真正解析芽在 $A$ 上的值。
因为 $h\le h_u$，也有真实有界商
$$
D_u=A^hD_{u,h},\qquad D_{u,h}\in\mathcal A_h.
\tag{2.5}
$$
在 $\operatorname{Ran}R\subseteq\operatorname{Dom}X$ 上先算
$(X+D_u)R=I+D_uR$。右端为实际有界单位，因为 $D_uR$ 拟幂零。
实际闭逆的唯一性给
$$
\boxed{
\gamma R=R(I+D_uR)^{-1}\in\mathcal B,\qquad
\gamma R-R=-\gamma R\,D_uR.
}
\tag{2.6}
$$
$\gamma R$ 亦因酉共轭而拟幂零。因此 $\gamma$ 保持 $\mathcal B$，
且 $\chi_{\mathcal B}\circ\gamma=\chi_{\mathcal B}$。

R139 对每个 $C\in\mathcal A_h$ 给真实有界除法
$$
\gamma C-C=A^h C_\zeta,\qquad C_\zeta\in\mathcal A_h.
\tag{2.7}
$$
结合 (2.5)—(2.6)，
$$
\frac{\gamma R-R}{A^h}:=-\gamma R D_{u,h}R\in\mathcal B,\qquad
\chi_{\mathcal B}\!\left(\frac{\gamma R-R}{A^h}\right)=0.
\tag{2.8}
$$
左侧只是已明确写出的真实因式的简称，绝非预设一般有界除法。

### 2.1 本文使用的有限代数运算

若
$$
E=\sum_{k=1}^N R^k C_k,\qquad C_k\in\mathcal A_h,
\tag{2.9}
$$
有限望远镜和 (2.7)—(2.8) 给
$$
\gamma E-E=A^h E_\zeta,\qquad
E_\zeta\in\mathcal B,\quad\chi_{\mathcal B}(E_\zeta)=0.
\tag{2.10}
$$
每个项或者剩下 $R$ 或 $\gamma R$ 正幂，或者出现 (2.8)；
因此差商的字符确实为零。

若 $U=cI+E$、$c\ne0$、$E$ 如 (2.9)，则 $U$ 可逆，且
$$
U^{-1}-c^{-1}I=-c^{-1}EU^{-1},
\tag{2.11}
$$
$$
\gamma(U^{-1})-U^{-1}
=-(\gamma U)^{-1}(\gamma U-U)U^{-1}.
\tag{2.12}
$$
(2.12) 同样有真实 $A^h$ 因子，差商字符为零。
将 (2.9) 的表达式乘以这些指定单位的逆，仍保留所需的
零字符差商性质。

这里只使用有限多次乘加及明确的单位逆。
没有声称在 $\mathcal B$ 任意范数极限上，
未经控制的“除 $A^h$”操作自动连续。

## 3. 倾斜双模式 Bell 系数及循环基向量

沿用 R145/R147 的实际局部函数
$$
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z).
$$
对三模式 $(u,v,w)$，R145 给范数整的有界单位
$$
\mathcal B_{\rm joint}(s,t,\tau)
=\prod_j H(sa_j+tb_j+\tau c_j,V_j).
\tag{3.1}
$$
令
$$
B_w=\mathcal B_{\rm joint}(0,0,1),\qquad
\mathcal V_w=B_w^{-1}e^w.
\tag{3.2}
$$
R16 给 $e^w$ 循环，$B_w$ 为有界交换单位，所以
$$
\boxed{\mathcal V_w\ \text{循环}.}
\tag{3.3}
$$
R145 的整真空轨道还保证 $\mathcal V_w$ 属于
$X=X_u$、$Y=X_v$ 的全部混合自然乘积域，
且在这个向量上所有次序给同一个混合导数。

定义倾斜双 Bell 函数
$$
\widetilde B(s,t)
=\mathcal B_{\rm joint}(s,t,1)B_w^{-1},\qquad
C_{k\ell}=\partial_s^k\partial_t^\ell\widetilde B(0,0).
\tag{3.4}
$$
其有限乘积是
$$
\prod_j H(sa_j+tb_j+c_j,V_j)H(c_j,V_j)^{-1}.
\tag{3.5}
$$
对所有 $j<j_v$，有 $b_j=a_j=0$，该因子精确为 $I$。
其他局部因子属于 $\mathcal A_h$；范数整极限及 Cauchy 微分给
$$
\boxed{
C_{k\ell}\in\mathcal A_h,\quad C_{00}=I,\quad
\chi(C_{k\ell})=0\ (k+\ell>0).
}
\tag{3.6}
$$
这是由真实低位因子取消得到的尾代数归属，不是形式首阶猜测。

对任意标量多项式 $F$，混合域网格与整恒等式求导给
$$
\boxed{
F(u,v)e^w
=B_w\sum_{k,\ell\ge0}\frac{C_{k\ell}}{k!\ell!}
(\partial_U^k\partial_V^\ell F)(X,Y)\mathcal V_w.
}
\tag{3.7}
$$
和式有限，所有自然混合词的实际定义域已由 R145 付清。
有界 $C_{k\ell}\in\{A\}'$ 保持相关域并与闭算子域交换。
左侧属于 $H$，也可直接由 Rademacher 次高斯矩和 Hölder 得到；
无需预设点态乘法在整个 $H$ 上有界。

## 4. 用空谱逆消去全部 $X$ 幂

将 (3.7) 的有限算子多项式按 $X$ 次数排序，其次数至多 $p$。
最高 $X^p$ 系数恰为
$$
P_r^w(Y),\qquad
P_r^w(z)=\sum_{\ell=0}^m\frac{C_{0\ell}}{\ell!}r^{(\ell)}(z).
\tag{4.1}
$$
任何 $\partial_U$ 正阶导数都会降低 $X$ 次数。
其余各 $X^i$ 系数是次数至多 $m$ 的 $Y$ 多项式，
全部有界系数在 $\mathcal A_h$。

对 $0\le i\le p$，混合自然域及真逆关系给
$$
R^pX^iY^j\mathcal V_w=R^{p-i}Y^j\mathcal V_w.
\tag{4.2}
$$
因此存在有限个 $\mathcal A_h$ 系数多项式 $D_k(z)$，
每个次数至多 $m$，使
$$
T(z)=P_r^w(z)+\sum_{k=1}^p R^kD_k(z)
\tag{4.3}
$$
满足
$$
\boxed{
T(Y)\mathcal V_w
=R^pB_w^{-1}\bigl[F(u,v)e^w\bigr].
}
\tag{4.4}
$$
$T(Y)$ 仅在自然 $m$ 次幂域上使用；没有将其宣称为全 $H$ 上有界。

记 $c_m=[V^m]r\ne0$。$T$ 的最高系数为
$$
U=c_mI+\sum_{k=1}^pR^k[D_k]_{z^m}\in\mathcal B^\times.
\tag{4.5}
$$
令
$$
P(z)=U^{-1}T(z)\in\mathcal B[z].
\tag{4.6}
$$
它为次数 $m$ 的首一多项式，且
$$
\chi_{\mathcal B}(P(z))=c_m^{-1}r(z).
\tag{4.7}
$$
由 (2.9)—(2.12)，可写
$$
P(z)=c_m^{-1}P_r^w(z)+E(z),
\tag{4.8}
$$
每个 $E$ 系数字符为零；更强地，每个系数的 gauge 差有真实
$A^h$ 因子，差商在 $\mathcal B$ 中的字符为零。
这是有限表达式 (4.3)、一个明确的单位逆 (4.5) 和 §2.1 的直接应用。

## 5. 首个 gauge 差保留完整的平移判据

记 $d=W_h$、$c=c_{j_v}$。R125 给
$$
\gamma Y=Y+D_v,\qquad D_v=A^hD_{v,h},
\tag{5.1}
$$
具有相同的全部自然幂域。对系数施加 $\gamma$，定义
$$
Q(z)=(\gamma P)(z+D_v).
\tag{5.2}
$$
它是实际 $\gamma(P(Y))$ 的算子多项式，仍首一、次数 $m$。

R147 的单模式倾斜 Bell 计算给
$$
(\gamma P_r^w)(z+D_v)-P_r^w(z)=A^hL_r^w(z),
\tag{5.3}
$$
$$
\chi_{\mathcal B}(L_r^w(z))
=e^{-2c}\frac{\zeta^h-1}{d}[r(z-2b)-r(z)].
\tag{5.4}
$$
$e^{-2c}$ 永不为零。其依据为最低位的实际公式
$$
c_h\widetilde B_v(t)
=\frac{e^{-2c}(e^{-2bt}-1)+2bt}{d}
$$
与 $\gamma Y-Y$ 的首系数逐项抵消，故允许 $r$ 的任意重根。

对 (4.8) 的误差，
$$
(\gamma E)(z+D_v)-E(z)
=[(\gamma E)-E](z)+
\sum_j(\gamma E_j)[(z+D_v)^j-z^j].
$$
第一部分由 §4 有真实 $A^h$ 因子且差商字符零；
第二部分由 (5.1) 提取 $A^h$ 后，
每项仍有字符零的 $\gamma E_j$ 因子。因此
$$
\boxed{Q(z)-P(z)=A^hL(z),\qquad L(z)\in\mathcal B[z],}
\tag{5.5}
$$
$$
\boxed{
\chi_{\mathcal B}(L(z))
=\frac{e^{-2c}(\zeta^h-1)}{c_m d}[r(z-2b)-r(z)].
}
\tag{5.6}
$$
因 $P,Q$ 均首一，$\deg L\le m-1$。
所有空谱逆新增项在真实差商后仍带零字符因子。

## 6. 有限自由模中的真实有界 Bézout 证书

取 $\zeta^h\ne1$。由 (1.1)、(4.7)、(5.6)，
$\chi_{\mathcal B}(P)$ 和 $\chi_{\mathcal B}(L)$ 互素。
因为 $P$ 首一，$\mathcal B[z]/(P)$ 为秩 $m$ 的自由模。
在基 $1,z,\ldots,z^{m-1}$ 上，乘 $L$ 的矩阵施加字符后可逆，
故行列式字符非零，是 $\mathcal B$ 中的实际有界单位。
伴随矩阵及带余除法给
$$
a(z)P(z)+b_0(z)L(z)=1,\qquad
a,b_0\in\mathcal B[z],\quad\deg b_0\le m-1.
\tag{6.1}
$$
结合 (5.5)，得到
$$
\boxed{A^h=(A^h a-b_0)P+b_0Q.}
\tag{6.2}
$$
$m=1$ 时也成立，$a$ 可取零。
这里没有用一般多变量互素推出 Bézout；
使用的是首一多项式的有限自由模及已核明的单位行列式。

## 7. 深正则化完成跨核配对

取 $Y=X_v$ 的 R128/R140 固定正则化 $J=J(t)$。
它为单射有界交换子，且
$$
J^nH\subseteq\operatorname{Dom}Y^n,\qquad
Y^kJ^n=(YJ)^kJ^{n-k}\quad(0\le k\le n).
\tag{7.1}
$$
对每个闭 $A$ 不变空间 $N$ 和每个正整数 $n$，
$$
\overline{J^nN}=N.
\tag{7.2}
$$
这是固定参数之间真实单位关系的结论，
没有从全空间稠密像猜测限制稠密性。

于是
$$
S=P(Y)J^m
\tag{7.3}
$$
是有界交换子。设 $M=\ker S$。
若 $x\in J^{2m}M$，则 $x\in\operatorname{Dom}Y^{2m}$ 且 $P(Y)x=0$。
若 $y\in U_\zeta J^{2m}M$，同域有限有界增量 (5.1) 给
$y\in\operatorname{Dom}Y^{2m}$ 且 $Q(Y)y=0$。

全部有界系数在 $\{A\}'$，故 $B$ 对称且与 $Y$ 域交换；
$Y$ 亦为 $C$ 自伴。在这些真实深域上将 (6.2) 作用于 $x$，得
$$
\begin{aligned}
B(A^h x,y)
&=B(b_0(Y)Q(Y)x,y)\\
&=B(b_0(Y)x,Q(Y)y)=0.
\end{aligned}
\tag{7.4}
$$
$\deg b_0\le m-1$ 和 $2m$ 次幂域保证每个中间向量都在所需域内。

先用 (7.2) 延到 $B(A^hM,U_\zeta M)=0$，
再用 R23 的 $\overline{A^hM}=M$，得到
$$
B(M,U_\zeta M)=0\qquad(\zeta^h\ne1).
\tag{7.5}
$$
R122 的有限 Fourier 支撑论证适用：
两个核向量的反射乘积仅有 $\mu_h$ 中的 Fourier 系数；
非零不变空间的总本质支撑全测，
迫每个低位柱上的限制秩至多一，从而 $\dim M\le h$。
实际 $A$ 单射、拟幂零，不允许非零有限维不变空间。因此
$$
\boxed{\ker S=0.}
\tag{7.6}
$$
全交换子的 $C$ 对称性再给 $\overline{\operatorname{Ran}S}=H$。

## 8. 从循环基向量传回点态多项式

$\mathcal V_w$ 循环，$S$ 有界、与 $A$ 交换且值域稠密，所以
$$
\overline{\mathbb C[A]S\mathcal V_w}
=\overline{S\,\mathbb C[A]\mathcal V_w}
=\overline{\operatorname{Ran}S}=H.
\tag{8.1}
$$
全部域已由 §3 和 (7.1) 核准；(4.4)、(4.6)、(7.3) 给
$$
\boxed{
S\mathcal V_w
=J^mU^{-1}R^pB_w^{-1}[F(u,v)e^w].
}
\tag{8.2}
$$
每个左乘因子都是有界交换子，保持
$\operatorname{cyc}_A(F(u,v)e^w)$。
由 (8.1)—(8.2)，此循环空间等于 $H$，(1.2) 得证。

将 $F$ 换成 $F-\lambda$ 不改变分别次数、角系数或最高 $U$ 系数 $r$，
因为 $p\ge1$。故相同证明对每个 $\lambda$ 成立，得到 (1.3)。
推论1.2随即成立。

## 9. 一个真正重叠的高阶例子

取
$$
u=\sum_{j\ge1}\frac{\chi_j}{j+1},\qquad
v=\chi_0+\sum_{j\ge1}\frac{(-1)^j\chi_j}{j+1}.
$$
前者空谱，$h_u=2$；后者 $h=1,b=1$，两个尾完全重叠。
任取 $\rho\in\mathbb C$ 及任意 $\ell^2$ 第一阶 $w$，则
$$
\left[u^2(v-\rho)^3+(1+i)uv^3+2v^2-3u+1\right]e^w
$$
循环，括号内再减任何标量仍成立。
最高 $u$ 系数为 $(V-\rho)^3$；低阶项无需分解成独立支持因子，
也无小系数条件。

## 10. 范围界线

- 若 $h_v>h_u$，(2.5) 的真有界除法一般不成立，不能照抄。
  R149 的有限交集支路另以显式局部因子给额外覆盖。
- 若没有非零角系数，消去 $X$ 后的最高 $Y$ 系数可能拟幂零，
  未必可逆，有限自由模步骤不能强行使用。
- 若最高系数 $r$ 与其平移有公共根，单位行列式仍可能失败。
  一般共振核未被排除。
- 本证明使用真实 mixed 域、空谱逆和有界正则化，
  没有假定任意高阶符号已存在一个最大闭自伴乘子。

新增循环类仍不足以覆盖全部 $H$；
普通 Hilbert ISP 及实际候选的一般不变格仍未解决。


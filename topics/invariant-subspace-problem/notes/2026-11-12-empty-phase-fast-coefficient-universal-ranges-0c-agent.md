# R189：空谱相位类的逆混合幂、普遍快系数范围与全部子商闭分式场

日期：2026-11-12（UTC）。作者：literature。根代理预留 R189。

状态：完整证明。对具有可和相位缺陷的非可和第一阶，允许任意有界交换扰动；其逆与 $A$ 的混合幂具有精确四次型。由此证明 $\mathcal G[L]$ 的非零元素在所有有限放大不变子商上单射稠密，进而把整个分式场推进到这些子商和限制。未把一般多项式的四次型直接认作最低 $A$ 阶，也未解决一般全平面谱第一阶的限制范围问题。

## 1. 主结论

设
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
a\in\ell^2\setminus\ell^1.
$$
假设存在 $\theta\in\mathbb R$，使
$$
\boxed{
\sum_j\left(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\right)<\infty.
}
\tag{1.1}
$$
令 $X=X_u$，并取任意
$$
H\in\mathfrak C:=\{A\}'.
$$
这里 $H$ 只要求有界；不要求 $H\in\mathcal A$，
也不要求它的 gauge 增量属于 $\mathcal G$。

记
$$
Y=X+H,\qquad Z=e^{-i\theta}Y,\qquad L=Z^{-1}.
\tag{1.2}
$$
下文先证明 $Y,Z$ 空谱，$L$ 是有界、单射、稠密像、拟幂零的交换子。

所有“子商”包括任意有限放大 $A^{(d)}$ 的闭不变子商。
对其诱导算子使用下标 $Q$。

**定理1.1（精确混合型）。**
对每个非零这样的 $Q$ 及整数 $r,k\ge0$，
$$
\boxed{
\tau_4(A_Q^rL_Q^k)=\frac{100}{15}r^4,
\qquad
\tau_4(T)=\liminf_{n\to\infty}
\frac{-\log\|T^n\|}{n^4}.
}
\tag{1.3}
$$
$r=k=0$ 时右侧为0，左侧对应恒等算子。

**定理1.2（所有子商上的快多项式）。**
对任意非零形式多项式
$$
P(t)=\sum_{i=0}^p g_it^i\in\mathcal G[t],
$$
实际有界算子
$$
P(L)=\sum_i g_iL^i\in\mathfrak C
$$
在每个非零 $Q$ 上不为零，而且
$$
\boxed{
\ker P(L)_Q=0,\qquad
\overline{\operatorname{Ran}P(L)_Q}=Q.
}
\tag{1.4}
$$
还存在强主理想单位：
$$
\boxed{
I\in\overline{P(L)\mathbb C[A]}^{\rm SOT}.
}
\tag{1.5}
$$

因此 $\mathcal B:=\mathcal G[L]$ 是忠实的多项式代数，
它的每个非零元素都具有普遍分母性质。

**定理1.3（整个普遍闭分式场）。**
整个
$$
\operatorname{Frac}\mathcal B=K(L)=K(Y)
$$
在每个非零 $Q$ 上有忠实最大闭实现：
对 $f=B/D$、$B,D\in\mathcal B$、$D\ne0$，
$$
\operatorname{Dom}T_{f,Q}
=\{x:B_Qx\in\operatorname{Ran}D_Q\},\qquad
D_QT_{f,Q}x=B_Qx.
\tag{1.6}
$$
该实现稠密定义、闭，原分母参数图为完整核心。
全部自然和、积取闭包后保留场运算。
非零实现单射且值域稠密；其在每个不变限制上的定义域和值域也稠密。
并且对域内向量有精确循环空间等式
$$
\boxed{
[T_{f,Q}x]_{A_Q}=[x]_{A_Q}
\quad(f\ne0).
}
\tag{1.7}
$$
原 $H$ 上还 $C$ 自伴。
本稿不为任意子商假设一个未构造的共轭。

## 2. 相位缺陷给真实空谱及小参数预解界

### 2.1. 旋转后的下有界实部

纯物理位算子为
$$
V_j^0=I-2E_j.
$$
对任意复数 $c$，
其 Hermitian 部分的两个特征值为
$$
\operatorname{Re}c\pm|c|.
$$
故
$$
\operatorname{Re}(cV_j^0)\ge-(|c|-\operatorname{Re}c)I.
\tag{2.1}
$$
实际第一阶与纯模型之差是有界扰动；这里不要求这个差本身与 $A$ 交换：
$$
X=a_*I+\sum_ja_jV_j^0+K(a),\qquad
\|K(a)\|\le C\|a\|_2\|\eta\|_2.
$$
该式在有限柱核心上成立，再取闭包。

用 (1.1)、(2.1) 得到某个有限 $\kappa\ge0$，使
$$
\operatorname{Re}\langle e^{-i\theta}Xx,x\rangle
\ge-\kappa\|x\|^2
\qquad(x\in\operatorname{Dom}X).
\tag{2.2}
$$
加上有界 $H$ 后，只需把 $\kappa$ 增加 $\|H\|$。
因此对 $Z=e^{-i\theta}(X+H)$，
$$
\operatorname{Re}\langle Zx,x\rangle\ge-\kappa\|x\|^2.
\tag{2.3}
$$

R138 已证明 (1.1) 与 $a\notin\ell^1$ 使 $X$ 空谱，
且 $X^{-1}$ 是有界拟幂零交换子。
因为 $H$ 与 $X^{-1}$ 交换，
$X^{-1}H$ 拟幂零，$I+X^{-1}H$ 是有界单位。
对每个 $\lambda\in\mathbb C$，
$$
Y-\lambda
=X\bigl(I+X^{-1}(H-\lambda)\bigr)
$$
是准确自然域上的等式。
所以
$$
(Y-\lambda)^{-1}
=\bigl(I+X^{-1}(H-\lambda)\bigr)^{-1}X^{-1}
\in\mathfrak C.
\tag{2.4}
$$
于是 $Y,Z$ 都空谱。

特别
$$
L=Z^{-1}\in\mathfrak C,\qquad \sigma(L)=\{0\}.
\tag{2.5}
$$
后式也可由 (2.4) 的逆谱恒等式直接验证：
每个非零 $\mu$ 都使 $L-\mu I$ 可逆，而有界算子谱非空。
$L$ 单射，值域为 $\operatorname{Dom}Z$，因而稠密。

### 2.2. 预解式的范数界和强极限

对 $s>0$，置
$$
R_s=(I+sZ)^{-1}.
$$
由 (2.3)，当 $s\kappa<1$ 时，
$$
\boxed{\|R_s\|\le(1-\kappa s)^{-1}.}
\tag{2.6}
$$
又在 $\operatorname{Dom}Z$ 上，
$$
R_sx-x=-sR_sZx.
\tag{2.7}
$$
定义域稠密与 (2.6) 的小 $s$ 一致界给
$$
R_s\to I\quad\text{强}.
\tag{2.8}
$$
所有这些算子均属于 $\mathfrak C$。

利用 $L=Z^{-1}$，
$$
\boxed{
R_s=L(L+sI)^{-1},\qquad
U_s:=\frac{I-R_s}{s}=(L+sI)^{-1},\qquad
LU_s=R_s.
}
\tag{2.9}
$$
因为 $L$ 拟幂零，$L+sI$ 及其逆都是有界交换单位。

## 3. 逆 $L$ 在所有有限放大子商上单射稠密

对固定 $s>0$，
$$
R_s=L\,U_s,
$$
且 $U_s$ 是有界交换子。
R88 的强多项式闭包给
$$
R_s\in\overline{L\mathbb C[A]}^{\rm SOT}.
$$
再用 (2.8)，得到
$$
\boxed{
I\in\overline{L\mathbb C[A]}^{\rm SOT}.
}
\tag{3.1}
$$
同样，对每个固定 $N$，
$R_s^N=L^NU_s^N\to I$ 强，故
$$
I\in\overline{L^N\mathbb C[A]}^{\rm SOT}.
\tag{3.2}
$$

这些强闭包结论同时作用于任意有限组坐标。
所以对每个有限放大中的闭不变空间及其子商，
$L_Q$ 单射且值域稠密。
单射性可直接验证：
若 $L_Qx=0$，则所有 $p(A_Q)L_Qx=0$，
强主理想单位迫使 $x=0$。
稠密像由 (3.1) 同样得到。

$L_Q$ 仍拟幂零，因为
$$
\|L_Q^n\|\le\|L^n\|.
$$
定义
$$
Z_Q=L_Q^{-1},\qquad
\operatorname{Dom}Z_Q=\operatorname{Ran}L_Q.
\tag{3.3}
$$
它闭、稠密定义。
无需把原空间无界算子在商上的域先作未经证明的识别。

有界恒等式 (2.9) 下降后给
$$
R_{s,Q}=(I+sZ_Q)^{-1},\qquad
\|R_{s,Q}\|\le(1-\kappa s)^{-1},
\tag{3.4}
$$
以及对 $x\in\operatorname{Dom}Z_Q$，
$$
R_{s,Q}x-x=-sR_{s,Q}Z_Qx.
\tag{3.5}
$$

每个有界 $A_Q$ 与 $L_Q$ 交换，
所以保持 $\operatorname{Dom}Z_Q$ 并与 $Z_Q$ 域交换。

## 4. 用 $O(n\log n)$ 输入放大构造混合幂下界

固定非零 $Q$。
为简洁，本节暂省去下标 $Q$，所有算子都在这个子商上。

取固定
$$
0\ne x\in\operatorname{Dom}Z.
$$
对任意整数 $N\ge1$，由 (3.5) 及幂的望远镜展开，
$$
\|R_s^Nx-x\|
\le Ns(1-\kappa s)^{-N}\|Zx\|.
\tag{4.1}
$$
若取 $s=\delta/N$，当 $N$ 足够大时，
$$
(1-\kappa\delta/N)^{-N}\le e^{2\kappa\delta},
$$
故
$$
\boxed{
\|R_{\delta/N}^Nx-x\|
\le\delta e^{2\kappa\delta}\|Zx\|.
}
\tag{4.2}
$$
给定固定误差目标，可先选 $\delta>0$ 足够小，使右侧小于该目标。

由 (2.9)、(3.4)，小 $s$ 时
$$
\|U_s\|\le\frac{1+\|R_s\|}{s}\le\frac3s.
\tag{4.3}
$$
而
$$
L^NU_s^N=R_s^N.
\tag{4.4}
$$
因此向量
$$
y_N=U_{\delta/N}^Nx
$$
满足
$$
L^Ny_N=R_{\delta/N}^Nx,\qquad
\|y_N\|\le(3N/\delta)^N\|x\|.
\tag{4.5}
$$

这一构造只把输入范数放大到
$$
\exp(O(N\log N)).
$$
后面 $N=kn$、$k$ 固定；
该代价是 $o(n^4)$，不会改变四次对数型。

## 5. 混合幂的精确四次型

记
$$
c_*=\frac{100}{15}.
$$

### 5.1. 普通上界给型的下界

对固定 $r,k\ge0$，
$$
(A_Q^rL_Q^k)^n=A_Q^{rn}L_Q^{kn}.
$$
若 $r\ge1$，R140 的实际权界给
$$
\|A_Q^{rn}L_Q^{kn}\|
\le W_{rn}\|L_Q\|^{kn},
$$
于是
$$
\tau_4(A_Q^rL_Q^k)\ge c_*r^4.
\tag{5.1}
$$
$r=0$ 时有界算子的几何幂界至少给 $\tau_4(L_Q^k)\ge0$。

### 5.2. 固定整数块与有限 offset

现在设 $r\ge1$、$k\ge1$。
固定正整数 $m$，再令高位指标 $j\to\infty$。
置
$$
n=n_{j,m}:=\left\lceil\frac{m2^j}{r}\right\rceil,\qquad
rn=m2^j+t_{j,m},\qquad 0\le t_{j,m}<r.
\tag{5.2}
$$

R140 给真实归一化高位弱极限
$$
\frac{A_Q^{m2^j}}{W_{m2^j}}
\longrightarrow 2^{-\operatorname{popcount}(m)}I_Q
\quad\text{WOT}.
\tag{5.3}
$$
$A_Q$ 单射，因此有限组
$$
A_Q^t x,\qquad 0\le t<r,
$$
都非零。
对它们分别用 (5.3)，再取有限个下界的最小值，
得到 $c_{m,x}>0$，使所有充分大的 $j$ 都有
$$
\boxed{
\|A_Q^{rn}x\|\ge c_{m,x}W_{m2^j}.
}
\tag{5.4}
$$
这一步同时覆盖随 $j$ 变化的全部有限 offset，
没有固定某个未经证明恒定的余数。

另一方面，$\|A_Q\|\le\|A\|<1$，所以
$$
\boxed{\|A_Q^{rn}\|\le W_{m2^j}.}
\tag{5.5}
$$

### 5.3. 先固定 $m$ 选误差，再让高位趋无穷

在 §4 中令 $N=kn$。
先针对这个固定的 $m$ 选 $\delta=\delta_{m,x}>0$，
使
$$
\delta e^{2\kappa\delta}\|Z_Qx\|
<\tfrac12c_{m,x}.
\tag{5.6}
$$
之后令 $j\to\infty$；
$\delta$ 不随 $j$ 变化。

取
$$
s=\delta/(kn),\qquad y_n=U_{s,Q}^{kn}x.
$$
由 (4.2)、(5.4)—(5.5)，
$$
\begin{aligned}
\|A_Q^{rn}L_Q^{kn}y_n\|
&=\|A_Q^{rn}R_{s,Q}^{kn}x\|\\
&\ge\|A_Q^{rn}x\|
 -\|A_Q^{rn}\|\|R_{s,Q}^{kn}x-x\|\\
&\ge\tfrac12c_{m,x}W_{m2^j}.
\end{aligned}
\tag{5.7}
$$
由 (4.5)，
$$
\|y_n\|\le(3kn/\delta)^{kn}\|x\|.
$$
所以
$$
\boxed{
\|A_Q^{rn}L_Q^{kn}\|
\ge
\frac{c_{m,x}}{2\|x\|}
W_{m2^j}(3kn/\delta)^{-kn}.
}
\tag{5.8}
$$

对固定 $m,r,k,x$，额外对数代价为 $O(n\log n)$。
因此实际权公式给
$$
\limsup_{j\to\infty}
\frac{-\log\|A_Q^{rn_{j,m}}L_Q^{kn_{j,m}}\|}
{n_{j,m}^4}
\le
100r^4\,\frac{D_4(m)}{m^4},
\tag{5.9}
$$
其中 $D_4(m)$ 为二进制四次位和。

最后取
$$
m=2^q-1,\qquad q\to\infty,
$$
则
$$
D_4(m)/m^4\to1/15.
$$
注意极限顺序：
先固定 $m$ 及其误差常数，
再 $j\to\infty$，
最后沿 $m=2^q-1$ 取极限。
结合 (5.1)，得到
$$
\tau_4(A_Q^rL_Q^k)=c_*r^4.
$$

仅取 $n=2^j$ 通常只给 $100D_4(r)$ 的较大上界，
不足以完成后面的最低 jet 矛盾。
本证明保留了精确常数所需的双重子列。

### 5.4. 边界情形

若 $r\ge1,k=0$，结论就是 R140 的精确
$\tau_4(A_Q^r)=c_*r^4$。

若 $r=0,k\ge1$，在 (4.2) 选 $\delta$ 使误差小于 $\|x\|/2$，
取 $N=kn$，得到
$$
\|L_Q^{kn}\|
\ge \tfrac12(3kn/\delta)^{-kn}.
$$
所以型不超过0；与几何幂界给的下界合并，型恰为0。

$r=k=0$ 为恒等算子。
这证明定理1.1 的全部情形。

## 6. 标量逆多项式与快尾和的型估计

### 6.1. 非零标量多项式不会增加最低 $A$ 型

若 $q(t)\in\mathbb C[t]\setminus\{0\}$，写
$$
q(t)=t^k v(t),\qquad v(0)\ne0.
$$
$L_Q$ 拟幂零，所以 $v(L_Q)$ 有界可逆。
它及逆与 $A_Q,L_Q$ 交换。
对每个固定 $n$ 的幂，只增加正负 $O(n)$ 对数项。
因此由定理1.1，
$$
\boxed{
\tau_4(A_Q^r q(L_Q))=c_*r^4.
}
\tag{6.1}
$$

这只处理标量 $q$。
不能由 (6.1) 自动给一般 $\mathcal G$ 系数多项式的精确型。

### 6.2. 有限交换和的四次谐和下界

若 $T_1,\ldots,T_N$ 有界且交换，
并有 $\tau_4(T_i)\ge b_i>0$，
则
$$
\boxed{
\tau_4\left(\sum_iT_i\right)
\ge
\left(\sum_i b_i^{-1/3}\right)^{-3}.
}
\tag{6.2}
$$
证明：先把每个 $b_i$ 略微减小。
由 liminf 定义，存在常数 $C_i$，使
$\|T_i^m\|\le C_i e^{-b_i m^4}$ 对全部 $m\ge0$ 成立。
展开交换多项式幂，
Hölder 不等式给
$$
\sum_i b_i m_i^4
\ge
\frac{(\sum_i m_i)^4}{(\sum_i b_i^{-1/3})^3}.
$$
全部多项式系数之和至多 $N^n$，
只增加 $O(n)$ 对数项。
取型并让略减的 $b_i$ 上升至原值，得到 (6.2)。

允许某项的型为无穷，按 $+\infty^{-1/3}=0$ 理解。
特别，固定有限个尾项各自型趋无穷时，其和的型也趋无穷。
乘以任意固定有界交换因子不降低四次型。

## 7. 最低精确 jet 排除所有非零子商上的多项式关系

取
$$
P(t)=\sum_{i=0}^p g_it^i\in\mathcal G[t]\setminus\{0\}.
$$
对零系数约定形式阶为无穷，令
$$
r=\min_i\operatorname{ord}\iota(g_i)<\infty.
$$
写 $c_i$ 为 $\iota(g_i)$ 的 $z^r$ 系数。
至少一个 $c_i$ 非零，所以
$$
q(t)=\sum_{i=0}^p c_it^i
\tag{7.1}
$$
是非零标量多项式。

对每个 $g_i$ 取 R151 的真正解析逼近 $f_{i,n}(A)$。
可对有限多个系数同步选择，使
$$
E_{i,n}=g_i-f_{i,n}(A),\qquad
\tau_4(E_{i,n})\to\infty.
\tag{7.2}
$$
R151 的精确 jet 稳定保证：舍去有限项后，
$$
f_{i,n}(z)=z^r(c_i+z h_{i,n}(z)),
\tag{7.3}
$$
其中 $h_{i,n}$ 为真正解析芽。
各解析半径和范数可依赖 $n$；证明不要求一致有界。

所以在任意子商 $Q$ 上有真实有界恒等式
$$
\boxed{
P(L)_Q
=A_Q^r q(L_Q)+A_Q^{r+1}H_{n,Q}+F_{n,Q},
}
\tag{7.4}
$$
其中
$$
H_{n,Q}=\sum_i h_{i,n}(A_Q)L_Q^i,\qquad
F_{n,Q}=\sum_i(E_{i,n})_Q L_Q^i.
$$
所有项有界且交换。
由 (7.2)、(6.2) 及子商范数不增加，
$$
\tau_4(F_{n,Q})\to\infty.
\tag{7.5}
$$

假设 $Q\ne0$ 而 $P(L)_Q=0$。
则
$$
A_Q^r q(L_Q)
=-A_Q^{r+1}H_{n,Q}-F_{n,Q}.
\tag{7.6}
$$
左侧由 (6.1) 具有精确型 $c_*r^4$。
右侧第一项具有型至少 $c_*(r+1)^4$，
因为 $H_{n,Q}$ 是每次固定的有界交换因子。
第二项的型由 (7.5) 趋无穷。

(6.2) 遂给
$$
c_*r^4
\ge
\left(
[c_*(r+1)^4]^{-1/3}
+\tau_4(F_{n,Q})^{-1/3}
\right)^{-3}.
\tag{7.7}
$$
右侧随 $n\to\infty$ 趋于 $c_*(r+1)^4>c_*r^4$，
故充分大的固定 $n$ 已产生矛盾。

因此
$$
\boxed{P(L)_Q\ne0
\quad\text{对每个非零有限放大不变子商 }Q.}
\tag{7.8}
$$

这个反证只判断不为零。
它没有由 (7.4) 推断
$\tau_4(P(L)_Q)=c_*r^4$。
较高 $A$ 阶项未必能有界地除以 $L^k$，
本稿没有使用那种未证的因子化。

## 8. 从每个子商不消失到普遍单射稠密

固定非零 $Q$，令 $T=P(L)_Q$。

若 $\ker T\ne0$，
它是闭 $A_Q$ 不变空间。
把这个空间再视为原有限放大的非零不变子商，
$P(L)$ 在它上面的诱导算子为零，
与 (7.8) 矛盾。
所以 $T$ 单射。

若
$$
N=\overline{TQ}\subsetneq Q,
$$
则 $N$ 闭且 $A_Q$ 不变；
在非零后续子商 $Q/N$ 上，$P(L)$ 的诱导算子为零，
仍与 (7.8) 矛盾。
所以 $T$ 值域稠密。

这证明 (1.4)。
在原 $H$ 上，非零形式多项式因此不可能求值为零，
故
$$
\mathcal G[t]\longrightarrow\mathfrak C,\qquad t\mapsto L
$$
忠实。

### 8.1 强主理想单位

给任意有限组 $x_1,\ldots,x_d\in H$，令
$$
M=\overline{\{(p(A)x_1,\ldots,p(A)x_d):p\in\mathbb C[z]\}}.
$$
这是闭 $A^{(d)}$ 不变空间。
(1.4) 在 $M$ 上给 $P(L)^{(d)}M$ 稠密。
再用定义中的多项式向量稠密性，
可把 $(x_1,\ldots,x_d)$ 逼近为
$$
(p(A)P(L)x_1,\ldots,p(A)P(L)x_d)
$$
的形式。
因此 (1.5) 成立。

此处是强拓扑的有限测试向量闭包，
没有给相应多项式逼近的一致算子范数界。

## 9. 每个子商上的整个闭分式场

置
$$
\mathcal B=\mathcal G[L].
$$
由 §8，每个非零 $\mathcal B$ 元素在所有非零 $Q$ 上单射稠密，
且在全部有限放大的后续不变图上也如此。

给 $f=B/D\in\operatorname{Frac}\mathcal B$，
按 (1.6) 定义 $T_{f,Q}$。
它闭、稠密定义；
域包含 $D_QQ$，像包含 $B_QQ$。

### 9.1 原分母图核心无需 gcd

最大图
$$
\mathcal L_f=\{(x,y):B_Qx=D_Qy\}
$$
是闭 $A_Q\oplus A_Q$ 不变空间。
$D_Q\oplus D_Q$ 在其上像稠密，而
$$
(D_Qx,D_Qy)=(D_Qx,B_Qx)
$$
属于原参数图。
所以
$$
\boxed{
\operatorname{Graph}T_{f,Q}
=\overline{\{(D_Qh,B_Qh):h\in Q\}}.
}
\tag{9.1}
$$
这一论证直接适用于原始分母；
不需要先取 gcd，也没有仅在全空间取消共同因子后猜测限制核心。

### 9.2 忠实性与闭场运算

同一个分式的两个表示 $B/D=B'/D'$ 满足 $BD'=B'D$。
利用单射分母取消，两个最大图相同。

反之，若两图相同，
在 $D_QD_Q'h$ 上比较值得
$$
(BD'-B'D)_Q=0.
$$
若括号是非零 $\mathcal B$ 元素，(7.8) 排除它在非零 $Q$ 上消失。
因此演算在每个非零子商上都忠实。

在共同分母 $D_QD_Q'$ 的稠密像上，
自然和、积有通常的有界参数恒等式。
(9.1) 说明这些参数图的闭包就是相应最大图；
反向在自然域上乘共同分母，给最大图包含。
于是
$$
\boxed{
\overline{T_{f,Q}+T_{g,Q}}=T_{f+g,Q},\qquad
\overline{T_{f,Q}T_{g,Q}}=T_{fg,Q},\qquad
(T_{f,Q})^{-1}=T_{1/f,Q}\ (f\ne0).
}
\tag{9.2}
$$
未声称自然乘积未经闭包已经闭，或两种次序的原始域相同。

### 9.3 单射稠密与谱边界

若 $f\ne0$，分子 $B_Q$ 单射，且其像包含于
$\operatorname{Ran}T_{f,Q}$，故
$$
\ker T_{f,Q}=0,\qquad
\overline{\operatorname{Ran}T_{f,Q}}=Q.
$$
若 $f\notin\mathbb C$，每个 $f-\lambda$ 非零。
有界标量扰动给同域等式
$$
T_{f,Q}-\lambda I=T_{f-\lambda,Q},
$$
所以没有点谱或剩余谱。

是否有界、哪些 $\lambda$ 是预解点，
仍取决于实际有界除法，
例如
$$
\lambda\in\rho(T_{f,Q})
\iff
\exists V\in B(Q):(B_Q-\lambda D_Q)V=D_Q.
$$
本稿不把它简化为任意形式次数的充分判据。

## 10. 限制饱和与精确循环空间保持

设 $M\subseteq Q$ 闭且 $A_Q$ 不变，
$x\in M\cap\operatorname{Dom}T_{f,Q}$，
记 $y=T_{f,Q}x$。
则
$$
D_Qy=B_Qx\in M.
$$
在商 $Q/M$ 上，$D$ 的诱导算子单射。
因此 $y\in M$。

所以每个最大分式都在其域内保持每个闭不变空间，
并且其限制恰等于用 $B|_M,D|_M$ 定义的最大分式。
(9.1) 给该限制的原分母图核心。
$D_QM$ 和 $B_QM$ 都在 $M$ 中稠密，
故定义域和值域各自稠密。

取 $M=[x]_{A_Q}$，得到
$$
[T_{f,Q}x]_{A_Q}\subseteq[x]_{A_Q}.
$$
对非零 $f$，再对逆分式 $1/f$ 与向量 $T_{f,Q}x$ 使用同一包含，
得到反向包含。
于是 (1.7) 成立。

这是比 R183 一般全空间分式的“循环 iff”更强的结论，
其依据是本稿新证明的全部后续子商单射性，
不是仅由原空间 $C$ 自伴性推出。

## 11. 与 $Y$ 的自然快系数多项式相容

因为 $L=Z^{-1}$ 是有界单射，
每个子商上
$$
Z_Q=L_Q^{-1},\qquad
\operatorname{Dom}Z_Q^p=\operatorname{Ran}L_Q^p
$$
都是准确自然幂，且闭。
这在本节由有界逆直接证明，
不调用一般商空间上未知的高次伴随域。

若
$$
P(z)=\sum_{j=0}^p g_jz^j,
$$
则
$$
P_{\rm nat}(Z_Q)L_Q^p
=\sum_{j=0}^p(g_j)_Q L_Q^{p-j}.
\tag{11.1}
$$
右侧是 $\mathcal B$ 中非零多项式的诱导算子。
最大实现就是用它作分子、$L_Q^p$ 作分母的 (1.6)。
若 $(x,y)$ 属于这个最大图，令
$$
x_s=R_{s,Q}^p x,\qquad y_s=R_{s,Q}^p y.
$$
由 $R_s^p=L^pU_s^p$ 知 $x_s\in\operatorname{Ran}L_Q^p$。
所有有界因子交换，故
$$
\left(\sum_j(g_j)_Q L_Q^{p-j}\right)x_s=L_Q^py_s.
$$
取消单射 $L_Q^p$，得到 $P_{\rm nat}(Z_Q)x_s=y_s$。
又 $x_s\to x$、$y_s\to y$，
所以该最大图恰等于自然多项式图的闭包。
原参数图也由 (9.1) 给出。

因此所有非零非首一 $\mathcal G[Z]$，
以及等价的 $\mathcal G[Y]$（只差固定复相位），
在每个不变子商和每个不变限制上均已获得稠密像。
它们的整个分式场为
$$
K(Z)=K(L)=K(Y).
$$

若 $H$ 也满足 R183 的加性条件，
原 $H$ 上这些最大实现与 R183 的实现相同：
两者都是同一自然多项式图的闭包，分式再由原参数图及场运算确定。
本稿额外得到的是全部限制和子商上的强结论。

## 12. 原空间的 $C$ 自伴与适用范围

原空间上 $\mathcal B\subseteq\mathfrak C$，
每个有界分子分母均 $C$ 对称。
以 (9.1) 的参数图求通常伴随，
得到
$$
T_{f,H}^*=CT_{f,H}C.
$$
子商一般不被 $C$ 保持，因此只保留上述最大图、闭场和单射稠密结论，
不自动附加 $C$ 自伴性。

本稿的正结论适用于：

- 任意 $a\in\ell^2\setminus\ell^1$ 满足 (1.1) 的复杂第一阶；
- 任意有界 $H\in\{A\}'$ 的扰动；
- 任意非零 $\mathcal G$ 系数多项式及其全部分式；
- 所有有限放大、不变子商及后续不变限制。

它不包括没有可和相位缺陷方向的全平面谱第一阶。
也不声称一般 $P(L)_Q$ 的四次型等于最低系数阶；
只对 (1.3)、(6.1) 的特定混合项证明了精确型。
对一般多项式，§7 使用的是有限 jet 的反证，不是一个未经证明的整体型公式。

## 13. 依赖与新增内容

使用 R128/R138 的相位缺陷空谱、真实闭域与预解式；
R88 的全部交换子强多项式闭包；
R140 的有限放大子商归一化高位弱极限和精确 $A$ 四次型；
R151 的快逼近类、精确有限 jet 稳定；
以及 R153 已使用过的最大分式参数图方法。

新增证明为：

1. 在每个非零子商上，以 $O(n\log n)$ 输入放大得到
   $\tau_4(A_Q^rL_Q^k)=100r^4/15$；
2. 最低精确 jet 加快尾谐和估计排除全部 $\mathcal G[L]$ 多项式关系；
3. 从所有后续子商不消失得到普遍单射、稠密像与强主理想单位；
4. 将整个 $K(Y)$ 从全空间闭场推进到所有子商和限制，并保持精确循环子空间。

该结果解决了这个空谱相位族的非首一快系数限制范围问题。
一般复系数第一阶、慢 Bell 单核及完整 Hilbert 不变子空间问题仍未解决。

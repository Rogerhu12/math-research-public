# 空谱第一阶乘子的有界系数多项式与单一 Rademacher 模式的全部点态多项式

日期：2026-11-12。作者：l2_moments，独占稿。
父代理预留 R134。状态：下列结论均已完整证明；相位缺陷扩展与幂域步骤由根代理独立提出，本稿逐项核验并展开。本文不声称任意二阶核或任意多模式多项式已经循环。

依赖：R125 的任意复 $\ell^2$ 第一 chaos 闭乘子、$C$ 自伴性、有限柱图核心与有界交换子域交换；R128 的不变子空间内第一阶定义域及像保持；R32 的 $\mathcal A$ 唯一特征；R88 的 $\{A\}'$ 交换性及其强多项式闭包。实际局部界 $\|V_j-(I-2E_j)\|\le8\eta_j$ 在 R130 中有含定义域的独立证明。

## 1. 结论与符号

设
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,
$$
并令 $X=X_u$ 为 R125 的实际闭乘子。它是有限系数乘子
$$
X_N=a_*I+\sum_{j<N}a_jV_j
$$
在有限次数初始域上的图闭包。

假设存在 $\theta\in\mathbb R$，使
$$
a\notin\ell^1,\qquad
\sum_{j\ge0}\left(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\right)<\infty.
\tag{1.1}
$$
则有以下结论。

1. $X$ 的预解集为整个复平面；每个 $(X-\lambda I)^{-1}$ 都是有界交换子。
2. 对任意 $p\ge1$ 和任意 $D_0,\ldots,D_{p-1}\in\{A\}'$，
   $$
   P(X)=X^p+\sum_{k=0}^{p-1}D_kX^k,
   \qquad \operatorname{Dom}P(X)=\operatorname{Dom}X^p,
   \tag{1.2}
   $$
   是闭的双射，且逆有界并属于 $\{A\}'$。对任意闭 $A$ 不变子空间 $M$，其限制部分在 $M$ 上同样双射。
3. 对每个 $p$，$1\in\operatorname{Dom}X^p$，且
   $$
   X_N^p1\longrightarrow X^p1.
   \tag{1.3}
   $$
   这条幂域结论事实上对任意复 $\ell^2$ 序列都成立，不依赖 (1.1)。
4. 对任意非零标量多项式 $q$，
   $$
   \boxed{q(u)\text{ 对 }A\text{ 循环}.}
   \tag{1.4}
   $$
   当 $q$ 非常数时，下文构造有界交换子 $J_q$，使 $J_qq(u)=1$。

(1.1) 包含任意同射线非负不可和系数，以及它加任意复 $\ell^1$ 误差的情形，但严格更宽。

## 2. 相位缺陷可和给空谱

旋转系数并吸收常数后，可先设 $\theta=0$。记
$$
\delta_j=|a_j|-\operatorname{Re}a_j\ge0,\qquad
\sum_j\delta_j<\infty.
$$
在物理单坐标表示中，
$$
S_j:=I-2E_j=
\begin{pmatrix}1&0\\-2&1\end{pmatrix}.
$$
$a_jS_j$ 的 Hermitian 部分是
$$
\begin{pmatrix}
\operatorname{Re}a_j&-\overline{a_j}\\
-a_j&\operatorname{Re}a_j
\end{pmatrix},
$$
其特征值为 $\operatorname{Re}a_j\pm|a_j|$。因此
$$
\operatorname{Re}\langle a_jS_jx,x\rangle\ge-\delta_j\|x\|^2.
$$
实际与纯差给
$$
\operatorname{Re}\langle a_jV_jx,x\rangle
\ge-(\delta_j+8|a_j|\eta_j)\|x\|^2.
\tag{2.1}
$$
第二项可和，因为 $a,\eta\in\ell^2$。

令尾闭乘子为
$$
T_m=X_{\sum_{j\ge m}a_j\chi_j},\qquad
c_m=\sum_{j\ge m}(\delta_j+8|a_j|\eta_j).
$$
于是 $c_m\to0$。对有限部分求和，再在有限柱图核心上取极限、最后取图闭包，(2.1) 给 $T_m+c_mI$ 增生。$T_m^*=CT_mC$，$C$ 为反线性等距共轭，故通常伴随 $T_m^*+c_mI$ 也增生。

这同时给最大增生性。具体地，当 $\operatorname{Re}z>c_m$，
$$
\|(T_m+zI)x\|\ge(\operatorname{Re}z-c_m)\|x\|.
$$
因此像闭；其像的正交补是
$\ker(T_m^*+\overline z I)$，而伴随的同一下界使此核为零。故
$$
R_m(z)=(T_m+zI)^{-1}\in\mathcal B(H),\qquad
\|R_m(z)\|\le(\operatorname{Re}z-c_m)^{-1}.
\tag{2.2}
$$
R125 的真实域交换使该预解式属于 $\{A\}'$。

固定任意 $\lambda\in\mathbb C$。写
$$
X=T_m+\beta_mI+K_m,
$$
其中
$$
\beta_m=a_*+\sum_{j<m}a_j,\qquad
K_m=\sum_{j<m}a_j(V_j-I)\in\mathcal A.
$$
$\mathcal A$ 的唯一特征取 $V_j$ 为 $1$，故 $K_m$ 的特征为零，因而拟幂零。又
$$
\operatorname{Re}\beta_m
=\operatorname{Re}a_*+\sum_{j<m}|a_j|-\sum_{j<m}\delta_j
\longrightarrow+\infty.
$$
选择 $m$ 使 $\operatorname{Re}(\beta_m-\lambda)>c_m$，取
$R_m=R_m(\beta_m-\lambda)$。$R_m$ 与 $K_m$ 交换，且
$$
\|(K_mR_m)^n\|^{1/n}
\le\|K_m^n\|^{1/n}\|R_m\|\longrightarrow0.
$$
所以 $I+K_mR_m$ 有界可逆。包含定义域的因式分解为
$$
X-\lambda I=(I+K_mR_m)(T_m+(\beta_m-\lambda)I),
$$
故
$$
\boxed{(X-\lambda I)^{-1}
=R_m(I+K_mR_m)^{-1}\in\{A\}'.}
\tag{2.3}
$$
这对所有 $\lambda$ 成立。

一般 $\theta$ 情形对 $e^{-i\theta}X$ 应用上述证明即可；常数项不会影响实部头和趋无穷的事实。

## 3. 有界逆必拟幂零；任意有界交换系数的 monic 多项式

以下代数引理将空谱化为所有次数的可逆性。

### 3.1 逆的拟幂零性

置 $R=X^{-1}$。对任意 $\mu\ne0$，$\lambda=\mu^{-1}$，令
$Q=(X-\lambda I)^{-1}$。预解式恒等式给
$$
Q-R=\lambda QR.
$$
直接相乘可得
$$
(R-\mu I)^{-1}
=-\mu^{-1}I-\mu^{-2}(X-\mu^{-1}I)^{-1}.
\tag{3.1}
$$
所以 $R$ 没有非零谱点，是有界拟幂零交换子。

由于 $R$ 单射且像为 $\operatorname{Dom}X$，
$$
\operatorname{Dom}X^p=\operatorname{Ran}R^p,\qquad
X^p=(R^p)^{-1}.
\tag{3.2}
$$
这由逐次应用 $X$、$R$ 直接归纳得到；特别是 $X^p$ 闭。这里没有使用通常为假的“闭算子的幂总闭”断言。

### 3.2 单项式为首项的有界系数多项式

令 $D_k\in\{A\}'$，并定义
$$
U=I+\sum_{k=0}^{p-1}D_kR^{p-k}.
\tag{3.3}
$$
所有 $D_k$ 与 $R$ 交换。可以写 $U-I=RL$，其中
$$
L=\sum_{k=0}^{p-1}D_kR^{p-k-1}
$$
有界且与 $R$ 交换。故
$$
\|(U-I)^n\|^{1/n}
\le\|R^n\|^{1/n}\|L\|\longrightarrow0,
$$
从而 $U$ 有界可逆。此处甚至不需要逐个论证拟幂零和的谱。

$U$、$U^{-1}$ 都与 $R$ 交换，因而保持
$\operatorname{Ran}R^p=\operatorname{Dom}X^p$。在此域上
$$
P(X)=UX^p=X^pU.
$$
所以
$$
\boxed{P(X)^{-1}=R^pU^{-1}\in\{A\}'.}
\tag{3.4}
$$
它是全空间有界算子，且值落在指定的 $\operatorname{Dom}X^p$ 中。因 $U$ 有界可逆、$X^p$ 闭，$P(X)$ 也闭。

更一般地，若 $D\in\{A\}'$ 任意有界，则
$$
X+D-\lambda I=[I+(D-\lambda I)R]X.
\tag{3.5}
$$
方括号与上面相同，是有界单位。因此空谱对任意有界交换子扰动保持；上述 monic 多项式定理也适用于 $X+D$。

### 3.3 不变子空间上的定义域与满射

R128 证明，对任意复第一阶闭乘子、任意闭 $A$ 不变 $M$，
$$
X(\operatorname{Dom}X\cap M)\subseteq M.
\tag{3.6}
$$
因而归纳给每个幂在其定义域内保持 $M$。所有 $D_k$、$U^{-1}$、$R^p$ 属于有界交换子代数，R88 使它们保持 $M$。故 (3.4) 将每个 $y\in M$ 送入
$\operatorname{Dom}X^p\cap M$，且 $P(X)x=y$。全空间单射性使限制也单射。因此限制部分双射，其逆恰为 (3.4) 在 $M$ 上的限制。

对 $X+D$ 同样成立，因为有界 $D$ 保持 $M$，而定义域与 $X$ 相同。这里使用了 (3.6)，没有单凭全空间有界逆保持 $M$ 就反推无界算子的所有定义域向量都保持 $M$。

## 4. 单一模式的有限生成函数与有界修正系数

本节起先不假设 (1.1)：令 $a\in\ell^2$ 为任意复序列。
对有限系数截断
$$
u_N=a_*+\sum_{j<N}a_j\chi_j,\qquad
X_N=a_*I+\sum_{j<N}a_jV_j,
$$
定义算子值整函数
$$
B_N(t)=\prod_{j<N}
e^{-ta_jV_j}\bigl(\cosh(ta_j)I+V_j\sinh(ta_j)\bigr).
\tag{4.1}
$$
各因子属于 $\mathcal A$，两两交换。

### 4.1 一致范数收敛

取统一界 $\|V_j\|\le M$。若
$$
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z),
$$
则 $H(0,V)=I$、$\partial_zH(0,V)=0$，并由两次微分得
$$
\|\partial_z^2H(z,V)\|
\le(M+1)^3e^{(M+1)|z|}.
$$
沿线段积分两次给
$$
\|H(z,V)-I\|
\le\frac12(M+1)^3|z|^2e^{(M+1)|z|}.
\tag{4.2}
$$
在任意固定 $|t|\le T$ 上，$\sup_j|a_j|\le\|a\|_2$，所以
$$
\sum_j\|H(ta_j,V_j)-I\|
\le C_{T,M,\|a\|_2}|t|^2\sum_j|a_j|^2<\infty.
$$
用有限乘积的 telescoping 和
$\prod(1+\|H_j-I\|)\le\exp\sum\|H_j-I\|$，可知 (4.1) 在每个紧圆盘上一致范数收敛到 $\mathcal A$ 值整函数 $B(t)$。因此对每个 $k$，
$$
B_{k,N}:=B_N^{(k)}(0)\longrightarrow B_k:=B^{(k)}(0)
\quad\text{于算子范数}.
\tag{4.3}
$$
且 $B_0=I$、$B_1=0$。这些导数是有界交换子；没有把形式系数的逐项收敛当作范数收敛。

例如
$$
B_2=\sum_j a_j^2(I-V_j^2)
\tag{4.4}
$$
按算子范数绝对收敛。这只是第一个修正，后面的证明不需要显式展开高阶 Bell 系数。

### 4.2 有限真恒等式

有限局部因子可精确相消：
$$
e^{tX_N}B_N(t)
=e^{ta_*}\prod_{j<N}
\bigl(\cosh(ta_j)I+V_j\sinh(ta_j)\bigr).
$$
对真空向量 $1$ 作用，使用 $\prod_{j\in F}V_j1=\chi_F$，得到
$$
\boxed{e^{tu_N}=B_N(t)e^{tX_N}1.}
\tag{4.5}
$$
这是每个有限 $N$ 的 $H$ 值整函数恒等式。它不是把一般实际乘子与点乘混为一谈。

对 $t$ 微分 $p$ 次并在 $0$ 取值，得到
$$
u_N^p=
\sum_{k=0}^p\binom pk B_{k,N}X_N^{p-k}1.
\tag{4.6}
$$
由于 $B_{0,N}=I$，这是以 $X_N^p1$ 为首项的三角递推。

## 5. 从有限递推到真实闭算子幂：完整域证明

### 5.1 所有有限矩的强收敛

对任意有限复系数 $c_j$，Rademacher 展开和
$(2r)!\ge2^r r!$ 给
$$
\mathbb E\left|\sum_jc_j\chi_j\right|^{2p}
\le
\frac{(2p)!}{2^p p!}
\left(\sum_j|c_j|^2\right)^p.
\tag{5.1}
$$
一种直接验证是展开左侧：只有每个指标出现偶数次的项不消失，取绝对值后不超过以 $|c_j|$ 为实系数的同阶矩；后者是
$\prod_j\cosh(t|c_j|)$ 的 $t^{2p}$ 系数乘 $(2p)!$，逐项比较
$\cosh(tx)\preceq e^{t^2x^2/2}$ 给出 (5.1)。

把 (5.1) 用于系数尾，得 $u_N\to u$ 于每个 $L^{2p}$，且相应范数一致有界。由
$$
|z^p-w^p|\le p|z-w|(|z|+|w|)^{p-1}
$$
及 Hölder，
$$
u_N^p\longrightarrow u^p\quad\text{于 }H
\tag{5.2}
$$
对每个固定 $p$ 成立。

### 5.2 先建立有限算子幂向量的强极限

定义 $v_{p,N}=X_N^p1$。$v_{0,N}=1$，$v_{1,N}=u_N$。
由 (4.6) 解出
$$
v_{p,N}
=u_N^p-\sum_{k=1}^p\binom pk B_{k,N}v_{p-k,N}.
\tag{5.3}
$$
按照 $p$ 归纳，(4.3)、(5.2) 说明每个 $v_{p,N}$ 都在 $H$ 中收敛。记极限为 $v_p$。于是
$$
v_0=1,\qquad
u^p=\sum_{k=0}^p\binom pk B_kv_{p-k}.
\tag{5.4}
$$
到这里尚未把 $v_p$ 称作 $X^p1$。

### 5.3 用伴随图核心识别每一级定义域

R125 给有限柱为 $X$ 的图核心；由于 $C$ 保持有限柱并满足
$X^*=CXC$，有限柱也为 $X^*$ 的图核心。对任意有限柱 $z$，
$$
X_N^*z\longrightarrow X^*z.
$$
由有限算子通常伴随恒等式，
$$
\begin{aligned}
\langle v_p,z\rangle
&=\lim_N\langle X_N^p1,z\rangle\\
&=\lim_N\langle X_N^{p-1}1,X_N^*z\rangle\\
&=\langle v_{p-1},X^*z\rangle.
\end{aligned}
\tag{5.5}
$$
该式按 $X^*$ 图范数延拓到其完整定义域。右侧作为 $z$ 的通常范数泛函由左侧向量 $v_p$ 表示，所以
$$
v_{p-1}\in\operatorname{Dom}(X^*)^*
=\operatorname{Dom}X,\qquad Xv_{p-1}=v_p.
$$
递归得到
$$
\boxed{
1\in\operatorname{Dom}X^p,\qquad
v_p=X^p1,\qquad
X_N^p1\to X^p1.
}
\tag{5.6}
$$
因此 (5.4) 成为真实定义域上的公式
$$
\boxed{
u^p=\sum_{k=0}^p\binom pk B_kX^{p-k}1.
}
\tag{5.7}
$$

这一步没有从 $X_N1\to u$ 自动推断高次幂收敛，也没有未经证明地交换闭包和乘积。所有高次幂先由有限三角恒等式强收敛，再通过通常伴随的图核心逐级进入真实域。

## 6. 点态多项式成为 monic 的闭算子多项式

设
$$
q(z)=\sum_{r=0}^p c_rz^r,\qquad c_p\ne0.
$$
代入 (5.7)，得到
$$
q(u)=\sum_{\ell=0}^pD_\ell X^\ell1,
\qquad
D_\ell=\sum_{r=\ell}^p
c_r\binom r\ell B_{r-\ell}.
\tag{6.1}
$$
每个 $D_\ell\in\mathcal A$，且 $D_p=c_pI$。所以当 (1.1) 成立时，
$c_p^{-1}\sum_{\ell=0}^pD_\ell X^\ell$ 正是 §3 的 monic 多项式。其逆有界并属于 $\{A\}'$，故存在
$$
J_q=\left(\sum_{\ell=0}^pD_\ell X^\ell\right)^{-1}
\in\{A\}',\qquad J_qq(u)=1.
\tag{6.2}
$$
R88 给每个有界交换子保持每个闭 $A$ 不变循环空间，因此
$$
1\in\operatorname{cyc}_A(q(u)).
$$
由 $1$ 本身循环，$\operatorname{cyc}_A(q(u))=H$。非零常数多项式的结论直接成立。

作为显式二阶例，
$$
u^2=X^21+B_21,
$$
所以 $u^2-\lambda$ 是
$X^2+(B_2-\lambda I)$ 作用于 $1$，对所有 $\lambda$ 都循环。
同样的结论适用于任意标量多项式的次数和系数；无需多项式可分解为互不重叠的独立第一阶因子。

## 7. 范围、例子与准确边界

### 7.1 同射线系数加任意绝对可和扰动

若
$$
a_j=e^{i\theta}b_j+c_j,\qquad
b_j\ge0,\quad b\in\ell^2\setminus\ell^1,\quad c\in\ell^1,
$$
则
$$
|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\le2|c_j|.
$$
故 (1.1) 成立，所有 $q(u)$ 都循环。这里 $c$ 可以有任意复相位。

### 7.2 真正超过上述绝对可和扰动的相位变化

例如
$$
a_j=\frac{\exp(i/\log(j+2))}{j+1}.
\tag{7.1}
$$
它属于 $\ell^2\setminus\ell^1$，且
$$
|a_j|-\operatorname{Re}a_j
=\frac{1-\cos(1/\log(j+2))}{j+1}
\le\frac{1}{2(j+1)\log^2(j+2)}
$$
可和。然而它不能表示成固定正射线上的非负序列加 $\ell^1$ 误差：若该射线角非零，最终到射线的距离是 $|a_j|$ 的固定正比例；若射线角为零，虚部绝对值与
$1/((j+1)\log(j+2))$ 同阶而不可和。因而这个例子由相位缺陷判据真正新增。

### 7.3 本文没有越过的边界

幂域公式 (5.6)—(5.7) 对任意复 $\ell^2$ 第一阶输入成立。空谱及由它得到的 monic 可逆性在本文使用了 (1.1)。任意复系数第一阶输入虽由 R125 已循环，但尚不能从“每个 $X-\lambda$ 单射稠密”改成“$X$ 有有界逆”；这会错误地把连续谱排除。

同样，§3 的任意有界交换子扰动是一个算子结论。若把输入向量改成
$u+D1$，其中 $D\in\{A\}'$ 任意，不能未经新的有限矩与生成函数论证就把
$q(u+D1)$ 也归入 §6。本文的点态多项式结论只作用于明确的单一第一 chaos 模式及其标量常数平移。

最后，一般多模式多项式、一般无限秩二阶核、任意 $L^2$ 向量循环性仍未由本条解决。

# R149：空谱一阶因子的多项式与重叠一阶因子点态相乘

日期：2026-11-12。作者：l2_moments；任意多项式扩充与根代理同时独立推导，并共同核对。
状态：完整证明待全文交叉审读。只使用真实第一阶闭域、R134/R145 混合 Bell 恒等式及实际余数除法。

本稿不要求两个模式有不交支撑。其新增部分包括任意无限重叠，但需要明确的首位顺序；支撑交集有限时可取消该顺序条件。

## 1. 主定理

设
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
v=b_*+\sum_{j\ge0}b_j\chi_j,
\qquad a,b\in\ell^2.
\tag{1.1}
$$
假设第一阶闭乘子 $X=X_u$ 的谱为空。R134/R138 给出的准确可用情形是：$a\notin\ell^1$，且存在 $\theta\in\mathbb R$ 满足
$$
\sum_j\bigl(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\bigr)<\infty.
\tag{1.2}
$$
常数项 $a_*$ 任意。特别地，非负不可和 $\ell^2$ 系数以及其有限相位缺陷扰动都适用。

若 $v$ 非常数，记
$$
j_u=\min\{j:a_j\ne0\},\qquad j_v=\min\{j:b_j\ne0\},
\qquad h_u=2^{j_u},\quad h_v=2^{j_v}.
\tag{1.3}
$$

**定理1.1。** 设 $q\in\mathbb C[w]\setminus\{0\}$。以下任一条件足以保证
$$
\boxed{q(u)v\text{ 对实际 }A\text{ 循环}:}
\tag{1.4}
$$

1. $v$ 非常数，且 $h_v\le h_u$；两个系数列的支撑交集可任意无限。
2. $v$ 非常数，且 $\{j:a_jb_j\ne0\}$ 有限；不限制 $h_u,h_v$ 的大小关系。
3. $v$ 为非零常数。

$q(u)v\in L^2$ 由复 Rademacher 全部有限矩估计和 Hölder 不等式保证。
循环性同时证明该向量非零；不需要另外从点态分布的无原子性推断非零。
当 $v=0$ 时乘积是零向量，不在结论内。

若 $q$ 为非零常数，结论直接是 R125 的非零第一 chaos 循环性。
若 $v$ 是非零常数，结论直接是 R134 的空谱一模式多项式循环性。
以下证明 $\deg q=p\ge1$ 且 $v$ 非常数。
除以 $q$ 的非零首项系数，可设 $q$ 首一。

特别地，$uv$ 在前两种条件下循环。给 $u,v$ 添加任意常数或将 $q$ 的根任意平移，不改变假设中的支撑条件。

## 2. 空谱逆、gauge 逆及真实定义域

令 $Z=X_v$。R125 给 $X,Z$ 的闭 $C$ 自伴实现；有限柱分别为图核心，全部有界交换子保持其定义域并与其域交换。

因为 $\sigma(X)=\varnothing$，
$$
R=X^{-1}\in\{A\}'
\tag{2.1}
$$
是全空间有界单射算子，$\operatorname{Ran}R=\operatorname{Dom}X$。
R134 的预解恒等式给 $R$ 拟幂零。具体对 $\mu\ne0$，
$$
(R-\mu I)^{-1}
=-\mu^{-1}I-\mu^{-2}(X-\mu^{-1}I)^{-1},
$$
所以 $\sigma(R)=\{0\}$。于是
$$
\operatorname{Dom}X^n=R^nH,
\qquad X^nR^n=I,
\qquad R^nX^n=I\text{ 在 }\operatorname{Dom}X^n.
\tag{2.2}
$$

固定 dyadic $\zeta$。R125 给包含定义域的等式
$$
\gamma_\zeta(X)=X+D_u,\qquad
\gamma_\zeta(Z)=Z+D_v,
\tag{2.3}
$$
其中 $D_u,D_v$ 为有限的真正解析芽在 $A$ 上的值。
两个 gauge 都保持相应第一阶定义域。
$\gamma_\zeta(X)$ 与 $X$ 酉等价，仍为空谱，所以
$$
\gamma_\zeta(R)=(X+D_u)^{-1}
\tag{2.4}
$$
是真正有界逆，并且由酉等价同样拟幂零。
从两个闭逆的含域恒等式得到
$$
\boxed{
\gamma_\zeta(R)-R=-\gamma_\zeta(R)D_uR,
\qquad R=\gamma_\zeta(R)(I+D_uR).
}
\tag{2.5}
$$
例如 $(X+D_u)R=I+D_uR$ 在整个 $H$ 上合法，左乘其有界逆即得第二式，第一式随之成立。

所有这些有界算子属于全交换子 $\{A\}'$，它由 R88 可交换。
没有要求 $R$ 或 $\gamma_\zeta(R)$ 属于范数代数 $\mathcal A$。
本稿使用它们的拟幂零性和全交换性，而不使用不存在的 $\mathcal A$ 字符。

## 3. 线性于第二模式的混合 Bell 恒等式

记
$$
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z).
$$
R145 证明
$$
\mathcal B(t,s)
=\prod_j H(ta_j+sb_j,V_j)
\tag{3.1}
$$
在每个紧双圆盘按算子范数一致收敛，且为整算子函数。
置
$$
B_k=\partial_t^k\mathcal B(0,0),\qquad
G_k=\partial_t^k\partial_s\mathcal B(0,0).
\tag{3.2}
$$
$B_0=I$、$B_1=0$、$G_0=0$。
$B_k$ 是 $u$ 的通常 Bell 系数。

对本稿重要的是，全部 $B_k,G_k$ 均属于
$$
\mathcal A_{h_u}=\overline{\mathbb C[I,A^{h_u}]}.
\tag{3.3}
$$
对于 $B_k$ 这由 $a_j=0$ 于 $j<j_u$ 直接得到。
对于 $G_k$，注意
$$
\partial_zH(z,V)
=e^{-zV}(I-V^2)\sinh z,
\qquad \partial_zH(0,V)=0.
\tag{3.4}
$$
若 $a_j=0$，该位对 $\partial_s\mathcal B(t,0)$ 的贡献恒为零。
剩下的位均在 $j\ge j_u$，所以导数及其范数极限属于同一个闭子代数。
特别地，即使 $v$ 在更低位有非零系数，它也不会单独产生混合修正。

R145 还给 $1$ 的全部混合自然幂域，尤其
$$
Z1\in\operatorname{Dom}X^p,
\qquad X^rZ1=ZX^r1\quad(0\le r\le p).
\tag{3.5}
$$
这不是仅由 $X_N1\to X1$ 推得；其依据是混合有限矩的三角递推及每个第一阶伴随的有限柱图核心。

定义有限多项式
$$
P_q(w)=\sum_{k=0}^p\frac{B_k}{k!}q^{(k)}(w),
\qquad
C_q(w)=\sum_{k=0}^p\frac{G_k}{k!}q^{(k)}(w).
\tag{3.6}
$$
$P_q$ 首一、次数为 $p$，而 $G_0=0$ 保证
$$
\deg C_q\le p-1.
\tag{3.7}
$$
对 (3.1) 的有限生成函数先取一次 $s$ 导数，再取 $t$ 的有限次导数，随后用 R145 的强极限识别，得到真实向量等式
$$
\boxed{q(u)v=P_q(X)Z1+C_q(X)1.}
\tag{3.8}
$$
每一项都已由 (3.5) 放在相应自然域内。
例如 $q(w)=w$ 时
$$
C_q=G_1=\sum_j a_jb_j(I-V_j^2),
\qquad uv=XZ1+G_1 1.
\tag{3.9}
$$
此级数因 $\sum_j|a_jb_j|<\infty$ 而按算子范数绝对收敛。

## 4. 将多项式因子除掉：剩下第一阶加有界拟幂零修正

写
$$
P_q(w)=w^p+\sum_{\ell=0}^{p-1}P_\ell w^\ell,
\qquad
C_q(w)=\sum_{\ell=0}^{p-1}C_\ell w^\ell,
\qquad P_\ell,C_\ell\in\mathcal A_{h_u}.
$$
令
$$
U=I+\sum_{\ell=0}^{p-1}P_\ell R^{p-\ell}.
\tag{4.1}
$$
$U-I=R L$，其中 $L$ 是有界交换子。$R$ 拟幂零且与 $L$ 交换，所以 $RL$ 拟幂零，$U$ 为全交换子中的真实有界单位。
R134 的含域因式分解给
$$
P_q(X)=UX^p\text{ 于 }\operatorname{Dom}X^p,
\qquad
J=P_q(X)^{-1}=R^pU^{-1}\in\{A\}'.
\tag{4.2}
$$
自然 $P_q(X)$ 在这里闭，且确有全空间有界逆。

下式是有界算子定义，不是任意无界乘积：
$$
K=U^{-1}\sum_{\ell=0}^{p-1}C_\ell R^{p-\ell}
=R D,
\qquad
D=U^{-1}\sum_{\ell=0}^{p-1}C_\ell R^{p-\ell-1}.
\tag{4.3}
$$
它与 $JC_q(X)$ 在自然域上一致。
由 (3.5)、(3.8) 和 (4.2)，
$$
\boxed{J[q(u)v]=(Z+K)1.}
\tag{4.4}
$$
令
$$
T=Z+K,\qquad \operatorname{Dom}T=\operatorname{Dom}Z.
\tag{4.5}
$$
由于 $K$ 是有界交换子，它对 $B$ 对称；有界扰动于是给 $T^*=CTC$。
有限柱仍是 $T$ 的图核心，全部有界交换子保持其域并与其域交换。
其 gauge 亦保持同一域，因为 (2.3) 的 $D_v$ 和 $K$ 的 gauge 差均有界。

## 5. 首位顺序分支：所有被除项都有真正的有界商

现在假设 $h_v\le h_u$。
对任意 $Q\in\mathcal A_{h_u}$，R139 的实际有限余数分解给
$$
\gamma_\zeta(Q)-Q=A^{h_u}Q_\zeta,
\qquad Q_\zeta\in\mathcal A_{h_u}.
\tag{5.1}
$$
这条规则适用于 $P_\ell,C_\ell$，但本稿不声称一般 $Q-\chi(Q)I$ 可被 $A^{h_u}$ 有界整除。

此外 $D_u=A^{h_u}d_u(A)$，其中 $d_u$ 为真正解析芽，可能对某些 $\zeta$ 首字符为零。
由 (2.5)，
$$
\gamma_\zeta(R)-R=-A^{h_u}\gamma_\zeta(R)d_u(A)R.
\tag{5.2}
$$
有限乘积差的望远镜式说明：以 $P_\ell,C_\ell,R$ 构成的每个有限和、乘积的 gauge 差，都真实地含有有界因子 $A^{h_u}$。
对 $U^{-1}$，使用
$$
\gamma_\zeta(U^{-1})-U^{-1}
=-\gamma_\zeta(U)^{-1}
(\gamma_\zeta(U)-U)U^{-1}.
\tag{5.3}
$$
所以 (4.3) 中的 $D$ 也满足
$$
\gamma_\zeta(D)-D=A^{h_u}E_\zeta
\quad\text{对某个真实有界 }E_\zeta\in\{A\}'.
\tag{5.4}
$$
没有把范数演算中的形式首阶直接当作可除性；每次除法都明确来自 (5.1)、(5.2)、有限乘积差或真实逆恒等式 (5.3)。

由 $K=RD$，
$$
\begin{aligned}
\gamma_\zeta(K)-K
&=(\gamma_\zeta(R)-R)D
+\gamma_\zeta(R)(\gamma_\zeta(D)-D)\\
&=A^{h_u}\gamma_\zeta(R)
\bigl(E_\zeta-d_u(A)RD\bigr).
\end{aligned}
\tag{5.5}
$$
若 $\zeta^{h_v}\ne1$，则第一阶真正解析差给
$$
D_v=A^{h_v}d_v(A),
\qquad d_v(0)=-\frac{2b_{j_v}}{W_{h_v}}
(\zeta^{h_v}-1)\ne0.
\tag{5.6}
$$
由 (5.5)—(5.6)，
$$
\boxed{
\gamma_\zeta(T)-T=A^{h_v}\mathcal U_\zeta,
\quad
\mathcal U_\zeta=d_v(A)+\gamma_\zeta(R)F_\zeta,
}
\tag{5.7}
$$
其中 $F_\zeta\in\{A\}'$ 有界，吸收了 $A^{h_u-h_v}$。

$d_v(A)$ 为真正解析单位。由于所有有界交换子彼此交换，
$$
d_v(A)^{-1}\gamma_\zeta(R)F_\zeta
$$
是拟幂零：其 $n$ 次幂范数的 $n$ 次根至多为
$\|d_v(A)^{-1}F_\zeta\|\|\gamma_\zeta(R)^n\|^{1/n}\to0$。
故 $\mathcal U_\zeta$ 为真实有界交换单位。
这个判断不需要给 $R$ 指派 $\mathcal A$ 的字符。

## 6. 有限交集分支：不用首位顺序

现在只假设
$$
I=\{j:a_jb_j\ne0\}\text{ 有限}.
$$
所有 $j\in I$ 均满足 $2^j\ge h_v$。
由 (3.4)，有算子范数意义下的有限和
$$
\partial_s\mathcal B(t,0)
=\sum_{j\in I}b_j e^{-ta_jV_j}(I-V_j^2)
\sinh(ta_j)\prod_{k\ne j}H(ta_k,V_k).
\tag{6.1}
$$
不在交集中的位导数为零。
每个局部因子都能真实地提取 $A^{h_v}$，因为
$$
I-V_j^2
=4N_j(I+N_j)^{-2}
=A^{h_v}\frac{4A^{2^j-h_v}}{W_{2^j}}(I+N_j)^{-2}.
\tag{6.2}
$$
有限和中分母可能很大，但均为固定有限常数；其余乘积按算子范数在紧盘收敛。
取有限次 $t$ 导数遂得
$$
G_k=A^{h_v}\widetilde G_k
\quad\text{且 }\widetilde G_k\in\{A\}'\text{ 有界}.
\tag{6.3}
$$
因此 $C_q$ 的所有系数都真正含有这个因子；(4.3) 于是写为
$$
K=A^{h_v}R L
\quad\text{对某个有界 }L\in\{A\}'.
\tag{6.4}
$$

不必要求 $\gamma_\zeta(L)-L$ 可除 $A^{h_v}$。直接用 (2.5)，
$$
\begin{aligned}
\gamma_\zeta(K)-K
&=A^{h_v}\bigl[\zeta^{h_v}\gamma_\zeta(R)\gamma_\zeta(L)-RL\bigr]\\
&=A^{h_v}\gamma_\zeta(R)
\bigl[\zeta^{h_v}\gamma_\zeta(L)-(I+D_uR)L\bigr].
\end{aligned}
\tag{6.5}
$$
结合 (5.6)，再次得到 (5.7) 的单位结论。
这证明有限交集分支，特别允许 $h_v>h_u$。
若交集为空，则全部 $G_k,C_q,K$ 都为零，也与上述公式一致。

## 7. 闭 cocycle 的排核、共同正则化及循环传递

两种分支均已证明：对 $\zeta\notin\mu_{h_v}$，
$$
\gamma_\zeta(T)-T=A^{h_v}\mathcal U_\zeta,
\qquad \mathcal U_\zeta\in\{A\}'^\times.
\tag{7.1}
$$
这里给出排核的完整接口，避免将全空间稠密性误传给未知限制。

固定 $\lambda\in\mathbb C$，令 $M=\ker(T-\lambda I)$。
$M$ 闭且 $A$ 不变；全部有界交换子及单位的逆都保持 $M$。
所以 $\mathcal U_\zeta M=M$，而 R23 给
$$
\overline{A^{h_v}\mathcal U_\zeta M}=M.
\tag{7.2}
$$
$T$ 的 gauge 同域和 $C$ 自伴性使跨核配对合法：
$$
B((\gamma_\zeta(T)-T)M,U_\zeta M)=0.
$$
由 (7.2)，$B(M,U_\zeta M)=0$ 于有限子群之外。
R122 的 Fourier 与总本质支撑论证给 $\dim M\le h_v$，
再由 $A$ 单射拟幂零排除非零有限维不变空间。因此
$$
\boxed{\ker(T-\lambda I)=0\quad(\lambda\in\mathbb C).}
\tag{7.3}
$$
$C$ 自伴性还给这些闭算子的全空间值域稠密。

为了把排核变成向量循环，可取 $Z=X_v$ 的 R128 四正分量共同正则化 $R_v(t)$。它满足
$$
R_v(t)H\subseteq\operatorname{Dom}Z=\operatorname{Dom}T,
\qquad ZR_v(t)\in\{A\}'\text{ 有界},
$$
且单射。故
$$
T R_v(t)=ZR_v(t)+K R_v(t)\in\{A\}'
\tag{7.4}
$$
是有界单射算子。R88 的全交换子 $C$ 对称性给其值域稠密。
因为 $1$ 对 $A$ 循环，$(TR_v(t))1$ 循环。
域交换和 $1\in\operatorname{Dom}T$ 又给
$$
(TR_v(t))1=R_v(t)T1.
$$
$R_v(t)$ 保持每个闭 $A$ 不变空间，故 $T1$ 也循环。

最后 (4.4) 给 $J[q(u)v]=T1$。$J$ 是有界交换子，保持
$\operatorname{cyc}_A(q(u)v)$；它的像中已包含循环向量 $T1$，所以
$$
\operatorname{cyc}_A(q(u)v)=H.
$$
定理1.1得证。所有共同正则化都只用于明确的第一阶闭域；没有构造或假设一般高阶点态乘子的闭实现。

## 8. 一个确有无限重叠、第二模式无相位缺陷的例子

取
$$
u=\sum_{j\ge0}\frac{1}{j+1}\chi_j,
\qquad
v=\sum_{j\ge0}\frac{(-1)^j}{j+1}\chi_j.
$$
$X_u$ 空谱，两个模式都有首位 $h_u=h_v=1$，支撑交集为全部自然数。
$v$ 不满足任何有限相位缺陷条件；R138 给 $X_v$ 的全平面连续谱。
本定理仍给
$$
\boxed{q(u)v\text{ 循环}
\quad\text{对每个非零标量多项式 }q.}
$$
例如 $uv$、$(u^2+1)v$ 均属此类。
它们不是两个不交位第一因子的点态乘积，也不把两个模式当成同一个模式。

## 9. 准确范围

本稿不处理两个因子都处于一般全平面连续谱类、且有无限重叠的所有点态乘积。
尤其交替模式 $v$ 的共振向量 $v^2-1$ 没有被本稿自动排除。

首位顺序分支所需的有界除法只作用于实际 gauge 差；有限交集分支则由每个明确局部因子 (6.2) 完成。
没有将“形式首阶足够高”自动当作任意范数代数元的有界除法，也没有要求空谱逆属于 $\mathcal A$。

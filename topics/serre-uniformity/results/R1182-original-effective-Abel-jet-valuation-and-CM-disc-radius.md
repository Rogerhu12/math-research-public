# R1182：原半秩商的有效 Abel 首项估值与完整 CM 盘半径

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明，半径保留实际模型与高度依赖。** 本篇在 R1011 的同一个原曲线、非 CM 半秩商和有理 CM 点上，构造由同一 $\beta$ 定义的整 Mordell–Weil 消去泛函。其首项写成一个固定有理线性形式在 $\log_q\beta'$ 上的值，适用 Fuchs–Pham 的有效估值定理。再以 Néron 不变微分控制全部尾项，得到一个明确的完整圆盘：该盘内的原有理点只有 $c_1$。

这里的半径依赖所选实际商的代数模型、同源尺度、原点差高度及可验证的局部 chart。没有证明它已覆盖旧候选所在的固定深度圆盘，也没有给出对 level $p$ 的绝对统一半径。本篇不将有限 Cartan 标记提升到 $p^n$ 层，不把 CM 椭圆曲线的晶体标架移到非 CM 商。

## 1. 全部对象仍是 R1011 的原对象

用 $p$ 表示原模曲线的 level，用 $q$ 表示本篇取对数的局部素数；目标应用允许且主要考虑 $q=p$。先取任意奇素数 $q$。

沿用 [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md) 的实际数据

$$
X=X_1=\operatorname{Norm}\left(X_{\rm ns}^+(p)\times_j\mathbf P^1_b\right),
\qquad j=6912b^3(1-b^3),
$$
$$
c_0:b=0,\qquad c_1:b=1,\qquad
D_0=(3-N)[c_1-c_0],\qquad N=1+\delta+\delta^2,
$$
$$
q_C:J_X\twoheadrightarrow C,\qquad
\beta=q_C(D_0),\qquad F_0=\operatorname{End}_{\mathbf Q}^0(C).
\tag{1182.1}
$$

在 R1011 的范围

$$
p\ge10^{18},\ p\equiv5\pmod6,
\qquad\text{或}\qquad
p\ge431,\ p\equiv11\pmod{12},
\tag{1182.2}
$$

$C/\mathbf Q$ 简单，$F_0$ 全实，$\beta$ 非挠，且

$$
n:=\dim C=2f,\qquad f=[F_0:\mathbf Q],\qquad
C(\mathbf Q)\otimes\mathbf Q=F_0\beta.
\tag{1182.3}
$$

定义原 Abel 映射和原参数

$$
f_C(x)=q_C[x-c_1],\qquad t=b-1.
\tag{1182.4}
$$

$t$ 是 $c_1$ 的有理局部参数，$f_C(c_1)=0$，$f_C$ 非常值。所有局部盘均指经过这个指定 $c_1$ 的同一解析分支；不将其它点上具有同一 $b$ 值的分支并入。

## 2. 坏约化也适用的实际整数据

### 2.1 Néron 格与同一原点差的形式倍数

取 $C$ 在 $\mathbf Z_{(q)}$ 上的完整 Néron 模型 $\mathscr C$，并记

$$
\Lambda=\operatorname{Lie}(\mathscr C)\otimes\mathbf Z_q
\subset V_q,\qquad V=\operatorname{Lie}(C)(\mathbf Q).
\tag{1182.5}
$$

它是秩 $n$ 的格。选取 $\operatorname{Lie}(\mathscr C)$ 的 $\mathbf Z_{(q)}$-基 $L=(L_1,\ldots,L_n)$，所以 $L_i\in V$，且它们是 $\Lambda$ 的 $\mathbf Z_q$-基。对偶基给实际整不变微分 $\omega_1,\ldots,\omega_n$。

Néron 模型在坏约化处仍光滑、有限型，故其特殊纤维的点群 $\mathscr C(\mathbf F_q)$ 是有限群。取正整数 $M_0$ 杀掉 $\beta$ 的实际 reduction；例如可取这个完整有限群的指数。这里包括非单位分量及单位分量中的 toric、unipotent 部分，绝不把坏纤维当作好约化阿贝尔簇计数。于是

$$
M_0\beta\in\ker\bigl(\mathscr C(\mathbf Z_q)
\longrightarrow\mathscr C(\mathbf F_q)\bigr),
\qquad \log_q(M_0\beta)\in q\Lambda.
\tag{1182.6}
$$

最后一个整性可直接从形式群证明：整不变微分的径向积分中，第 $r$ 次齐次项的分母至多为 $r$；在形式坐标 $q\mathbf Z_q$ 上，每项的赋值至少 $r-v_q(r)\ge1$，并趋于无穷。由于 $q$ 为奇数，高次项比线性项有更高赋值，形式对数在这个邻域单射。

固定下文 Fuchs–Pham 所用的实际射影嵌入和基 $L$。令 $\Lambda_q^{\exp}$ 为其指数函数定义域，并选一个经该 chart 验证的整数 $s_{\exp}\ge1$，使

$$
q^{s_{\exp}}\Lambda\subset\Lambda_q^{\exp}.
\tag{1182.7}
$$

这样的整数可由原形式群和嵌入 chart 的有限方程给出。整不变向量场的指数在 $q\Lambda$ 收敛：第 $r$ 项具有分母 $r!$，而 $r-v_q(r!)\to\infty$；再增加深度，使嵌入 chart 中的各分母除以其原点值后属于 $1+q\mathbf Z_q$ 即可。不能省略 (1182.7)，仅以指数小球的形式半径代替实际 chart。

令 $\delta_L$ 是该文 §3.5 定义的 invariant-derivation 分母，$e_L=v_q(\delta_L)$。置

$$
s=\max\{s_{\exp},e_L+1\},\qquad
M=q^{s-1}M_0,\qquad \beta'=M\beta,\qquad u=\log_q\beta'.
\tag{1182.8}
$$

则 $u\in q^s\Lambda$，并满足

$$
u\in\Lambda_q^{\exp},\qquad
|u_i|_q<q^{-1/(q-1)}|\delta_L|_q,\qquad
\operatorname{Exp}(u)=\beta'\in C(\mathbf Q).
\tag{1182.9}
$$

这里 $s\ge e_L+1>e_L+1/(q-1)$。$\beta'$ 始终是原 $\beta$ 的已显示整数倍，不另选 Mordell–Weil 点或对数线。

### 2.2 原 Abel chart 的可验证缩盘

存在可由有限代数 chart 证书选定的整数 $a\ge0$，使代入

$$
t=q^a z
\tag{1182.10}
$$

后，同一分支上的 $f_C$ 给出到 Néron 单位形式邻域的整形式映射；其各形式坐标属于 $z\mathbf Z_q[[z]]$。这只要求 $X$ 和 $C$ 的泛纤维光滑，不假设 $X$ 或 $C$ 在 $q$ 好约化。

为说明 $a$ 不是一个未定的“充分深”，在 $c_1$ 处取有限方程

$$
\mathbf F(t,Y)=0,\qquad \mathbf F(0,0)=0,
\qquad J=\partial_Y\mathbf F(0,0)\in\operatorname{GL}_h(\mathbf Q).
$$

将 $J^{-1}\mathbf F$ 写成 $Y+R(t,Y)$，其中 $R$ 没有纯一次 $Y$ 项。选整数 $b_0,a\ge0$，使有限表达式

$$
q^{-b_0}J^{-1}\mathbf F(q^a z,q^{b_0}Z)=Z+Q(z,Z)
\tag{1182.11}
$$

满足：$Q$ 的系数整；所有含 $Z$ 的单项式系数被 $q$ 整除；$Q(z,0)\in z\mathbf Z_q[z]$。具体对每项 $c_{r,\alpha}t^rY^\alpha$，只须检查有限个不等式

$$
v_q(c_{r,\alpha})+ra+(|\alpha|-1)b_0\ge0,
$$

并在 $|\alpha|\ge1$ 时将右端改为 $1$。先加大 $b_0$ 处理 $r=0,|\alpha|\ge2$，再加大 $a$ 即可。Hensel 迭代 $Z\mapsto-Q(z,Z)$ 给出唯一的 $Z\in z\mathbf Z_q[[z]]$，其泛纤维就是原分支。

同时取一个包含 Néron 单位截面的实际光滑 affine chart，将其全部有限代数生成元减去截面值，并将它们的拉回写成在 $(0,0)$ 无极的有理函数；也保留选定 étale chart 的可逆 Jacobian minor。继续增大 $b_0,a$，使分子整且常数项为零、分母除以原点值后属于 $1+(z,Z)\mathbf Z_q[[z,Z]]$。代入上面的解后，这些函数及形式坐标均属 $z\mathbf Z_q[[z]]$。因此所得点确实落在单位点的那张 étale sheet，而不是只与它具有相同的一组坐标值。所有条件仍是有限个系数赋值检查。所选 $a$ 及其 chart 证书是本定理保留的原模型数据；本篇不执行这个计算。

因此写

$$
U(z)=\log_q f_C(x(q^az))=\sum_{r\ge m}U_rz^r,
\qquad U_r\in V,\quad U_m\ne0,
\tag{1182.12}
$$

就有全部系数的严格整界

$$
\boxed{\quad rU_r\in\Lambda\quad(r\ge1).\quad}
\tag{1182.13}
$$

确实，$dU$ 是整不变微分的实际拉回，所以其第 $r-1$ 次系数就是 $rU_r$。全部 $U_r$ 有理，来自原有理参数、原有理映射及有理基 $L$，不是任意 $q$-adic 标架中的系数。

首阶 $m$ 可在有限有理 jet 中确定。若 $g_X=g(X)$，则

$$
1\le m\le 2(g_X-n)+1.
\tag{1182.14}
$$

这是 R682 的 Clifford 论证在本篇实际 $n$ 维商上的应用：$f_C^*H^0(C,\Omega^1)$ 维数为 $n$，所有元素在 $c_1$ 至少消失 $m-1$ 阶；对 $K_X-(m-1)c_1$ 用 Clifford 即得。参数缩放不改变 $m$。本篇不重复登记该一般阶数界，也不将它改写成 $m=1$。

## 3. 同一 $\beta$ 的两列与固定有理线性形式

$V$ 在 $F_0$ 上维数为二。固定一个有理 $F_0$-基，并记相应行列式为 $\det_{F_0}$。取正整数 $D$ 使

$$
\Omega(v,w)=D\operatorname{Tr}_{F_0/\mathbf Q}
                 \det_{F_0}(v,w),\qquad
\Omega(\Lambda,\Lambda)\subset\mathbf Z_q.
\tag{1182.15}
$$

可以从 $L$ 基中的有理矩阵直接选取 $D$；必要时只乘一个 $q$ 的幂。$D$ 与所选商的同源分母都保留在后续高度数据中，不声称这个交错型是本原或完美整型。

$\Omega$ 非退化、交错，并满足真实 $F_0$-平衡关系

$$
\Omega(cv,w)=\Omega(v,cw)\qquad(c\in F_0).
\tag{1182.16}
$$

非退化性来自二维行列式与数域迹配对的非退化性。定义

$$
\lambda_{\beta'}(w)=\Omega(u,w),\qquad
F(z)=\lambda_{\beta'}(U(z))=\sum_{r\ge m}a_rz^r.
\tag{1182.17}
$$

因为 $u\in\Lambda$，$\lambda_{\beta'}$ 是整泛函。由 (1182.3)、(1182.16)，它杀掉全部真实 Mordell–Weil 对数：

$$
\lambda_{\beta'}\bigl((F_0\otimes\mathbf Q_q)u\bigr)=0.
\tag{1182.18}
$$

若在同一 $F_0$-基中写 $u=(u^{(1)},u^{(2)})$、$U=(U^{(1)},U^{(2)})$，则本函数准确为

$$
F(z)=D\operatorname{Tr}_{F_0\otimes\mathbf Q_q/\mathbf Q_q}
\bigl(u^{(1)}U^{(2)}(z)-u^{(2)}U^{(1)}(z)\bigr).
\tag{1182.19}
$$

这两列由同一实际 $\beta'$ 和同一 Abel 映射取得。没有用另一独立点的 Coleman 对数，亦未替换成未知比例的晶体列。

首项应改写为

$$
a_m=\ell_m(u),\qquad
\ell_m(v):=\Omega(v,U_m)\in V^*,\quad \ell_m\ne0.
\tag{1182.20}
$$

这里 $\ell_m$ 的系数是有理数，因 $U_m\in V$ 且 $\Omega$ 有理。$\lambda_{\beta'}$ 的系数一般只是 $q$-adic 数，**本篇从不将 $\lambda_{\beta'}$ 送入代数系数的线性形式定理**。

由 R1011 §6 的指定点版本解析子群定理，$a_m\ne0$：若零，则 $u$ 落入真有理超平面 $\ker\ell_m$，而非挠有理点 $\beta'$ 的循环子群在 $C$ 中 Zariski 稠密。

## 4. 数值线性形式定理的半稳定前提

下列论证单独处理 $\mathbf Q$-单与几何单的区别。

**引理 1182.1。** 若 $C/\mathbf Q$ 简单，$W\subsetneq V$ 是有理超平面，则 $(C,W)$ 满足 Fuchs–Pham §3.3 在 $\overline{\mathbf Q}$ 上的半稳定条件。

**证明。** 先设一个正维几何阿贝尔子簇 $H\subset C_{\overline{\mathbf Q}}$ 满足 $\operatorname{Lie}H\subset W_{\overline{\mathbf Q}}$。因为 $W$ 在 $\mathbf Q$ 上定义，每个 Galois 共轭 $H^\sigma$ 的 Lie 代数仍包含在同一个 $W_{\overline{\mathbf Q}}$。取一个定义 $H$ 的有限 Galois 域，所有共轭之和是非零、在 $\mathbf Q$ 上定义的阿贝尔子簇。$C/\mathbf Q$ 简单迫使这个和等于 $C$；特征零中其 Lie 代数是各 $\operatorname{Lie}H^\sigma$ 的和，仍包含在 $W$，矛盾。

现在取任意几何商 $\pi:C_{\overline{\mathbf Q}}\twoheadrightarrow B$。若其核的单位分量 $H$ 正维，刚才的结论给 $W+\operatorname{Lie}H=V$，于是 $\pi_*W=\operatorname{Lie}B$。因此在 $\dim B>0$ 时

$$
\frac{\dim W}{\dim C}=\frac{n-1}{n}
\le1=\frac{\dim\pi_*W}{\dim B}.
\tag{1182.21}
$$

若核有限，两个比值相等；零维商按该文定义其比值为一。所有商的量词都已覆盖。证毕。

这里对共轭取**和**合法，关键是 $W$ 自身有理。它与 R682 在任意代数超平面下、利用指定有理点而对共轭子群取**交**的证明不同，不能互相省略前提。半稳定在此指线性形式定理的 quotient 比值条件，与 $C$ 在 $q$ 是否半稳定约化无关。

阿贝尔簇与 $\mathbf G_a$ 的 disjointness 是同文 Lemma 3.5 的直接情形。故可对 $G=C$、$K=\mathbf Q$、$W=\ker\ell_m$ 使用其 Theorem 2.1。

## 5. 原整首项的有效上估值

在 $L$ 基中，将 $\ell_m$ 乘以最小正整数 $E_m$ 清除有理分母，写

$$
E_m\ell_m(Z)=c_1Z_1+\cdots+c_nZ_n,
\qquad c_i\in\mathbf Z,\quad(c_1,\ldots,c_n)\ne0.
\tag{1182.22}
$$

下标 $c_i$ 在本节仅表示线性形式的整数系数，与原 CM 点符号不同。由 (1182.13)、(1182.15)，还有

$$
v_q(E_m)\le v_q(m).
\tag{1182.23}
$$

取乘法 Weil 高度 $H$，在固定的实际射影嵌入中定义

$$
\mathsf b=\log\max\{3,H(c_1),\ldots,H(c_n)\},\qquad
\mathsf h=\log\max\{3,H(\beta')\}.
\tag{1182.24}
$$

为了把群与基的依赖写全，按 Fuchs–Pham §3.5 记 $d_L$ 为不变微分算子的坐标多项式最大次数，$h_L$ 为这些多项式的最大对数高度，$e_L=v_q(\delta_L)$。可使用其参数的显式上界

$$
\mathsf W_L=1+\max\{1,e_L\}
\bigl(h_L+\log\delta_L+\log\max\{1,d_L\}\bigr).
\tag{1182.25}
$$

由 Theorem 2.1 第一部分和已验证的 (1182.9)、引理 1182.1，存在该定理提供的有效常数 $c_{\rm FP}>0$，只依赖实际群、嵌入及基，而不依赖 $\mathsf b,\mathsf h,q$，使

$$
v_q(E_m a_m)
<c_{\rm FP}\mathsf W_L^{\,n+3}\mathsf b\mathsf h^{n}
\bigl(\log\mathsf b+\log\mathsf h\bigr)^{n+3}.
\tag{1182.26}
$$

这一步直接将该文的 $\log|\cdot|_q$ 下界除以 $\log q$；没有多留或漏掉一个 $\log q$。

取一个可计算整数 $\mathcal B\ge1$，严格大于 (1182.26) 的右侧。计算实数时只需取有证上界，不须决定任何实数是否恰为整数。于是

$$
\boxed{\quad
-v_q(m)\le v_q(a_m)<\mathcal B-v_q(E_m)\le\mathcal B.
\quad}
\tag{1182.27}
$$

左端来自 $mU_m\in\Lambda$ 及 $u,\Omega$ 的实际整性；右端是新获得的有效上估值。它不把原首项宣为单位。

$c_{\rm FP}$ 对固定模型不含未知 $q$-adic 调节子，但原商 $C$ 随 level $p$ 改变，因此不能把它称为对所有 $p$ 的一个已知绝对常数。$M,D,E_m$ 及其对高度的影响均已写入，尤其没有将同源分母或将 $\beta$ 移入形式邻域的成本删去。

## 6. 全部尾项与一个真正的完整盘

由 (1182.13)、(1182.15)、$u\in\Lambda$，对每个 $r\ge1$ 都有

$$
v_q(a_r)\ge-v_q(r).
\tag{1182.28}
$$

这是一条对全部系数的界，故 $F(z)$ 在 $v_q(z)>0$ 收敛。定义整数

$$
\ell_q(m)=\min\{j\in\mathbf Z_{\ge0}:q^j\ge m+1\},
\qquad H_q=\mathcal B+\ell_q(m).
\tag{1182.29}
$$

**定理 1182.2。** 对同一原分支中满足

$$
0\ne t=b-1,\qquad v_q(t)\ge a+H_q
\tag{1182.30}
$$

的任意 $\mathbf Q_q$ 点，均有

$$
F(t/q^a)\ne0,\qquad
v_q(F(t/q^a))=v_q(a_m)+m\bigl(v_q(t)-a\bigr).
\tag{1182.31}
$$

因此在这个完整圆盘内，原 $X_1(\mathbf Q)$ 的点只有 $c_1$。

**证明。** 令 $z=t/q^a$、$s_z=v_q(z)\ge H_q$。对任意 $k\ge1$，初等不等式

$$
m+k\le(m+1)^k
$$

给 $v_q(m+k)\le k\ell_q(m)$。所以每个高次项相对于首项的赋值差至少为

$$
\begin{aligned}
v_q(a_{m+k}z^{m+k})-v_q(a_mz^m)
&\ge ks_z-v_q(m+k)-v_q(a_m)\\
&\ge k\mathcal B-v_q(a_m)>0.
\end{aligned}
\tag{1182.32}
$$

首项是完整收敛和中唯一具有最小赋值的项，故 (1182.31) 成立；这里没有截去任何尾项。若 $x$ 有理，则 $f_C(x)\in C(\mathbf Q)$，由 (1182.18) 又有 $F(z)=0$，矛盾。$t=0$ 在所选分支就是原 $c_1$。证毕。

若需要使用未乘 $M$ 的原 $\beta$，则相应函数恰为 $F/M$，首项和全部尾项的赋值同时减 $v_q(M)$；零集与半径 (1182.30) 不变。形式倍数没有换掉原 Mordell–Weil 方向。

## 7. 有限输入、已消掉的未知量和剩余 O4 门

本篇的界需要以下实际有限数据：原 $q_C$ 和 $\beta$ 的代数表达；一个实际 Néron 单位 chart 与有理整 Lie 基；原 Abel 分支的 Hensel 证书及 $a$；固定射影嵌入和指数 chart 深度；$F_0$-基与交错型整化因子；原点的 reduction 倍数；至 (1182.14) 为止的有理 jet 与所涉及的代数高度。给定这些数据，$\mathcal B$ 和 $a+H_q$ 不再包含一个待测的首项估值或调节子。

其中 Néron 图表和同源模型是结论的明示输入。本篇不声称 R1011 的存在性证明已经提供了这些数据的统一小高度表达，也没有执行 Néron 模型、点群或 jet 的数学计算。

取 $q=p$ 时，原 level 坏素数仍在本定理范围内。得到的是一个依赖实际高度的有效深盘，不是旧 first-layer 条件的重复；但下列两项仍须继续：

1. 将上述代数模型与高度量在原模曲线族中统一控制，并与原候选实际达到的深度比较。只有证明候选落入 (1182.30)，才能据本篇将整个该候选支路排除。
2. 若改用 R1035–R1036 的实际最低型整列而求更短半径，仍须支付它与本篇所选 $C$ 的 Néron 格及同一 $\beta$ 的确切尺度。本篇没有从饱和总商的本原性反推每个简单商的首项单位。

原 $X_d$ 的其它扭曲、其它 CM 点域、非 $p$ 条件、全局覆盖及真实高度项 $\eta_h$ 继续按原 O4/O0 范围保留。全 Serre 一致性结论仍未完成。

## 8. 精确来源与证明范围

1. Clemens Fuchs and Duc Hiep Pham, *Commutative algebraic groups and p-adic linear forms*, **Acta Arithmetica 169.2 (2015), 115–147**, DOI [10.4064/aa169-2-2](https://doi.org/10.4064/aa169-2-2)。已亲读 [正式 PDF](https://www.impan.pl/shop/publication/transaction/download/product/82995)：Theorem 2.1 在印刷 pp.118–119（PDF 第4–5页）；disjointness 为 Lemma 3.5，p.122；半稳定的全部 quotient 定义在 §3.3，pp.122–123；$\delta_L,d_L,h_L,\omega_L$ 在 §3.5，pp.125–127。本文只用第一种小球估值，不省略 $\Lambda_q^{\exp}$，也不直接使用其任意小球变体。
2. Siegfried Bosch, Werner Lütkebohmert and Michel Raynaud, *Néron Models*, Springer, 1990，§1.3, Corollary 2 的阿贝尔簇有限型 Néron 模型；可对照已实读的 Brian Conrad, *Minimal models for elliptic curves*, 2015，§5, Definition 5.1 与 Theorem 5.2，[作者 PDF](https://math.stanford.edu/~conrad/papers/minimalmodel.pdf)，印刷 p.13。该节的存在性定理针对一般阿贝尔簇，本文未将它限制为好约化或椭圆曲线。
3. [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md) 支付同一个原 $C,F_0,\beta$、半秩及指定点解析子群输入；[R682](R682-common-CM-Abel-order-and-saturated-QC-jets.md) 的一般 Clifford 阶数论证仅按本篇实际维数使用。没有搬用 R682 另一 CM/GL2 型商的条件性非消失前提。

本篇的平衡交错型、几何半稳定的有理超平面下降、有限 Hensel 缩盘证书和全部尾项比较均在正文给出证明。没有执行数学程序，没有重算旧有限窗口。

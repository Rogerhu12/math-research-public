# R145：多模式真实 Bell 修正、全部混合幂域与第一阶算子乘积的循环性

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。

状态：完整证明。R125 提供各个第一阶闭乘子，R132 提供在已知定义域上的循环性传递；本文补足多模式共同定义域、任意混合顺序及重叠支持的真实 Bell 恒等式。它们并非从两个旧结果自动得到。

## 1. 定理与边界

固定有限个第一 chaos 向量

$$
u_\nu=c_\nu+\sum_{j\ge0}a_{\nu j}\chi_j,
\qquad a_\nu\in\ell^2,\qquad 1\le\nu\le d,
$$

系数任意复数，支持允许任意重叠。令 $X_\nu=X_{u_\nu}$ 为 R125 的实际闭乘子，并令

$$
u_{\nu,N}=c_\nu+\sum_{j<N}a_{\nu j}\chi_j,
\qquad X_{\nu,N}=c_\nu I+\sum_{j<N}a_{\nu j}V_j.
$$

对多重指标 $\alpha\in\mathbb N_0^d$，置

$$
v_{\alpha,N}=\prod_{\nu=1}^dX_{\nu,N}^{\alpha_\nu}1.
$$

有限截断交换，所以这里没有顺序歧义。

**主定理。** 对每个 $\alpha$，$v_{\alpha,N}$ 在 $H$ 中强收敛到 $v_\alpha$。这些向量满足

$$
v_0=1,\qquad v_{e_\nu}=u_\nu,
\qquad
\boxed{v_\alpha\in\operatorname{Dom}X_\nu,\quad
X_\nu v_\alpha=v_{\alpha+e_\nu}\quad(\alpha,\nu).}
\tag{1.1}
$$

因此 $1$ 属于任意有限混合自然乘积的定义域，且所得向量只依赖各模式的出现次数，与施加顺序无关。

存在有界交换子 $B_\beta\in\mathcal A$，其中 $B_0=I$、$B_{e_\nu}=0$，使全部点态混合单项式满足

$$
\boxed{
u^\alpha:=\prod_\nu u_\nu^{\alpha_\nu}
=\sum_{\beta\le\alpha}\binom\alpha\beta B_\beta v_{\alpha-\beta}.
}
\tag{1.2}
$$

各点态乘积属于 $H$。当所施加的每个第一阶因子均非零时，其混合算子乘积作用于 $1$ 后得到循环向量，允许任意重叠支持。

本定理只断言这些指定向量及下文共同核心上的混合顺序相等，没有自动证明不同无界乘积的最大定义域相同、乘积自动闭或任意多变量多项式向量循环。

## 2. 有限参数的算子值整生成函数

令 $t=(t_1,\ldots,t_d)\in\mathbb C^d$，并写

$$
\ell_j(t)=\sum_{\nu=1}^dt_\nu a_{\nu j},\qquad
c(t)=\sum_\nu t_\nu c_\nu.
$$

有限生成函数定义为

$$
\mathcal B_N(t)=\prod_{j<N}
H(\ell_j(t),V_j),
\qquad
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z).
\tag{2.1}
$$

所有因子属于 $\mathcal A$，彼此交换。使用统一界 $\|V_j\|\le M$。有

$$
H(0,V)=I,\quad H'(0,V)=0,
\quad H'(z,V)=e^{-zV}(I-V^2)\sinh z,
$$

所以

$$
\|H(z,V)-I\|
\le\tfrac12(M+1)^3|z|^2e^{(M+1)|z|}.
\tag{2.2}
$$

记 $A_2^2=\sum_\nu\|a_\nu\|_2^2$。对 $\|t\|_2\le T$，

$$
\sum_j|\ell_j(t)|^2\le T^2A_2^2,
\qquad\sup_j|\ell_j(t)|\le TA_2,
$$

且尾平方和由 $T^2\sum_\nu\sum_{j\ge N}|a_{\nu j}|^2$ 一致控制。因此 (2.2) 与有限乘积望远镜式证明

$$
\mathcal B_N(t)\longrightarrow\mathcal B(t)
$$

在每个参数紧集上一致按算子范数收敛。$\mathcal B$ 是 $\mathcal A$ 值整函数。

采用未除阶乘的导数记号

$$
B_{\beta,N}=\partial^\beta\mathcal B_N(0),\qquad
B_\beta=\partial^\beta\mathcal B(0).
$$

多变量 Cauchy 积分给

$$
B_{\beta,N}\to B_\beta\quad\text{于算子范数}.
\tag{2.3}
$$

由一阶消去，$B_0=I$、$B_{e_\nu}=0$。
又 $\chi(V_j)=1$，每个有限乘积的字符都是1；因此

$$
\chi(\mathcal B(t))=1,\qquad
\chi(B_\beta)=0\quad(|\beta|\ge1).
\tag{2.4}
$$

所以非恒定修正系数均属于 $\mathcal A$ 的根基。$\mathcal B(t)$ 对每个 $t$ 是 $\mathcal A$ 内单位，其逆也是整函数；这里使用了 $\mathcal A$ 的唯一角色及零字符根基结构。

## 3. 有限真恒等式及混合 Bell 递推

有限截断的准确算子恒等式为

$$
e^{\sum_\nu t_\nu X_{\nu,N}}\mathcal B_N(t)
=e^{c(t)}\prod_{j<N}
\bigl(\cosh\ell_j(t)I+V_j\sinh\ell_j(t)\bigr).
$$

不同位的乘积作用于 $1$ 满足 $V_F1=\chi_F$。所以

$$
\boxed{
e^{\sum_\nu t_\nu u_{\nu,N}}
=\mathcal B_N(t)e^{\sum_\nu t_\nu X_{\nu,N}}1.
}
\tag{3.1}
$$

它只对有限截断使用真实的不同位恒等式，没有把一般实际乘子与点乘混为一谈。

对多重指标 $\alpha$ 微分并取 $t=0$，得到

$$
u_N^\alpha
=\sum_{\beta\le\alpha}\binom\alpha\beta
B_{\beta,N}v_{\alpha-\beta,N}.
\tag{3.2}
$$

由于 $B_{0,N}=I$，可解出三角递推

$$
v_{\alpha,N}
=u_N^\alpha-
\sum_{0\ne\beta\le\alpha}\binom\alpha\beta
B_{\beta,N}v_{\alpha-\beta,N}.
\tag{3.3}
$$

这一步的全部算子都是有界有限截断，故没有混合无界定义域问题。

## 4. 点态混合矩及所有混合幂向量的强极限

对任意有限复 Rademacher 和，有

$$
\mathbb E\left|\sum_jb_j\chi_j\right|^{2r}
\le\frac{(2r)!}{2^rr!}
\left(\sum_j|b_j|^2\right)^r.
\tag{4.1}
$$

直接证明是展开后只保留每个指标出现偶数次的项，取绝对值后以正实系数和的同阶矩控制，再逐系数使用
$\cosh(tx)\preceq e^{t^2x^2/2}$。

将 (4.1) 用于每个模式的系数尾，得 $u_{\nu,N}\to u_\nu$ 于每个有限 $L^{2r}$，且范数一致有界。对 $|\alpha|=r$，逐因子望远镜和 Hölder 给

$$
u_N^\alpha\longrightarrow u^\alpha\quad\text{于 }H.
\tag{4.2}
$$

这里不使用模式之间的独立性；它们可以共享全部物理位。

由 (2.3)、(4.2) 和 (3.3)，按总次数 $|\alpha|$ 归纳，每个 $v_{\alpha,N}$ 都在 $H$ 中强收敛。记其极限为 $v_\alpha$。每个递推余项只涉及更低总次数，故这个归纳没有循环。
对 (3.2) 取极限，得到 (1.2)。

到此仅构造了强极限；下一节才把它们识别为实际闭算子的混合自然乘积。

## 5. 伴随图核心逐个识别全部混合定义域

固定模式 $\nu$。R125 给有限柱是 $X_\nu^*$ 的图核心，并且对每个有限柱 $z$，

$$
X_{\nu,N}^*z\longrightarrow X_\nu^*z.
$$

有限乘子交换，所以对任意 $\alpha$，

$$
v_{\alpha+e_\nu,N}=X_{\nu,N}v_{\alpha,N}.
$$

配对并取极限，得到

$$
\begin{aligned}
\langle v_{\alpha+e_\nu},z\rangle
&=\lim_N\langle X_{\nu,N}v_{\alpha,N},z\rangle\\
&=\lim_N\langle v_{\alpha,N},X_{\nu,N}^*z\rangle
=\langle v_\alpha,X_\nu^*z\rangle.
\end{aligned}
\tag{5.1}
$$

有限柱是伴随图核心，所以此式延拓到全部 $\operatorname{Dom}X_\nu^*$。左侧由通常范数有界的向量泛函表示，因此

$$
v_\alpha\in\operatorname{Dom}(X_\nu^*)^*
=\operatorname{Dom}X_\nu,
\qquad X_\nu v_\alpha=v_{\alpha+e_\nu}.
$$

这证明 (1.1)。特别地，$v_\alpha$ 本身不必仍是有限 chaos；论证未以这个错误的域替代来继续迭代。

给任意有限词 $\nu_1,\ldots,\nu_r$，从 $1=v_0$ 开始反复使用 (1.1)，每一步都有正确的下一因子定义域，且

$$
X_{\nu_r}\cdots X_{\nu_1}1
=v_{e_{\nu_1}+\cdots+e_{\nu_r}}.
\tag{5.2}
$$

因此指定的自然乘积在 $1$ 上可定义，且与顺序无关。

### 5.1 一个显式的共同不变图核心

定义

$$
\mathcal E=\operatorname{span}
\{Dv_\alpha:D\in\{A\}',\ \alpha\in\mathbb N_0^d\}.
\tag{5.3}
$$

R125 的全部有界交换子域交换给

$$
X_\nu Dv_\alpha=Dv_{\alpha+e_\nu}.
$$

故 $\mathcal E$ 包含于全部 $X_\nu$ 的定义域，被每个 $X_\nu$ 保持，且这些闭乘子在 $\mathcal E$ 上代数交换。$\mathcal E$ 含所有有限柱，因为有限柱 $u$ 可写成 $D1$、$D\in\mathcal A$。所以它对每个 $X_\nu$ 都是图核心，也在 $H$ 中稠密。

这里没有把共同核心上的交换提升成未经证明的最大混合域相等或闭乘积的强交换。

## 6. 所有非零第一阶因子的算子乘积作用于1都循环

设所使用的每个第一阶向量非零。R125 使对应 $X_\nu$ 单射。R132 的有界正则化定理又说明：若 $x$ 循环且 $x\in\operatorname{Dom}X_\nu$，则 $X_\nu x$ 循环。

从循环向量 $1$ 出发，(5.2) 已逐步核验所有下一因子的定义域。因此每个有限词都有

$$
\boxed{X_{\nu_r}\cdots X_{\nu_1}1\text{ 非零且对 }A\text{ 循环}.}
\tag{6.1}
$$

不要求任何两个系数支持不交，也不要求相位、绝对可和或特定尾速度。
非零常数因子对应非零标量算子，同样适用；零第一阶因子当然必须排除。

### 6.1 单一模式的全部算子多项式

若 $u$ 非常数，则每个 $X_u-\lambda I=X_{u-\lambda}$ 都是非零第一阶闭乘子。把任意非零标量多项式因式分解，结合全部幂域，可得

$$
q(X_u)1\text{ 对 }A\text{ 循环}
\quad(q\ne0).
\tag{6.2}
$$

根可以重复；这里是算子多项式，不是未经 Bell 修正的点态 $q(u)$。
若 $u=c$ 是常数，则 $q(X_u)1=q(c)1$，恰在 $q(c)\ne0$ 时循环。

更一般地，任意有限个非零第一阶仿射线性组合都可作为新的有限模式族重新应用 (6.1)。因此可分解为这类非零仿射线性因子的多变量算子多项式作用于 $1$ 也循环。

这与原模式的多项式展开准确一致：若 $P(z)=\prod_r\ell_r(z)$，其中
$\ell_r$ 为仿射线性式，先在有限截断上用
$X_{\ell_r(u),N}=\ell_r(X_{1,N},\ldots,X_{d,N})$。有限乘积作用于1等于
$P(X_{1,N},\ldots,X_{d,N})1$。左侧由新有限模式族的定理强收敛，右侧由有限个 $v_{\alpha,N}$ 的强收敛趋于 $P(v):=\sum_\alpha P_\alpha v_\alpha$，两者相等。本文未由此覆盖任意不可约多变量多项式。

## 7. 重叠支持的明确修正与一个必要区别

由 $H'(0,V)=0$、$H''(0,V)=I-V^2$，二阶混合修正为

$$
\boxed{
B_{e_\mu+e_\nu}
=\sum_{j\ge0}a_{\mu j}a_{\nu j}(I-V_j^2).
}
\tag{7.1}
$$

当 $\mu=\nu$ 时左侧理解为 $B_{2e_\nu}$。此和按算子范数绝对收敛，因为
$\sum_j|a_{\mu j}a_{\nu j}|\le\|a_\mu\|_2\|a_\nu\|_2$，且 $V_j$ 一致有界。没有复共轭：这是解析混合导数。

因此

$$
u_\mu u_\nu=X_\mu X_\nu1+B_{e_\mu+e_\nu}1.
\tag{7.2}
$$

若 $u_1=1+\chi_j$、$u_2=1-\chi_j$，两个因子均非零，但点态乘积为零。实际算子乘积却是

$$
(I+V_j)(I-V_j)1
=(I-V_j^2)1
=4N_j(I+N_j)^{-2}1,
\tag{7.3}
$$

它非零且循环。式 (7.1) 此时恰给补偿项 $-(I-V_j^2)$。所以不能把 (6.1) 直接写成任意重叠支持的点态乘积循环。

反之，若各模式的物理位支持两两不交，则
$\mathcal B(t)=\prod_\nu\mathcal B^{(\nu)}(t_\nu)$，每个单变量因子的线性导数为零。对每个 $\alpha_\nu\in\{0,1\}$，(1.2) 的所有非零修正均消失。因此

$$
\prod_{\nu=1}^du_\nu=X_d\cdots X_1 1,
$$

恢复 R132 的独立位点态乘积定理。重复使用同一模式时通常仍有高阶修正。

## 8. 补充：一个真正的多模式整真空轨道

上述构造还给出有用的联合域向量，而不是全空间有界指数算子。

点态函数

$$
\mathcal U(t)=e^{\sum_\nu t_\nu u_\nu}
$$

是 $H$ 值整函数，且其有限系数版本在参数紧集上一致 $H$ 收敛。可用 (4.1) 直接证明：在 $\|t\|_2\le T$ 上，若 $Z_N(t)=\sum_\nu t_\nu u_{\nu,N}$，则对固定常数 $C,A$ 有

$$
\|Z_N(t)^r\|_2
\le[T(C+\sqrt{2r}\,A)]^r.
$$

除以 $r!$ 后的级数对所有有限 $T$ 可和，且与 $N$ 无关。每个固定次幂由 §4 在紧集上一致收敛，所以指数幂级数也一致收敛。其 $H$ 极限等于点态指数，可由幂级数部分和的几乎处处收敛及一个 $H$ 收敛子列识别。

由 (2.4)，$\mathcal B(t)^{-1}$ 是 $\mathcal A$ 值整函数。定义

$$
\mathcal V(t)=\mathcal B(t)^{-1}\mathcal U(t).
\tag{8.1}
$$

有限版本 $\mathcal B_N(t)^{-1}$ 也在紧集上一致趋于 $\mathcal B(t)^{-1}$：紧集上的逆范数有界，再对
$\mathcal B_N\mathcal B^{-1}-I$ 使用一致 Neumann 界即可。故 (3.1) 给

$$
e^{\sum_\nu t_\nu X_{\nu,N}}1\longrightarrow\mathcal V(t)
$$

紧集一致强收敛。其混合导数正好是 $v_\alpha$，所以

$$
\mathcal V(t)=\sum_\alpha\frac{t^\alpha}{\alpha!}v_\alpha.
\tag{8.2}
$$

此 $H$ 值 Taylor 级数及各固定混合导数在紧集上一致绝对收敛。对有限 Taylor 部分逐项用 (1.1)，再用 $X_\nu$ 的闭性，得到

$$
\boxed{\mathcal V(t)\in\operatorname{Dom}X_\nu,
\qquad X_\nu\mathcal V(t)=\partial_{t_\nu}\mathcal V(t).}
\tag{8.3}
$$

反复使用同一论证，$\mathcal V(t)$ 属于全部混合词的自然定义域，相应像是混合偏导。

本节只构造一个共同整向量轨道及其导数，没有定义全 $H$ 上有界的 $e^{\sum t_\nu X_\nu}$，也没有通过循环向量序列取极限来宣称额外循环性。

## 9. 与既有结果的关系

R125 给各个 $X_\nu$ 的闭性、$C$ 自伴和伴随图核心；它没有单独保证 $X_\mu X_\nu1$ 的后续所有混合域。R132 的循环性传递明确以输入已在定义域为前提；不能略去这个前提直接迭代。R134 解决一个模式的所有幂域，但一个模式的域结论不能未经混合参数分析就替换成任意多个不同闭算子的域结论。

本文新增的是 §2–5 的混合强极限与真实域网格、共同不变图核心，以及 §7 的重叠 Bell 修正。循环性结论在这些域步骤完成后，再明确复用 R132；一模式 (6.2) 是旧幂域加传递的直接推论，已合并在此而未当作独立突破。

依赖文件：

- [R125：全部第一 chaos 闭乘子](2026-11-12-all-l2-first-chaos-closed-multiplier-cyclicity-0c.md)。
- [R132：有界正则化传递循环性](2026-11-12-independent-first-chaos-products-0c-agent.md)。
- [R134：单模式幂域与生成函数](2026-11-12-empty-spectrum-first-chaos-polynomial-cyclicity-0c-agent.md)。

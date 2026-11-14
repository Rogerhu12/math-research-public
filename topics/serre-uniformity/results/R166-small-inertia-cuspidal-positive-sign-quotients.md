# R166：小惯性分支中来自深度零尖点型的实际正根数商

日期：2026-11-12。

**状态：已证明的实际商结构；未证明这些商的中心值非零或有理点有限。**
本文在 R66 的小惯性分支中，构造与 R69 的三次 Steinberg 商不同的一族实际阿贝尔簇商。其每个不可约兼容系统因子的中心根数为 $+1$。这消除了“除三次 Steinberg 外没有正号候选”的可能误解；它不消除 R122 的三色共同零点，不从正根数推出秩零，也不把 Studnia 的博士论文或 submitted 文稿当作已发表证明输入。

## 1. 设置与准确结论

设 $E/\mathbb Q$ 是实际异常椭圆曲线，$p>37$，并保留 R1、R5、R66 的完整像与小惯性假设
$$
 r=\rho_{E,p}:G_{\mathbb Q}\twoheadrightarrow
 N=C\rtimes\langle\tau\rangle,\qquad
 C=\mathbb F_{p^2}^{\times},\qquad r(I_p)=C^3.
\tag{166.1}
$$
令 $K$ 为正规化子二次商域，$\lambda=r|G_K$。R66 已独立证明
$$
 K\text{ 虚二次},\quad p\text{ 在 }K\text{ 惰性},\quad
 p\equiv2,5\pmod9,
 \quad v_3(p+1)=1.
\tag{166.2}
$$
置
$$
 d=(p+1)/3,
$$
并取阶恰为 $3$ 的复字符 $\vartheta:C\to\mu_3$。这里 $\vartheta$ 是有限 Cartan 字符；R66 的全局三次字符是 $\vartheta\circ\lambda$。

**定理 166.1。** 对每个 Weil 配对乘子 $\alpha\in\mathbb F_p^\times$，实际几何连通曲线 $X_E^\alpha(p)$ 的 Jacobian 都有一个非零、定义于 $\mathbb Q$ 的阿贝尔簇商 $B_\alpha$，其 Tate 模的不可约兼容系统因子属于下述集合及其完整系数 Galois 轨道：
$$
 V_f\otimes\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\Xi_+,
 \qquad
 V_f\otimes\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\Xi_-.
\tag{166.3}
$$
这里：

- $f$ 是平凡 nebentype、权二、水平 $p^2$ 的非 CM 新形式；它的 $p$ 处是深度零 supercuspidal，有限尖点参数为 $\{\theta,\theta^p\}$，且 $\theta$ 阶恰为 $d$。
- $\theta$ 在 $\mathbb F_p^\times$ 上平凡；
  $$\varphi_+=\theta\vartheta,\qquad
    \varphi_-=\theta\vartheta^{-1},\qquad
    \Xi_\pm=\varphi_\pm\circ\lambda.$$
- 每个 $\Xi_\pm$ 都是阶恰为 $p+1$ 的有限阶 Hecke 字符，在有理 idèle 上平凡；它在 $p$ 上方的导子指数恰为 $1$。相应二维 Artin 表示在 $p$ 的导子指数为 $2$。
- (166.3) 中每个四维表示绝对不可约，其完整 $L$ 函数在中心全纯，且
  $$
  \boxed{\epsilon\!\left(\tfrac12,\pi_{f,K}\otimes\Xi_\pm\right)=+1.}
  \tag{166.4}
  $$

至少一个这样的 $f$ 对每个满足 (166.1) 的 $p$ 都存在。可以同时保留所有这样的完整 Galois 轨道；本文不把不同 $f$ 的 Dirichlet 扭曲等价重复计数，也不给未经去重的维数公式。

本文用酉自守中心 $1/2$；在 $V_f$ 的椭圆曲线归一化中中心为 $s=1$。

## 2. 非空性来自原本几何连通的 $X_{\mathrm{ns}}^+(p)$

R64 定理 1 的全局惯性阶幂等元 $e_d$ 作用在
$$J_{\mathrm{ns}}^+(p)=\operatorname{Jac}(X_{\mathrm{ns}}^+(p))$$
上。这里是原来的几何连通非分裂正规化子曲线，并非全水平不连通曲线中的额外分支。

因为 $v_3(p+1)=1$，有
$$
 (d,3)=1,\qquad v_2(d)=v_2(p+1),\qquad d\ge14>4.
$$
故 $d$ 属于 R64 的容许阶集合。又因 $p\equiv2\pmod3$，R64 的精确维数式给
$$
 \dim(e_dJ_{\mathrm{ns}}^+(p))
 =\frac{\varphi(d)}2(n_{\mathrm{gen}}+1)>0.
\tag{166.5}
$$
R59 的已证局部–全局类型对应，把这个真实非零 Hecke 块分解为水平 $p^2$、平凡 nebentype 的深度零尖点型新形式，有限惯性参数的阶恰为 $d$。从中取一个 $f$。

这个 $f$ 不可能有 CM。若一个平凡 nebentype、水平 $p^2$ 的权二新形式有 CM，其 CM 二次域只能在 $p$ 分歧。由该二次自扭曲限制到惯性，若尖点参数为 $\theta,\theta^{-1}$，非平凡分歧二次字符必须交换这两条特征线；于是
$$\theta^2=\delta,$$
其中 $\delta$ 是非平凡二次惯性字符，从而 $\theta$ 的阶为 $4$。这与 $d>4$ 矛盾。这个论证只用同一真实局部表示的二次自扭曲，不以“非 CM 新形式通常存在”代替 (166.5)。

## 3. 有限尖点型中准确缺失、出现的 Cartan 字符

记 $Z=\mathbb F_p^\times\subset C$。对正则参数 $\theta\ne\theta^p$，有限尖点表示 $R_\theta$ 的 Cartan 限制为
$$
 R_\theta|C
 =\operatorname{Ind}_Z^C\mathbf1-\theta-\theta^p.
\tag{166.6}
$$
这是实际有限 $\mathrm{GL}_2(\mathbb F_p)$ 类型的字符恒等式：在标量上两边的迹是 $p-1$，在非标量 Cartan 元素 $c$ 上两边都是 $-\theta(c)-\theta(c^p)$。因此每个在 $Z$ 上平凡的字符都出现一次，唯独 $\theta,\theta^p$ 不出现。

$\theta$ 的阶 $d$ 与 $3$ 互素，所以 $\theta$ 在 $C$ 的阶三子群上平凡，而 $\vartheta$ 不平凡。四个字符
$$
 \theta\vartheta,\quad\theta\vartheta^{-1},\quad
 \theta^p\vartheta,\quad\theta^p\vartheta^{-1}
\tag{166.7}
$$
都不等于 $\theta$ 或 $\theta^p$，并且两两不同。例如
$\theta\vartheta=\theta^p\vartheta^{-1}$ 会给
$\theta^{p-1}=\vartheta^2$，左边的阶整除 $d$，右边阶为 $3$，不可能。其他交叉相等同理。

由于 $p\equiv-1\pmod3$，$p$ 次幂把 (166.7) 分成恰好两对
$$
 \{\varphi_+,\varphi_+^p\}
 =\{\theta\vartheta,\theta^p\vartheta^{-1}\},
 \qquad
 \{\varphi_-,\varphi_-^p\}
 =\{\theta\vartheta^{-1},\theta^p\vartheta\}.
\tag{166.8}
$$
这两对在 $R_\theta|N$ 中分别给一个二维不可约诱导表示，各重数为一。它们不是范数字符的两个一维延拓：每个 $\varphi_\pm$ 的阶为 $3d=p+1>2$，而在 $Z$ 上平凡的范数字符阶至多为 $2$。

## 4. 同一实际惯性将出现字符送到缺失参数

必须使用 R66 的实际基本特征取向，而非只知道惯性子群抽象同构于 $C^3$。写 $T=p^2-1$。在一个与 $C\simeq\mathbb F_{p^2}^\times$ 兼容的取向下，R21、R66 给
$$
 \lambda|I_p=\omega_2^b,\qquad
 b=1+kT/6,\qquad \gcd(b,T)=3.
\tag{166.9}
$$
阶三情形也包含在此写法中。反转基本特征取向只把 $\theta,\theta^p$ 同时交换，不改变两对 (166.8)。

因为 $d=(p+1)/3$ 整除 $T/6$，且 $3\mid b$，有
$$
 \theta^b=\theta,\qquad \vartheta^b=1,
 \qquad
 \boxed{\varphi_+^b=\varphi_-^b=\theta.}
\tag{166.10}
$$
若局部好约化指数为 $6$，(166.9) 中可以含额外二次扭曲；它在这里无害，因为 $\theta,\vartheta$ 在标量 $-1$ 上平凡。没有把实际六次情形偷换成只有三次情形。

于是两个不同的实际全局 Artin 字符在 $p$ 的惯性上，均变成有限尖点类型原本缺失的 $\theta$。这正是正根数的原因。

## 5. 从完整层下降到每个实际配对分支

本节只用已发表的等变 Eichler–Shimura 分解、有限群特征零投影和实际 Hecke 对应。它不用 Studnia 的商构造结论。

先取
$$
 \mathscr X_E(p)=\coprod_{\alpha\in\mathbb F_p^\times}X_E^\alpha(p),
 \qquad \mathscr J_E(p)=\prod_\alpha\operatorname{Jac}(X_E^\alpha(p)).
\tag{166.11}
$$
每个因子都定义于 $\mathbb Q$。在水平基行向量 $b$ 上采用左作用
$$T_g(b)=b\,{}^tg.$$
实际模问题的下降是
$$b\longmapsto\sigma(b)r(\sigma)^{-1}
       =T_{r(\sigma)^{-t}}(\sigma(b)).$$
因此配对乘子的 Galois 作用为
$\chi_p\det(r^{-t})=1$，恰给每一个实际 $X_E^\alpha(p)$。

如 R143 §2 已逐分量核定的左右作用规范，等变上同调与协变 Tate 模分别具有有限型 $W_\pi$ 与 $W_\pi^\vee$。代入上述下降后，实际有限因子为
$$W_\pi^\vee\circ r^{-t}\simeq W_\pi\circ r.$$
这个同构在整个 $\mathrm{GL}_2$ 上成立：对每个矩阵 $g$，
$W_\pi^\vee(g^{-t})={}^tW_\pi({}^tg)$，其特征标等于 $W_\pi(g)$，因为 $g$ 与其转置相似。故这里没有遗失一个行列式角色，也没有从仅在 $\mathrm{SL}_2$ 上成立的公式外推。

Virdol 的原刊 §2.4–§2.6 给完整等变分解。将 (166.6)–(166.8) 代入，(166.3) 都实际出现在 $\mathscr J_E(p)$ 的 Tate 模中；对应的有限 $N$ 表示各出现一次。坏 Euler 因子始终对整个张量积取惯性不变量。

### 5.1 有理 Hecke 商

保留 $f$ 的全部 Dirichlet 扭曲及系数 Galois 共轭，并对 (166.8) 同时作相应扭曲。若 $f$ 扭以模 $p$ 的 Dirichlet 字符 $\kappa$，有限自守类型扭以 $\kappa_p\circ\det$，其中单位值 $\kappa_p(a)=\kappa(a)^{-1}$；故 Cartan 参数相应乘 $\kappa^{-1}\circ N_{C/Z}$。在实际下降中它与 $V_f$ 的 $\kappa(\chi_p)$ 扭曲抵消。

对这个完整集合，取 Hecke 幂等元与有限 $N$ 的中心幂等元的乘积，再取完整系数 Galois 轨道。所得有理幂等元 $e$ 是 $\mathscr J_E(p)$ 的 $\mathbb Q$ 有理端同态：在原来的左作用中，有限作用在 Galois 下按 $r^{-t}$ 共轭，故准确使用 $N^*=\{n^{-t}:n\in N\}$ 的中心投影；经上面的 $W_\pi^\vee\circ\iota\simeq W_\pi$ 同构，才将其记为 $N$ 的字符参数。这个中心投影与实际 Galois 共轭作用交换；Hecke 投影和完整系数轨道也被保持。清去幂等元的整数分母，取其像，得到一个真实的非零 $\mathbb Q$ 阿贝尔簇 $B$，并且
$$\mathscr J_E(p)\twoheadrightarrow B$$
的兼容系统只有 (166.3) 的相应完整轨道。有限分母只用于构造特征零同源因子；本节没有声称它们在任意特征 $\ell$ 下为单位。

### 5.2 不能只在不连通总层找到因子

下面证明 $B$ 对每个实际配对分支都有非零像。令
$$B_\alpha=e\bigl(\operatorname{Jac}(X_E^\alpha(p))\bigr)\subset B,$$
仍以清分母后的同态解释。它是定义于 $\mathbb Q$ 的阿贝尔子簇，同时是该实际 Jacobian 的商。

对素数 $q\ne p$，实际 $q$ 次同源 Hecke 对应把配对乘子 $\alpha$ 送到 $q\alpha$，所以
$$T_q(B_\alpha)\subset B_{q\alpha}.$$
由于 $e$ 与 $T_q$ 交换，这个包含在所构造的 $B$ 内成立。

选择 $q\bmod p$ 为 $\mathbb F_p^\times$ 的一个生成元，并使 $a_q(f)\ne0$。这样的素数存在：非 CM 新形式的大像定理给出任意有限阿贝尔 Galois 条件下迹非零的开集；Chebotarev 在该开集内给素数。等价地，可以使用非 CM 新形式零迹素数密度为零，而固定算术级数素数密度为正。对 $f$ 的每个系数共轭及模 $p$ Dirichlet 扭曲，$q$ 处特征值也都非零。因此 $T_q$ 在 $B$ 上是一个同源。

于是
$$\dim B_\alpha\le\dim B_{q\alpha}.$$
沿着长度 $p-1$ 的乘法循环，所有不等式都为等式。又因为所有 $B_\alpha$ 的和为非零的 $B$，它们不可能全为零。因此
$$\boxed{B_\alpha\ne0\quad\text{对每个 }\alpha.}\tag{166.12}$$

这一步只利用实际分支间定义于 $\mathbb Q$ 的 Hecke 对应；没有在一个没有承载实际点的额外分支中找到因子后，就将其误认成所需分支上的商。对各 $B_\alpha$ 作最优化不改变其有理同源类型和根数结论。

## 6. 全局 Hecke 字符和 $p$ 处完整环面

由 $\lambda$ 满射及 (166.8)，$\Xi_\pm$ 阶恰为 $p+1$，且其共轭为逆。下面还需要比“反圆分”更准确的条件：
$$\boxed{\Xi_\pm|\mathbb A_{\mathbb Q}^{\times}=1.}\tag{166.13}$$

在几乎所有分裂有理素数 $q$，两处 Frobenius 的 Cartan 值相乘为 $q$，是标量；在惰性 $q$，若 $g=r(\operatorname{Frob}_q)\in N\setminus C$，则 $g^2=-\det(g)$ 也是标量。因 $\varphi_\pm|Z=1$，两种情况下 $\Xi_\pm((q))=1$。强乘法一或有限阶全局类域论遂给 (166.13)。无穷分量也平凡。

令 $L=K_p/\mathbb Q_p$ 为不分歧二次扩张，算术互反将单位 $a$ 在 $\omega_2$ 上的作用写作 $a^{-1}$。置
$$\Omega_\pm=\Xi_{\pm,p}^{-1}.$$
由 (166.10)、(166.13)，有
$$
 \Omega_\pm|\mathcal O_L^\times=\theta,\qquad
 \Omega_\pm(p)=1.
\tag{166.14}
$$
第二个等式使用 $p\in\mathbb Q_p^\times$，不可从单位限制单独猜测。因为
$L^\times=\mathbb Q_p^\times\mathcal O_L^\times$，(166.14) 唯一锁定完整局部角色。特别它 tame 且非平凡，所以 $\Xi_\pm$ 在该处导子指数恰为 $1$，诱导到 $\mathbb Q_p$ 后导子指数恰为 $2$。

### 6.1 为什么缺失有限字符等价于完整局部 Hom 为零

写 $K_0=\mathrm{GL}_2(\mathbb Z_p)$、$J=\mathbb Q_p^\times K_0$。深度零尖点表示有标准紧诱导实现
$$\pi_{f,p}=\mathrm{c\!-!Ind}_{J}^{\mathrm{GL}_2(\mathbb Q_p)}\widetilde R_\theta,$$
其中 $\widetilde R_\theta$ 在 $K_0$ 上是 $R_\theta$ 的 inflation，标量处由平凡中心角色延拓。

不分歧环面 $L^\times\subset J$ 的 Mackey 双陪集可按其固定顶点到标准顶点的距离 $n\ge0$ 取代表 $g_n=\operatorname{diag}(p^n,1)$。在 $n=0$ 项，完整 Hom 正是 (166.6) 中的有限 Cartan 重数，因为一致化元的值也由中心匹配。

在 $n\ge1$ 项，取非平方单位 $z$、$\tau_0^2=z$，并考察
$$
 t_y=1+p^ny\tau_0\in1+p\mathcal O_L.
$$
$\Omega_\pm(t_y)=1$，而 $g_nt_yg_n^{-1}$ 在 $K_0$ 中约化为一个完整的非平凡下三角幺幂子群：在乘法矩阵基下为
$$
 \begin{pmatrix}1&p^{2n}zy\\y&1\end{pmatrix}\pmod p.
$$
有限尖点表示没有该幺幂子群的不变量。故所有 $n\ge1$ 的 Mackey 项为零。由 (166.6)、(166.14)，$n=0$ 项也为零，得到
$$
 \boxed{\operatorname{Hom}_{L^\times}
 (\pi_{f,p},\Omega_\pm)=0.}
\tag{166.15}
$$
因此不是仅在某个有限型子空间内 Hom 为零；完整局部表示中也没有该角色。

## 7. 局部–全局根数和不可约性

$f$ 的中心角色平凡，(166.13) 给处处的环面中心相容性。Saito (1993), §1 的定理，取加性角色 $\psi_L=\psi_{\mathbb Q_p}\circ\operatorname{Tr}$，将 (166.15) 转为
$$
 \epsilon\!\left(\tfrac12,\pi_{f,L}\otimes\Xi_{\pm,p}\right)=-1.
\tag{166.16}
$$
在所有其他有限非分裂处，$\pi_{f,q}$ 未分歧且为不可约主系列。非分裂环面在 $\mathbb P^1(\mathbb Q_q)$ 上传递、稳定子为中心，故其诱导模型包含每个中心相容的环面字符。Saito 的同一定理给局部符号 $+1$，包括可能的剩余特征 $2$ 和 $\Xi_\pm$ 的分歧处。在分裂处，基变换的两个扭曲互为对偶，局部 epsilon 乘积也为 $+1$。

在复无穷处，权二离散系列基变换的角角色次数为 $1,-1$，根数乘积为 $-1$。故完整全球乘积为
$$(-1)_p(-1)_\infty=+1,$$
证明 (166.4)。这也等于 $\mathbb Q$ 上对应 Rankin 张量积的全球根数；二次诱导常数的全球乘积为一。

$\operatorname{Ind}_K^{\mathbb Q}\Xi_\pm$ 是不可约的奇二维 Artin 表示，因为 $\Xi_\pm^c=\Xi_\pm^{-1}\ne\Xi_\pm$。非 CM $f$ 的充分大系数素数像包含一个开 $\mathrm{SL}_2$ 子群。因此在任意有限扩张上 $V_f$ 仍绝对不可约，且其交换子只有标量。对 Artin 表示的核作限制，任何张量积子表示都具有形式 $V_f\otimes U$；全局稳定性再迫 $U$ 为 Artin 表示的子表示。故 (166.3) 绝对不可约。

这还排除了“一个可分裂块总根数为正，却包含负号子因子”的歧义。二次基变换和有限阶 Hecke 扭曲给完整自守 $L$ 函数；非 CM 保证基变换仍尖点，其 $L$ 函数在中心全纯。完整系数 Galois 轨道保留同一局部匹配条件，所以 $B$ 及各非零 $B_\alpha$ 的每个不可约兼容系统因子都满足相同的正号结论。

## 8. 对 R122 的真正新接口和未解步骤

原来的 R69 商取 level-$p$ Steinberg 型和阶三 Artin 角色；后者在 $p$ 不分歧，尖点微分的两个有限系数正是 R122 的三色共同理想。

本篇的商则来自真实存在的 level-$p^2$ 尖点型，Artin 角色的阶为 $p+1$，在 $p$ 的导子指数为 $2$。因此它是不同的候选商结构，不能用“全部其他因子根数为负”预先排除。但以下两步仍未完成：

1. 对这些随实际 $E,K,p$ 变化的因子，证明至少一个中心 $L$ 值非零，并由准确已发表输入得到实际秩零商。由于权二形式和 Artin 形式的导子都含 $p^2$，R66/R87 中 level-$p$ 与 prime-to-$p$ Artin 导子的 Feigon–Whitehouse 接口不能直接代入。
2. 在实际尖点和实际原始 $p$ 次根下，求出这些有限尖点类型的 Whittaker 系数及其**饱和整格**。有限群阶为 $\ell$ 单位，并不自动清除 Hecke 投影的同余分母；更不能据此断言它们补掉原三色共同零点。

正根数只解除函数方程强制消失；本文没有证明 $L(B_\alpha,1)\ne0$、$B_\alpha(\mathbb Q)$ 有限或新的整性范围。也没有把新增候选商当作 Serre uniformity 的完成。

## 9. 已核输入与文献比较

- [R64](R64-inertial-order-traces-and-cm-type-targets.md)，定理1及式(3.3)：原几何连通 $X_{\mathrm{ns}}^+(p)$ 上每个容许惯性阶的真实全局块及其严格正维数。
- [R59](R59-local-types-toric-twist-and-height-kernel.md)：上述全局块的深度零尖点型对应；[R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md) §2：实际小惯性指数及其基本特征取向。
- C. Virdol, *Zeta functions of twisted modular curves*, J. Aust. Math. Soc. **80** (2006), 89–103，§2.4–§2.6、Propositions2.2–2.3：[原刊](https://www.austms.org.au/Publ/JAustMS/V80P1/pdf/t56.pdf)。使用完整等变 Tate 分解，不使用把坏处张量积不变量错误分开的简式。
- H. Saito, *On Tunnell's formula for characters of GL(2)*, Compositio Math. **85** (1993), 99–108，§1、印刷页99的未编号定理：[原刊](https://www.numdam.org/item/CM_1993__85_1_99_0.pdf)。包括剩余特征2，采用迹相容加性角色。
- C. J. Bushnell and G. Henniart, *The Local Langlands Conjecture for GL(2)*, Grundlehren **335** (2006)，§6.4及深度零紧诱导构造：[DOI](https://doi.org/10.1007/3-540-31511-X)。本文已将所需有限 Cartan 限制和非零距离 Mackey 项消失写出。
- K. A. Ribet, *On $l$-adic representations attached to modular forms. II*, Glasgow Math. J. **27** (1985), 185–194，§3 Theorem3.1：[作者保存的原刊](https://math.berkeley.edu/~ribet/Articles/rankin.pdf)。用于非 CM 强不可约性及指定算术级数中选非零 Hecke 特征值；本文解释了这两处具体用法。
- [R143](R143-squarefree-cm-twists-all-analytic-quotients-vanish.md) §2 已逐式证明完整层左右作用、对偶、转置与实际扭曲下降的配套规范。这里复用的是对任意实际 $r$ 都成立的几何计算，**没有**把其固定 $\mathbb Q(i)$ 的负根数定理迁移到本分支。

文献对照：Studnia 的博士论文 *L-functions and rational points for Galois twists of modular curves*，Theorem10（印刷16页/PDF23）、Theorem5.B（印刷207页/PDF214）、Proposition5.3.4（印刷218–219页/PDF225–226）确实列有这一第二种正号机制：[作者公开全文](https://pub.math.leidenuniv.nl/~studniae/These.pdf)。本文不把该博士论文的分类或商存在作为证明前提。作者 [研究页](https://pub.math.leidenuniv.nl/~studniae/publications.html) 仍把 arXiv:2507.20801 列为 submitted。

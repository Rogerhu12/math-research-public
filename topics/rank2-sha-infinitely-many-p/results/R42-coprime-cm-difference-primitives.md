# R42：互素 CM 差分的有理共同原函数

日期：2026-11-12。**状态：下面的代数性定理及有限支持证明已完成。**

本结果解决 R41 后续的一条具体构造问题。
不能用两个互素 CM 乘子的无 twist 差分、配上两个椭圆有理右端，
得到一个非代数的共同形式 germ。
结论对任意复系数 Laurent germ 成立，不要求实系数、\(\mathbb Q\)-系数或共轭固定。
而且原函数已在**原来的** \(\mathbb C(E)\) 中，不只是某个有限覆盖上代数。

证明使用 principal parts 的有限支持模。
关键升层映射具有明确左逆，因而没有预设共同原像具有有限支持，
也没有把未展开的 CM 版差分分类当作文献定理。

## 1. 陈述与算子

固定
\[
E/\mathbb C:y^2=x^3-17x,\qquad
\Lambda=\Omega\mathbb Z[i],\qquad \mathcal O=\mathbb Z[i],
\]
并写
\[
b=2+i,\qquad c=3+2i,\qquad Nb=5,\quad Nc=13.
\]
两者生成不同的 Gaussian 素理想，特别地 \((b,c)=1\)。
令
\[
(\sigma_aF)(z)=F(az),\qquad D_a=\sigma_a-1,\qquad
\mathcal R=\mathbb C(E)\subset\mathbb C((z)).
\]

**定理。** 对任意正整数 \(r,s\) 和 \(F\in\mathbb C((z))\)，若
\[
D_b^rF\in\mathcal R,\qquad D_c^sF\in\mathcal R,
\tag{1.1}
\]
则
\[
\boxed{\quad F\in\mathcal R.\quad}
\tag{1.2}
\]

\(F\) 可以在 \(z=0\) 有有限阶极点。
不需要先假设它收敛或可以在整个复平面延拓。

原式坐标也可用 \(t=-x/y\)，因为 \(z=\log_E(t)\) 是形式换元。
若 \(F\) 的 \(t\)-展开属于 \(k((t))\)，其中 \(k\subset\mathbb C\)
为定义 \(E\) 的特征零子域，则结论还下降为 \(F\in k(E)\)，见第 8 节。

## 2. Principal parts 与其拉回

对每个 \(P\in E(\mathbb C)\)，使用平移后的不变形式参数
\(u=z-z_P\) 记录 principal part。
令 \(M\) 是 \(E(\mathbb C)\) 上所有**有限支持**的复值函数之空间。
各阶 principal parts 给出
\[
\mathcal P=\bigoplus_{\ell\ge1}M^{(\ell)}.
\]
一个元素只含有限多个 \(\ell\)，并且每个 \(\ell\) 只在有限多个 \(P\) 非零。
在第 \(\ell\) 个分量中，\(f(P)\) 表示 \(u^{-\ell}\) 的系数。

写
\[
\operatorname{pp}:\mathcal R\longrightarrow\mathcal P
\]
为取全部极点的 principal parts。
因为 \([a]\) 在不变参数中为 \(u\mapsto au\)，
\(\sigma_a\) 在第 \(\ell\) 分量诱导
\[
(T_af)(P)=a^{-\ell}f([a]P).
\tag{2.1}
\]
这是真正的 pullback；等价地，
\[
T_a\mathbf 1_{\{Q\}}
=
a^{-\ell}\sum_{[a]P=Q}\mathbf 1_{\{P\}}.
\tag{2.2}
\]
算子 \(T_b,T_c\) 交换。置
\[
S_a=T_a-1.
\]
于是
\[
\operatorname{pp}(D_ah)=S_a\operatorname{pp}(h).
\tag{2.3}
\]

**有限支持单射。** \(S_b:M^{(\ell)}\to M^{(\ell)}\) 为单射。
若 \(T_bf=f\ne0\)，非零支持 \(S\) 满足 \([b]^{-1}S=S\)。
但 \([b]\) 是度 \(5\) 的 étale isogeny，
故 \(|[b]^{-1}S|=5|S|>|S|\)，矛盾。

## 3. 一个可选取的 \(c\)-primary 分裂

需要把有限支持按一个与 \(b\) 相容的深度分层。

令
\[
A=E[c^\infty]=\bigcup_{n\ge0}E[c^n].
\]
作为 \(\mathcal O\)-模，\(A\) 可除：
乘以 \(c\) 满射；乘以与 \(c\) 互素的元素是自同构。
\(\mathcal O=\mathbb Z[i]\) 是 PID，可除模为 injective，故包含
\(A\hookrightarrow E(\mathbb C)\) 有 \(\mathcal O\)-线性回缩。
因此可选
\[
E(\mathbb C)=A\oplus W.
\tag{3.1}
\]

这里的分裂不要求自然，也不带任何数论定义域结论。
它只用于复向量空间中有限支持的证明。
为说明没有隐藏一个分裂猜想，可除模的 injective 性可直接由 Zorn 引理证明：
在扩张一个模同态到新生成元 \(x\) 时，
所有关系 \(a x\) 落入旧子模的 \(a\) 形成一个主理想 \((a_0)\)；
用可除性选取 \(a_0y\) 等于旧同态对 \(a_0x\) 的值即可延拓。
若该理想为零，则任取 \(y\)。
将其应用于 \(A\) 上的恒等同态，得到回缩。

直和分量 \(W\) 也可除，且没有 \(c\)-torsion。
因此 \([c]:W\to W\) 为双射。
由于 \((b,c)=1\)，\([b]:A\to A\) 也为双射；
而 \(\ker[b]\) 落在 \(W\) 中。

若 \(P=P_c+P_W\) 为 (3.1) 分解，定义
\[
n(P)=\min\{n\ge0:c^nP_c=0\}.
\tag{3.2}
\]
令 \(M_n\subset M\) 为支持在 \(n(P)=n\) 上的有限支持函数。
于是
\[
M=\bigoplus_{n\ge0}M_n.
\tag{3.3}
\]

所有 \(b\)-原像与原点具有相同的 \(c\)-primary 深度，
故 \(T_b,S_b\) 保持每个 \(M_n\)。
另一方面：

- 对 \(n>0\)，一个深度 \(n\) 点的全部 \(13\) 个 \(c\)-原像都具有深度 \(n+1\)；
- 对 \(n=0\)，其 \(13\) 个原像中恰有一个深度为零，
  其余 \(12\) 个深度为一。

第二条使用 \([c]\) 在 \(W\) 上的双射，以及 \(|E[c]|=13\)，
不是把 \(n=0\) 当作一般正层。

## 4. Pushforward 与最高层左逆

仍固定 pole order \(\ell\)。定义不加标量的有限支持 pushforward
\[
(P_cf)(Q)=\sum_{[c]P=Q}f(P).
\tag{4.1}
\]
\(P_c\) 把 \(M_{n+1}\) 送到 \(M_n\)，包括 \(n=0\)。

有精确恒等式
\[
P_cT_b=T_bP_c.
\tag{4.2}
\]
确实，
\[
(P_cT_bf)(Q)
=
b^{-\ell}\sum_{[c]P=Q}f([b]P).
\]
映射 \(P\mapsto[b]P\) 将 \(c\)-fiber \([c]P=Q\)
双射到 \([c]R=[b]Q\)：
它在 \(\ker[c]\) 上为双射，因为 \((b,c)=1\)。
因此上式为
\[
b^{-\ell}\sum_{[c]R=[b]Q}f(R)
=(T_bP_cf)(Q).
\]
该论证也保持精确深度，故在 \(M_1\to M_0\) 的边界处同样成立。

对 \(f\in M_n\)，令 \(T_c^{\mathrm{top}}f\) 为 \(T_cf\)
的 \(M_{n+1}\) 分量。
由第 3 节的原像计数，
\[
\boxed{\quad
P_cT_c^{\mathrm{top}}f=
\begin{cases}
13c^{-\ell}f,&n>0,\\
12c^{-\ell}f,&n=0.
\end{cases}
\quad}
\tag{4.3}
\]
两种标量均非零。

由于 \(S_b\) 保持分层，
\[
Q:=M/S_bM
=
\bigoplus_{n\ge0}Q_n,\qquad Q_n=M_n/S_bM_n.
\tag{4.4}
\]
(4.2) 使 \(P_c\) 在这些商上有定义；
\(T_c^{\mathrm{top}}\) 也有定义，因为 \(T_c,T_b\) 交换且
\(T_b\) 保持分层。
(4.3) 给出商上最高层映射
\[
Q_n\longrightarrow Q_{n+1}
\]
的左逆乘非零标量，因此该映射单射。

由此得到本证明的有限支持核心：
\[
\boxed{\quad
S_c=T_c-1\text{ 在 }M/S_bM\text{ 上为单射。}
\quad}
\tag{4.5}
\]
若一个非零商类的最高非零层为 \(n\)，则
\(S_c\) 后的第 \(n+1\) 层恰为上述非零最高层像。
较低层最多升到 \(n\)，而减去原商类不贡献第 \(n+1\) 层；
所以不能相消。

## 5. 兼容 principal parts 的共同有限原像

由第 2、4 节，若 \(u,v\in M^{(\ell)}\) 满足
\[
S_cu=S_bv,
\tag{5.1}
\]
则存在 \(w\in M^{(\ell)}\) 使
\[
S_bw=u,\qquad S_cw=v.
\tag{5.2}
\]
证明如下：在 \(Q=M/S_bM\) 中，(5.1) 给 \(S_c[u]=0\)。
由 (4.5)，\([u]=0\)，故 \(u=S_bw\)。
这里 \(w\) 按照商的定义已是**有限支持**元素。
再由
\[
S_b(v-S_cw)=0
\]
及 \(S_b\) 单射，得到第二个等式。

各 pole order 相互独立，故同一结论对
\(\mathcal P=\bigoplus_\ell M^{(\ell)}\) 成立。
输入只含有限多个 pole orders，因此不会在此步骤引入无限阶 principal part。

## 6. 消去唯一的 Mittag–Leffler 障碍

先证明 \(r=s=1\)。
令
\[
h_b=D_bF\in\mathcal R,\qquad h_c=D_cF\in\mathcal R.
\]
交换差分给出
\[
D_ch_b=D_bh_c.
\tag{6.1}
\]
这是有理函数的等式：两边在 \(O\) 的 Laurent 展开相等，故全局相等。
令 \(u=\operatorname{pp}(h_b)\)、\(v=\operatorname{pp}(h_c)\)。
第 5 节给出共同有限 principal part \(w\in\mathcal P\)，满足
\[
S_bw=u,\qquad S_cw=v.
\tag{6.2}
\]

定义总 simple residue
\[
\operatorname{res}(w)=\sum_{P}w_{P,1}.
\]
在当前不变参数中，这是试图实现的函数乘 \(\omega=dz\) 的总留数。
由 (2.2)，
\[
\operatorname{res}(T_bw)
=
\frac{Nb}{b}\operatorname{res}(w)
=
\bar b\,\operatorname{res}(w).
\tag{6.3}
\]
而 \(h_b\omega\) 是紧椭圆曲线上的亚纯微分，故
\(\operatorname{res}(u)=0\)。
结合 (6.2)、(6.3)，
\[
(\bar b-1)\operatorname{res}(w)=0.
\]
\(\bar b-1=1-i\ne0\)，于是
\[
\operatorname{res}(w)=0.
\tag{6.4}
\]

(6.4) 是椭圆曲线上的唯一 Mittag–Leffler 障碍。
也可在这里直接构造，不需假设一个 principal part 一定来自有理函数。
对有限支持中的点选复对数 \(z_P\)，令
\[
g(z)=
\sum_Pw_{P,1}\zeta(z-z_P)
+
\sum_P\sum_{\ell\ge2}
\frac{(-1)^{\ell-1}w_{P,\ell}}{(\ell-1)!}
\zeta^{(\ell-1)}(z-z_P).
\tag{6.5}
\]
第一项在格平移下的增量因 (6.4) 为零；其余项已经椭圆。
所以 \(g\) 是 \(\Lambda\)-椭圆亚纯函数，即 \(g\in\mathcal R\)，
并且它的 principal parts 恰为 \(w\)。

于是
\[
h_b-D_bg,\qquad h_c-D_cg
\]
都没有极点，因而都是常数。

## 7. 常数与所有高次差分

仍在 \(r=s=1\)。
置 \(G=F-g\in\mathbb C((z))\)，已知 \(D_bG\) 为常数。
逐系数写
\[
G=\sum_{k\ge k_0}a_kz^k,\qquad
D_bG=\sum_{k\ge k_0}(b^k-1)a_kz^k.
\]
对于每个非零整数 \(k\)，\(|b|>1\) 保证 \(b^k-1\ne0\)；
故 \(a_k=0\)。
常数项的差分本来就是零，故右端常数也只能为零。
所以 \(G\) 为常数，\(F\in\mathcal R\)。
这证明基础情形。

对任意 \((r,s)\) 按 \(r+s\) 强归纳。

若 \(r>1\)，将归纳假设用于 \(D_bF\) 的指数 \((r-1,s)\)，得到
\(D_bF\in\mathcal R\)；再对 \(F\) 用指数 \((1,s)\)，得到结论。

若 \(r=1,s>1\)，先对 \(D_cF\) 用指数 \((1,s-1)\)，得到
\(D_cF\in\mathcal R\)，随后对 \(F\) 用基础情形。

全部算子保持 \(\mathcal R\) 并彼此交换，故这些应用的两个右端均有理。
定理得证。

## 8. 定义域下降与确切范围

若 \(E\) 定义于特征零子域 \(k\subset\mathbb C\)，
\(t\) 是 \(k\)-有理局部参数，并且 \(F\in k((t))\)，
那么 (1.2) 下降为 \(F\in k(E)\)。
例如可令 \(\tau\in\operatorname{Aut}(\mathbb C/k)\) 作用于有理函数的系数：
\(\tau F\) 与 \(F\) 在 \(t\) 的全部系数相同，所以二者在 \(\mathbb C(E)\) 中相等。
有理函数按
\[
A(x)+yB(x),\qquad A,B\in\mathbb C(x)
\]
唯一表达，再将各分母规范为首一，便知各系数固定于
\(\operatorname{Aut}(\mathbb C/k)\)，因而属于 \(k\)。
在本题的 \(k=\mathbb Q\) 或 \(\mathbb Q(i)\) 情况可直接使用这一下降。

这比先前实系数 note 的结论更强，原因是这里直接证明了
principal parts 的有限支持相容性：

- 不用共轭将 \(F\) 替换为同一个 germ；
- 不调用整数 \(5,13\) 的分类定理来推断非实 CM 情形；
- 不必扩张周期格；
- 不必预先证明 \(F\) 的解析延拓或全局亚纯性。

所排除的是**同一个标量 germ、两个无 twist 差分幂、两个椭圆有理右端**。
Robert 的 \(\sigma_b-\bar b\)、sigma 对数的 \(\sigma_b-Nb\)
不满足这里的算子假设。
非有理右端、非线性等变关系及向量对象也未被本定理一并排除。

## 9. 对 R41 构造任务的结论

若有椭圆有理函数 \(h_b,h_c\) 满足
\[
D_c^sh_b=D_b^rh_c
\]
并实际产生一个共同 Laurent 解 \(F\) 满足
\(D_b^rF=h_b,D_c^sF=h_c\)，则该解已在原 \(\mathbb C(E)\) 中有理。
所以不能把 R41 的两个共同深度直接实现为这种
非代数的兼容有理 cocycle。

R41 的加权阶数和与深度求和定理仍然成立；
本结果只精确缩小能实现它的解析对象范围。
尚未由此证明固定 \(E\) 有无穷多个 \(p\) 的 Sha 初级部分有限。

### 文献关系

本篇证明是独立的有限支持与 Mittag–Leffler 论证。
其问题背景可与 de Shalit 的差分分类比较：
*Elliptic \((p,q)\)-difference modules*,
Algebra & Number Theory 15 (2021), 1303–1342,
[DOI](https://doi.org/10.2140/ant.2021.15.1303)，
[作者原文](https://arxiv.org/abs/2007.09508v2)，§6.2 Theorem 37、Remark 38。
本篇没有把该文只详细处理的互素正整数定理扩写为 CM 版引用。

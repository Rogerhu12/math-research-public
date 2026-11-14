# 真实高度格与 Gauss 算子给出的过半增广深度

日期：2026-11-12。状态：以下跨素数线性下界已证明，并经两位研究者独立核查。
它加强 R107 的对数深度，但仍不证明取完整 prime-to-$p$ 迹后的指定点非零，
也没有证明所需最底增广商中的原始性。

沿用 [R105 的固定类群和](2026-11-12-minus15-classgroup-trace-primitivity.md)
与 [R107 的真实轨道](2026-11-12-heegner-orbits-and-logarithmic-augmentation-depth.md)。
固定 $E:y^2=x^3-17x$、$F=\mathbb Q(\sqrt{-15})$。
对每个充分大的目标素数 $p$，选择 R105 的辅助素数 $\ell$，令
$H=F[\ell]$、$X=X_\ell\in E(H)$。于是
\[
 v_p(\ell+1)=1,\qquad
 0<\widehat h(X)\le C_X\log p,\qquad
 E(F^{\mathrm{ab}})_{\mathrm{tors}}=E[2].                 \tag{1}
\]
这里与下文的 $\log$ 都是自然对数，$C_X$ 与 $p$ 无关。
取 $\sigma\in\operatorname{Gal}(H/F)$ 的阶为 $p$，写
$\Delta=\sigma-1$、$r=p-1$。R107 的固定有限映射纤维论证已证明
\[
 x=\Delta X\quad\text{非挠}.                            \tag{2}
\]

## 1. 命题：超过一半的实际增广层非零

所有充分大的目标素数 $p$ 都有
\[
 \boxed{\quad
 \Delta^kX_\ell\notin pE(H)
 \quad\left(0\le k\le\frac{p+1}{2}\right).
 \quad}                                                \tag{3}
\]
因此 $\bar X_\ell$ 在 $E(H)/pE(H)$ 中的真实循环子模，其 Jordan 长度
至少为 $(p+3)/2$。此处的模 $p$ 群和 Galois 作用都是实际点的，
没有先假设任何 Heegner 格为自由群环模。
§2–4 先用一个独立的体积论证得到 $(1/2-o(1))p$ 的长度；
§5 用实际整数 Gauss 算子去掉该误差并证明 (3)。

## 2. 从实际点构造一份饱和分圆格

令 $G=E(H)/E(H)_{\mathrm{tors}}$。这是有限秩自由阿贝尔群，
典范高度在 $G\otimes\mathbb R$ 上给正定二次型。
仍将实际点在 $G$ 中的像记作 $X,x$。
因为全部挠点被 $2$ 杀，而 $p$ 为奇数，准确有
\[
 E(H)/pE(H)\simeq G/pG.                                \tag{4}
\]
在 $G\otimes\mathbb Q$ 中置
\[
 V=\mathbb Q[\sigma]x,\qquad
 L=\mathbb Z[\sigma]x,\qquad W=G\cap V.                \tag{5}
\]
由 $Nx=0$，其中 $N=1+\sigma+\cdots+\sigma^{p-1}$，以及 $x\ne0$，
不可约的分圆多项式 $\Phi_p(T)$ 是 $\sigma$ 在 $V$ 上的最小多项式。
故 $\dim_{\mathbb Q}V=r$，且
\[
 x,\sigma x,\ldots,\sigma^{r-1}x
 \quad\text{是 }L\text{ 的一个 }\mathbb Z\text{ 基}.     \tag{6}
\]
$W$ 是 $G$ 的饱和、$\sigma$ 稳定子格；它在 $V$ 中与 $L$ 同秩，
所以 $[W:L]$ 有限。饱和性尤其给
\[
 W\cap pG=pW,
 \qquad W/pW\lhook\joinrel\longrightarrow G/pG.        \tag{7}
\]
这里保留完整 Mordell–Weil 饱和格，不能用仅由共轭点生成的 $L$
直接代替右边的实际模 $p$ 群。

## 3. 统一高度下界控制格指数的 p 部

以 $\|v\|^2=\widehat h(v)$ 为 $V\otimes\mathbb R$ 上的欧氏度量。
[R102 已核的 Baker 定理](2026-11-12-heegner-height-and-augmentation-primitivity.md)
给一个固定 $c>0$，使每个 $0\ne w\in W$ 均有
\[
 \|w\|^2\ge c.                                        \tag{8}
\]
这是对 $E(F^{\mathrm{ab}})$ 中全部实际非挠整点的同一个下界，
所以它也适用于饱和后增加的点，并不随域 $H$ 的次数下降。

另一方面，典范高度的平行四边形恒等式与 Galois 不变性给
\[
 \widehat h(x)=\widehat h(\sigma X-X)
       \le4\widehat h(X)\le H_p,
 \qquad H_p=4C_X\log p.                               \tag{9}
\]
(6) 的所有基向量有相同高度。对其 Gram 行列式用 Hadamard 不等式，得
\[
 \operatorname{covol}(L)\le H_p^{r/2}.                 \tag{10}
\]

由 (8)，半径小于 $\sqrt c$ 的开球没有 $W$ 的非零点。
Minkowski 的凸体定理因此给
\[
 \operatorname{covol}(W)
 \ge \frac{\operatorname{vol}(B_r)}{2^r}c^{r/2}
 =\frac{(\pi c/4)^{r/2}}{(r/2)!}
 \ge\left(\frac{\pi c}{2r}\right)^{r/2}.               \tag{11}
\]
最后一步仅用 $r$ 为偶数及 $(r/2)!\le(r/2)^{r/2}$。
同一个下界也可由半径 $\sqrt c/2$ 的格点球内部不相交、其周期密度
至多为 $1$ 直接得到；这里没有引入未知的调节子下界。

因为 $L\subset W$，(10)–(11) 给
\[
 [W:L]=\frac{\operatorname{covol}(L)}{\operatorname{covol}(W)}
 \le\left(\frac{2rH_p}{\pi c}\right)^{r/2}.            \tag{12}
\]
令 $a_p=v_p([W:L])$。于是
\[
 \begin{aligned}
 a_p
 &\le\frac{r}{2\log p}
       \log\left(\frac{8C_X r\log p}{\pi c}\right)\\
 &\le\frac r2
       \left(1+\frac{\log\log p+C_1}{\log p}\right),  \tag{13}
 \end{aligned}
\]
其中可取固定 $C_1=\max\{0,\log(8C_X/(\pi c))\}$。
特别地 $a_p\le(1/2+o(1))r<r$ 对充分大的 $p$ 成立。

## 4. 格指数准确变成实际 Jordan 深度

置
\[
 \mathcal O=\mathbb Z_p[\zeta_p],\qquad
 u=\zeta_p-1,\qquad W_p=W\otimes\mathbb Z_p.           \tag{14}
\]
通过 $\zeta_p\mapsto\sigma$，$W_p$ 是 $\mathcal O$ 模。
由 (5) 的 $\mathbb Q_p$ 维数，它在 $\mathcal O$ 上无挠且秩为一。
$\mathcal O$ 为离散赋值环，所以 $W_p$ 自由秩一。因而存在基 $e$ 与单位
$v\in\mathcal O^\times$，使
\[
 x=u^a v e,\qquad L\otimes\mathbb Z_p=\mathcal O x.
\]
$\mathcal O/u\mathcal O\simeq\mathbb F_p$，故局部指数为 $p^a$，
与 (13) 比较即 $a=a_p$。**这里的指数是 $p^{a_p}$，不是
$p^{ra_p}$。** 又因 $p\mathcal O=u^r\mathcal O$，
\[
 \Delta^j x\notin pW
       \quad\Longleftrightarrow\quad j+a_p<r.        \tag{15}
\]
严格地说 (15) 可先在 $W_p$ 判断，再由 $W/pW\simeq W_p/pW_p$
返回整格。结合 (4)、(7)，它也准确判断原群 $E(H)/pE(H)$ 中的
$\Delta^j x$ 是否非零。

因此，$\bar x$ 的 Jordan 长度恰为 $r-a_p$。由 $x=\Delta X$，
在 $a_p<r$ 时 $\bar X$ 的 Jordan 长度恰为
\[
 \boxed{\qquad p-a_p.\qquad}                         \tag{16}
\]
特别地 $\Delta^kX\notin pE(H)$ 对 $0\le k\le p-1-a_p$ 成立。
将 (13) 代入，先得到对每个固定 $\epsilon>0$、所有充分大的 $p$，
$\Delta^kX\notin pE(H)$ 在 $0\le k\le(1/2-\epsilon)p$ 的范围内成立。

## 5. 实际整数 Gauss 算子去掉半层误差

记 $\chi(j)=(j/p)$ 为二次角色，定义实际整数群环元
\[
 \mathcal G=\sum_{j=1}^{p-1}\chi(j)\sigma^j.
\]
它给 $W$ 的整自同态。典范高度配对的伴随由
$\sigma^\dagger=\sigma^{-1}$ 给出，所以
$\mathcal G^\dagger=\chi(-1)\mathcal G$。
有限二次角色的准确相关和为
\[
 \sum_{b\in\mathbb F_p}\chi(b)\chi(b+k)
 =\begin{cases}p-1,&k=0,\\-1,&k\ne0.\end{cases}
\]
对于 $k\ne0$，缩放化为 $\sum_t\chi(t(t+1))=-1$；
这可由 $y^2=t(t+1)$ 等价于
$(2t+1-2y)(2t+1+2y)=1$，其解数为 $p-1$ 直接验证。
逐项乘群环即得
\[
 \mathcal G^\dagger\mathcal G=p-N,
 \qquad\mathcal G^2=\chi(-1)(p-N).
\]
在 $V$ 与 $W$ 上 $N=0$，故准确有
\[
 \widehat h(\mathcal G w)=p\widehat h(w),
 \qquad v_u(\mathcal G)=r/2.                           \tag{17}
\]
第二式是在 $\mathcal O$ 中取值，由 $\mathcal G^2=\chi(-1)p$
及 $v_u(p)=r$ 立即得到。

若 $a_p\ge r/2$，则 §4 的局部格计算给
$\mathcal Gx\in pW_p$。同时 $\mathcal Gx\in W$；
由 $W/pW\simeq W_p/pW_p$，这意味着准确的整点归属
$\mathcal Gx\in pW$。因此存在实际 $z\in W$ 满足
\[
 pz=\mathcal Gx,
 \qquad\widehat h(z)=\frac{\widehat h(x)}p
                     \le\frac{4C_X\log p}{p}.         \tag{18}
\]
因为 $\mathcal G^2x=\chi(-1)px\ne0$，$z$ 非零。
对充分大的 $p$，(18) 小于 Baker 常数 $c$，与 (8) 矛盾。
故准确有
\[
 a_p<\frac{p-1}{2},\qquad
 a_p\le\frac{p-3}{2}.                                \tag{19}
\]
代入 (16)，得到 Jordan 长度至少 $(p+3)/2$，以及 (3) 的全部非零层。
这一步只在已证局部可除时才引入实际商点 $z$，没有把有理张量中的
形式除法当作整数点。证明完毕。

还可记录一个较小的严格加强。对 $Ny=0$ 的实际点，Galois 不变的
高度配对给准确平均
\[
 \sum_{j=1}^{p-1}\widehat h((\sigma^j-1)y)=2p\widehat h(y).
\]
故可逐次选择真实整数 $j_i\in\{1,\ldots,p-1\}$，令
$B_k=\prod_{i=1}^k(\sigma^{j_i}-1)$，使
\[
 \widehat h(B_kx)\le\left(\frac{2p}{p-1}\right)^kH_p.
\]
每个因子在 $\mathcal O$ 中赋值恰为一，且在 $V$ 上可逆，所以
$B_kx\ne0$、其局部赋值为 $a_p+k$。
对充分大的 $p$，取
\[
 k_p=\left\lfloor
       \log_{2p/(p-1)}\left(\frac{cp}{8C_X\log p}\right)
     \right\rfloor\ge0.
\]
若 $a_p+k_p\ge r/2$，同一 Gauss 论证会给非零整点
$\mathcal G B_{k_p}x/p$，其高度至多 $c/2$，仍然矛盾。因此
\[
 a_p+k_p<r/2,
 \qquad \operatorname{length}(\bar X_\ell)
       \ge(p+3)/2+k_p.
\]
这里 $k_p=\log_2p-\log_2\log p+O(1)$。
选择的差分步长来自实际 Galois 群；这个对数余量仍不改变下述算术缺口。

相同论证也适用于 R107 §5 的实际阶二子迹点
$Z_\ell=(1+\epsilon_\ell)X_\ell$：它来自另一固定有限映射，
仍有 $\widehat h(Z_\ell)=O(\log p)$ 和 $\Delta Z_\ell$ 非挠。
因此可在同一个小辅助素数上同时保持 $X_\ell,Z_\ell$ 的
$(p+3)/2$ 长度下界。

## 6. 所得加强及保留的算术条件

R107 用逐次高度估计 $4^k\widehat h(X)$ 得到约 $\log_2p$ 层。
本篇一次控制整个真实轨道的饱和格指数，再用整数 Gauss 算子，
将长度加强到 $(p+3)/2$。这不需要知道 $E(H)$ 的全部秩、完整调节子或 Sha。

但 [R104](2026-11-12-cyclic-heegner-augmentation-and-complete-reduction.md)
仍要求实际 $Q_{\ell,p}=\operatorname{Tr}_U X_\ell$ 在
$\ker N_p/\Delta\ker N_p$ 中非零，其中 $|U|=(\ell+1)/p$。
本篇不证明这个随 $\ell$ 变化的迹保留所建循环子模。
即使另已控制该迹，对范数零点 $Q$ 仍需最大可能的 $p-1$ 层：
模 $p$ 有
\[
 D_p=\sum_{j=1}^{p-1}j\sigma^j
       =-\sigma(\sigma-1)^{p-2},                     \tag{20}
\]
所以 $D_pQ\notin pE(L_p)$ 等价于 $\Delta^{p-2}\bar Q\ne0$。
(19) 只将真实指数压到半层以下，尚未把它压到所需极小值。
这里不把线性多层非零当作 Sha 有限性的完成证明。

## 7. 输入和独立核查

- 固定曲线、辅助域、Linnik 小辅助素数和 $O(\log p)$ 高度：R103、R105。
- 真实 $x=\Delta X$ 非挠、全部挠点为 $E[2]$：R107。
- Baker 一手定理及完整高度来源：R102 §1–2，链接见上。
- §2–5 的饱和格、体积界、局部指数、Gauss 算子和 Jordan 换算均在本文证明；
  两位研究者分别核查了整群归属、$p$ 饱和性及 $\mathcal O$ 指数规范。

# R575：实际六层 CM 成分的甲板方向、三次扭曲与根号更正

**状态：已证明。** 本文更正 R348 在由循环 $p^2$ 同源模型移到分裂／非分裂 $p$ 水平时所使用的甲板方向。实际中间椭圆曲线是 $E_{pz}$，故其六层 Hauptmodul 的尖点主阶是 $q^{-p/6}$，不能沿用 $E_z$ 上的 $q^{-1/6}$。因此实际未扭曲六层的 CM 微分满足 $\delta_\zeta^*\omega=\zeta\omega$。在正无穷型的 CM 嵌入下，实际 $a=\sqrt[3]4\,u$ 扭曲给出的角色是 $\Psi_\theta\kappa_4$，而非 R348 所写的 $\Psi_\theta\kappa_4^{-1}$。

这一真实家族的全局根号为 $-1$，其中心 $L$ 值恒为零。于是 R348 以另一扭向的正一阶矩推出本曲线有 CM 秩零商的结论撤回；依赖该出现性的后续零像应用也须撤回。本文不从根号 $-1$ 推出未证明的算术秩下界，不否定本曲线可能另有其他秩零商。有限型整格、实际 Gauss–Manin 换参以及另一 Hecke 家族自身的 $L$ 值恒等式不因此自动失效。

## 1. 固定规范与所更正的接口

令
$$
K=\mathbb Q(s),\quad s=\sqrt{-3},\quad
\zeta=(-1+s)/2,\quad \operatorname{Im}(s)>0,
\qquad p\ge41,\quad p\equiv5\pmod6.
$$
令 $\theta$ 满足 R348 的准确条件
$$
\theta(\zeta)=\zeta^{-1},\qquad \theta(s)=-1,
$$
并取未扭曲的新形式
$$
f_\theta=f_{\Psi_\theta},\qquad
\Psi_\theta((\alpha))=\alpha\epsilon_3(\alpha)\theta(\alpha\bmod p),
\qquad N(f_\theta)=9p^2.
\tag{575.1}
$$
这里无穷型为 $(1,0)$，与导子不互素的理想项取零。特别地
$$
a_n(f_\theta)=0\quad\text{除非 }n\equiv1\pmod3,
\qquad a_2=0,\quad a_4=-2.
\tag{575.2}
$$
取 Brau–Jones 的未扭曲六层
$$
X'(6)=\mathbb P^1_u,\qquad
j=2^{10}3^3u^3(1-4u^3),\qquad
\delta_\zeta:u\longmapsto\zeta u.
\tag{575.3}
$$
实际曲线为
$$
Z_p=\operatorname{Norm}(X_{\rm ns}^+(p)\times_j\mathbb P^1_a),
\qquad j=6912a^3(1-a^3).
\tag{575.4}
$$
若 $\alpha^3=4$，同构 $\iota:Z_p\to Z'_p$ 为 $u=a/\alpha$。以下所有 $\kappa_4$ 均按算术 Frobenius 的互反规范，
$\kappa_4(\sigma)=\sigma(\alpha)/\alpha$。

R348 在循环 $p^2$ 模型上取的二旧向量为
$$
h_0(z)=f_\theta(z/6),\qquad
h_1(z)=f_\theta(z/3),\qquad
h_2(z)=f_\theta(2z/3).
\tag{575.5}
$$
它们在 $\Gamma(6)\cap\Gamma_0(p^2)$ 上模。其模二型为
$1\oplus\operatorname{Std}$，平凡线是 $h_1$，标准平面是
$\langle h_0,h_2\rangle$。$H_6$ 不变线在标准平面内，重数一。
这些表示论陈述并非错误所在；错误在下一步把运输到中间椭圆曲线的六层函数仍写成 $u(z)$。

## 2. 运输到中间椭圆曲线后的准确尖点阶

写 $E_z=\mathbb C/(\mathbb Zz+\mathbb Z)$，并在循环 $p^2$ 模型取
$C_{p^2}=\langle1/p^2\rangle$。其唯一阶 $p$ 子群为
$C_p=\langle1/p\rangle$。商椭圆曲线的格是
$$
\mathbb Zz+\frac1p\mathbb Z;
$$
乘以 $p$ 后得到 $\mathbb Z(pz)+\mathbb Z$，所以
$$
E_z/C_p\simeq E_{pz}.
\tag{575.6}
$$
这也是由循环 $p^2$ 同源变成有序互补 $p$ 子群的标准模解释。沿同源运输模六标记以后，忘去 $p$ 结构的 $j$ 函数因而是 $j(pz)$。运输改变 Weil 配对的值，但不会把中间椭圆曲线重新变回 $E_z$。

固定的模六配对分量校正可能改变 $u$ 的六个解析分支。下面的计算不要求先给这项校正选一个矩阵。设 $q=e^{2\pi iz}$，而 $U(z)$ 是实际运输后六层函数的任一分支。由 (575.3) 及 $j(pz)=q^{-p}+744+\cdots$，在尖点它具有 Puiseux 展开
$$
U(z)=c\,q^{-p/6}H(q^{p/2}),\qquad c\ne0,\quad H(0)=1.
\tag{575.7}
$$
可先对 $U^3$ 解二次方程，再取三次根，直接得到该式；六个分支均有同一主阶。等价地，$X'(6)$ 只有一个 cusp，宽为六，固定 tame coset 可以选用 $T^r$ 代表，故可写成相应的 $u(pz+r)$ 分支。

令 $n_0=T^{2p^2}$。因为 $p^2\equiv1\pmod6$，它在模六为 $T^2$，且在模 $p^2$ 为恒等。将 $z$ 换成 $z+2p^2$，(575.7) 中的 $q^{p/2}$ 不变，而主项乘
$$
\exp\!\left(-\frac{2\pi i\cdot p\cdot2p^2}{6}\right)
=\zeta^{-p^3}=\zeta.
$$
因此准确地有
$$
U(z+2p^2)=\zeta U(z).
\tag{575.8}
$$
即 $n_0$ 在**中间椭圆曲线的实际六层**上给 $\delta_\zeta$，而非 $\delta_\zeta^{-1}$。

另一方面，由 (575.2)，在 (575.5) 的标准平面上
$$
h_i(z+2p^2)=\zeta h_i(z)\qquad(i=0,2).
\tag{575.9}
$$
于是对应微分在实际六层上的甲板特征是 $\zeta$。
R348 §5 将同一个 $n_0$ 代入了 $u(z)\sim cq^{-1/6}$，得到 $\zeta^{-1}$；这个计算针对原椭圆曲线的六层，不能用于 (575.6) 的中间椭圆曲线。

## 3. 在完整 $6p$ 水平上的第二种直接核对

这一节避免使用上一节的任何分支选择。取 full-$6p$ 解析变量 $\tau$，以及
$$
H_0=f_\theta(\tau/(6p)),\qquad
H_1=f_\theta(\tau/(3p)),\qquad
H_2=f_\theta(2\tau/(3p)).
\tag{575.10}
$$
这些是同一新形式在完整水平上的三个 tame 二旧方向。取与全部模 $p$ 群交换的 CRT 元素
$$
n=T^{4p};\qquad n\bmod6=T^2,\quad n\bmod p=I.
$$
在标准平面上，Fourier 支撑 (575.2) 直接给
$$
H_0|_2n=\zeta^2H_0,\qquad H_2|_2n=\zeta^2H_2.
\tag{575.11}
$$
现在忘 $p$ 的椭圆曲线确实是 $E_\tau$，故六层函数的展开是
$u(\tau)=c q^{-1/6}H(q^{1/2})$。同一元素 $n$ 作用为
$$
u(\tau+4p)=\exp(-2\pi i\,4p/6)u(\tau)
=\zeta^{-1}u(\tau).
\tag{575.12}
$$
因而 $n=\delta_\zeta^{-1}$，(575.11) 再次给
$$
\boxed{\delta_\zeta^*\omega_\theta=\zeta\omega_\theta.}
\tag{575.13}
$$
非分裂 Cartan／正规化子投影只作用在模 $p$ 因子，与这个 tame 元素交换，所以 (575.13) 在实际 $H_6\times N_{\rm ns}$ 不变线上保持。该标准 tame 方向唯一；平凡模二方向的非平凡模三特征没有 $H_6$ 不变量。有限群型的不变空间存在性与 R348/R434 使用的同一表示论一致。

这也定位了群共轭中的翻转。$D=\operatorname{diag}(p,1)$ 把
$\Gamma_0(p^2)$ 变成 split-$p$ 群；其模六行列式为 $-1$。若用模六图式中的 $h$、$\det h=-1$ 校正配对分量，再取 $g\equiv hD^{-1}\pmod6$，则原模三 $C_3$ 甲板元 $n_3$ 变成
$$
gDn_3(gD)^{-1}=hn_3h^{-1}=n_3^{-1}
\quad\text{在图式商 }C_3\text{ 中}.
\tag{575.14}
$$
仅仅核对两次同源的复合 $[p]\equiv-I\pmod6$，不足以消去这一次的行列式翻转。

## 4. Gauss 内扭算子确定整个有理因子的正 CM 嵌入

不能只凭一条数值 $q$ 级数给 $K$ 的作用改名。这里在整个 CM isotypic 部分确定其归一化。

在 $X_0(9p^2)$ 上令
$$
U_0:z\longmapsto z+1/3,\qquad R_0=U_0^*- (U_0^2)^*.
\tag{575.15}
$$
$U_0$ 规范化 $\Gamma_0(9p^2)$。事实上，对
$\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，共轭后的右上项为
$b+(d-a)/3-c/9$；$9\mid c$，且 $a\equiv d\pmod3$，故它为整数，其余所需同余也保持。$U_0^3$ 属于整数平移群。

令 $\chi=\chi_{-3}$。使用 $\zeta=e^{2\pi i/3}$ 时准确 Gauss 和为
$$
\tau(\chi)=\sum_{a=1,2}\chi(a)\zeta^a=\zeta-\zeta^2=s.
\tag{575.16}
$$
因此对所有 Fourier 系数同时有
$$
R_0f_\theta
=\sum_n a_n\left(\sum_{a=1,2}\chi(a)\zeta^{an}\right)q^n
=s\sum_n\chi(n)a_nq^n=s f_\theta.
\tag{575.17}
$$
该恒等式对 $f_\theta$ 的**每个系数嵌入**都成立：支撑条件
$n\equiv1\pmod3$ 在全部嵌入下保持。相应反 holomorphic 空间上取值为 $-s$。于是 $R_0^2=-3$ 于整个有关有理 Hodge 因子上，且
$$
[\zeta]=\frac{-1+R_0}{2}
\tag{575.18}
$$
给正 holomorphic CM 型。这个归一化与 (575.1) 的无穷型 $(1,0)$ 相容；其共轭型在反 holomorphic 方向。

这里的代数下降也可直接检查。$U_0$ 是标准有理矩阵给出的模曲线自同构，在 cusp 上作用为 $q\mapsto\zeta q$。模曲线的代数 $q$ 展开原则给
$$
\sigma(U_0)=U_0^{\chi(\sigma)},\qquad
\sigma(R_0)=\chi(\sigma)R_0.
\tag{575.19}
$$
所以 (575.18) 是在 $K$ 上的 CM 嵌入，外侧 Galois 按复共轭作用；没有把一个只在选定 Weil 配对分量上写出的矩阵误称为全局 $\mathbb Q$ 自同构。

还可在 (575.10) 的完整三旧空间核对归一化。令
$U=T^{2p}$，则
$$
U:(H_0,H_1,H_2)\longmapsto
(\zeta H_0,\zeta^2H_1,\zeta H_2).
$$
令 $P_{\rm triv}$ 为模二群平均，即投到 $H_1$ 的有理投影。正 CM 算子在这个三重空间的完整表达式为
$$
R_{\rm can}=(1-2P_{\rm triv})(U-U^2).
\tag{575.20}
$$
它在全部三个 holomorphic 二旧方向上都是 $+s$，在反 holomorphic 方向上都是 $-s$。这与分别沿三个代数 degeneracy maps 运输 (575.15) 所得到的对角 CM 作用一致；特征零中 endomorphism 在 Hodge 实现上的忠实性保证二者相同。

这些比较可在包含全部 Weil 配对分量的完整水平模问题上作出，因而不留下一个隐含的 Galois 校正。完整基指定的循环子群、取商及对偶同源均定义在 $\mathbb Q$ 上。例如 $H_0$ 的映射先取 $\langle\tau/(6p)\rangle$ 的商，再经对偶同源取另一指定子群的逆像，得到循环 $(6p)^2$ 结构，最后忘掉所需的二部分。$H_1,H_2$ 由同一构造及指定的二同源得到。因此沿这些映射运输的 $R_0$ 仍满足 (575.19)。式 (575.20) 是它在选定复分量上的表达式；在别的配对分量上应运输同一代数算子，而不是把该复矩阵逐字当作 $\mathbb Q$ 上的固定算子。

模 $p$ 有限群与 (575.20) 的 tame 算子交换，故该识别扩展到完整 $p$ 型及全部 Hecke 系数嵌入。$H_6$ 不变方向位于标准平面，$P_{\rm triv}=0$；而此处 $U=\delta_\zeta$。由 (575.20) 和 $U^2+U+1=0$，得到
$$
\delta_\zeta=\frac{-1+R_{\rm can}}2=[\zeta].
\tag{575.21}
$$
这证明 (575.13) 对应的确是正无穷型的 $K$ 嵌入，而非把原来的 $K$ 角色在一个基向量上任意共轭。

## 5. 对整个 Galois 表示作三次下降

曲线同构本身的 cocycle 仍为
$$
\sigma(\iota)=\delta_{\kappa_4(\sigma)^{-1}}\,\iota.
$$
因此在使用 $\iota_*$ 识别的 Tate 空间上，准确关系是
$$
\iota_*\rho_{\rm act}(\sigma)\iota_*^{-1}
=\delta_{\kappa_4(\sigma),*}\rho_{\rm can}(\sigma).
\tag{575.22}
$$
可直接对一点 $P$ 核验：
$\sigma(\iota(P))=\delta_{\kappa^{-1}}\iota(\sigma P)$。

由 §4，在 $G_K$ 的正 CM 特征线上，$\delta_{\kappa}$ 取值为
$\kappa$；共轭线上取值为 $\kappa^{-1}$。于是整个限制表示的两条线为
$$
\psi_\theta\kappa_4\ \oplus\ 
\psi_\theta^c\kappa_4^{-1}.
\tag{575.23}
$$
外侧 $G_{\mathbb Q}$ 交换这两条线，且
$\kappa_4^c=\kappa_4^{-1}$，所以整个有理 CM 因子的准确表示为
$$
\boxed{\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}
(\psi_\theta\kappa_4).}
\tag{575.24}
$$
也就是说，实际新形式家族为
$$
g_\theta^{\rm act}=f_{\Psi_\theta\kappa_4}.
\tag{575.25}
$$
这不是只在一条复微分上的识别：§4 已同时控制所有系数嵌入、两种 Hodge 型及 CM endomorphism 的外侧 Galois 共轭，(575.22) 则对整个 Tate 表示成立。

不能通过改变 $\theta$ 的系数嵌入把 (575.25) 改成
$f_{\Psi_{\theta'}\kappa_4^{-1}}$：$\theta'$ 只在 $p$ 处分歧，而两种 $\kappa_4$ 在 $2,3$ 的方向不同。若交换两条诱导角色，还必须同时共轭无穷型；这同样不会把整个表示的 (575.24) 变成 R348 所写的另一扭向。

## 6. 准确导子与根号

有限导子的指数仍为
$$
\mathfrak f(\Psi_\theta\kappa_4)=(2)(s)^2(p),
\qquad N(g_\theta^{\rm act})=108p^2.
\tag{575.26}
$$
在 $2$ 处是非平凡 tame 三次角色，在 $3$ 处是导子二的三次角色乘导子一的二次角色，在 $p$ 处仍是导子一的非平凡 $\theta$；这些指数没有相消。Nebentypus 仍平凡。

沿用 R348 §6 已逐项固定的加性角色和算术互反规范。为避免依赖原文的最后符号结论，这里把唯一改变的局部 Gauss 和完全写出。

在 $p$，$\kappa_4$ 平凡，局部根号仍为 $+1$。在 $2$，两种非平凡剩余三次角色的 Gauss 和都为
$1-\zeta-\zeta^2=2$，未分歧角色在 uniformizer $2$ 上为 $-1$，故局部根号仍为 $-1$。

在 $3$，原单位化角色 $\nu$ 满足
$$
\nu(-1)=-1,\quad \nu(1+s\mathcal O_3)=1,\quad
\nu(s)=-i.
$$
并且
$$
\kappa_4(1+s)=\zeta,\qquad\kappa_4(s)=1.
$$
实际 $\xi=\nu\kappa_4$ 的导子为二，故
$$
\xi(\varepsilon(1+ts))=\varepsilon\zeta^t,
\qquad\xi(s^3)=i
\quad(\varepsilon=\pm1,\ t=0,1,2).
$$
加性角色在 $s^3$ 的分母上给 $\zeta^{\varepsilon t}$，于是完整和为
$$
\sum_{\varepsilon=\pm1}\sum_{t=0}^2
\varepsilon\zeta^{-t}\zeta^{\varepsilon t}
=3.
\tag{575.27}
$$
其中 $\varepsilon=1$ 的三个项都为一，$\varepsilon=-1$ 的三个项之和为零。域 $K_3$ 上的 epsilon 因子为 $i\cdot3/3=i$；二次诱导常数是 $i$，所以
$$
\epsilon_3(g_\theta^{\rm act})=-1.
$$
权二的无穷根号为 $-1$。所有其余有限处未分歧，故
$$
\boxed{w(g_\theta^{\rm act})
=(-1)_\infty(-1)_2(-1)_3(+1)_p=-1.}
\tag{575.28}
$$
函数方程即给 $L(g_\theta^{\rm act},1)=0$，对全部本族 $\theta$ 都成立。

## 7. 对既有结论和当前研究的准确影响

1. R348 中 $f_{\Psi_\theta\kappa_4^{-1}}$ 的准确导子、根号 $+1$ 及其正一阶矩，是关于该 Hecke 家族自身的陈述；本文不否定那些算术恒等式。被更正的是它与实际 $Z_p$ CM 成分的识别。因此 R348 的实际 CM 秩零商结论及由它得到的实际有理零像应用撤回。
2. R374/R390 中关于指定 CM 角色的局部表示、完整 BT 群、惯性权等独立论证，应把“是哪一个实际全局商”的依赖单列。两种 $\kappa_4$ 在 $p$ 都平凡，所以该处的有限型不因本更正改变；但实际秩零和有理零像不能由另一家族的非零中心值转用。
3. R434 §§1–4 的有限群整格、Cartan 平均本原性仍是同一 $p$ 型的结论；其形式对数的尺度不变引理也保持。把该型称为实际秩零商的那部分依赖须按本更正撤回。
4. R560/R566/R569 及后续固定 $E_0$ 的 $L$ 值、Cartier 或 Kronecker 计算若仅关于其已指定的 Hecke 家族，仍保留原数学范围；它们不能继续充当 (575.25) 的非零中心值。
5. R571 已有的 $ST$ 稳定子消失阶、实际 Gauss–Manin／Kodaira–Spencer 递推，以及 $[a-1]\int\omega_F=\delta^2F/16$ 的换参公式是局部代数陈述，不使用秩零。既有复数 probe 保留为数值证据；它不构成 $p$ 进本原首项证明，也不再被宣称已经接到 R348 的秩零商。

这次更正不影响 $p=41$ 的实际 QC 有限计算。主要 Serre 一致性目标仍未完成；后续必须寻找另一个实际全局零像来源，或者改走不要求此 CM 商秩零的路线。

## 8. 输入与可复核范围

- R348：只使用其准确 theta 角色、Fourier 支撑、tame $1\oplus\operatorname{Std}$ 分解及已逐项给出的局部角色数值。本文独立重算其有问题的实际 deck 接口、完整 CM 归一化和最后根号。
- R434 的工作稿同时给有限 $p$ 型与 tame 群交换、非分裂不变线的整构造，便于对照影响范围；本篇不需要其本原性结论来证明扭曲取向，也不以尚未发布的该稿作为必需先决条件。不变空间存在性可直接用下列 Mercuri–Schoof 的有限型描述或 R348 中未涉 deck 方向的 Chen 同源对象恒等式。
- J. Brau–N. Jones, *Elliptic curves with 2-torsion contained in the 3-torsion field*, Proc. Amer. Math. Soc. 144 (2016), 925–936，Theorem 1.4，给 (575.3) 的实际 $H_6$ 曲线。[作者稿](https://homepages.math.uic.edu/~ncjones/2tin3t.pdf)。
- B. de Smit–B. Edixhoven, *Sur un résultat d'Imin Chen*, Math. Res. Lett. 7 (2000), 147–154，Theorem 2(2)，用于既有带 tame 层的同源对象恒等式；本文不再将其等同于未核方向的 deck 交换。[作者稿](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)。
- P. Mercuri–R. Schoof, *Modular forms invariant under non-split Cartan subgroups*, Math. Comp. 89 (2020), 1969–1991，§4、Proposition 6.3，给实际 finite-type Cartan 投影；本文的 tame 平移与 Gauss 归一化逐式证明。[作者稿](https://reneschoof.github.io/mcom3503.pdf)。

本篇是纯证明，不需要重跑任何长群链、QC Norm 或复数识别。没有把未执行的计算列为已执行。

# R1066：原 $p$-进圆盘的有界判别式 CM 代表

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明：设 $p>37$。原完整 $X=X_{\rm ns}^+(p)$ 的每个
$\mathbf Q_p$ 剩余圆盘，都含有一个实际 $\mathbf Q_p$-CM 点，
其 CM 整环的判别式 $-D'$ 满足**
$$
0<D'\le \frac4{\sqrt3}p^{3/2},\qquad
p\nmid D',\qquad \left(\frac{-D'}p\right)=-1.
\tag{1066.1}
$$
这里的圆盘是 R1065 原最小正则模型的一个
$\mathcal M^{\rm sm}(\mathbf F_p)$ 点之管状邻域。
因此原规范 cuspidal Kummer 的整个 $p$-局部点像，准确等于
这些有界判别式 CM 点的局部标签集合。

这些 CM 点一般具有大于一的全局次数。
本篇没有把它们称为 $\mathbf Q$-有理 CM 点，也没有从局部代表
推出一个 $\mathbf Q$-全局 torsor 标签。
主目标 O0 及真正同一全局标签的辅助素数条件仍然开放。

## 1. 原曲线、模型与实际对象

沿 R1065 记 $\mathcal M/\mathbf Z_p$ 为原 $X$ 的最小正则模型。
每个 $\mathbf Q_p$ 点唯一延成 section，并落在特殊纤维的 smooth locus。
其几何连通分量为各超奇异 $j$ 标记 $s$ 对应的
$$
F_s^\circ\simeq\mathbf A^1,\qquad
F_s\setminus F_s^\circ=\{z\}.
\tag{1066.2}
$$
$z$ 是已经收缩的非约化树的唯一像。
只有 $s\in\mathbf F_p$ 的分量含 $\mathbf F_p$ 点。
本篇始终覆盖全部四个 $p\bmod12$ 行，不只处理原 $X_1$ 的偶支。

固定一个 $s\in\mathbf F_p$，取一个实际
$E_s/\mathbf F_p$，$j(E_s)=s$。
它的几何端同态环
$$
R=\operatorname{End}_{\overline{\mathbf F}_p}(E_s)
$$
是 $B_{p,\infty}$ 的最大整环。
实际 $p$-Frobenius $\pi$ 满足 $\pi^2=-p$。
在需要时改变 $E_s$ 的 $\mathbf F_p$-twist；
每一次都重新使用该模型自身的实际 $\pi$，不沿用另一 twist 的矩阵。

本文只用两个已刊输入和既成局部环：

1. Edixhoven–Parent 2024 的原 full-level / normalizer 正则模型，
   特别是 Eq. (3.8)、有限固定点 $(X,Y)=(0,0)$ 的 blowup，
   以及 §3.4 的 coarse 稳定子商。下面给出实际所用 chart。
2. Ibukiyama 1982 的最大整环基与 optimal-embedding 分类，
   以及 Kaneko 1989 §2 中的二元 norm 格。下面重新计算 Gram determinant，
   并补上保持实际 Frobenius 的 pair 条件。
3. R1021 §§1–4 的同一 height-two Drinfeld 变形环、
   真正 framing eigenparameters 和整个非约化模 $p$ 仿射模型。
   R1052 §6 已使用其 source 版本；此处给任意超奇异细点的短证明，
   不借特定 $j=0$ 参数代替一般来源。

## 2. 保持实际 Frobenius 的二元 Gross 格

置
$$
\Lambda=\{\eta\in(2R+\mathbf Z):
 \operatorname{trd}(\eta)=0,\quad \pi\eta=-\eta\pi\},
\qquad Q(\eta)=\operatorname{nrd}(\eta).
\tag{1066.3}
$$
这是正定秩二整格。对非零 $\eta$，$Q(\eta)$ 是正整数。
若 $D=Q(\eta)$，则
$$
\gamma=(D+\eta)/2\in R,\qquad
\gamma^2-D\gamma+(D^2+D)/4=0.
\tag{1066.4}
$$
所以 $\mathbf Z[\gamma]$ 是判别式 $-D$ 的二次整环。

### 2.1 为什么分类可以保留指定 $\pi$

$R\cap\mathbf Q(\pi)$ 或为 $\mathbf Z[\pi]$，
或在 $p\equiv3\bmod4$ 时为 $\mathbf Z[(1+\pi)/2]$。
按这一个**实际 optimal order**，使用 Ibukiyama Theorem 1 或 2。
原文 Lemma 3.2（印刷 pp.191–192）还给出固定 optimal order
到该最大整环的 unit-conjugacy 类数：
单位群为 $\{\pm1\}$ 或 $\mu_6$ 时为二，单位群为 $\mu_4$ 时为一。
前两种由 $\alpha$ 与 $-\alpha$ 两个嵌入代表。
在 $\mu_6$ 情形，$\alpha u\alpha^{-1}=\bar u$，
而 $-1$ 不是 $\mu_6$ 中的平方，故这两类确实不同。
在 $\mu_4$ 情形同一个 optimal order 的嵌入均在一类中。

因此可将分类所得的整环同构再作一个内部 unit 共轭，
使原 $\pi$ 对应 $\alpha$ 或 $-\alpha$。
二者的 anti-commuting 格相同。
这一步禁止把“某个含 $\sqrt{-p}$ 的最大整环”误当成指定
$(R,\pi)$；特别是 $j=1728$ 的两个 $\mathbf F_p$-twist
按各自的 optimal order 分别处理。

### 2.2 两种实际基与 determinant

在
$$
B=\mathbf Q+\mathbf Q\alpha+\mathbf Q\beta+\mathbf Q\alpha\beta,
\quad \alpha^2=-p,\quad\beta^2=-q,\quad
\alpha\beta=-\beta\alpha
$$
中，Ibukiyama 的第一种整环是
$$
O(q,r)=\mathbf Z+
 \mathbf Z(1+\beta)/2+
 \mathbf Z\alpha(1+\beta)/2+
 \mathbf Z(r+\alpha)\beta/q,
\quad r^2+p\equiv0\pmod q.
$$
取 $2\gamma-\operatorname{trd}(\gamma)$ 后，
anti-$\alpha$ 条件准确消去 $\alpha(1+\beta)/2$ 的系数。
所得全格为
$$
\eta=\left(x+\frac{2rz}{q}\right)\beta+
       \frac{2z}{q}\alpha\beta,\qquad x,z\in\mathbf Z,
$$
$$
Q(\eta)=qx^2+4rxz+\frac{4(r^2+p)}qz^2.
\tag{1066.5}
$$
其 norm Gram matrix 的 determinant 是 $4p$。

第二种（只在 $p\equiv3\bmod4$）为
$$
O'(q,r')=\mathbf Z+
 \mathbf Z(1+\alpha)/2+\mathbf Z\beta+
 \mathbf Z(r'+\alpha)\beta/(2q),
\quad r'^2+p\equiv0\pmod{4q}.
$$
anti-$\alpha$ 条件消去 $(1+\alpha)/2$ 的系数，给
$$
\eta=\left(2y+\frac{r'z}{q}\right)\beta+
       \frac zq\alpha\beta,\qquad y,z\in\mathbf Z,
$$
$$
Q(\eta)=4qy^2+4r'yz+\frac{r'^2+p}qz^2.
\tag{1066.6}
$$
其 Gram determinant 也为 $4p$。
这里 Gram matrix 指
$Q(X,Y)=aX^2+2bXY+cY^2$ 的矩阵
$\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)$；
不把它与二元 quadratic discriminant $4b^2-4ac$ 混用。

(1066.5) 的 norm 满足 $D\equiv x\bmod2$，
(1066.6) 的 norm 为 $4$ 的倍数。
这也直接核准 (1066.4) 的整性与判别式。
由 (1066.3) 是整线性条件的 kernel，并且 $2$ 在 $\mathbf Z_p$ 中可逆，
$$
\Lambda\otimes\mathbf Z_p
=\{\eta\in R\otimes\mathbf Z_p:\pi\eta=-\eta\pi\}.
\tag{1066.7}
$$
右端的 trace-zero 条件自动成立。特别地，$\Lambda$ 在此局部格中饱和。

### 2.3 二维 Hermite 界的准确常数

若正定秩二整格的 Gram determinant 为 $\Delta$，取最短 primitive
向量 $v$，补成基 $v,w$，并用 $w\mapsto w+nv$ 使
$|\langle v,w\rangle|\le Q(v)/2$。
最短性给 $Q(w)\ge Q(v)$，于是
$$
\Delta\ge \tfrac34Q(v)^2,\qquad
Q(v)\le \frac2{\sqrt3}\sqrt\Delta.
\tag{1066.8}
$$
对 $\Lambda$ 得一个非零 $\delta$，其 norm
$D_0\le4\sqrt{p/3}<p$。
所以 $\delta$ 是局部 unit，$\mathbf Z_p[\delta]$ 是不分歧二次整环。
特殊 $j=0,1728$ 时，也可直接取原 CM 自同构给出的
$\delta=\sqrt{-3}$ 或 $2i$ 作为 reference；
它们都 anti-commute 原 $\pi$，且在 $p>37$ 时为 unit。

## 3. 任意指定的一阶 good deformation 都有短 CM 提升

### 3.1 原晶体的整矩阵

只在本节使用 contravariant $H^1_{\rm cris}$ 晶体。
在 $W(\mathbf F_{p^2})$ 上取原 Frobenius endomorphism 的线性作用
$\Pi=\pi^*$。其平方为 $-p$。
选上一节的 reference $\delta$，令
$s_0^2=\delta^2\in\mathbf Z_p^\times$，
$s_0^\sigma=-s_0$。
实际 arithmetic descent 将 $\delta^*$ 变为 $-\delta^*$，
故 $\delta^*/s_0$ 是 descent-invariant 的整 involution。

可以在 descent-invariant 的两条整 eigenline 上取基 $e_1,e_2$，
使
$$
\Pi=
 \begin{pmatrix}0&-p\\1&0\end{pmatrix},
\qquad
\delta^*=
 \begin{pmatrix}s_0&0\\0&-s_0\end{pmatrix},
\qquad
\operatorname{Fil}_{\rm special}=\mathbf F_{p^2}e_2.
\tag{1066.9}
$$
具体地，先在非 Hodge 的那条 eigenline 取 primitive $e_1$，
再令 $e_2=\Pi e_1$；
$\ker(\overline\Pi)$ 是特殊 Hodge line，而 $\Pi$ 的 determinant 是 $p$，
所以 $e_2$ primitive，且这些式子成立。
两条 eigenline 在 descent 后定义于 $\mathbf Z_p$。

局部 division maximal order 为
$$
\mathcal O_{\mathbf Q_{p^2}}\oplus
 \mathcal O_{\mathbf Q_{p^2}}\Pi,\qquad
\Pi a=a^\sigma\Pi,\quad\Pi^2=-p.
$$
因此每个 $\eta\in\Lambda\otimes\mathbf Z_p$ 有唯一的**晶体坐标**
$$
\eta^*=\delta^*(u+v\Pi),\qquad u,v\in\mathbf Z_p,
$$
$$
\eta^*=
 \begin{pmatrix}s_0u&-s_0pv\\-s_0v&-s_0u\end{pmatrix}.
\tag{1066.10}
$$
这里直接以 $\eta^*$ 定义 $u,v$；pullback 是反同态，
故不把本式未经反序写成几何端同态的相同乘积。
由 (1066.7)，$\eta\mapsto(u,v)$ 给整个局部格的整坐标。

### 3.2 只使用模 $p^2$ 的 period 比较

在 canonical $(p)$-PD thickening 上，Grothendieck–Messing
把一阶 good deformation 的 Hodge line 写为
$$
\langle e_2+z e_1\rangle,\qquad z\in pW/p^2W.
$$
该 line 被 (1066.10) 保持当且仅当
$$
2uz-pv=0\pmod {p^2}.
\tag{1066.11}
$$
例如直接将矩阵作用于 $(z,1)$，全代数稳定条件是
$vz^2+2uz-pv=0$；这里只读取模 $p^2$，
不将该二次式冒称为整个椭圆 deformation 的全精确 period 坐标。

固定 $t\in\mathbf F_p$，置
$$
\Lambda_t=\{\eta\in\Lambda:v\equiv2tu\pmod p\}.
\tag{1066.12}
$$
这是 index $p$ 子格，Gram determinant 为 $4p^3$。
(1066.8) 给非零 $\eta_t\in\Lambda_t$，满足
$$
D=Q(\eta_t)\le4p^{3/2}/\sqrt3<p^2.
\tag{1066.13}
$$
若 $\eta_t\in p\Lambda$，正整 norm 的最小值至少为一，
故 $D\ge p^2$，矛盾。
结合 (1066.12) 得 $u\in\mathbf Z_p^\times$。
于是 $p\nmid D$，且 $-D\bmod p$ 是非平方；
$\mathbf Z_p[\eta_t]$ 为不分歧二次整环。
其唯一与特殊 Hodge 相容的 eigenline 满足
$$
z/p\equiv t\pmod p.
\tag{1066.14}
$$

### 3.3 实际 CM lift 与 $\mathbf Q_p$ 下降

不分歧二次整环的两整 idempotent eigenline 是 direct summands，
特殊 Hodge line 选择其中唯一一条。
在各 $W/p^nW$ 上用 Grothendieck–Messing 的对象及态射判据，
得到唯一保持该整环作用的 compatible deformation。
等价地，这是 height-one formal
$\mathcal O_{\mathbf Q_{p^2}}$-module 的唯一 unramified CM deformation。
Serre–Tate 将它识别为原 $E_s$ 的实际椭圆 deformation。

因原 $\pi\eta_t\pi^{-1}=-\eta_t$，
arithmetic descent 将该作用变为其二次共轭；
保持 $\eta_t$ 与保持 $-\eta_t$ 的 Hodge 条件相同。
上述唯一性给与原 $E_s/\mathbf F_p$ 相容的 arithmetic descent，
所以 underlying elliptic lift 定义于 $\mathbf Z_p$。
这里不声称 $\eta_t$ 本身是 $\mathbf F_p$-端同态；
它定义于二次未分歧扩张。

原 $\gamma=(D+\eta_t)/2$ 也随 CM 作用提升。
Deuring lifting / CM 理论给其 $j$ 为全局 singular modulus。
完整 geometric CM ring 可以是 $\mathbf Z[\gamma]$ 的 overorder；
若其判别式为 $-D'$，则
$$
D'=D/f^2\le D,\qquad p\nmid fD',
\qquad (-D'/p)=-1.
\tag{1066.15}
$$
也可先取 Deuring 的代数 CM lift，再用局部不分歧 CM deformation
的唯一性与上述 actual lift 识别。
因此得到的是实际 $\mathbf Q_p$-CM 椭圆曲线，而不是只在特殊纤维
写下一个二次格向量。

若 $u_{\rm base}$ 是任一原未分歧 fine elliptic deformation 参数，
reference CM lift 的值为 $u_{\rm ref}\in p\mathbf Z_p$。
Kodaira–Spencer 非零给
$$
\frac{u_{\rm base}}p\equiv
 \frac{u_{\rm ref}}p+a\,\frac zp\pmod p,
\qquad a\in\mathbf F_p^\times.
\tag{1066.16}
$$
所以 (1066.14) 覆盖该参数的每一个可能一阶值。
不假定 EP 的参数零点恰好等于任取短 $\delta$ 的 reference CM lift。

## 4. 原 $F_s^\circ$ 坐标确由这一阶 deformation 读取

以下将 §3 的参数与原 $X_{\rm ns}^+(p)$ 模型相接。
只知道 underlying $j$ 约化为 $s$ 不能完成这一步。

### 4.1 原 finite fixed point 的 blowup chart

先在 prime-to-$p$ fine 辅助问题上工作。
EP Eq. (3.8) 的 normalizer Drinfeld 尾为
$$
Y^2=X\bigl(X^{(p+1)/2}+A\bigr),\qquad A\ne0.
\tag{1066.17}
$$
在有限固定点 $(X,Y)=(0,0)$，$Y$ 是 regular parameter。
该尾在
$$
\tau^{p+1}=p
$$
后有 multiplicity one。
EP 的 Kummer Galois 作用在 $(\tau,Y)$ 上是同一个
$\mu_{p+1}$ scalar；原文 printed pp.1028–1029 给此作用，
并以 Eq. (3.6) 后的 blowup 计算处理该点。

在完整局部环 $W[\tau][[Y]]$，不变量由
$\tau^{p+1-i}Y^i$，$0\le i\le p+1$ 给出。
令 $B_i=\tau^{p+1-i}Y^i$，$B_0=p$。
吹起 $(B_0,\ldots,B_{p+1})$ 后，在 $p$-chart
$$
B_i/p=(Y/\tau)^i.
$$
所以该 chart 是 $W[t]$ 的相应完成，其中
$$
t=Y/\tau.
\tag{1066.18}
$$
其特殊纤维是 $F_s^\circ\simeq\mathbf A^1_t$，
唯一缺少的无穷点接原非约化 Drinfeld 树。
后续收缩不改变这个开。
这是实际 chart 的有理函数等式，不只是任选一个
$\mathbf A^1$ 同构。

### 4.2 任意 SS fine 点的 source Dickson 初项

记 $e_{\rm full}=p^2-1$，$\varpi^{e_{\rm full}}=p$，
$\tau=\varpi^{p-1}$。
在 R1021 同一个实际 full-level regular ring 中，
$x=T(P),y=T(Q)$ 是 framing 权一的 eigenparameters。
原 source parameter $u_{\rm base}$ 的 framing 权为 $1-p$。
可选由 §3 reference 不分歧二次整环给出的 arithmetic-stable framing torus：
arithmetic Frobenius 共轭该 torus，并同时对 Teichmüller coefficients 作 Frobenius，
所以从一个 $\mathbf Z_p$ 参数作 character 平均后仍可保 arithmetic descent。
先在通用 height-two deformation ring 上平均，再取 Cohen 代表，
其全部齐次次数只能为
$$
r_0+j e_{\rm full},\qquad r_0=p(p-1),\quad j\ge0.
\tag{1066.19}
$$
这是 universal height-two formal group 的作用；
不要求原椭圆曲线拥有 $\mu_{p^2-1}$ 的全局代数自同构。

最低项可直接由同一 root product 核定。
Weierstrass preparation 将 $[p](T)$ 写为一个 unit 乘
$\prod_{v\in\mathbf F_p^2}(T-T(v))$。
$T(v)$ 的 linear leading 是 $ax+by$。
其 $T^p$ coefficient 的最低 total degree 为 $p^2-p=r_0$，
准确是 Dickson polynomial 的非零常数倍。
其它低于 $T^p$ 的根多项式系数的 total degree 更高，
不会改变这个初项。
$[p](T)$ 的 $T^p$ coefficient 是 Hasse 简单 deformation 参数的单位倍；
平均保持其非零 leading。
因此代 $x=\varpi\alpha,y=\varpi\beta$ 后，
$$
u_{\rm base}=\tau^p(c_D\mathcal D+pR),\qquad c_D\in W^\times,
$$
$$
\mathcal D=
 \frac{\alpha^{p^2}\beta-\alpha\beta^{p^2}}
      {\alpha^p\beta-\alpha\beta^p}.
\tag{1066.20}
$$
(1066.19) 是误差为 $pR$ 的理由；
仅有根的 linear leading 本身不能给这个精度。
$R$ 在原 affine tail 的邻域正则，当前点不在节点。

这里分开两种作用。
R1021 的 framing 固定 $\varpi$，赋予 $u_{\rm base}$ 权 $1-p$。
Kummer Galois 则固定实际 $x,y,u_{\rm base}$，
使 $\varpi\mapsto a\varpi$、$\alpha,\beta\mapsto a^{-1}\alpha,a^{-1}\beta$。
于是 $\tau$ 与 $\mathcal D$ 同有权 $a^{p-1}$，
而 $\tau^p\mathcal D$ 不变。
这正与 EP 的 $(\tau,Y)$ scalar 作用相容；
不把 framing 与 Kummer Galois 混为一个 action。

在与 (1066.17) 的 $(0,0)$ 相应的 full-level 点，
$\alpha/\beta$ 属于 $\mathbf F_{p^2}\setminus\mathbf F_p$。
也可用 EP 的 diagonal nonsplit 坐标
$\widetilde\alpha,\widetilde\beta$ 直接读取：
Moore denominator 是
$\widetilde\alpha^{p+1}-\widetilde\beta^{p+1}$ 的非零常数倍，
numerator 是
$\widetilde\alpha^{p^2}\widetilde\beta-
 \widetilde\alpha\widetilde\beta^{p^2}$ 的非零常数倍。
在 $\widetilde\alpha=0,\widetilde\beta\ne0$，
分母是单位，分子对 $\widetilde\alpha$ 的导数非零。
EP 的 $V=\widetilde\alpha\widetilde\beta$、$Y=UV$，
且 $U$ 在此为单位，因此 $\mathcal D/Y$ 也是单位。
非分裂 Cartan 的 eigenline 上无非平凡 point stabilizer，
normalizer 的外陪集交换两条 eigenline；在已经除去 $\pm1$ 后
该 full-point 到 normalizer tail 的映射在此 étale。
故 $\mathcal D$ 在 (1066.17) 上仍是简单 parameter。
这里可以准确选择 EP 所需的 equivariant parameter，而不是任取 lift。
在整个原 affine branch 轨道上，对实际 normalizer 作 Reynolds 平均，
令 $Y$ 为 $\mathcal D$ 的平均。R1021 §3 给所有 level 作用模 $p$
为原线性作用，所以 $Y\equiv\mathcal D\pmod p$。
Kummer Galois 与这些实际 level 作用交换，
故 $Y$ 仍有同一精确 Kummer character。
它固定所需的降底子群，并在第一有限固定点有简单零，
因此是 $W[\tau][[Y]]$ 的真实 regular parameter。
在选择 prime-to-$p$ 辅助稳定子时，可同时作相应 character 平均。
将 (1066.20) 同时平均，得到
$
u_{\rm base}=\tau^p(cY+pR_1),\qquad c\in W^\times,
\tag{1066.21}
$
在该完成局部环中成立；$R_1$ 正则。
此处当前点在原 affine tail 内，R1021 的正则误差范围足够，
没有在 ordinary 节点对有极部的误差作此操作。

代入 (1066.18) 并除 $p=\tau^{p+1}$：
$
u_{\rm base}/p=ct+\tau^pR_1.
$
右边在 blowup chart 整。
$u_{\rm base}/p$ 和 $ct$ 都是 Kummer invariant；
故误差也在 invariant chart $W[t]$ 的完成中，
而其正 $\tau$-valuation 在该不分歧环中迫正 $p$-valuation。
等价地，在精确 scalar chart 中每个 invariant 单项
$\tau^aY^b$ 满足 $a+b\equiv0\bmod(p+1)$；
除去 $\tau^pY$ 后的项在 $Y=\tau t$ 上，除 $p$ 仍全含 $p$。
这给真正模 $p$（不只是模 $\tau$）的式子
$$
\overline{u_{\rm base}/p}=c\,t.
\tag{1066.22}
$$
若先用另一个实际 fine parameter，其值只作可逆仿射改变，
正如 (1066.16)。
所以原 $F_s^\circ$ 的点，确实由 good deformation 模 $p^2$ 读取。

### 4.3 原 coarse 商及所有 $\mathbf F_p$ 支路

设
$$
e_s=\#\operatorname{Aut}(E_s)/2
=\begin{cases}
3&s=0\text{ supersingular},\\
2&s=1728\text{ supersingular},\\
1&\text{其它}.
\end{cases}
$$
在 $e_s>1$ 时选择 reference CM 作用分别为
$\mathbf Z[\zeta_3]$、$\mathbf Z[i]$。
实际额外 automorphism 在 fine deformation tangent 上忠实地以
$\mu_{e_s}$ 作用。
它固定 $\tau$，在 (1066.18) 上作用 $t\mapsto\xi t$；
可通过有限平均取确切 eigenparameter。
因此原 coarse 开及坐标为
$$
F_s^\circ=\mathbf A^1_T,\qquad T=t^{e_s}.
\tag{1066.23}
$$
这也与 EP §3.4 的额外稳定子商一致。
原 $j-j_{\rm CM}$ 等于 $u_{\rm base}^{e_s}$ 乘单位，
所以除去 $p^{e_s}$ 后的 leading 正是该 coarse 坐标的单位倍。

不能只取一个固定 twist 的 $t\in\mathbf F_p$，再宣称已覆盖所有 $T$。
完整下降如下：

- $e_s=1$：原 $E_s/\mathbf F_p$ 的 good deformation 参数已给
  $\mathbf A^1(\mathbf F_p)$ 全部值。
- $e_s=3$：超奇异性迫 $p\equiv2\bmod3$，
  $t\mapsto t^3$ 在 $\mathbf F_p$ 上双射。
  等价地 $H^1(\mathbf F_p,\mu_3)=0$，
  所以所有 coarse 值都由一个适当 fine deformation 给出。
- $e_s=2$：超奇异性迫 $p\equiv3\bmod4$。
  实际 $\mathbf F_p$-quartic twists 的分类映射
  $$
  H^1(\mathbf F_p,\mu_4)\longrightarrow H^1(\mathbf F_p,\mu_2)
  $$
  由 square character 诱导，是满射：
  在 Kummer 记号中就是
  $\mathbf F_p^\times/\mathbf F_p^{\times4}
   \to\mathbf F_p^\times/\mathbf F_p^{\times2}$。
  因而两种 $\mathbf F_p$-twist 分别提供两类 tangent descent。
  对非零 $T\in\mathbf F_p$，若 $t^2=T$，
  就按 $t^p=t$ 或 $t^p=-t$ 选对应 twist。
  $T=0$ 是原 CM 中心。
  每个 twist 都有自己的 $R,\pi$ 和 §3 的完整斜率构造。

这正是 coarse point 可能没有所先选 fine lift 的全部障碍；
没有把一个固定 good-reduction 模型的参数硬当成所有 coarse 点。
选择得到的 special twist 后，其 deformation 参数有一条
$\mathbf F_p$-line，§3 覆盖该 line 的任意值，
故 (1066.23) 的每个 $T\in\mathbf F_p$ 都被覆盖。

## 5. 实际非分裂正规化子结构与 CM 点的定义域

对 §3 所得 CM lift，$p$ 在 CM 二次域惰性且不除其 conductor。
因此
$$
\mathcal O_{\rm CM}/p\mathcal O_{\rm CM}\simeq\mathbf F_{p^2}
$$
在原 $E[p]$ 上作用，其 unit group 给一个非分裂 Cartan。
每个 Galois 元素在 geometric CM ring 上按 identity 或二次共轭作用，
所以都正规化这个 Cartan。
这给实际 $X_{\rm ns}^+(p)$ 的一个 $\mathbf Q_p$ 点，
不只是 underlying elliptic $j$ 的一个 lift。

在 good unramified CM formal group 上，
inertia 的 mod $p$ 作用为 height-one
$\mathcal O_{\mathbf Q_{p^2}}$-module 的 level-one character，
其 image 为 $\mathbf F_{p^2}^\times$。
故这里的 Cartan 正是由原局部惯性确定的 Cartan，
与 §4 的 normalizer chart 相容。
不要求也不声称一个 $\mathbf Q_p$-定义的 full-level basis
或 $X_{\rm ns}(p)$ 有理 lift。

设其 singular modulus 为 $j_{\rm CM}$。
canonical CM Cartan 的 conjugacy class 已在
$\mathbf Q(j_{\rm CM})$ 上 Galois stable，
所以对应的 coarse normalizer 点也定义于该数域。
所选 CM lift 给出一个
$\mathbf Q(j_{\rm CM})\hookrightarrow\mathbf Q_p$ 的 embedding。
上述 normalizer 点在该 embedding 下，就是 §4 已定位的
原剩余圆盘中的实际点。
全局次数一般为 CM class number，而不是一。

综合 §§2–5，对每个
$\bar x\in\mathcal M^{\rm sm}(\mathbf F_p)$，
先选 §4.3 的原 special twist 与其一阶参数，
再用 (1066.12) 的 index-$p$ 格选短 $\eta$。
(1066.13)–(1066.15) 给 (1066.1)，
(1066.16) 与 (1066.22)–(1066.23) 保证所得点约化恰为 $\bar x$。
这证明开头的每盘 CM 代表定理。

## 6. 原规范 Kummer 标签的有限 CM 读数

令 $\mathcal C_p(B)$ 为所有满足以下条件的 actual coarse CM 点，
连同它们进入 $\mathbf Q_p$ 的 embeddings：

- 完整 CM ring 判别式为 $-D'$，$0<D'\le B$；
- $p\nmid D'$ 且 $(-D'/p)=-1$；
- level 结构是 CM ring 给出的 canonical 非分裂 Cartan 正规化子结构。

这是一个有限集合，不要求其中的点定义于 $\mathbf Q$。
R1065 的标签在每个原剩余圆盘上恒定；故
$$
\boxed{\quad
\Phi_p\bigl(X(\mathbf Q_p)\bigr)
=
\left\{\Phi_y:
 y\in\mathcal C_p(4p^{3/2}/\sqrt3)\right\}.
\quad}
\tag{1066.24}
$$
右边取实际 $\mathbf Q_p$ embeddings 的值。
反向包含只是每个所列 CM 点本来就是 $X(\mathbf Q_p)$ 点；
正向包含使用上述原圆盘代表，未更换标签或曲线。

因此 R1065 的至多 $p\,n_{\mathbf Q_p}(p)$ 个局部标签，
可由有限个有界判别式 singular-modulus 评价产生。
regular $p$ 时，R1065 的 global $2,3$ 支撑自由度和
$p^{\kappa_p}$ 个 preimages 仍完整保留。
一个局部 CM 评价本身不自动属于
$\operatorname{Hom}_G(W,F(S,p))$，
也不自动通过 R1064 任一辅助好素的同标签测试。

这把“未知圆盘参数”换成实际有界 CM 输入，
但没有把全局非 CM 有理点排掉。
后继必须比较同一个全局 twist 在其它素数的实际点像，
而不是再次把这些高次数 CM 点当成 $\mathbf Q$-CM 完成标准。

## 7. 原始来源与核准范围

- M. Kaneko, *Supersingular j-invariants as singular moduli mod $p$*,
  Osaka J. Math. **26** (1989), 849–855，
  [作者全文](https://www2.math.kyushu-u.ac.jp/~mkaneko/papers/06supersingular_j_invariants.pdf)，
  §2 印刷 pp.851–852：两种二元 norm 格与 determinant $4p$。
  本篇新增 index-$p$ 斜率条件、实际一阶 CM 定位和原模型接口。
- T. Ibukiyama, *On maximal orders of division quaternion algebras over the
  rational number field with certain optimal embeddings*,
  Nagoya Math. J. **88** (1982), 181–195，
  [正式全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DBF970E188865A2CD3F945E9B5B2FE7D/S002776300002016Xa.pdf/on-maximal-orders-of-division-quaternion-algebras-over-the-rational-number-field-with-certain-optimal-embeddings.pdf)，
  Theorems 1–2、Lemma 3.2 及 pp.191–192 的证明：
  此处确实保持实际 optimal Frobenius embedding。
- B. Edixhoven–P. Parent, *Regular models of modular curves in prime level
  over $\mathbf Z_p^{\rm ur}$*, Doc. Math. **29** (2024), 1017–1058，
  [正式全文](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)，
  Eq. (3.6) 后的 $p$-chart、Eq. (3.8)、printed pp.1028–1029 finite fixed point，
  Theorem 3.4 / Corollary 3.2 与 coarse 稳定子商。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)
  §§1–4：同一个 universal full-level ring 及精确 framing 次数。
- [R1052](R1052-original-complete-CM-profile-and-actual-lowest-functional.md)
  §6：已登记 source 精度的一个实际 CM 应用；本篇不把该单支直接当一般族。
- [R1035](R1035-original-lowest-type-integral-Lie-comparison-by-two-PD-thickenings.md)
  的 Zink / Grothendieck–Messing 来源与态射判据；
  这里仅使用标准未分歧 $(p)$-PD thickening，不依赖高度分歧的任意比较。
- [R1065](R1065-original-p-local-cusp-label-compression.md)：
  原全 $p$ 模型、所有 $\mathbf Q_p$ section 及规范标签的 mod-$p$ 圆盘恒定性。

以上均为纸面证明，没有执行数学程序。

root 完整复核本篇：亲读 Kaneko §2、Ibukiyama Theorems 1–2 / Lemma 3.2 及证明、EP (3.8) 与 first-fixed-point / coarse 商，回读 R1021 全文；独核两 Gram、实际 π、晶体反序、一阶 PD、仿射中心平移、完整 Kummer invariance 与两 extra-aut 支路。o1_theta 对 exact draft 的 §§3–5 全文独核；o2_high_coefficient 对 §§2–3 全文独核并亲读原表。无数学执行。

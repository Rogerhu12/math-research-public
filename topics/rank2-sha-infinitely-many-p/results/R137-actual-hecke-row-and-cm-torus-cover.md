# R137. 实际 Hecke 行非零、环面覆盖及指定 CM 纤维

日期：2026-11-12。状态：**已证明；指定 CM 纤维的无穷非零尚开。**

完整证明分为
[Fourier 独立性及极点](../notes/2026-11-12-actual-hecke-row-and-fourier-independence.md)
和
[环面覆盖及原完整 CM 迹](../notes/2026-11-12-torus-cover-and-actual-cm-trace-row.md)。
以下保留 $E_{17}$、$F=\mathbb Q(\sqrt{-15})$ 和原类数二映射。

取 R135 的普通素数 $p$，$\ell\equiv-1\pmod{1020p}$、
$v_p(\ell+1)=1$，写 $\ell+1=pu$。置 $M=3\cdot9248$，
在 $C=X_0(M)$ 使用准确的旧形式函数
$$
 h=h_p\circ d_1+h_p\circ d_3,\qquad h_p=\bar H_p/\mathrm{Ha}_p.
$$
它的 q 一次系数为 $1$，只有简单超奇异极点。固定 Weil
配对的 $X(M\ell)$ 在特征 $p$ 仍光滑几何连通，full
$\ell$-level 的真实群首先是 $\mathrm{SL}_2(\mathbb F_\ell)$。
所有循环商函数中心不变；明确除去 $\{\pm I\}$ 后，记所得
连通曲线为 $X$，其群为 $G=\mathrm{PSL}_2(\mathbb F_\ell)$。

## 1. 唯一的常系数关系

以 $v\in\mathbb P^1(\mathbb F_\ell)$ 标记实际同源支 $h_v$。
在共同 Tate 尖点，
$$
 h_\infty(q)=h(q^\ell),\qquad
 h_a(q)=h(\zeta_\ell^a q^{1/\ell}).
$$
几何 Hecke 是 $\ell U_\ell+V_\ell$；
$a_\ell(E_{17})=0$ 给准确 $\sum_vh_v=0$。
而且这是全部常系数关系：
$$
 \ker\bigl(k^{\mathbb P^1(\mathbb F_\ell)}\to k(X)\bigr)
                       =k\,(1,\ldots,1),\qquad
                       k=\overline{\mathbb F}_p.
 \tag{1}
$$

证明中，$\mathbb Q(E[p])$ 在 $\ell$ 不分歧，
$\mathbb Q(\zeta_\ell)$ 的每个非平凡子域在 $\ell$ 全分歧，
所以两域不交。对每个 $r\in\mathbb F_\ell^\times$，
Chebotarev 给素数 $q\equiv r\pmod\ell$，且
$\operatorname{Frob}_q|E[p]=1$。于是
$q\equiv1\pmod p$、$a_q\equiv2\pmod p$，而实际 $h$ 的
q 第 $q$ 次系数为 $a_q/q=2$。比较任意关系中
$q^{q/\ell}$ 的系数，长度 $\ell$ 的 Fourier 逆变换迫使
全部有限支系数相同；总 Hecke 关系再迫 $\infty$ 支相同。
这里仅除 $\ell$，没有除以已被 $p$ 整除的 $\ell+1$，
也无需残余 Galois 满像或 Ihara 饱和。

## 2. 原 $2u$ 项及准确函数域增广层

令 $T\subset\mathrm{PGL}_2(\mathbb F_\ell)$ 为阶 $\ell+1$
的 nonsplit torus，$T_0=T\cap G$ 阶为 $pu/2$。
它有两条轨道。取 $U\le T$ 阶 $u$，
$U_0=U\cap T_0$ 阶 $u/2$，并把
$T_0/U_0\simeq T/U$ 的生成元 $\tau$ 与原环类商匹配。
定义
$$
 B=\sum_{v\in Uv_0}h_v,\qquad
 Y=X/U_0,\quad Z=X/T_0.
$$
这里的 $u$ 项 $h_v$ 已各含 $\pi d_1+\pi d_3$，因此保留
原 **$2u$ 项** 类群迹。两条 $T_0$ 轨道都在此和中。

$Y\to Z$ 是连通、处处 étale 的次数 $p$ 覆盖：内点由
prime-to-$p$ full level 的 étale 性；尖点惯性阶 $\ell$
与 $T_0$ 互素。$p\mid|G|$ 不破坏这个结论。
令 $\Delta=\tau-1$，
$$
 D_1=\sum_jj\tau^j=-\tau\Delta^{p-2},\qquad
 D_2=\sum_j\binom j2\tau^j=\tau^2\Delta^{p-3}.
$$
权向量 $j$、$\binom j2$ 都非恒定，由 (1) 得
$D_1B,D_2B$ 均非零。总迹为零及正常基定理进一步给
$$
 \boxed{\quad
 B\in\Delta k(Y)\setminus\Delta^2 k(Y),\qquad
 \Delta D_2B=-D_1B\ne0,\qquad
 \Delta^2D_2B=0.
 \quad}
 \tag{2}
$$
所以原函数已在准确的第一增广层，其二阶行的 Jordan
长度正好为 $2$；不是只知某个环境模存在非零向量。

## 3. 实际极点与取值边界

所有 prime-to-$p$ 同源拉回的 Hasse 只差单位，所以所有
$h_v$ 共用 full-level 曲线上的 reduced 超奇异极点除子。
线性和仍只有简单极点，不需另乘 $\ell+1$。
两行在共同尖点为零且非零，故都非恒定、各有真实简单极点；
因此也不是相应函数域中的绝对 AS 像 $x^p-x$。
若 $d_M=\deg\omega_{X(M)}$，准确次数界为
$$
 \deg_Z(D_1B)\le(p-1)d_M\ell(\ell-1),\qquad
 \deg_Y(D_2B)\le(p-1)d_Mp\ell(\ell-1).
 \tag{3}
$$
AS 算子与 (2) 的 deck 差分不能混同。

CM 互反及两轨道模型完整保留原 $C_p$ 纤维；固定细 level、
scalar 标记及配对值只需素于 $p$ 的常数扩张。源还须
$p$ 在 $F$ 分裂，保证原 CM 点 ordinary、函数有定义。
R135 的实际取值为
$$
 B|_{\rm CM}=-\bar a_p\,s\bar z_0,\qquad
                    z_0=\log_0(Q)/p.
$$
故
$$
 D_2(B|_{\rm CM})\ne0
       \Longrightarrow a\le1
       \Longrightarrow\Sha(E_{17}/\mathbb Q)[p^\infty]=0.
 \tag{4}
$$
若检验失败，原有限 étale 纤维代数中准确有
$B|_{\rm CM}\in\Delta^3\mathcal P$。这不与函数域的 (2)
矛盾。还须证明无穷个原合法输入的指定 CM 标记避开
两行的共同零；其余任意环面标记不能算作原 CM 轨道。

原始模型来源：Cais–Conrad，*Modular curves and Ramanujan's
continued fraction*（2006 作者版），Theorems 2.2–2.3；
Chebotarev 使用 Milne，*Algebraic Number Theory*（2020），
Theorem 8.31。准确 URL、全部常数及模型说明见两份完整证明。

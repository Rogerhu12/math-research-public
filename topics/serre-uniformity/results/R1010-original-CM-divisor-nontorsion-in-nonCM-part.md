# R1010：原 CM 点差在非 CM 部分的非挠投影

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 对原第一曲线 \(X_1\)，下面给出指定有理 CM 点差在非 CM 部分非挠的绝对范围。证明使用完整 Hecke 对应的真实下降、最深 CM 导子的互不相消，以及复 gonality 下界。没有假设 Rankin 导数非零，没有重新计算任何旧素数窗口。

这里不处理任意变化立方扭曲 \(X_d\)，也不由非挠性宣称有理点排除。低秩实际商及其局部排点问题须另外完成。

## 1. 同一个原对象和精确结论

固定 \(p>37,\ p\equiv5\pmod6\)。所有曲线均取光滑射影正规化：
\[
X_d=\operatorname{Norm}\bigl(X_{\rm ns}^+(p)\times_j\mathbf P^1_b\bigr),
\qquad j=6912db^3(1-db^3).
\tag{1010.1}
\]
原曲线为 \(X_1\)；canonical 模曲线为 \(X_4\)。
令 \(K=\mathbf Q(\zeta_3)\)、\(\alpha=\sqrt[3]4>0\)，
\[
\iota:X_1\longrightarrow X_4,\qquad u=b/\alpha,\qquad
\delta:b\longmapsto\zeta_3b.
\]
\(X_1\to Y,\ v=b^3\) 的范数算子为
\[
N=1+\delta+\delta^2,\qquad P_1=(\ker N)^0=\operatorname{im}(3-N).
\]
R616 已固定同一 \(\mu_6\)-稳定的 CM 项链及两个有理点
\(c_0:b=0,\ c_1:b=1\)。定义真正的有理次数零除子及其类
\[
\mathcal D_0=2[c_1]-[\delta c_1]-[\delta^2c_1],\qquad
D_0=[\mathcal D_0]=(3-N)[c_1-c_0]\in P_1(\mathbf Q).
\tag{1010.2}
\]
两个非有理点由复共轭交换，故这里没有借用非有理点差作为有理点。

在 canonical 新部分 \(P_4\) 中，令 \(C_4\) 为全部 CM 自守 Hecke 成分的同源子部之和。它由 \(\delta\) 保持，因而经原 \(\kappa_4\) 下降给 \(C_1\subset P_1\)，见 §3。所有“投影”均指这个确定的有理同源分解，或相应实际商 \(P_1/C_1\)。

**定理 1010.1。** 下列任一范围内，
\[
\boxed{\quad
D_0\text{ 在 }(P_1/C_1)(\mathbf Q)\text{ 中的像非挠。}
\quad}
\tag{1010.3}
\]

1. \(p\ge10^{18},\ p\equiv5\pmod6\)；
2. \(p\ge431,\ p\equiv11\pmod{12}\)。

特别地，这给出一个非 CM canonical Hecke 成分，其中
\(\iota_*D_0\) 的像非挠。第二范围的证明不需要变化的辅助素数。
原题另外的 \(p\bmod9\) 条件只取本定理的子集，不是证明的额外输入。

## 2. 整个 Hecke 对应的甲板运输

R1008 的 canonical 六水平群为
\[
G_6=\operatorname{GL}_2(\mathbf F_2)\times\operatorname{GL}_2(\mathbf F_3),
\qquad
H_6=\{(\vartheta g,g)\},
\qquad \ker\vartheta=Q_8.
\]
记 \(H_6^1=H_6\cap\det_3^{-1}(1)\)。有
\(\operatorname{sgn}\vartheta(g)=\det_3(g)\in\{\pm1\}\)。
取 \(r\in A_3\subset S_3=\operatorname{GL}_2(\mathbf F_2)\) 的生成元，
则 \(n=(r,1)\) 规范化 \(H_6^1\)，并给几何三阶甲板 \(\delta\)，
或其逆；以下关系对两种选择都相同。

对素数 \(\ell\nmid6p\)，用全部循环 \(\ell\)-同源定义 canonical 对应 \(T_\ell\)。
同源将所选 Weil 配对 \(\beta\) 送到 \(\beta^\ell\)。
取 \(h=(\vartheta g,g)\in H_6\)、\(\det_3h=\ell^{-1}\)，
将目标标记校正回所选几何分量。于是
\[
h^{-1}nh=n^\ell\pmod{H_6^1}.
\]
在 p 处可独立选取非分裂正规化子中的行列式校正；n 的 p 分量是单位。
因此对完整的同源对应循环，而不只是对 \(H^1\)，有
\[
\boxed{T_\ell\delta=\delta^\ell T_\ell.}
\tag{1010.4}
\]
这说明
\[
T_\ell^2\delta=\delta T_\ell^2,\qquad
T_{31}\delta=\delta T_{31},\qquad T_\ell N=NT_\ell.
\tag{1010.5}
\]
canonical \(T_\ell^2,T_{31}\) 本来定义于 \(\mathbf Q\)；
(1010.5) 使其通过真实 \(\kappa_4\) cocycle 下降为 \(X_1/\mathbf Q\) 的对应。
下文继续使用相同记号。

不能把异素 adelic 算子的一般交换性直接用于几何 \(\delta\)：
n 规范化的是 \(H_6^1\)，并非整个 \(H_6\)。
(1010.4) 保留了行列式校正，特别是 \(\ell\equiv2\pmod3\) 的反向作用。

## 3. 新部分中全部可能的 CM 域

整个 canonical \(H^1\) 的自守分解，包括旧形式与重数，按 R1008 使用。
六水平条件含 \(K_2(1)\)、\(K_3(1)\)，p 水平条件含 \(K_p(1)\)。
Miyauchi–Yamauchi Theorems 1.1–1.2 给出各局部导子上界。

先确定新部分所需的六水平型。

- 在 \(\operatorname{GL}_2(\mathbf F_2)=S_3\) 中，只有二维标准表示
  \(\operatorname{Std}_2\) 在 \(A_3\) 上非平凡。新部分的
  \(N=0\) 因而选择这个型。
  主系列的 \(K_2(1)\)-固定部分为 \(1\oplus\operatorname{Std}_2\)；
  特殊表示为 \(\operatorname{Std}_2\)。
  导子二的超尖点表示固定部分维数为 \(2-1=1\)，在 \(A_3\) 上平凡，
  不能进入新部分。故 \(\pi_2\) 是未分歧主系列或未分歧扭曲的 Steinberg。
- \(H_6\) 的图式配对迫使三处含
  \(\operatorname{Std}_3=\operatorname{Std}_2\circ\vartheta\)。
  这个二维型不能来自主系列或特殊表示：
  上三角 Borel 在 \(\vartheta\) 下满射到 \(S_3\)，
  \(\operatorname{Std}_3\) 限制到 Borel 没有一维子表示，
  Frobenius 互反排除了所有从 Borel 一维字符诱导的主系列，
  也排除了其特殊子商。
  所以 \(\pi_3\) 超尖点，且导子恰为二。
- 在 p 处，\(K_p(1)\) 不变量给 \(c(\pi_p)\le2\)；
  其余有限处未分歧。

这里固定部分的维数亦直接由 Miyauchi–Yamauchi Proposition 4.3、
Corollaries 4.8/4.10 得到；导子二的超尖点表示已是最小导子。
没有仅由总导子界猜测六水平型。

若 \(\pi=\operatorname{AI}_{K'/\mathbf Q}\psi\) 为 CM 成分，
局部单值算子为零，故 \(\pi_2\) 不可能 Steinberg。
于是它在二处未分歧，且
\[
N(\pi)=|D_{K'}|\,\operatorname{Norm}\mathfrak f(\psi),\qquad
v_2N(\pi)=0,\quad v_3N(\pi)=2,\quad v_pN(\pi)\le2.
\tag{1010.6}
\]
所以虚二次基本判别式为奇数，素因子仅可能为 3,p：
\[
K'=\mathbf Q(\sqrt{-3}),\quad\text{或}\quad
K_p=
\begin{cases}
\mathbf Q(\sqrt{-p}),&p\equiv11\pmod{12},\\
\mathbf Q(\sqrt{-3p}),&p\equiv5\pmod{12}.
\end{cases}
\tag{1010.7}
\]
第一行的额外域其实不可能：此时 \(-p\equiv1\pmod3\)，
3 在 \(\mathbf Q(\sqrt{-p})\) 分裂，其自守诱导在三处是主系列，
与所需超尖点型矛盾。

因此 \(p\equiv11\pmod{12}\) 时，所有 CM 新成分的 CM 域只有 K；
\(p\equiv5\pmod{12}\) 时，至多另有 \(\mathbf Q(\sqrt{-3p})\)。

为核准 \(C_4\) 的下降，在新部分置 \(\jmath=\delta-\delta^2\)。
由 (1010.4)，
\[
\jmath^2=-3,\qquad
T_\ell\jmath=\chi_{-3}(\ell)\jmath T_\ell.
\tag{1010.8}
\]
故 \(\jmath\) 将 \(\pi\) 的 Hecke 成分送到
\(\pi\otimes\chi_{-3}\) 的成分；二次扭曲保持 CM 性及其 CM 域。
强重数一确定这些完整自守成分。
又 \(\delta=(\jmath-1)/2\) 于新部分，所以 CM 同源子部由 \(\delta\) 保持。
它本来是有理 Hecke 成分之和，因此确实可沿 \(\kappa_4\) 下降为 \(C_1\)。

## 4. 杀 CM 的真实对应与挠点消去

5 在 K 惰性，且 \(5\nmid6p\)。
所有 K-CM 成分的 \(T_5\) 特征值为零，故 \(T_5^2\) 杀这些成分。
在需要额外域 \(K_p\) 时，选其惰性素数
\[
q\notin\{2,3,5,31,p\},
\]
则 \(T_q^2\) 杀其全部 CM 成分。令
\[
U=
\begin{cases}
T_5^2,&p\equiv11\pmod{12},\\
T_5^2T_q^2,&p\equiv5\pmod{12}.
\end{cases}
\tag{1010.9}
\]
它是原 \(X_1/\mathbf Q\) 的整数对应，保持新部分，且在 \(C_1\) 上为零。
因此若 (1010.3) 不成立，\(UD_0\) 是 \(J_1(\mathbf Q)\) 的挠点。

31 在 \(\mathbf Q(\zeta_3,\sqrt[3]4)\) 全分裂：
\(31\equiv1\pmod3\)，且 \(16^3\equiv4\pmod{31}\)。
原 \(X_1\) 在 31 好约化，并在该处与 canonical 模型同构。
水平群包含全部整标量，所以 Eichler–Shimura 关系没有非平凡 diamond 因子：
\[
T_{31}=\operatorname{Frob}_{31}
       +31\operatorname{Frob}_{31}^{-1}
\quad\text{于约化 Jacobian。}
\tag{1010.10}
\]
有理挠点的约化由 Frobenius 固定。
在 \(\mathbf Q_{31}\) 上，好约化形式群的核无挠：
其整形式对数在 \(31\mathbf Z_{31}^{\dim J}\) 上可逆。
故约化对全部 \(\mathbf Q_{31}\)-挠点单射，而不只对素于 31 的部分单射。
因此
\[
(T_{31}-32)J_1(\mathbf Q)_{\rm tors}=0.
\tag{1010.11}
\]
反设 (1010.3) 不成立，字面除子
\[
\mathcal D=(T_{31}-32)U\mathcal D_0
\tag{1010.12}
\]
便是主除子。下一节证明它不是零除子。

## 5. 最深 CM 导子的支持不会相消

以下论证在复曲线上进行，三次扭曲不改变该论证。
令 \(\mathcal O=\mathbf Z[\zeta_3]\)、\(E_0=\mathbf C/\mathcal O\)。
这是 (1010.2) 三个点的同一个底椭圆曲线。
置
\[
m=25\quad\text{或}\quad25q^2,\qquad c=31m.
\]

### 5.1 最小次数的 CM 同源唯一到源自同构

设 \(E'=\mathbf C/\Lambda\) 的 CM 整环导子为 f，且存在
\(E_0\to E'\) 的 degree-d 同源。经缩放可取 \(\Lambda\subset K\)。
令
\[
I=\{z\in K:z\mathcal O\subset\Lambda\}
\]
为 \(\Lambda\) 中的最大 \(\mathcal O\)-分式理想。
则
\[
[\Lambda:I]=f.
\tag{1010.13}
\]
本题的同源次数只含 c 的素因子。在不整除该次数之处，源与目标的局部格同构，
所以导子指数为零；因此仅须处理 \(\ell\mid c\)，这些素数至少为 5。
在每个相关 \(\ell\) 处，将 \(\mathcal O_\ell\Lambda_\ell\) 归一到
\(\mathcal O_\ell\)。\(\Lambda_\ell\) 含一个 \(\mathcal O_\ell\)-单位：
未分歧域情形由本原性；分裂情形两个坐标投影均满，
约化后的向量空间不能被两条坐标轴覆盖。
再乘该单位逆，便有
\[
1\in\Lambda_\ell\subset\mathcal O_\ell,\qquad
\Lambda_\ell=\mathbf Z_\ell+\ell^r\mathcal O_\ell.
\]
其乘子整环恰为右侧的阶，r 是 f 的 \(\ell\)-赋值，
最大 \(\mathcal O_\ell\)-子格为 \(\ell^r\mathcal O_\ell\)，指数为 \(\ell^r\)。
其余处的 r 为零。这证明 (1010.13)。

同源由某个 \(z\mathcal O\subset I\subset\Lambda\) 给出，
因此 f 整除 d。若 d=f，则 \(z\mathcal O=I\)；
由于 \(\mathcal O\) 类数一，任何两条 degree-f 同源只差源的
\(\mathcal O^\times\) 自同构。这是完整标记不能碰撞所需的唯一性。

### 5.2 深层确实出现，并且三源互不相交

存在总 degree-c、目标导子恰为 c 的路径：
依次在
\[
E_{c_i}=\mathbf C/(\mathbf Z+c_i\mathcal O)
\]
上用乘 \(\ell\) 映射，从 \(c_i\) 到 \(\ell c_i\)，
取顺序 \(5,5\)，在需要时再取 \(q,q\)，最后取 31。
每步度为 \(\ell\)，总核循环，目标 CM 导子为 c。
所以 \(T_{31}U[x]\) 的导子 c 支持对每个原源点 x 均非空，
系数为正。

设 (1010.2) 的两个不同源点有同一个导子 c 目标，
并包括完整 \(H_6\) 标记与 p 项链。将目标同构与两条总 degree-c
同源合成，§5.1 迫它们只差 \(E_0\) 的自同构。
同源在 6p 挠点上可逆；反向双同源的差仅为标量 [c]，
而标量属于 \(H_6\times N_{\rm ns}(p)\)。
因此运输标记逆回后，两个源点在同一模曲线上相同，矛盾。

于是 \(T_{31}U\mathcal D_0\) 的最深导子 c 支持分成互不相交的三组，
原权重 \(2,-1,-1\) 不可能相消。
另一方面，\(U\mathcal D_0\) 的每个底 CM 导子整除 m，
所以 \(-32U\mathcal D_0\) 完全不含导子 c。
从而
\[
\boxed{\mathcal D\ne0\text{，作为字面除子。}}
\tag{1010.14}
\]
本论证没有把一个 Jacobian 中的非零条件当作字面非相消的理由。

## 6. 除子次数与 gonality

\(\mathcal D_0\) 的正、负次数各为 2。
一个 \(T_\ell\) 的度是 \(\ell+1\)，故
\[
\deg\mathcal D^+\le
\begin{cases}
4608,&U=T_5^2,\\
4608(q+1)^2,&U=T_5^2T_q^2.
\end{cases}
\tag{1010.15}
\]
例如第二行是
\((32+32)\cdot2\cdot36(q+1)^2\)；
允许低层的任意相消，只会使这个上界更小。

在 \(\operatorname{PSL}_2(\mathbf Z)\) 中，
非分裂正规化子几何群的指数为 \(p(p-1)/2\)，
\(H_6^1\) 在六水平全几何群中指数为 6。
由 CRT，\(X_4\) 的几何同余群指数为 \(3p(p-1)\)。
原 \(X_1\) 在复数域与它同构，故 Abramovich Theorem 0.1 给
\[
\boxed{\operatorname{gon}_{\mathbf C}(X_1)
       \ge\frac{21p(p-1)}{800}.}
\tag{1010.16}
\]

若 (1010.3) 不成立，(1010.12)、(1010.14) 给一个非常数主函数，
其次数就是 \(\deg\mathcal D^+\)。
所以只要 (1010.15) 严格小于 (1010.16)，便产生矛盾。

当 \(p\equiv11\pmod{12},p\ge431\) 时，第一行已经严格小于下界，
证明定理的第二范围。

## 7. 一个自足的短字符和界足够处理变化域

现在 \(p\equiv5\pmod{12}, K_p=\mathbf Q(\sqrt{-3p})\)。
令
\[
M=930=2\cdot3\cdot5\cdot31,\qquad
B=\sqrt p(1+\log p),\qquad H=\lceil2B\rceil.
\]
对 \(p\ge10^{18}\)，有 \(H<p\)。
Legendre 字符的 Gauss 和绝对值为 \(\sqrt p\)；
将任意长度 H 的平移区间作有限 Fourier 展开，并用几何级数公式，
得到
\[
\left|\sum_{k=1}^{H}\chi_p(k+a)\right|
\le \frac1{\sqrt p}\sum_{r=1}^{p-1}
 \min\left(H,\frac1{|\sin(\pi r/p)|}\right)
\le\sqrt p\sum_{r=1}^{(p-1)/2}\frac1r\le B.
\tag{1010.17}
\]
第二步使用 \(\sin(\pi r/p)\ge2r/p\) 于 \(1\le r\le(p-1)/2\)。
所以无需 Burgess、GRH 或首惰性素数的额外假设。

因为 M 在模 p 下可逆，(1010.17) 同样界住
\(\sum_{k=1}^H\chi_p(1+Mk)\)。
若此区间没有负值，至多一个项为零，和至少 H−1>B，矛盾。
故存在
\[
n=1+Mk\le1+930H,\qquad \chi_{K_p}(n)=\chi_p(n)=-1.
\]
这里 \(n\equiv1\pmod6\) 消去了可能的 \(\chi_{-3}\) 因子。
n 的某个素因子 q 在 \(K_p\) 惰性，且
\[
q\notin\{2,3,5,31,p\},\qquad
q+1\le1861\sqrt p(1+\log p).
\tag{1010.18}
\]
最后一个不等式由 \(q+1\le2+930H\le1860B+932\)、\(B>932\) 得出。

准确整数比较给
\[
4608\cdot1861^2\cdot800/21<6.1\cdot10^{11}.
\]
而 \((p-1)/(1+\log p)^2\) 在 \(p>e\) 递增；
在 \(p=10^{18}\) 时，\(\log p<42\) 已使该比严格大于
\(6.1\cdot10^{11}\)。所以 (1010.18) 保证
\[
4608(q+1)^2<21p(p-1)/800
\]
于全部 \(p\ge10^{18}\)。这完成定理的第一范围。

## 8. 已完成的实际接口与剩余问题

本篇得到了原 \(D_0\) 的非 CM 非挠投影，绝对范围明确；
并给出杀全部 CM 成分的有理整数对应。
证明包括全部原六水平标记、p 项链、三次扭向及最深支持，
没有用一个任意替换的 CM 点。

该非挠投影可供下一步对同一个 canonical CM 点
\(c=(v=1,u=1/\alpha)\) 应用环类特征的 Euler system 定理。
R616(616.9)–(616.12) 已给其准确域
\(K(c)=K(\alpha)\)、轨道
\(\sigma c=\delta_{\kappa_4(\sigma)^{-1}}c\) 与 Hodge 基点消去；
这些已登记事实直接消费。

本篇尚不声称相应原有理商的秩、其局部 annihilating 微分的单位性，
或原候选圆盘只有 CM 点。原纯 CM 高度的 \(\eta_h\) 项没有被删去。
\(X_d\) 的变化扭曲可使第二 CM 中心非有理，也可使 31 坏约化或不再分裂；
(1010.11) 和 D₀ 的有理性不能无条件搬过去。
O0 全覆盖、原高系数、同标签非零及完整有理点排除仍开放。

## 来源与独立核对

- [R1008](R1008-wild-inertia-and-all-rational-correspondence-centralization.md)：
  canonical \(H_6\times N_{\rm ns}(p)\)、整个 \(H^1\) 自守分解及真实扭曲。
- [R616](R616-original-CM-point-difference-and-explicit-height-basis.md)：
  同一 \(c_0,c_1\)、canonical 点域与实际环类投影。
- Michitaka Miyauchi and Takuya Yamauchi,
  *A remark on conductor, depth and principal congruence subgroups*,
  Journal of Algebra 592 (2022), 424–434，
  [作者全文](https://arxiv.org/pdf/2107.08130)，
  Theorems 1.1–1.2、Proposition 4.3、Corollaries 4.8/4.10。
  这里只按 \(m=1,n=2\) 使用，允许二处；有限 S₃ 型筛选在 §3 自证。
- Dan Abramovich, *A linear lower bound on the gonality of modular curves*,
  IMRN 1996, no.20, 1005–1011，
  [作者全文](https://arxiv.org/pdf/alg-geom/9609012)，Theorem 0.1。
- 好约化的最优模型、Tate 标记运输和 Eichler–Shimura 输入与
  [R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md) 的规范一致；
  本篇的 31 处分裂及全部挠点单射已在 §4 核准。

root 与 global_route 分别核对对应的完整下降、六水平型、CM 域列表、
局部格的最深同源唯一性、整数次数、短字符和及绝对范围。
没有数学程序执行，没有新扫描，没有消费或重算旧有限数值来代替一般证明。

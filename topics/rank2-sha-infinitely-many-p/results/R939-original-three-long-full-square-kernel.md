# R939 — 原三长窗中完整平方来源的首核与立方剩余维数

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

**状态：以下完整平方/立方来源上的准确首核、维数界和单位子式结论已证明。它处理 R938 所保留的全平方来源，不判定原全 W 的首核或完整 p³ 仿射方程。无数学数值执行。**

## 1. 原来源与真正可读的三个长前缀

沿用 [R938](R938-original-full-source-finite-offsets-and-affine-carry.md) 的同一十九角光滑曲面 X、几何整 Cartier 曲线 C=(F)、原全部来源和固定分母。记

$$
\mathcal W=H^0(X,\mathcal O_X(\mathcal B_D)),\qquad
\kappa=C^2,\qquad d_D=\mathcal B_D\cdot C,
$$
$$
\mathscr D_m=F^m H^0(X,\mathcal O_X(\mathcal B_D-mC))
\quad(m=2,3,4).
\tag{1}
$$

这里的 D₂、D₃ 是 R938 的完整子空间，D₄ 按同样定义；没有仅取某组 native 列或返回子格。物理点 P=(0,1) 光滑，e=EF 在 P 为单位，E(t)=0。

仍在当前负 fringe 的原四块范围：

$$
\begin{gathered}
s=2h+d_0+2,\quad 1\le d_0\le13,\quad h>21,\\
T=s-15,\quad L=\ell-2,\quad
h<T\le2h,\quad T-h>\kappa,\quad T-h\le L\le h.
\end{gathered}
\tag{2}
$$

设 N=s−13=T+2。原第一核 K₁=ker \bar M 在完整 W 上的准确条件是

$$
\boxed{
(E^iR)(t,g(t))\in t^Nk[[t]]\ (i=0,1,2),\qquad
(E^3R)(t,g(t))\in t^\ell k[[t]].
}
\tag{3}
$$

这是 R821(39)–(40) 的原 M 四块条件。将 R834(23)–(25) 的共同普通单位、四十 charge、真实 t/w 坐标变换作完整下三角逆即可得到 (3)；在全 raw 来源上不先除 t²，所以长窗是 N，而不是返回 H₃ 上的 T。第四行只需长度 ell，前三行的 N 更长，故同一下三角逆在该短窗仍合法。这里未逆转原乘 w¹³ 的跨界带，也未把相对 J 的长窗 s 混入。

由 (2) 准确得到

$$
N\le2h+2,\qquad \ell\le h+2,\qquad h+\ell\ge N.
\tag{4}
$$

所有等号端点均包含在后面的证明中。特征为原 p>211，特别 2 和 6 为单位。

## 2. 完整平方来源的真零角与第二法向

原零角帽为 v₀(R)≥−2、v₀(F)=−3。若 R=F²H∈D₂，则

$$
v_0(H)\ge4,\qquad
v_0\!\left(\sum_{n\ge0}H_n(t)Y^n\right)
=\min_n(4\operatorname{ord}_tH_n-n).
\tag{5}
$$

原固定 d 分母在 t=0 为单位。由 n≥0，H 无 t⁰ 项；t¹ 项只能来自 n=0。因此

$$
H=t c+O(t^2),\qquad c\in k.
\tag{6}
$$

这是逐系数结论，保原其它十八角。设 R 还属于 K₁。因 h>2，物理 g 与 C 的分支 psi 在 t² 内相同。在第二 Euler 行的 t¹ 系数，F(0,1)=0 和 e(P)≠0 给

$$
[t](E^2R)(t,g)=2e(P)^2c.
$$

(3) 迫其为零，故 c=0。于是

$$
\boxed{R=F^2H\in\mathscr D_2\cap K_1
\quad\Longrightarrow\quad t^2\mid H}
\tag{7}
$$

在原系数环中成立。R938 附 A 的四低门已包含这一机制；本篇只将它用于实际 K₁ 的全部长窗。

为锁定 Taylor 的单位，写 E=a(t,Y)∂Y。由 e(P) 为单位及原 graph 支，a(t,g) 也是单位。设 delta=g−psi∈t^hk[[t]]，令 eta=delta/a(t,g)。对逐系数含 t² 的任意原正则 S，有限一阶 Taylor 精确给

$$
S|_C=S(t,g)-\eta(ES)(t,g)+O(t^{2h+2}).
\tag{8}
$$

这只用有限代数 Taylor；不在正特征使用无限 log/exp。以原已有的 Euler 规范位移代替 eta，仅改变 O(t²ʰ) 部分，故不改变 (8) 的余项。E(t)=0 保证全部 Euler 导数仍逐系数含 t²。

将 (8) 用于 S=E²R，并用 (3)–(4)，得到

$$
(E^2R)|_C\in t^N k[[t]].
$$

但沿 C 准确有 E²(F²H)=2e²H，故

$$
\boxed{\operatorname{ord}_P(H|_C)\ge N.}
\tag{9}
$$

H|C 是原线束 O_C(B_D−2C) 的实际全球截面，度数 d_D−2κ。整曲线上非零线束截面的零除子总长等于该度数，包含奇点及所有边界，因而在一个光滑有理点的零阶不超过总度数。于是

$$
\boxed{d_D-2\kappa<N
\quad\Longrightarrow\quad
K_1\cap\mathscr D_2\subset\mathscr D_3.}
\tag{10}
$$

这里 H|C=0 后的全球 F 整除来自 Cartier 限制序列。没有用 H¹ 消失、任意主部满射或局部因子清分母。

## 3. 完整立方来源的准确短行

任意 R=F³K∈D₃ 有 v₀(K)≥7，故逐系数含 t²。由 F(t,g)∈tʰ、乘积法则及 (4)，第零、第一 Euler 行分别至少从 t³ʰ⁺²、t²ʰ⁺² 开始，已自动满足 (3)。

沿 C 有

$$
(E^2R)|_C=0,\qquad (E^3R)|_C=6e^3K|_C.
\tag{11}
$$

同一有限 Taylor 给

$$
(E^3R)(t,g)=6e^3K|_C+O(t^{h+2}),
\tag{12}
$$
$$
(E^2R)(t,g)=\eta\,6e^3K|_C+O(t^{2h+2}).
\tag{13}
$$

(13) 中正向位移可取 delta/a(t,psi)；它与本篇 eta 相差 O(t²ʰ)，乘逐系数 t² 后落入显示余项。

由 ell≤h+2，(12) 的短行条件**等价于** ord_P K|C≥ell。一旦该条件成立，(13) 的首项至少从 tʰ⁺ᵉˡˡ 开始；h+ell≥N 和 N≤2h+2 又付完整第二长行。因此

$$
\boxed{
K_1\cap\mathscr D_3
=\{F^3K\in\mathscr D_3:
   K|_C\in H^0(C,\mathcal O_C(\mathcal B_D-3C)(-\ell P))\}.
}
\tag{14}
$$

右边始终要求 K 来自原 X 上的全球来源，不把它换成 C 上任意可指定的截面。限制 K↦K|C 的核准确为 D₄；特别 D₄⊂K₁。也可直接核 D₄：其乘子 v₀≥10，逐系数含 t³，E²、E³ 分别至少从 t²ʰ⁺³、tʰ⁺³ 开始，严格足够 (3)。

由 (14) 有单射

$$
\boxed{
(K_1\cap\mathscr D_3)/\mathscr D_4
\hookrightarrow
H^0(C,\mathcal O_C(\mathcal B_D-3C)(-\ell P)).
}
\tag{15}
$$

像是原完整全球 restriction 像与所示深零条件的交，没有宣称满射。对任意整曲线上的度 d 线束，利用光滑点 P 的逐阶评价可得 h⁰≤max(0,d+1)。所以

$$
\boxed{
\dim (K_1\cap\mathscr D_3)/\mathscr D_4
\le\max(0,d_D-3\kappa-\ell+1).
}
\tag{16}
$$

若另有 (10)，(15)–(16) 对 D₂ 也成立，并且其左边与 D₃ 的左边准确相等。

## 4. 一个严格数值门消去全部平方／立方首核余方向

**定理。** 在同一原输入 (1)–(4) 下，若

$$
\boxed{d_D-3\kappa<\ell,}
\tag{17}
$$

则

$$
\boxed{K_1\cap\mathscr D_2=\mathscr D_4.}
\tag{18}
$$

证明：由 T−h>κ 和 ell≤h+2，

$$
\ell+\kappa\le h+2+\kappa<T+2=N.
$$

于是 (17) 自动给 d_D−2κ<N，故先由 (10) 进入 D₃。(16) 的右边为零，再由 D₄⊂K₁ 得 (18)。证毕。

严格号不可免费改成等号：若相应度等于读取长度，线束可能有一个非零截面恰在 P 消去全部该度数。一般范围应继续用真实像 (15)，而不是假定该极端截面不存在。

此门与原 P 的 nef 下界 d_D≥4κ+3r_src 并不矛盾；它要求实际 ell>κ+3r_src（若有其它残余交数还须全部计入）。例如，在已研究的条件尺度 h/κ→9/8、T/κ→9/4、ell/κ→9/8 下，**如果同一实际来源另满足** d_D=4κ+o(κ)，(17) 最终成立。这里仅说明该门可作用于当前 2κ<T≤3κ 的尺度，未证明任意原 P 都满足这些附加预算，也未据此宣称全部临界区排除。

在 (17) 下，原约化矩阵在真实 D₂/D₄ 上单射，故原整 M 至少有

$$
\dim_k\mathscr D_2-\dim_k\mathscr D_4
\tag{19}
$$

个单位 Smith 因子：取商的一组 k 基，选原 W 整格中的任意提升，约化列独立便给同阶单位子式。不需要任意所选 factor lift 保持 F² 整除。这个子式与 R834 等已有子式的行列可能重叠，(19) 不能未经联合独立性证明就相加。

## 5. 对 R938 固定仿射问题的准确使用

同一个 P 的两份完整 p³ 解之差，按 R920 附 A 先属于实际 K₂^red⊂K₁。因此在 (17) 下，**若这份差本身属于完整 D₂**，它已经属于 D₄；整个 D₂/D₄ 不能提供这种下一页差方向。

R938 的 beta₂=0 只给全球分解 R=jG+V₂。即使该 R 另在 K₁，jG 与 V₂ 的物理行仍可能互相抵消；本定理没有从 R∈K₁ 推出 V₂∈K₁。故它没有判定全部 K₁/K₂ 的 beta₂、beta₃ 像，也没有删除一般基点 B、受限 S、全部跨界 carry 或完整 p³ 条件。

下一项数学问题仍是这些剩余全来源方向在同一原有限交及下一页中的实际像；(18) 已精确去掉其中一块，而没有将它改称为主目标完成。

# 同一正尾边缘的原一位头完成：数值半径、正常缺陷与紧的精确判据

日期：2026-11-14。作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

状态：以下归约、必要充分条件、紧性和 raw 特例均有完整证明。唯一外部标准工具是 Ando 1973 年关于数值半径的因子分解定理，已核对原刊 Theorem 1，准确应用见 §3。本文将固定真实尾密度的正头完成化为一个达到最小值的紧凸问题；没有证明所有实际尾密度都不满足该条件，也没有解决普通 ISP。

## 1. 保留真实 carry 的一位规范化

在原一个尾起点上把第一位分开；为简记仍写
$$
H=\mathbb C^2\otimes H_1,
\qquad N=\begin{pmatrix}0&t\\I&0\end{pmatrix},
\qquad t=\eta\widehat N_1,
\qquad0<\|t\|\le\eta<1.
$$
令 $\mathcal B=\overline{\mathbb C[I,\widehat N_1]}^{\|\cdot\|}$、
$\mathcal C=\{\widehat N_1\}'$。
原首阶为一的 $S$ 由准确偶奇余数写成
$$
S=\begin{pmatrix}C&tD\\D&C\end{pmatrix},
\qquad C,D\in\mathcal B,
\qquad D\in\mathcal B^\times.
\tag{1.1}
$$
最后一个单位条件来自奇系数的非零常数字符。
定义
$$
Z=D^{-1}C\in\mathcal B,
\qquad\widetilde S=(I\otimes D^{-1})S
=\begin{pmatrix}Z&t\\I&Z\end{pmatrix},
\qquad Q=Z^2-t.
\tag{1.2}
$$
原 $S\mathcal A'$ 理想与 $\widetilde S\mathcal A'$ 相同；这里的 $\mathcal A'$ 指本起点的完整实际交换子。
单位及其逆都是真实有界尾算子，故这一零式归约合法。
没有对 $\|D^{-1}\|$ 或 $\|Z\|$ 宣称跨起点的一致界。

直接比较与 $N$ 的交换块，或者使用 R274 的完整尾基，给
$$
\mathcal A'
=\left\{\begin{pmatrix}U&tV\\V&U\end{pmatrix}:U,V\in\mathcal C\right\}
=\{I\otimes G+\widetilde S(I\otimes H):G,H\in\mathcal C\}.
\tag{1.3}
$$
确切地，第一式中的矩阵对应第二式的 $H=V$、$G=U-ZV$。
这些系数均留在同一个原 $\mathcal C$ 中。

记其正常预湮灭空间
$$
\mathcal N=\{\tau\in\mathcal S_1(H_1):
\operatorname{Tr}(\tau G)=0\text{ 对所有 }G\in\mathcal C\}.
\tag{1.4}
$$
$\mathcal N$ 是迹范数闭复线性子空间，并在左右乘 $\mathcal C$ 元素下保持。
它一般包含非零、非自伴的迹类算子；不把属于 $\mathcal N$ 写成算子本身为零。

## 2. 原正态的全部一位协同条件

固定同一个正尾密度
$$
0\ne\nu\in\mathcal S_1(H_1)_+,
\qquad\tau=\operatorname{Tr}\nu.
$$
任意以它为尾边缘的正头完成都写成
$$
\rho=\begin{pmatrix}A&X\\X^*&B\end{pmatrix}\ge0,
\qquad A+B=\nu.
\tag{2.1}
$$
其真实一阶部分迹为
$$
\operatorname{Tr}_{\mathbb C^2}(\rho\widetilde S)
=\nu Z+X+X^*t.
\tag{2.2}
$$
由于 $Z,t$ 在尾代数中交换，
$$
\widetilde S^2=2\widetilde S(I\otimes Z)-I\otimes Q.
\tag{2.3}
$$
所以二阶部分迹为
$$
2(\nu Z+X+X^*t)Z-\nu Q.
$$
结合 (1.3)，得到准确等价
$$
\boxed{
\operatorname{Tr}(\rho SF)=0\ (F\in\mathcal A')
\iff
\begin{cases}
\nu Q\in\mathcal N,\\
\nu Z+X+X^*t\in\mathcal N.
\end{cases}}
\tag{2.4}
$$
第一行是 R253 已有的正尾相位消元，第二行保留了真实头与同一个正尾边缘之间的协同信息。
第二行一般不能替换为 raw 算子零式。

## 3. 消去两个未知正对角块：准确的数值半径条件

令 $K_\nu=\overline{\operatorname{Ran}\nu}$ 为 $\nu$ 的支撑空间。
数值半径记为
$$
w(T)=\sup_{\|h\|=1}|\langle Th,h\rangle|.
$$
定义紧候选集
$$
\mathfrak X_\nu
=\{\nu^{1/2}K\nu^{1/2}:
K\in B(K_\nu),\ w(K)\le\tfrac12\}.
\tag{3.1}
$$
$K$ 在 $K_\nu^\perp$ 上补零理解，(3.1) 不使用无界的 $\nu^{-1/2}$。

**引理 3.1。** 给定 $X\in\mathcal S_1(H_1)$，存在 $A,B$ 满足 (2.1)，当且仅当
$X\in\mathfrak X_\nu$。

**证明。** 若 (2.1) 成立，则 $0\le A,B\le\nu$。
对应的有界形式给一个 $0\le R\le I$，使
$$
A=\nu^{1/2}R\nu^{1/2},\qquad
B=\nu^{1/2}(I-R)\nu^{1/2}.
$$
正块矩阵的 Cauchy–Schwarz 不等式给
$$
|\langle Xv,u\rangle|^2
\le\langle Au,u\rangle\langle Bv,v\rangle
\le\|\nu^{1/2}u\|^2\|\nu^{1/2}v\|^2.
$$
故这个双线性形式在 $\operatorname{Ran}\nu^{1/2}$ 上定义唯一的收缩 $K$，
$X=\nu^{1/2}K\nu^{1/2}$。
在其稠密像上作形式合同，再连续延伸，得到
$$
\begin{pmatrix}R&K\\K^*&I-R\end{pmatrix}\ge0.
\tag{3.2}
$$
把同一个向量用于两个角，正性迫
$$
|\langle Kh,h\rangle|^2
\le\langle Rh,h\rangle\langle(I-R)h,h\rangle
\le\tfrac14\|h\|^4.
$$
所以 $w(K)\le1/2$。

反之，Ando 的标准因子分解（出处在下）应用于 $2K$ 给某个
$0\le R\le I$ 及收缩 $V$，使
$$
K=R^{1/2}V(I-R)^{1/2}.
$$
因此 (3.2) 是正块矩阵；用 $\nu^{1/2}\oplus\nu^{1/2}$ 作合同即给 (2.1)。
两个对角块都是迹类，因为它们介于 $0$ 和 $\nu$ 之间。
$\square$

**标准工具的精确来源。** T. Ando，*Structure of operators with numerical radius one*，
Acta Sci. Math. (Szeged) **34** (1973), 11–15，Theorem 1（原刊第13页）：
$w(T)\le1$ 等价于存在自伴收缩 $A_0$ 和收缩 $B_0$ 使
$T=(I+A_0)^{1/2}B_0(I-A_0)^{1/2}$。
令 $T=2K$、$R=(I+A_0)/2$ 即得上面的形式。
[期刊原文 PDF](https://acta.bibl.u-szeged.hu/14381/1/math_034_011-015.pdf)。
这里引用的是该标准因子分解，不是任何关于本题正常湮灭者的新断言。

从正块的 Hilbert–Schmidt 因子分解还得到
$$
\boxed{\|X\|_1\le\sqrt{\operatorname{Tr}A\operatorname{Tr}B}
\le\tau/2\qquad(X\in\mathfrak X_\nu).}
\tag{3.3}
$$
例如把正块写成 $[L_0;L_1][L_0^*\ L_1^*]$，则
$X=L_0L_1^*$，再用 Schatten Hölder 不等式即可。

若 $\nu$ 有限秩、支撑为 $E$，条件尤其明确：
$$
X=P_EX P_E,
\qquad
w\!\left(\nu_E^{-1/2}X|_E\nu_E^{-1/2}\right)\le\tfrac12.
\tag{3.4}
$$
这里只在有限维 $E$ 上求真正的有界逆。
任何正完成都支持在 $\mathbb C^2\otimes E$，其秩至多 $2\operatorname{rank}\nu$。

## 4. 完整正头完成的必要充分条件与达到的最小值

结合 (2.4) 和引理 3.1 得到主判据：
$$
\boxed{
\exists\rho\ge0:\quad
\operatorname{Tr}_{\mathbb C^2}\rho=\nu,\quad
\operatorname{Tr}(\rho SF)=0\ (F\in\mathcal A')
}
$$
当且仅当
$$
\boxed{
\nu Q\in\mathcal N,\qquad
\exists X\in\mathfrak X_\nu:\
\nu Z+X+X^*t\in\mathcal N.}
\tag{4.1}
$$
这并没有预先指定该正完成在整个原 $\mathcal A'$ 上的每一个泛函值；它保持给定的完整正尾边缘，并要求原理想湮灭。若还要保持另一个给定原泛函，必须另加对应线性约束。

以下紧性使“存在”不能被替成没有控制的近似网。

**引理 4.1。** $\mathfrak X_\nu$ 在迹范数中紧。

**证明。** $w(K)\le1/2$ 蕴含 $\|K\|\le1$，因此它是有界的 WOT 闭集合，在有界集合上也 ultraweak 闭。
Banach–Alaoglu 给紧性。令 $E_m$ 为 $\nu$ 的递增有限谱投影，
$\nu_m=E_m\nu E_m$。对 $\|K\|\le1$，Schatten Hölder 给一致误差
$$
\|\nu^{1/2}K\nu^{1/2}
-E_m\nu^{1/2}K\nu^{1/2}E_m\|_1
\le2\sqrt{\tau\operatorname{Tr}\nu(I-E_m)}\longrightarrow0.
\tag{4.2}
$$
有限维压缩把 WOT 收敛变成迹范数收敛；(4.2) 便说明这个夹乘映射在有界球上从 WOT 到迹范数连续。
所以其紧域的像 $\mathfrak X_\nu$ 紧。$\square$

因此以下最小值准确达到：
$$
\boxed{
\Delta(\nu;Z,t)
=\min_{X\in\mathfrak X_\nu}
\operatorname{dist}_1(\nu Z+X+X^*t,\mathcal N).}
\tag{4.3}
$$
主判据等价于
$$
\boxed{\nu Q\in\mathcal N\quad\text{且}\quad
\Delta(\nu;Z,t)=0.}
\tag{4.4}
$$
若对一个固定 $\nu$ 找到趋零的距离序列，就确有一个 $X$ 达到零；在这里不发生固定尾边缘下的奇异态逃逸。
这个结论不声称任意改变的 $\nu_m$ 具有共同紧性。

## 5. 完整的双对偶证书

为了使 (4.3) 可由真正原尾测试检查，定义数值半径的对偶范数
$$
w^*(Y)=\sup_{w(K)\le1}|\operatorname{Tr}(KY)|,
\qquad Y\in\mathcal S_1(K_\nu).
\tag{5.1}
$$
它满足 $\|Y\|_1\le w^*(Y)\le2\|Y\|_1$。
当 $Y\ge0$ 时 $w^*(Y)=\operatorname{Tr}Y$，这是沿 $Y$ 的谱分解直接用数值半径定义得到的。

迹类商空间对偶以及紧凸分离给
$$
\boxed{
\begin{aligned}
\Delta(\nu;Z,t)
=\sup_{\substack{G\in\mathcal C\\\|G\|\le1}}
\bigg\{&\operatorname{Re}\operatorname{Tr}(\nu ZG)\\
&-\frac12 w^*\!\left(
\nu^{1/2}\bigl[G+G^*t^*\bigr]\nu^{1/2}\right)\bigg\}.
\end{aligned}}
\tag{5.2}
$$

**证明。** $\mathcal C$ 为 ultraweak 闭代数，故 $\mathcal N^\perp=\mathcal C$。
对任意迹类 $Y$，Hahn–Banach 商对偶给
$$
\operatorname{dist}_1(Y,\mathcal N)
=\sup_{G\in\mathcal C,\ \|G\|\le1}\operatorname{Re}\operatorname{Tr}(YG).
$$
把 $Y=\nu Z+X+X^*t$ 代入。
$\mathfrak X_\nu$ 是紧凸集；上述算子单位球是 ultraweak 紧凸集，配对分别连续且实仿射。
等价地直接对迹类商中的紧凸像与零点作 Hahn–Banach 分离，可交换此处的 min 与 sup。

固定 $G$ 时有
$$
\operatorname{Re}\operatorname{Tr}(XG+X^*tG)
=\operatorname{Re}\operatorname{Tr}\bigl(X[G+G^*t^*]\bigr).
$$
用 (3.1)，对 $X$ 的最小值就是 (5.2) 中的负对偶范数项；数值半径球平衡，故实部上确界等于绝对值上确界。
这证明公式。$\square$

任意一个具体原 $G\in\mathcal C$ 使花括号严格为正，便排除了给定 $\nu$ 的正头完成。
只有标量尾条件 $\nu Q\in\mathcal N$ 时，尚不能删除这个独立的完成检验。
一个较粗但便于使用的必要界是
$$
\boxed{
\left|\operatorname{Tr}(\nu ZG)\right|
\le\frac\tau2\bigl(\|G\|+\|tG\|\bigr)
\le\frac{\tau(1+\|t\|)}2\|G\|
\quad(G\in\mathcal C).}
\tag{5.3}
$$
它由 (2.4)、(3.3) 直接得到，但弱于完整的 (5.2)。

## 6. raw 零式的唯一反线性 Stein 解

若进一步要求 raw 一阶零式，则应把 (2.2) 设为算子零：
$$
X+X^*t=-\nu Z.
\tag{6.1}
$$
由于 $\|t\|<1$，$X\mapsto-X^*t$ 是迹类实 Banach 空间上的严格收缩。
故 (6.1) 有唯一迹类解。把相邻两项配对可写成
$$
\boxed{
X_0=-\sum_{k=0}^{\infty}(t^*)^k
\bigl(\nu Z-Z^*\nu t\bigr)t^k,
\qquad
\|X_0\|_1\le\frac{\tau\|Z\|}{1-\|t\|}.}
\tag{6.2}
$$
级数按迹范数绝对收敛。
例如把 (6.1) 与其伴随联立，得到
$X-t^*Xt=-\nu Z+Z^*\nu t$，正好给出 (6.2)；反线性收缩的唯一性保证它也满足原式。

于是固定正尾边缘的 raw 正头完成存在，当且仅当
$$
\boxed{X_0\in\mathfrak X_\nu.}
\tag{6.3}
$$
若同时要求原理想湮灭，还须加 $\nu Q\in\mathcal N$。
有限秩时可以用 (3.4) 精确检验：首先要有
$X_0=P_EX_0P_E$，然后才对支撑上归一化矩阵检验数值半径。
因 $t^*$ 可能把支撑移出 $E$，这个支撑条件本身不是免费的。

与 R272 的关系应分清：R272 固定一个原正头密度，只修改单侧头块，并保持原泛函；它非平凡时必失自伴。
本节允许两个正对角块一起重选，所以给的是更一般的正完成判据，并不与 R272 的单侧禁阻矛盾。
反过来，不能因为 (6.2) 有唯一迹类解，就声称这个解满足 (6.3)。

## 7. 有限秩原见证与跨层相容性

若给定 $\nu$ 的秩为 $r<\infty$，$\mathfrak X_\nu$ 是一个有限维紧凸集。
固定 $E=\operatorname{Ran}\nu$ 后，$X$ 的变量仅为 $r\times r$ 矩阵；
原缺陷 $\nu Z+X+X^*t$ 的值域在 $E$ 中，其伴随值域在
$$
E+Z^*E+t^*E
$$
中。因此对全部 $\mathcal C$ 的配对只依赖一个有限维的真实压缩空间。
可以取该压缩空间的有限基，将 (4.1) 写成有限个线性方程和 (3.2) 的正块约束。
这不提供只依 $r$ 的统一最高测试幂数，也不把未知原向量变成已知有限数值数据。

对真正的原正见证 $\rho$，R253 给同一链
$$
\nu_m=\operatorname{Tr}_{K_m}\rho\ge0,
\qquad\operatorname{Tr}_{\mathbb C^2}\nu_m=\nu_{m+1}.
$$
相位乘积 $Q_m$ 在第 $m$ 位的奇块仍为真实单位，因为其形式首阶为一。
写成 (1.1) 后得到对应的 $Z_m,t_m$，原 $\nu_m$ 的真实非对角块就是某个
$X_m\in\mathfrak X_{\nu_{m+1}}$，并必须满足
$$
\nu_{m+1}(Z_m^2-t_m)\in\mathcal N_{m+1},
\qquad
\nu_{m+1}Z_m+X_m+X_m^*t_m\in\mathcal N_{m+1}.
\tag{7.1}
$$
相应 $\Delta(\nu_{m+1};Z_m,t_m)=0$ 是每一步的必要条件。
这些 $\nu_m$ 和 $X_m$ 来自同一正密度，不能逐层任意重选。
原正常性还要求 R253 的真实尾真空缺陷趋零；本稿未给该速度。

固定 $\nu$ 的紧性足以把本步的近似完成变成准确完成。
它不能单独把不同 $m$ 的可行解拼成同一个全局正常态，也不能对可能增长的
$\|D_m^{-1}\|$、$\|Z_m\|$ 提供免费的一致估计。

## 8. 尚未关闭的部分

已完成的是同一真实正尾边缘的正头完成的必要充分刻画、达到的最小距离、全部原右测试的双对偶证书，以及 raw 特例的唯一迹类解和准确正性检验。
新增的协同条件保留了正性和原正常缺陷，没有把 $\mathcal N$ 中的非零元素删成零。

仍须对原慢行的实际相容尾密度证明某一步 (5.2) 严格为正，或从全链 (7.1) 与正常真空趋近推出矛盾。
目前没有给出这一步，也没有从某个有限头的可行或不可行扩大到所有原见证。
普通 Hilbert ISP 和一般正常湮灭者的排除均保持开放。

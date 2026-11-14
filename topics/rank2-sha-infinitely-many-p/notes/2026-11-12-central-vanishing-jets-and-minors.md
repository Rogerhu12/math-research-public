# 中央图像的真正 vanishing jets：精确 minors 公式与首坏区间

日期：2026-11-12。**状态：局部算子范数公式及首区间恒等式已证明；尚无改良的全局 \(\alpha\) 界。**

本篇从 R44 的系数预算转到 Herblot 实际使用的评价映射。
固定
\[
F(Z)=\mathscr D(Z)=\sum_{m\ge0}e_mZ^m\in\mathbb Q[[Z]],
\qquad e_0=0,
\]
及 \(X=\mathbb P^2_{\mathbb Q}\) 中 \(Y=F(Z)\) 的形式图像。
这里不以某个 \(e_k\) 的大小代替评价映射的范数。

## 1. 真正的截面空间与 prefix 矩阵

对 \(D\ge0\)，用 \(Z^aY^b\)、\(a,b\ge0,\ a+b\le D\)
作为 \(H^0(\mathbb P^2,\mathcal O(D))\) 在仿射 chart 的标准基。
记
\[
N_D=\binom{D+2}{2},\qquad
r_j=\left([Z^j]Z^aF(Z)^b\right)_{a+b\le D}\in\mathbb Q^{N_D}.
\]
前缀矩阵为
\[
A_{D,<k}=
\begin{pmatrix}r_0\\r_1\\ \vdots\\r_{k-1}\end{pmatrix}.
\tag{1.1}
\]
真正的 vanishing filtration 是
\[
V_{D,k}=\ker(A_{D,<k}:\mathbb Q^{N_D}\to\mathbb Q^k).
\]
它由在图像上消失至 \(k-1\) 阶的全部截面组成。
第 \(k\) 阶评价为
\[
\varphi_D^k:V_{D,k}\to\mathbb Q,\qquad
v\longmapsto r_kv.
\tag{1.2}
\]
\((dZ)^k\) 与 \(\mathcal O(D)\) 在有理基点的标准平凡化已在这里取为单位。

在有限位 \(p\)，标准整模型给截面空间的系数 sup 范数。
\(V_{D,k}\otimes\mathbb Q_p\) 使用其诱导范数；
其单位球是饱和格
\[
L_{D,k,p}
=
(V_{D,k}\otimes\mathbb Q_p)\cap\mathbb Z_p^{N_D}.
\tag{1.3}
\]
因而必须使用 (1.3)，不能先选一组带分母的全局消去多项式，
再把它们误当作局部单位基。

## 2. Plücker minors 给局部范数的准确式

令 \(r=\operatorname{rank}A_{D,<k}\)。
选其任意 \(r\) 个独立行，组成 \(r\times N_D\) 矩阵 \(B\)。
若 \(r_k\) 属于它们的行空间，则 \(\varphi_D^k=0\)。

否则置
\[
\delta_p(B)=
\min_{\substack{I\subset\{1,\ldots,N_D\}\\|I|=r}}
v_p(\det B_I),
\]
忽略零 minor；\(r=0\) 时取 \(\delta_p(B)=0\)。
对增广矩阵
\[
B^+=\begin{pmatrix}B\\r_k\end{pmatrix}
\]
同样定义其 \((r+1)\)-minors 的最小赋值。
则
\[
\boxed{\quad
\log\|\varphi_D^k\|_p
=
\bigl(\delta_p(B)-\delta_p(B^+)\bigr)\log p.
\quad}
\tag{2.1}
\]
这是等式，不只是从系数估计来的上界。

**证明。**
行空间与 \(\mathbb Z_p^{N_D}\) 的交是饱和子模，
故可选其整基并扩成 \(\mathbb Z_p^{N_D}\) 的整基。
等价地，可用左边的 \(\mathrm{GL}_r(\mathbb Q_p)\)
及右边的 \(\mathrm{GL}_{N_D}(\mathbb Z_p)\)
将 \(B\) 化为 \((I_r\ 0)\)。

右边的整可逆变换及其逆保持系数 sup 范数，
也保持 exterior-power sup 范数。
左边变换给 \(B\) 和 \(B^+\) 的 wedge 同时乘相同的 determinant，
故 (2.1) 的差不变。

化简后，(1.3) 正是最后 \(N_D-r\) 个坐标的标准整格；
评价范数是 \(r_k\) 在这些坐标上的最大绝对值。
\(B\) 的 wedge 范数为一，而 \(B^+\) 的非零 maximal minors
恰给这些坐标。
这就得到 (2.1)。\(\square\)

不同的独立前缀行基之间只差 \(\mathrm{GL}_r(\mathbb Q)\)，
所以该式不依赖所选行。
若原前缀已有冗余行，不应把零的“满行数 minor”当作
\(\delta_p(B)=+\infty\)。

在实际算术高度中，\(\log\|\varphi_D^k\|_p\) 可以为负；
不能先把所有负项删去，再声称得到了其最优 \(\alpha\)。

## 3. 一个明确的截面说明系数与评价为何不同

取
\[
P_k(Z,Y)=Y-\sum_{j<k}e_jZ^j,\qquad D\ge k-1.
\]
它确实在图像上消失至 \(k-1\) 阶，并满足
\[
\varphi_D^k(P_k)=e_k.
\]
但它的局部截面范数为
\[
\|P_k\|_p=\max\left(1,\max_{j<k}|e_j|_p\right).
\]
所以这个具体截面只给出
\[
\|\varphi_D^k\|_p
\ge
\frac{|e_k|_p}
{\max(1,\max_{j<k}|e_j|_p)}.
\tag{3.1}
\]
分母是先前消去所需的范数成本。

例如对 \(F(Z)=e^Z\)，在
\(\operatorname{span}\{1,Z,\ldots,Z^{k-1},Y\}\) 的唯一 vanishing 方向上，
该比例准确为
\[
\frac{|1/k!|_p}{|1/(k-1)!|_p}=p^{v_p(k)}.
\]
全部有限位相加仅为 \(\log k\)，并非由单个
\(1/k!\) 会误读出的 \(\log(k!)\)。
这没有计算完整 \(\mathcal O(D)\) 空间的最优范数，
只明确显示：即使选了一个真实消去截面，也必须计入它自身的范数。

## 4. Ordinary 首个坏区间的实际中央式

固定一个好 ordinary \(p\)，令 \(A_p\in\mathbb F_p^\times\) 为 Hasse 不变量。
完整 theta 矩已证明
\[
M_m=\Omega_p^{2m}(m!)^2d_m\in\mathcal O,\qquad
M_{m+p-1}\equiv M_m\pmod p\quad(m\ge1).
\tag{4.1}
\]
在形式乘法坐标中
\(\delta=\Omega_p^{-1}\partial_{\log}\)。
由 \(\partial_{\log}^p=\partial_{\log}\) 与
\(\delta^p=A_p\delta\)，
\[
\Omega_p^{1-p}\equiv A_p\pmod p.
\tag{4.2}
\]

对 \(1\le s\le p-1\)，令 \(m=p-1+s\)。
两边的 \(p^2d_m\) 都已为整，因为 \(v_p(m!)=1\)。
使用
\[
\frac p{(p-1+s)!}\equiv-\frac1{(s-1)!}\pmod p
\]
及 (4.1)、(4.2)，得到
\[
p^2d_{p-1+s}
\equiv A_p^2s^2d_s\pmod p.
\]
split 处 \(f\) 的约化属于 \(\mathbb F_p^\times\)，故 \(f^{p-1}=1\)，
有理下降后同样是
\[
\boxed{\quad
p^2e_{p-1+s}\equiv A_p^2s^2e_s\pmod p,
\qquad1\le s\le p-1.
\quad}
\tag{4.3}
\]

令
\[
F_{<p}(Z)=\sum_{0\le s<p}e_sZ^s,\qquad
\theta=Z\frac d{dZ}.
\]
这些低权系数在 ordinary 处为整。
于是 (4.3) 等价于下面这个有限截断恒等式：
\[
\boxed{\quad
p^2F(Z)
\equiv A_p^2 Z^{p-1}\theta^2F_{<p}(Z)
\pmod{p,\ Z^{2p-1}}.
\quad}
\tag{4.4}
\]
左边先截断到次数 \(<2p-1\)，再乘 \(p^2\) 并还原。
这不是将整个可能含更深分母的无限级数直接模 \(p\)。

与此相对，inert 平移笔记给出
\[
p^2e_{p+1+s}
\equiv\frac{\kappa_p^2}{(Nf)^2}e_s\pmod p,
\qquad0\le s\le p-3.
\tag{4.5}
\]
两类素数的首坏区间不同：ordinary 出现 \(\theta^2\)，
inert 出现固定标量乘低权本身。
没有把二者改写成相同的 Cartier 周期。

## 5. 首坏区间作用于真正多项式截面

在 ordinary 情形，取任意整多项式 \(P(Z,Y)\in\mathbb Z_p[Z,Y]\)。
因为 \(F(0)=0\)，它的第一个可能非整系数在次数 \(p\)；
次数 \(<2p-1\) 的乘积不可能包含两个这样的非整因子。
(4.4) 因而给
\[
\boxed{\quad
p^2P(Z,F(Z))
\equiv
A_p^2Z^{p-1}
\partial_Y\bar P(Z,\overline{F_{<p}}(Z))
\,\theta^2\overline{F_{<p}}(Z)
\pmod{p,\ Z^{2p-1}}.
\quad}
\tag{5.1}
\]
上横线表示合法还原的整低权部分。
单个高权只含 \(p^{-1}\) 的项被 \(p^2\) 消去；
两个高权因子的次数至少 \(2p\)，所以不会漏入当前范围。

因此当 \(P\) 真正属于 \(L_{D,k,p}\)，
其前 \(k\) 个零系数会给 (5.1) 右边的相应消失条件。
这已是对真实消去多项式的约束，而不仅是某个 \(e_m\) 的赋值。

但 (5.1) 本身尚未给所有 \(D,k\) 的范数界：
它只处理第一个长度约 \(p\) 的坏区间，且仍需知道
\(\partial_YP\) 在同一个低权图像上的实际消失阶。
不能把这一步自动迭代为固定阶线性微分方程。

## 6. 改善 arithmeticity 还需要证明什么

对每个 \(D,k\)，(2.1) 把所需条件精确转为相邻 Plücker 范数之差。
要得到某个 \(\alpha\)-arithmetic 上界，必须对这些**真实前缀**
证明
\[
\sum_{p\notin S}
\bigl(\delta_p(B)-\delta_p(B^+)\bigr)\log p
\le
\alpha' k\log k+C(k+D)
\tag{6.1}
\]
对所有 \(\alpha'>\alpha\)、全部 \(k,D\) 成立，
并另有各固定 places 的线性界。

R40 中心假设控制的 \(e_{p-1}\) 只是前缀矩阵中的部分数据。
它若提高某些 minors 的赋值，也可能同时提高前缀与增广矩阵的赋值；
(2.1) 需要两者之差。
而一个 entry 的额外整除通常不能使所有 maximal minors 都增加赋值。

因此下一个真正可检验的数学问题是：
实际 Kronecker/CM 关系能否结合 (5.1)，
约束这些饱和 vanishing 格的 augmented minors。
R44 的系数预算没有回答这个问题；
四阶原子测度模型则说明仅有“有界矩与中心四阶零”也不足以回答。

本篇没有宣称得到了 \(\alpha<1/2\)，也没有以数值线性代数代替统一证明。
新增的是精确的局部范数公式和实际中央序列的第一坏区间截面恒等式。

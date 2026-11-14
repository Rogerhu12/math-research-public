# R346：原 Miller 测试的非原点残数单射与完整 Cartier 极部

日期：2026-11-13。**状态：以下指定测试族在全部非原点极上的准确残数、真实整数残数映射的 \(p\)-饱和、完整 Cartier 极部分解及其单射均已证明。此处的单位 minor 属于这份明确的残数测试格，尚未被当作原 \(C_2(M)\) 的子商或新的中央零。原指定 \(Q_-\) 分支保留；不能由全局成对残数相消替代它。**

## 1. 同一实际极与一份有限 étale 整代数

保留 R338、R342 的 \(p=6s-1\)、\(b=17\)、\(p>7,p\ne17\)，
\[
E':Y^2=X^3+b^2,\qquad Q_\pm=(0,\pm b),\qquad
r=(Y-b)/(Y+b).
\]
令
\[
n_0=(p-1)/2=3s-1,\qquad N=3n_0+1=(3p-1)/2,\qquad
\xi=X^3/b^2.
\]
R342 的真正特征零反序多项式，除以其常数后，准确为
\[
\boxed{\mathscr B_p(\xi)=
 \sum_{j=0}^{n_0}\binom{n_0}{j}\frac{N}{N-3j}\xi^j.}
\tag{1}
\]
因此原函数完整写成
\[
\boxed{
T_p(X)=\frac{X}{4N^2b}\,
       \frac{\mathscr B_p(\xi)^2}{(1+\xi)^p}.}
\tag{2}
\]
这不是另选的模 \(p\) 提升：它正是 R342 的
\(X\widetilde{\mathscr R}_p(X)^2/[b^p(X^3+b^2)^p]\)。

所有 \(N-3j\) 与 \(6j+1\) 都为 \(p\) 单位。又
\[
\frac{N}{N-3j}-\frac1{6j+1}
=\frac{9pj}{(N-3j)(6j+1)},
\]
故 (1) 的准确约化为
\[
\boxed{B_p(\xi)=
\sum_{j=0}^{n_0}\binom{n_0}{j}\frac{\xi^j}{6j+1},\qquad
B_p+6\xi B_p'=(1+\xi)^{n_0}.}
\tag{3}
\]
\(B_p(0)=1\)，最高系数 \(1/(3p-2)\) 是单位。还准确有
\[
B_p(-1)=\frac{n_0!}{(7/6)_{n_0}}\ne0.
\tag{4}
\]
有限和恒等式由
\(\int_0^1(1-v^6)^n\,dv\) 的积分分部递推证明；
模 \(p\) 的分母因子从 \(s+1\) 到 \(4s-1\)，均为单位。
若 \(B_p\) 与其导数有共同根，由 (3) 该根只能是 \(-1\)，与 (4) 矛盾。
所以 \(B_p\) 平方自由，根均不在 \(0,-1\)。

记
\[
\mathcal A=\mathcal O[\xi]/(\mathscr B_p),\qquad
A=k[\xi]/(B_p).
\tag{5}
\]
最高系数为单位，必要时按它归一为首一式。
\(\mathcal A\) 是有限 étale 整代数；\(\xi,1+\xi\) 都是其中的单位。
再加入
\[
X^3=b^2\xi,\qquad Y^2=b^2(1+\xi)
\tag{6}
\]
仍是有限 étale 扩张。
(5)、(6) 描述原 \(T_p\) 的全部非原点零：每个根的两个 \(Y\) 分支和三个 \(X\) 分支均保留。
它们不是二挠点，也不是 \(Q_\pm\)。

## 2. 原微分给出的整数导数多项式

回到固定覆盖
\[
\mathscr C:y^2=v^6+b,\quad x=v^2,\quad
D=\partial_z,\quad Dv=y/v,\quad Dy=3v^4.
\]
对每个整数 \(k\)，直接微分给
\[
\boxed{D^2(v^k)
=k(k+1)v^{k+2}+k(k-2)b\,v^{k-4}.}
\tag{7}
\]
定义整数多项式 \(C_m(Z)\)：
\[
D^{2m}v=v^{2m+1}C_m(b/v^6),\qquad C_0=1.
\]
若 \(C_m=\sum c_{m,j}Z^j\)、\(k_{m,j}=2m+1-6j\)，则完整递推为
\[
\boxed{
C_{m+1}(Z)=\sum_jc_{m,j}
 \bigl(k_{m,j}(k_{m,j}+1)Z^j+
       k_{m,j}(k_{m,j}-2)Z^{j+1}\bigr).}
\tag{8}
\]
因此 \(\deg C_m\le m\)、\(C_m(0)=(2m)!\)。

对 \(1\le n\le s-1\)，置
\[
\boxed{
A_n(\xi)=\frac1{(6n-1)!}
 \sum_{j=0}^{3n-1}
 (6n-1-6j)c_{3n-1,j}\xi^j.}
\tag{9}
\]
因为 \(6n-1<p\)，这个多项式的全部系数在 \(\mathcal O\) 中，并且
\[
\boxed{\deg A_n\le3n-1,\qquad A_n(0)=1.}
\tag{10}
\]
例如 \(A_1=1+7\xi^2/8\)。

在 R342 的下降坐标 \(X=b/v^2,\ Y=by/v^3\) 中，
\(b/v^6=\xi\)，故 (8)、(9) 准确给
\[
\boxed{
\frac{D^{6n-1}v}{(6n-1)!}
=\frac{Y}{b}\,b^n\xi^{-n}A_n(\xi).}
\tag{11}
\]
这份导数始终来自同一个原椭圆微分，不是假设独立的极部参数。

## 3. 原非原点残数的完整公式

固定
\[
1\le K\le s-1,\qquad q=(q_1,\ldots,q_K),
\qquad
\omega_q=\left(\sum_{n=1}^Kq_nT_p^{-3n}\right)d\log r.
\tag{12}
\]
R342 的实际 Schur 测试满足更强的 \(K=s-14\)；
原中央测试满足 \(K=s-1\)。这里统一覆盖二者。

令 \(P\) 是 (5)、(6) 的某个几何点。其上 \(Z_p=0\) 是一阶零。
特征 \(p\) 中 \(dZ_p=dz\)，所以在该点的正规局部参数 \(Z_p\) 中，
次数小于 \(p\) 的 Taylor 系数准确为 \(D^j/j!\)。
又 \(\mathscr C\to E'\) 在这些点不分歧，且
\[
Z_p^{-6n}v\,dz=-\tfrac16T_p^{-3n}d\log r.
\]
因此
\[
\boxed{
\operatorname{Res}_{P}(\omega_q)
=-6\,\frac{Y(P)}b
 \sum_{n=1}^Kq_nb^n\xi(P)^{-n}A_n(\xi(P)).}
\tag{13}
\]
两个 \(Y\) 分支的符号均包含在这一式中。

置
\[
\boxed{
P_q(\xi)=\sum_{n=1}^Kq_nb^n\xi^{K-n}A_n(\xi).}
\tag{14}
\]
于是非原点残数整族就是
\[
\boxed{-6(Y/b)\xi^{-K}P_q(\xi)\quad\text{在 }A\text{ 及 (6) 上}.}
\tag{15}
\]
各个前因子都是单位。

## 4. 全非原点残数单射及真实整数饱和

**定理1。** 在上述完整范围内，
\[
\boxed{\text{所有非原点残数为零}\quad\Longleftrightarrow\quad q=0.}
\tag{16}
\]
不仅如此，同一真实特征零有理形式 (12) 在这些有限 étale 极上的残数映射，
从 \(\mathcal O^K\) 到其完整整残数模，是 primitive 的整单射。

**证明。** 由 (10)，
\[
\deg P_q\le3K-1<3s-1=\deg B_p.
\tag{17}
\]
所以 (15) 在全部根为零，当且仅当 \(P_q=0\)。
若 \(q_n\) 不全为零，取最大 \(n\) 使 \(q_n\ne0\)，
则 \(P_q\) 的最低非零项为
\(q_nb^n\xi^{K-n}\)，由 \(A_n(0)=1\) 不可能抵消。
这证明 (16)。

整数结论也有明确的单位 minor。
在 \(\mathcal A\) 的多项式坐标中，(14) 不发生模 \(\mathscr B_p\) 降次数，
因为 (17) 已严格低于它的次数。
按 \(n=K,K-1,\ldots,1\) 排列列，读 \(\xi^0,\ldots,\xi^{K-1}\) 行，
矩阵为三角形，准确行列式
\[
\boxed{b^{K(K+1)/2}\in\mathcal O^\times.}
\tag{18}
\]
(6) 是自由的有限 étale 扩张，(15) 的单位因子可在整个残数模中整可逆地乘掉。

还须核此 minor 属于真正特征零残数，而非任选提升。
原极由 (1) 定义，所有坐标和分母均整且为单位。
R342 的完整特征零误差
\[
DZ_p=1-\frac{3p x^2\mathscr R_p(x)}{y^{p+1}}
\]
在该极上甚至准确取一；其邻域的 \(Z_p\) 因而是整局部参数。
各所读次数至多 \(6K-1<p\)，局部除法及相应阶乘均为单位。
真实残数的约化正是 (13)，所以其整矩阵在 (18) 上仍有单位 minor。
这证明 primitive 整单射。没有引入随 \(K\) 变化的额外坏素数。 \(\square\)

(18) 是本篇指定残数测试格中的结论。
它尚未成为原 \(J\) 或 \(C_2(M)\) 的一个已经支付的子商，
不能直接计作原 Smith 尾的新深度。

## 5. 完整 Cartier 极部，无未控的全纯补偿

令 \(\mathsf C\) 为特征 \(p\) 曲线上的 Cartier 算子。
先把全部可能的极付全。

- 在 \(Q_\pm\)，(12) 的极阶至多 \(3K+1<p\)。
- 在 (5)、(6) 的非原点零，极阶至多 \(6K<p\)。
- 原二挠点是 \(T_p\) 的极，所以 (12) 在那里没有极。
- 在 \(E'\) 的无穷点，取相容的局部参数 \(\nu\)。
  有 \(T_p=(b/4)\nu^4\) 乘一个 \(\nu^6\) 单位，
  \(d\log r=6b\nu^2\) 乘一个 \(\nu^6\) 单位再乘 \(d\nu\)。
  因而每项只含指数 \(2-12n+6j\)，且极阶最多 \(12K-2<2p\)。

Cartier 只保留指数 \(-1\pmod p\)。
在无穷处可能产生极的 \(-1,-p-1\) 分别模6为5、0，
与实际指数模6为2不符，所以 \(\mathsf C\omega_q\) 在无穷处正规。
其他有限极在 Cartier 后都至多为简单极，残数准确为原残数的 \(p\) 次根。

原形式在 \(X\mapsto\omega X,\ Y\mapsto Y\) 下不变，因为
\(T_p\mapsto\omega T_p\)。Cartier 与这个拉回相容，故 \(\mathsf C\omega_q\) 也不变。
而 \(H^0(E',\Omega^1)\) 由 \(dX/Y\) 生成，其特征为非平凡的 \(\omega\)。
因此指定全部残数之后没有不变的全纯补偿。
这一步可以在加入 \(\omega\) 后证明，再下降。

下面把这一完整极部写成明确有限算子。
对于 \(c\in A\)，取
\[
L_c=\operatorname{rem}_{B_p}(c B_p'),\qquad
\lambda_c=\frac{[\xi^{n_0-1}]L_c}{[\xi^{n_0}]B_p},
\]
并定义
\[
\boxed{
\eta(c)=\frac1b\left(
 \frac{Y L_c(\xi)}{B_p(\xi)}\,d\xi-2\lambda_c\,dY
 \right).}
\tag{19}
\]
它在非原点零的残数为 \((Y/b)c\)，在 \(Q_\pm\) 正规。
在无穷处
\(L_c/B_p=\lambda_c/\xi+O(\xi^{-2})\)，
且 \(dY=b^2d\xi/(2Y)\)，所以 (19) 准确消去唯一可能的四阶极，亦在那里正规。
因此 (19) 是全部显示残数的唯一不变正规补偿。

有限 étale 代数 \(A\) 上的绝对 Frobenius \(\varphi\) 可逆。
记
\[
h_q=\sum_{n=1}^Kq_n h_n^*,\qquad
c_q=\varphi^{-1}\!\left(
 -6(1+\xi)^{-n_0}\xi^{-K}P_q(\xi)\right).
\tag{20}
\]
因为
\((Y/b)^p=(Y/b)(1+\xi)^{n_0}\)，(20) 正是 (15) 残数的 \(p\) 次根。
R342 又给 \(\operatorname{Res}_{Q_-}\omega_q=-3h_q\)，故完整 Cartier 恒等式为
\[
\boxed{\mathsf C\omega_q=h_q^{1/p}\,d\log r+\eta(c_q).}
\tag{21}
\]
证明是两侧所有极及残数都相同，差为不变全纯微分，因而为零。

特别
\[
\boxed{
q\longmapsto\mathsf C\omega_q\pmod{k\,d\log r}
\text{ 是 }p^{-1}\text{ 半线性单射，Frobenius twist 后秩为 }K.}
\tag{22}
\]
因为右端落在 \(k\,d\log r\) 会使所有非原点残数为零，再由定理1强迫 \(q=0\)。
这里不能把半线性映射未经 twist 称为 \(k\)-线性。

## 6. 指定中央支与原二阶配对的准确含义

R342 的实际 \(q_n(\lambda,P)\) 由同一个 canonical 来源核向量
\(\bar P\in\ker\beta_1^M\) 和 \(\lambda\in C_2(M)^\vee\) 给出，范围 \(K=s-14\)。
若这个向量非零，则定理1和 (21) 给一个准确、非零的非原点极部，
并有原整数单位 minor (18)。
这不是任意独立测试：其两个接触尾和首 Bockstein 商仍按 R338 保留。

对原中央下一位，R342 的指定向量是
\[
q_n^{\rm cent}
=\frac{[w^{s-n}]\overline{\widehat S_<}}{6n(6n+1)},
\qquad1\le n\le s-1.
\]
因 \([w]\widehat S_<=1\)，它的最后一个系数准确为
\[
\boxed{q_{s-1}^{\rm cent}
=\frac1{6(s-1)(6(s-1)+1)}\ne0.}
\tag{23}
\]
所以这个真实中央测试在某个非原点极上必有非零残数，
其 Cartier 类模 \(k\,d\log r\) 也非零。
即便指定 \(Q_-\) 的中央聚合发生相消，此结论仍成立；
它并不把非原点残数当作中央非零。

后继的准确问题是：
原 \(\bar P,\lambda\) 的来源条件及首 Bockstein 像，
是否强迫 (15) 在某些或全部非原点极消失，
或是否把 (19) 对应为原 \(C_2(M)\) 的一个真正子商。
只有支付这种原 canonical 极界或 Serre 对偶连接，
(18)、(22) 才能控制原剩余像。
总残数相消不能提供该连接；
在 \(Y\mapsto-Y\) 下 \(T_p\) 固定而 \(d\log r\) 变负，原 \(Q_-\) 观察始终须单独保留。

## 固定精确证书

- [check-jzero-off-origin-residue-and-cartier.py](../scripts/check-jzero-off-origin-residue-and-cartier.py)
  及其 JSON：核原微分递推、前三个导数多项式、实际反序整提升、
  明确单位 minor 和 (19) 的完整无穷极消去。
- 所有可变 \(p\) 结论由上述统一次数、整性和局部证明给出；没有目标素数扫描。

依赖：R324 的实际参数整性；R338 的完整二阶商；
R342 的同一原 Gaussian 重标、指定分支残数和全部 \(p\) 依赖零极。


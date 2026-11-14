# R239 附录：出生一实际Riccati、负实根正核及图系数分拆限制

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文全部 Riccati、负实根、正核、微分不等式和最后的有理反例均为自足有限结论。它们尚未证明两个任意大小等权组加一位的完整二维相邻比较；普通 ISP 仍开。沿用已固定的出生一真空系数归约中的同源完整逆。

## 1. 实际有限系数及 Riccati

设 q,L≥1、N=q+L，固定普通秩 1≤j<N，定义

$$Z_j(z)=\sum_r\binom qr\binom L{j-r}z^r,\qquad z>0,$$

其中只取合法 r。记 Θ=z∂_z、m=Θlog Z_j、v=Θm。它们是同一个实际加权 j 元子集中短组占据数的均值、方差。

有限权比准确为

$$\frac{p(r+1)}{p(r)}=\frac{z(q-r)(j-r)}{(r+1)(L-j+r+1)}.$$

在整个合法支持上对两边求和，端部流量为零，故

$$\mathbb E[z(q-r)(j-r)-r(L-j+r)]=0.$$

展开得到真正的 Riccati 身份

$$\boxed{(z-1)(v+m^2)-[z(q+j)+L-j]m+zqj=0.}\tag{1.1}$$

对 z≠1，等价地

$$v=-m^2+a(z)m-b(z),\quad
 a=q+j+\frac N{z-1},\quad b=\frac{zqj}{z-1}.$$

因此

$$\boxed{\Theta v=(a-2m)v-\frac{z(Nm-qj)}{(z-1)^2}.}\tag{1.2}$$

这些是实际多项式路径的微分约束，不是允许各高度独立选择的数值关系。在 z=1 直接从有限超几何分布得到

$$m(1)=qj/N,\qquad v(1)=\frac{qL j(N-j)}{N^2(N-1)}.$$

还可以直接使用相邻系数比。置 ρ_j=Z_(j−1)/Z_j，则此前的真实线性递推和 ΘZ_j 身份给

$$\boxed{\Theta\rho_j=
\frac{z(N-j+1)\rho_j^2+[qz+L-(z+1)j+1]\rho_j-j}{z-1}.}\tag{1.3}$$

在 z=1，ρ_j=j/(N−j+1)。实际高端为

$$\rho_j(z)\sim\frac{j}{q-j+1}z^{-1}\ (j\le q),\qquad
\rho_j(z)\longrightarrow\frac{j-q}{N-j+1}\ (j>q).\tag{1.4}$$

(1.4) 只由 Z_j 的最高非零系数取得，不使用数值拟合。

### 1.1 奇点初值不能被误作唯一性

z=1 是上述 Riccati 的奇点。不能只给 m(1)=qj/N 就宣布唯一选出实际多项式。线性化差的主部为 Θδm≈Nδm/(z−1)，容许高阶消失的非实际分支。

一个可直接核验的例子是 q=L=j=1。Z=1+z 满足

$$z(1-z)Z''+(1+z)Z'-Z=0.$$

同一方程的另一个解是

$$W(z)=(1+z)\log z-2(z-1).$$

W 在 z=1 三阶消失。因此 Z+cW 在 1 附近仍为正，且给相同的 m(1)、v(1)，但 c≠0 时不是真实有限系数多项式。实际全局论证必须保留完整多项式、负实根或高端条件，不能把这个奇点初值当作额外免费唯一性定理。

## 2. 全部非零根为互异负实根：有限 Rolle 证明

令 r_0=max(0,j−L)，d=min(q,L,j,N−j)。我们证明

$$\boxed{Z_j(z)=Cz^{r_0}\prod_{\nu=1}^d(z+\lambda_\nu),
\quad C>0,\quad\lambda_\nu>0\text{ 两两不同}.}\tag{2.1}$$

先取 j≤min(q,L)。对 f(x)=x^q(1−x)^L，Leibniz 公式给

$$\frac1{j!}f^{(j)}(x)=(-1)^j x^q(1-x)^{L-j}
 Z_j\!\left(-\frac{1-x}{x}\right).\tag{2.2}$$

f^(j) 在 0、1 的重数分别为 q−j、L−j。逐次 Rolle 定理给 j 个互异内部零点；次数为 N−j，扣除端部重数后恰剩 j，所以这些内部根均简单且穷尽。变换 z=−(1−x)/x 把 (0,1) 一一送至负实轴，故 Z_j 的 j 个根全为互异负实根。

其余情况用有限二项式恒等式归约。准确有

$$\frac{\binom Nq}{\binom Nj}Z_j^{q,L}(z)=Z_q^{j,N-j}(z),\qquad
 Z_j^{q,L}(z)=z^qZ_{N-j}^{q,L}(z^{-1}).\tag{2.3}$$

第一条逐个 z^r 系数由阶乘相等证明；第二条是取子集补集。可先通过交换两组取 q≤L。当 q<j≤L，第一条把秩改成 q，且 q≤min(j,N−j)，故应用已证情形。当 j>L，第二条把秩改成 N−j<q≤L；它产生准确的强制零根重数 j−L，全部非零根是负实根的倒数。交换两组只作 z 取倒数及乘正单项式。这样证明 (2.1) 的全部范围。

## 3. 沿权参数的完整有限正核

从 (2.1) 删除强制单项式后，定义

$$F_j(s)=\frac{d}{ds}\log[s^{-r_0}Z_j(s)]
=\sum_{\nu=1}^d\frac1{s+\lambda_\nu},\qquad s>0.$$

于是

$$\boxed{\frac{F_j(s)-F_j(t)}{t-s}
=\sum_{\nu=1}^d\frac1{(s+\lambda_\nu)(t+\lambda_\nu)}.}\tag{3.1}$$

对角取连续极限。对任意有限的 s_a>0，(3.1) 构成 Gram 矩阵，故半正定；其秩不超过 d。这是一个真正的正核，来自同一个实际多项式的全部根。

特别，固定 z>0，置

$$p_\nu=\frac z{z+\lambda_\nu}\in(0,1),\qquad
 M_r=\sum_{\nu=1}^d p_\nu^r.$$

则 M_0=d、M_1=m−r_0，且

$$\boxed{M_{r+1}=M_r-\frac1r\Theta M_r\quad(r\ge1).}\tag{3.2}$$

对任意有限阶与 ℓ≥0，所有矩阵

$$[M_{a+b+\ell}]_{a,b}\succeq0,\qquad
 [M_{a+b+\ell}-M_{a+b+\ell+1}]_{a,b}\succeq0\tag{3.3}$$

都分别是节点 p_ν、正权 p_ν^ℓ 及 p_ν^ℓ(1−p_ν) 的 Gram 矩阵。只要矩阵大小≤d，它们严格正；更大阶有准确秩约束。将 (1.1)–(1.2) 递推代入 (3.2)，便把这些全部实际正性条件写成固定位置单比值的有理不等式，而不是独立选择各个形式矩。

### 3.1 两条明确的三阶导数约束

写 ξ=m−r_0。由

$$M_2=\xi-v,\qquad M_3=\xi-\frac32v+\frac12\Theta v,$$

(3.3) 的两个二阶行列式给

$$\boxed{\xi(v+\Theta v)\ge2v^2,\qquad
(d-\xi)(v-\Theta v)\ge2v^2.}\tag{3.4}$$

d≥2 时均严格，因为 p_ν 两两不同；d=1 时均为等号。另一个二阶行列式给

$$\boxed{v\le\xi(1-\xi/d),}\tag{3.5}$$

d≥2 时严格。式 (3.4)–(3.5) 的全部参数、阶数及强制零根都已保留。它们比只要求 m 落在支持区间、v>0 更强。它们沿 z 参数成立；绝不宣称高度序列 H_n 有全 Hankel 正性，也尚未声称这些有限阶必要条件已经充分支付矩阵四次式。

## 4. 三个正图边系数不能分别免费使用标量相邻序

出生一的实际三节点协方差图边为正。相应固定源 Gram 可写成

$$H_n=S_{1,n}\begin{pmatrix}1&1\\1&1\end{pmatrix}
 +S_{0,n}\begin{pmatrix}0&0\\0&1\end{pmatrix}
 +S_{e,n}\begin{pmatrix}1&0\\0&0\end{pmatrix},$$

其中在完整 shear H_n=A_n|α|²+B_n|β+δ_nα|² 的记号下

$$S_{1,n}=B_n\delta_n,\quad S_{0,n}=B_n(1-\delta_n),\quad
S_{e,n}=A_n-B_n\delta_n(1-\delta_n).\tag{4.1}$$

三者都是严格正的真实图系数。确实，把短组—池、单独位—池、短组—单独位的未归一导纳分别记 a,b,c>0，二维协方差为 [[a+c,−c],[−c,b+c]]。先准确求逆并交换源坐标，得到 S_e=K_0wa/(ab+ac+bc)、S_0=K_0wb/(ab+ac+bc)、S_1=K_0wc/(ab+ac+bc)。三条导纳的正性由删去相应两位后的普通 Newton 差给出，且群聚只求正边权之和。它们不分别具有所需标量 log 凸性。

取真实参数 q=2,L=3,z=16,w=1/100；将全部 H_n 除以共同正数 K_0=(q!)²z^q。此时 h=4，整个矩阵的相邻系数一已在仓库的全高度四定理覆盖。对 S_0 的 n=1,2,3，精确值却为

$$\frac{167}{6520672},\quad\frac{16909}{183598176},\quad
\frac{167}{569620},$$

从而

$$\frac{S_{0,2}^2}{S_{0,1}S_{0,3}}
=\frac{8296663252194670655}{7344457079993490888}>1.\tag{4.2}$$

对 S_e 的 n=2,3,4，精确值为

$$\frac{8068091}{2868721500},\quad\frac{2613601}{2278480000},\quad\frac1{25600},$$

所以

$$\frac{S_{e,3}^2}{S_{e,2}S_{e,4}}
=\frac{39191957837185067043}{3272286042388925500}>1.\tag{4.3}$$

这些数直接从 Z_j 的有限和、其均值方差及完整 MP (3.2) 重算。反例只排除把三个正固定 rank-one 项分别当作 log 凸序列的证明；它不是完整 H_n 相邻比较的反例。

后续应在实际单比值 Riccati 路径上保留 (3.1)–(3.3) 的同一个有限正核，并真正把三个四次中间系数或整个矩阵缺陷接到它，而不能以核的存在代替这一步。

## 证明入口与精确核验

沿用[出生一完整真空归约](R239-appendix-birth-one-two-group-singleton-vacuum-reduction.md)的同源完整逆。[独立有理程序](../notes/2026-11-14-birth-one-riccati-negative-root-kernel-check-0c.py)对120组实际有限系数验证Riccati、相邻比、强制根矩、严格微分约束、Hankel/局部化小矩阵，并准确重算两个图系数反例，输出ALL_PASS 120；不把有限核验当尚未证明的一般矩阵比较。

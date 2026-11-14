# R150 附录：四不同半权两块的内部 Gram 配对均非零

日期：2026-11-13（UTC）。作者：normal_resume_2220 / Astra-ISP-1cf8c51d。

状态：**已证明。** 在原非割线均值、本质第三矩维数三、外均值、四个不同支点的完整临界截面中，唯一的 \(2+2\) 半权分割的两块内部配对都非零。此结论独立于尚未完成的三角形 Gram 消去。

## 1. 原归一、中央三次与两个半块

沿用[四不同单点半权排除](R150-appendix-reduced-four-point-single-half-weight-exclusion.md)的原数据：
\[
\lambda(u_i)=1,\qquad
y=\sum_iw_i u_i,\qquad
H=\frac14\sum_iw_i u_i^2,\qquad
V=\frac18\sum_iw_i u_i^3,
\]
\[
w_i\ne0,\qquad w_0+w_1=w_2+w_3=\frac12.
\tag{1.1}
\]
四个 \(u_i\) 是四个不同物理支点的非零代表，彼此线性独立。设
\[
y_+=w_0u_0+w_1u_1,\quad
y_-=w_2u_2+w_3u_3,\quad
u=y_+-y_-,\quad L=u_0-u_1,\quad M=u_2-u_3,
\]
\[
R=w_0w_1,\quad S=w_2w_3,\quad
\delta=w_1-w_0,\quad \epsilon=w_3-w_2.
\]
则 \(R,S\ne0\)，且 \(u,L,M\) 是 \(W=\ker(\lambda|_E)\) 的一组基。第三普通矩的中央表达式直接展开为
\[
T_3=3u(RL^2-SM^2)+2R\delta L^3+2S\epsilon M^3.
\tag{1.2}
\]
这里的对称张量在 \(W^*\) 上取值。用对应坐标 \((\zeta,\ell,m)\)，其不可约普通节点三次曲线写为
\[
C:\ 3\zeta(R\ell^2-Sm^2)+2R\delta\ell^3+2S\epsilon m^3=0.
\tag{1.3}
\]
节点是 \(P=[1:0:0]\)。在原四维对偶空间中，这个方向由
\[
\varepsilon=(1,1,-1,-1)
\]
代表；其在 \(u,L,M\) 上的值分别为 \(1,0,0\)。

记
\[
A=K(y_+,y_+),\qquad B=K(y_-,y_-).
\tag{1.4}
\]
物理曲线的自配对为零，所以
\[
A=2R\,K(u_0,u_1),\qquad B=2S\,K(u_2,u_3).
\tag{1.5}
\]
因此本稿只需证明 \(AB\ne0\)。

## 2. 同一原二次关系上的节点纤维

令原四维物理映射为
\[
\Phi(z)=[K(u_0,v(z)):K(u_1,v(z)):K(u_2,v(z)):K(u_3,v(z))].
\]
此前的外均值、降秩及有基点排除已经证明：

- \(\Phi\) 由四个无公因子的独立五次式给出；
- 原二阶完整梯度给非零二次关系 \(N\)，\(\Phi(\mathbb P^1)\subset\{N=0\}\)；
- 从 \([\lambda]=(1,1,1,1)\) 投影并去掉准确二次公因子后，得到 \(C\) 的双有理参数化 \(\psi:\mathbb P^1\to C\)；
- \(\psi\) 是普通节点三次的归一化，故每个光滑点的原像只有一个。

原四个支点都不是投影中心的原像。因为 \(\Phi(s_i)\) 非零，其第 \(i\) 个坐标为 \(K(u_i,u_i)=0\)，而 \(\lambda(u_i)=1\)。所以在这些点上 \(\psi\) 确实等于从 \(\lambda\) 的普通投影，不需要通过消去公因子解释其值。

节点纤维直线是
\[
\mathfrak l=\mathbb P\operatorname{span}(\lambda,\varepsilon).
\]
从同一原 \(N,H,V,y\) 直接收缩得
\[
N(\lambda,\lambda)=0,\quad
N(\lambda,\varepsilon)=\frac{A-B}{4},\quad
N(\varepsilon,\varepsilon)=\frac{A+B}{2}.
\]
因此
\[
N(c\lambda+d\varepsilon)
=\frac d2\big((A-B)c+(A+B)d\big).
\tag{2.1}
\]
[单点半权排除稿](R150-appendix-reduced-four-point-single-half-weight-exclusion.md)第二节的一般节点纤维引理已经证明 \(\mathfrak l\) 不包含在原二次曲面中。故 (2.1) 立即排除
\[
A=B=0.
\tag{2.2}
\]
该引理保留了节点原像与中心除子相交的所有重数，本稿没有另加横截假设。

## 3. 排除仅一个半块配对为零

反设 \(A=0,\ B\ne0\)。由 (1.5) 得 \(K(u_0,u_1)=0\)。故对 \(i=0,1\)，
\[
K(L,u_i)=K(u_0-u_1,u_i)=0.
\tag{3.1}
\]
也就是说，\(\psi(s_0),\psi(s_1)\) 都位于平面直线 \(\ell=0\)。在该直线上，(1.3) 限制为
\[
S m^2(-3\zeta+2\epsilon m)=0.
\tag{3.2}
\]
其支集只有节点 \(P=[1:0:0]\) 和
\[
P_*=[2\epsilon:0:3].
\]
后者是光滑点：在该点 \(\partial T_3/\partial\zeta=-3Sm^2\ne0\)。允许 \(\epsilon=0\)，所以相同块内权重不构成例外。

先证明 \(\psi(s_0),\psi(s_1)\) 都不能等于节点。若其中一个等于 \(P\)，其原四维像必须位于 \(\mathfrak l\)。由物理自配对及 \(K(u_0,u_1)=0\)，该四维像的前两个坐标都为零；无基点性又保证它非零。因此它必有形式
\[
\Phi(s_i)=[0:0:\rho:\rho],\qquad \rho\ne0.
\]
写成 \(c\lambda+d\varepsilon\) 时，前两坐标为 \(c+d\)，故 \(c=-d\) 且 \(d\ne0\)。但是在 \(A=0\) 下，(2.1) 给出
\[
N(c\lambda+d\varepsilon)=\frac B2d(d-c)=Bd^2\ne0,
\]
与 \(\Phi(s_i)\in\{N=0\}\) 矛盾。故两点都不能映到节点。

结合 (3.2)，只能有
\[
\psi(s_0)=\psi(s_1)=P_*.
\]
四个原支点不同，特别是 \(s_0\ne s_1\)；这违反普通节点三次归一化在光滑点上的单原像性质。于是 \(A=0,\ B\ne0\) 不可能。

交换两个半块，同一证明排除 \(B=0,\ A\ne0\)。该对称情形也可直接在 (2.1) 中检验：四维节点像若为 \([\rho:\rho:0:0]\)，则 \(c=d\ne0\)，从而 \(N=Ad^2\ne0\)。

## 4. 已支付的结论

由 (2.2) 及第三节，
\[
\boxed{AB\ne0,\qquad K(u_0,u_1)\ne0,\qquad K(u_2,u_3)\ne0.}
\]
因此后续对当前四不同余类进行代数消去时，可以合法局部化两个半块内部 Gram 边。这个局部化不排除任何原完整临界点，也不需要假设两块配对彼此不等；\(A=B\ne0\) 的中心相切分支仍在余类中。

本稿只使用此前已证明的原无基点映射、普通节点归一化、原 \(N\) 的纤维限制和明确的中央三次展开，不使用有限域样本、待证的三角形理想归约或正性假设。

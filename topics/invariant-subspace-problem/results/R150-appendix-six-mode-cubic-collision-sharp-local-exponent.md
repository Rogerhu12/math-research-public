# R150 附录：原六模式立方碰撞点的局部三次幂确为最小幂

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明。** 对原平方证明选出的三个真实空谱 first，其匹配立方 Bell 余式在下述点的完整局部梯度理想中，最小归属幂恰为三。证明用一个五维 Artin 商准确杀掉全部十七个梯度，同时保留余式的非零平方。这是局部多项式理想结论，不是实际算子的核、非循环性或全局归属结论。

## 1. 同一完整目标和命题

保留[完整第三矩 Schur 消元](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)的原 $R_3(y,H)$、$B_r(y,H)$、$K$ 和 $J_3$。置
$$
p_0:\quad y_j=1\ (0\le j\le5),\qquad H_m=0\ (0\le m\le10),
$$
$$
\mathcal O=\mathbb C[y_0,\ldots,y_5,H_0,\ldots,H_{10}]_{\mathfrak m_{p_0}},
\qquad I=(\nabla R_3)\mathcal O.
$$
[已证局部三次归属](R150-appendix-six-mode-cubic-local-jacobian-cube.md)给每个 $r\in\mathbb C^6$ 的 $B_r^3\in I$。

本稿证明：对 $r=e_0$，以及[原平方稿](R150-appendix-six-mode-exact-jacobian-jets-and-all-square-fibers.md)的三个方向
$$
r=(A,B,0,0,0,1),\qquad
A=-\frac{521d^2-46784d+271360}{160(5d-704)},\quad B=A+d,
\tag{1.1}
$$
其中 $d$ 分别为
$$
f(d)=3725d^3-43931504d^2+6080833024d+52565262336
\tag{1.2}
$$
的三个原实根，准确有
$$
\boxed{B_r^2\notin I,\qquad B_r^3\in I.}
\tag{1.3}
$$
若 $B_r\in I$，其平方也会属于 $I$，所以 (1.3) 确定了最小正整数幂。

## 2. 杀掉全部梯度的有限代数商

取
$$
\mathcal A=\mathbb Q[\varepsilon]/(\varepsilon^5).
$$
以下所有递推都在这个五维代数内准确进行；不存在未控制的无限余项。

先取[完整临界有理图](R150-appendix-finite-atomic-ordinary-moment-critical-families.md)的切片
$$
(\gamma,m,h,k)=(1,1,0,\varepsilon),
\quad S=2-4\varepsilon,\quad P=1-4\varepsilon+8\varepsilon^2.
$$
以初值
$$
Y_0=Y_1=1,\qquad \mathsf H_0=0,\quad\mathsf H_1=\varepsilon
$$
和共同递推 $u_{j+2}=S u_{j+1}-P u_j$，生成 $Y_0,\ldots,Y_5$ 与 $\mathsf H_0,\ldots,\mathsf H_{10}$。记这张准确图在 $\mathcal A$ 中的坐标列为 $X^{\rm graph}$。

置明确非零有理数
$$
\theta=
\frac{11724705008711537212210669677396027690777}
{4503720621100410677799641360100057447392}.
\tag{2.1}
$$
把 $y_2$ 改为 $Y_2+\theta\varepsilon^2$，其余坐标暂时不变。原变量顺序仍是 $(y_0,\ldots,y_5,H_0,\ldots,H_{10})$。令
$$
W=\{3,4,5,8,9,10,11,12,13,14,15,16\},\qquad
M=(\nabla^2R_3(p_0))_{W,W}.
$$
前稿已付 $\det M\ne0$，且 $\det M\equiv70\pmod{103}$。

对 $j=2,3,4$ 依次执行以下有限步骤。若当前列为 $X$，计算
$$
b_j=-[\varepsilon^j](\partial_WR_3)(X),\qquad
z_j=M^{-1}b_j,
\tag{2.2}
$$
并对 $i\in W$ 将 $X_i$ 增加 $(z_j)_i\varepsilon^j$。此操作不改变此前次数小于 $j$ 的系数，并准确消掉十二个所选梯度的第 $j$ 次系数。最后得到列 $X(\varepsilon)$。

对这个由 (2.1)–(2.2) 完全确定的列，准确恒等式为
$$
\boxed{
R_3(X(\varepsilon))=0,\qquad
(\partial_iR_3)(X(\varepsilon))=0
\quad(0\le i\le16)
\quad\text{在 }\mathcal A\text{ 中}.
}
\tag{2.3}
$$
特别，(2.3) 包括未在 (2.2) 中直接消去的五个梯度；没有用选出的十二行代替全部方程。

这是一个有限有理证书。[自含验证器](../notes/2026-11-13-six-mode-cubic-collision-sharp-cube-verify.py)从原完整 $R_3$ 公式和已发表 $J_3^{-1}$ 出发，构造真实 $M$，执行三次十二阶有理消元，然后准确验证全部十七个梯度及目标值为零。[完整证书数据](../notes/2026-11-13-six-mode-cubic-collision-sharp-cube-verification.json)列出三个 $z_j$、全部十七个坐标的五项系数及下文的匹配余式数据。所有运算使用 `Fraction`；截断只因目标环本身有关系 $\varepsilon^5=0$，不是近似误差。

因为 $X(0)=p_0$，任何在 $p_0$ 非零的多项式代入 $X$ 后都是 $\mathcal A\otimes_{\mathbb Q}\mathbb C$ 中的单位。因此代入准确延伸为局部环同态
$$
\varphi:\mathcal O\longrightarrow\mathbb C[\varepsilon]/(\varepsilon^5),
\qquad \varphi(I)=0.
\tag{2.4}
$$

## 3. 一个明确匹配余式的平方仍非零

对 $r=e_0$，有
$$
B_{e_0}=y_0^3-6y_0H_0-(J_3^{-1}\ell)_0.
$$
准确代入给
$$
[\varepsilon^0]\varphi(B_{e_0})=
[\varepsilon^1]\varphi(B_{e_0})=0,
$$
$$
[\varepsilon^2]\varphi(B_{e_0})=
\theta\frac{249584547}{496533016}
=\frac{47147804379765958101497006756940790592697}
{36029764968803285422397130880800459579136}\ne0.
\tag{3.1}
$$
在 $\mathbb C[\varepsilon]/(\varepsilon^5)$ 中，平方恰有非零的 $\varepsilon^4$ 系数，即 (3.1) 的平方。因此 $B_{e_0}^2\notin I$。

## 4. 三个原真实 first 均保留同一非零平方

令 $v$ 为前稿给出的完整 Hessian 零方向：固定四个图参数，$v_{y_2}=1$，并由
$$
M v_W=-(\nabla^2R_3(p_0))_{W,y_2}
$$
确定其余十二项。定义余式沿此方向的一次系数
$$
L_r=\left.\frac{d}{dt}B_r(p_0+t v)\right|_{t=0}.
\tag{4.1}
$$
整个 $B_r$ 在完整临界图上恒零；(2.2) 的首个修正说明 $X-X^{\rm graph}=\theta\varepsilon^2v+O(\varepsilon^3)$。因此
$$
\boxed{\varphi(B_r)=\theta L_r\varepsilon^2+O(\varepsilon^3).}
\tag{4.2}
$$
这里的 $O(\varepsilon^3)$ 只是有限商中三、四次项的简记。

还需核对 (1.1) 的三个 $L_r$ 都非零。置
$$
N(d)=-(521d^2-46784d+271360),\qquad L(d)=160(5d-704),
$$
所以 $A=N/L$、$B=(N+dL)/L$。清去 (4.1) 中的 $L(d)^3$，再对原三次式 $f(d)$ 取余，得到次数至多二的有理多项式 $C(d)$。完整有理余式列于证书数据中。小的可复算非零证书为
$$
\overline f(d)=80+85d+56d^2+17d^3,\qquad
\overline C(d)=45+5d+71d^2
\quad\text{在 }\mathbb F_{103}[d]\text{ 中},
$$
$$
\boxed{\operatorname{Res}_{d}(\overline f,\overline C)=14\ne0.}
\tag{4.3}
$$
全部有理分母在模 $103$ 下为单位；验证器同时在 $\mathbb Q[d]$ 中直接执行 Euclidean 算法，给
$$
\gcd(f,C)=1,\qquad\gcd(f,L)=1.
$$
因此 $f$ 的每个根都有 $L_r\ne0$，特别包括三个原真实空谱方向。由 (4.2)，其余式平方的 $\varepsilon^4$ 系数为 $\theta^2L_r^2\ne0$。结合 (2.4)，三者的 $B_r^2$ 都不属于完整局部梯度理想。再与已证 $B_r^3\in I$ 合并即得 (1.3)。

## 5. 精确范围

本稿证明的是指定碰撞点的局部幂次下界和最小幂，不将有限 Artin 商解释为实际联合谱或正常见证。它同时排除这些方向的全局一次或二次 Jacobian 归属，因为全局归属会在局部化后继续成立。

本稿没有证明三次幂在全局归属；别的临界点可能要求更高幂。原完整临界集的其余分支、全局可用的 Bell 自然幂证书、$F^3$ 零参数循环性和普通 ISP 仍须继续处理。

# R155：空谱锚与任意有界辅助模式的点态多项式

日期：2026-11-12。作者：l2_moments。
状态：完整证明，根代理与 literature 已全文审读通过。
本正文在执行器失效后重建；已补明常数多项式 $q$ 的单独分支。

本稿不要求辅助模式有快尾，也不要求首位次序或有限支撑交集。
关键条件是关于空谱锚的最高次点态系数在实际0锚处非零，
从而其倾斜后的真实有界系数为单位。

## 1. 主定理

设
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,
$$
其 R125 闭第一阶乘子 $X=X_u$ 为空谱。
由 R134/R138，一个明确且精确的非有界情形条件是
$a\notin\ell^1$，且存在 $\theta$ 使
$$
\sum_j\left(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\right)<\infty.
\tag{1.1}
$$
任意常数 $a_*$ 和共同相位均允许。

另取有限个有界辅助第一模式
$$
v_\nu=c_{\nu,*}+\sum_jc_{\nu j}\chi_j,\qquad
c_{\nu\cdot}\in\ell^1,\qquad 1\le\nu\le d.
\tag{1.2}
$$
它们可以任意慢、任意相位、完全重叠。记
$$
\beta_\nu=v_\nu(0)=c_{\nu,*}+\sum_jc_{\nu j},\qquad
Z_\nu=X_{v_\nu}\in\mathcal A.
\tag{1.3}
$$
其中 $0$ 指全部物理位为0，即全部 $\chi_j=1$。

再取任意复 $\ell^2$ 指数方向
$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
\tag{1.4}
$$
给定标量多项式
$$
F(U,V_1,\ldots,V_d)=\sum_{i=0}^pU^ir_i(V_1,\ldots,V_d),
\qquad p\ge1,
\tag{1.5}
$$
假设
$$
\boxed{r_p(\beta_1,\ldots,\beta_d)\ne0.}
\tag{1.6}
$$

**定理1.1。** 对全部 $\lambda\in\mathbb C$，
$$
\boxed{
(F(u,v_1,\ldots,v_d)-\lambda)e^w
\text{ 对实际 }A\text{ 循环}.
}
\tag{1.7}
$$
目标向量自动非零。不存在首位排序、矩形角、平移互素、
辅助系数快尾或支撑不交条件。

特别地，对任意 $p\ge1$ 及任意辅助模式多项式 $r_0,\ldots,r_{p-1}$，
$$
\left[u^p+\sum_{i<p}u^ir_i(v_1,\ldots,v_d)-\lambda\right]e^w
$$
对全部 $\lambda$ 循环。

另一个直接推论是：若 $v$ 为 $\ell^1$ 第一模式且 $v(0)\ne0$，
则任意非零标量多项式 $q$ 都满足
$$
q(u)v e^w\text{ 循环}.
\tag{1.8}
$$
当 $\deg q\ge1$ 时由主定理取最高系数为非零常数乘 $V$；
当 $q$ 为非零常数时，使用 R147 已证的 $v e^w$ 循环性，
若 $v$ 自身为非零常数则直接使用 $e^w$ 循环性。
因此没有把 $p=0$ 偷渡进 (1.5)。

## 2. 空谱锚、共同域及指数基

R125 给 $X$ 闭且 $C$ 自伴，有限柱为图核心，
并且每个有界 $A$ 交换子保持 $\operatorname{Dom}X$ 且与 $X$ 交换。
归纳可知这些交换子保持每个自然幂域 $\operatorname{Dom}X^k$。

由于 $X$ 空谱，其逆
$$
R=X^{-1}\in\{A\}'
\tag{2.1}
$$
在全空间有界。
R134 给 $R$ 拟幂零；也可直接证明：
对每个 $\lambda$，$X-\lambda$ 有有界逆，
所以 $I-\lambda R=(X-\lambda)R$ 为有界单位，
从而 $\sigma(R)=\{0\}$。
所有有界交换子互相交换，这是 R88 的全交换子强闭包结论。

反复使用真实逆关系得到
$$
\boxed{\operatorname{Dom}X^k=\operatorname{Ran}R^k,\qquad
X^k=(R^k)^{-1}.}
\tag{2.2}
$$
特别地，$X^k$ 闭、单射、满射。
这里的闭性来自有界单射 $R^k$ 的闭逆图，
没有对任意闭算子自然幂作一般性假设。

定义
$$
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z),
\qquad V_j=(I-N_j)(I+N_j)^{-1}.
$$
由 R145 的有限多模式 Bell 定理，
$$
\mathcal B(t,s)=
\prod_j H\!\left(
b_j+ta_j+\sum_{\nu=1}^ds_\nu c_{\nu j},V_j
\right)
\tag{2.3}
$$
是范数整单位函数，字符恒为1。
置
$$
B_w=\mathcal B(0,0),\qquad
\widetilde B(t,s)=\mathcal B(t,s)B_w^{-1},\qquad
\xi_w=B_w^{-1}e^w.
\tag{2.4}
$$
R16/R147 给 $e^w\in H$ 且循环，所以 $\xi_w$ 也循环。

R145 的真实混合幂域结论还给
$$
\xi_w\in\bigcap_{k\ge0}\operatorname{Dom}X^k.
\tag{2.5}
$$
可从规范联合整真空轨道在指数参数 $(0,\ldots,0,1)$ 的导数得到此式。
每个辅助 $Z_\nu$ 有界并属于 $\mathcal A$，故它及任意有界辅助 Bell 系数
都保持所有这些幂域，与每个 $X^k$ 在自然域上交换。

## 3. 真实倾斜 Bell 多项式

记
$$
C_{k,\alpha}
=\partial_t^k\partial_s^\alpha\widetilde B(0,0),
\qquad k\ge0,\quad\alpha\in\mathbb N^d.
\tag{3.1}
$$
这些都是 $\mathcal A$ 的有界元素，且
$$
C_{0,0}=I,\qquad
\chi(C_{k,\alpha})=0\quad\text{若 }k+|\alpha|>0.
\tag{3.2}
$$
此处不要求它们属于快尾代数 $\mathcal G$。

有限位生成恒等式以及 R145 的真实混合域，给
$$
e^{tu+\sum_\nu s_\nu v_\nu+w}
=
B_w\widetilde B(t,s)\,
\mathcal V(t,s),
\tag{3.3}
$$
其中 $\mathcal V(0,0)=\xi_w$，且在零点的全部混合导数为
$$
\partial_t^k\partial_s^\alpha\mathcal V(0,0)
=X^kZ_1^{\alpha_1}\cdots Z_d^{\alpha_d}\xi_w.
\tag{3.4}
$$
这条等式涉及已证明存在的自然幂域；
不把 $e^{tX}$ 当作一个无条件有界的全空间指数群。

(3.3) 也可先对所有模式作有限位截断验证。
辅助 $v_\nu$ 在一致函数范数收敛，$Z_\nu$ 在算子范数收敛；
一般 $u,w$ 的混合 Rademacher 矩和 Bell 整函数极限由 R145 控制。
先得到混合导数强极限，再用 $X^*$ 的有限柱图核心识别幂域，
正是 R145 的已证域步骤，而非从 $X_N1\to u$ 自动推出高次幂收敛。

对 (3.3) 施加 $F(\partial_t,\partial_s)$，得到
$$
\boxed{
F(u,v_1,\ldots,v_d)e^w=B_wP_F(X)\xi_w,
}
\tag{3.5}
$$
其中实际有限 Bell 多项式为
$$
P_F(X)
=
\sum_{k,\alpha}
\frac{C_{k,\alpha}}{k!\alpha!}
(\partial_U^k\partial_V^\alpha F)(X,Z_1,\ldots,Z_d).
\tag{3.6}
$$
和有限，所有有界系数与 $X$ 的全部幂域交换。
因此 (3.6) 在自然域 $\operatorname{Dom}X^p$ 上定义良好。

## 4. 最高实际系数及其非零字符

将 (3.6) 按 $X$ 次数整理为
$$
P_F(X)=L X^p+\sum_{i<p}D_iX^i,
\qquad L,D_i\in\mathcal A.
\tag{4.1}
$$
最高 $X^p$ 项只能来自 $k=0$ 和 (1.5) 的最高 $U^p$ 项。
所以
$$
\boxed{
L=\sum_{\alpha\ge0}
\frac{C_{0,\alpha}}{\alpha!}
(\partial^\alpha r_p)(Z_1,\ldots,Z_d).
}
\tag{4.2}
$$
这是有限和。
由 (3.2) 和 $\chi(Z_\nu)=\beta_\nu$，
$$
\boxed{\chi(L)=r_p(\beta_1,\ldots,\beta_d)\ne0.}
\tag{4.3}
$$
$\mathcal A$ 的唯一字符性质使 $L$ 成为实际有界单位。
因此能对 (4.1) 真正首一化，而不是仅对形式首项作除法。

注意最高系数一般不只是 $r_p(Z)$；
它包含真实辅助模式倾斜与 Bell 修正。
(4.2)—(4.3) 验证的是整个修正后的系数，故没有遗漏重叠位贡献。

## 5. 自然域上的完整有界逆

令 $E_i=L^{-1}D_i$，并定义
$$
U=I+\sum_{i<p}E_iR^{p-i}.
\tag{5.1}
$$
所有因子是有界交换子并互相交换。
有 $U-I=RK$，其中 $K$ 有界且与 $R$ 交换。
所以
$$
\|(RK)^n\|^{1/n}\le\|R^n\|^{1/n}\|K\|\to0.
$$
$U$ 是有界交换单位，逆也与 $A$ 交换。

在准确的自然域 $\operatorname{Dom}X^p=\operatorname{Ran}R^p$ 上，
$$
\boxed{
P_F(X)=LU X^p,\qquad
J_F:=P_F(X)^{-1}=R^pU^{-1}L^{-1}\in\{A\}'.
}
\tag{5.2}
$$
逐项校验使用 $R^{p-i}X^p=X^i$ 于该域。
有界可逆的 $LU$ 乘闭算子 $X^p$ 仍闭，
故 $P_F(X)$ 在自然域上已经是闭算子。
其逆 $J_F$ 定义于整个 $H$ 且有界。

减去任意标量只改变 (4.1) 的常数系数；
最高单位 $L$ 和上述机制完全保留。
所以
$$
\sigma(P_F(X))=\varnothing.
\tag{5.3}
$$
这里是实际闭算子的空谱结论，不只是形式逆级数。

### 5.1 每个不变限制上的准确加强

设 $M$ 为闭 $A$ 不变空间。
R128 给 $\operatorname{Dom}X\cap M$ 在 $M$ 中稠密，且 $X$ 将此域映入 $M$。
R88 又使全部有界交换子，包括 $R$ 和 (5.2) 中的单位逆，都保持 $M$。
因为 $XR=I$，有
$$
R M=\operatorname{Dom}X\cap M,
$$
从而 $RM$ 稠密于 $M$，其有限幂也有稠密像。

逐级使用域与像保持可得
$$
\boxed{\operatorname{Dom}X^p\cap M=R^pM.}
\tag{5.4}
$$
例如若 $x\in\operatorname{Dom}X^p\cap M$，
则 $Xx,\ldots,X^px$ 全在 $M$，故 $x=R^p(X^px)$；
反向由 $R$ 保持 $M$ 直接成立。

因此每个 $P_F(X)-\lambda$ 的限制在稠密域 $R^pM$ 上单射、满射到 $M$，
其逆就是相应有界全局逆在 $M$ 上的限制。
这来自实际逆因式和 R128 的域保持，
并非把全空间稠密像直接下放到一个未知限制。

## 6. 循环性传回点态向量

由 (3.5)、(5.2)，
$$
\boxed{
\xi_w=J_FB_w^{-1}\,[F(u,v_1,\ldots,v_d)e^w].
}
\tag{6.1}
$$
右边左乘的是有界 $A$ 交换子，所以它保持目标向量的闭循环空间。
该循环空间因此包含循环向量 $\xi_w$，必为全 $H$。
目标向量也自动非零，否则 (6.1) 将给 $\xi_w=0$。

用 $F-\lambda$ 重复同一证明即可。
因为 $p\ge1$，减去 $\lambda$ 不改变 $r_p$ 和 (1.6)，
从而得到 (1.7) 的全部参数结论。

全部向量确实属于 $H$：
辅助 $v_\nu$ 有界，$u$ 有任意有限 Rademacher 矩，
$e^w$ 有所需有限指数矩；Hölder 不等式控制多项式乘指数。
上述真实 Bell 域论证进一步识别了相应实际算子表达式。

## 7. 无首位及矩形角限制的例子

取
$$
u=\sum_{j\ge0}\frac{\chi_j}{j+1},\qquad
v=\sum_{j\ge7}\frac{(-1)^j}{(j+1)^2}\chi_j.
$$
第一个系数列正、属于 $\ell^2\setminus\ell^1$，所以 $X_u$ 空谱。
第二个模式任意慢且有界，首位高于 $u$，并与 $u$ 有无限支撑交集。
取
$$
F(U,V)=U^2+(V^5+2)U+V^9-3.
\tag{7.1}
$$
其最高 $U$ 系数恒为1，所以对任意复 $\ell^2$ 第一阶 $w$ 与任意 $\lambda$，
$$
\boxed{[u^2+(v^5+2)u+v^9-3-\lambda]e^w\text{ 循环}.}
\tag{7.2}
$$
这里 $U^2V^9$ 的矩形角系数为零；
本证明不要求 R150 的矩形角，也不要求 R149 的首位顺序或有限交集支路。

## 8. 边界

最高锚条件 (1.6) 的作用是得到 (4.3) 的真实单位。
若 $r_p(\beta)=0$，不能按同一式子对 $L$ 作有界除法。
本稿不据此判定目标向量有核，而是保持该分支未解决。

辅助模式的 $\ell^1$ 假设提供有界 $Z_\nu$ 与全部幂域交换；
本稿不把一般无界辅助方向的高次乘法域自动纳入。
任意 $H$ 端点、一般慢共振和完整 Hilbert ISP 仍开放。

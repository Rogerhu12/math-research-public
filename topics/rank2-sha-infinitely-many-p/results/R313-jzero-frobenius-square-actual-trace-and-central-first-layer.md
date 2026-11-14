# R313：实际 Frobenius 平方同源迹、固定极族与原中央首层

日期：2026-11-13。**状态：以下正密度惰性族、原二十四极微分的完整 $[-p]$ 同源迹、真实 $H_3$ 乘子、全部 Newton 进位及模 $p^2$ 的原中央运输均已证明。迭代的极点准确趋于其原约化的 $(p+1)$ 挠点提升。本文没有把这一运输后的中央行宣布为非零。**

R310 的第三类微分具有固定代数极点。将其 Cartier 平方的全纯缺陷直接看成中央导数，会丢掉真实 theta 乘子。本篇使用实际有限同源 $[-p]$，在特征零写出全部移动极和代数常数，然后进入原来的同一个 $H_3$ 参考商。

## 1. 原微分与一族真正非空的惰性素数

沿 R310 固定
$$
E_b:y^2=x^3+b,\qquad b=17,\qquad dz=\frac{dx}{2y},
\qquad X=x^3,
$$
$$
\begin{aligned}
C_3(X)&=X^3-204bX^2-384b^2X+64b^3,\\
D(X)&=(X+4b)C_3(X),\\
N(X)&=(X+b)(7X^2-4bX+16b^2)/7,\\
g&=N(X)/D(X),\qquad \eta=g\,dz,\\
H&=\sigma^{34}x^2(X-8b)(X+4b)C_3(X),\qquad S=Hg.
\end{aligned}                                                    \tag{1}
$$
这里 $H=H_3$、$S$ 都是 R306–308 识别过的原来源；$H(0)=1$，$S=z^6+\cdots$。本文不改变它们的 period、Schwartz 向量或 Gaussian。

对 $D$ 的四个根 $r$，写
$$
A_r=\frac{N(r)}{D'(r)},\quad
a^3=r,\quad y_r^2=r+b,\quad
P_a=(a,y_r),\quad \varrho_a=\frac{A_r}{6a^2y_r}.
$$
每个 $r$ 取三个 $a$ 和一个 $y_r$，共十二个 $P_a$；其负点给另外十二极。R310 的准确分解是
$$
\eta=\sum_a\varrho_a\xi_{P_a},\qquad
\xi_P=\frac{2y(P)}{x-x(P)}\,dz.                            \tag{2}
$$
$\xi_P$ 的留数在 $P,-P$ 分别为 $1,-1$，并且在 $O$ 的系数为零。换掉某个 $y_r$ 的符号不会改变 (2)。

令 $L/\mathbb Q$ 为这二十四极坐标的 Galois 闭包，并加入 $\mu_3$。选定一个复共轭 $c\in\operatorname{Gal}(L/\mathbb Q)$。它满足
$$
c^2=1,\qquad c|_{\mathbb Q(\mu_3)}\ne1.
$$
Chebotarev 对实际共轭类 $[c]$ 给出一个正 Dirichlet 密度的素数集合 $\mathcal P$。删去有限个坏素数及 $p\le7$，对每个 $p\in\mathcal P$，
$$
\boxed{
p\equiv5\pmod6,\qquad
\text{全部二十四极及其留数均在未分歧二次扩张中，约化在 }\mathbb F_{p^2}.}
                                                                    \tag{3}
$$
这里 Frobenius 的阶至多二，所以每个对应完备域的剩余次数至多二；不是先假设一个所需的有限 Galois 类非空。

可将有限坏集合取为包含 $2,3,7,17,107$ 以及 $L$ 的分歧素数的集合。下列原多项式恒等式保证再删去这些有限素数后，所有极互异、非零、不是二挠点，且留数为单位：
$$
\begin{aligned}
\operatorname{disc}_X D&=2^{24}3^{15}\cdot107\,b^{12},\\
\operatorname{Res}_X(D,7N)&=2^{16}3^{18}b^{12},\\
D(0)&=256b^4,\qquad D(-b)=729b^4.
\end{aligned}                                                       \tag{4}
$$
以下总在这一族中；可统一嵌入 $K_p=\mathbb Q_{p^2}$，其整数环记 $\mathcal O_p$。

## 2. Cartier 平方的完整有限极关系

用 $\mathcal C(a^p\omega)=a\mathcal C(\omega)$ 的规范。若微分在点 $P$ 有简单极和留数 $r$，$\mathcal C^2$ 在同一点保简单极，并把留数换成 $r^{1/p^2}$。由 (3)，这个留数仍是 $r$。故两微分之差处处全纯，存在唯一 $a_p\in\mathbb F_{p^2}$ 使
$$
\boxed{\mathcal C^2\bar\eta=\bar\eta+a_p\,d\bar z.}       \tag{5}
$$
事实上 (1) 在 $\mathbb Q$ 上，所以 $a_p\in\mathbb F_p$。

$E_b$ 在这些素数处超奇异。也可以直接计算：在 $\mathcal C(dz)$ 中只可能出现 $(x^3+b)^{(p-1)/2}$ 的 $x^{p-1}$ 系数，而 $3\nmid p-1$。于是
$$
\mathcal C(d\bar z)=0,\qquad
\mathcal C^2(\mathcal C^2\bar\eta)=\mathcal C^2\bar\eta.      \tag{6}
$$
这说明 (5) 选出一个实际 Cartier 平方固定的代表，并不赋予 $a_p$ 非零性。

在 $O$ 用原整参数 $t=x^{-1/2}$，取 $t=z+\cdots$。准确有
$$
dz=(1+bt^6)^{-1/2}dt,\quad
g=t^6\frac{(1+bt^6)(7-4bt^6+16b^2t^{12})}
 {7(1+4bt^6)(1-204bt^6-384b^2t^{12}+64b^3t^{18})}.
$$
局部 Cartier 公式给出一个完整有限系数证书：
$$
\boxed{a_p=[t^{p^2-1}]\bigl(g(t)(1+bt^6)^{-1/2}\bigr)\pmod p.}       \tag{7}
$$
这个高位系数不是原 $s_{p+1}$。将 (5) 运回原观察还需要以下特征零同源及 theta 乘子。

## 3. 任意奇数乘法的准确第三类迹

记 $[n]_*$ 为有限同源对一形式的实际迹。在加法坐标中，
$$
[n]_*(f\,dz)(z)=\frac1n
          \sum_{T\in E[n]}f(z/n+T)\,dz.                  \tag{8}
$$
这与 $[n]_*dz=n\,dz$ 相容。选择不同周期提升不影响椭圆函数的和。

令 $\psi_n$ 为原奇数除法多项式；对 $P\notin E[n]$，且 $[n]P\ne-[n]P$，有
$$
\boxed{
[n]_*\xi_P
=\xi_{[n]P}-\frac2n\frac{\partial_z\psi_n}{\psi_n}(P)\,dz.}          \tag{9}
$$
这里除法多项式的任意非零常数规范都给同一对数导数。

**完整代数证明。** 令
$$
x([n]Q)=R_n(x(Q))=\frac{N_n(x(Q))}{\psi_n(x(Q))^2}.
$$
由原微分的乘法关系，$y([n]Q)=y(Q)R_n'(x(Q))/n$。固定一般目标点的横坐标 $v$；其 $n^2$ 个原像的横坐标是
$F_v(T)=N_n(T)-v\psi_n(T)^2$ 的根。若 $a=x(P)$，则
$$
\sum_{F_v(t)=0}\frac1{t-a}=-\frac{F_v'(a)}{F_v(a)}.
$$
因此 (8) 左边的系数准确为
$$
-\frac{2y(P)}n\frac{F_v'(a)}{F_v(a)}
=\frac{2y(P)R_n'(a)}{n(v-R_n(a))}
 -\frac{4y(P)}n\frac{\psi_n'(a)}{\psi_n(a)}.
$$
第一项是 $\xi_{[n]P}/dz$，第二项是 (9) 的常数，因为 $\partial_z=2y\partial_x$。一般点上的恒等式延拓为全局微分恒等式。这同时支付全部 $n^2$ 个原像；没有只取一个循环或一个部分 trace。

若用 R310 的 $\zeta$ 写法，(9) 等价于
$$
[n]_*\xi_P=\xi_{[n]P}+2\bigl(n\zeta(P)-\zeta(nP)\bigr)dz.
$$
本篇使用 (9) 的代数规范，不把其中任一个准对数常数单独当作新中央值。

## 4. 真实 $[-p]$ lift 和全部移动极

对 $p\in\mathcal P$，设 $\phi=[-p]$。由于 $a_p(E_b)=0$，其约化满足
$$
\bar\phi=\operatorname{Frob}_p^2.
$$
这是一条实际次数 $p^2$ 的有限平坦同源，不是形式上选定的 Frobenius 矩阵。

定义
$$
\begin{aligned}
P_a^{(1)}&=[-p]P_a,\\
g_1(z)&=\sum_a\varrho_a
       \frac{2y(P_a^{(1)})}{x(z)-x(P_a^{(1)})},\\
A_p&=\frac2p\sum_a\varrho_a
                    \frac{\partial_z\psi_p}{\psi_p}(P_a).
\end{aligned}                                                       \tag{10}
$$
原六个三挠点不会落入 $E[p]$，其余十八点由 R310 已证非挠，故这里所有除法分母非零。(9) 给
$$
\boxed{\phi_*\eta=(g_1+A_p)\,dz.}                         \tag{11}
$$
在 $O$ 取值还给出同一常数的完整 $p$ 挠点表达
$$
\boxed{A_p=-\frac1p\sum_{T\in E[p]}g(T).}                 \tag{12}
$$
$g(O)=0$，所以包含 $T=O$ 不带额外项。

这个常数虽然用 $1/p$ 写出，却是 $p$ 整的，而且
$$
\boxed{A_p\bmod p=a_p.}                                  \tag{13}
$$
下面说明其整性和准确 Cartier 规范，不能只从 (12) 的项数猜测。

有限平坦同源在相对对偶微分上的迹是整的；其一般纤维就是 (8)。此处可以在原正式参数中直接核定：写目标参数为 $t=F(u)$，其中 $F(u)\equiv u^{p^2}\pmod p$。用 $F(u)-t$ 的首一 Weierstrass 方程表示有限自由代数，其微分迹在一般纤维为
$$
f(u)du\longmapsto\operatorname{Tr}\bigl(f(u)/F'(u)\bigr)dt.
$$
首一多项式的对偶基恒等式
$\operatorname{Tr}(u^{q-1}/W'(u))=1$、
$\operatorname{Tr}(u^j/W'(u))=0$（$0\le j<q-1$）
证明此映射整。取 $q=p^2$ 后，其约化为
$$
u^{qk+q-1}du\longmapsto t^kdt,\qquad
u^jdu\longmapsto0\quad(j\not\equiv q-1\bmod q),
$$
恰是 $\mathcal C^2$。该证明同样适用于不含极的整邻域。所有移动极的约化由 (3) 仍是原互异极，故在 $O$ 可应用此整迹。

于是 (11) 的左边在 $O$ 整，$g_1(O)=0$，给 $A_p\in\mathbb Z_p$。其模 $p$ 的微分是 (5)，且 $g_1\equiv g\pmod p$，从而得到 (13)。

## 5. 四个真实 CM 轨道及整局部误差

全部十二正极的和仍可压成四个真实项，不丢角色权。对每个原 $r$ 选一个 $P=(a,y)$，并置
$$
a_1=x([-p]P),\qquad y_1=y([-p]P),\qquad
r_1=a_1^3,\qquad B_{r,1}=A_r\frac{a_1^2y_1}{a^2y}.
$$
$[-p]$ 与 $[\omega]$ 对易，而 $\varrho_{[\omega]P}=\omega\varrho_P$。直接相加三个分式得
$$
\boxed{
g_1(X)=\sum_{D(r)=0}\frac{B_{r,1}}{X-r_1},\qquad
g_1(t)=\sum_{D(r)=0}\frac{B_{r,1}t^6}{1-r_1t^6}.}         \tag{14}
$$
没有把原留数重新换成 $H$ 在新点的留数。

由 $\bar\phi=\operatorname{Frob}_p^2$ 及 (3)，
$$
[-p]P_a\equiv P_a\pmod p.
$$
所以 $r_1\equiv r$、$B_{r,1}\equiv A_r\pmod p$，这些量全部整，且原分母常数项为一。因此
$$
\boxed{g_1-g\in p\,t^6\mathcal O_p[[t^6]].}              \tag{15}
$$
这是实际移动极的完整形式级数同余，不是单个有限样本。

更高系数可由四个实际极显式获得。若
$$
z=t\,\mathscr L_b(t^6),\qquad
\mathscr L_b(T)=\sum_{j\ge0}
\frac{(-1)^j\binom{2j}{j}b^j}{4^j(6j+1)}T^j,
$$
则 $v_j=[z^{6j}]g_1(z)$ 对每个 $j\ge1$ 准确为
$$
\boxed{
v_j=\frac1j[T^{j-1}]
\left(\sum_{D(r)=0}\frac{B_{r,1}}{(1-r_1T)^2}\right)
                         \mathscr L_b(T)^{-6j}.}          \tag{16}
$$
这是 Lagrange 反演，保留了原加法坐标转换及其全部分母。

## 6. 同一个 $H_3$ 的完整同源运输

对一个同 frame 的来源 $T=Hf$，定义实际有限迹算子
$$
\boxed{
\mathscr T_{p,H}T(z)
=-\frac{H(z)}p\sum_{R\in E[p]}
               \frac{T(-z/p+R)}{H(-z/p+R)}.}             \tag{17}
$$
每个商按同一原 theta 平凡化取值。$T/H=f$ 是椭圆函数，所以改变某个周期提升时，两个 theta 因子及其 Gaussian、半特征完全相消。外面的原 $H(z)$ 仍保留。故 (17) 是 $H\phi_*(f\,dz)/dz$ 的实际表达，绝不省成一个无乘子的来源迹。

特别
$$
\mathscr T_{p,H}H=-pH,\qquad
\boxed{\mathscr T_{p,H}S=Hg_1+A_pH.}                      \tag{18}
$$
在特征零中，$Hg_1$ 一般不是全局全纯 theta 截面：$H$ 的零在原 $P_a$，而新微分的极在 $[-p]P_a$。以下仅把它作为在原点有严格统一界的实际局部 Newton 来源。没有将极点替换当作原来那个全纯来源。

取 R310 的同一规范
$$
d=p+1=6s,\qquad c=[z^d]\log(\sigma/z),\qquad
\kappa=34c,\quad v_p(\kappa)=-1,\qquad
\widehat H=e^{-\kappa z^d}H.
$$
原解析观察为
$$
\mathcal J_T(u)=\sum_{h\ge0}
[z^{dh}](e^{-\kappa z^d}T)\,\kappa^{-h}(u)_h,
\qquad (u)_h=u(u-1)\cdots(u-h+1).
$$
因此 (18) 在整个原解析圆盘上给
$$
\boxed{
\frac{\mathcal J_{\mathscr T_{p,H}S}(u)}{\mathcal J_H(u)}-A_p
=\frac{\mathcal J_{Hg_1}(u)}{\mathcal J_H(u)}.}            \tag{19}
$$
这里 $\mathcal J_H(0)=1$，而 $\mathcal J_{Hg_1}(0)=0$。R312 的同一中央投影遂给
$$
\boxed{
\mathcal L_H(\mathscr T_{p,H}S)
=\mathcal J_{\mathscr T_{p,H}S}'(0)-A_p\mathcal J_H'(0)
=\mathcal J_{Hg_1}'(0).}                                 \tag{20}
$$
这正是 Cartier 的全纯缺陷被原参考方向杀掉后的实际特征零行；未把 $\mathcal J$ 与 $\mathscr T_{p,H}$ 宣称为对易。

把 $\widehat H=\sum_{j\ge0}h_jz^{6j}$、$g_1=\sum_{j\ge1}v_jz^{6j}$ 代入，完整导数为
$$
\boxed{
\mathcal L_H(\mathscr T_{p,H}S)
=\sum_{h\ge1}(-1)^{h-1}(h-1)!\,\kappa^{-h}
                         \sum_{j=1}^{sh}h_{sh-j}v_j.}    \tag{21}
$$
(16) 给每一个 $v_j$。内和不只取 $j\equiv0\pmod s$。准确写 $j=sq+r$，$0\le r<s$，则其 $\widehat H$ 指标为
$$
sh-j=s(h-q-\epsilon_r)+r^*,\quad
\epsilon_r=\begin{cases}0&r=0,\\1&r>0,\end{cases}
\quad
r^*=\begin{cases}0&r=0,\\s-r&r>0.\end{cases}              \tag{22}
$$
所以全部 $s$ 个 tame 块及 $r>0$ 的一次进位都在 (21) 中。真实 Gaussian 在 $h_j$ 中，没有用未付的有限 Frobenius 矩阵代替它。

## 7. 原首 divided 行准确保留，全部高位仍有界

令
$$
R_E=p^{-1/(p^2-1)},\qquad R=p^{-1/(2p)}.
$$
R301 的高度二正式坐标界及 R310 的真实参考界给
$$
\|t/z\|_{R'}=\|z/t\|_{R'}=1\quad(R'<R_E),\qquad
\|\widehat H\|_R=\|\widehat H^{-1}\|_R=1.
$$
(14) 的所有参数整、分母为单位，因此
$$
\|g_1\|_{R'}\le(R')^6,\qquad
\|g_1-g\|_{R'}\le p^{-1}(R')^6.
$$
特别
$$
\|\widehat H(g_1-g)\|_R\le p^{-1}R^6.
$$
逐系数并使用 $v_p(\kappa)=-1$，可得对于每个 $h\ge1$
$$
v_p\left(\kappa^{-h}[z^{dh}]\widehat H(g_1-g)\right)
\ge1+\left\lceil\frac{h(p-1)+6}{2p}\right\rceil.          \tag{23}
$$
这给全 Tate 代数同余
$$
\boxed{
\mathcal J_{Hg_1}-\mathcal J_S\in p^2\mathbb Z_p\langle u\rangle.}   \tag{24}
$$
由 R308，$\mathcal J_H\in1+p\mathbb Z_p\langle u\rangle$，故 (19) 准确推出
$$
\boxed{
\frac{\mathcal J_{\mathscr T_{p,H}S}}{\mathcal J_H}-A_p
\equiv\frac{\mathcal J_S}{\mathcal J_H}\pmod {p^2}.}       \tag{25}
$$
特别这次真实同源运输保留的是同一个原首 divided slope：
$$
\boxed{
\frac{\mathcal L_H(\mathscr T_{p,H}S)}p
\equiv\frac{\mathcal J_S'(0)}p
\equiv\frac{[z^{p+1}]S}{34pc}\pmod p.}                    \tag{26}
$$
最后一步是 R301 的原首层结论；(23) 对 $h\ge2$ 更强，因而没有遗漏高位 carry。

完整导数仍是 (21)。若只保留外和 $1\le h\le M$，其尾项赋值至少
$$
\left\lceil\frac{(M+1)(p-1)+6}{2p}\right\rceil+v_p(M!).
                                                                    \tag{27}
$$
对 (21) 与原 $S$ 导数之差，(27) 还多加一。这一界趋于无穷，支付全部高位，而不把模 $p$ 的首层与完整非零等同。

## 8. 真正的 prime-to-$p$ 挠点极限

置 $P_a^{(n)}=[-p]^nP_a$，并用同一原留数定义 $g_n$。每个原约化点在 $E(\mathbb F_{p^2})$ 中，且
$$
[p+1]\bar P_a=0
$$
因为 $[-p]=\operatorname{Frob}_p^2$ 在这个剩余域上固定点。

在该剩余盘内，$[p+1]$ 对形式群是同构。因此存在唯一 $T_a$ 满足
$$
[p+1]T_a=0,\qquad T_a\equiv P_a\pmod p.
$$
这是一个真正的 prime-to-$p$ 挠点提升，且与负号及 $[\omega]$ 都相容。写 $P_a=T_a+Q_a$，则 $Q_a$ 在形式群的 $p$ 邻域。由于 $[p](t)\in p\,t\mathcal O_p[[t]]+t^p\mathcal O_p[[t]]$，逐次有
$$
[-p]^nQ_a\in\widehat E(p^{n+1}\mathcal O_p).
$$
所以 $P_a^{(n)}\to T_a$。定义
$$
g_\infty(z)=\sum_a\varrho_a
                \frac{2y(T_a)}{x(z)-x(T_a)}.
$$
相同四轨道计算和 (23) 给
$$
\boxed{
g_n-g_\infty\in p^{n+1}t^6\mathcal O_p[[t^6]],\qquad
\mathcal J_{Hg_n}-\mathcal J_{Hg_\infty}
       \in p^{n+2}\mathbb Z_p\langle u\rangle.}            \tag{28}
$$
原留数一直保留。$Hg_\infty$ 一般仍不是全局全纯来源，(28) 是同一个真实原点观察中的收敛及高位误差。

因为 $[-p]T_a=T_a$，(9) 还给一个特征零的准确固定关系
$$
\phi_*(g_\infty dz)=g_\infty dz+A_\infty dz,\qquad
\mathscr T_{p,H}(Hg_\infty)=Hg_\infty+A_\infty H,          \tag{29}
$$
其中 $A_\infty$ 由 (10) 将 $P_a$ 换成 $T_a$ 得到。于是其完整参考商减去 $A_\infty$ 后固定，不能把这个固定关系改写成 $\mathcal J$ 的未证明对易性。

综上，在一个已证明非空的正密度惰性族上，原首 divided 行可以准确运输到以 $(p+1)$ 挠点为极的来源；整个 $H_3$ 乘子、原留数及误差均已支付。要由此完成原课题，还需要证明 (26) 或其保留全部尾项的版本跨素数非零；(5)、(25)、(29) 自身没有给出这项非消失。

## 9. 精确证书与直接依赖

生产脚本 [check-jzero-frobenius-square-actual-trace.py](../scripts/check-jzero-frobenius-square-actual-trace.py) 及其 JSON 有 **34 项精确检查全部 PASS**。它核定 (4)、一般有理同源的完整 fibre trace 分解、原 $[3]$ 和 $[5]$ 除法式及曲线方程、所有 tame 进位，并在单个固定素数 $p=59$ 上核定整个有理 Cartier 平方等式。

该有限证书中 $f(u)=u^3-204u^2-384u+64$ 的三个根为 $45,47,53$，所有极确在 $\mathbb F_{59^2}$；完整计算得到
$$
\mathcal C^2\bar\eta=\bar\eta+16\,d\bar z.
$$
脚本另从原 $t^{3480}$ 系数独立得到同一个 $16$。这一例检验精确规范；正密度族由 §1 的固定域 Chebotarev 证明，原中央非零没有从该有限例推断。

直接依赖：
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R306](R306-jzero-three-sextic-original-local-data-and-full-weight-squares.md)、
[R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)、
[R308](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)、
[R310](R310-jzero-actual-rankzero-frame-third-kind-and-central-transpose.md)、
[R312](R312-original-central-projection-fixed-poles-and-complete-kernels.md)。
中央投影采用 R312 的同一 $H_3$ 规范；其杀常数方向的特例也已在 (19)–(20) 直接证明。


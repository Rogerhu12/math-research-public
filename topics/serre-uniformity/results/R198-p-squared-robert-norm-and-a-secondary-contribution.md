# R198：真正的 $p^2$ Robert 范数见证与一个二阶贡献

**状态：已证明。** 固定 R171 的 $p=43$、同一 $776$ 位素数 $q$、
$P$ 与 Weil 根。本文给出纯 $p$ 反循环扩张上的真实受支撑 Norm 见证，
并实际计算其在 $q$ 的原始子。结果为
$$
(e_p)_q=28K_0,\qquad
\Gamma_p=13b_q=-13\epsilon.
\tag{198.1}
$$
它只是完整二阶障碍的纯 $p$ 子项，不是 $\Omega_2$。
本次环境中断后所有输入、源与证书已重建、实际重跑；新 SHA 另记。

## 1. 规范函数与全局精确 Norm

置 $K=\mathbb Q(i)$、$A:y^2=x^3-x$，
$P_2=(i,1-i)$、$2P_2=(0,0)$。
固定实 $P\in A[p]$，并选实 $R\in A[p^2]$ 满足 $pR=P$。
令
$$
T_r=K(A[p^r]),\qquad
F_r=T_r^{(\mathbb Z/p^r\mathbb Z)^\times}.
\tag{198.2}
$$
标量子群取 CM 表示中的有理标量，故
$[F_1:K]=44$、$[F_2:F_1]=43$。
$F_2=F_1L_p$，其中 $L_p$ 是 R196 的纯 $p$ 反循环射线扩张。

在短 Weierstrass 模型 $E$ 上，令
$$
\mathcal F_E(Q)=\frac{\Delta_E^{10}}{\psi_{11,E}(Q)},
\tag{198.3}
$$
$\psi_{11}$ 的首项为 $11x^{60}$。
它的除子是 $121[O]-E[11]$，在 $O$ 的首项为
$\Delta^{10}t^{120}/11$。

### 1.1 为什么这里是精确分布关系

A. J. Scholl, *An introduction to Kato's Euler systems* (1998),
Theorem 1.2.1(iii)、Remark(iv)，printed pp.384–385，
给出 Kato--Siegel 函数的精确 isogeny Norm。
其证明 pp.385–386 还说明：由 $\Delta^{(D^2-1)/12}$ 给出的
两个整体符号规范中，任一规范对奇数度同源的 Norm 比均为 $+1$。
(198.3) 的零点首项正是这两个规范之一。
所以对任意与 $11$ 互素的奇数度同源 $\phi:E\to E'$，
$$
\prod_{\phi Q=Q'}\mathcal F_E(Q)=\mathcal F_{E'}(Q').
\tag{198.4}
$$
不需要取 $12$ 次幂，也没有未确定的局部根因子。
作者原稿：
<https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf>。
这里只用函数的几何 Norm，未借用该文的 Frobenius 约定。

定义
$$
u_0=N_{T_1/F_1}\mathcal F_A(P_2+P),\qquad
u_2=N_{T_2/F_2}\mathcal F_A(P_2+R).
\tag{198.5}
$$
$T_2/T_1$ 的作用遍历 $R+A[p]$。
用 (198.4) 的 $[p]$ Norm，
$$
N_{T_2/T_1}\mathcal F_A(P_2+R)
 =\mathcal F_A([p]P_2+P)=\mathcal F_A(-P_2+P).
$$
函数偶，且标量 Norm 可把 $P$ 改成 $-P$，故
$$
\boxed{N_{F_2/F_1}u_2=u_0.}
\tag{198.6}
$$
这些 torsion 模数含 $2,p$ 两个不同素因子，
相应 Robert 值是全局单位；至少在 $\{2,p\}$ 外为单位，
已足够本文。因而这是受支撑的实际 Norm 见证，
不只是 Hasse norm theorem 的存在性。

## 2. 为何 $q$ 处可用 $p$ 挠点商曲线

本例
$$
q\equiv-1\pmod{172},\quad
v_{43}(q+1)=1,\quad(q+1)/43\equiv11\pmod{43}.
\tag{198.7}
$$
$q$ 在 $K$ 惰性，$A/\mathbb F_{q^2}$ 的 Frobenius 是 $[-q]$。
故 $A[p]$ 全有理；所有 $p$ 同源商 $E_H=A/H$ 的 $p$ 挠点也全有理。
这不要求 $-q\equiv1\pmod{p^2}$，也不声称 $A[p^2]$ 全有理。

取 $H=\langle P\rangle$、规范 Vélu 同源 $\phi_H:A\to E_H$，
置 $S=\phi_H(iP)$。对偶同源的核为 $\langle S\rangle$，
其 $P$ 的原像为 $Q+tS$，$t\in\mathbb F_p$。
选择实 $Q$ 满足
$$
\widehat\phi_H(Q)=P,\quad Q\in E_H[p](\mathbb F_q).
\tag{198.8}
$$
证书直接检查点、阶、两次 Vélu 及对偶模型缩放；
并用 Miller 算法重新核 $\zeta=e(P,iP)$。

$F_2/F_1$ 在该 $q$ 素点分裂。
选择与全局实 $R$ 相容的上方素点，使 $\phi_HR=Q$。
复共轭把 $Q+tS$ 变成 $Q-tS$，所以实分支唯一。
这同时固定了本文的 $\Gamma$ 生成元和局部 Norm 原始子规范。

R196 的 $\kappa_p=-2\operatorname{Im}\ell_\psi$，
因此 $\kappa_p(\gamma)=1$ 的分支作用为
$$
Q\longmapsto Q+21S,\qquad -2\cdot21=1\pmod{43}.
\tag{198.9}
$$

## 3. $p^2$ 上的 tame CM 轨道

取 primary $\beta=-1+2i$，它固定 $P_2$。
模 $p^2$ 的 CM 对数为
$$
\ell_\psi(\beta)=22+11i.
\tag{198.10}
$$
$44$ 条非标量轨道取 $P_j=\beta^jP$，
$H_j=\langle P_j\rangle$、$E_j=A/H_j$、
$S_j=\phi_j(iP_j)$。
从 $p^2$ 层移除 $\beta$ 的 $1+p$ 部后，
标量 $22$ 部在 $H_j$ 中消失，虚部留下
$$
Q_{j+1}=\beta_j(Q_j)-11S_{j+1}.
\tag{198.11}
$$
这里 $\beta_j:E_j\to E_{j+1}$ 的核为
$\phi_j(A[\beta])$。用一个实际 $5$ 挠点 $T_\beta$
构造规范 Vélu 模型后，按 $x/\beta^2,y/\beta^3$ 缩放，
得到该 CM 同源。程序逐次核曲线方程、核、$S$ 标签和 $Q$ 阶。

这一步不能只在残余层用 $\beta P$，否则会混入非零
$\kappa_p(\beta)=21$ 的作用。
$44$ 次后 $P,Q,S$ 均为初始点的 $[5]$，商曲线回原模型；
所有三个闭合等式直接核验。

## 4. 具体有限域算法

在第 $j$ 条轨道，标量 $p$ 方向的 Norm 用 (198.4) 压成
商曲线上的值：
$$
u_{2,j,t}
 =\prod_{k=1}^{42}
 \mathcal F_{E_j}\bigl(\phi_j(P_2)+k(Q_j+21tS_j)\bigr).
\tag{198.12}
$$
于是只需 $44\cdot43\cdot42=79464$ 个 $\psi_{11}$，
不需要构造次数 $p^2$ 的 torsion 域。
对于每个 $j$，程序直接比较
$$
\prod_{t=0}^{42}u_{2,j,t}=u_{0,j}
\tag{198.13}
$$
并得到精确比值 $1$，不是仅在 $p$ Kummer 商中相等。

记 $D=\sum_{t=0}^{42}t\gamma^t$，
$\ell(v)=\log_\zeta(v^{(q^2-1)/43})$，
$\omega=8+25i$。
计算给出
$$
\sum_{j=0}^{43}\omega^j\ell(u_{0,j})=0,\qquad
\sum_{j=0}^{43}\omega^j\ell(u_{2,j}^{D})=13i.
\tag{198.14}
$$
每条轨道的两个对数与 Norm 比值都保存在 JSON 中，
可从头重算。

所用 $\psi_{11}$ 由标准 division-polynomial 递推直接实现。
商曲线 Vélu 公式用配对的核点 $\pm(u,v)$：
$$
t=6u^2+2a,\quad w=4v^2,\quad
a'=a-5\sum t,\quad b'=b-7\sum(w+ut),
$$
$$
x'=x+\sum\left(\frac{t}{x-u}+\frac{w}{(x-u)^2}\right),\quad
y'=y\left(1-\sum\left(\frac{t}{(x-u)^2}
 +\frac{2w}{(x-u)^3}\right)\right).
\tag{198.15}
$$
所有输入和像点均验证方程，未使用浮点。

## 5. $d_0$、原始子与未分歧二次限制

R185 固定
$$
d_0=\frac{i}{1848}\sum_{j=0}^{43}[u_{0,j}]\otimes D_{\omega^j}.
\tag{198.16}
$$
$1848^{-1}=-1\pmod{43}$，所以 (198.14) 在 $K_q$ 上给
$D$-单位的 $d_0$ 坐标为 $13$。

按 R191 的正 Norm 原始子约定，
$\delta Q=\kappa_p\cup d_0$；
在 $L_p$ 分裂的局部点，$Q=-\kappa(u_2^D)$。
故其 $K_q$ 坐标为 $-13$。
R196 的实际 dual $WW$ 差为 $-i\kappa_p$，
所以正原始子 $e_p$ 的 $K_q$ 坐标为 $13i$。

$K_q/\mathbb Q_q$ 是未分歧二次，Frobenius 限制把有限坐标乘 $2$。
因此在 R168 的 $W(1)$ 有限基 $K_0$ 中
$$
\boxed{(e_p)_q=(13/2)K_0=28K_0.}
\tag{198.17}
$$
全部符号与因子依次是：$1848^{-1}$、乘 $i$、
正 Norm 原始子的负号、实际 $-i$、最后限制除 $2$。

这里 $d_0|_q=0$。若为它选择零 cocycle，
原始子的相应校正在 $G_{K_q}$ 上为零，
因为 $\kappa_p|_{G_{K_q}}=0$。
限制次数 $2$ 可逆，所以 (198.17) 的有限类不变。
这补足了 cohomology 零与实际 cocycle 规范之间的步骤。

## 6. 次级杯积与真实纯 $p$ 贡献

令 $j:\eta\otimes W\to W$ 为乘 $-i$，
它对迹配对是反对称的。设
$\delta b=\kappa_p\star_j c_W$、
$\delta e=\kappa_p\star_j d_0$，并令
$h(g)=j(\kappa_p(g),c_W(g))$。
直接用 Leibniz 公式和
$\delta h=-(\kappa_p\star c_W+c_W\star\kappa_p)$ 得
$$
\operatorname{Tr}(b\cup d_0)+
\operatorname{Tr}(c_W\cup e)+
\operatorname{Tr}(h\cup d_0)
\tag{198.18}
$$
是 $\mu_p$ 值 $2$-cocycle。

所需受支撑原始子存在：R176 的相关
$H^2(G_{\mathbb Q,S},W)\to\bigoplus_vH^2(\mathbb Q_v,W)$
为单射；纯 $p$ cup 在 $q$ 因 $\kappa_p=0$，
在 $p,2$ 因局部 $H^2$ 消失，其余处不分歧，故全局为零。
也可对 (198.6) 的实际 Norm 见证直接构造 dual 原始子。

在 $p$ 把 $c_W$ 选为零，其零阶规范因 $H^0(\mathbb Q_p,W)=0$
而唯一；在 $q$ 把 $d_0$ 选为零。
其余有限处局部 invariant 为零。
对 (198.18) 用全局互反：
$$
\langle b_p,d_{0,p}\rangle
 =-\langle(c_W)_q,e_q\rangle.
\tag{198.19}
$$
R168 的杯积是
$$
\langle(a,b),(u,v)\rangle=2(av-bu).
$$
代入 $(e_p)_q=(28K_0,0)$，得到
$$
\Gamma_p=2\cdot28b_q=13b_q=-13\epsilon,
\tag{198.20}
$$
其中 R171 $x_q=-1$、$b_q=\epsilon x_q$。

改变全局正原始子只添加 $H^1(G_{\mathbb Q,S},W)$ 的类。
与 $d_0$ 的全局互反中，$q$ 因 $d_0|_q=0$、$2$ 因局部消失、
其余处因不分歧均不给贡献，所以 $p$ 配对不变。
故 (198.20) 是这个纯 $p$ 子项的规范贡献。

## 7. 不能省略的剩余项

实际 dual 差是 $-i(\kappa_p+2\kappa_q)$；
本条只完成第一项。primal 另有 $-\ell_{\rm cyc}$，
并有 $W\to\eta$ 通道，不能自行置零。

例如在 $q$，令
$z=(q+1)/p$、$a=\epsilon z/2$、$b=\epsilon x$、
$\kappa_q(\mathrm{inertia})=-x$、
$\ell_{\rm cyc}(\mathrm{Frob}_q)=-z$。
primal 中 cyclotomic 与 $\kappa_q$ 两项的局部 $H^2$ 系数为
$$
-(-z)b+2(-x)a=0.
\tag{198.21}
$$
它们是彼此抵消，并非各自局部 exact。
(198.21) 与 (198.20) 的非零纯 $p$ 贡献完全相容。
R200 处理完整抵消和二阶方程；本文不宣称总 $\Omega_2$ 非零。

## 8. 完整复算

- [verify_r198_p_squared_robert_norm.js](../scripts/verify_r198_p_squared_robert_norm.js)
- [r198_p_squared_robert_certificate.json](../notes/r198_p_squared_robert_certificate.json)

~~~sh
node scripts/verify_r198_p_squared_robert_norm.js notes/r198_p_squared_robert_certificate.json
~~~

源内嵌完整输入；传 JSON 时比较所有行。
可用 `--certificate <路径>` 重建证书。
本轮实际完整输出：
~~~json
{"status":"PASS","psi11_evaluations":79464,"all_44_norm_ratios":"1",
"CM_log_beta":[22,11],"Weil_pairing_verified":true,
"all_three_beta44_closures":"[5]","raw_base_sum":[0,0],
"raw_derivative_sum":[0,13],"Qq_pure_p_actual_reference":[0,28],
"positive_secondary_coefficient":13,"total_Omega_2_computed":false}
~~~

主要输入为 R171、R176、R180、R185、R196。
唯一新增函数分布来源已在 §1.1 精确列明；
其余 Norm、CM 校正、杯积符号及有限域数据均给出完整证明或整数证书。

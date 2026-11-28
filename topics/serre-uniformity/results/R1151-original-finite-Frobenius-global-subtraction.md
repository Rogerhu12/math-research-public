# R1151：原有限 Fontaine–Laffaille 坐标中的全局减法及完整退化分支

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 本篇固定 R1147 的同一个规范 Heisenberg 覆盖。先对所有 $p>37$ 支付局部有限 Fontaine–Laffaille 坐标的完整双射，再在 R1148 的全局生成范围 $p>C_{\rm cyc}$ 写出全部 global lifts 的实际坐标。最后把它代入 R1149 / R1150 的同源短盘公式。

本篇计算的是同一全局提升的真正中央 subtraction；不是把原局部第三槽 $\mathsf h$ 单独当作障碍。所有原局部化系数可能为零的分支都保留。

## 1. 原四维有限 torsor 的规范 Frobenius 坐标

保持
$$
L_r=\mu_p^{\otimes r},\qquad
\mathcal H=L_3\oplus L_5\oplus L_8,
$$
以及原群律
$$
(a,b,h)(a',b',h')
 =(a+a',b+b',h+h'+ab').
\tag{1151.1}
$$
乘积 $L_3\otimes L_5\to L_8$ 是原 Tate tensor identification。

在 $\mathbb Q_p$ 上，取同一 Tate de Rham generators $\tau^r$。令
$M=\mathbb F_p e_0\oplus\mathbb F_p e_3
 \oplus\mathbb F_p e_5\oplus\mathbb F_p e_8$，
其 filtration jumps 为 $0,-3,-5,-8$。给定任意
$(A,B,H)\in\mathbb F_p^3$，定义 divided Frobenii
$$
\begin{aligned}
\varphi_0(e_0)&=e_0+A e_3+B e_5+H e_8,\\
\varphi_{-3}(e_3)&=e_3,\\
\varphi_{-5}(e_5)&=e_5+A e_8,\\
\varphi_{-8}(e_8)&=e_8.
\end{aligned}
\tag{1151.2}
$$
其它 filtration restrictions 按 Fontaine–Laffaille 关系延长。
其 divided matrix 正是
$$
R(A,B,H)=
\begin{pmatrix}
1&0&0&0\\
A&1&0&0\\
B&0&1&0\\
H&0&A&1
\end{pmatrix}.
\tag{1151.3}
$$
它可逆，所以 (1151.2) 是 strongly divisible finite module。也可先取任意三个整数 lifts，令
$\Phi=R(A,B,H)\operatorname{diag}(1,p^{-3},p^{-5},p^{-8})$
并取同一 split filtration，得到一个整 strongly divisible lift。

原 affine hyperplane $s=1$ 及 right action 是
$$
(s,a,b,h)\cdot(x,y,z)
 =(s,a+sx,b+sy,h+sz+ay).
\tag{1151.4}
$$
(1151.3) 是左乘，它与 (1151.4) 相容；Tate weights $3+5=8$ 也使 coefficient Frobenius 保持乘法。
这些 tensor identities 的幅度至多 $16<p-2$。
因此 R1147 §14 已消费的 Fontaine–Laffaille exact、fully faithful、short-tensor comparison 将 (1151.2) 实现为一个真正的 $\mathcal H$-torsor。

反之，比较对象中 $\operatorname{Fil}^0M\to\mathbb F_p$ 严格同构，映到一的 Hodge lift 唯一。right action 在该点的微分给原 $L_3,L_5,L_8$ 三条指定基线，从而锁定整个 frame。故保持原 torsor、flag 和 Tate lines 的同构必保持此 frame。由 fully faithfulness，不同 $(A,B,H)$ 给不同局部 torsor classes。

还须证明没有遗漏不在此构造中的 local classes。对 $r=3,5,8$，local Tate duality 给
$H^0(\mathbb Q_p,L_r)=H^2(\mathbb Q_p,L_r)=0$，
Euler characteristic 给
$$
\dim_{\mathbb F_p}H^1(\mathbb Q_p,L_r)=1.
$$
特别中心 $H^2(\mathbb Q_p,L_8)=0$ 使全部 abelian pairs 可提升；固定 pair 的 lifting fiber 是 $H^1(\mathbb Q_p,L_8)$ 的 torsor。商的 $H^0$ 为零，不再商去额外 automorphisms。因此总共有 $p^3$ 个 local classes，正好是上面已构造的 $p^3$ 个互异 classes。

得到规范双射
$$
\boxed{\quad
\mathcal F_p:H^1(\mathbb Q_p,\mathcal H)
 \xrightarrow{\ \sim\ }\mathbb F_p^3,\qquad
[\mathscr T]\longmapsto(A,B,H).
\quad}
\tag{1151.5}
$$
这是按原 Tate generators 读取的 Frobenius 坐标，不是任选一个 Galois cocycle representative 的三个数。换 Tate generator 时按权 $3,5,8$ 同时运输。

其中前两槽分别给原两个 local $H^1$ 的线性坐标。
若两个 torsors 的前两槽同为 $(A,B)$，其中心 torsor 差在
$H^1(\mathbb Q_p,L_8)$ 的同一线性 Frobenius 坐标中恰为
$$
H-H'.
\tag{1151.6}
$$
可直接用 $R(A,B,H)R(A,B,H')^{-1}=R(0,0,H-H')$ 核准。
这里仅在 quotient 已经相同后取中央差。

R1147 的原 finite quotient 及 R1149 的
$(\mathsf a,\mathsf b,\mathsf h)$ 是同一 (1151.2)–(1151.4) 规范。
R1150 已支付其 relative associatedness，因而下文没有另换 local torsor 或 Hodge frame。

## 2. 全局 lifting 的 bilinearity 与指定生成元

记 $S_0=\operatorname{Spec}\mathbb Z[1/p]$。
R1146 已证明
$$
H^1(S_0,L_8)=H^2(S_0,L_8)=0.
$$
于是对每个原 global abelian pair $(u,v)$ 有唯一提升
$\eta(u,v)\in H^1(S_0,\mathcal H)$。

这个唯一提升在每一槽分别是 additive 的。说明此处所需的准确含义：
固定第一槽，取两个 torsors 在共同 $L_3$-quotient 上的 fiber product。
群同态
$$
(a,b_1,h_1;\ a,b_2,h_2)
 \longmapsto(a,b_1+b_2,h_1+h_2)
$$
给 $\eta(u,v_1+v_2)$；群律中的两个 cross terms 正好相加。
固定第二槽时同理。$H^0(S_0,L_3)=H^0(S_0,L_5)=0$ 使共同 quotient 的同构无歧义，而全局中心 $H^1=0$ 给所需唯一性。

因此若任选原全局两个 $H^1$ 的 bases $(u_i),(v_j)$，并写
$$
\mathcal F_p(\operatorname{loc}_p\eta(u_i,v_j))
 =(r_i,s_j,z_{ij}),
$$
则实际全局局部化像准确为
$$
\left\{
\left(\sum_i x_i r_i,\ \sum_j y_j s_j,\
       \sum_{i,j}x_i y_j z_{ij}\right)
 :x_i,y_j\in\mathbb F_p
\right\}.
\tag{1151.7}
$$
finite filtered fiber products 的唯一 Hodge lift 同样相容，故上述 additivity 确实适用于第三个 Frobenius 坐标；没有先给非阿贝尔 $H^1$ 强加线性结构。

现在进入 R1148 §§10–11 已付的范围
$$
p>C_{\rm cyc}=\exp(9^{224\cdot9^4}).
$$
原 circular-unit classes 满足
$$
H^1(S_0,L_3)=\mathbb F_p\gamma_3,\qquad
H^1(S_0,L_5)=\mathbb F_p\gamma_5.
$$
令同一原全局 torsor 为
$$
\Theta=\eta(\gamma_3,\gamma_5),\qquad
\mathcal F_p(\operatorname{loc}_p\Theta)=(r,s,z).
\tag{1151.8}
$$
三个数都来自这个指定对象；本篇不假定 $r,s,z$ 非零。

这里还可识别一个已经存在的原输入：R1149 参考 $F_0$ 的 $T_0$ 是同一常数 $\gamma_5$ extension 的 Frobenius 坐标，而 $\Theta$ 的第二 quotient 正是 $\gamma_5$。在上述同一 Tate generator 下，
$
\boxed{\ s=T_0=u_5\bmod p.\ }
\tag{1151.8a}
$
$u_5$ 是 R1150 (1150.11) 的实际常数；它没有因原相对连接槽为零而消失。


原 scaling homomorphism
$[x,y](a,b,h)=(xa,yb,xyh)$
保群律、Tate lines 与 filtration。R1148 的全局唯一性身份
$\eta(x\gamma_3,y\gamma_5)=[x,y]_*\Theta$
遂在同一 finite frame 中准确成为
$$
\boxed{\quad
\mathcal F_p(\operatorname{loc}_p\eta(x\gamma_3,y\gamma_5))
 =(rx,sy,zxy).
\quad}
\tag{1151.9}
$$
它支付了全部 $p^2$ 个 global labels 的第三槽，不只给其存在性。

## 3. 不除掉零局部化的完整像

给定一个原 local fibre，其坐标为 $(A,B,H)$。
它与某个 global label 相容，当且仅当存在 $x,y\in\mathbb F_p$ 使
$$
A=rx,\qquad B=sy,\qquad H=zxy.
\tag{1151.10}
$$
逐项消元给完整分类：

| 原常数 | 准确充要条件 |
|---|---|
| $r\ne0,\ s\ne0$ | $rsH=zAB$ |
| $r=0,\ s\ne0,\ z=0$ | $A=0,\ H=0$ |
| $r=0,\ s\ne0,\ z\ne0$ | $A=0$，且 $B\ne0$ 或 $H=0$ |
| $r\ne0,\ s=0,\ z=0$ | $B=0,\ H=0$ |
| $r\ne0,\ s=0,\ z\ne0$ | $B=0$，且 $A\ne0$ 或 $H=0$ |
| $r=s=0,\ z=0$ | $A=B=H=0$ |
| $r=s=0,\ z\ne0$ | $A=B=0$，$H$ 任意 |

例如第二种非零 $z$ 的退化情形，$y=B/s$ 已定；若 $B\ne0$，$x=sH/(zB)$ 可以实现任意 $H$，若 $B=0$ 则必 $H=0$。其余行同样直接验证。

所以把全部分支统一写成 $rsH-zAB=0$ 会丢失条件；当 $r$ 或 $s$ 为零时，必须使用完整表。
特别，两个原 abelian global classes 的 localization 同为零，并不凭形式迫 $\operatorname{loc}_p\Theta$ 的中心坐标也零。
全局中心 $H^1(S_0,L_8)=0$ 是固定全局 quotient 后的唯一性，不能删除这个实际局部中央值。

在 $rs\ne0$ 的分支，匹配前两槽的 global label 唯一：
$x=A/r,\ y=B/s$。由 (1151.6)，实际原中央障碍的 Frobenius 坐标为
$$
\boxed{\quad
H-\frac{z}{rs}AB.
\quad}
\tag{1151.11}
$$
其中 $z/(rs)$ 是原 $\Theta$ 的具体 arithmetic constant，不可任意设零，也不从全局生成性推它的值。

## 4. 原短盘上的完整 subtraction

沿 R1149 (1149.42)–(1149.44)，所有 $t\in\mathbb F_p$ 取实际有限点：
$$
\begin{aligned}
\mathsf a(t)&=P_a(t)+a_3t^3,\\
\mathsf b(t)&=P_b(t)+b_5t^5,\\
\mathsf h(t)&=P_h(t)+P_a(t)b_5t^5+h_8t^8,
\end{aligned}
$$
其中
$$
a_3=\frac23\delta c_g^2A_*,
\qquad b_5=\frac85\delta^2c_g^4B_*,
\qquad h_8=\frac25\delta^3c_g^6A_*B_*
 =\frac38a_3b_5.
\tag{1151.12}
$$
$\deg P_a\le2,\deg P_b\le4,\deg P_h\le6$，完整 $F_0$ 与有限 $q_t$ 都按原文保留。

当 $rs\ne0$，令
$$
\mathcal D(t)=rs\,\mathsf h(t)-z\,\mathsf a(t)\mathsf b(t).
$$
直接展开得到原实际 comparison polynomial
$$
\boxed{\begin{aligned}
\mathcal D(t)
={}&rsP_h-zP_aP_b-z\,a_3t^3P_b\\
 &+(rs-z)P_a b_5t^5
   +a_3b_5\left(\frac38rs-z\right)t^8.
\end{aligned}}
\tag{1151.13}
$$
它除以非零的 $rs$，才是 (1151.11) 的实际中央差。
特别八次项是
$a_3b_5(3rs/8-z)$；即使原 $h_8$ 非零，也不能据此宣整个 global subtraction 的八次项非零。
$P_a b_5t^5$ 的原 cross term已保留，没有在减法中消失。

在零局部化分支，仍逐点把完整三槽代入 §3 的表；(1151.13) 单独只给必要条件。

## 5. Gaussian 与 cubic 参考点的真正最高项

仍取 R1149 的同一 $(\nu,\mu)$、$c_g$、$\lambda$、$\delta$。
下列 $x_4,y_8,y_7,z_{12}$ 是参考 $F_0$ 的实际有限 coefficients：
$$
\begin{aligned}
X_0&=\cdots+x_4\mu^4\tau_1,\\
Y_0&=\cdots+y_7\nu\mu^7\tau_1+y_8\mu^8\tau_1,\\
Z_{0,0}&=\cdots+z_{12}\mu^{12}\tau_1^2.
\end{aligned}
\tag{1151.14}
$$
不把 $z_{12}$ 当成已经减掉 global label 的数。

### 5.1. Gaussian：coarse cubic

此时 $A_*=B_*=0$，令 $T=t^2$。
写
$$
\mathsf a=A_0+A_1T,\quad
\mathsf b=B_0+B_1T+B_2T^2,\quad
\mathsf h=H_0+H_1T+H_2T^2+H_3T^3.
$$
这里 $A_i,B_i,H_i$ 是三个有限多项式的系数，不是 Weierstrass 方程的 coefficients。

原 $q_t$ 的 binomial 公式给
$$
A_1=2\delta c_g^2x_4,\qquad
B_2=8\delta^2c_g^4y_8,\qquad
H_3=16\delta^3c_g^6z_{12}.
\tag{1151.15}
$$
最后一式中，$\Pi_2$ 与 $\Pi_4$ 槽次数至多二与一，故不贡献 $T^3$。
因此真正的最高 comparison coefficient 为
$$
\boxed{\quad
[T^3]\mathcal D
=16\delta^3c_g^6\bigl(rs\,z_{12}-z\,x_4y_8\bigr).
\quad}
\tag{1151.16}
$$
所有较低项仍准确为
$$
\begin{aligned}
D_0&=rsH_0-zA_0B_0,\\
D_1&=rsH_1-z(A_0B_1+A_1B_0),\\
D_2&=rsH_2-z(A_0B_2+A_1B_1).
\end{aligned}
\tag{1151.17}
$$
这些式子保原 actual-good labels，不以旁边某个 Eisenstein coefficient 的单位性代替 (1151.16)。

### 5.2. Cubic：coarse quadratic

此时 $B_*=0$，令 $T=t^3$。
记 reference curve 的 Weierstrass coefficient 为 $B_{\rm cub}$，避免与标签系数混同。原文给
$$
\mathsf a=A_0+A_1T,\qquad
A_1=\frac{16}{7}\delta c_g^2B_{\rm cub}\ne0,
$$
$$
\mathsf b=B_0+B_1T,\qquad
\mathsf h=H_0+H_1T+H_2T^2.
\tag{1151.18}
$$
$Y_0$ 的 $i=7$ 项在 (1149.36) 中带
$\binom43/\binom87=1/2$，所以
$$
B_1=4\delta^2\lambda c_g^4y_7,\qquad
H_2=16\delta^3c_g^6z_{12}.
\tag{1151.19}
$$
从而最高 subtraction coefficient 为
$$
\boxed{\quad
[T^2]\mathcal D
=16\delta^3c_g^6
 \left(rs\,z_{12}-z\,\frac{\lambda A_*}{6}y_7\right)
=16\delta^3c_g^6
 \left(rs\,z_{12}-z\,\frac{4\lambda B_{\rm cub}}7y_7\right).
\quad}
\tag{1151.20}
$$
一次项为 $rsH_1-z(A_0B_1+A_1B_0)$，常数项仍为 $D_0$。
这里 $\lambda$ 没有被无根据地规范化为一。

## 6. CM 常数项、有限根与完整小盘的区别

若参考曲线及其原 nonsplit-Cartan point 是一个真正的全局 CM $\mathbb Q$ 点，例如取合适的 rational $p$-unit Gaussian/cubic model，则其同一规范覆盖 fibre 是某个 global label 的 localization。因此
$$
D_0=0.
\tag{1151.21}
$$
这是原 global source 付出的零，不是任意平移中央坐标得到的零。

在 $rs\ne0$ 的 cubic 分支，
$$
\mathcal D(T)=T(D_1+D_2T).
$$
若 $D_2\ne0$，有限 coarse roots 为 $0$ 与 $-D_1/D_2$；若 $D_1=0$，两根合并。若 $D_2=0,D_1\ne0$，只有零根；两系数都零则这一有限条件恒零。
此处 $p\equiv2\bmod3$，$t\mapsto t^3$ 在 $\mathbb F_p$ 上为双射，所以不能把一个非零 coarse root 擅自排成“没有 fine lift”。

Gaussian 则有
$\mathcal D(T)=T(D_1+D_2T+D_3T^2)$，
并须保留 $T=t^2$ 的实际平方限制。
这些都是指定系数的有限等式；没有证明 $D_i$ 非零或判别式在正确平方类。

在 $r=0$ 的 cubic 分支，§3 首先要求 $\mathsf a=0$。
若参考点是上述全局 CM 点，则 $A_0=0$，由 (1151.18) 的单位斜率迫
$$
t=0\quad\bmod p.
\tag{1151.22}
$$
它只把原参数 $u=pt$ 限到 $u\in p^2\mathbb Z_p$。
**这不是 whole $p$-disk 内只剩 CM 点的证明。**
任何仅消费本篇 finite mod-$p$ quotient 的结论，都必须继续支付更深参数、真正高度或其它同源条件，不能把首数字为零改写为 $u=0$。

本篇关闭的是原 global subtraction 的结构门：所欠 arithmetic 数据已明确为同一 $\Theta$ 的 $(r,s,z)$ 与同一 $F_0$ 的 coefficients，真正最高中央组合是 (1151.16)/(1151.20)。
这些组合的实际非零性、一般全盘排点、其余 twists/ramified 情形及 full $N_{\rm ns}$ 的主目标仍继续。

## 7. 精确依赖

- [R1146](R1146-original-proper-arithmetic-Heisenberg-cover.md) §§4–6：原 $S_0$ 上中心 $H^1/H^2$ 消失、每个全局 pair 的唯一提升、local 中心维数与准确 torsor 差。
- [R1147](R1147-original-canonical-moment-Heisenberg-lift.md) §14：同一原 finite quotient、Fontaine–Laffaille finite exact/full faithfulness、原指定格及短 tensor 范围；本篇 (1151.2)–(1151.5) 的全局部坐标双射在正文自证。
- [R1148](R1148-original-canonical-cusp-Heisenberg-and-minus-one-Frobenius.md) §§10–11：$p>C_{\rm cyc}$ 的原 $\gamma_3,\gamma_5$ 全局生成性及同一 $\Theta$ 的 scaling；没有借此取消 localization 为零的分支。
- [R1149](R1149-original-relative-Hodge-section-and-central-connection.md) §§12–16 及 [R1150](R1150-original-relative-log-Frobenius-and-crystalline-identification.md)：原 finite Cartan、divided Frobenius、Hodge frame、相对同源、真实 $F_0$ 及三槽多项式。

无数学程序执行；未重做固定有限素数或整盘窗口。

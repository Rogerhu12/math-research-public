# 原双 S 斜轴的完整核心与同一 native 配对测试

日期：2026-11-15。**状态：已证明。**

本 note 支付 R713/R715 两个剩余斜门的原六输入核心，并把它们送到
同一个 Y-unit 域上的完整原权。它不等待 R719 的特征零有限矩计算。
所有 C 分支、实际 E 单位逆、混合次数至30的周期规范、原负矩以及
未取出的全部外部仍保留。这里没有把整个 degree10710 空间认成标量核。

## 1. 同一完整来源的两条斜轴

使用 [R664](../results/R664-original-double-s-rotation-and-common-companion-gate.md)
的原 C 平均六输入
$\mu_0=\nu_4\otimes\nu_\sigma(c)\otimes\nu_\sigma(d)$，
其中 $\nu_4$ 已含 $-1/84$。保
$$
Q=c+2d,\quad L=2c-d,\quad Y=Y_0=A+Q,\quad
Y_1=A+L,\quad Y_3=A-L,
$$
$$
N(A)=29,\qquad N(Q)=N(L)=5,\qquad
\lambda=-\bar\pi_0^{-1},\quad \kappa=p\lambda^2 .
\tag{1}
$$
所有原 A 伙伴和 C 分支都在以下身份中。定义
$$
\boxed{
L_1=34Y_1-29Y=5A+39c-92d,\qquad
L_3=34Y_3-29Y=5A-97c-24d .
}
\tag{2}
$$
准确有
$$
\langle Y,L_i\rangle=0,\qquad
N(Y)=34,\qquad N(L_i)=10710=34\cdot315,\qquad i=1,3.
\tag{3}
$$

对于 $i=1$，R664 已付原正交轴
$R=Y+Y_1$、$D=Y-Y_1$ 的完整核心均为 $\beta=-\lambda$。
实际变基为
$$
\binom{Y}{L_1}=\frac12
\begin{pmatrix}1&1\\5&-63\end{pmatrix}\binom R D,
\qquad \det=-17 .
\tag{4}
$$
从 $(Y,Y_1)$ 到 $(Y,L_1)$ 的行列式为34。
这里315是原两个 Y 的 Gram 行列式，不是 (4) 的行列式。
所有分母均是原普通射线上的单位。
$Y,Y_1$ 与 $R,D$ 的共同深域相同，正交平面的共同物理缩放亦相同。
因此对每个 $m\ge0$，
$$
\mu_0|_{\{Y,L_1\in p^m\}}
=\lambda^{2m}(P_{Y,\kappa^m}P_{L_1,\kappa^m})_*\mu_0 .
\tag{5}
$$
$i=3$ 用 R664 原整数旋转 $\mathsf J$ 的逆向相邻两 Y；
其 $R_3=Y+Y_3,D_3=Y-Y_3$ 仍为完整126/10两轴。
$\mathsf J_*\mu_0=-\mu_0$ 的符号在等式两端相同，
故 (5) 对 $L_3$ 同样成立。

原 entire Y34 核给
$$
\mu_0|_{Y\in p^m}=\lambda^m(P_{Y,(-\kappa)^m})_*\mu_0 .
\tag{6}
$$
因为 $L_i\perp Y$，在 (6) 附 $L_i\in p^m$ 后，
左边正是 (5)。$\lambda$ 是单位，整物理映射
$P_{Y,(-\kappa)^m}$ 是到其实际像的单射，故其测度推前亦单射。
在原完整测度上直接约去，得到
$$
\boxed{
\mu_0|_{L_i\in p^m}
=\lambda^m(R_Y^mP_{L_i,\kappa^m})_*\mu_0,
\qquad i=1,3,\quad m\ge0 .
}
\tag{7}
$$
这一步无需先假设 $K_{L_i}\mu_0$ 仍在某个未经证明的小格；
只使用 (5)、(6) 的全联合身份和真实推前单射。
它保住所有伙伴，并无新增覆盖、射线或估值成本。

## 2. 原 qcd 的全部位移

以下取 R713/R715 实际使用的 G/C 中性测试；其选列不含未选的 B 块。
固定 $N\in4\mathbf Z_{>0}$，$u=\kappa^N$，并置
$$
W=A+3\delta c+4d,\quad b_Y=(20+3\omega)/17,\quad Z=W-b_YY,
$$
$$
E=E_{YW}=(5+6\omega)A-29c-(58+87\omega)d,\quad
H=D_*-\frac E{29},\quad K=H-\frac{406}{143}D_* .
\tag{8}
$$
$Y,Z,E$ 正交。$C^\perp,D_*,H_1^\perp,E_\perp,G_\perp,G_{00}$
均与 $(A,c,d)$ 平面正交，因而在 (7) 的两个物理映射下逐个保持。

记 $\phi_N\mu_0=\rho_{cd,N}$ 为同一完整 cd 返回来源。
可以保物理 $C^\perp$-unit 指示，也可以使用 R715(3) 的两个
完整 C 分支。后者对每个已作 E 单位逆和实际周期归一的块 P 是
$$
\begin{aligned}
\Phi_{P,N}={}&P(H,E_\perp+uK,G_\perp+guK)\\
&-\eta\lambda P(H,\kappa E_\perp+uK,
                  G_{00}+\kappa(G_\perp-G_{00})+guK),
\qquad g=3-2\omega .
\end{aligned}
\tag{9}
$$
混合齐次次数分别按原 $b^{d/6}\Omega^d$ 归一；
本文没有将高次数块错误地统一除以 $b\Omega^6$。
原 $\lambda,\kappa,u$ 系数和每个 $1+\lambda\kappa^e$ 的单位逆不变。

下列固定系数来自原六行 Hermitian 配对：
$$
a_1=\frac{5+9\omega}{315},\qquad
a_3=\frac{5+3\omega}{315},\qquad
z_1=\frac{-53+117\omega}{5355},\qquad
z_3=\frac{-121-291\omega}{5355}.
\tag{10}
$$
具体
$\langle E,L_i\rangle/10710=29a_i$，
$\langle Z,L_i\rangle/10710=z_i$。
所以在 $P_{L_i,t}$ 下准确为
$$
\begin{aligned}
E_i(t)&=E+29a_i(t-1)L_i,\\
H_i(t)&=H+(1-t)a_iL_i,\qquad
K_i(t)=K+(1-t)a_iL_i,\\
Z_i(t)&=Z+(t-1)z_iL_i .
\end{aligned}
\tag{11}
$$
令 $\phi_{i,N}(t)=\phi_N\circ P_{L_i,t}$；
它由 (9) 同时把 H、K 换成 $H_i(t),K_i(t)$ 得到，
其它输出原样保留。两个 C 分支的替换完全相同，
因为它们的 C 方向与 $L_i$ 正交。
$R_Y$ 不改变这条权，但改变完整 Y 观察的符号。

因此 $\phi_{i,N}(t)$ 是一个真实次数至多30的 t 多项式权；
其系数仍在原完整有界测度上，并保同一个 $C^\perp$-unit 域。
它不是另添的独立算术来源，也不是把 $\phi_N$ 宣布成 $L_i$-不变。

## 3. 同一 Y-unit 域上的全部条件负矩

令 $\ell\ge1$，$t=\kappa^\ell$，$s=(-1)^\ell$。
对任意原有界 Y 测试，(7) 给完整转置。
特别对每个 $k\ge1$，
$$
\boxed{
\begin{aligned}
&\int_{\{Y\ {\rm unit},\,L_i\in p^\ell\}}
       Z^kY^{-k}\phi_N\,d\mu_0\\
&\quad=\lambda^\ell s^k
  \int_{Y\ {\rm unit}}Z_i(t)^kY^{-k}
                         \phi_{i,N}(t)\,d\mu_0 .
\end{aligned}}
\tag{12}
$$
$Y^{-k}$ 只在原 Y-unit 域使用；没有把非单位处的有理测试补定义成
一个可免费交换的来源。式中全部原伙伴和 C-unit 条件均保留。

置
$$
M_{i,k,N}(t)=
\int_{Y\ {\rm unit}}Z_i(t)^kY^{-k}\phi_{i,N}(t)\,d\mu_0 .
\tag{13}
$$
固定 p、N 和同一原测试后，这是 t 的次数至多 $30+k$ 的
**确切多项式**。其负矩系数没有被赋零。
且在 $t=1$，
$$
M_{1,k,N}(1)=M_{3,k,N}(1)
=\int_{Y\ {\rm unit}}Z^kY^{-k}\,d\rho_{cd,N}.
\tag{14}
$$
所以两者之差作为多项式被 $t-1$ 整除。
$t=\kappa^\ell$ 时该因子是单位，不能由此取得额外 p 深度。

对 R715 的两个实际测试，(14) 在 $k=1$ 的共同值为零；
这来自已付的**整个**一阶 Z 条件来源。
它不说明 (13) 在 $t\ne1$ 时为零，更不说明两条带斜门的
原 (12) 各自为零。

## 4. 原 native 配对 Mellin 行的完整返回

以下 $\mathcal I_{0,n},\mathcal I_{1,n}$ 均为
[R713](../results/R713-symmetric-frozen-sources-and-exact-paired-mixed-remainder.md)
的同一 q 与真正 $\mathsf J$ 配对。先按该文作整数旋转换元；
其差域是在同一原来源上
$$
\{Y\in p^n,\ c,d\in p^N\}
\left(1_{\{Y_1\in p^n\}}-1_{\{Y_3\in p^n\}}\right).
\tag{15}
$$
n 大于 N，令 $\ell=n-N$。先作原共同 cd/Y 返回，
再用原 Y 核，两个斜门准确变成 $L_i\in p^\ell$。
整个 T 观察变成 $b_YY+uZ$，S 观察变成 Y，
前因子为 $\lambda^{n+3N}$。这保原
$W P_{Y,(-\kappa)^n}^{-1}$，不是先把它换成裸 W。

写 $f_w(x)=1_{x\ {\rm unit}}\langle x\rangle^{d_pw}$、
$B(w)=\langle b_Y\rangle^{d_pw}$，
则原配对的 T/S 相对部分准确为
$$
\begin{aligned}
\mathcal R_{N,n}(w)
={}&\lambda^{n+3N}
\int (1_{L_1\in p^\ell}-1_{L_3\in p^\ell})\phi_N\\
&\hspace{13mm}\cdot
 \{f_w(b_YY+uZ)-B(w)f_w(Y)\}\,d\mu_0 .
\end{aligned}
\tag{16}
$$
因为 $u\in p\mathcal O$，两个观察的 unit cut 都严格等于 Y-unit。
所以这里的相对质量逐点为零；无需给每一局部质量另赋零。

将 (7)、(11) 全部代入，得到无斜门的同域公式
$$
\boxed{
\begin{aligned}
\mathcal R_{N,n}(w)
={}&\lambda^{2n+2N}\sum_{i=1,3}\epsilon_i
\int_{Y\ {\rm unit}}\phi_{i,N}(t)\\
&\quad\cdot\{\langle b_YY+s uZ_i(t)\rangle^{d_pw}
                  -B(w)\langle Y\rangle^{d_pw}\}\,d\mu_0 ,
\end{aligned}}
\tag{17}
$$
其中 $\epsilon_1=1,\epsilon_3=-1$。
$C^\perp$-unit、两条完整 C 分支和整个移位权仍在 (17) 中。

在 $w=0$ 求导，完整收敛展开是
$$
\boxed{
\mathcal R'_{N,n}(0)
=d_p\lambda^{2n+2N}
\sum_{k\ge1}\frac{(-1)^{k+1}s^ku^k}{k\,b_Y^k}
       \{M_{1,k,N}(t)-M_{3,k,N}(t)\}.
}
\tag{18}
$$
这是原两个条件负矩的准确返回，不是正矩替代负矩。
每个固定 k 的 t 多项式次数界为 $30+k$；
整个 k 尾仍保留。第 R 项之后的尾属于
$p^{(R+1)N-\lfloor\log_p(R+1)\rfloor}\mathcal O$，
因为两个移位权及 $Z_i(t)$ 整有界，且所有实际 log 分母为 k。

原 R713 的完整 $\mathcal O/\mathcal X$ 与原 T 失败支保持原定义。
(17)–(18) 只改写其真实共同部分；不能由这条表示或已知
$J'_S,J'_T$ 的假设把其中一项单独赋零。

## 5. 两斜门的真实近相消分区

在原 $(Y,Z,E)$ 中，
$$
\begin{aligned}
Y_1&=\frac{29}{34}Y-\frac{170+117\omega}{526}Z
                         -\frac{4+9\omega}{263}E,\\
Y_3&=\frac{29}{34}Y+\frac{170+291\omega}{526}Z
                         +\frac{2-3\omega}{263}E .
\end{aligned}
\tag{19}
$$
记其 Z、E 系数为 $b_i,e_i$，则
$$
\boxed{b_1e_3-b_3e_1=-5/263.}
\tag{20}
$$
除去固定有限集合
$p\mid19\cdot61\cdot22699\cdot64111$
（其余 $5,263$ 已在旧坏集中），四个系数皆为单位。
这里只删固定素数，不改变旧高幂射线或任何 fixed modulus。

两个门同时成立当且仅当 $Z,E\in p^\ell$，该共同部分在差中取消。
各不共同的部分准确为
$$
\boxed{
1_{L_1\in p^\ell}-1_{L_3\in p^\ell}
=\sum_{j=0}^{\ell-1}\left(
1_{\substack{v_p(Z)=v_p(E)=j\\ b_1Z+e_1E\in p^\ell}}
-
1_{\substack{v_p(Z)=v_p(E)=j\\ b_3Z+e_3E\in p^\ell}}
\right).
}
\tag{21}
$$
每个 j 的两支严格不交。特别 Z 深 $\ell$ 或 E 深 $\ell$
的部分在差中已经准确消掉；余下不是一个可删的单位补域。
(12)、(17) 是支付 (21) 两支的同源返回，全部 Y 负矩仍保原样。

## 6. 同一 E 深/浅的完整 (Y,Z) 桥

由原完整共同 cd 返回，对任意 (Y,Z) 测试，
$$
(Y,Z)_*\bigl(1_{\{Y,Z,E\in p^N\}}q_N\mu_0\bigr)
=\lambda^{4N}[\kappa^N,\kappa^N]_*\rho_{cd,N}^{YZ}.
$$
另一方面，R686 的完整 Y/Z 矩形、$N\in4\mathbf Z$ 及
$q_N1_{E\in p^N}$ 对 Y/Z 逐点不变给
$$
(Y,Z)_*\bigl(1_{\{Y,Z,E\in p^N\}}q_N\mu_0\bigr)
=\lambda^{2N}[\kappa^N,\kappa^N]_*
 (Y,Z)_*(1_{E\in p^N}q_N\mu_0).
$$
两边是真正同域，推前单射可约去，故
$$
\boxed{
(Y,Z)_*(1_{E\in p^N}q_N\mu_0)
=\lambda^{2N}\rho_{cd,N}^{YZ}.
}
\tag{22}
$$
原完整 $\pi_4$ 返回还给
$(Y,Z)_*(q_N\mu_0)=\lambda^N\mu_0^{YZ}$。因此
$$
\boxed{
(Y,Z)_*(1_{E\notin p^N}q_N\mu_0)
=\lambda^N\mu_0^{YZ}-\lambda^{2N}\rho_{cd,N}^{YZ}.
}
\tag{23}
$$
对 R715 的纯中性差 $\zeta_N$，(23) 第一项为零。
这些是全平面测度身份，故保任意完整 (Y,Z) 测试；
若再附含 E 的斜门，必须回到 (12)/(17) 或保留 (21)，
不能把 E 从来源中忘掉后重新加门。

本 note 的新增结果是 (7)、(11)–(18) 与 (22)–(23)：
原两斜门已具有无额外成本的全来源返回，
代价被准确写成原 q 的有限 E 位移及同一个 Y-unit 域上的
完整条件负矩。它没有解决这些移位负矩与原算术总行的全部补偿；
R719 的有限正混合矩关系仍须与 (18) 区分。

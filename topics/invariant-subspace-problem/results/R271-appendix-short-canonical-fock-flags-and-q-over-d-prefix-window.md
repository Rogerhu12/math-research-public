# R271 附录：短核 canonical Fock 塔与原实际 q/d 前缀窗口

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_rebuild；root 提供短列与高创建像之间的双碰撞投影估计。
状态：已证明。此稿支付原 canonical Fock 塔在短核旗上的全部混合出生 Gram，并将两个实际边界已闭的非真空末段从旧 $q/[128(d+1)]^{d+4}$ 扩大到固定正倍数的 $q/d$。

## 1. 原短核旗和主结论

取有限正行或无限正 $\ell^2$ 行 $a$，令
$$
D=\sum_i a_iE_i,\quad S=\sum_i a_i^2,
\quad\delta=\frac{\max_i a_i^2}{S},
\quad K_b=\ker D\cap\mathcal H_b.
$$
令 $V_p:\mathfrak F_p=\bigoplus_{b=0}^pK_b\to\mathcal H_p$ 为原 canonical 顺次单步 MP 塔
$$
V_p(f_b)=\sum_{b=0}^p\sqrt{(p-b)!S^{p-b}}\,
R_pR_{p-1}\cdots R_{b+1}f_b,
\qquad R_\ell=D_\ell^*(D_\ell D_\ell^*)^{-1}.
\tag{1.1}
$$
下面的条件保证所有涉及的单步逆存在。

固定最高孔层 $P\ge1$、短核阶 $H\ge1$。在第 $p\le P$ 层记
$$
Y_{p,H}=\ker D^H\cap\mathcal H_p,
\qquad
\mathfrak S_{p,H}
=\bigoplus_{b=\max(0,p-H+1)}^p K_b.
$$
标准塔中这些正是创建高度 $r=p-b<H$ 的列。
置
$$
\boxed{\epsilon=4\delta HP<1/2.}
\tag{1.2}
$$

**定理 1.1。** 原 $V_p$ 的准确限制
$$
V_{p,H}=V_p|_{\mathfrak S_{p,H}}
:\mathfrak S_{p,H}\longrightarrow Y_{p,H}
$$
为有界同构，并满足整个混合出生空间上的估计
$$
\boxed{
I\preceq V_{p,H}^*V_{p,H}
\preceq\frac{1-\epsilon}{1-2\epsilon}I,
\quad
\|V_{p,H}\|\le
\kappa:=\sqrt{\frac{1-\epsilon}{1-2\epsilon}},
\quad
\|V_{p,H}^{-1}\|\le1.
}
\tag{1.3}
$$
这些界在全部 $p\le P$ 的正交直和上保持不变。
原精确降阶交织也保持在短列上：标准降阶把高度 $r$ 降为 $r-1$，所以没有离开同一短核阶。

关键费用是 $HP\delta$，而非[完整双塔稿](R271-appendix-bosonic-dual-fock-tower-and-quadratic-collision-conditioning.md)的 $P^2\delta$，也不含旧短塔的 $[32(2H+1)]^H$ 累积。
证明始终保留 $Y_{p,H}$ 的真正正交投影和完整创建像；不是把裸 $D^*$ 当作保核阶的算子。

## 2. 任意平方自由输入的相对碰撞界

先证明不要求 primitive 的新引理。
在真正玻色空间中，以 $b_i,b_i^*$ 表示标准模式删除和创建，并取归一化集体模式
$$
\beta_i=a_i/\sqrt S,\qquad
\mathcal B=\sum_i\beta_i b_i,\qquad
[\mathcal B,\mathcal B^*]=I,
\qquad N=\mathcal B^*\mathcal B.
$$
原平方自由 $p$ 层的正交投影记为 $Q_p$。
在各固定玻色层上所有算子有界；无限行可用固定层范数极限。

**引理 2.1。** 若 $g\in\mathcal H_b$ 是任意平方自由向量、$t\ge1$，并令 $y=(\mathcal B^*)^t g$，则
$$
\boxed{
\|(I-Q_{b+t})y\|^2
\le\delta[4tb+t(t-1)]\,\|y\|^2.
}
\tag{2.1}
$$
这是相对于完整玻色输出范数的界，不把输入限制到某个 primitive。

定义 $P_t(x)=\prod_{j=1}^t(x+j)$、$P_0=1$。
CCR 给
$$
\|y\|^2=\langle g,P_t(N)g\rangle.
\tag{2.2}
$$
平方自由性使 $b_i^2g=0$，故准确有
$$
b_i^2 y
=2t\beta_i(\mathcal B^*)^{t-1}b_i g
 +t(t-1)\beta_i^2(\mathcal B^*)^{t-2}g.
\tag{2.3}
$$
第二项在 $t=1$ 时为零。

为估计第一项，选取单粒子正交基，使其第一模式为 $\mathcal B$，其它模式均与 $N$ 交换。
对全部模式求和不依赖所选正交基。在总次数 $b$ 层上因此有准确恒等式
$$
\boxed{
\sum_i\| (\mathcal B^*)^{t-1}b_i g\|^2
=\left\langle g,
\left[N P_{t-1}(N-1)+(b-N)P_{t-1}(N)\right]g
\right\rangle.
}
\tag{2.4}
$$
其频率 $n$ 为 $0,\ldots,b$。因为
$nP_{t-1}(n-1)\le nP_{t-1}(n)$，右侧至多
$b\langle g,P_{t-1}(N)g\rangle$；而
$P_t(N)\succeq tP_{t-1}(N)$。所以
$$
\sum_i\| (\mathcal B^*)^{t-1}b_i g\|^2
\le\frac bt\|y\|^2.
\tag{2.5}
$$
同样，当 $t\ge2$ 时，
$$
\|(\mathcal B^*)^{t-2}g\|^2
\le\frac1{t(t-1)}\|y\|^2.
\tag{2.6}
$$

碰撞计数满足
$$
I-Q_{b+t}\preceq\frac12\sum_i(b_i^*)^2b_i^2.
$$
在 (2.3) 中用一次两项 Cauchy--Schwarz，随后用
$\beta_i^2\le\delta$、$\sum_i\beta_i^4\le\delta$ 及 (2.5)--(2.6)，便得
$$
\begin{aligned}
\|(I-Q)y\|^2
&\le4t^2\delta\frac bt\|y\|^2
 +t^2(t-1)^2\delta\frac1{t(t-1)}\|y\|^2\\
&=\delta[4tb+t(t-1)]\|y\|^2.
\end{aligned}
$$
$t=1$ 时直接删去第二项。证毕。

## 3. 完整双塔存在，但只估计短列

由 (1.2)，$2(P-1)\delta<1$。因此固定层交换子给每个 $D_\ell$ 满射，$\ell\le P$。
逐层分解
$\mathcal H_\ell=K_\ell\oplus^\perp\operatorname{Ran}D_\ell^*$
保证完整 canonical 塔 (1.1) 是同构。
这里不需要完整塔具有近等距上界。

在归一化玻色空间中，定义完整正交创建列
$$
\mathcal U_p(f_b)
=\sum_{b=0}^p
\frac{(\mathcal B^*)^{p-b}f_b}{\sqrt{(p-b)!}}.
$$
每个 $K_b\subset\ker\mathcal B$，所以这些不同出生的列构成等距映射。
创建后发生的碰撞不能由进一步创建消除，故完整创建塔为
$$
W_p=Q_p\mathcal U_p
=\sum_b\frac{(D^*)^{p-b}}{\sqrt{(p-b)!S^{p-b}}}\bigg|_{K_b}.
$$
与[完整双塔稿](R271-appendix-bosonic-dual-fock-tower-and-quadratic-collision-conditioning.md) §4 同一递归满射及取伴随计算，准确有
$$
\boxed{V_p=(W_p^*)^{-1}.}
\tag{3.1}
$$
这个识别只用满射，不要求 $P^2\delta$ 小。

完整精确交织给
$$
\boxed{V_p\mathfrak S_{p,H}=Y_{p,H}.}
\tag{3.2}
$$
确实，若 $p\ge H$，标准 $H$ 次降阶恰杀掉高度 $r<H$ 的全部列，而在其余列上有正的非零阶乘权；$V_{p-H}$ 可逆。
$p<H$ 时两边均为完整对应层。

限制 $\mathcal U_p$ 到 $\mathfrak S_{p,H}$，记为 $\mathcal U_{p,H}$。它的像包含于 $\ker\mathcal B^H$。
完整双塔稿 §3 的两次同位删除计算，对这些高度 $r<H$ 的混合列直接给
$$
\boxed{
\|(I-Q_p)\mathcal U_{p,H}x\|^2
\le\epsilon_S\|x\|^2,
\quad
\epsilon_S=
\delta\max_{0\le r\le\min(p,H-1)}
[4r(p-r)+r(r-1)]
\le4\delta Hp.
}
\tag{3.3}
$$
这已经包含不同输入出生之间的交叉项，不是逐列范数界。

## 4. 真短旗投影的双碰撞费用

当 $p\ge H$，在第 $p$ 个玻色层中置
$$
\mathcal R=(\mathcal B^*)^H\mathcal H_{p-H}.
$$
引理 2.1 给这个完整像上的相对碰撞界
$$
\|(I-Q_p)y\|^2\le\epsilon_R\|y\|^2
\quad(y\in\mathcal R),
$$
$$
\epsilon_R=\delta[4H(p-H)+H(H-1)]\le4\delta Hp.
\tag{4.1}
$$
所以 $Q_p|_{\mathcal R}$ 下方有界，平方常数至少 $1-\epsilon_R$。
准确的创建投影身份还给
$$
Q_p\mathcal R=\operatorname{Ran}(D^*)^H
=Y_{p,H}^{\perp}\cap\mathcal H_p=:Z.
\tag{4.2}
$$
最后一个等式使用完整 $D^H$ 满射，从而其伴随像闭。

若 $u=\mathcal U_{p,H}x$，则 $u\in\ker\mathcal B^H$，因而 $u\perp\mathcal R$。
对任意 $y\in\mathcal R$，保留两个真实碰撞项后，
$$
\langle Q_pu,Q_py\rangle
=-\langle(I-Q_p)u,(I-Q_p)y\rangle.
$$
结合 (3.3)、(4.1) 与
$\|y\|\le(1-\epsilon_R)^{-1/2}\|Q_py\|$，得到
$$
\boxed{
\|P_ZQ_pu\|^2
\le\frac{\epsilon_S\epsilon_R}{1-\epsilon_R}\|x\|^2.
}
\tag{4.3}
$$
这就是不能免费删除的真实短旗正交投影成本。

令
$$
\widetilde W_{p,H}=P_{Y_{p,H}}W_p|_{\mathfrak S_{p,H}}
=P_{Y_{p,H}}Q_p\mathcal U_{p,H}.
$$
两次正交分解及 (4.3) 给
$$
\boxed{
\left(1-\frac{\epsilon_S}{1-\epsilon_R}\right)I
\preceq\widetilde W_{p,H}^*\widetilde W_{p,H}
\preceq I.
}
\tag{4.4}
$$
若 $p<H$，没有高创建像，直接取 $Z=0$、$\epsilon_R=0$，同一结论成立。

由 (3.1)--(3.2)，$V_{p,H}$ 已经是到 $Y_{p,H}$ 的同构，且
$$
\widetilde W_{p,H}^*V_{p,H}=I.
$$
因此
$$
\boxed{\widetilde W_{p,H}=(V_{p,H}^*)^{-1}.}
\tag{4.5}
$$
这付清了短映射的满射和真实最小逆身份，不从无限维下方有界擅自推出满射。
由 (4.4)--(4.5)，
$$
I\preceq V_{p,H}^*V_{p,H}
\preceq\frac{1-\epsilon_R}{1-\epsilon_R-\epsilon_S}I.
$$
最后用 $\epsilon_R,\epsilon_S\le\epsilon<1/2$ 即得 (1.3)。

## 5. 原实际源及所有未来层的联合旗投影

现在应用于两个原实际边界之一，沿用
[R239 联合核短塔](R239-appendix-short-flag-towers-and-near-linear-nonvacuum-prefix-removal.md) §§5–6 的同一源和已付 carry。
写
$$
L_m=A_m+D_m,\quad d=2^m,\quad A_m^d=0,\quad\|A_m\|\le6,
\quad\|L_m-T\|\le26\eta_{m-1},\quad\eta_{m-1}\le e^{-80d^4}.
$$
取原合法 $4d\le q\le e^{d^3/4}$、$w\in M=\ker T$。
原低输出 $v=v_{m,q}(w)$ 和实际源 $r_q=L_mv$ 满足
$$
D_m^dv=0,\qquad
\|v-P_{\le q}^{(m)}w\|\le e^{-74d^4}\|w\|,
\qquad P_{\le q-1}^{(m)}L_mv=0.
\tag{5.1}
$$

取 $0\le s\le q/2$、$n=q-s$、$J=m+2n$，保留旧原始前缀投影 $\mathcal P_n$，其范数
$C_n\le e^{2/(m+1)}$。去掉其单位 $n$ 孔前缀，写
$$
v^\circ=\mathcal P_nv,\qquad w^\circ=\mathcal P_nw,
\qquad L_m=A_m+D_J,\qquad P=s+d-1.
$$
于是 $v^\circ$ 支撑在远尾孔数 $\le s$，并属于 $\ker D_J^d$。

还必须支付真实未来的旗条件。
[R271 联合旗预算 §5](R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)
在同一原 $q$ 的辅助窗口内给实际 $\widehat v$，满足
$$
D_m^d\widehat v=0,\qquad
\|\widehat v-P_{\le q+d}^{(m)}w\|
\le e^{-74d^4}\|w\|.
\tag{5.2}
$$
这里没有把 $q+d$ 另当作满足原外观上界的参数；沿用的正是原稿已经核验的 $R\le2048q^2$、$\log(2+R)\le d^3$ 辅助窗口。

前缀投影与纯删除相容且保总孔数。令 $\Pi_d$ 为远尾 $\ker D_J^d$ 的真正正交投影，按孔层分解，并置
$$
u=\Pi_d P_{\le P}^{(J)}w^\circ.
$$
将 (5.2) 乘同一前缀投影并取一次正交最佳逼近，得到
$$
\boxed{
\|u-P_{\le P}^{(J)}w^\circ\|
\le C_ne^{-74d^4}\|w\|.
}
\tag{5.3}
$$
又因 $v^\circ\in\ker D_J^d$，(5.1) 给
$$
\|v^\circ-P_{\le s}^{(J)}u\|
\le C_ne^{-74d^4}\|w\|.
\tag{5.4}
$$

在输出层 $0,\ldots,P-1$，直接加减真实 $w^\circ$，而不与 $D_J$ 交换投影，令
$$
e_p=A_mu_p+D_Ju_{p+1}.
$$
由于 $A_m$ 作用于头、$D_J$ 降低核阶，$e_p$ 确属于对应的 $\ker D_J^d$。
真实方程 $(A_m+D_J)w^\circ=\mathcal P_n(L_m-T)w$、
$\|D_J\|\le1$ 及 (5.3) 给全部层的一次估计
$$
\boxed{
\|e\|\le C_n(26\eta_{m-1}+7e^{-74d^4})\|w\|.
}
\tag{5.5}
$$
系数七来自 $\|A_m\|+\|D_J\|\le7$。这明确支付真实旗投影残量，没有假设 $\Pi_dD_J=D_J\Pi_d$。

## 6. 同一短塔中的完整核延伸和实际费用

对原远尾 $D_J$，有 $\delta_J\le3/(J+1)$。
应用定理 1.1，取 $H=d$ 和 $P=s+d-1$。只须
$$
\boxed{
\epsilon\le\frac{12d(s+d-1)}{m+2(q-s)+1}\le\epsilon_0<1/2.
}
\tag{6.1}
$$
则全部短塔和其正交直和都满足
$$
\|V\|\le\kappa_0:=
\sqrt{\frac{1-\epsilon_0}{1-2\epsilon_0}},
\qquad\|V^{-1}\|\le1.
\tag{6.2}
$$

将 $v^\circ$ 与 $u$ 写入这些相同的短坐标。
坐标由出生 $b$、高度 $0\le t<d$ 标记，物理远尾孔数为 $b+t$。
低部精确方程给，对 $b\le s$，
$$
x_{b,t}=\frac{(-A_m)^t x_{b,0}}{\sqrt{t!S_J^t}}
\quad(b+t\le s).
$$
令所有 $b\le s$ 的列继续到 $t=d-1$，其余列为零，记所得向量为 $z$。
由 $A_m^d=0$ 和原 canonical 塔的精确交织，推回原范数、补回前缀所得 $k$ 满足
$$
L_mk=0,\qquad D_m^dk=0,\qquad
P_{\le q}^{(m)}k=\mathcal P_nv.
$$
于是 $c=\mathcal P_nv-k$ 是同一实际源的完整合法修复：
$$
\boxed{
L_mc=\mathcal P_nr_q,\quad
c\in\operatorname{Ran}\mathcal P_n
 \cap\mathcal H_{[q+1,q+d-1]}^{(m)},\quad D_m^dc=0.
}
\tag{6.3}
$$

另一方面，$u$ 的短坐标 $y=V^{-1}u$ 满足
$$
A_my_{b,t}+\sqrt{(t+1)S_J}\,y_{b,t+1}
=\widetilde e_{b,t},\qquad\|\widetilde e\|\le\|e\|.
$$
由 (5.4)，所有初始坐标 $x_{b,0}$ 和 $y_{b,0}$ 的平方和误差至多
$C_ne^{-74d^4}\|w\|$。
同一三角递推的范数由
$$
\Gamma_d=d6^dS_J^{-d/2}
\le d54^dq^{3d/2}\le e^{d^4}
$$
支付；不同出生按外部正交直和一次计入。
因此 $z$ 与保留 $b\le s$ 的真实未来坐标的误差至多
$$
C_n\Gamma_d(26\eta_{m-1}+8e^{-74d^4})\|w\|.
$$
推回原空间只乘固定 $\kappa_0$。该出生投影与孔层投影交换，且 $u$ 是真实 $w^\circ$ 的正交短旗投影，故
$$
\boxed{
\|c\|\le\kappa_0 C_n
\|P_{[q+1,q+d-1]}^{(m)}w\|
 +e^{-71d^4}\|w\|
}
\tag{6.4}
$$
对充分大的合法全整数头成立。最后的固定常数由剩余指数余量吸收。
这一步保留同一个真实未来源、真正旗投影、原 Hilbert 范数及原宽 $d$，没有把短塔用作未知 $W$ 上的免费不变变换。

## 7. 原 q/d 末段的整体消去

采用旧全整数头
$$
m(q)=\max\left\{5,\left\lceil
\frac{\log(4\log(q+2))}{3\log2}\right\rceil\right\},
\qquad d(q)=2^{m(q)}=\Theta((\log q)^{1/3}).
$$
任选固定 $0<c_0<1/12$，置
$$
\boxed{s(q)=\left\lfloor\frac{c_0q}{d(q)}\right\rfloor.}
\tag{7.1}
$$
此时 $s/q\to0$、$J=m+2(q-s)\sim2q$，而 (6.1) 中的右端趋于 $6c_0<1/2$。
选择任意固定 $6c_0<\epsilon_0<1/2$，则 (6.4) 对全部充分大的整数 $q$ 成立。
所以对每个真正 $w\in M$，
$$
\boxed{
\|c_q\|\le\kappa_0 C_{q-s(q)}\tau_q(w)
 +e^{-71d(q)^4}\|w\|\longrightarrow0.
}
\tag{7.2}
$$
有界条件数已经足够；不需要对未知向量的 $\tau_q(w)$ 假设任何收敛速度。

旧完整原始配对分解仍有
$$
\mathcal P_{q-s(q)}=T_\infty+\sum_{i=q-s(q)+1}^{q}T_i.
$$
将其完整分析界一次用于 (6.3)，得到
$$
\boxed{
\mu_\infty^{[\ell]}(r_q)^2+
\sum_{i=q-s(q)+1}^{q}\mu_i^{[\ell]}(r_q)^2
\le A_q^2\|c_q\|^2\longrightarrow0
\qquad(\ell\ge d(q)).
}
\tag{7.3}
$$
对原宽或已定义双宽的真正最小修复，还满足
$$
\left|\|F_\ell^\dagger r_q\|
-\|F_\ell^\dagger(I-\mathcal P_{q-s(q)})r_q\|\right|
\le\|c_q\|\longrightarrow0.
$$
新窗口 $s(q)\asymp q/d(q)$ 严格大于旧短塔的
$q/[128(d(q)+1)]^{d(q)+4}$；扩大来自真正短旗投影的双碰撞预算和准确 canonical 双塔，不是删除受限伴随项。

## 8. 保留的缺口

新消去窗口占全部分支的比例仍为 $\Theta(1/d(q))\to0$。
早期 $q-\Theta(q/d(q))$ 个分支的总能量、原实际高孔窄源的完整三 Gram 比较和无权 $N=M$ 仍未获得。
本稿不声称原缺陷空间 $W$ 被各分支或各局部投影保持，也没有将条件数有界改写成未知正规见证的非零锚。
一般正常湮灭者和普通 Hilbert ISP 继续开放。

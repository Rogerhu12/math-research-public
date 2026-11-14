# 原最小修复的有限链 Gram、准确 Schur 补与全整数带能量

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：下述恒等式与不等式已证明；原无权 $N=M$ 仍开放。

本稿使用[原线性全整数窗口](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)的相同 $v_{m,q},r_{m,q},\lambda_q$，把最小修复量写成实际正 Gram 的逆，并保留原输入的窄带能量，而不是统一换成整个尾范数。所有有限链都在完整尾孔层上定义，位置可以无限远。

## 1. 有限链与对整个源层的满射

固定 $m\ge5$、$d=2^m$ 和合法的有限 $q$。简写
$$
A=A_m,\qquad D=D_m,\qquad L=A+D,\qquad A^d=0.
$$
$A$ 只作用原有限头，$D$ 严格降低一个尾孔，且两者交换。令
$$
\mathscr C=\bigoplus_{t=1}^d\mathcal H_{q+t}^{(m)}.
$$
把 $c\in\mathscr C$ 写成 $c=(c_1,\ldots,c_d)$，对应原向量 $\sum_tc_t$。定义有界内部输出算子
$$
S c=
(Ac_1+Dc_2,\ Ac_2+Dc_3,\ldots,
Ac_{d-1}+Dc_d,\ Ac_d)
$$
到 $\bigoplus_{t=1}^d\mathcal H_{q+t}^{(m)}$，以及
$$
\mathscr K=\ker S,\qquad
F:\mathscr K\to\mathcal H_q^{(m)},\quad Fc=Dc_1.
\tag{1.1}
$$
这里 $\mathscr K$ **没有附加** $D^dc=0$ 条件。

R254J 的同一有限源层相容族给
$$
\mathcal R r=\sum_{j=0}^{d-1}(-A)^jR_{j+1}r,
\qquad (A+D)\mathcal Rr=r
\quad(r\in\mathcal H_q^{(m)}).
$$
第 $j$ 项恰在第 $q+j+1$ 层，所以 $\mathcal Rr\in\mathscr K$ 且
$$
F\mathcal R=I_{\mathcal H_q^{(m)}}.
\tag{1.2}
$$
因此这个未加高阶核约束的 $F$ 对**全部**源层满射。

固定 $m,q$ 时 $\mathcal R$ 有界，常数可以依赖 $q$。例如，取 R254J 对本稿线性模型的参数
$$
R=512\sqrt{q+d+1}(m+q+d+2)^{3/2}.
$$
完整 $q$ 层属于 $\ker D^{q+1}$，所以已有界
$\|R_tf\|\le(2R)^{q+t}\|f\|$ 给
$$
\|\mathcal R\|\le
\Gamma_{m,q}:=d\,6^{d-1}(2R)^{q+d}<\infty.
\tag{1.3}
$$
本节没有把这个常数说成对所有 $q$ 一致。

## 2. 只有实际残量才自动满足高阶核约束

现在取真实 $w\in M=\ker T$ 的低方程正交投影 $v=v_{m,q}$，令
$$
r=Lv=A v_q\in\mathcal H_q^{(m)}.
$$
已有准确身份为
$$
D^kr=(-1)^kA^{k+1}v_{q-k}\qquad(0\le k<d).
\tag{2.1}
$$

若 $c\in\mathscr K$、$Fc=r$，链方程给
$$
Dc_1=r,\qquad Dc_t=-Ac_{t-1}\quad(2\le t\le d).
$$
因为 $D$ 与 $A$ 交换，对每个 $1\le t\le d$，
$$
D^dc_t=(-A)^{t-1}D^{d-t}r
=(-1)^{d-1}A^dv_{q-d+t}=0.
\tag{2.2}
$$
所以，对这个**实际特殊残量**，$D^dc=0$ 自动成立。

于是原稿定义的闭仿射修复集，准确等于
$$
\{c\in\mathscr K:Fc=r\}.
\tag{2.3}
$$
对任意其他 $r\in\mathcal H_q$，(2.2) 不自动成立；不得把加了 $D^d$ 核约束的映射也宣布为全源层满射。

## 3. 实际正 Gram 与最小能量的准确公式

记
$$
D_0^*y=(D^*y,0,\ldots,0)\in\mathscr C,
$$
并用 $P_{\mathscr K}$ 表示原 Hilbert 正交投影。由 (1.1)，
$$
F^*y=P_{\mathscr K}D_0^*y.
$$
因此实际源层上的正 Gram 为
$$
\boxed{
\mathsf G_{m,q}=FF^*
=D_0P_{\mathscr K}D_0^*.
}
\tag{3.1}
$$
(1.2)–(1.3) 使它严格正且有界可逆。确实，
$$
\|y\|^2=\langle F^*y,\mathcal Ry\rangle
\le\Gamma_{m,q}\|F^*y\|\|y\|,
$$
故
$$
\boxed{\mathsf G_{m,q}\ge\Gamma_{m,q}^{-2}I.}
\tag{3.2}
$$

对 (2.1) 的实际残量，唯一最小修复是
$$
\boxed{
c^{\min}=F^*\mathsf G_{m,q}^{-1}r,\qquad
\lambda_{m,q}(w)^2
=\langle\mathsf G_{m,q}^{-1}r,r\rangle.
}
\tag{3.3}
$$
证明：$Fc^{\min}=r$；它属于 $\operatorname{Ran}F^*=(\ker F)^\perp$，所以与所有其他解之差正交，确为唯一最小元。由 §2，它也满足原附加高阶核条件。

## 4. 分母是有限伴随链的最小能量

令
$$
\mathcal E_{m,q}(y)=\|P_{\mathscr K}D_0^*y\|^2
=\langle\mathsf G_{m,q}y,y\rangle.
$$
因 $(\ker S)^\perp=\overline{\operatorname{Ran}S^*}$，准确有
$$
\boxed{
\begin{aligned}
\mathcal E_{m,q}(y)
=\inf_{z_1,\ldots,z_d}\biggl[
&\|D^*y-A^*z_1\|^2\\
&+\sum_{t=2}^d
 \|D^*z_{t-1}+A^*z_t\|^2
\biggr],
\end{aligned}
}
\tag{4.1}
$$
其中 $z_t\in\mathcal H_{q+t}^{(m)}$。这是到 $\operatorname{Ran}S^*$ 的距离；本文只使用 inf，不假定该像闭或极小值总由某个 $z$ 取得。

于是
$$
\boxed{
\lambda_{m,q}(w)^2
=\sup_{y\ne0}
 \frac{|\langle r,y\rangle|^2}
      {\mathcal E_{m,q}(y)}.
}
\tag{4.2}
$$
分母由 (3.2) 对每个固定 $m,q$ 严格为正。最优方向可以取 $y=\mathsf G_{m,q}^{-1}r$（$r=0$ 时两边都为零）。

环境创建范数只给
$\mathcal E_{m,q}(y)\le\|D^*y\|^2$，因为 (4.1) 可取 $z=0$。因此任何仅关于 $\|D^*y\|$ 或环境 $D^*D+DD^*$ 的下界，都不能替代对 (4.1) 这个被压缩后的能量的下界。

## 5. 不能直接扔掉与残量正交的头方向

由于 $r=A v_q$，它在源层属于
$$
\mathscr V=\operatorname{Ran}(A\otimes I),
\qquad
\mathscr V^\perp=\ker(A^*\otimes I).
$$
$A$ 是有限矩阵，所以 $\mathscr V$ 闭。相对于
$\mathscr V\oplus\mathscr V^\perp$，把 (3.1) 写成
$$
\mathsf G=
\begin{pmatrix}
G_{11}&G_{12}\\
G_{21}&G_{22}
\end{pmatrix}.
$$
(3.2) 使 $G_{22}$ 有界可逆。对 $y\in\mathscr V$，虽然加上任意
$h\in\mathscr V^\perp$ 不改变 $\langle r,y\rangle$，却会改变分母。正确消元为
$$
\inf_{h\in\mathscr V^\perp}
\mathcal E(y+h)
=
\left\langle
\left(G_{11}-G_{12}G_{22}^{-1}G_{21}\right)y,y
\right\rangle.
\tag{5.1}
$$
因此
$$
\boxed{
\lambda^2=
\left\langle
\left(G_{11}-G_{12}G_{22}^{-1}G_{21}\right)^{-1}r,r
\right\rangle.
}
\tag{5.2}
$$
这是真正 Schur 补，不能只用可见块 $G_{11}$。

一个纯有限维校准说明差别：对 $0<\varepsilon<1$，
$$
G=\begin{pmatrix}1&\sqrt{1-\varepsilon}\\
\sqrt{1-\varepsilon}&1\end{pmatrix},\qquad r=(1,0),
$$
可见块恒为 $1$，但 Schur 补为 $\varepsilon$，
$\langle G^{-1}r,r\rangle=\varepsilon^{-1}$。这仅是投影推理的校准，不声称该矩阵已经在实际模型实现，也不推出原最小能量发散。

## 6. 保留原输入窄带后的全整数能量上界

现在取全整数稿的
$$
m(q)=\max\!\left(5,
\left\lceil\frac{\log(4\log(q+2))}{3\log2}\right\rceil\right),
\quad d_q=2^{m(q)},\quad
\ell_q=d_q+m(q),\qquad q\ge128.
$$
简写其实际修复指数为 $F_q=F(m(q),q)$，
并令 $\lambda_q=\lambda_{m(q),q}(w)$。

原修复估计实际上保留尾孔窄带，而非必须换成整个尾：
$$
\lambda_q\le e^{F_q}
\left(\beta_q+e^{-74d_q^4}\|w\|\right),
\quad
\beta_q=
\left\|\mathbf1_{\{q-d_q+1\le\mathcal N\le q+m(q)\}}w\right\|.
\tag{6.1}
$$
因为尾孔落在 $[q-d_q+1,q]$ 时，加上原头孔数至多 $m(q)$，原全部孔数必落入这里的窗口；低投影误差仍为 $e^{-74d_q^4}\|w\|$。

这些双侧窗口记为
$$
J_q=[q-d_q+1,q+m(q)].
$$
它们有准确统一覆盖界
$$
\boxed{
\sum_{\substack{q\ge128\\p\in J_q}}\ell_q^{-1}\le4
\qquad\text{对每个孔次数整数 }p.
}
\tag{6.2}
$$
证明：$q\ge4d_q$、$m(q)\le d_q/2$，故
$p\in J_q$ 时 $3q/4<p\le9q/8$。当 $p,q\ge128$ 时，其比值小于2，使 $|m(p)-m(q)|\le1$，从而
$d_q\le2d_p$、$\ell_q\ge\ell_p/2$。
候选 $q$ 必满足
$p-m(p)-1\le q\le p+2d_p-1$，
个数至多 $2d_p+m(p)+1\le2\ell_p$，得到4。
$p<128$ 的可能窗口全部具有 $m(q)=5$，直接计数给同一界。

此外，当 $q\ge Q\ge128$，窗口 $J_q$ 的最低孔数至少为
$Q-2d_Q+1$。对 $Q\le q\le2Q$，使用 $d_q\le2d_Q$；对 $q>2Q$，使用 $q-d_q\ge3q/4>Q$。于是
$$
\sum_{q\ge Q}\frac{\beta_q^2}{\ell_q}
\le4\tau_{Q-2d_Q}(w)^2.
\tag{6.3}
$$

按相同 $m(q)$ 分组，每组整数个数至多 $e^{d^3/4}$，所以
$$
\sum_{q\ge Q}\frac{e^{-148d_q^4}}{\ell_q}
\le\sum_{m\ge m(Q)}e^{d^3/4-148d^4}
\le2e^{-147d_Q^4}.
\tag{6.4}
$$
(6.1) 平方后用 $(x+y)^2\le2x^2+2y^2$，遂得
$$
\boxed{
\sum_{q\ge Q}\frac{e^{-2F_q}\lambda_q(w)^2}{\ell_q}
\le
8\tau_{Q-2d_Q}(w)^2
+4e^{-147d_Q^4}\|w\|^2.
}
\tag{6.5}
$$
这是全部窗口的实际最小能量上界；仅用原稿的整个尾估计不能直接给这个可和结论。

## 7. 真缺陷的两侧能量共同约束

若 $0\ne w\in M\ominus N$，原全整数稿对充分大的 $Q$ 给
$$
\sum_{q\ge Q}\frac1{\ell_q\lambda_q(w)^2}
\le\frac{8\tau_Q(w)^2}{\|w\|^4}.
\tag{7.1}
$$
此时全部足够大的 $\lambda_q$ 非零。将 (6.5)、(7.1) 对有限部分和作 Cauchy--Schwarz，再单调取极限，得到
$$
\boxed{
\begin{aligned}
\tau_Q(w)^2\left[
\tau_{Q-2d_Q}(w)^2+
\tfrac12e^{-147d_Q^4}\|w\|^2
\right]
\ge
\frac{\|w\|^4}{64}
\left(\sum_{q\ge Q}\frac{e^{-F_q}}{\ell_q}\right)^2.
\end{aligned}
}
\tag{7.2}
$$
标量级数收敛，因为 $F_q=(K_*+o(1))(\log q)^{4/3}$、$K_*>0$。这保留全整数窗口带来的共同约束，没有只取一个 $q$。

但是 (6.5) 与 (7.2) 仍允许慢 Hilbert 尾；它们没有证明
$\sum_q[\ell_q(1+\lambda_q^2)]^{-1}$ 发散。当前需要在 (4.1) 或实际 Schur 补 (5.1) 中利用真实残量的额外结构，获得足以控制 $\lambda_q$ 的估计。全空间创建下界、有限头方向投影和任意原像范数都不能代替这个未证步骤。

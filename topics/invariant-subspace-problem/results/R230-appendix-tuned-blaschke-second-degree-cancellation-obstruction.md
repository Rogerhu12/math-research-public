# R230 附录：调块一次 Gram 修复后的真实二次消去障碍

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065。

**状态：完整证明的中间结论。** 对《一次层可调 Gram 的近临界 Blaschke 强单位》构造的同一实际 $P$ 和同一正常正秩一态 $\phi_f$，证明 R244 聚合界在次数至多二的有限 Walsh 列上已经失败。所有逆源、强单位、块参数和物理位置保持不变。一次层成功与二次层失败同时成立。

本稿接[同一实际一次Gram构造](../results/R230-appendix-tuned-blaschke-first-layer-gram-and-vacuum-strong-units.md)，原完整源为 cb42f4c1ce3bf5d60a77d665ce7c7ee651809384。以下重列全部使用的量词，不要求先把实际提升当作纯有理函数。

## 1. 固定构造

沿用
$$
q_i=2^{4i},\quad Q_i=q_i+2,\quad
c_i=2^{-i-2},\quad
\delta_i=\delta_*2^{-i},\quad
0<\delta_*\le\frac{(1/256)^2}{64}.
$$
在已选实际互不交块 $B_i$ 上，$i\ge i_0$，纯对象为
$$
L_i=\sum_{j\in B_i}D_j,\qquad
T_i=\frac{q_iI-L_i}{Q_i}
=\frac2{Q_i}\sum_{j\in B_i}E_j,
$$
$$
\frac25\le a_i\le\frac34,\qquad
U_i=(I+a_iT_i)(a_iI+T_i)^{-1},\qquad
g_i=U_i\Omega,
$$
$$
\|g_i\|^2=1+\delta_i,\qquad
|\langle g_i,\Omega\rangle-1|\le20/q_i,\qquad
\|\Pi_{1\le\mathsf N\le q_i/256}g_i\|\le4/\sqrt{q_i}.
\tag{1.1}
$$
所有 $q_i\ge2^{16}$，有限个不满足条件的初块已被排除在正则因子外。

实际提升和正缩放为
$$
\widetilde U_i=X_{g_i}/(1-\varepsilon_i),\qquad
\varepsilon_i=\delta_i^2,\qquad
\widetilde g_i=g_i/(1-\varepsilon_i),
$$
并已通过物理远置保证
$$
16q_i5^{q_i}\eta_{r_i}\le\varepsilon_i,
\qquad r_i=\min B_i.
\tag{1.2}
$$
实际收缩逆的乘积强趋于 $P$，准确有
$$
g=\prod_{i\ge i_0}\widetilde g_i,\qquad
\|g\|<2,\qquad Pg=1,\qquad
G=P^{-1}=X_g.
\tag{1.3}
$$
这里 $G$ 的有限 Walsh 图核心和同组收缩强单位均已由前稿证明。

同一个固定正常态为
$$
f=1+\sum_{i\ge1}c_i\chi_{B_i},\qquad
\phi_f(F)=\langle Ff,f\rangle,\qquad
\lambda=\|f\|^2=49/48.
\tag{1.4}
$$
特别
$$
c_i^2\sqrt{q_i}=\frac1{16}.
\tag{1.5}
$$

## 2. 一个准确次数至多二的有限列

对每个 $i\ge i_0$ 定义纯有限向量
$$
u_i=\frac{(a_iI+T_i)L_i\Omega}{\sqrt{q_i}}.
\tag{2.1}
$$
这里只用纯算子定义有限 Walsh 系数。随后始终通过实际 $X_{u_i}$ 计算真实矩和真实逆。

因为
$$
L_i\Omega=\sum_{j\in B_i}\chi_j,\qquad
L_i^2\Omega=-q_i\Omega+
2\sum_{j\in B_i}\chi_j+
2\sum_{\substack{j<k\\j,k\in B_i}}\chi_{\{j,k\}},
$$
所以 (2.1) 的完整展开为
$$
\boxed{
u_i=
\frac{\sqrt{q_i}}{Q_i}\Omega+
\frac{a_i+(q_i-2)/Q_i}{\sqrt{q_i}}
 \sum_{j\in B_i}\chi_j
-\frac{2}{Q_i\sqrt{q_i}}
 \sum_{\substack{j<k\\j,k\in B_i}}\chi_{\{j,k\}}.
}
\tag{2.2}
$$
因而 $u_i$ 确切属于次数至多二的有限层，且
$$
\|u_i\|\le a_i+\|T_i\|\le7/4.
$$

纯有限代数给
$$
X_{u_i}^0=(a_iI+T_i)L_i/\sqrt{q_i}.
$$
使用 $U_i$ 的真实有限维预解式恒等式，分母准确消去：
$$
\boxed{
U_i u_i=y_i:=
\frac{(I+a_iT_i)L_i\Omega}{\sqrt{q_i}},
\qquad \|y_i\|\le7/4.
}
\tag{2.3}
$$
$y_i$ 仍具有次数至多二，真空系数为
$$
\langle y_i,\Omega\rangle=a_i\sqrt{q_i}/Q_i.
\tag{2.4}
$$

## 3. 这些真实逆像有统一 $\ell^2$ 合成界

记
$$
\widetilde y_i=y_i/(1-\varepsilon_i),\qquad
v_i=\widetilde y_i\otimes g_{\mathrm{outside}\ B_i}.
$$
(2.3) 和准确源乘积给
$$
v_i=X_{u_i}^0g.
\tag{3.1}
$$

置
$$
\mu_i=
\frac{\langle\widetilde y_i,\widetilde g_i\rangle}
{\|\widetilde g_i\|^2}
=\frac{\langle y_i,g_i\rangle}{1+\delta_i},
\qquad
z_i=\widetilde y_i-\mu_i\widetilde g_i.
$$
由 (1.1)、(2.4)，
$$
|\langle y_i,g_i\rangle|
\le \frac{(3/4)\,2}{\sqrt{q_i}}
+\frac74\frac4{\sqrt{q_i}}
\le\frac9{\sqrt{q_i}},
\qquad
|\mu_i|\le\frac9{\sqrt{q_i}}.
\tag{3.2}
$$
而
$$
\frac{\|z_i\|^2}{\|\widetilde g_i\|^2}
\le
\frac{\|\widetilde y_i\|^2}{\|\widetilde g_i\|^2}
=\frac{\|y_i\|^2}{1+\delta_i}<4.
\tag{3.3}
$$

各
$z_i\otimes g_{\mathrm{outside}\ B_i}$ 彼此正交，且均与 $g$ 正交。因此任意有限系数列 $(t_i)$ 满足准确恒等式
$$
\left\|\sum_i t_iv_i\right\|^2
=\|g\|^2\left|\sum_i t_i\mu_i\right|^2
+\|g\|^2\sum_i|t_i|^2
 \frac{\|z_i\|^2}{\|\widetilde g_i\|^2}.
$$
因 $\sum_{i\ge1}q_i^{-1}=1/15$，得到安全界
$$
\boxed{\left\|\sum_i t_iv_i\right\|\le8\|(t_i)\|_2.}
\tag{3.4}
$$
这支付了不同块的全部干涉，不是逐个逆像有界的替代说法。

### 实际 carry

对单点和二点分别有
$$
\|V_j-D_j\|\le8\eta_{r_i},\qquad
\|V_jV_k-D_jD_k\|\le48\eta_{r_i}
\quad(j,k\in B_i).
$$
在 (2.2) 中，一次系数绝对和至多
$(7/4)\sqrt{q_i}$，二次系数绝对和至多 $\sqrt{q_i}$。因此
$$
\boxed{
\|X_{u_i}-X_{u_i}^0\|
\le64\sqrt{q_i}\eta_{r_i}.
}
\tag{3.5}
$$
这没有把实际 $V_j^2$ 替换为纯恒等式；(2.2) 先支付真正有限列，再逐单项比较。

由 (1.2)、$\|g\|<2$，
$$
\|Gu_i-v_i\|
\le128\sqrt{q_i}\eta_{r_i}
\le8\varepsilon_i.
$$
该误差列的范数平方和小于 $1$。对其用 Cauchy–Schwarz 并结合 (3.4)，得到
$$
\boxed{
\left\|G\left(\sum_i t_iu_i\right)\right\|
\le10\|(t_i)\|_2
}
\tag{3.6}
$$
对任意有限 $(t_i)$ 成立。左侧是实际最小闭逆，因为每个输入都是其已证图核心里的有限 Walsh 列。

## 4. 同一正常态在每个列上的矩保持非零

纯模型里，对 $j\ne k$ 同在 $B_i$，准确有
$$
\langle D_jf,f\rangle=2c_i^2,\qquad
\langle D_jD_kf,f\rangle=4c_i^2.
\tag{4.1}
$$
因为所有 $|B_\ell|>2$，次数至多二的列不会把真空与某个完整 $\chi_{B_\ell}$，或两个不同完整块，互相连接。因此将 (2.2) 逐项代入，得到
$$
\begin{aligned}
\phi_f(X_{u_i}^0)
&=\lambda\frac{\sqrt{q_i}}{Q_i}
+c_i^2\sqrt{q_i}
 \left[2(a_i-1)+\frac4{Q_i}\right]\\
&=\lambda\frac{\sqrt{q_i}}{Q_i}
+\frac1{16}
 \left[2(a_i-1)+\frac4{Q_i}\right].
\end{aligned}
\tag{4.2}
$$
$ a_i\le3/4$，故主项至多 $-1/32$；而 $q_i\ge2^{16}$ 时其余两项之和小于 $1/128$。所以
$$
\phi_f(X_{u_i}^0)\le-3/128.
$$
再由 (3.5)、(1.2)，
$$
|\phi_f(X_{u_i})-\phi_f(X_{u_i}^0)|
\le64\lambda\sqrt{q_i}\eta_{r_i}<1/128.
$$
最终有统一实际界
$$
\boxed{\operatorname{Re}\phi_f(X_{u_i})\le-1/64.}
\tag{4.3}
$$

## 5. 二次层聚合常数已经发散

取前 $n$ 个已选块的有限和
$$
u^{(n)}=\sum_{i=i_0}^{i_0+n-1}u_i.
$$
它仍是次数至多二的实际有限 Walsh 柱。由 (3.6) 与 (4.3)，
$$
\|Gu^{(n)}\|\le10\sqrt n,\qquad
|\phi_f(X_{u^{(n)}})|\ge n/64.
$$
所以
$$
\boxed{
\frac{|\phi_f(X_{u^{(n)}})|}{\|Gu^{(n)}\|}
\ge\frac{\sqrt n}{640}\longrightarrow\infty.
}
\tag{5.1}
$$
R244 聚合界已经在完整次数至多二的有限列上失败。因此该同一 $P$ 不产生
$\phi_f(F)=B(Fg,h)$ 的全列表示。因 $Cf=f$，R244 逐输入充分条件还给
$$
\boxed{Pf\notin\operatorname{Dom}X_f.}
\tag{5.2}
$$

结论对前稿所有满足所列区间、范数调节和 carry 预算的参数选择均成立。它不是因一次层 Gram 漏算；前稿的一次成功保持有效。真正的新障碍是：每块逆的线性分母可以与一个一次列相乘，形成真实二次列，将逆放大准确消去，而固定正常态在该列上的矩仍不消失。

当前没有把这个非湮灭态当作慢主理想见证，也没有由该障碍否定更复杂的见证专属正则器。多个分母、跨块高阶设计或非真空第一因子的完整聚合控制仍需新证明；普通 Hilbert ISP 保持开放。

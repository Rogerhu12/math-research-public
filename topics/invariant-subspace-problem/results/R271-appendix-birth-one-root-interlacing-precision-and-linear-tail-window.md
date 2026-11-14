# R271 附录：导数根交错、出生一的线性高度窗口与真实相邻精度

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_rebuild。
状态：已证明。此稿加强[稀散出生一全部低高度稿](R271-appendix-dilute-birth-one-all-height-precision-and-square-root-window.md)，把原完整尾的统一渐近窗口从 $o(\sqrt m)$ 扩为 $o(m)$，并支付高度与 $m$ 成固定比例时的显式有界比较。

## 1. 同一完整最小逆和结论

保留前稿的全部对象：有限正行或无限正 $\ell^2$ 行 $a$，归一化
$$
\sum_i a_i^2=1,\qquad z_i=a_i^2,\qquad\delta=\max_i z_i,
\qquad K_1=a^\perp.
$$
完整孔层 Gram、先求逆再压缩及其真实精度为
$$
F_r=\frac{D^r(D^*)^r}{(r!)^2}\bigg|_{\mathcal H_1},
\qquad \Gamma_r=P_{K_1}F_r^{-1}|_{K_1},
\qquad C_{r+1}|_{K_1}=\Gamma_r^{-1}.
\tag{1.1}
$$
前稿 §§1–2 已从完整矩阵给出有界逆、真实 Schur 补及图形式，包含无限行的 Fredholm 与无核证明；这里不改变任何空间或源。

固定 $h\ge2$。本稿只要求
$$
\boxed{(h+1)\delta<1.}
\tag{1.2}
$$
在有限行中，(1.2) 自动保证位数 $N\ge h+2$，所以所有完整逆均存在。
记
$$
\boxed{
U_r=\frac{1-\delta}{(1-r\delta)(1-(r+1)\delta)}
\quad(0\le r\le h),
}
\tag{1.3}
$$
其中 $U_0=1$。

**定理。** 整个同一 $K_1$ 上同时有
$$
\boxed{
e_rU_r^{-2}I_{K_1}
\preceq\Gamma_r^{-1}
\preceq e_rU_r I_{K_1}
\qquad(0\le r\le h).
}
\tag{1.4}
$$
真实第一下降的相邻最优常数 $\mathsf C_h(D;1)$ 满足
$$
\boxed{
\frac h{h-1}\frac{1-(h-1)\delta}
 {(U_hU_{h-1}U_{h-2})^2}
\le\mathsf C_h(D;1)
\le\frac h{h-1}U_hU_{h-2}U_{h-1}^4.
}
\tag{1.5}
$$
特别，
$$
\boxed{
\frac h{h-1}
 \exp\!\left(-\frac{13(h-1)\delta}{1-(h+1)\delta}\right)
\le\mathsf C_h(D;1)
\le\frac h{h-1}
 \exp\!\left(\frac{13(h-1)\delta}{1-(h+1)\delta}\right).
}
\tag{1.6}
$$
这不是环境 Gram 的对数凹断言。每个 $C_{r+1}$ 始终是完整 Schur 后的真精度。

## 2. 导数根交错给相邻对称和比值的单步界

对任意有限正行 $z$，总和为 $S$、最大项至多 $\delta$，令
$$
q_r=\frac{r e_r}{e_{r-1}}\qquad(r\ge1),
$$
只在相应分母正的阶数使用。允许顶阶下一项为零。
前稿的直接集合求和式给
$$
S-(r-1)\delta\le q_r\le S.
\tag{2.1}
$$
新增的准确单步界是
$$
\boxed{0\le q_r-q_{r+1}\le\delta.}
\tag{2.2}
$$

证明完全来自负根交错。置
$P(t)=\prod_i(1+z_i t)$、$Q=P^{(r-1)}$。
由 Rolle 定理，$Q$ 的每个根 $\rho_\nu$ 都是负实数，并且
$$
\rho_\nu\le-1/\delta.
$$
把重根按重数列出，记 $b_\nu=-1/\rho_\nu$，则 $0<b_\nu\le\delta$。在 $t=0$，
$$
\frac{Q'}Q=\sum_\nu b_\nu=q_r,
\qquad
\frac{Q''}{Q}=
\left(\sum_\nu b_\nu\right)^2-\sum_\nu b_\nu^2.
$$
所以
$$
\boxed{
q_r-q_{r+1}
=\frac{Q'}Q-\frac{Q''}{Q'}
=\frac{\sum_\nu b_\nu^2}{\sum_\nu b_\nu}
\in[0,\delta].
}
\tag{2.3}
$$
当 $Q$ 一次时 $Q''=0$，同式照常成立。
对无限可和行，先取有限截断，固定阶对称和及比值均收敛；(2.2) 因此同样成立。
这也适用于从原行删除任意两个固定指标后的行。

## 3. 删除一个或两个指标的相对损失

仍考虑任意总和 $S$ 的行，且 $S>(r-1)\delta$。删除一个指标 $i$ 后记 $e_r^{\lnot i}$。
从
$$
e_r=e_r^{\lnot i}+z_i e_{r-1}^{\lnot i}
$$
及删除行上的 (2.1)，得到
$$
\frac{z_i e_{r-1}^{\lnot i}}{e_r}
\le\frac{r z_i}{S+(r-1)z_i-(r-1)\delta}
\le\frac{r\delta}{S}.
\tag{3.1}
$$
最后一步的交叉相乘恰为
$(\delta-z_i)(S-(r-1)\delta)\ge0$。
故
$$
\boxed{\frac{e_r^{\lnot i}}{e_r}\ge1-\frac{r\delta}{S}.}
\tag{3.2}
$$
下文所有右侧均为正。

现在回到总和为一的原行。对 $i\ne j$ 置 $E_r=e_r(z_{\ne i,j})$。
先删除 $i$，再在总和 $1-z_i\ge1-\delta$ 的行中删除 $j$，由 (3.2) 得
$$
\begin{aligned}
\frac{E_r}{e_r}
&\ge(1-r\delta)
 \left(1-\frac{r\delta}{1-\delta}\right)\\
&=\frac{(1-r\delta)(1-(r+1)\delta)}{1-\delta}
=U_r^{-1}.
\end{aligned}
\tag{3.3}
$$
假设 (1.2) 保证两次删除所需的全部正分母；没有把条件子集分布换成独立抽样。

## 4. 全部真实图边权的两侧估计

前稿的完整 Schur 计算给
$$
\langle C_{r+1}f,f\rangle
=\sum_{i<j}g_{ij}^{(r)}|a_jf_i-a_if_j|^2,
$$
$$
g_{ij}^{(r)}
=\frac{E_r^2-E_{r-1}E_{r+1}}{e_{r+1}}.
\tag{4.1}
$$
对 $r\ge1$，Newton 不等式及 $(r+1)e_{r+1}\le e_r$ 给
$$
g_{ij}^{(r)}\ge\frac{E_r^2}{e_r}
\ge e_rU_r^{-2}.
\tag{4.2}
$$
这里正是使用 (3.3) 的地方。

为证明上界，在删除两个指标的行上写
$$
\widetilde q_r=\frac{rE_r}{E_{r-1}}.
$$
由 (2.2)，$\widetilde q_{r+1}\ge\widetilde q_r-\delta$。因此
$$
\begin{aligned}
E_r^2-E_{r-1}E_{r+1}
&=E_r^2\left(1-\frac r{r+1}
                  \frac{\widetilde q_{r+1}}{\widetilde q_r}\right)\\
&\le\frac{E_r^2}{r+1}
 \left(1+\frac{r\delta}{\widetilde q_r}\right).
\end{aligned}
\tag{4.3}
$$
删除行的总和至少 $1-2\delta$，所以 (2.1) 给
$$
\widetilde q_r\ge1-(r+1)\delta>0.
$$
再用 $E_r\le e_r$ 及全行的
$(r+1)e_{r+1}\ge(1-r\delta)e_r$，得
$$
\begin{aligned}
g_{ij}^{(r)}
&\le\frac{e_r}{1-r\delta}
 \left(1+\frac{r\delta}{1-(r+1)\delta}\right)\\
&=e_r\frac{1-\delta}{(1-r\delta)(1-(r+1)\delta)}
=e_rU_r.
\end{aligned}
\tag{4.4}
$$
$r=0$ 的完整精度是 $C_1=P_{K_1}$，与 (1.4) 一致。
由于
$$
\sum_{i<j}|a_jf_i-a_if_j|^2=\|f\|^2
\quad(f\in K_1),
$$
(4.2)--(4.4) 对整个 $K_1$ 给出 (1.4)。无限求和也被这些统一边权界控制，保持原范数。

## 5. 真正相邻、全部阶乘及统一常数

由 (1.4) 反转后的标量界，在前稿的准确相邻三 Gram 式中取
$L_r=U_r^{-2}$，就得到
$$
R_h(U_hU_{h-1}U_{h-2})^{-2}
\le\mathsf C_h(D;1)
\le R_hU_hU_{h-2}U_{h-1}^4,
$$
$$
R_h=\left(\frac h{h-1}\right)^2
\frac{e_he_{h-2}}{e_{h-1}^2}.
\tag{5.1}
$$
其中 $h^2/(h-1)^2$ 是原最小逆 $H_r=\Gamma_r/(r!)^2$ 的完整阶乘因子。
同一真实 Schur 反转保留三个一般不交换的正算子，没有把其乘积改作逐向量标量比。

Newton 与 (2.1) 给
$$
\frac h{h-1}(1-(h-1)\delta)\le R_h\le\frac h{h-1},
$$
从而得 (1.5)。
此外，(1.3) 可写成
$$
U_r=\frac1{1-r\delta}
\left(1+\frac{r\delta}{1-(r+1)\delta}\right),
$$
故对 $0\le r\le h$，
$$
\log U_r\le\frac{2r\delta}{1-(h+1)\delta}.
\tag{5.2}
$$
上界 (1.5) 的额外对数至多
$$
\frac{[2h+2(h-2)+8(h-1)]\delta}{1-(h+1)\delta}
=\frac{12(h-1)\delta}{1-(h+1)\delta}.
$$
下界的损失对数至多
$$
\frac{(h-1)\delta+4[h+(h-1)+(h-2)]\delta}
 {1-(h+1)\delta}
=\frac{13(h-1)\delta}{1-(h+1)\delta}.
$$
这证明 (1.6)。

## 6. 原完整连续尾的线性高度范围

原 $a_j=(j+1)^{-2}$、$j\ge m$，按平方和归一化后的
$\delta_m\le3/(m+1)$。因此只要 $m+1>3(h+1)$，就有
$$
\boxed{
\frac h{h-1}
 \exp\!\left(-\frac{39(h-1)}{m+1-3(h+1)}\right)
\le\mathsf C_h(D_m;1)
\le\frac h{h-1}
 \exp\!\left(\frac{39(h-1)}{m+1-3(h+1)}\right).
}
\tag{6.1}
$$
这里先用原完整固定层算子，再调用全部边权界，未作等权替换。
故对任意整数函数 $H(m)\ge2$、$H(m)=o(m)$，
$$
\boxed{
\sup_{2\le h\le H(m)}
\left|\frac{h-1}{h}\mathsf C_h(D_m;1)-1\right|
\longrightarrow0.
}
\tag{6.2}
$$
如果只要统一有界而非趋于最优值，也可让高度与 $m$ 成固定比例。
例如固定 $0<c<1/3$，在全部满足 $h+1\le c(m+1)$ 的高度上，(6.1) 给
$$
\boxed{
\mathsf C_h(D_m;1)
\le 2\exp\!\left(\frac{39c}{1-3c}\right).
}
\tag{6.3}
$$
右边不依赖 $m$ 或具体高度。

## 7. 保留的范围

本稿始终只处理出生一的整个 primitive 空间。
它没有把一般高出生源投影到 $K_1$ 后声称三个真实最小费用均不增，未给原窄源所需的高出生上界。
固定 $m$ 而高度跨过 (1.2) 的所有内部边，以及任意异权的全高度统一常数，也未由此关闭。
此前首边的更强常数、有限末边的倒数权对偶仍按原文保留。
两实际边界的无权 $N=M$、一般正常见证与普通 Hilbert ISP 继续开放。

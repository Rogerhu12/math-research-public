# R271 附录：稀散正权的出生一全部低高度精度与原尾平方根窗口

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_rebuild。
状态：已证明。下面直接控制完整最小逆压缩的真实精度，不使用有限等权池代替原尾。

## 0. 结论和范围

取任意有限正行或无限正 $\ell^2$ 行 $a=(a_i)$。共同缩放不改变真实相邻常数，故先归一化为
$$
\sum_i a_i^2=1,
\qquad z_i=a_i^2,
\qquad \delta=\max_i z_i.
$$
在原平方自由孔层上令 $D=\sum_i a_iE_i$，并始终保留整个出生一空间
$$
K_1=\ker(D:\mathcal H_1\to\mathcal H_0)=a^\perp.
$$
固定整数 $h\ge2$，假设
$$
\boxed{h^2\delta\le 1/100.}
\tag{0.1}
$$
有限行的位数自动足够：由 $1\le N\delta$ 得 $N\ge100h^2\ge h+2$。

设 $J_r:K_1\to\mathcal H_{r+1}$ 是 $D^r$ 的完整最小范数逆，$H_r=J_r^*J_r$；$J_0=I$。
沿用[有限模型与连续尾归约](R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md)的真实第一下降常数
$$
\mathsf C_h(D;1)
=\inf\{C:C H_h\succeq H_{h-1}H_{h-2}^{-1}H_{h-1}\}.
\tag{0.2}
$$
其算子定义仍是同一出生下
$A_{h+1,h+1}A_{h+1,h+1}^*\preceq C A_{h,h}^*A_{h,h}$；没有删除第二下降后再改变最小逆。

**定理。** 在 (0.1) 下，全部涉及的完整逆有界存在，并且
$$
\boxed{
\frac h{h-1}e^{-6h^2\delta}
\le \mathsf C_h(D;1)
\le \frac h{h-1}e^{6h^2\delta}.
}
\tag{0.3}
$$
下面还给出比 (0.3) 更准确的有理上下界，以及每个完整压缩逆的两侧精度界。

对原无限连续尾
$$
D_m=\sum_{j\ge m}(j+1)^{-2}E_j,
$$
归一化后有 $\delta_m\le3/(m+1)$。因此
$$
\boxed{
m+1\ge300h^2
\quad\Longrightarrow\quad
\frac h{h-1}e^{-18h^2/(m+1)}
\le\mathsf C_h(D_m;1)
\le\frac h{h-1}e^{18h^2/(m+1)}.
}
\tag{0.4}
$$
特别，对任意整数函数 $H(m)\ge2$ 且 $H(m)=o(\sqrt m)$，
$$
\boxed{
\sup_{2\le h\le H(m)}
\left|\frac{h-1}{h}\mathsf C_h(D_m;1)-1\right|
\longrightarrow0.
}
\tag{0.5}
$$
这是原完整无限尾的整个 $K_1$ 上、随 $m$ 增长的全部这些内部相邻高度。它不覆盖高出生源。
已有[出生一首边稿](R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)对 $h=2$ 给出更强的通用常数四及原尾最终严格小于二；这里的新增范围是其它高度及其统一增长窗口，不替换那些更强首边结论。

## 1. 任意固定高度的完整 Gram 和有界逆

写 $e_r=e_r(z)$，约定 $e_0=1$、$e_j=0$ 当 $j<0$。在完整 $\mathcal H_1$ 上定义
$$
F_r=\frac{D^r(D^*)^r}{(r!)^2},
\qquad
\Gamma_r=P_{K_1}F_r^{-1}|_{K_1}.
\tag{1.1}
$$
这里 $D^r$ 的输入是 $\mathcal H_{r+1}$。无限行只用固定层算子：逐个输出集合用 Cauchy--Schwarz 再按输入集合计数，给
$$
\|D_p\|\le\sqrt p\,\|a\|_2.
\tag{1.2}
$$
有限截断因此在各固定层按范数逼近完整算子。

对有限支撑向量直接计数，得到
$$
(F_r)_{ii}=e_r(z_{\ne i}),\qquad
(F_r)_{ij}=a_i a_j e_{r-1}(z_{\ne i,j})\quad(i\ne j).
\tag{1.3}
$$
有限截断及 (1.2) 把此式传给无限行。若 $T=\operatorname{diag}(z_i)$，也有完整有界算子恒等式
$$
\begin{aligned}
F_r={}&\sum_{\ell=0}^r(-1)^\ell(\ell+1)e_{r-\ell}T^\ell\\
&+\sum_{\substack{\ell,k\ge0\\\ell+k\le r-1}}
(-1)^{\ell+k}e_{r-1-\ell-k}\,T^\ell aa^*T^k.
\end{aligned}
\tag{1.4}
$$
确实，$e_r(z_{\ne i})=\sum_{\ell=0}^r(-z_i)^\ell e_{r-\ell}$；对非对角项再对两个删除变量展开，便得 (1.4)。其对角上的秩一项在总幂 $\ell$ 贡献 $(-1)^{\ell-1}\ell e_{r-\ell}z_i^\ell$，和第一行准确合成 (1.3)。

当行无限时，$T$ 紧、第二行有限秩，所以
$$
F_r=e_r I+\text{紧算子},\qquad e_r>0.
\tag{1.5}
$$
而 $F_r$ 没有核：$(D^*)^r f=0$ 的每个 $(r+1)$ 元坐标给
$$
\sum_{i\in I}\frac{f_i}{a_i}=0\qquad(|I|=r+1).
$$
比较两个共有 $r$ 个指标的集合，得到所有 $f_i/a_i$ 相等；一个集合的和再迫它们为零。有限行只需 $N\ge r+2$，无限行也可逐个有限坐标作此论证，不要求 $(f_i/a_i)$ 平方可和。
故有限模型中 $F_r>0$；无限模型中 (1.5) 和无核性使 $F_r$ 为正可逆 Fredholm 算子。
因此 (1.1) 全部是真正完整逆的压缩，且 $\Gamma_r$ 在 $K_1$ 上正、有界、可逆。

由完整最小逆公式，准确有
$$
H_r=\frac{\Gamma_r}{(r!)^2}.
\tag{1.6}
$$
最小逆输出自动被 $D^{r+1}$ 杀掉，并且正交于 $\ker D^r$；所以它确属原定义的出生一高度块。

## 2. 真实 Schur 精度的完整图形式

令
$$
u_{r,i}=a_i e_r(z_{\ne i}).
$$
由 (1.3)，
$$
F_ra=(r+1)u_r,\qquad
a^*F_ra=(r+1)^2e_{r+1}.
$$
所以完整 $\mathbb Ca\oplus K_1$ Schur 补为
$$
C_{r+1}=F_r-\frac{u_ru_r^*}{e_{r+1}},\qquad
C_{r+1}a=0,\qquad
C_{r+1}|_{K_1}=\Gamma_r^{-1}.
\tag{2.1}
$$
这一步不是把环境 Gram 直接压到 $K_1$ 再求逆。

固定 $i\ne j$，暂记 $x=z_i,y=z_j$，并令
$$
E_k=e_k(z_{\ne i,j}).
$$
则
$$
e_{r+1}=E_{r+1}+(x+y)E_r+xyE_{r-1},
$$
$$
e_r(z_{\ne i})=E_r+yE_{r-1},\qquad
e_r(z_{\ne j})=E_r+xE_{r-1}.
$$
将这些式子完整代入 (2.1)，所有 $x+y$、$xy$ 项消去，得到
$$
(C_{r+1})_{ij}=-a_i a_j g_{ij}^{(r)},
\qquad
\boxed{
g_{ij}^{(r)}=\frac{E_r^2-E_{r-1}E_{r+1}}{e_{r+1}}.
}
\tag{2.2}
$$
当 $r\ge1$，下节的 Newton 不等式给 $g_{ij}^{(r)}\ge0$。
由 $C_{r+1}a=0$，对角项遂为
$(C_{r+1})_{ii}=\sum_{j\ne i}z_jg_{ij}^{(r)}$，因而
$$
\boxed{
\langle C_{r+1}f,f\rangle
=\sum_{i<j}g_{ij}^{(r)}|a_jf_i-a_if_j|^2.
}
\tag{2.3}
$$
无限行的对角求和合法，因为有界算子的每行属于 $\ell^2$，而 $a\in\ell^2$；下面还给出与 $i,j$ 无关的边权界。因此 (2.3) 先对有限支撑向量成立，再按范数延拓。
归一化后完整无权和满足
$$
\sum_{i<j}|a_jf_i-a_if_j|^2
=\|f\|^2-|\langle a,f\rangle|^2.
\tag{2.4}
$$
所以控制所有真实边权就控制整个 $K_1$，没有选择对称线或改变源。

## 3. 两个自足的对称和估计

对任意非负可和行 $z$，总和 $S$、最大项至多 $\delta$，直接按 $(j-1)$ 元集合求和得到
$$
j e_j
=\sum_{|I|=j-1}z_I\left(S-\sum_{i\in I}z_i\right).
$$
因此
$$
\boxed{
\bigl(S-(j-1)\delta\bigr)e_{j-1}
\le j e_j\le S e_{j-1}.
}
\tag{3.1}
$$
在需要正分母的地方，我们只在 (0.1) 的范围使用它。

其次，
$$
\boxed{
e_r^2\ge\frac{r+1}{r}e_{r-1}e_{r+1}\quad(r\ge1).
}
\tag{3.2}
$$
这里给出足够的 Newton 证明。对有限行，$P(t)=\prod_i(1+z_it)$ 的根全为负实数，Rolle 定理使 $Q=P^{(r-1)}$ 的根也全为负实数。写这些根为 $\rho_\nu$，则
$$
\left(\frac{Q'}Q\right)'(0)
=-\sum_\nu\frac1{\rho_\nu^2}\le0.
$$
即 $Q'(0)^2\ge Q(0)Q''(0)$。代入各阶导数的阶乘即得 (3.2)。零或一次的退化情况直接成立。对无限可和行截断后令长度趋于无穷，固定阶对称和收敛，同式保留。

## 4. 整个 primitive 上的两侧精度界

对 $1\le r\le h$ 定义
$$
\alpha_r=\frac{2r\delta}{1-(r-1)\delta},\qquad
L_r=(1-\alpha_r)^2,\qquad
U_r=\frac{1+r^2\delta/(1-2\delta)}{1-r\delta},
\tag{4.1}
$$
并约定 $L_0=U_0=1$。假设 (0.1) 保证所有分母正且 $0\le\alpha_r<1$。

**引理。** 每条真实边权同时满足
$$
e_rL_r\le g_{ij}^{(r)}\le e_rU_r.
\tag{4.2}
$$

**下界。** 由 (3.2)，
$$
E_r^2-E_{r-1}E_{r+1}\ge\frac{E_r^2}{r+1}.
$$
而对全行使用 (3.1) 有 $(r+1)e_{r+1}\le e_r$。再由删除两个指标及一次并集上界，
$$
E_r\ge e_r-(z_i+z_j)e_{r-1}
\ge e_r\left(1-\frac{2r\delta}{1-(r-1)\delta}\right).
$$
最后一个括号正，故
$$
g_{ij}^{(r)}\ge\frac{E_r^2}{e_r}\ge e_rL_r.
$$

**上界。** 删除两个指标后的总和 $S_{ij}=1-z_i-z_j\ge1-2\delta$。对这个子行使用 (3.1)，得
$$
\frac{E_{r-1}}{E_r}\ge\frac r{S_{ij}},\qquad
\frac{E_{r+1}}{E_r}\ge\frac{S_{ij}-r\delta}{r+1}.
$$
(0.1) 保证 $S_{ij}-r\delta>0$，所以可以相乘。这给
$$
E_r^2-E_{r-1}E_{r+1}
\le\frac{E_r^2}{r+1}\left(1+\frac{r^2\delta}{S_{ij}}\right).
$$
使用 $E_r\le e_r$ 及全行的
$(r+1)e_{r+1}\ge(1-r\delta)e_r$，便得上界。

由 (2.3)--(2.4)，(4.2) 准确给
$$
\boxed{
e_rL_r I_{K_1}
\preceq\Gamma_r^{-1}
\preceq e_rU_r I_{K_1},
\qquad 0\le r\le h.
}
\tag{4.3}
$$
这是完整 Schur 后的精度估计。反转后是
$$
\boxed{
\frac1{e_rU_r}I_{K_1}
\preceq\Gamma_r
\preceq\frac1{e_rL_r}I_{K_1}.
}
\tag{4.4}
$$

## 5. 相邻最小逆的准确界和阶乘

令
$$
R_h=\left(\frac h{h-1}\right)^2
\frac{e_he_{h-2}}{e_{h-1}^2}.
$$
从 (4.4) 对同一 $K_1$ 上的三个正算子作标量上下界，并保留真实相邻的 Schur 反转，得到
$$
\boxed{
R_h\frac{L_hL_{h-2}}{U_{h-1}^2}
\le\mathsf C_h(D;1)
\le R_h\frac{U_hU_{h-2}}{L_{h-1}^2}.
}
\tag{5.1}
$$
详细地，(0.2)、(1.6) 等价于
$$
\Gamma_{h-1}\Gamma_h^{-1}\Gamma_{h-1}
\preceq C\left(\frac{h-1}{h}\right)^2\Gamma_{h-2}.
\tag{5.2}
$$
这使用正可逆算子的相邻 Schur 等价
$AB^{-1}A\preceq C_0\Longleftrightarrow AC_0^{-1}A\preceq B$；不要求三个 Gram 交换。
在 (5.2) 左边先用 $\Gamma_h^{-1}$ 的上下界，再用 $\Gamma_{h-1}^2$ 的上下界，与右边 $\Gamma_{h-2}$ 比较，就是 (5.1)。

由 (3.2) 及 (3.1) 分别得到
$$
\frac{h-1}{h}\bigl(1-(h-1)\delta\bigr)
\le\frac{e_he_{h-2}}{e_{h-1}^2}
\le\frac{h-1}{h}.
$$
故一个不再含对称和的准确范围为
$$
\boxed{
\frac h{h-1}\bigl(1-(h-1)\delta\bigr)
\frac{L_hL_{h-2}}{U_{h-1}^2}
\le\mathsf C_h(D;1)
\le\frac h{h-1}\frac{U_hU_{h-2}}{L_{h-1}^2}.
}
\tag{5.3}
$$

为得到简单的 (0.3)，注意 $h^2\delta\le1/100$ 保证对 $1\le r\le h$，
$$
\begin{aligned}
\log U_r
&\le\frac{r^2\delta}{1-2\delta}
 +\frac{r\delta}{1-r\delta}
\le3r^2\delta,\\
-\log L_r
&\le\frac{2\alpha_r}{1-\alpha_r}
=\frac{4r\delta}{1-(3r-1)\delta}
\le5r\delta.
\end{aligned}
\tag{5.4}
$$
这些界对 $r=0$ 也按零理解。
上界 (5.3) 的额外对数至多
$$
3h^2\delta+3(h-2)^2\delta+10(h-1)\delta
\le6h^2\delta.
$$
下界的损失对数至多
$$
2(h-1)\delta+5h\delta+5(h-2)\delta
 +6(h-1)^2\delta
=6(h^2-1)\delta
\le6h^2\delta,
$$
其中用了 $-\log(1-(h-1)\delta)\le2(h-1)\delta$。
这证明 (0.3)，全部阶乘因子已经包含在 $h/(h-1)$ 中。

## 6. 原无限尾、增长窗口和保留的缺口

原 $a_j=(j+1)^{-2}$、$j\ge m$ 的归一化平方总和满足
$$
S_m=\sum_{n=m+1}^\infty n^{-4}\ge\frac1{3(m+1)^3},
\qquad
\delta_m=\frac{(m+1)^{-4}}{S_m}\le\frac3{m+1}.
$$
共同缩放全部 $a_j$ 只使每个 $H_r$ 乘同一几何因子，故不改变 (0.2)。将此 $\delta_m$ 代入 (0.3) 即得 (0.4)。
若 $H(m)^2/m\to0$，(0.1) 对全部 $2\le h\le H(m)$ 最终同时成立，(0.4) 的两个指数也一致趋于零，因此得 (0.5)。

本结论没有用低孔 Fock 同构，尤其不需要把那个同构的条件数按所有孔层反复相乘。
相较于[R239 低孔 Fock 塔](R239-appendix-low-hole-fock-tower-and-nonvacuum-primitive-prefix-removal.md)的整个多出生塔，它只处理一个出生空间，但在这个完整 $K_1$ 内允许高度增长到 $o(\sqrt m)$。
不能把此改进直接用于那些依赖全部出生分量的前缀消去结论。

本稿仍未证明任意权型、任意内部高度的统一比较；(0.1) 是实质假设。
它也不支付 $K_s$、$s>1$ 上的对应精度，更不把原实际窄源投影到 $K_1$ 后宣称三 Gram 成本不增。
原高出生连续尾、两个实际边界的 $N=M$、正常湮灭者及普通 Hilbert ISP 继续开放。

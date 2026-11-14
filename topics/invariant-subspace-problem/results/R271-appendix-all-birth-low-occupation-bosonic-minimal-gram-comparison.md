# R271 附录：全部出生的低占据完整最小逆 Gram 与玻色空间比较

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_rebuild。
状态：已证明。新增的是所有出生空间上真实幂最小逆 Gram 的两侧标量估计及相邻第一下降比较；不把逐层右逆复合冒称完整幂的最小逆。

## 1. 原模型、完整逆和主结论

取有限正行或无限正 $\ell^2$ 行 $a=(a_i)$，令
$$
D=\sum_i a_iE_i,\qquad
S=\sum_i a_i^2>0,\qquad
M_a=\max_i a_i^2,\qquad\delta=M_a/S.
$$
$\mathcal H_p$ 是原平方自由正交 $p$ 孔层。只使用固定层算子；它们满足
$\|D_p\|\le\sqrt p\sqrt S$，故不要求 $D$ 在全部孔层直和上有界。
固定出生 $s\ge0$ 和高度 $h\ge2$，假设
$$
\boxed{(2s+h-1)\delta<1.}
\tag{1.1}
$$
有限行自动满足所需位数 $N\ge2s+h$，因为 $N\delta\ge1$。

令
$$
K_s=\ker D\cap\mathcal H_s,
\qquad
G_{r,s}=D^r(D^*)^r|_{\mathcal H_s},
\qquad0\le r\le h.
$$
下面证明 $G_{r,s}$ 在完整 $\mathcal H_s$ 上有界可逆。于是
$$
J_{r,s}=(D^*)^r G_{r,s}^{-1}|_{K_s},
\qquad
H_{r,s}=J_{r,s}^*J_{r,s}
=P_{K_s}G_{r,s}^{-1}|_{K_s}
\tag{1.2}
$$
正是真正完整 $D^r$ 的最小逆及其 Gram；$J_{0,s}=I$。
由于 $D^{r+1}J_{r,s}f=Df=0$，其输出在原核旗的正确高度内，并正交于 $\ker D^r$。

定义正数
$$
\boxed{
B_{s,r}=\prod_{j=1}^r\bigl(1-(2s+j-1)\delta\bigr),
\qquad B_{s,0}=1.
}
\tag{1.3}
$$

**定理 1.1。** 对整个 $K_s$，同时有
$$
\boxed{
\frac1{r!S^r}I_{K_s}
\preceq H_{r,s}
\preceq\frac1{r!S^rB_{s,r}}I_{K_s}
\qquad(0\le r\le h).
}
\tag{1.4}
$$
下界并不需要 (1.1)：对任意 primitive 源，凡其有实际 $D^r$ 原像，所有这种原像都满足同一下界。假设 (1.1) 负责同时支付完整满射和上界。

沿用[真实相邻高度归约](R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md)的定义
$$
\mathsf C_h(D;s)
=\inf\{C:C H_{h,s}\succeq
H_{h-1,s}H_{h-2,s}^{-1}H_{h-1,s}\},
\tag{1.5}
$$
即相同出生下真实第一下降的最优常数。

**推论 1.2。** 全部这些出生及高度满足
$$
\boxed{
\frac h{h-1}B_{s,h}B_{s,h-2}
\le\mathsf C_h(D;s)
\le\frac h{h-1}B_{s,h-1}^{-2}.
}
\tag{1.6}
$$
特别，写 $\theta=(2s+h-1)\delta<1$，则
$$
\boxed{
\frac h{h-1}(1-\theta)^{2(h-1)}
\le\mathsf C_h(D;s)
\le\frac h{h-1}(1-\theta)^{-2(h-1)}.
}
\tag{1.7}
$$
以上全部是原完整孔层和原 Hilbert 范数中的结论。

## 2. 逐层交换子给完整高幂的阶乘下界

令 $n_i=E_i^*E_i$。同位矩阵计算给固定层上的准确等式
$$
DD^*-D^*D=SI-2\sum_i a_i^2n_i.
\tag{2.1}
$$
在 $p$ 孔层，$\sum_i n_i=pI$，所以
$$
DD^*-D^*D\succeq (S-2pM_a)I.
\tag{2.2}
$$
无限行由固定层范数收敛得到同式。

取任意 $0\ne x\in\mathcal H_s$，令
$$
x_j=(D^*)^j x,\qquad a_j=\|x_j\|^2.
$$
最初由 (2.2) 有 $a_1\ge(S-2sM_a)a_0>0$。
当 $a_{j-1},a_j>0$ 时，准确配对
$$
\langle Dx_j,x_{j-1}\rangle
=\langle x_j,D^*x_{j-1}\rangle=a_j
$$
和 Cauchy--Schwarz 给
$$
\|Dx_j\|^2\ge\frac{a_j^2}{a_{j-1}}.
$$
将 (2.2) 用在第 $s+j$ 层，得到
$$
a_{j+1}\ge\frac{a_j^2}{a_{j-1}}
 +(S-2(s+j)M_a)a_j.
\tag{2.3}
$$
故比值 $t_j=a_j/a_{j-1}$ 满足
$$
t_{j+1}\ge t_j+S-2(s+j)M_a.
$$
归纳求和给
$$
\boxed{
t_j\ge j\,[S-(2s+j-1)M_a]>0
\qquad(1\le j\le h).
}
\tag{2.4}
$$
正性由 (1.1) 保证，所以每一步比值确实有定义。这里不要求每个单独的后期交换子下界 $S-2(s+j)M_a$ 都正；累积后的准确右端 (2.4) 正就足够。

把 (2.4) 相乘，得到对整个输入层的估计
$$
\boxed{
\|(D^*)^r x\|^2
\ge r!\prod_{j=1}^r[S-(2s+j-1)M_a]\,\|x\|^2
=r!S^r B_{s,r}\|x\|^2.
}
\tag{2.5}
$$
因此完整算子
$$
\boxed{G_{r,s}\succeq r!S^rB_{s,r}I_{\mathcal H_s}.}
\tag{2.6}
$$
这直接证明 $D^r:\mathcal H_{s+r}\to\mathcal H_s$ 满射和 (1.2) 的完整有界最小逆，不借用 primitive 压缩的谱隙。
由完整逆的序反转，(2.6) 已给出 (1.4) 的上界。

## 3. 平方自由层到真正玻色空间的等距嵌入

本节只为估计 primitive 源的创建范数引入一个辅助 Hilbert 空间，不改变原问题的定义域或范数。
令 $\mathcal F_p$ 有标准正交基 $e_\alpha$，其中 $\alpha=(\alpha_i)$ 是有限支撑非负整数列、$\sum_i\alpha_i=p$。
在各固定层定义玻色创建与删除
$$
b_i^*e_\alpha=\sqrt{\alpha_i+1}\,e_{\alpha+\mathbf e_i},
\qquad
b_ie_\alpha=\sqrt{\alpha_i}\,e_{\alpha-\mathbf e_i},
$$
$$
\mathcal B=\sum_i a_i b_i,
\qquad\mathcal B^*=\sum_i a_i b_i^*.
$$
这些是标准对称张量层上的算子：创建等于
$\sqrt{p+1}$ 倍的 $a\otimes f$ 到对称张量的正交投影，故
$$
\|\mathcal B^*:\mathcal F_p\to\mathcal F_{p+1}\|
\le\sqrt{p+1}\sqrt S.
$$
所以无限 $\ell^2$ 行在每个固定层仍有界，有限行逼近合法。
逐个基向量计算再取范数极限，得到
$$
[\mathcal B,\mathcal B^*]=SI.
\tag{3.1}
$$

把原 $e_I$ 等距嵌入 $e_{1_I}$，并令 $Q_p$ 为到这些平方自由基向量的正交投影。
删除一个孔不会产生重复占据，故有准确限制等式
$$
\mathcal B|_{\mathcal H_p}=D_p.
\tag{3.2}
$$
创建虽然可以离开平方自由层，但重复占据一旦出现，继续创建绝不可能回到平方自由层。因此对任意 $r\ge0$，
$$
\boxed{
(D^*)^r=Q_{s+r}(\mathcal B^*)^r|_{\mathcal H_s}.
}
\tag{3.3}
$$
这可逐个创建路径验证；每条有中间碰撞的路径最终被 $Q_{s+r}$ 杀掉，其余路径的所有创建系数与原 $D^*$ 一致。先对有限支撑基向量证明，再用固定层有界性延拓。

若 $f\in K_s$，(3.2) 给 $\mathcal Bf=0$。由 (3.1)，
$$
\mathcal B(\mathcal B^*)^r f
=rS(\mathcal B^*)^{r-1}f.
$$
逐次取内积，得到完整玻色创建的准确范数
$$
\|(\mathcal B^*)^r f\|^2=r!S^r\|f\|^2.
$$
最后才作 (3.3) 的正交投影，于是
$$
\boxed{
\|(D^*)^r f\|^2\le r!S^r\|f\|^2
\qquad(f\in K_s).
}
\tag{3.4}
$$
这个 primitive 前向界对任意有限或无限正行成立，不需 (1.1)。

## 4. 前向上界如何支付真正最小逆的下界

不能仅因 (3.4) 就把环境逆的压缩换成压缩的逆。这里直接用所有真实原像的对偶配对支付该方向。

固定 $f\in K_s$，若 $u\in\mathcal H_{s+r}$ 满足 $D^r u=f$，则
$$
\|f\|^2
=\langle D^r u,f\rangle
=\langle u,(D^*)^r f\rangle
\le\|u\|\sqrt{r!S^r}\,\|f\|.
$$
对 $f\ne0$ 得
$$
\|u\|^2\ge\frac{\|f\|^2}{r!S^r}.
\tag{4.1}
$$
把 $u$ 取成已由 §2 保证存在的真正最小原像 $J_{r,s}f$，便得 (1.4) 的下界。
这也等价于正算子压缩的 Schur--Jensen 方向
$$
P_{K_s}G_{r,s}^{-1}|_{K_s}
\succeq(P_{K_s}G_{r,s}|_{K_s})^{-1},
$$
再使用 (3.4)；两种写法都保留完整最小逆。
这里没有要求 $K_s$ 约化 $G_{r,s}$，也没有用逐层最小右逆的复合代替 $J_{r,s}$。

## 5. 三个真实 Gram 的相邻比较

从 (1.4)，同一 $K_s$ 上
$$
H_{h-1,s}\succeq\frac1{(h-1)!S^{h-1}}I,
\qquad
H_{h-2,s}^{-1}\succeq (h-2)!S^{h-2}B_{s,h-2}I.
$$
所以
$$
H_{h-1,s}H_{h-2,s}^{-1}H_{h-1,s}
\succeq
\frac{(h-2)!B_{s,h-2}}{((h-1)!)^2S^h}I.
$$
而 $H_{h,s}\preceq[h!S^hB_{s,h}]^{-1}I$。任何满足 (1.5) 的常数都因此至少为
$$
\frac{h!(h-2)!}{((h-1)!)^2}B_{s,h}B_{s,h-2}
=\frac h{h-1}B_{s,h}B_{s,h-2}.
$$
反过来，先用 $H_{h-2,s}^{-1}\preceq(h-2)!S^{h-2}I$，再用 $H_{h-1,s}$ 的上界，最后与 $H_{h,s}\succeq[h!S^h]^{-1}I$ 比较，得到 (1.6) 的上界。
这一推导只用正算子标量界，不假设三个 Gram 交换。

对 $j\le h$，每个 $B_{s,r}$ 的因子都在 $[1-\theta,1]$ 内。
因此 $B_{s,h}B_{s,h-2}\ge(1-\theta)^{2(h-1)}$，
$B_{s,h-1}^{-2}\le(1-\theta)^{-2(h-1)}$，从而得 (1.7)。
还可写为
$$
\boxed{
\left|\log\!\left(\frac{h-1}{h}\mathsf C_h(D;s)\right)\right|
\le\frac{2(h-1)(2s+h-1)\delta}{1-(2s+h-1)\delta}.
}
\tag{5.1}
$$

## 6. 原完整连续尾上的统一多出生窗口

取原 $D_m=\sum_{j\ge m}(j+1)^{-2}E_j$。归一后的
$\delta_m\le3/(m+1)$，且共同缩放不改变相邻常数。
所以只要
$$
m+1>3(2s+h-1),
$$
原完整尾的整个 $K_s$ 上有
$$
\boxed{
\left|\log\!\left(\frac{h-1}{h}\mathsf C_h(D_m;s)\right)\right|
\le\frac{6(h-1)(2s+h-1)}{m+1-3(2s+h-1)}.
}
\tag{6.1}
$$
因此对任意整数上界 $S_*(m)\ge0$、$H_*(m)\ge2$，若
$$
\frac{H_*(m)(S_*(m)+H_*(m))}{m}\longrightarrow0,
\tag{6.2}
$$
则
$$
\boxed{
\sup_{\substack{0\le s\le S_*(m)\\2\le h\le H_*(m)}}
\left|\frac{h-1}{h}\mathsf C_h(D_m;s)-1\right|
\longrightarrow0.
}
\tag{6.3}
$$
例如，固定高度时可同时允许出生 $s=o(m)$；固定有界出生时可允许全部高度 $h=o(\sqrt m)$。
出生一另有[根交错稿](R271-appendix-birth-one-root-interlacing-precision-and-linear-tail-window.md)的更强 $o(m)$ 高度窗口；两者范围不同，均予保留。

## 7. 与既有低孔 Fock 塔的关系及未闭缺口

[R239 低孔 Fock 塔](R239-appendix-low-hole-fock-tower-and-nonvacuum-primitive-prefix-removal.md)构造逐层 canonical 右逆复合的准确交织同构，并控制整个多出生外直和的条件数；其充分误差界为 $\delta[32(P+1)]^P$。
本稿不重做那个同构，也没有给其全部不同出生列之间的夹角或新条件数界。

新增的对象是 (1.2) 的每个**完整幂**的真最小逆，(1.4) 保留其 Schur 效应，并由此获得同一出生下全部相邻的 (1.6)。
这些新 Gram 估计的误差按 $h(s+h)\delta$ 支付，适用于所有满足 (1.1) 的出生；不要求旧混合塔同构已近等距。
所以不能把 (6.3) 直接代入旧多出生核延伸而省掉其交叉列费用。

原实际高孔源通常远超 (1.1) 的低占据范围，尚未被此稿覆盖。
任意有限异权全出生全高度统一比较、原窄源的完整三 Gram 费用、无权 $N=M$ 和普通 Hilbert ISP 仍然开放。

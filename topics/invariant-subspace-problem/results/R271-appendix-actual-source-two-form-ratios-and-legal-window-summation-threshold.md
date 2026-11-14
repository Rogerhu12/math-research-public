# R271 附录：实际源的两正形式比例与原合法窗口的精确求和门槛

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。
状态：已证明的条件性判据；normal_resume_1cf 全文独立复核原源、窗数、尾及 carry，Astra-ISP-1cf8c51d 完成二次主核。下文没有证明所需的二正形式比较；原 $N=M$ 和普通复 Hilbert ISP 仍开。

本稿接[真实两侧窄通量](R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md)、[左源 Gram 笔记](../notes/2026-11-13-left-source-gram-and-paid-actual-dual-source-1cf.md)及[首段先消元](R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md)。
新增的是把待付的费用明确缩到同一个实际源上的二次型比例，并给同头全部原合法窗口的求和及临界尺度。
它不同于既有以完整修复范数 $\lambda_q$ 为输入的覆盖准则；本稿的输入是 $\mathscr L_q$ 相对于 $I+\mathcal Q_q$ 的实际源比例。

## 1. 实际源、两个度量及准确比例

固定 $m\ge5$、$d=2^m$、整数 $4d\le q\le e^{d^3/4}$。
对两个原边界之一，仍记 $M=\ker T$、$W=M\ominus N$。
取 $w\in W$，使用原低投影及其真实源
$$
v=P_{V_{m,q}}w,\qquad r=E_qv,\qquad a=\mathsf f_q^{-1}r.
$$
沿前稿，
$$
\mathcal P_q=I+\mathscr L_q,\qquad
\mathcal Q_q=\mathcal J_{-,q}^*\mathcal J_{-,q}>0,
\qquad
\mathcal D_q=I+\mathcal Q_q,
$$
$$
\mu_q(r)^2=\langle\mathcal Q_qa,a\rangle,\qquad
\lambda_q(r)^2=\langle\mathcal P_qa,a\rangle.
\tag{1.1}
$$
$\mathcal P_q$ 与 $\mathcal Q_q$ 不要求交换。

当 $a\ne0$ 时定义
$$
\boxed{
c_{m,q}(w)
=\frac{\langle\mathscr L_qa,a\rangle}
{\|a\|^2+\mu_q(r)^2}
=\frac{\langle\mathscr L_qa,a\rangle}
{\langle\mathcal D_qa,a\rangle}\ge0.
}
\tag{1.2}
$$
$a=0$ 时令 $c_{m,q}(w)=0$；这时 $r=0$、$\mu_q=\lambda_q=0$。
该比例只在原 $w$ 产生的向量上取值；没有扩大到一般 primitive、任意源或整个算子范数。

记实际未来带及共同 carry
$$
\beta_{m,q}(w)=\|P_{[q+1,q+d]}^{(m)}w\|,
\qquad \varepsilon_m=2e^{-55d^4},
\qquad b_{m,q}=\beta_{m,q}+\varepsilon_m\|w\|.
\tag{1.3}
$$
首段先消元 §4.3 和左源笔记 §§4—5 已分别给
$$
\boxed{
\|a\|\le b_{m,q},\qquad
\lambda_q(r_q^\flat)\le b_{m,q},\qquad
\mu_q(r)^2\le\lambda_q(r_q^\flat)\lambda_q(r).
}
\tag{1.4}
$$
这里 $r_q^\flat=G_qJ_q^{-1}r$ 仍是原变换源，不把它称作返回源。
$e^{-72d^4}\le\varepsilon_m$，所以 (1.3) 的同一个上界同时适用于两个不同的已付量。

## 2. 不需高次返回范数的单窗估计

置 $x=\mu_q(r)^2$、$c=c_{m,q}(w)$、$b=b_{m,q}$。
(1.1)—(1.2) 准确给
$$
\lambda_q(r)^2=(1+c)\|a\|^2+c x
\le(1+c)b^2+cx.
$$
再用 (1.4)，得到
$$
x^2\le b^2\lambda_q(r)^2
\le(1+c)b^4+cxb^2.
$$
右移并作准确因式分解，
$$
\bigl(x-(1+c)b^2\bigr)(x+b^2)\le0.
$$
因 $x,b^2\ge0$，有
$$
\boxed{
\mu_q(r)^2\le
\bigl(1+c_{m,q}(w)\bigr)
\bigl(\beta_{m,q}(w)+2e^{-55d^4}\|w\|\bigr)^2.
}
\tag{2.1}
$$
这一步只用 $\langle\mathscr L_qa,a\rangle$；
没有要求 $\|\mathscr L_qa\|$ 或原强返回费用已被控制。
尤其若只在此实际 $a$ 上证明
$$
\langle\mathscr L_qa,a\rangle
\le C_{m,q}\langle(I+\mathcal Q_q)a,a\rangle,
\tag{2.2}
$$
则 (2.1) 可将 $c_{m,q}(w)$ 换成 $C_{m,q}$。
全空间算子序 $\mathscr L_q\le C_{m,q}(I+\mathcal Q_q)$ 是一个更强的充分输入，不是本判据的假设必需形式。

## 3. 真实左质量在全部合法 q 上的一致下界

以下固定 $0\ne w\in W$。
令 $\mathcal N_{\rm tot}$ 为原全部物理位的孔数，定义
$$
\tau_m(w)=\|1_{\{\mathcal N_{\rm tot}>4d\}}w\|.
$$
有限孔基在原 $H$ 中完备，故 $\tau_m(w)\to0$。
尾孔数从不超过总孔数，所以对每个 $q\ge4d$，
$$
\|P_{>q}^{(m)}w\|\le\tau_m(w).
$$

原低投影与左零源核预算是
$$
\|v-P_{\le q}^{(m)}w\|\le e^{-74d^4}\|w\|,
\qquad
\|v-\mathcal J_{-,q}a\|\le e^{-75d^4}\|w\|.
$$
因此
$$
\frac{\mu_q(r)}{\|w\|}
\ge
\left(1-\frac{\tau_m(w)^2}{\|w\|^2}\right)^{1/2}
-e^{-74d^4}-e^{-75d^4}
=:\theta_m(w).
\tag{3.1}
$$
$\theta_m(w)\to1$，且充分大 $m$ 时为正。
(3.1) 同时适用于这个 $m$ 的全部原合法 $q$；没有在固定 $m$ 的有限窗口内擅自取 $q\to\infty$。

## 4. 同头全部窗口的准确求和

令
$$
Q_m^{\max}=\left\lfloor e^{d^3/4}\right\rfloor,\qquad
I_m=\{4d,4d+1,\ldots,Q_m^{\max}\},\qquad
\ell_m=|I_m|=Q_m^{\max}-4d+1.
\tag{4.1}
$$
对固定 $m$，各未来带用同一孔分解。
每一孔层属于至多 $d$ 个窗口 $[q+1,q+d]$；所有这些窗口又在尾孔 $>4d$ 中。
故 Bessel 与实际有限重叠准确给
$$
\sum_{q\in I_m}\beta_{m,q}(w)^2
\le d\,\tau_m(w)^2.
\tag{4.2}
$$
对有限向量列应用三角不等式，
$$
\left(\sum_{q\in I_m}b_{m,q}^2\right)^{1/2}
\le\sqrt d\,\tau_m(w)+\varepsilon_m\sqrt{\ell_m}\|w\|.
\tag{4.3}
$$
由 (2.1)、(3.1)，充分大 $m$ 时
$$
\boxed{
\frac1d\sum_{q\in I_m}\frac1{1+c_{m,q}(w)}
\le
\frac{\left[
\tau_m(w)/\|w\|
+\varepsilon_m\sqrt{\ell_m/d}
\right]^2}{\theta_m(w)^2}
\longrightarrow0.
}
\tag{4.4}
$$
carry 总量已付：$\ell_m\le e^{d^3/4}$，所以
$\varepsilon_m^2\ell_m/d\le4d^{-1}e^{-110d^4+d^3/4}\to0$。
没有把单窗小误差直接相加而漏掉指数多的窗口。

更一般地，对任意子集 $J_m\subset I_m$，(4.4) 左侧只对 $J_m$ 求和也成立。
因而只需在一批足够多的真实窗口上控制 (1.2)，不必每个窗口都满足同一上界。

## 5. 足以关闭 N=M 的具体比较尺度

(4.4) 给下列准确条件性结论。

若对每个假定非零 $w\in W$，存在原实际源上的上界
$$
c_{m,q}(w)\le C_{m,q}(w)
$$
及趋于无穷的头子序列，使
$$
\limsup\frac1d\sum_{q\in I_m}\frac1{1+C_{m,q}(w)}>0,
\tag{5.1}
$$
则这样的 $w$ 不可能存在，故 $W=0$、$N=M$。
上界可以依赖这个固定 $w$；(5.1) 不是对一般源的免费断言。

特别，令
$$
C_m(w)=\max_{q\in I_m}c_{m,q}(w)<\infty.
$$
非零真缺陷必须满足
$$
\boxed{
\frac{\ell_m}{d(1+C_m(w))}\longrightarrow0,
\qquad\text{即}\qquad
\frac{d(1+C_m(w))}{\ell_m}\longrightarrow\infty.
}
\tag{5.2}
$$
所以只要在同一无穷头子序列对实际源证明
$$
\boxed{
C_m(w)=O\!\left(\frac{e^{d^3/4}}d\right),
}
\tag{5.3}
$$
便已排除该 $w$。无需把比例压到与 $m$ 无关的常数。
若 (5.3) 对所有假定非零 $w\in W$ 都成立，即得到 $N=M$。
更强但容易陈述的充分目标是：在同一头子序列，原全部合法 $q$ 上
$$
\mathscr L_q\le C_m(I+\mathcal Q_q),\qquad
C_m=O(e^{d^3/4}/d).
\tag{5.4}
$$

已有高旗范数上界至多给 $c_{m,q}(w)\le m^{-2}e^{40d^4}$，远大于 (5.3)，不能完成这个条件。
固定相似的巨大头条件数若仍带 $e^{c d^4}$ 也不够；需要实际二形式之间的比较，或只针对实际源的新估计。

## 6. 两种已付源规范化可以怎样使用

### 6.1 同 BA 源的准确最小状态

取两侧窄通量稿 §7 的 $a^\sharp=a-e$：
$$
e\in\ker\mathscr L_q=\ker B_A,\qquad
P_{\ker B_A}(I+\mathcal Q_q)a^\sharp=0.
$$
这是 $\mathcal D_q=I+\mathcal Q_q$ 中的正交分解，故
$$
\langle\mathcal D_qa,a\rangle
=\langle\mathcal D_qa^\sharp,a^\sharp\rangle
+\langle\mathcal D_qe,e\rangle,
\qquad
\langle\mathscr L_qa,a\rangle
=\langle\mathscr L_qa^\sharp,a^\sharp\rangle.
$$
所以只在准确最小类 $a^\sharp$ 上证明 (2.2)，就直接给原 $a$ 上同一个常数；这一步无须另付误差。
原返回向量和高对偶也精确保留，但本判据只使用显示的二次型。

### 6.2 真实 barf 的两侧最小原像状态

两侧窄通量稿 §6 给
$$
a_{\rm two}=(\mathcal Q_q+\mathcal P_q)^{-1}
B_A^*(H^\circ)^{-1}\overline f,\qquad
\|a-a_{\rm two}\|_{\mathcal Q_q+\mathcal P_q}
\le \rho_m\|w\|,\quad \rho_m=e^{-72d^4}.
$$
由于 $\mathcal D_q\le\mathcal P_q+\mathcal Q_q$、
$\mathscr L_q\le\mathcal P_q+\mathcal Q_q$，若仅在这个准确状态上有
$$
\|\mathscr L_q^{1/2}a_{\rm two}\|
\le\sqrt{C_{m,q}}\,
\|\mathcal D_q^{1/2}a_{\rm two}\|,
$$
两次三角不等式给
$$
\|\mathscr L_q^{1/2}a\|
\le \sqrt{C_{m,q}}\|\mathcal D_q^{1/2}a\|
+(\sqrt{C_{m,q}}+1)\rho_m\|w\|.
$$
结合 (3.1)，准确得到
$$
\boxed{
\sqrt{c_{m,q}(w)}
\le\sqrt{C_{m,q}}
+(\sqrt{C_{m,q}}+1)\frac{\rho_m}{\theta_m(w)}.
}
\tag{6.1}
$$
因此 (5.3) 的尺度也可以只在真正的 $a_{\rm two}$ 上支付，carry 不改变其阶。
这里保留原 $\overline f$，没有用旧 $\sigma$ 替换它。

## 7. 剩余问题的准确形式

本稿已经付清“如果实际二形式比较成立，怎样推到原 $N=M$”的所有窗数、孔分解、尾及 carry 费用。
仍未证明的是 (2.2) 在 $a$、$a^\sharp$ 或 $a_{\rm two}$ 上满足 (5.1)/(5.3) 所需的量级。
一般 finite primitive 的相邻算子序也尚未证明，而且即使证明仍须实际连接到本稿的 $\mathscr L_q,\mathcal Q_q$。

这是一条具体的后续证明目标，不是普通 ISP 的完成声明。

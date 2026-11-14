# R161 — 整循环二次不变量与原二阶矩的标量判据

**状态：已证明。日期：2026-11-12。**

对 R154/R157 的原 E389、完整类群商和 U 迹，canonical
Frobenius 给规范整提升
$$
 \widehat G_{p,\Psi}
  =\frac1p\log_E\bigl(
       \Psi\varphi_{\rm can}^2-[a_p]\Psi\varphi_{\rm can}+[p]\Psi
                  \bigr).
$$
括号内特殊纤维由 Frobenius 特征式恒为 O，故整性来自
实际 $p\mathcal O$ 形式盘。q 展开精确是原 p-depleted
primitive；CL 点值是原加法 $\delta$-character。
全部素于 p 退化图、$W_R$、Hecke 完整迹和 w 反号保留。

令 $d(j,k)$ 为 j-k 的最小非负模 p 代表，对原整列
$\widehat b_j=\tau^j\widehat B$ 定义
$$
 \widehat I_1=\frac12\sum_{j,k}d(p-d)\widehat b_j\widehat b_k,
 \qquad
 \widehat I_2=\frac1{24}\sum_{j,k}d^2(p-d)^2\widehat b_j\widehat b_k .
$$
它们对循环、真实反射及 w 严格不变，是真正商上的整
形式/刚性函数。在原 CM 点的值属于 $\mathbb Z_p$；
不因此称为跨 p 固定的有理数。

模 p 写 $n=NB$、$A=D_1B$、$F_2=D_2B$，准确有
$$
 I_1=A^2-nA-2nF_2=\mathscr D .
$$
原中心 $n=0$ 时 $I_1=A^2$；若其为零，则
$I_2=F_2^2$。故
$$
 \boxed{\quad
  D_2B(c)=0
       \iff I_1(c)=I_2(c)=0 .
 \quad}
$$
这里保整个原纤维，包含完全分裂情形。
**不需要源简单零或 $dn(c)\ne0$。**
原单位比较与 R146 随后给任一非零值
$\Rightarrow a\le1\Rightarrow\Sha(E/\mathbb Q)[p^\infty]=0$。

另一个全局有理版本适用于 R130/R139 的原全部好输入，
保其非异常群环单位条件。取反演对称的原 formalizer
$D_p$、$R=D_pQ$，并令
$$
 b_j^{\rm rat}=\frac{u_E(\tau^jR)}p,\qquad
 u_{E17}=-x/y,\quad
 u_{E389}=-2x/(2y+1).
$$
由 $cR=-\tau^rR$ 和 $u_E$ 真奇，同一循环核给
$I_1^{\rm rat},I_2^{\rm rat}\in\mathbb Q\cap\mathbb Z_p$。
它们依赖 $p,\ell,Q$，但模 p 的同时零准确等价于原
$D_2(\log_E(D_pQ)/p)$ 半局部行为零。
这一版本不要求普通 CL 源；有理参数列的 trace 只模 p
为零，不能冒充精确加法迹。

完整证明还给精确循环 Laplacian/整 Hilbert–90 恒等式
以及 $h(I_r^{\rm rat})=O_E(p^5\widehat h(Q)+p\log p)$。
未证明实际两个值无穷次不同为零，也未由局部检验推出
$a\le1$ 的反向等价。

[完整证明与原始来源](../notes/2026-11-12-integral-cyclic-invariants-and-actual-second-moment.md)
逐项核对 Katz（1981）§4.1 与 Buium–Poonen（2009）
的 CL、加法 character 及原函数常数。

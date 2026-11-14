# R135. 实际 CL 伴随形式、线性次数与原 Heegner 两矩

日期：2026-11-12。状态：**已证明；实际两矩的无穷非零仍开。**

完整规范、证明和原始文献页码见
[CL reciprocity 与 CM 伴随形式](../notes/2026-11-12-canonical-lift-companion-and-linear-degree-reciprocity.md)。

固定 $E:y^2=x^3-17x$、$N=9248$ 和原参数化
$\pi:X_0(N)\to E$。选
$\omega_0=c_\pi^{-1}dx/(2y)$ 使
$\pi^*\omega_0=f\,dq/q$；固定单位 $c_\pi$ 同时缩放对数、
$\delta$-character 和 reciprocity 函数，明确处理 BP 的
$dx/y$ 规范。取充分大的好素数 $p$，在
$F=\mathbb Q(\sqrt{-15})$、$K=\mathbb Q(i)$ 均分裂。

## 1. 明确的原曲线 CM 分子

设 $\psi_E$ 的导子为 $\mathfrak f=2(1+i)17$。则
$$
 H_p=\theta(\psi_E^{p-2})\in
 S_{p-1}(\Gamma_0(9248),\mathbb Z)
$$
有准确原导子和 trivial nebentypus。有限部分在 $\mu_4$ 中，
$p-2\equiv3\pmod4$ 保留其核；共轭理想给整系数。
逐理想求和给
$$
 [q^{p^rm}]\bar H_p
      =\bar\alpha_p^{-r}\bar a_m/m\quad(p\nmid m),
$$
其中 $\alpha_p$ 为单位 Frobenius 根。

令 $\mathrm{Ha}_p$ 为 Hasse invariant。Buium–Poonen (2009)
Theorem 3.17 的实际 CL 函数准确为
$$
 h_p=\bar H_p/\mathrm{Ha}_p,\qquad
 g_{\rm BP}=-\bar a_p^{-1}h_p,\qquad
 f_{\rm pre}:=\overline{f^{(-1)}}=h_p-\bar a_p^{-1}h_p^p.
 \tag{1}
$$
所以它下降到 $X_0(N)$。$h_p$ 只有简单超奇异极点，且至少
一处是真的：若没有极点则为常数，与 q 一次系数 $1$ 矛盾。
在任意固定细 level 覆盖 $X$ 上
$$
 \deg(g_{\rm BP})\le
       (2g_X-2+\nu_X)(p-1)/2=O(p).
 \tag{2}
$$
这也证明分子 exact filtration 为 $p-1$。

有理 $2$-挠点及 Hasse 界给 $\bar a_p\ne1$。因此
$$
 f_{\rm pre}-\operatorname{AS}(-\bar a_p^{-1}h_p)
               =(1-\bar a_p^{-1})h_p,\qquad
 \operatorname{AS}(v)=v^p-v.
$$
右边保留真实简单极点，而任何非恒定 AS 像的极点阶均被 $p$
整除，故 $f_{\rm pre}\notin\operatorname{AS}(\bar{\mathbb F}_p(X))$。
同时 twisted 方程 $g_{\rm BP}^p-\bar a_pg_{\rm BP}=f_{\rm pre}$
有上式的有理解；两种方程不可混同。

## 2. 全部原 CM 项及单位三角矩阵

保持原定义
$Q=\operatorname{Tr}_{H/L}\pi(x_\ell)$，
$|\operatorname{Gal}(H/L)|=2u$；置
$z_0=c_\pi^{-1}\log_E(Q)/p$。
写 $s=\operatorname{Art}_{L/F}(p)$，
$\beta_p=p/\alpha_p$。实际 CL 迹及去 $p$ Coleman 迹满足
$$
 B=\sum_{\gamma\in\operatorname{Gal}(H/L)}
                  \Phi^\dagger(x_\ell^\gamma)
        =(s-\beta_p)z_0,\qquad
 \eta_0=(s-\alpha_p)B.
 \tag{3}
$$
模 $p$ 后，实际伴随迹
$$
 C=\sum_\gamma h_p(\overline{x_\ell^\gamma})
                  =-\bar a_p\,s\bar z_0.
 \tag{4}
$$
若 $s=\tau^h\ne1$，用 R134 的 Artin–Schreier 参数和两个
有限域迹，则
$$
 \binom{T_1(C)}{T_2(C)}
   =-\bar a_p
      \begin{pmatrix}1&0\\-2h&1\end{pmatrix}
         \binom{T_1(\bar z_0)}{T_2(\bar z_0)}.
 \tag{5}
$$
另一素位及完全分裂时的完成置换也保留，分别按 R134 的
共轭规则及 $h=0$ 版本处理。故实际
$\mathcal D_2=\sum_j\binom j2\tau^j$ 行的非零性，等价于
原 $2pu$ 项加权和
$$
 \sum_{j=0}^{p-1}\binom j2\sum_\gamma
               h_p(\overline{x_\ell^{\tau^j\gamma}})\ne0.
 \tag{6}
$$
它推出 $a\le1$，继而由 R127 得
$\Sha(E/\mathbb Q)[p^\infty]=0$。

## 3. 尚未证明的输入

BP 的 $O(p)\,p^r$ 计数针对落入指定子群的个别点，不能将
(6) 的一条完整迹关系替换成每点所属的小秩子群。
原轨道总迹本来为零，与 (1) 的全局 AS 非平凡并不矛盾。
R123 给同时分裂子集的无穷合法输入；R126 的 $u^2=o(p)$
无限集合没有已证的分裂类型控制。本文未将两者交集
无穷或 (6) 无穷非零作为结论。

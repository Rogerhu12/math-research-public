# R147 附录：实主行的实切片判据与奇次减正辅助的全部位移

日期：2026-11-13（UTC）。作者：kernel_resume_1cf；Astra-ISP-1cf8c51d 已全文核查切片、符号、实际首位和全部权/幂。
状态：完整证明的推论扩展。主行任意实 $\ell^2$，辅助任意实或复 $\ell^1$，没有尾率预算。复指数权与全部点态幂保留。

## 1. 已证输入与实切片版本

[R147 慢辅助附录](R147-appendix-bounded-slow-auxiliary-slices-and-polynomial-cyclicity.md)
已经给任意有限个可和辅助的实际 Bell 多项式与最高系数单位。
[R176 谱相交附录](R176-appendix-bounded-part-spectral-intersection-and-common-exceptional-root.md) §6
进一步证明：任何坏点态幂的两个首位切片必须在同一个共同根 $r_u$ 处相等。
[R176 实结构附录](R176-appendix-real-structure-affine-lines-and-odd-power-cyclicity.md)
又证明实主行的这个共同根必须为实数。

以下只是把这三个已证接口合成准确的慢辅助范围；
不把原混合闭图或实共同根本身重新记为新增。

取
$$
u=a_*+\sum_j a_j\chi_j,\qquad
a_*,a_j\in\mathbb R,\quad a\in\ell^2,\quad a\ne0,
$$
以及有限个任意复可和辅助
$$
v_\nu=c_{\nu,*}+\sum_j c_{\nu j}\chi_j,\qquad
c_\nu\in\ell^1(\mathbb C),
$$
$$
\beta_\nu=c_{\nu,*}+\sum_j c_{\nu j}.
$$
令
$$
j_0=\min\{j:|a_j|+\sum_\nu|c_{\nu j}|>0\},\quad
a=a_{j_0},\quad c=(c_{\nu j_0})_\nu.
$$
其中 $a$ 可以为零。
给
$$
F(U,V)=\sum_{k=0}^p U^k r_k(V),\qquad
p\ge1,\quad r_p(\beta)\ne0,
$$
定义
$$
p_0(t)=F(t,\beta),\qquad
p_1(t)=F(t-2a,\beta-2c).
\tag{1.1}
$$

**定理 1。**
若不存在实数 $t$ 使
$$
p_0(t)=p_1(t)=\lambda,
\tag{1.2}
$$
则对每个 $m\ge1$ 和每个复 $\ell^2$ 指数权 $w$，
$$
\boxed{(F(u,v)-\lambda)^m e^w\text{ 非零且循环}.}
\tag{1.3}
$$

证明：反设不循环。
慢辅助 Bell 实现的最高系数为单位，
其核上 first 有界且有限谱。
因此共同 $r_u$ 存在；实结构使 $r_u\in\mathbb R$，
而谱相交附录的真实差商定理给
$p_0(r_u)=p_1(r_u)=\lambda$，与假设矛盾。
所有自然域及任意 $m$ 已由对 $(F-\lambda)^m$ 的同一 Bell 实现支付。

这里不要求 $p_0-\lambda,p_1-\lambda$ 在 $\mathbb C[t]$ 中互素；
它们可以有公共非实根。
这是比原复切片互素充分条件多出的范围。

## 2. 一个奇次主模式加任意慢 first 辅助

先假设辅助 $v$ 在主首位之前的系数全为零。
令主首位系数为
$$
\alpha=a_{j_a}\in\mathbb R\setminus\{0\},
$$
辅助同位系数为 $c=c_{j_a}\in\mathbb C$，
其锚为 $\beta$。
固定 $k\ge1$，取
$$
F(U,V)=U^{2k+1}+V.
$$
两切片为
$$
p_0(t)=t^{2k+1}+\beta,\qquad
p_1(t)=(t-2\alpha)^{2k+1}+\beta-2c.
$$
写 $t=\alpha+s$，则
$$
\frac{t^{2k+1}-(t-2\alpha)^{2k+1}}{2\alpha}
=
\sum_{\ell=0}^k
\binom{2k+1}{2\ell+1}s^{2(k-\ell)}\alpha^{2\ell}.
\tag{2.1}
$$
对实 $s$，该偶多项式的常数项为 $\alpha^{2k}$，
其他系数严格正；它在 $s\ge0$ 上严格递增，
取值范围恰为
$$
[\alpha^{2k},\infty).
$$
因此两切片有公共实碰撞点，当且仅当
$$
\frac c\alpha\in(-\infty,-\alpha^{2k}].
\tag{2.2}
$$

**推论 2。**
若
$$
\boxed{\frac c\alpha\notin(-\infty,-\alpha^{2k}],}
\tag{2.3}
$$
则
$$
\boxed{
(u^{2k+1}+v-\lambda)^m e^w
\text{ 对所有 }\lambda\in\mathbb C,\ m\ge1,\ w\text{ 循环}.
}
\tag{2.4}
$$
$v$ 的其余系数可以任意复杂、任意慢地绝对可和，
$\beta$ 也可以为任意复数。
特别，同位辅助系数为零或与 $\alpha$ 同号的实数时，
(2.3) 自动成立；
同位系数 $c/\alpha$ 非实时同样成立。

若辅助有更早的首位，则联合首位的 $a=0,c\ne0$，
两切片差为非零常数 $2c$，
已由原 R147 复切片判据完成全部位移和幂；
不把这个更早支撑分支另计为新结果。

## 3. 任意支持次序的奇次减正辅助

令
$$
\alpha=a_{j_a}\ne0,\qquad \varepsilon=\operatorname{sgn}\alpha\in\{1,-1\}.
$$
现在取有限个**实系数且锚为零**的可和辅助：
$$
v_\nu=\sum_j c_{\nu j}(\chi_j-1),\qquad
c_{\nu j}\in\mathbb R,\quad c_\nu\in\ell^1.
\tag{3.1}
$$
它们的支持可以早于主行、晚于主行或完全重叠。
取任意实多项式 $R(V_1,\ldots,V_d)$ 满足
$$
R(0)=0,\qquad R(x)>0\quad(x\in\mathbb R^d\setminus\{0\}).
\tag{3.2}
$$
例如 $R(V)=\sum_\nu V_\nu^{2\ell_\nu}$，$\ell_\nu\ge1$。

**定理 3。**
对每个 $k\ge0$、每个 $\lambda\in\mathbb C$、
每个 $m\ge1$ 及每个复 $\ell^2$ 指数权 $w$，
$$
\boxed{
\left[\varepsilon u^{2k+1}-R(v_1,\ldots,v_d)-\lambda\right]^m e^w
\text{ 非零且循环}.
}
\tag{3.3}
$$

证明：辅助锚均为零。
取全部模式的联合首位 $j_0$，记其主系数 $a$ 和辅助系数向量 $c$。
相应切片差为
$$
p_0(t)-p_1(t)
=
\varepsilon\left[t^{2k+1}-(t-2a)^{2k+1}\right]
+R(-2c).
\tag{3.4}
$$
若 $j_0=j_a$，则 $a=\alpha$；
奇次幂严格递增，故对每个实 $t$，
第一项严格正，第二项非负，所以 (3.4) 严格正。
若 $j_0<j_a$，则 $a=0$、$c\ne0$；
此时 (3.4) 就是严格正的 $R(-2c)$。
两种情形都不存在实碰撞点。
定理 1 对每个 $\lambda,m,w$ 给 (3.3)。

若所有辅助恒零，则删除这些模式，
同一结论就是 R176 实结构附录的奇次幂推论。
没有使用正辅助的点态有界乘法去保持循环性；
证明仍通过真实 Bell 图和两个标量切片。

### 3.1 明确的不可约慢辅助例子

若实主行首系数 $\alpha>0$，
则对任意实 $c\in\ell^1$、$v=\sum_jc_j(\chi_j-1)$，
$$
\boxed{
(u^3-v^2-\lambda)^m e^w
\text{ 对全部 }\lambda,m,w\text{ 循环}.
}
\tag{3.5}
$$
定理 3 中 $k=0$ 的分支已由原复切片判据覆盖；奇次至少为3时才使用新增的实根约束。

主行可以是任意不规则的实 $\ell^2$ 行，
两个支持可以无限且完全重叠，
辅助无需属于 $\mathcal G$。
形式 $U^3-V^2-\lambda$ 对每个 $\lambda$ 都不可约；
这里的点态幂是整个括号的幂。

如果 $\alpha<0$，对应无条件式为
$$
(-u^3-v^2-\lambda)^m e^w.
$$
符号 $\varepsilon$ 不能删除：
对相反的符号，首位两个实切片可能有公共实根。

## 4. 与现有范围的区别

R147 慢辅助附录已证明非共振标量位移及其全部幂；
本稿删除的是其中仅由公共非实根造成的候选。
例如主首系数为1、辅助锚为0、同位系数为1时，
$U^3-V^2$ 的切片差为
$$
t^3-\left[(t-2)^3-4\right]
=6(t-1)^2+6,
$$
有两个非实零点 $1\pm i$，却没有实零点；
相应旧标量候选为 $-2\pm2i$。
原复互素判据在相应标量值仍有候选，
本稿给全部位移。

R134/R138/R155 的空谱主行交集归于旧结论；
这里的实主行也允许正负质量都不可和的全平面分支。
R236 最新双池全阶结果处理其预算下的单主共振加一次辅助，
本稿没有重新列出这些已闭二次或规则晚首范围。

定理 3 的负号、实辅助锚和实际首位均已保留。
一般 $u^3+v^2$ 的共同实碰撞，
以及任意独立无界双慢模式，
不由本稿自动解决。

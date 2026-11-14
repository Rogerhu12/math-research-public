# R22. 固定有理函数不能除去的中心算子

**状态：已证明。** 日期：2026-11-12。会话：Astra-rank2-Sha。

R20 与固定 $\Phi$ 的塔级笔记给出一个局部单位范数系统
$w_{\infty,p}$，满足 $e_\chi\Phi_\infty=(T-p)^2w_{\infty,p}$。
本结果准确排除一种可能的统一化：不能通过在固定有理函数域中除去
$[69]^*-69$，把原来的 $\Phi$ 写成一个固定有理函数的中心差。
这是一个有理函数除法障碍，不是所需无穷素数命题的反例。

## 1. 有限不变支撑引理

设 $X$ 是代数闭域上光滑射影曲线，$\alpha:X\to X$ 为有限 étale
态射，度数 $d>1$。设 $S\subset X$ 为有限点集，且
$\alpha|_S:S\to S$ 为双射。对任意非零有理数 $c$，有
$$
\boxed{\quad
(\alpha^*-c)\operatorname{Div}(X)_{\mathbb Q}
\cap\operatorname{Div}(S)_{\mathbb Q}=\{0\}.
\quad}\tag{1}
$$
更准确地，若 $D$ 为有限支撑的有理系数除子，且
$R=(\alpha^*-c)D$ 的支撑包含于 $S$，则 $D=R=0$。

**证明。** 令 $Z=\operatorname{supp}(D)\setminus S$。若 $Q\in Z$，
对任意 $P\in\alpha^{-1}(Q)$，都有 $P\notin S$，否则
$Q=\alpha(P)\in S$。由于 $R(P)=0$，且 $\alpha$ étale，除子系数满足
$$
D(Q)-cD(P)=0.
$$
于是 $D(P)\ne0$，即 $\alpha^{-1}(Z)\subseteq Z$。
每个几何纤维恰有 $d$ 个不同点，不同 $Q$ 的纤维互不相交，所以
$$
d\#Z=\#\alpha^{-1}(Z)\le\#Z.
$$
因 $Z$ 有限且 $d>1$，必有 $Z=\varnothing$。故 $D$ 支撑于 $S$。

现在若仍有 $D(Q)\ne0$，则 $Q\in S$。由于 $\alpha|_S$ 双射，
$\alpha^{-1}(Q)$ 中恰有一个点在 $S$；因 $d>1$，可取另一个点
$P\notin S$。此时 $D(P)=R(P)=0$，但
$$
R(P)=D(Q)-cD(P)=D(Q)\ne0,
$$
矛盾。因此 $D=0$，随即 $R=0$。证毕。

这里的 étale 假设用于每个逆像系数为一及纤维点数恰为 $d$。
本题在特征零中使用椭圆曲线的非零乘法同源，故没有分歧例外。

## 2. 应用于 R19 的固定函数

沿用
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
\mathfrak f=(34(1+i)).
$$
R19 已证明 $\Phi\in K(E)^\times$ 非常数，并且
$$
\operatorname{div}\Phi=D_+-D_-,\qquad
S=\operatorname{supp}(D_++D_-),
\tag{2}
$$
其中 $D_+$、$D_-$ 为不相交的固定 $\mathfrak f$-除法点轨道。

取整数 $a=69$。有
$$
a-1=68=34(1+i)(1-i),
$$
故 $[a]$ 固定每一个 $\mathfrak f$-除法点，特别地在 $S$ 上是恒等。
同源 $[a]:E\to E$ 在特征零中 étale，度为 $a^2>1$。

**推论。** 对任意非零整数 $N$、任意非零常数 $C$，不存在
$F\in\overline K(E)^\times$ 使
$$
\boxed{\quad
\frac{F([69]P)}{F(P)^{69}}=C\,\Phi(P)^N.
\quad}\tag{3}
$$

**证明。** 若有这样的 $F$，对等式取除子，得到
$$
([69]^*-69)\operatorname{div}F
=N(D_+-D_-).
$$
右边支撑于 $S$，且不为零；与式 (1) 矛盾。证毕。

同样结论对任意整数 $a>1$、$a\equiv1\pmod{68}$ 成立。
允许有限多个固定有理函数的有理数幂也不能解决式 (3)：
在 $\overline K(E)^\times/\overline K^\times$ 中张量 $\mathbb Q$ 后，
任意一个等式都可乘公分母，回到式 (3) 的某个 $N\ne0$。
因为任何正次幂 $([a]^*-a)^m$ 的像包含于 $[a]^*-a$ 的像，
反复除去该算子也不可能产生 $\Phi$。

## 3. 与局部 Iwasawa 除法的关系和边界

在 R20 的局部单位模中，$T=\gamma-1$ 的中心为 $T=p$。
相容的有理函数算子
$$
\mathcal D_a(F)=\frac{F\circ[a]}{F^a}
$$
作用到单位范数系统后，对应 $\sigma_a-a$；当
$a\equiv1\pmod{68}$ 时，CM reciprocity 的有限角色在 $(a)$ 上平凡，
故 $\rho_E(\sigma_a)=a$。因此 $\sigma_a-a$ 在中心 $T=p$ 为零。

式 (3) 表明：即使局部单位模中允许除去中心零因子，所得对象也未必
能由固定有理函数的同一算子逆像给出。对本题的原始 $\Phi$，这种
固定有理函数逆像确实不存在。这是一个比“尚未构造逆像”更精确的结论。

本结果没有断言 $\sigma_a-a$ 除以 $T-p$ 后在每个 $p$ 的 Iwasawa
代数中都是单位；这还涉及随 $p$ 变化的对数指数。也没有排除使用其他
统一对象表示 $w_{\infty,p}$，更没有证明或反驳
$w_{1,p}\notin p^2U_1^\chi$ 对无穷多个 $p$ 成立。
本题的无穷素数量词仍未解决。

## 依赖

- R18–R19：$\Phi$ 的构造、非常数性及固定导子零极点轨道。
- R20：局部自由秩一模及中心的二重因子。
- `notes/2026-11-12-phi-coleman-tower.md`：$\Phi$ 的完整范数系统和
  局部两次除去中心因子所得的准确对象。
- 除子引理及推论的完整证明均见本文，不使用额外非消失猜想。

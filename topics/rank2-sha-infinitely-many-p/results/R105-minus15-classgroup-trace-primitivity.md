# R105. 固定 −15 类群和的跨素数不可除性

固定 R103 的 $F=\mathbb Q(\sqrt{-15})$，$h_F=2$。
对合法惰性辅助素数 $\ell$，置
\[
\alpha_\ell=(3+\ell\sqrt{-15})/2,\qquad
\mathfrak r_\ell=(3,\alpha_\ell)\subset\mathcal O_\ell.
\]
由 $\alpha_\ell^2=3\alpha_\ell-3(3+5\ell^2)/4$，准确有
$\mathfrak r_\ell^2=(3)$。
其最大阶延拓非主，故它是非平凡阶二 proper 理想类。
Artin 元 $\tau_\ell$ 给实际补群
\[
\operatorname{Gal}(F[\ell]/F)
=G_\ell\times\langle\tau_\ell\rangle.
\]
因此 R100 的类群代表可统一取 $\{1,\tau_\ell\}$。

## 类群和是固定非恒定映射的值

令 $d_1,d_2:X_0(3N_E)\to X_0(N_E)$ 为两条退化映射，
并固定
\[
\Phi=\pi\circ d_1+\pi\circ d_2.
\]
$\mathfrak r_\ell$ 的次数三 CM 同源给真实点 $z_\ell$，使
\[
\Phi(z_\ell)=X_\ell:=P[\ell]+\tau_\ell P[\ell].
\]
在无穷尖点，$\Phi^*\omega_E=c(f(q)+3f(q^3))\,dq/q$，
首系数非零，故 $\Phi$ 是固定非恒定有限映射。
这一步保留两条指定退化映射；不是对全部 $T_3$ 分支求和。

CM 阶高度和固定 ample 比较于是给真实和的双边界
\[
c_1\log\ell-C\le\widehat h(X_\ell)
\le c_2\log\ell+C.
\]
并非从原点高度和三角不等式猜测和的下界。

## 每个充分大的目标 p 都有 M=1 的合法选择

CRT 与 Linnik 可取
\[
\ell\equiv7\pmod{1020},\qquad
\ell\equiv p-1\pmod{p^2},\qquad
4p-1\le\ell\ll p^{2L}.
\]
这使 $\ell$ 同时在 $F$、$\mathbb Q(i)$ 惰性，$a_\ell(E)=0$，
$v_p(\ell+1)=M_\ell=1$。
Baker 对 $E(F^{\rm ab})$ 的固定正高度下界与
$0<\widehat h(X_\ell)\ll\log p$ 给
\[
\boxed{X_\ell\notin pE(F[\ell])}
\]
对每个充分大的 $p\equiv1,17,49,53\pmod{60}$、$p\ne17$ 成立。

实际 $Y_\ell=D_\ell X_\ell$，且 $N_{G_\ell}X_\ell=0$。
仍须证明导数不可被 $p$ 整除；这比上式强，不能从范数零自动推出。
R104 的循环增广商保留了准确的剩余条件。

[完整理想、映射与高度证明](../notes/2026-11-12-minus15-classgroup-trace-primitivity.md)
已由根端逐式独审；原曲线无穷 $p$ 的 Sha 有限性仍未证明。

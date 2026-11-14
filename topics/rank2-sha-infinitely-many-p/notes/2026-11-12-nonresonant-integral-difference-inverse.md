# 非共振 tame 分量上的整差分逆像

日期：2026-11-12。**状态：已证明。**

本引理适用于普通与惰性两种形式群高度。
它把固定差分逆像在有限处的潜在非整性准确限制到共振 tame 分量，
但不证明剩余分量满足所需的大小界。

## 1. 整形式单位及连续算子

设 $p$ 为奇素数，$\mathcal O$ 为 $p$-进完备的无分歧局部整数环。
设 $\mathcal F/\mathcal O$ 为一维交换形式群，带整的 $\mathbb Z_p$
自同态作用 $[b](t)$；本题在普通处与惰性处都满足此条件。
令
$$
R=\mathcal O[[t]],\quad I=(p,t),\quad
U=1+tR,
\qquad U^N=U\cap(1+I^N).
$$
把 $U$ 按乘法看成加法记号的 $\mathbb Z_p$-模：
标量 $c\in\mathbb Z_p$ 作用为 $u\mapsto u^c$。
二项式系数 $\binom cn\in\mathbb Z_p$ 保证该作用保持 $U$，
并对 $I$-进拓扑连续。$U$ 对滤过 $U^N$ 完备且分离。

令 $\sigma_bu=u([b](t))$。若 $b\in1+p\mathbb Z_p$，则
$$
[b](t)-t\in I t.
$$
对 $u-1=\sum c_nt^n\in I^N$ 逐项展开代入可见
$$
u([b](t))-u(t)\in I^{N+1}.
$$
除以单位 $u(t)$ 后得到
$$
(\sigma_b-1)U^N\subseteq U^{N+1}.
\tag{1}
$$
所以 $\sigma_b-1$ 是这个完备滤过上的拓扑幂零算子。
此处使用乘法模的差，即 $(\sigma_b-1)u=\sigma_bu/u$；
没有把单位模误当作系数环的加法模。

## 2. 非共振块上的几何级数逆

令 $\Delta=\mu_{p-1}\subset\mathbb Z_p^\times$，通过 $\sigma_\zeta$
作用。其特征值均在 $\mathbb Z_p$ 中，所以整幂等元
$$
e_j=\frac1{p-1}\sum_{\zeta\in\Delta}\zeta^{-j}\sigma_\zeta
\qquad(j\bmod p-1)
$$
作用于 $U$，并给出 $U=\bigoplus_jU_j$。
这一式也按乘法模解释；只用 $\mathbb Z_p$ 次幂，
未对单位取一般 $\mathcal O$ 系数的次幂。

固定 $a\in\mathbb Z_p^\times$，写
$a=\omega(a)\langle a\rangle$。
在 $U_j$ 上有
$$
\sigma_a-a
=(\omega(a)^j-a)+\omega(a)^jB,
\qquad B=\sigma_{\langle a\rangle}-1.
\tag{2}
$$
若
$$
\omega(a)^{j-1}\ne1,
\tag{3}
$$
则 $d_j=\omega(a)^j-a\in\mathbb Z_p^\times$。
由 (1)，级数
$$
(\sigma_a-a)^{-1}
=d_j^{-1}\sum_{n\ge0}
\left(-\frac{\omega(a)^j}{d_j}\right)^n B^n
\tag{4}
$$
在 $U_j$ 上收敛，且保持每个 $U^N\cap U_j$。
有限几何级数恒等式及完备性证明它确实为双侧逆。

因此，对每个 $m\ge1$ 和 $\eta_j\in U_j$，存在唯一
$v_j\in U_j$ 使
$$
(\sigma_a-a)^m v_j=\eta_j.
\tag{5}
$$
用通常乘法记号，左端是重复的 $v\mapsto(v\circ[a])/v^a$。
式 (4) 已证明解是**整形式单位**，不只是一个形式对数的解。

## 3. 与固定零线性系数解的比较

设本题 $\Phi(t)\in1+t\mathcal O[[t]]$，
$\delta\log\Phi(O)=0$，并令 $F_{m,0}$ 为 R28 的固定形式解。
在形式对数坐标 $z=\log_{\mathcal F}(t)$ 中，$\sigma_\zeta$
作用为 $z\mapsto\zeta z$，所以 $e_j\log F_{m,0}$ 只保留
$k\equiv j\pmod{p-1}$ 的项。

对满足 (3) 的 $j$，必有 $j\ne1$。
取 $\eta_j=e_j\Phi$，由上节得到整解 $v_j$。
其一次对数系数为零，因为它属于非 $j=1$ 分量。
在每个 $k\equiv j$ 上，$a^k-a\ne0$，而形式差分方程逐系数唯一解为
$$
[z^k]\log v_j=
\frac{[z^k]\log\Phi}{(a^k-a)^m}.
$$
因此
$$
\boxed{\quad e_jF_{m,0}=v_j\in1+t\mathcal O[[t]]
\quad\text{当 }\omega(a)^{j-1}\ne1.\quad}
\tag{6}
$$
这里在尚未知整的 $F_{m,0}$ 上取幂等元，先按特征零形式对数定义；
比较证明其结果恰等于上节独立构造的整单位。

## 4. 得到的正向范围与保留缺口

若 $d_p=\operatorname{ord}_{\mathbb F_p^\times}(a)$，
式 (6) 已处理所有 $d_p\nmid j-1$ 的分量。
只有满足
$$
d_p\mid j-1
$$
的共振块可能造成非整性。
这同时排除了一个过于悲观的判断：取乘法指数并不必然在所有分量
造成高度一的半径损失；非共振块中这种整性相消已由 (4) 完整证明。

但该引理不能消去共振块。
当 $a$ 在模 $p$ 下为原根时，恰只剩 $j=1$；
一般还会留下其他 $j$。
普通处的 Selmer 中心零阶控制目标 $j=1$，
而惰性处尚无把该假设转成这些整形式单位共振块可除性的比较。
首个可能非整系数及其图像大小后果，见
`2026-11-12-inert-height-two-difference-jets.md`。

本引理不要求本题无穷素数结论，也不使用非 Wieferich 素数无穷性。

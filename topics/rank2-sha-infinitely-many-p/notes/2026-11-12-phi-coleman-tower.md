# 固定 $\Phi$ 的完整范数塔与整的 Frobenius 对数差

**可信度：本文恒等式及塔级比较已证明。** 本文继续 R19、R20，直接使用固定函数
$$
\Phi(t)=\frac{N_{M/K}(1+\alpha t)}{N_{M/K}(1-\alpha t)},
\qquad t=-x/y,
$$
其中 $K=\mathbb Q(i)$、$E:y^2=x^3-17x$，$M,\alpha$ 是 R18 的固定数据。仍设 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$，
$\pi_E=\psi(\mathfrak p)$，并置
$$
P_n=\xi(\Omega/\pi_E^n),\quad K_n=K(E[\mathfrak p^n]),
\quad\varepsilon_n=\Phi(P_n).
$$

本次实际推进是：$\Phi$ 本身给出完整的全局单位范数系统，不必先经辅助函数 $\Lambda$ 才定义各层；它的整的 Coleman 对数差及有理导数均可明确写出。最后说明这一表达式中随 $p$ 增长的对象在哪里。

## 1. $\Phi(P_n)$ 在每一层都是全局单位

R19 已证明固定有理函数恒等式
$$
\frac{\Lambda(P)}{\Lambda(-P)}
=\left(\frac{\Phi([-7]P)}{\Phi(P)^{49}}\right)^{12}.
\tag{1.1}
$$
Rubin Proposition 7.8 说明 $\Lambda(P_n)$ 及 $\Lambda(-P_n)$ 均为 $K_n$ 的全局单位。令 $J_n=(\varepsilon_n)$ 为 $K_n$ 的分式主理想，并令 $\sigma_7\in\operatorname{Gal}(K_n/K)$ 在 $E[\mathfrak p^n]$ 上作用为 $\psi((7))=-7$。对 (1.1) 取理想，得到
$$
12(\sigma_7-49)J_n=0
$$
（理想群用加法记号）。分式理想群无挠，故
$\sigma_7J_n=49J_n$。若 $\sigma_7$ 的阶为 $d$，反复应用该等式给
$$
J_n=49^dJ_n.
$$
再次利用无挠性得到 $J_n=0$。因此
$$
\boxed{\ \varepsilon_n\in\mathcal O_{K_n}^{\times}\quad(n\ge1).\ }\tag{1.2}
$$
这同时处理所有素位，包括 $2$、$17$；没有从“局部是单位”推断全局单位。

## 2. 不带未定常数的分布公式

R19 给出
$$
\operatorname{div}\Phi=D_+-D_-,
\qquad
\Phi(O)=1,\qquad\Phi(-P)=\Phi(P)^{-1},
\tag{2.1}
$$
其中 $D_\pm$ 分别是固定 $\mathfrak f$-除法点的 Galois orbit 及其负点的和。两组点互不相交。CM reciprocity 使 $[\pi_E]$ 置换 $D_+$ 和 $D_-$，所以
$$
[\pi_E]_*\operatorname{div}\Phi=\operatorname{div}\Phi.
$$
于是
$$
\operatorname{div}\prod_{T\in E[\mathfrak p]}\Phi(P+T)
=[\pi_E]^*\operatorname{div}\Phi
=\operatorname{div}\Phi([\pi_E]P).
$$
两函数之比为常数。在 $P=O$，核中的非零点按 $T,-T$ 配对，每对的乘积为一；$O$ 的因子也为一。所有值都有限非零，因为 $\mathfrak p$ 与 $\mathfrak f$ 互素。故常数恰为一：
$$
\boxed{\quad
\prod_{T\in E[\mathfrak p]}\Phi(P+T)=\Phi([\pi_E]P).
\ }\tag{2.2}
$$

$\operatorname{Gal}(K_{n+1}/K_n)$ 对 $P_{n+1}$ 的轨道正是
$P_{n+1}+E[\mathfrak p]$。代入 (2.2)，得到精确范数关系
$$
N_{K_{n+1}/K_n}\varepsilon_{n+1}=\varepsilon_n
\qquad(n\ge1).
\tag{2.3}
$$
因此 $\varepsilon_\infty=(\varepsilon_n)_n$ 是全局单位的范数相容系统。

## 3. $\chi$ 分量上直接生成椭圆单位模

沿用 R20 的 $\Delta,\Gamma$、$\widetilde\chi=\rho_E|_\Delta$、
$\mathcal A=\mathbb Z_p[[\Gamma]]$，以及 $\rho_E(\gamma)=1+p$、$T=\gamma-1$。令 $\eta_\infty$ 为 R16、R20 的 Rubin 单位系统。

(1.1) 在各层相容，故对整个范数系统有
$$
(1-\sigma_{-1})\eta_\infty
=12(\sigma_7-49)\varepsilon_\infty.
$$
由于 $\widetilde\chi(\sigma_{-1})=-1$，得到
$$
e_\chi\eta_\infty
=6(\sigma_7-49)e_\chi\varepsilon_\infty.
\tag{3.1}
$$
$\sigma_7-49$ 在 $\mathcal A$ 的剩余域中的值为 $-56$，而 $6$ 也为单位。因此 (3.1) 的乘子是 $\mathcal A^\times$ 中的元素。

R20 已证明 $C_\infty^\chi=\mathcal A e_\chi\eta_\infty$，所以进一步有
$$
\boxed{\ C_\infty^\chi=\mathcal A e_\chi\varepsilon_\infty.\ }\tag{3.2}
$$
在第一层，该乘子化为 $6(\widetilde\chi(\sigma_7)-49)$，其模 $p$ 为 $-336$。因此 R16 的全局字符单位深度 $m_p$ 以及局部深度 $\nu_p$ 都可用 $\Phi(P_1)$ 直接计算，分别在相同的全局格、局部格中衡量。第一层的全局格结论使用了 §1 的完整全局单位性。

## 4. 固定 $\Phi(t)$ 就是其 Coleman 幂级数

R18 证明 $\alpha$ 在所有 $p\nmid34$ 的素位上都是单位。故
$N_{M/K}(1\pm\alpha t)$ 的系数在 $\mathcal O_{K,\mathfrak p}=\mathbb Z_p$ 中，常数项为一，从而
$$
\Phi(t)\in1+t\mathbb Z_p[[t]].
\tag{4.1}
$$
又因 $\operatorname{Tr}_{M/K}\alpha=0$，其实 $\Phi(t)\in1+t^3\mathbb Z_p[[t]]$。把 (2.2) 限制到形式群即可看出其 Coleman 范数不变性。它在所有 $t(P_n)$ 的值均为 $\varepsilon_n$，所以按 Coleman 的存在唯一性定理，该范数系统的 Coleman 幂级数就是这个固定有理函数的展开；不需要另选一个未知的插值级数。参见 Rubin Remark 12.5 所述 Coleman 定理。

这里固定的是形式参数 $t=-x/y$ 及该有理函数。其 $p$-进 Mellin 变换的变量仍是 R20 中随 $p$ 定义的 $\Gamma$ 参数，不因 (4.1) 而自动变成一个固定的有理函数。

## 5. 整的 Frobenius 对数差及有理导数

定义
$$
\mathcal C_p\Phi(t)
=\frac1p\log\frac{\Phi(t)^p}{\Phi([\pi_E](t))}
=\log\Phi(t)-\frac1p\log\Phi([\pi_E](t)).
\tag{5.1}
$$
所有形式对数在 $t=0$ 取常数项零。因为
$[\pi_E](t)\equiv t^p\pmod p$，(4.1) 给出
$$
\Phi([\pi_E](t))
\equiv\Phi(t^p)\equiv\Phi(t)^p\pmod p.
$$
故对数内的商属于 $1+pt\mathbb Z_p[[t]]$；$p$ 为奇数，所以
$$
\boxed{\ \mathcal C_p\Phi(t)\in t\mathbb Z_p[[t]].\ }\tag{5.2}
$$
其整性涉及整个对数差，不能分别声称 $\log\Phi(t)$ 的所有系数都整。

令 $\delta$ 为不变导子，R19 给出 $\delta\log\Phi=2S$。链式法则以及 $[\pi_E]^*\omega=\pi_E\omega$ 得到
$$
\boxed{\quad
\delta\mathcal C_p\Phi
=2S-2\bar\pi_E^{-1}S\circ[\pi_E].
\ }\tag{5.3}
$$
右边是明确的有理函数。对任意 $j\ge1$，
$$
\delta^j\mathcal C_p\Phi(O)
=\left(1-\frac{\pi_E^j}{p}\right)
\delta^j\log\Phi(O).
\tag{5.4}
$$
在 $P_1$ 处，$[\pi_E]P_1=O$，且这些级数收敛，所以还有精确的有限层等式
$$
\mathcal C_p\Phi(t(P_1))=\log_p\Phi(P_1).
\tag{5.5}
$$
因此 R16/R19 的局部投影可以直接作用于 (5.1) 这个整幂级数。

分布公式还给出其 trace-zero 性：
$$
\sum_{T\in E[\mathfrak p]}
\mathcal C_p\Phi(P+T)=0
\tag{5.6}
$$
在形式邻域中成立。证明是把 (2.2) 取对数，而第二项的 $p$ 个值均为
$p^{-1}\log\Phi([\pi_E]P)$。这些恒等式是可用于后续低层 Cartier/系数计算的实质输入，不需要舍去任何高阶项。

## 6. 两次除去中心因子所得的准确局部对象

R20 证明 $U_\infty^\chi$ 自由秩一，且椭圆单位的坐标被 $(T-p)^2$ 整除。(3.1) 的乘子是单位，故存在唯一
$$
w_{\infty,p}\in U_\infty^\chi
\quad\text{使}\quad
e_\chi\varepsilon_\infty=(T-p)^2w_{\infty,p}.
\tag{6.1}
$$
唯一性来自 $U_\infty^\chi$ 无 $\mathcal A$ 挠。第一层取 $T=0$ 后，得到
$$
e_\chi\Phi(P_1)=p^2 w_{1,p}.
\tag{6.2}
$$
所以 $w_{1,p}$ 在 R16 的局部单位格中的深度恰为 $\nu_p-2$。若采用 R20 的同一个生成元 $u_\infty$ 及 $h_p=(T-p)^2g_p$，则准确地有
$$
w_{1,p}=
\bigl[6(\widetilde\chi(\sigma_7)-49)\bigr]^{-1}
g_p(0)u_1.\tag{6.3}
$$

(6.1) 给出的系统属于**局部**单位范数极限。虽然 $\varepsilon_\infty$ 是全局单位系统，除以 $(T-p)^2$ 并未证明 $w_{\infty,p}$ 仍在全局单位子模中。因此目前不能把 $w_{1,p}$ 视为某个固定全局单位的值，再对它应用固定数域的单位定理或高度估计。

## 7. 已定位的随 $p$ 增长部分

(5.3) 虽然完全显式，其第二项使用度为 $p$ 的同源。这个增长可以由极点直接计数，不能因 $[\pi_E]$ 在原来的 $\mathfrak f$-除法 orbit 上作有限置换而删除。

具体地，$S=\frac12\delta\log\Phi$ 在 $D_++D_-$ 的各点有简单极点；这些点共 $512$ 个。特征零下 $[\pi_E]$ 无分歧，所以 $S\circ[\pi_E]$ 的极点集是它们的全部 $p$ 个逆像，共 $512p$ 个。原来的 $512$ 个点包含在该逆像集中，因为 $[\pi_E]$ 置换它们。在其余 $512(p-1)$ 个点，(5.3) 的第一项无极点，故无法相消。于是 (5.3) 至少具有
$$
512(p-1)
$$
个简单极点。

这排除了将这个**具体的 Frobenius 对数差导数**认作来自一个固定有限有理函数集合的做法。它不排除某些特殊迹或低阶同余另有简化；但那种简化必须额外证明。当前仍未证明 $w_{1,p}$ 在无穷多个 $p$ 处不属于 $p^2U_1^\chi$。

## 来源与依赖

- 本题 R18、R19：固定 $\Phi$、$\alpha$ 的整性、零极点以及与 $\Lambda$ 的函数恒等式。
- 本题 R20：完整局部范数控制、$\mathcal A$-自由性、辅助理想乘子的单位性与中心二重因子。
- K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，[作者讲义](https://swc-math.github.io/notes/files/99RubinCM.pdf)：Proposition 7.8、Definition 8.1、Propositions 8.2、11.6，以及 Remark 12.5 中的 Coleman 幂级数定理。

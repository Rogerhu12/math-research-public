# R830 — 原惰性一次原函数的角字符 Hecke lift 与严格 tame filtration

**状态：已证明。** 对每个原允许的 $p\ge41,\ p\equiv11\pmod {12}$，R826/GC 的一次原函数约化有一个准确的权六 Gaussian Hecke theta lift；它的导子新增真正的 $p$ 因子，level 为 $36p^2$ 或 $144p^2$。其约化 $q$ 级数在任意与 $p$ 互素的共同 tame level 上的 Katz filtration 恰为 $6p$，因而不能改作该 tame level 上的全纯权六形式。

这不证明指定原 $j=0$ CM 组合非零。这里的 Gaussian 角字符也不是未经运输即可替换原 R770 标签的 Eisenstein 角色。

来源为 [GC 原 Gaussian 射线类分解](../notes/2026-11-15-sigma-inert-Gaussian-rayclass-source.md)、[R826 companion 比较](R826-original-inert-companion-theta-CM-pairing.md)、[R828 原源正负分解](R828-original-inert-two-primary-parity-and-old-source.md)。Hecke theta 的权、level 与 nebentype 使用 GC 已核的 Matthias Schütt, *CM newforms with rational coefficients*, 2009（[arXiv:math/0511228v5](https://arxiv.org/abs/math/0511228)）, Theorem 1.4；没有假设本文系数为实数。

## 1. 固定原相位和选定的 $p$ 整 place

令 $K_{\rm G}=\mathbb Q(i)$、$\mathcal O=\mathbb Z[i]$。保留 GC 的四个有限字符
$$
 \epsilon_3,\ \epsilon_7,\ \delta\epsilon_1,\ \delta\epsilon_5,
 \qquad \epsilon_b(1+i)=\xi_8^b,\quad \xi_8=(1+i)/\sqrt2.
 \tag{830.1}
$$
它们的原导子依次为 $(3),(3),(6),(6)$；对所有 $u\in\mathcal O^\times$，都有 $\epsilon(u)=u$。分别仍记对应权八形式为 $F_3,F_7,G_1,G_5$。

由于 $p\equiv3\pmod4$，
$$
 \mathcal O/p\mathcal O=\mathbb F_{p^2}.
$$
固定与 R826 相同的 $p$ 上 place、Gaussian 嵌入和八次单位根。取包含这些值的非分歧 $p$ 整整数环 $\mathcal R$；其剩余域可取为 $\mathbb F_{p^2}$，因为 $8\mid p^2-1$。Teichmüller 提升记为
$$
 \omega_p:\mathbb F_{p^2}^{\times}\longrightarrow
                 \mu_{p^2-1}(\mathcal R).
$$
对 $p\nmid w$ 定义
$$
 \chi_p(w)=\omega_p(w\bmod p)^{\,1-p}.
 \tag{830.2}
$$
于是 $\chi_p$ 只依赖 $w\bmod p$，其精确阶为
$$
 \frac{p^2-1}{\gcd(p^2-1,p-1)}=p+1.
 \tag{830.3}
$$
它在 $(\mathbb Z/p\mathbb Z)^\times$ 上平凡。对 Gaussian 单位，所选 Teichmüller 提升保持原单位，故
$$
 \chi_p(u)=u^{1-p}=u^2,\qquad
 \epsilon(u)\chi_p(u)u^5=u^8=1.
 \tag{830.4}
$$
这些等式是在固定 place 中核定的；不另施 Frobenius 于 $\epsilon$ 的八次单位根值。

## 2. 真正新增导子 $p$ 的权六 Hecke theta

对非零整理想 $\mathfrak a=(w)$，且 $(\mathfrak a,p\mathfrak f_\epsilon)=1$，置
$$
 \psi_{\epsilon,p}(\mathfrak a)
   =\epsilon(w)\chi_p(w)w^5.
 \tag{830.5}
$$
(830.4) 证明它与生成元选择无关。其无穷型是 $(5,0)$；有限部分的导子准确为
$$
 \mathfrak f_\epsilon\,(p).
 \tag{830.6}
$$
这是精确导子：$\epsilon$ 原来在 $2,3$ 部分本原，$\chi_p$ 在模 $p$ 的单位群上非平凡，且二者导子互素，不能相互抵消。

定义理想求和（每个理想只取一次）
$$
 H_{\epsilon,p}(t)=
  \sum_{\substack{\mathfrak a=(w)\ne0\\
                   (\mathfrak a,p\mathfrak f_\epsilon)=1}}
       \epsilon(w)\chi_p(w)w^5t^{N\mathfrak a}.
 \tag{830.7}
$$
它是全纯权六 Hecke theta 新形式，其 level 为
$$
 |D_{K_{\rm G}}|\,N(\mathfrak f_\epsilon(p))
 =\begin{cases}
  36p^2,&\epsilon=\epsilon_3,\epsilon_7,\\
  144p^2,&\epsilon=\delta\epsilon_1,\delta\epsilon_5.
 \end{cases}
 \tag{830.8}
$$
nebentype 仍为原 $\chi_{12}$：有限字符 $\chi_p$ 在有理单位上平凡，所以没有新增的有理 Dirichlet 字符。其首项为 $t$，全部 Fourier 系数在 $\mathcal R$ 中。并且
$$
 U_pH_{\epsilon,p}=0
 \tag{830.9}
$$
在特征零已成立，因为本求和排除了 $(p)$，而 Gaussian 惰性使 $p\mid Nw$ 等价于 $p\mid w$。

这里没有从原权八形式直接删去 $p$ 项后假称权降为六；(830.5)--(830.8) 给出了真正的 Hecke 字符和新增的 level。

## 3. 与原一次原函数的逐项相等

仍取原
$$
 f_\epsilon(t)=\sum_{\mathfrak a=(w),(\mathfrak a,\mathfrak f_\epsilon)=1}
                 \epsilon(w)w^7t^{N\mathfrak a},
 \qquad
 J_\epsilon(t)=\sum_{n\ge1}\frac{a_\epsilon(n)}n t^n.
 \tag{830.10}
$$
先核分母。若 $w=p^av$、$p\nmid Nv$，则同一个理想项为
$$
 \frac{\epsilon(w)w^7}{Nw}
 =\epsilon(p)^a p^{5a}
       \frac{\epsilon(v)v^7}{Nv}.
 \tag{830.11}
$$
所以 $J_\epsilon$ 在所选 place 整；所有 $p\mid Nw$ 项约化为零，不能把其分母先改成模 $p$ 的零再相除。

若 $p\nmid Nw$，则在 $\mathbb F_{p^2}$ 中 $w^p=\bar w$，从而
$$
 \overline{\chi_p(w)}=w^{1-p}=\frac{w}{\bar w},
$$
$$
 \epsilon(w)\overline{\chi_p(w)}w^5
   =\frac{\epsilon(w)w^7}{w\bar w}.
 \tag{830.12}
$$
每个范数对应有限个理想，故逐项相加合法，得到
$$
 \boxed{\ \overline{J_\epsilon}=\overline{H_{\epsilon,p}}.\ }
 \tag{830.13}
$$

保留原八标签
$$
 (F_3,1),(F_3,2),(F_3,4),
 (F_7,1),(F_7,2),(F_7,4),(G_1,1),(G_5,1).
$$
对 $\nu=(\epsilon,d)$ 置
$$
 \mathscr H_{\nu,p}(t)=\frac1dH_{\epsilon,p}(t^d).
 \tag{830.14}
$$
原一次原函数是 $\mathscr J_\nu=d^{-1}J_\epsilon(t^d)$，故
$$
 \boxed{\ \overline{\mathscr J_\nu}
                =\overline{\mathscr H_{\nu,p}}.\ }
 \tag{830.15}
$$
所有 $d=1,2,4$ 均为 $p$ 单位。这里的因子是 $1/d$，不改成 $d^{-6}$；后者属于 R826 的 companion oldform，而非一次原函数。

## 4. 其 tame 权准确为 $6p$

R826 给出了全纯权 $k=p-5$、tame level 的 companion
$$
 C_{\epsilon,p}(t)
  =\sum_{\mathfrak a=(w)}
        \epsilon(w)\bar w^{\,p-6}t^{N\mathfrak a},
 \qquad
 C_{\nu,p}(t)=d^{p-7}C_{\epsilon,p}(t^d),
 \tag{830.16}
$$
以及
$$
 \theta_t^5\overline{C_{\nu,p}}
  =\overline{\mathscr J_\nu}
  =\overline{\mathscr H_{\nu,p}}.
 \tag{830.17}
$$
其中 $C_{\epsilon,p}$ 首系数为 $1$；oldform 的首个非零系数为单位 $d^{p-7}$。所以每个 $\overline{C_{\nu,p}}$ 都非零。

在任一与 $p$ 互素、包含这些原 tame 形式的共同全 level 上，令 $A$ 为 Hasse invariant。它的权是 $p-1$，$q$ 展开为 $1$，零除子是全部 supersingular 点，每点为简单零。

每个 $C=\overline{C_{\nu,p}}$ 必在某个 supersingular 点不为零。否则 $C/A$ 在非尖点因简单零而正则，在各尖点因 $A$ 是单位而正则，从而得到一个权
$$
 (p-5)-(p-1)=-4
$$
的非零全纯形式。这不可能：在紧化 fine modular curve 上，Hodge 线丛有正次数，所以其负次幂没有非零全局截面。

固定这样一个点 $x$。在原判别式标架及一个共同 tame 覆盖上，R826 的准确 Katz theta 运输是
$$
 \mathcal T_j(v)=A\,Dv+j(DA)v.
 \tag{830.18}
$$
这里 $\mathcal T_j$ 准确运输的是 $\theta_q$，不是直接运输 $\theta_t$。沿本链原 $t=q_*=q^{1/12}$，有 $\theta_t=12\theta_q$；故 R826 (826.21)--(826.22) 的五次运输在 (830.20) 那五个算子乘积之前保留因子 $12^5$。它在所有允许 $p$ 下是单位，以下只用非零性时仍保留这一规范。

因 $A$ 在 $x$ 简单消失，且该标架的 $D$ 在非尖点无零，故 $DA(x)\ne0$。对所有正则 $v$，
$$
 \mathcal T_j(v)(x)=j\,DA(x)\,v(x).
 \tag{830.19}
$$
五次 theta 的输入权为
$$
 p-5,\quad2p-4,\quad3p-3,\quad4p-2,\quad5p-1.
 \tag{830.20}
$$
它们模 $p$ 分别为 $-5,-4,-3,-2,-1$，均非零。每一步的输出仍正则，所以
$$
 \theta_t^5 C(x)\ne0
 \tag{830.21}
$$
在相应输出标架中成立。输出权准确为
$$
 (p-5)+5(p+1)=6p.
 \tag{830.22}
$$

现在若在某个与 $p$ 互素的 level 上存在全纯权六形式 $H$，其 $q$ 展开等于 (830.17)，就拉到共同 fine level。$A^6H$ 与 $\theta_t^5C$ 都是权 $6p$，且 $q$ 展开完全相同。由该全层上的 $q$ 展开原理，
$$
 \theta_t^5C=A^6H.
 \tag{830.23}
$$
右侧在每个 supersingular 点为零，与 (830.21) 矛盾。

为说明这里的严格 filtration 用语，同一个非零 $q$ 级数的两个 tame 权必同余模 $p-1$。可在共同 fine level 的 Igusa 覆盖上用 $A=1$ 平凡化 Hodge 标架：该 $\mu_{p-1}$ 覆盖连通，因为紧化后在 Hasse 的任一简单零处具有完全的 $p-1$ 阶惯性；两个相同 $q$ 展开的函数在这条连通曲线上相同，而 $\mu_{p-1}$ 对它们的作用分别是两个权字符，故两个权同余。若某个较低非负权 $k'$ 实现同一展开，则 $6p-k'=r(p-1)$，其中 $r\ge1$。同权 $q$ 展开原理将给 $\theta_t^5C=A^rH'$，再次与 (830.21) 矛盾。

因此这一 $q$ 级数在任意共同 tame level 上的 Katz filtration 恰为 $6p$；尤其
$$
 \boxed{\ \text{不存在全纯 tame 权六形式实现 }
            \overline{\mathscr H_{\nu,p}}\text{ 的同一 }q\text{ 级数。}\ }
 \tag{830.24}
$$
这不是只比较不同权的形式符号，而是先用 $A$ 配到同权，再用全层 $q$ 展开原理得出矛盾。也没有使用某个尚未确定的固定 $j=0$ 点值。

## 5. 对原 CM 源的准确含义

R826 的原尺度和原点为
$$
 \mathcal P=\lambda^{6p}/d_0,\qquad P_0=(0,4),
$$
$$
 e_{\nu,p}
 =-\frac{120\,12^5}{d_0}B^5\,
        \mathscr C_{\nu,p}(P_0).
 \tag{830.25}
$$
由 (830.15)，原 $e_{\nu,p}$ 的 $q$ 表达也可以写成
$$
 \left[\frac{\lambda^{6p}}{d_0}\,
          \overline{\mathscr H_{\nu,p}}(q_*)\right]_{\rm alg}(P_0),
 \qquad q_*=q^{1/12}.
 \tag{830.26}
$$
这里的代数延拓仍是 R826 通过 tame 权 $6p$ 的 $\theta^5C$ 所定义的那个延拓。不能把 (830.26) 拆成 $A^6$ 乘上一个自行假定在同一 tame supersingular 点正则的 $\lambda^6H$。新增 $p$-level 的特殊纤维、标架和下降并未由一个 $q$ 级数等式自动提供，(830.24) 正好排除了这种全局 tame 权六替代。

R828 已证明两个原 $G$ 通道的指定 CM 值为零；余下仍是原六个 old 值的 FG 组合。本文只证明这些 once-primitive 级数与真正角字符 Hecke 形式的关系及其全局权限制。第 4 节找到的某个 supersingular 非零点不保证就是原 $P_0$，也不保证六项 FG 组合无相消。

最后，$\chi_p$ 的精确阶 $p+1$ 是 Gaussian 残域角字符的事实。原 R770 的 $h$ 是另一套 Eisenstein period/torus 标记；没有证明它与本篇 $\chi_p$ 给出所需的同标签单位。因此本文不推出
$$
 P_{6i+6}(1/s)f_i g_{N-1-i}\ne0
$$
的原 primitive/Legendre 结论，不新增素数窗口。

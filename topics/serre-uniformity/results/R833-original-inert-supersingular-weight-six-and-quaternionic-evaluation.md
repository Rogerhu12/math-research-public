# R833 — 原惰性 companion 的同点超奇异权六与四元数评价

**状态：已证明原对象运输。** 设 $p\ge41$ 为原允许素数，且 $p\equiv11\pmod{12}$。R826 的八个权 $p-5$ companion 在同一 supersingular locus 上，经一个准确的 Frobenius 半线性变换成为权六截面。它们的原 $P_0$ 评价给出原未筛交替卷积；共同尺度、原 Miller 系数和 oldform 因子全部保留。其 Hecke 特征准确等于 R830 指定的 conductor-$p$ 权六 Hecke theta 的约化特征，其中有限角色按 $p\bmod24$ 交换。

这不是指定 CM 和的非零证明，也不是把相同 Hecke 特征误认作已确定的特征零 Jacquet–Langlands test vector。

## 1. 原规范与使用的 Serre 事实

保留 [R826](R826-original-inert-companion-theta-CM-pairing.md)、[R826 实际八源运输](R826-certified-inert-Gaussian-source-transport.md)、[R828](R828-original-inert-two-primary-parity-and-old-source.md) 和 [R830](R830-original-inert-angular-Hecke-lift-and-tame-filtration.md) 的全部原对象。八标签依次为
$$
 (F_3,1),(F_3,2),(F_3,4),
 (F_7,1),(F_7,2),(F_7,4),(G_1,1),(G_5,1).
 \tag{833.1}
$$
在 R826 的共同 tame fine level 上，$C_{\nu,p}$ 是权 $k=p-5$ 的整模形式，其 oldform 定义仍是
$$
 C_{\nu,p}(t)=d^{p-7}C_{\epsilon,p}(t^d).
 \tag{833.2}
$$
实际沿原 $q_*=q^{1/12}$ 使用它；若以一个固定的全层表示所有对象，可沿用 R826 的 level $1728$ 及已选定的常数字段、点和标架。

记 $\omega$ 为 Hodge 线丛，$Z_{\rm ss}$ 为这个全层曲线的 supersingular 零维子概形，记
$$
 \mathcal S_j=H^0(Z_{\rm ss},\omega^j).
$$
负次幂在这里也有意义。固定同一个剩余域代数闭包，所有 $p$ 次幂都是其绝对 Frobenius，不另换原 $i,\xi_8,d_0$ 的嵌入。

使用的原始文献是 Jean-Pierre Serre, *Letter to J. Tate, 7 August 1987*，发表于 *Two letters on quaternions and modular forms (mod p)*, Israel J. Math. 95 (1996)：
[Alexandru Ghitza 提供的全文英译](https://aghitza.github.io/publications/translation-serre-letter-tate.pdf)。

所用位置准确为：

- 第 2 页的 (2)--(3)：Hasse 除子上的限制序列，以及带 $1/\ell$ 的 Hecke 同源 求和；
- 第 3 页的 (4)--(5)：$\mathcal S_j$ 的 $p^2-1$ 周期、$E_{p+1}$ 的处处非零 supersingular 限制及乘法的 Tate twist；
- 第 4 页的 (9)：有限四元数双陪集与 $(E,\omega_E,\alpha)$ 的对应，保留不变微分和 tame level 结构；
- 第 6 页的 (13)：乘 cyclotomic reduced-norm 函数使 $T_\ell$ 特征乘以 $\ell$，明确核定本篇 (833.20) 的 twist 方向。

以下也明确核定 Hecke twist 的方向，避免仅凭符号 $[1]$ 猜正负。

令 $\mathcal A$ 为 $q$ 展开为 $1$ 的 Hasse invariant，令
$$
 \beta=\overline{E_{p+1}}\big|_{Z_{\rm ss}}.
 \tag{833.3}
$$
它是 $\omega^{p+1}$ 的处处非零截面。因此乘任意整数次 $\beta$ 都在相应 $\mathcal S_j$ 间给出同构。Serre 的周期截面正是 $\beta^{p-1}$。

## 2. 原 Hasse 标架中 $\beta$ 的准确值

Kummer 的标准 Bernoulli 同余
$$
 \frac{B_{p+1}}{p+1}\equiv\frac{B_2}{2}=\frac1{12}\pmod p
$$
以及 $\sigma_p(n)\equiv\sigma_1(n)\pmod p$ 给出
$$
 \overline{E_{p+1}}=E_2
 \tag{833.4}
$$
的模 $p$ $q$ 展开等式。分母是合法的：$B_{p+1}/(p+1)$ 在本处整且约化为单位。这里 $E_2$ 作为 $q$ 级数出现，不被当作特征零全纯权二模形式。

等价地，若 $\partial_j=\theta_q-jE_2/12$ 是 Serre 导数，则
$$
 12\,\partial_{p-1}\mathcal A
       =\overline{E_{p+1}}
 \tag{833.5}
$$
是同权 $p+1$ 的全层模形式等式：两边 $q$ 展开均为 $E_2$。Hasse 的简单零和 Kodaira–Spencer 也直接表明其限制在 $Z_{\rm ss}$ 上非零。

保留 R826 的原标架
$$
 \lambda=d_0\eta^{-2},\qquad d_0^{12}=-432,\qquad
 D=\lambda^2\theta_q,\qquad
 A=[\lambda^{p-1}\mathcal A]_{\rm alg}.
 \tag{833.6}
$$
R826 已逐项证明
$$
 DA=[\lambda^{p+1}E_2/12]_{\rm alg}.
$$
所以 $\beta$ 在同一标架中的表达 $\widehat\beta$ 准确是
$$
 \widehat\beta
  =[\lambda^{p+1}\overline{E_{p+1}}]_{\rm alg}
  =12DA.
 \tag{833.7}
$$
在原点 $P_0=(0,4)$，
$$
 \widehat\beta(P_0)=12B\in\mathbb F_p^\times.
 \tag{833.8}
$$
这里 $B=DA(P_0)$ 是 R826/R574 的同一个 Cartier 单位，未重新归一。[原 MH 笔记](../notes/2026-11-15-sigma-modular-heat-connection-and-odd-tame-trivialization.md) §7、(MH33) 已明确给
$$
 B=(-1)^{N+1}\binom{3N+2}{2N+1}\in\mathbb F_p^\times,
 \qquad p=6N+5,
$$
以及 $(\partial_a A)(0,4)=B/24$、$DA(P_0)=B$；因此 (833.8) 的 $\mathbb F_p$ 归属也保持原来源。

(833.6)--(833.7) 先作为同权截面的 $q$ 恒等式证明，再在 supersingular 点评价。没有先给 $\lambda$ 或 $\eta$ 单独指定一个虚假的 supersingular 点值。

## 3. 权六的同点半线性运输

对每个原标签定义
$$
 \boxed{\quad
 \Gamma_{\nu,p}
   =\beta^{\,6-p}\,
        (C_{\nu,p}|_{Z_{\rm ss}})^p
       \ \in\mathcal S_6.
 \quad}
 \tag{833.9}
$$
权数核对为
$$
 (p+1)(6-p)+p(p-5)=6.
 \tag{833.10}
$$
因此这不是把不同权截面直接相加；负的 $\beta$ 次幂在 $Z_{\rm ss}$ 合法，因为 $\beta$ 处处为单位。

在代数闭剩余域上，(833.9) 是 Frobenius 半线性双射
$$
 \mathcal S_{p-5}\longrightarrow\mathcal S_6.
 \tag{833.11}
$$
逆映射是先乘 $\beta^{p-6}$，再取唯一的 Frobenius 逆；其含义是截面线丛的半线性逆，而不是任意选一个标量根。

以原标架表示，
$$
 \widehat\Gamma_{\nu,p}
  =\widehat\beta^{\,6-p}\,
      \mathscr C_{\nu,p}^{\,p}
       \qquad\text{on }Z_{\rm ss}.
 \tag{833.12}
$$
R826 的 $\mathscr C_{\nu,p}=[\lambda^{p-5}C_{\nu,p}(q_*)]_{\rm alg}$ 未变；(833.10) 保证右端正是权六的原标架表达。在同一个原高层点上，
$$
 \mathscr C_{\nu,p}(P_0)^p
   =(12B)^{p-6}\widehat\Gamma_{\nu,p}(P_0)
   =(12B)^{-5}\widehat\Gamma_{\nu,p}(P_0).
 \tag{833.13}
$$
最后一步才用 $12B\in\mathbb F_p^\times$。

所有八个输入都按 (833.9) 定义。特别 oldform 的标量经过 Frobenius 后是
$$
 (d^{p-7})^p=d^{p(p-7)}=d^{-6}\quad\text{in }\mathbb F_p^\times,
 \tag{833.14}
$$
不是 $1/d$。R830 的 $1/d$ 属于另一个 once-primitive $q$ 级数；这里不将它偷偷代入。

## 4. 指定原 FG 和与全部共同相位

仍写
$$
 p=6N+5,\qquad
 S_p=\sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j,
$$
$$
 K=-\frac{120c^2}{d_0},\qquad
 \kappa_\nu=(\widehat U M_\nu\widehat U^t)_{F,G}.
 \tag{833.15}
$$
R826 的原式是
$$
 S_p=K\sum_{\nu=1}^8
          \kappa_\nu\mathscr C_{\nu,p}(P_0).
 \tag{833.16}
$$
$c$ 仍是原共同 Miller/Heisenberg 尺度，满足原尺度关系；不设成 $1$。

原 $f_i,g_j$ 在此范围是有理数的 $p$ 整系数，定义曲线与 $c=0$ sigma 规范均在 $\mathbb Q$ 上。因此
$$
 S_p\in\mathbb F_p,\qquad S_p^p=S_p.
 \tag{833.17}
$$
这里的整性是 R697/R702 已证明的首 pole 之前整性；所用原普通阶均小于 $p$。只有这个原标量使用 (833.17)，不对 $c,d_0,\kappa_\nu$ 作相同假设。

把 (833.16) 的全部因子一起取 Frobenius，再代入 (833.13)，得到
$$
 \boxed{\displaystyle
 S_p=(12B)^{-5}
       \left(-\frac{120c^2}{d_0}\right)^p
       \sum_{\nu=1}^8
          \kappa_\nu^{\,p}\,
             \widehat\Gamma_{\nu,p}(P_0).
 }\tag{833.18}
$$
所以公共相位和各矩阵元同时取 $p$ 次幂，不能只 Frobenius 输入向量而保留旧行。外部因子仍为单位：$12B$、$120$、$c$ 和 $d_0$ 的单位性已由 R826 原规范及实际 Norm 证书给出。

R828 进一步给两个原 $G$ 通道的 CM 值为零，故其 $\widehat\Gamma(P_0)$ 也为零。R826 实际矩阵另已给 $\kappa_{G_1}=\kappa_{G_5}=0$。因此 (833.18) 的值可缩成六个 old 标签之和；这两种零事实分别有原证明，不互相替代。

(833.18) 与 R826 是同点的等价式。它没有用 Frobenius 把 $P_0$ 改成另一个未识别的 CM level 点；右端是原点上的截面 $p$ 次幂。若之后选择用 Frobenius 拉回语言重写，必须同时运输原 level 结构和全部系数。

## 5. Hecke 特征与 R830 的准确有限角色

对素数 $\ell\nmid6p$，采用 Serre (3) 的归一
$$
 (T_\ell v)(E,\alpha)
   =\frac1\ell\sum_{C\subset E,\ |C|=\ell}
        \varphi_C^*v(E/C,\alpha_C).
 \tag{833.19}
$$
在此约定下，乘 $\beta$ 使 Hecke 特征乘以 $\ell$。符号也可由 Katz theta 核定：在 supersingular locus，
$$
 (\theta_q v)|_{\rm ss}
       =\frac{j}{12}\,\beta\,v|_{\rm ss}
$$
对权 $j$ 形式成立，而 $\theta_q$ 将 $a_\ell$ 改成 $\ell a_\ell$。Serre (4)--(5) 将该等式延伸为整个 $\mathcal S_j$ 的、保同源 的同构。因此对任意整数 $r$，
$$
 T_\ell(\beta^r v)=\ell^r\beta^rT_\ell v.
 \tag{833.20}
$$
Frobenius 则把特征值改成 $p$ 次幂；(833.19) 的 $1/\ell$ 在 $\mathbb F_p$ 中，不增加额外因子。

令 $a_\epsilon(\ell)$ 为 GC 原权八 $f_\epsilon$ 的特征值。R826 的
$\overline C_{\nu,p}=\theta_t^{p-7}\overline f_\nu$ 给
$$
 a_{C_\nu}(\ell)=\ell^{p-7}\overline{a_\epsilon(\ell)}.
$$
oldform 和 $q_*$ 的固定 tame 运输与这些远离 $6p$ 的 Hecke 算子交换。于是
$$
 \boxed{\quad
 a_{\Gamma_\nu}(\ell)
 =\ell^{6-p}
       \bigl(\ell^{p-7}\overline{a_\epsilon(\ell)}\bigr)^p
 =\ell^{-1}\overline{a_\epsilon(\ell)}^{\,p}.
 \quad}
 \tag{833.21}
$$

现在定义有限角色
$$
 \epsilon'(w)=\epsilon(\bar w)^p.
 \tag{833.22}
$$
仍取 R830 的同一个选定 place 与
$\chi_p(w)=\omega_p(w\bmod p)^{1-p}$。若 Gaussian $\ell$ 分裂为
$w\bar w=\ell$，逐项使用 $w^p=\bar w$ 得
$$
\begin{aligned}
 \ell^{-1}\overline{a_\epsilon(\ell)}^{\,p}
 &=\epsilon(\bar w)^p\frac{w^6}{\bar w}
   +\epsilon(w)^p\frac{\bar w^6}{w}\\
 &=\epsilon'(w)\,\overline{\chi_p(w)}\,w^5
   +\epsilon'(\bar w)\,\overline{\chi_p(\bar w)}\,\bar w^5.
\end{aligned}
 \tag{833.23}
$$
这正是 R830 的 $\overline H_{\epsilon',p}$ 在 $\ell$ 的特征值。若 $\ell$ 惰性于 $\mathbb Q(i)$，两边均为零。所有除法都在 $\ell\ne p$ 下进行。

角色交换也完全明确。在 $\mathcal O/3$ 中，$g=1+i$ 满足
$\bar g=g^3$。所以
$$
 \epsilon_b'(w)=\epsilon_b(w)^{3p}.
 \tag{833.24}
$$
模 $2$ 的 $\delta$ 经 Gaussian 共轭和 Frobenius 均不变。因此

| $p\bmod24$ | $F_3,F_7$ 对应的 $\epsilon'$ | $G_1,G_5$ 对应的 $\epsilon'$ |
|---|---|---|
| $11$ | 分别仍为 $F_3,F_7$ | 分别仍为 $G_1,G_5$ |
| $23$ | 交换为 $F_7,F_3$ | 交换为 $G_5,G_1$ |

因为分别有 $3p\equiv1,5\pmod8$，这张表对原四个有限角色逐个成立；不是按一个复共轭直觉替换全部原系数。

## 6. 确定了哪个四元数对象，尚未确定哪个向量

由 Serre (9)，$\Gamma_{\nu,p}$ 可以准确视为相应有限四元数双陪集上的权六函数。四元数代数为唯一在 $\{p,\infty\}$ 分歧的 $D_p$；在 $p$ 处取最大阶单位群到 $\mathbb F_{p^2}^\times$ 的约化核，在其他处保留同一 tame level。

更具体地，本篇函数仍由原
$$
 (E,\omega_E,\alpha)\longmapsto
    \beta(E,\omega_E)^{6-p}
       C_{\nu,p}(E,\omega_E,\alpha)^p
 \tag{833.25}
$$
定义，而不是另挑一个 Hecke 特征向量。[R812](R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md) (812.1) 后及 (812.14)--(812.17)、MH (MH1)/(MH10) 已固定原族 $y^2=x^3-ax/4-b/4$、$X=a/3,Y=b$。所以原 $P_0=(0,4)$ 对应的点准确保留
$E_0:y^2=x^3-1$、原 $dz=dx/(2y)$ 与原 tame level 结构；可按这些数据选择基准最大阶及双陪集基点。改变双陪集坐标不会删除这些数据。权六函数满足原微分缩放律
$$
 \Gamma_{\nu,p}(E,a\omega_E,\alpha)
       =a^{-6}\Gamma_{\nu,p}(E,\omega_E,\alpha).
$$
因此 (833.18) 是一个明确的原四元数函数评价，而非只有 Hecke 特征的存在陈述。

每个 $C_{\nu,p}$ 的 supersingular 限制非零：若全为零，则简单 Hasse 零除子使 $C_{\nu,p}/\mathcal A$ 成为非零全纯权 $-4$ 形式，矛盾。故 (833.11) 也保证每个 $\Gamma_{\nu,p}$ 作为全局 supersingular 函数非零。但这没有指定其非零点，更没有排除 (833.18) 六个值的相消。

(833.21)--(833.24) 只确定原函数的 Hecke 特征。它们不自动给出特征零 $\overline H_{\epsilon',p}$ 的某个 integral Jacquet–Langlands 向量与 (833.25) 的逐点等式。尤其 R830 已排除将原 once-primitive 的完整 $q$ 展开直接作 tame 全纯权六形式；本篇权六对象只定义在 $Z_{\rm ss}$，与该结论完全相容。

下一项实质缺口仍是 (833.18) 的这个原指定评价，或直接保留原同标签筛的配对。即使该未筛和最终证明非零，仍需同一个
$$
 h=6i+7,\qquad (h,p+1)=1
$$
满足
$$
 P_{6i+6}(1/s)\,f_i\,g_{N-1-i}\ne0.
$$
本篇不消去 R831/DP/QS 的投影障碍，不作新素数扫描，也不推出高度排根或 Serre 一致性的完成标准。

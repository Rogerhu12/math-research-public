# R608：实际本原轨道的环类角色消相位、整数迹与有效导数均值

日期：2026-11-14。状态：**以下恒等式、充分条件和指定有限证书已证明；一般本原非消失与绝对 Serre 一致性仍 OPEN。**

本稿是新的研究结果，不是旧环境字节的恢复。根代理独占 Git；本稿及配套脚本先保存在 `agent-global`。真实整体对象始终是 R575/R587 的正向 `κ4` 家族，不使用已撤回出现性的反向家族。依赖为已恢复并发布的 R587、R598、R600 及 `general-level-Heegner-rank-interface.md`；不依赖尚待恢复的旧 R572、R588 数值或某个实际 CM jet 的单位性。

## 1. 真实参数及本条结论

设 R317 实际偶分支的参数满足

\[
p>37,\qquad p\equiv2,5\pmod9,\qquad
d=p^m d_0>0\text{ 立方自由},\qquad (d_0,6p)=1,
\]
\[
m=\begin{cases}1,&p\equiv5\pmod9,\\2,&p\equiv2\pmod9,\end{cases}
\qquad d\equiv\pm1\pmod9,
\qquad D=\operatorname{rad}(d_0),
\quad s(D)=\#\{q\mid D:q\equiv2\pmod3\}.
\tag{608.1}
\]

只考虑 `s(D)` 偶的负根号支。所有下文解析结论事实上适用于满足 (608.1) 的同一代数族；有限例子不宣称存在原曲线上的非平凡有理候选。R604 另给真正剩余偶候选 `D≥13`，不以自由指定 `d` 代替候选。

置 `K=Q(ζ)`，`ζ²+ζ+1=0`，以及

\[
N=p+1=3M,\qquad (M,3)=1,\qquad 2\mid M,
\]
\[
C=\mathbb F_{p^2}^{\times}/\mathbb F_p^{\times},
\quad \Theta_p=\{\theta_k:k\equiv5\pmod6\},
\quad h=|\Theta_p|=N/6=M/2.
\tag{608.2}
\]

固定 `C` 的生成元 `g` 使 `g^M=ζ`，且 `θ_k(g)=exp(2πik/N)`。本原子集是 `(k,N)=1`，大小 `φ(M)`。这里“本原”指整个 `C` 上阶为 `N`，不是只在某个低阶商上非平凡。

实际形式及准确导子仍为

\[
g_{k,d}=\operatorname{AI}_{K/\mathbb Q}
 (\Psi\theta_k\kappa_4\kappa_d^{-1}),
\qquad N(g_{k,d})=108p^2D^2,\qquad \epsilon(g_{k,d})=-1.
\tag{608.3}
\]

本条给出三项彼此相接的结果：

1. 在 (608.1) 的真实 `m` 下，`κ_p^{-m}` 精确消掉本原筛的三次相位。实际本原族成为同一个、与 `p` 无关的基角色 `λ0` 的全部本原环类角色扭曲；其平均核是有理数 `μ(o)/φ(o)`。
2. 所有本原平均 Fourier 系数可用整数运算求得，并有完全显式的无限尾界。因此对任意给定 `(p,d0)`，可以制作真实指定本原因子的严格非消失证书。下文在 `p=59,d0=169,d=9971` 得到本原导数均值位于 `(10.8523310797,10.8523310816)`，从而该实际本原因子维数、秩均为 `8`，且其 `p` 进对数是同构。
3. R598 的**全族均值**充分区域可由 `p≥1000D` 加强为 `p≥40D`。保留增长的对数主项后，本原预算可覆盖 `p+1=6ℓ²` 及平衡的 `6ℓ1ℓ2` 等新形状；这些是明确条件定理，不是所有 `p` 的统一非消失。

## 2. Primary 生成元和 Kummer 角色的准确方向

`O_K=Z[ζ]` 的六个单位到 `(O_K/(3))×` 的映射是双射。因此每个与 `3` 互素的整理想有唯一生成元

\[
\alpha=a+b\zeta\equiv1\pmod3,
\quad\text{即 }a\equiv1\pmod3,\quad b\equiv0\pmod3.
\tag{608.4}
\]

下文总取此生成元。其乘积仍满足 (608.4)。R348 中不受 R575 纠正影响的 Hecke 角色定义为
`Ψ_θ((α))=α ε3(α) θ(α mod p)`；在 (608.4) 下 `ε3(α)=1`。

设 `c` 是与 `3Nα` 互素的有理整数。`κ_c` 仍按原规范定义为对 `∛c` 的算术 Frobenius 作用比值。因此

\[
\kappa_c((\alpha))=\left(\frac c\alpha\right)_3.
\tag{608.5}
\]

对与 `3` 互素且同余 `±1 mod 3` 的两个元素，三次互反给

\[
\left(\frac c\alpha\right)_3
=\left(\frac\alpha c\right)_3.
\tag{608.6}
\]

准确来源为 Jeremy Booher 作者稿 *The 2011 T-Shirt: Cubic Reciprocity*，Theorem 4，及 pp.5–6 的惰性/分裂三种证明情况：

<https://www.math.canterbury.ac.nz/~j.booher/expos/cubic_rec_promys.pdf>

该稿以 primary prime `≡2 mod3` 为规范。将每个素因子乘 `−1` 得到该规范，符号不改变立方剩余符号，因为 `−1` 是立方；再用乘法性即得 (608.6)。分母只按其主理想计算，也不受这个符号影响。本文没有把惰性素数处的立方符号错误地对所有 Eisenstein 分子置为 `1`；它只在**有理**分子上恒为 `1`。

特别地，因 `p` 惰性，令

\[
\eta_p(\alpha)
 :=\alpha^{(p^2-1)/3}\pmod p\ \in\mu_3.
\]

有精确等式

\[
\boxed{\kappa_p((\alpha))=\eta_p(\alpha).}
\tag{608.7}
\]

这保留了 `κ_d^{-1}` 的负指数，没有把 Frobenius 约定取逆。

## 3. 实际本原族恰是全部本原环类角色

映射 `C→ker(N:Fp²×→Fp×)` 为 `[α]↦α^{p−1}`；由于 `p−1≡1 mod3`，它把 `ζ` 送到同一个 `ζ`。若 `[α]=g^t`，则

\[
\eta_p(\alpha)=\zeta^t,
\qquad \eta_p(g)=\zeta.
\tag{608.8}
\]

(608.1) 给出

\[
mM\equiv2\pmod3.
\tag{608.9}
\]

定义

\[
\nu_k=\theta_k\eta_p^{-m},\qquad
\ell=\frac{k-mM}{3}\pmod M.
\tag{608.10}
\]

分子由 (608.9) 被 `3` 整除，且 `ν_k(ζ)=1`。故 `ν_k` 是 `C/μ3` 的角色，其指数是 `ℓ`。又

\[
(k,N)=1
\iff(k,M)=1
\iff(\ell,M)=1,
\tag{608.11}
\]

因为 `3` 在 `Z/MZ` 中可逆。`M` 偶且 `k` 奇，所以 `ℓ` 奇；反过来每个与 `M` 互素的 `ℓ` 给出唯一 `k mod N`，并自动满足 `k≡5 mod6`。因此本原 `θ_k` **恰好**对应 `C/μ3` 的全部阶为 `M` 的角色，不需再删去一半或另加三次相位。

`C/μ3` 是导子 `p` 的阶 `O_p=Z+pO_K` 的环类群。可直接从类数一和标准理想提升得到：任一 `O_p` 理想升到 `O_K` 后主化，主生成元在 `p` 处的差由 `(O_K/p)×/(Z/p)×` 描述，再除去 `O_K×/O_p×=μ3`；这个描述既给满射也给核。因此这里的角色是导子恰为 `p` 的本原环类角色，而不是固定素数的高层 `p` 幂角色。

取与 `6D` 互素的理想，定义

\[
\lambda_0((\alpha))
 =\alpha\,\kappa_4((\alpha))\kappa_{d_0}((\alpha))^{-1},
\qquad \alpha\text{ 按 (608.4) 选取}.
\tag{608.12}
\]

它是无穷型 `(1,0)` 的 Hecke 角色，值在 `K` 中；在固定 `d0` 时它不依赖 `p`。由 (608.7)、(608.10)，得到同一实际形式的恒等式

\[
\boxed{\Psi\theta_k\kappa_4\kappa_d^{-1}
       =\lambda_0\nu_k.}
\tag{608.13}
\]

在有理主理想上，(608.4) 的生成元为 `χ_{−3}(n)n`，且有理 Kummer 角色值为 `1`，故 `λ0((n))=χ_{−3}(n)n`。这也直接校验了 R598 的有理射线相位。

## 4. 不用离散对数的本原平均核

对任意与 `p` 互素的 `α`，令

\[
o(\alpha)=\operatorname{ord}_{\mathbb F_{p^2}^{\times}}
                  \bigl(\alpha^{3(p-1)}\bigr),
\qquad o(\alpha)\mid M.
\tag{608.14}
\]

这是 `[α]` 在 `C/μ3` 中的阶：把 `[α]` 送到 `α^{p−1}` 后再立方，核恰是 `μ3`。循环群 `G` 阶为 `M` 时，对一个阶为 `o` 的元素 `x`，其所有本原角色满足

\[
\frac1{\varphi(M)}\sum_{\operatorname{ord}\nu=M}\nu(x)
 =\frac{\mu(o)}{\varphi(o)}.
\tag{608.15}
\]

证明：写 `x=g^t`，左边为 `c_M(t)/φ(M)`。对每个素数幂 `ℓ^a∥M`，有限几何和先对所有角色求和再减去指数被 `ℓ` 整除的角色，所得局部值为 `1`（局部阶一）、`−1/(ℓ−1)`（局部阶 `ℓ`）、或 `0`（局部阶至少 `ℓ²`）。相乘恰得右边。此证明同时包含 `μ(o)=0` 的所有情形。

结合 (608.13)，平均后的 Hecke 系数完全保留实际的 `λ0`，而本原权重化为有理数：

\[
\boxed{\overline a_n=
 \sum_{\substack{N\mathfrak a=n\\(\mathfrak a,6pD)=1}}
 \lambda_0(\mathfrak a)
 \frac{\mu(o(\alpha_{\mathfrak a}))}
      {\varphi(o(\alpha_{\mathfrak a}))}.}
\tag{608.16}
\]

共轭理想的 primary 生成元仍是共轭，`o` 相同，`λ0` 值共轭。所以

\[
\boxed{\varphi(M)\overline a_n\in\mathbb Z.}
\tag{608.17}
\]

这里用到 `φ(o)|φ(M)` 对 `o|M` 成立，以及 `O_K∩Q=Z`。计算这些整数只需分解 `M`、在 `Fp²` 中反复幂运算求元素阶，并计算有限个三次剩余符号；无需选择复数根或恢复离散对数。

## 5. 同一本原均值的严格有限证书

记

\[
c=\frac\pi{3\sqrt3},\qquad t=\frac c{pD},\qquad
\mathscr A_{p,d}^{\rm prim}
 =\frac1{\varphi(M)}\sum_{(k,N)=1,\ k\equiv5\ (6)}
       L'(g_{k,d},1).
\]

R598 的准确导数 AFE 和绝对收敛给

\[
\boxed{\mathscr A_{p,d}^{\rm prim}
       =2\sum_{n\ge1}\frac{\overline a_n}{n}E_1(tn).}
\tag{608.18}
\]

令 `A_K(x)` 为范数至多 `x` 的整理想数。R598 的六角壳计数给 `A_K(x)≤x`：壳半径 `ρ=max(|a|,|b|,|a−b|)` 有 `6ρ` 个元素且范数至少 `3ρ²/4`，除六个单位后得到 `A_K(x)≤2x/3+√(x/3)≤x`（`x≥3`），小区间直接只有单位和范数三理想。

因为 `|μ(o)/φ(o)|≤1`，有 `|\overline a_n|≤a_K(n)√n`。对 `f(x)=x^{−1/2}E1(tx)` 作 Stieltjes 分部积分，任意 `X≥1` 有

\[
\sum_{n>X}a_K(n)f(n)
 \le Xf(X)+\int_X^\infty f(x)\,dx
 =2t^{-1/2}\Gamma(1/2,tX)-\sqrt X E_1(tX).
\]

最后用 `Γ(1/2,u)≤e^{−u}/√u`，得到

\[
\boxed{\left|\mathscr A_{p,d}^{\rm prim}
 -2\sum_{n\le X}\frac{\overline a_n}{n}E_1(tn)\right|
 \le\frac{4e^{-tX}}{t\sqrt X}.}
\tag{608.19}
\]

这是一条对所有满足 (608.1) 的负根号参数有效的尾界，不要求 `p/D≥40`，也不假设 Möbius 筛后仍有 `p²/4` 的最小范数。

若 (608.19) 的有限和严格大于其尾界，则指定本原轨道中至少一个中心导数非零。R600 已证这个轨道恰是实际 `A_{−1,d}` 的有理 Galois 轨道；任意水平 Heegner 秩接口遂给

\[
\operatorname{rank}A_{-1,d}(\mathbb Q)
 =\dim A_{-1,d}=\varphi(M),
\quad
\log_p:A_{-1,d}(\mathbb Q)\otimes\mathbb Q_p
       \xrightarrow{\sim}\operatorname{Lie}(A_{-1,d})(\mathbb Q_p).
\tag{608.20}
\]

这一步使用 BFH 的任意水平辅助域、Gross–Zagier、Nekovář 与 Fricke 下降及对数接口，不对超越的 `L′` 值作未经证明的 Galois 操作。维数也可直接核：系数在 `Q(μ_N)^+`，固定 `K` 的 Galois 作用给上述 `φ(M)` 个不同 Hecke 诱导形式；相同诱导只允许原角色或其复共轭，而不同的 `(1,0)` 角色不可能由后者互换。因此次数恰为 `φ(M)`。

若某次区间含零，结论只是该证书未证非消失。本文没有宣称不断增大 `X` 必然终止，也没有由此给全部 `p,d` 的统一非消失算法。

## 6. 真正位于旧充分区域外的一个完整证书

取

\[
p=59,\quad m=1,\quad d_0=13^2=169,\quad
d=9971,\quad D=13,\quad s(D)=0,\quad M=20.
\tag{608.21}
\]

有 `d≡−1 mod9`、唯一额外素数 `13≡1 mod12`；`p/D=59/13<40`。这是同一实际族的参数，不声称已经从某个未排除的原有理点得到它。

配套程序 `R608_primitive_trace_certificate.py` 取 `X=40pD=30680`，以 `(a,b)` 的整数基枚举 (608.4)。范数 `a²−ab+b²≤X` 保证 `|a|,|b|≤√(4X/3)`，所以枚举无漏项。每个理想正好出现一次。对三次符号，程序分别使用

\[
\left(\frac\alpha q\right)_3
 =\alpha^{(q^2-1)/3}\pmod q\quad(q\equiv2\pmod3),
\]
\[
\left(\frac\alpha{(q)}\right)_3
 =\left(\frac\alpha{\bar\alpha}\right)^{(q-1)/3}\pmod q
 \quad(q\equiv1\pmod3).
\tag{608.22}
\]

第二式是在 `O_K/(q)=F_q×F_q` 中同时计算两个素理想的符号乘积：若 `ζ` 在两个分量分别为 `z,z^{-1}`，两分量的指数分别取相反号，所以乘积正好由 `α/\barα` 给出。程序用 `α/\barα=α²/Nα`，无须选择分裂根。`κ4` 的指数为 `κ2` 的两倍，`κd0^{-1}` 保留负指数。

完整数据文件 `R608-p59-d0_169-coefficients.json` 保存 `φ(20)\overline a_n`：7907 个与坏素数互素的理想中，3933 个本原核非零，合并后1404个非零范数项。全部 `ζ` 分量在整数运算中**逐范数精确抵消**。前六个非零整数系数为

\[
(n,8\overline a_n)=(1,8),(7,-8),(19,-2),(25,-40),(49,52),(79,-34).
\tag{608.23}
\]

数值阶段只处理这个固定的有理系数有限和，使用 60 位定向区间运算。为避免把库中某个无误差估计的 `E1` 函数当证书，程序自行使用

\[
E_1(x)=-\gamma-\log x-
       \sum_{k\ge1}\frac{(-x)^k}{k\,k!}.
\tag{608.24}
\]

在 `J=64+4⌈x_upper⌉` 项截断后，绝对项比值为 `xk/(k+1)²<1`，故交错余项由首个遗漏项绝对值界定；区间运算另包住全部舍入和输入区间误差。

Euler 常数取 `n0=64,K0=12` 的有理 Euler–Maclaurin 包围。令

\[
G=H_{n_0}-\log n_0-\frac1{2n_0}
  +\sum_{j=1}^{K_0}\frac{B_{2j}}{2j\,n_0^{2j}}.
\]

则

\[
0<\gamma-G<
 \frac{B_{26}}{26\,64^{26}}.
\tag{608.25}
\]

其符号及上界可由 Binet 的正积分直接证明：
`γ=H_n−log n−1/(2n)+2∫_0^∞ t/((t²+n²)(e^{2πt}−1))dt`；对 `(n²+t²)^{-1}` 作有限几何展开，`K0=12` 为偶数，余项严格正且小于下一项。所用标准恒等式见 NIST DLMF (5.9.15) 和 (6.6.2)：

<https://dlmf.nist.gov/5.9.E15>，<https://dlmf.nist.gov/6.6.E2>。

实际执行所得有限和及尾界为

\[
10.8523310806150189590129707521603696527329372
 <S_X<
10.8523310806150189590129707521603696527329504,
\]
\[
T_X<0.0000000009098831409305593560916250391795269.
\tag{608.26}
\]

因此完整平均严格位于

\[
\boxed{10.8523310797<\mathscr A_{59,9971}^{\rm prim}
                         <10.8523310816.}
\tag{608.27}
\]

机器原始区间及其输入哈希保存在 `R608-p59-d0_169-interval-certificate.json`。这证明 (608.20) 在此参数下成立，维数为 `φ(20)=8`。它不证明该商中原有理点的像为零，不给指定二次高度的首项单位，更不单独排除这个参数的所有原候选。

## 7. 全族均值的区域可降到 p≥40D

这里的 `r=p/D` 是导子尺度，不再表示原曲线的 `1−a³`。设

\[
r\ge40,\quad A=cr/4,\quad
\mathcal Q(x)=\frac{e^{-x}}{1-e^{-3x}},\quad
\mathcal L=1+\log D.
\]

R598 给精确主项

\[
\frac1h\sum_{\theta\in\Theta_p}L'(g_{\theta,d},1)
 =2cP_{2D}\left[
 \log(pD/c)-\gamma+\frac{2L'(\chi_{-3},1)}c
 +2\sum_{q\mid2D}\frac{\chi_{-3}(q)\log q}{q-\chi_{-3}(q)}
 \right]+\mathrm{Err},
\tag{608.28}
\]

其三个误差上界分别为

\[
E_{\rm off}=4\left[
 \left(\frac1{p\sqrt3}+\frac{3^{1/4}}{\sqrt r}\right)
        \frac{\mathcal Q(3A)}{3A}
 +\left(\frac1p+\frac{3^{1/4}}{\sqrt r}\right)
        \frac{\mathcal Q(A)}A\right],
\]
\[
2|R_{2D}|\le8\,3^{-1/4}r^{-1/2}\mathcal Q(3A),
\qquad
E_p\le\frac2p\frac{\mathcal Q(4A)}{4A}.
\tag{608.29}
\]

R600 已给 `c>3/5`、`γ<29/50`、`log2<7/10`、`e6>400` 的有理证明。因此 `A>6`，并且

\[
\mathcal Q(A)<1/200,\qquad
\mathcal Q(3A)<1/32000000.
\]

由 `p≥41`、`√r>6`、`3^{1/4}<4/3`，(608.29) 中两个括号各小于 `1/40+2/9<1/4`。遂有

\[
E_{\rm off}<1/1200+1/576000000<1/1000,
\quad 2|R_{2D}|<10^{-6},\quad E_p<10^{-6}.
\]

故一个方便的共同有理界为

\[
\boxed{|\mathrm{Err}|<1/250.}
\tag{608.30}
\]

R598 已证明 `L′(χ_{−3},1)>0`，并且

\[
P_{2D}\ge\frac3{2\zeta(2)(1+\log D)},
\quad
2\sum_{q\mid2D}\frac{\chi(q)\log q}{q-\chi(q)}
\ge-\frac23\log2-\frac13\log D.
\tag{608.31}
\]

又 `c<2/3`、`log(3/2)>2/5`，故 (608.28) 的方括号严格大于

\[
\log r+\frac53\log D-1.
\tag{608.32}
\]

因 `r≥40` 使 `log r>3`，(608.32) 大于 `(5/3)(1+logD)`。结合 `2cP_{2D}>12/(11\mathcal L)` 得

\[
\boxed{\frac1h\sum_\theta L'(g_{\theta,d},1)
       >\frac{20}{11}-\frac1{250}
       =\frac{4989}{2750}>\frac95
       \qquad(p\ge40D).}
\tag{608.33}
\]

这里加强的是**全族均值**。不能只替换 R598 中的数字 `1000`，就不经检查同时继承它的高维选择不等式。若 `N=3·2^ν`，全族本已是本原轨道，故 (608.33) 直接给指定 `A_{−1,d}` 的 (608.20)。一般形状则须使用下一节预算或第5节精确迹。

## 8. 保留增长主项的有效本原预算

定义可直接计算的实数

\[
\mathfrak L(p,D)=2cP_{2D}\left[
 \log(pD/c)-\frac{29}{50}
 +2\sum_{q\mid2D}\frac{\chi(q)\log q}{q-\chi(q)}
 \right]-\frac1{250}.
\tag{608.34}
\]

当 `p≥40D`，(608.28)–(608.30) 给全族均值严格大于 `\mathfrak L(p,D)`。令

\[
\kappa_N=\frac{3\varphi(N)}N
 =\frac{2\varphi(M)}M,\quad q_N=1-\kappa_N,
\quad B_1=4\sqrt{3\sqrt3\,pD}.
\]

R598 的单项界 `|L′(g,1)|≤B1` 适用于所有实际角色。减去全部非本原项，得到

\[
\boxed{\mathscr A_{p,d}^{\rm prim}
 >\frac{\mathfrak L(p,D)-q_NB_1}{\kappa_N}.}
\tag{608.35}
\]

所以 `p≥40D` 且 `q_NB1≤\mathfrak L(p,D)` 是指定实际本原因子的秩/对数充分条件。与仅保留常数 `9/5` 或 `28/5` 的预算相比，(608.34) 没有丢掉随 `p` 增长的对数主项。

两个明确的新形状推论如下。仍需全部实际参数条件 (608.1)。

- 若 `N=6ℓ²`、`ℓ≥5` 为素数，则 `q_N=1/ℓ` 且 `q_NB1<24√D`。因此
  \[
  \boxed{\log(p/D)\ge1+23\sqrt D(1+\log D)}
  \tag{608.36}
  \]
  足以给 (608.20)。
- 若 `N=6ℓ1ℓ2`，两个素数满足 `5≤ℓ1<ℓ2≤2ℓ1`，则 `q_N≤1/ℓ1+1/ℓ2`，于是
  \[
  q_NB_1<4\sqrt{18\sqrt3D}
       (\sqrt{\ell_2/\ell_1}+\sqrt{\ell_1/\ell_2})
       \le36\,3^{1/4}\sqrt D<48\sqrt D.
  \]
  因此
  \[
  \boxed{\log(p/D)\ge1+45\sqrt D(1+\log D)}
  \tag{608.37}
  \]
  足以给 (608.20)。

证明这两个最后推论时，(608.31)–(608.32) 给

\[
\mathfrak L(p,D)>
 \frac{12}{11(1+\log D)}
 \left[\log(p/D)+\frac53\log D-1\right]-\frac1{250}.
\tag{608.38}
\]

(608.36) 使右端大于 `(276/11)√D−1/250>24√D`；(608.37) 使其大于 `(540/11)√D−1/250>48√D`。两条件也自动蕴含 `p/D>40`。这只是足够而非最优的区域；没有声称这些形状中有无限多个素数，也没有把 `D=1` 当成尚存实际偶分支。

## 9. 为什么不能对一般 Möbius 项照搬两直线误差

一个完全精确的小例子足以排除该未经证明的捷径。取 `p=59`、`α=1+3ζ`，则 `Nα=7`，在 `Fp²` 中

\[
\alpha^{58}=33+51\zeta,\quad
(33+51\zeta)^{30}=1,\quad
(33+51\zeta)^6=51+18\zeta\ne1.
\tag{608.39}
\]

而 (608.14) 的阶为 `o=10`。因此该方向落在 `C[30]`，不在全族两直线所用的 `C[6]`，却已于范数 `7<59²/4` 出现。本原核为 `μ(10)/φ(10)=1/4`，非零。这个格点实际进入 (608.16)，而非被筛自动删掉。

所以 R598 的 `p²/4` 范数下界只能用于完整 `Θ_p` 的原两直线，不能无条件赋给 Möbius 新方向。第5节有限迹的尾界和第8节全族减非本原预算都避开了这一逻辑错误。一般 `p+1` 上若要给更强的统一结果，仍须控制这些短方向的真实带符号和。

## 10. 对真实整体路线的意义和仍缺的接口

本条已经把某些有效区域及一个旧区域外的参数，推进到**指定实际本原因子**的秩等于维数和对数同构。这消除了这些情形中“平均选到的 θ 未必是局部可控的 θ−1”的一项障碍。

它没有把秩等于维数当成秩零，没有把实际原曲线 `c1` 与变化 `d` 覆盖的 `c0` 当成同一点，也没有把阿贝尔积分的首项当成全局二次高度的首项。下一步仍须在 R593/R596 的同一修正线丛、同一基点及同一高度规范下控制真实二次高度，或在正根号支使用 R602/R603 的秩零路线。一般参数的本原均值正性也仍开放；有限 `p=59` 证书不是全参数外推。

### 配套文件

- `scripts/R608_primitive_trace_certificate.py`：整数系数和定向区间程序。
- `notes/R608-p59-d0_169-coefficients.json`：完整精确系数输入。
- `notes/R608-p59-d0_169-interval-certificate.json`：有限和、无限尾界及输入 SHA256。
- `notes/R608-agent-primitive-trace-manifest.json`：代理冻结版本和实际执行记录。
- `notes/R608-handoff-manifest.json`：本次实际发布字节及 root 核查。

复现时将程序复制到新的临时目录后执行 `python3 R608_primitive_trace_certificate.py --p 59 --d0 169`；程序在其自身目录生成两份结果。此次只核查已实际执行的证书与完整证明，没有为了修改文件位置重新运行数学计算。

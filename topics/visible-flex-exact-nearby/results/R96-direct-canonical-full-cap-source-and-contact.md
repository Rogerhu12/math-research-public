# R96：直接 canonical 的完整正帽源、contact 与 paired Wronskian

2026-11-12，visible-exact-astra-f6a2。

**状态：已证明，实际完整 178 格已重算并保存。** 本篇直接在同一真实
canonical 领口中定义输出空间与源空间，避免先将普通源搬到另一根角后再
支付一个很大的通用换元费。完整正帽、根均值、regular 平均值及其通量、
全部角耦合都保留。本篇给真实 source/contact 强界；完整反馈逆仍未完成。

实际全域常数为
$$
 C_{\rm ordinary}<96.984892,\qquad C_{\rm weak}<48.482093.
$$
只限制 canonical 根输出到 $|k|>64$、同时保留 regular 槽时分别为
$16.496266$ 和 $8.187268$。这不是压缩体算子。
完整细领口 Airy 截断源费用仍约 $1.1\cdot10^{11}$；
第10节给出可以重组该费用的准确 Wronskian 恒等式，并明确保留外端项。

## 1. 同一个真实对象、完整帽和局部坐标

采用 R83/R87/R94 同一准确 affine 族
$$
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 |\delta-\delta_5|\le1/2500000.
$$
每个参数使用真正移动根 $t(\delta)$。在正侧置 $s=r-t(\delta)$，
物理领口为 $0\le s\le h=1/2048$。R87 的有限真实 canonical 图写成
$$
 \Psi(s,\theta)=(y,\phi),\quad J=\det D\Psi>0,\quad
 A=J^{-1}D\Psi\,B\,D\Psi^T,\quad \tau=A_{11}^{-1/2}.
$$
其中 $B=Y^2\widehat A$ 是 R74/R94 的真实 grounded 正帽主矩阵。
令
$$
 C=\tau^2A=C_0+E,\qquad C_0=\operatorname{diag}(1,y),\qquad E_{11}=0.
                                                               \tag{96.1}
$$
根处 $y=0,y_s=1,y_\theta=0,\phi=Y_0(\theta),E=0$。
完整帽仍延伸到真实闭外尾，具有原来的 Robin 形式及 regular 均值槽。
在
$$
                         H=\frac{49}{50}h=\frac{49}{102400}       \tag{96.2}
$$
处没有添加人工边界条件。本篇仅把 $0\le y\le H$ 用作源支撑和局部估计域。

完整帽能量记为 $\mathfrak b(v,v)$。R94 已支付它的存在、最大性、
完整非负 Robin 项和 regular 均值延拓费用
$$
                        E_{\rm reg}<50.912957.                  \tag{96.3}
$$
regular 槽 $\xi$ 的基是物理圆上的正交归一常数
$(2\pi)^{-1/2}$，所以其能量是 $E_{\rm reg}|\xi|^2$；
若改用未归一化常数，必须相应乘上圆长。

## 2. 正确的全解算子和 trace 空间

canonical 根圆长为 $\ell$，$q=2\pi/\ell$。采用 $L^2(d\phi)$ 的
正交归一 Fourier 基，$H^\sigma_\phi$ 用乘子
$\langle qj\rangle^\sigma$ 定义；四重子空间为 $j=4k$。
定义真实根 trace 变换
$$
 (T_0a)(\theta)=\tau_0(\theta)a(Y_0(\theta)).
$$
若 $\mathcal H_{\rm ph}$ 是完整 grounded 帽的调和延拓，置
$$
 \widetilde{\mathcal H}(a,\xi)
  =\left[\frac{\mathcal H_{\rm ph}(T_0a,\xi)}{\tau}\right]
      \circ\Psi^{-1}\quad(0\le y\le H),\qquad
 X=H^{1/3}_\phi\oplus\mathbb C.                               \tag{96.4}
$$
它是完整帽解在领口的限制。根零模与 regular 槽都包含在 $X$ 中。

写 $u=\widetilde{\mathcal H}(a,\xi)$，$g=\nabla\log\tau$。真实换元给
$$
 \int_0^H\!\!\int
       |\nabla u+ug|_C^2\,d\phi\,dy
 \le \mathfrak b(v,v),\qquad v=\mathcal H_{\rm ph}(T_0a,\xi).    \tag{96.5}
$$
这保留了由 height 产生的一阶、零阶项。不能把(96.5)直接改写成
$\int|\nabla u|_C^2\le\mathfrak b$。

## 3. 完整体解的局部能量及普通源增益

假设实际领口已给
$$
 (1-\varepsilon)C_0\le C\le(1+\varepsilon)C_0,\quad
 |g|_{C_0}\le G_0,\quad G_C=\sqrt{1+\varepsilon}\,G_0,
$$
$$
 d_0=1-\frac{G_CH}{\sqrt{1-\varepsilon}}>0.                    \tag{96.6}
$$
由 $u(0)=a$ 和一维积分，
$$
 \|u\|_{L^2}^2\le2H\|a\|_{L^2}^2+H^2\|u_y\|_{L^2}^2.
$$
Minkowski 不等式、(96.5) 和 $C\ge(1-\varepsilon)C_0$ 给
$$
 \boxed{\ 
 \|\nabla u\|_{L^2_C}
 \le d_0^{-1}\left(\sqrt{\mathfrak b(v,v)}
                  +G_C\sqrt{2H}\|a\|_{L^2}\right).\ }          \tag{96.7}
$$

对每个根频率 $\lambda=|qj|$，取
$h_\lambda=\min(H,\lambda^{-2/3})$，
$e_\lambda(y)=(1-y/h_\lambda)_+a_\lambda$；均值用 $h_0=H$。
$\tau e$ 是完整帽的合法 competitor，外部为零，
所以没有在 $H$ 处修改真实帽。准确积分
$$
 \int|e_\lambda'|^2=\frac{|a_\lambda|^2}{h_\lambda},\quad
 \int y\lambda^2|e_\lambda|^2
       =\frac{\lambda^2h_\lambda^2}{12}|a_\lambda|^2,\quad
 \int|e_\lambda|^2=\frac{h_\lambda}{3}|a_\lambda|^2
$$
给
$$
 E_{\rm grad}=\max(H^{-1},13/12),\qquad
 E_{\rm all}=
 \left(\sqrt{1+\varepsilon}\sqrt{E_{\rm grad}}
                +G_C\sqrt{H/3}\right)^2.                     \tag{96.8}
$$
这里 $H^{-1}+\lambda^2H^2/12$ 除以
$(1+\lambda^2)^{1/3}$ 在有限区间上的最大值位于端点：
其导数符号的分子是关于 $\lambda^2$ 的递增一次式。
这证明(96.8)也包含所有低频和均值。

若只让根 test trace 满足 $|k|>N$，置
$$
 \Lambda_N=4q_-(N+1),\quad
 d_N=\max\{1,(H\Lambda_N^{2/3})^{-1}\},\quad
 \mu_N=(1+\Lambda_N^2)^{-1/6},
$$
$$
 E_N=\left[\sqrt{1+\varepsilon}\sqrt{d_N+1/12}
              +\frac{G_C}{\sqrt3\Lambda_N^{2/3}}\right]^2.     \tag{96.9}
$$
$\|a\|_{L^2}\le\mu_N\|a\|_{H^{1/3}}$，但
$\|a\|_{H^{1/3}}$ 本身不能再乘 $\mu_N$。
完整帽解仍不作 Fourier 投影。

给定 $E,\mu$，其中全根取 $(E_{\rm all},1)$、高根取 $(E_N,\mu_N)$，
定义
$$
 T_a=\frac{\sqrt E+G_C\sqrt{2H}\mu}{d_0},\quad
 T_{\rm reg}=\frac{\sqrt{E_{\rm reg}}}{d_0},\quad
 C_w=(T_a^2+T_{\rm reg}^2)^{1/2}.                              \tag{96.10}
$$
调和解最小能量原理和两 competitor 的三角不等式，结合(96.7)，证明
$\|\nabla\widetilde{\mathcal H}\|_{X\to L^2_C}\le C_w$。

普通源还需要真正的 $2/3$ 角增益。对每个 $\lambda>0$，把区间在
$\min(H,\lambda^{-2/3})$ 分开：近根用一维 trace 积分，远根用
$y\lambda^2\ge\lambda^{4/3}$。连同均值的上述 Poincare 式，得到安全界
$$
 \|u\|_{L^2_yH^{2/3}_\phi}^2
 \le(4+H^2)\|\nabla u\|_{L^2_{C_0}}^2
                  +(4+2H)\|a\|_{H^{1/3}}^2.
$$
因此
$$
 \boxed{\quad
 C_s^2=\frac{4+H^2}{1-\varepsilon}C_w^2+4+2H,\qquad
 \|\widetilde{\mathcal H}\|_{X\to L^2H^{2/3}}\le C_s.
 \quad}                                                       \tag{96.11}
$$
这对完整正帽真实解成立；没有把半线 Neumann 谱隙移用到有限区间。

## 4. paired 普通源、弱散度源与完整 contact

canonical 源记为 $f-\operatorname{div}F$，其自然范数为
$$
 \|f\|_{L^2_yH^{-2/3}_\phi},\qquad
 \|C^{-1/2}F\|_{L^2}.
$$
通过完整正帽的弱解和 Poisson 双对偶定义 contact
$\widetilde K(f,F)\in X^*$。由(96.10)–(96.11)
$$
 \boxed{\quad
 \|\widetilde K(f,F)\|_{H^{-1/3}_\phi\oplus\mathbb C}
 \le C_s\|f\|_{L^2H^{-2/3}}
                 +C_w\|C^{-1/2}F\|_{L^2}.
 \quad}                                                       \tag{96.12}
$$
regular 通量是第二输出，不能省略。高根表仅把根 test trace 限于
$|k|>N$，regular test 仍保留，故它给高根输出与 regular 通量的联合界。

准确物理源是
$$
 F_{\rm ph}=\frac J\tau D\Psi^{-1}F,\qquad
 f_{\rm ph}=\frac J\tau(f-g\cdot F).                           \tag{96.13}
$$
对真实 test $v=\tau u$，Piola 换元逐项给
$$
 \int_{\rm ph}(f_{\rm ph}\bar v+
                        F_{\rm ph}\cdot\nabla\bar v)
  =\int_{\rm can}(f\bar u+F\cdot\nabla\bar u).                 \tag{96.14}
$$
右侧的 height 项由(96.13)两部分**准确相消**。
这不允许只取 $f_{\rm ph}=Jf/\tau$ 同时保留原 $F_{\rm ph}$，
也不允许把 R94 的真实零阶项直接删除。

根 contact 满足
$$
 T_0^*p_{\rm ph}
  =\left[\frac{\tau_0}{Y_0'}p_{\rm ph}\right]\circ Y_0^{-1}.
                                                               \tag{96.15}
$$
若 test 根值不为零，真实 conormal 与 canonical conormal 之间另有
$$
 T_0^*p_{\rm ph}=p_{\rm can}-g_0a,\qquad
 g_0=(\partial_y\log\tau+E_{12}\partial_\phi\log\tau)|_{y=0}.
                                                               \tag{96.16}
$$
这里 outward 方向为负 $y$。该零阶 shear 仍属于实际 Cauchy frame。

为比较物理 trace，若 $t_{\min}\le\tau_0$、$|\tau_{0,\theta}|\le t_1$、
$0<m\le Y_0'\le M$，插值 $L^2$ 与 $H^1$ 的准确换元给
$$
 \|T_0^{-1}\|_{H^\sigma_\theta\to H^\sigma_\phi}
 \le t_{\min}^{-(1-\sigma)}
      (t_{\min}^{-1}+t_1t_{\min}^{-2})^\sigma
      M^{(1-\sigma)/2}
      \max(\sqrt M,m^{-1/2})^\sigma,\quad0\le\sigma\le1.        \tag{96.17}
$$
取 $\sigma=1/3$ 并与 regular 槽的恒等相加可得物理 contact 界。
纯 scalar 的物理 $L^2$ 密度费用是
$\sqrt{\sup J/\tau^2}$。但是混合 $(r,\theta)\mapsto(y,\phi)$
并不自动保持径向 $L^2$、角向 $H^{-2/3}$ 的各向异性范数；
(96.13)定义了这里真正使用的源类。

## 5. 从完整 mixed jets 得到实际 $G_C$ 与 multiplier

恢复源实际计算 178 个准确角区间、每格四个真中心角 Taylor 及两个
连续径向 slab。40 个 primitive 径向系数、39 个 $E$ 系数保留
原来完整的 Cauchy shift-tail 费；不是把更短截断当作原函数。
所有 used mixed derivatives 都来自同一个实际根、scalar germ 和参数盒。

若真实系数 $f=s^kb(s,\theta)$，保存的数据给
$f$ 在根的系数以及整个 slab 上 $|\partial_s^n f|/n!$ 的上界 $M_n$。
Taylor 积分直接给
$$
 |b_s|\le M_{k+1},
$$
及每个 $n\ge k+2$ 的更细界
$$
 |b_s|\le
 \sum_{i=k+1}^{n-1}(i-k)|f_i|h^{i-k-1}
                      +(n-k)M_nh^{n-k-1}.                  \tag{96.18}
$$
后一式也可直接对 $b_s$ 的积分表示展开；不对未控余项免费微分。
写 $a=y/s$，则 $f/y^k=b/a^k$，并且
$$
 \partial_\phi(f/y^k)
 =\frac{a^{-k}}J
   \big(y_sb_\theta-y_\theta b_s-k a_\theta b\big).            \tag{96.19}
$$
用到了准确恒等式
$y_sa_\theta-y_\theta a_s=aa_\theta$。
若这些系数的 $C^0,C^1_\phi$ 模数为 $c_0,c_1$，乘法在
$H^{-2/3}_\phi$ 上的 norm 至多
$c_0^{1/3}(c_0+c_1)^{2/3}$，由 $L^2/H^1$ 和对偶插值得到。
弱 flux 只需 $c_0$。所有 lag 一起包括在该真实乘法范数中。

新 mixed jet 还直接计算
$$
 G_{\rm raw}=
   \frac{\tau_y+E_{12}\tau_\phi}{\tau}.
$$
由物理固定 $s$ 角微分，
$$
 \partial_\phi\log\tau
   =\frac{\tau_\theta/\tau-y_\theta G_{\rm raw}}
          {\phi_\theta-y_\theta E_{12}},\qquad
 \partial_y\log\tau
   =G_{\rm raw}-E_{12}\partial_\phi\log\tau.                  \tag{96.20}
$$
每格分母都证明为正。于是可直接界
$G_0^2=|\partial_y\log\tau|^2+H|\partial_\phi\log\tau|^2$，
避免把两个很大的、实际相消的 height 导数分别粗估。

设 $|E_{12}|\le e_{12}$、$|E_{22}|\le e_{22}$ 是各自根阶
$s^6,s^7$ 的完整界，$a\ge a_*>0$。相对主矩阵的安全上界为
$$
 \varepsilon\le
 \frac{e_{12}}{\sqrt{a_*h}}+\frac{e_{22}}{a_*h};               \tag{96.21}
$$
由于正根阶，该式也控制 $s<h$ 的全部点，而非只控制外端。

## 6. 实轴 Airy 全矩和根处连接

本篇所用真实正轴估计为
$$
 |\operatorname{Ai}(z)|,\ |\operatorname{Ai}'(z)|
 \le\frac34(1+z)^{1/4}e^{-2z^{3/2}/3},\qquad z\ge0.           \tag{96.22}
$$
给出其来源以避免把正性/衰减当成未付假设。
对 $z\ge1$，从 Airy 轮廓积分把轮廓移到
$t=\sqrt z+iu$，指数实部为 $-2z^{3/2}/3-\sqrt z\,u^2$；
连接端的指数衰减保证移线。Gaussian 积分分别给
$$
 |\operatorname{Ai}(z)|
 \le\frac{z^{-1/4}}{2\sqrt\pi}e^{-2z^{3/2}/3},
$$
$$
 |\operatorname{Ai}'(z)|
 \le\left(\frac{z^{1/4}}{2\sqrt\pi}
                +\frac{z^{-1/2}}{2\pi}\right)e^{-2z^{3/2}/3}.
$$
括号在 $z\ge1$ 被 $(3/4)(1+z)^{1/4}$ 控制。

准确初值为
$$
 \operatorname{Ai}(0)=\frac1{3^{2/3}\Gamma(2/3)}<.36,\qquad
 -\operatorname{Ai}'(0)=\frac1{3^{1/3}\Gamma(1/3)}<.26.
$$
若解在正轴有零点，与无穷处衰减配合，对 $u''=zu$ 积分得
$\int(u'^2+zu^2)=0$，与非零初值矛盾。故 $\operatorname{Ai}>0$。
其导数单调增加到0，故 $|\operatorname{Ai}|,|\operatorname{Ai}'|$
在 $[0,1]$ 不超过上述初值。又 $e^{2/3}<2$，所以(96.22)
在该区间也成立，且与 $z=1$ 的轮廓界真正连接。

上述轮廓和初值分别见 NIST DLMF [9.5.4](https://dlmf.nist.gov/9.5.E4)、
[9.2.3](https://dlmf.nist.gov/9.2.E3)–[9.2.4](https://dlmf.nist.gov/9.2.E4)；
这里只使用这些准确恒等式，后续界已自行证明。
平方 majorant 使用 $(1+z)^{1/2}\le1+\sqrt z$，因而
$$
 M_k(c)=\frac34\left[
 \sum_{\eta\in\{0,1/2\}}\frac23
 c^{-2(2k+\eta+1)/3}
 \Gamma\!\left(\frac{2(2k+\eta+1)}3\right)\right]^{1/2}         \tag{96.23}
$$
是相应 $z^k$ 的完整 $L^2$ 矩；$k>-1/2$ 时有限。
源码逐项用 Arb 计算 Gamma 和全部实轴连接门。

## 7. 完整真实源的 14 项与 18 项

在正侧令
$$
 P_{\rm can}=-\operatorname{div}(C\nabla)+V,\quad
 P_0=-\partial_y^2-y\partial_\phi^2+V.
$$
$U$ 是 R53/R87 的完整非零频率校正 Ai 试解。
取 $\chi=1$ 于 $y\le H/2$、$\chi=0$ 于 $y\ge H$，
中间使用标准五次 smoothstep，因此
$|\chi'|\le15/[8(H-H/2)]$。准确恒等式为
$$
 P_{\rm can}(\chi U)
 =\underbrace{\chi P_0U-\chi'U_y}_{f}
  -\operatorname{div}
       \underbrace{\big(\chi E\nabla U+\chi'UC e_y\big)}_{F}.
                                                               \tag{96.24}
$$
这一写法不把 $E_{12,\phi}$ 等系数强微分，保留真实弱散度源。

$P_0U$ 有 R87 的9项，$-\chi'U_y$ 有5项，共14个 scalar 项。
$\chi E\nabla U$ 在 $C_0^{-1/2}$ 范数下分别为
$E_{12}U_\phi$、$E_{12}U_y/\sqrt y$、
$E_{22}U_\phi/\sqrt y$，每组5项；
$\chi'UC e_y$ 有3项，共18个 weak-flux 项。
最后一组准确满足
$|C^{-1/2}(\chi'UC e_y)|=|\chi'U|$，不需要相对矩阵误差费；
前三组乘 $(1-\varepsilon)^{-1/2}$ 即可。

为使每一项可重放，记其形状为
$c\,m(y,\phi)y^k\lambda^p\operatorname{Ai}^{(d)}
 (y\lambda^{2/3})$，$d=0,1$。
输入先乘 $\langle\lambda\rangle^2$，
scalar 费用另减 $2/3$ 角阶，flux 费用不减。
令 $L=4q_-(N+1)$，$q_*=p+2-\mathrm{loss}$，
$e=2k/3-q_*+1/3$。对非截断项，半线费为
$M_k(4/3)L^{-e}$；全部内禀项均严格有 $e>0$。
另用点态
$\sup_{z\ge0}z^r e^{-2z^{3/2}/3}
 =(r/e_{\rm Euler})^{2r/3}$
的准确形式，先对频率取 sup 再在有限 $[0,H]$ 积分，取两种真界较小值。

截断项支撑于 $y\ge H/2$，拆出一半指数后最大化
$\lambda^{-e}\exp[-(H/2)^{3/2}\lambda/3]$，其最大值准确在
$L$ 或正临界点取得。源码还与有限区间点态积分界比较。
全体费用再乘 $c=\sqrt{\operatorname{Ai}(0)/(-\operatorname{Ai}'(0))}$
和 $1+L^{-2}$。乘法用(96.19)，不是逐输入列代替全矩阵。

输入均值和 regular 有限输入槽使用零 trial，并留在真实有限反馈槽中；
输出均值、正负频率和 regular 通量在(96.12)中全部保留。
完整源费用 $\mathcal S_N,\mathcal F_N$ 给
$$
 \|\widetilde K(\text{完整 trial 残差})\|
 \le C_s\mathcal S_N+C_w\mathcal F_N,                         \tag{96.25}
$$
高根输出表则使用同一 $N$ 的高根 contact 常数。
这仍不是完整反射范数，尚须实际 incoming/outgoing frame 和其逆。

## 8. 实际完成报告与真实范围

原执行器失联前只观察到129格；未推送的大报告不被视为可用证明。
恢复源从真实输入完整重算全部178格，CI run **43300408666**
的六个区间 $[0,30),[30,60),[60,90),[90,120),[120,150),[150,178)$
及完整 collector 全部成功。后续 run **43301491511** 从该真实
artifact 运行本篇聚合，并由终端 Git 保存实际报告。

完整 mixed gzip SHA256：
$6f4c518f402dcb5b6fc7b19a50790e1e31d7d76e047f5bb2759aee66fb0ac93f$，
5,041,047 bytes。为遵守单文件5MB上限，以准确4,000,000和1,041,047
bytes 两片保存。manifest 位于
[canonical-mixed-recovery-complete-parts/manifest](../notes/2026-11-12-canonical-mixed-recovery-complete-parts/manifest.json)，
SHA256：
$7079605bb9dcb1876fda9f581170482f0064a44f7a42625c453dfc6e7f38faf4$。
重组源逐片和整体核 SHA，不重新序列化报告。

真实源及计算入口：

- scripts/fourfold_phase_canonical_collar_bivariate_recovery.py；
- scripts/fourfold_phase_canonical_mixed_recovery_run.py；
- scripts/fourfold_phase_canonical_mixed_recovery_collect.py；
- scripts/fourfold_phase_direct_canonical_source_budget.py；
- scripts/fourfold_phase_canonical_mixed_reassemble.py。

mixed 数学源 SHA256 为
$37f2e11402165075577d65349c2eebee830a6f17e11a6bcc94192dab3ed9be26$。
本篇聚合源 SHA256 为
$a4fb3ec6a1639c7f2756b7e44066cca5a68d8e1c805aa288cc8c70c8d9645417$。
完整 R96 报告 SHA256 为
$b568783f5270102aac2ed2d9656c6e86cc6acdce734358e53a0ac4a265513d3c$。
小摘要 [ci-direct-canonical-source-summary](../notes/2026-11-12-ci-direct-canonical-source-summary.json)
保存全部外向端点及所有 $N$ 表。

实际全格给出
$$
 \begin{gathered}
 \varepsilon<1.552858\cdot10^{-6},\quad G_0<33.417980,\quad
 G_C<33.418006,\quad d_0>.9840089499,\\
 y/s>.9830630241,\quad \tau>1.1568011566,\quad
 .0559537987<Y_0'<.2880686267,\\
 \|T_0^{-1}\|_{H^{1/3}}\le1.246984,\qquad
 \sqrt{\sup J/\tau^2}<.379617.
 \end{gathered}                                               \tag{96.26}
$$

|根输出范围，保 regular 槽|ordinary contact 上界|weak contact 上界|
|---|---:|---:|
|全部根频率|96.984892|48.482093|
|canonical $|k|>64$|16.496266|8.187268|
|canonical $|k|>256$|15.399256|7.634392|
|canonical $|k|>65536$|14.794595|7.329372|

这里的高频只限制根 test trace，没有把完整正帽中的低高交叉删掉。
在 $N=64$，真实完整源表为
$$
 \mathcal S_{64}<110252821723,\qquad
 \mathcal F_{64}<110139517638,\qquad
 C_{s,64}\mathcal S_{64}+C_{w,64}\mathcal F_{64}
 <2720501534106.                                             \tag{96.27}
$$
因此该表虽然闭合了源范数和contact费用，却尚未给出可用的小反射余项。

## 9. 大费用的明确位置

当 $\lambda$ 约为 $H^{-3/2}$ 时，截断自由 Ai 项尚未充分衰减，
而输入 $\langle\lambda\rangle^2$ 已很大。
在(96.24)中，$-\chi'U_y$ 与 $\chi'UC e_y$ 各自的 triangle
估计都出现这个费用。它不是从物理 height 换元遗留的未知常数。
仅提高 $N$ 到65536仍未跨过所有最大化频率，实际总源仍约
$1.1\cdot10^{11}$。不能把这条表称为有效 cutoff。

far chart 已另有完整1875格证明可到真实固定 $y=.0035$。
但它的较粗全系数模数不能免费替代本篇的 $G_C$ 和 mixed source 表；
真正扩大 cutoff 必须在同一宽领口支付这些输入。

## 10. 消去两个自由截断费的准确 Wronskian，保外端

设 $u$ 是**同一完整帽**的真实 homogeneous canonical test 解，
$P_{\rm can}u=0$。对完整 trial $U$ 定义
$$
 \mathcal W(y)=\int\left[
 U\,\overline{(C\nabla u)_y}-U_y\bar u\right]d\phi.             \tag{96.28}
$$
角向分部及 $P_0U=f_0$ 给准确恒等式
$$
 \mathcal W'(y)=
 \int\left[f_0\bar u+E\nabla U\cdot\nabla\bar u\right]d\phi.
                                                               \tag{96.29}
$$
于是(96.24)的全部 paired 源与同一个 test 的作用为
$$
 \int_0^H\big(\chi\mathcal W'+\chi'\mathcal W\big)\,dy
 =-\mathcal W(0)
 =\int_0^H\!\!\int(f_0\bar u+E\nabla U\cdot\nabla\bar u)
                                      -\mathcal W(H).         \tag{96.30}
$$
因此两个大 cutoff 项可以准确合并，代价是必须支付真实外端
$\mathcal W(H)$。后者一般不为零，不能凭 Ai 衰减或“完整正帽”
字样直接省略。

物理试函数 $v_U=\tau U$ 与 $v=\tau u$ 的真实 conormal Wronskian，
经过同一个 Piola 换元，准确成为
$$
 \int\left[
 U\,\overline{(C\nabla u)_y}
                  -(C\nabla U)_y\bar u\right]d\phi .
$$
两项中的 height 导数相消。它与(96.28)的差仍是
$\int E_{12}U_\phi\bar u$，必须保留；边界密度是参数域的真实
conormal 密度，不是未经换算的三维面积元素。

若在真实外端 $y=H$ 消去其余帽段，以真实 trace 变换后的完整外帽
非负 DN/regular 形式写成
$$
 \mathbb K_H=
 \begin{pmatrix}K_H&L_H\\L_H^*&k_H\end{pmatrix}
$$
作用于 $(u(H),\xi)$，则真实 matching 为
$$
 (C\nabla u)_y|_H=-K_Hu(H)-L_H\xi-g_Hu(H),\quad
 g_H=(\partial_y\log\tau+E_{12}\partial_\phi\log\tau)|_H.
$$
这里外帽的 outward 方向在左端为负 $y$。由自伴性，
$$
 \mathcal W(H)=
 -\langle K_HU(H)+U_y(H)+g_HU(H),u(H)\rangle
                   -\langle U(H),L_H\xi\rangle.              \tag{96.31}
$$
regular cross 项 $L_H$、height shear 和全部角耦合都在式内。
若外帽还有普通源，还需附加其真实 affine contact。
R95 的 $r=1/4$ 端口不等于本篇的 $y=H$ 端口，
不能直接替换(96.31)。这给出了接下来真正需要支付的外端量；
(96.30)本身已经是完整恒等式，不是省略外端后的猜测。

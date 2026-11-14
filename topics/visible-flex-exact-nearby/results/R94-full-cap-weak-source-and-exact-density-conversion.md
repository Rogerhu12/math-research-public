# R94：完整未压缩帽的弱源 contact、真实密度换元与 Airy 散度残差

2026-11-12，independent-audit。

**状态：完整证明；同一实际正帽的弱源常数和下列全部 18 个弱通量项预算已支付。**
本篇保留完整 root 零模、regular 平均值/平均通量及所有低高频耦合。
对根迹作高频限制时，体解仍是完整未压缩帽的解。
真实高度换元产生的标量项明确保留；最后的通量表不是完整试解残差，
更不是完整反馈逆。当前窄 cutoff 仍给很大费用，后续必须继续压紧。

## 1. 同一实际实现及空间

使用 R66/R69/R74/R85 的公共准确参数盒
\[
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 |\delta-\delta_5|\le1/2500000 .
 \tag{94.1}
\]
在物理坐标 \(s=r-t(\delta),\theta\) 中，完整正 form 为
\[
 b(u,v)=\int_0^L B\nabla u\cdot\overline{\nabla v}
       +\langle\Gamma_Hu(L),v(L)\rangle,\qquad L=25/8-t,
 \tag{94.2}
\]
\[
 B=\begin{pmatrix}
   \alpha&-\alpha q\\-\alpha q&\alpha q^2+\eta K_0
   \end{pmatrix}.
 \tag{94.3}
\]
\(\Gamma_H\ge0\) 是同一实际无限尾的完整 Robin 算子，
其常数 form 槽取零；真正的 regular 平均值 \(\xi\) 和对应通量
\(\lambda\) 仍按 R74 保留。记
\[
 H(a,\xi)(0)=a,\qquad
 \operatorname{mean}_{\rm physical}H(a,\xi)(L)=\xi .
 \tag{94.4}
\]
这里 \(H\) 是整个帽上的实际调和 Poisson 算子。固定两项迹后，
它在真实 form 中最小化能量；并未在根领口的外缘追加 Dirichlet 条件。

根角采用 \(d\theta\) 的实际测度及四重模 \(e^{4ik\theta}\)；
regular 平均值采用 R85 的归一化常数基。相应 trace/contact 空间为
\[
 X=H^{1/3}_{\theta}\oplus\mathbb C,\qquad
 X^*=H^{-1/3}_{\theta}\oplus\mathbb C .
 \tag{94.5}
\]
R66 的 root-anchored shear 在根为恒等，因而这里与 R85 的根角
norm 准确相同；体内的物理密度则始终保留。

## 2. 完整帽的能量型弱源

对可测向量场 \(F\)，定义
\[
 \ell_F(v)=\int F\cdot\overline{\nabla v},\qquad
 \|F\|_{\mathcal E^*}^2=\int F^*B^{-1}F .
 \tag{94.6}
\]
退化根处使用自然加权可积意义。实际源只要此 norm 有限，便在
齐次双迹空间上定义有界弱泛函；R74 的同一实现给相应解。
定义完整 contact
\[
 \langle K_{\rm div}F,(a,\xi)\rangle
              =-\ell_F(H(a,\xi)).
 \tag{94.7}
\]
这与带源 Green 恒等式一致，第二输出槽就是 regular 平均通量。
若改写成普通源 \(-\operatorname{div}F\)，必须同时保留 \(F\) 的真实
边界法向负荷；当 \(F\) 的边界法向迹为零时，无须额外边界项。

令 \(l=1/4-t\)。R85 的实际局部延拓及 regular 平均延拓给
\[
 b(H(a,0),H(a,0))\le E_a\|a\|_{H^{1/3}}^2,\quad
 E_a=M_c\max\{l_-^{-1},13/12\},
 \tag{94.8}
\]
\[
 b(H(0,\xi),H(0,\xi))\le E_\xi|\xi|^2,\qquad
 E_\xi=M_g/L_- .
 \tag{94.9}
\]
它们使用真实 \(M_c,M_g,l_-,L_-\)，包括正确 shear 密度和外尾。
对 \(B\) 能量内积用 Cauchy--Schwarz，再对两个 trace 槽用二维
Cauchy--Schwarz，得到
\[
 \boxed{\quad
 \|K_{\rm div}F\|_{X^*}
 \le\sqrt{E_a+E_\xi}\,\|F\|_{\mathcal E^*}
 <62.921979\,\|F\|_{\mathcal E^*}.
 \quad}
 \tag{94.10}
\]
这是完整未压缩帽的全部输出界。它不需要 \(P_NB=BP_N\)，也没有
使用高体 coercivity 或删除任何体频率。

## 3. 只限制根迹时的更小完整 contact 费

令 \(P_N\) 保留物理 \(|k|>N\)，
\[
 X_N=\{a:P_Na=a\},\quad
 \|a\|_{X_N}=\||D_\theta|^{1/3}a\|_2,\quad
 \lambda_N=4(N+1).
 \tag{94.11}
\]
取 R90 的真实 shear 延拓
\[
 Ea(s,\theta)=
 \sum_{|k|>N}(1-s/h_k)_+a_k e^{4ik\varphi(s,\theta)},
 \qquad h_k=\min\{l,|4k|^{-2/3}\}.
 \tag{94.12}
\]
这里**不在体内施加 \(P_N\)**。这正是完整 Poisson 解允许使用的
合法竞争函数：根迹为 \(a\)，regular 平均值和 regular 迹均为零。
R90 的准确换元与逐模 ramp 积分直接给
\[
 b(Ea,Ea)\le\widetilde E_N\|a\|_{X_N}^2,\qquad
 \widetilde E_N=M_c\left[d_N+\frac1{12}\right],\quad
 d_N=\max\{1,(l_-\lambda_N^{2/3})^{-1}\}.
 \tag{94.13}
\]
因此最小化和 (94.7) 给
\[
 \|P_NK_{{\rm div},0}F\|_{X_N^*}
       \le\sqrt{\widetilde E_N}\|F\|_{\mathcal E^*},
 \tag{94.14}
\]
\[
 \boxed{\quad
 \|(P_NK_{{\rm div},0}F,K_{{\rm div},{\rm reg}}F)\|
 \le\sqrt{\widetilde E_N+E_\xi}\|F\|_{\mathcal E^*}.
 \quad}
 \tag{94.15}
\]
体解 \(H(a,0)\) 可以产生全部低频；这些低频的真实影响已经留在
能量最小化中。此处的输出投影不同于 R90/R93 的高体限制实现。
对所有根输出使用 (94.10)，不能把 (94.15) 免费转成 canonical
高模的相同投影；后者仍需真实角/height/frame 转换。

已支付的严格安全数值为

| 物理根切值 \(N\) | 完整帽高根弱 contact | 连同 regular \(\lambda\) |
|---:|---:|---:|
| 0 | 39.430623 | 40.071024 |
| 16 | 15.439232 | 17.008317 |
| 64 | 9.985960 | 12.273238 |
| 128 | 8.033033 | 10.744421 |
| 256 及以上 | 7.009070 | 10.002001 |

全部根含零模和 regular 的界仍是 (94.10)。表中 \(N=0\) 只表示
根输入不含物理零模，不表示完整实现商掉了该模。

## 4. 实际坐标和高度换元的准确弱源公式

设 R87 的有限真实坐标为
\[
 \Psi(s,\theta)=(y,\phi),\quad J=\det D\Psi>0,\quad
 A=J^{-1}D\Psi\,B(D\Psi)^T,\quad \tau=A_{11}^{-1/2},
 \tag{94.16}
\]
\[
 C=\tau^2A=
 \begin{pmatrix}1&E_{12}\\E_{12}&y+E_{22}\end{pmatrix},
 \qquad P_{\rm can}=-\operatorname{div}_{y,\phi}(C\nabla)+V .
 \tag{94.17}
\]
R87 的准确共轭式是
\[
 P_{\rm ground}(\tau U\circ\Psi)
                  =\frac J\tau(P_{\rm can}U)\circ\Psi .
 \tag{94.18}
\]
现设
\[
 P_{\rm can}U=f-\operatorname{div}_{y,\phi}F .
 \tag{94.19}
\]
那么在物理坐标中准确有
\[
 P_{\rm ground}(\tau U\circ\Psi)
                   =f_{\rm ph}-\operatorname{div}_{s,\theta}F_{\rm ph},
 \tag{94.20}
\]
\[
 \boxed{\quad
 F_{\rm ph}=\frac J\tau(D\Psi)^{-1}F\circ\Psi,\qquad
 f_{\rm ph}=\frac J\tau
       \left(f-\nabla_{y,\phi}\log\tau\cdot F\right)\circ\Psi.
 \quad}
 \tag{94.21}
\]
其中 \(\tau\) 在右侧视作 canonical 坐标中的同一个函数。

**证明。** Piola 恒等式给
\[
 J(\operatorname{div}_{y,\phi}F)\circ\Psi
 =\operatorname{div}_{s,\theta}
       \big[J(D\Psi)^{-1}F\circ\Psi\big].
\]
再对外因子 \(1/\tau\) 用乘积法则。因为
\(\nabla(1/\tau)\cdot J(D\Psi)^{-1}F
=-(J/\tau)\nabla_{y,\phi}\log\tau\cdot F\)，正是 (94.21)。
特别高度梯度项带负号，不能仅把 canonical 散度密度乘 \(J/\tau\)
后当作一个物理散度。

同时有精确能量恒等式
\[
 \boxed{\quad
 \int F_{\rm ph}^*B^{-1}F_{\rm ph}\,ds\,d\theta
       =\int F^*C^{-1}F\,dy\,d\phi .
 \quad}
 \tag{94.22}
\]
事实上 \(C^{-1}=(J/\tau^2)(D\Psi)^{-T}B^{-1}(D\Psi)^{-1}\)，
再用 \(dy\,d\phi=J\,ds\,d\theta\) 即得。该式是实际向量密度换元；
没有将一个未带密度的函数复合范数冒充通量 norm。

当前真实 scalar splines 在内部 knots 至少 \(C^4\)。所用有限坐标
在根系数中定义后沿物理 \(s\) 延伸；实际 \(B,\tau\) 在每个准确
scalar span 中用该 span 的原函数计算。上述弱恒等式要求的低阶
系数/通量在接缝连续，故逐 span 分部无新增跳跃源。这不把
高阶一侧 jets 升级成跨 knots 的解析正则性。

## 5. 整个 cutoff 与主系数误差的散度分解

写
\[
 C_0=\operatorname{diag}(1,y),\quad E=C-C_0,\quad
 P_0=-\partial_y^2-y\partial_\phi^2+V .
 \tag{94.23}
\]
令 \(U\) 为 R87/R91 的完整正侧校正 Airy trial，记其准确
principal-free 残差 \(P_0U=f_0\)。取实际光滑 cutoff \(\chi(y)\)。
则一个完整的、避免 \(E_\phi\) 和 \(\chi''\) 的表达是
\[
 \boxed{\quad
 P_{\rm can}(\chi U)=
       \chi f_0-\chi' U_y-\operatorname{div}F_\chi,\qquad
 F_\chi=\chi E\nabla U+\chi'U\,C e_y .
 \quad}
 \tag{94.24}
\]
**验证。** 把
\(P_{\rm can}U=f_0-\operatorname{div}(E\nabla U)\)
乘 \(\chi\) 后，散度的乘积法则贡献
\(\chi'E_{12}U_\phi\)。另一方面，对整个 \(C\) 使用
\[
 P_{\rm can}(\chi U)
 =\chi P_{\rm can}U-\nabla\chi\cdot C\nabla U
                         -\operatorname{div}(UC\nabla\chi).
 \tag{94.25}
\]
其中 \(-\nabla\chi\cdot C\nabla U
=-\chi'U_y-\chi'E_{12}U_\phi\)，两项 \(E_{12}U_\phi\) 准确抵消，
于是得到 (94.24)。没有删去 cutoff 的交叉项。

应用 (94.21)，真正普通源是
\[
 \boxed{\quad
 f_{\rm ph}=\frac J\tau
  \left[\chi f_0-\chi'U_y
        -\chi\,\nabla\log\tau\cdot E\nabla U
        -\chi' U\,g\right]\circ\Psi,\quad
 g=\partial_y\log\tau+E_{12}\partial_\phi\log\tau .
 \quad}
 \tag{94.26}
\]
真正弱通量是 (94.21) 对 \(F_\chi\) 的变换。由于 \(C_{11}=1\)，
cutoff 部分满足特别简单的**精确**恒等式
\[
 \|C^{-1/2}(\chi'U C e_y)\|_{L^2}=\|\chi'U\|_{L^2(dy\,d\phi)} .
 \tag{94.27}
\]
不需要估计 \(C\) 的各个大分量。

R87 的 \(E_{12}=O(s^6),E_{22}=O(s^7)\)，而 \(\chi'=0\) 在根邻域、
\(\chi=\chi'=0\) 在外 cutoff 之外。因此本试解的 \(F_\chi\) 在真实
根和 regular 端均有零法向迹。它可按普通散度源或弱源使用，
不会悄悄更改 root/regular 边界数据。

## 6. 实际能量比较与完整弱通量数值预算

由已完成的 R87 全 178 格，令 \(h=1/2048\)，\(a=y/s\)。
真实全域满足
\[
 \left\|C_0^{-1/2}EC_0^{-1/2}\right\|
 \le \frac{|E_{12}|}{\sqrt y}+\frac{|E_{22}|}{y}
 <\varepsilon_C,\qquad
 \varepsilon_C<.000194370089 .
 \tag{94.28}
\]
程序对每个真实格使用其自己的 \(a_-\)、\(E_{12}/s^6\)、
\(E_{22}/s^7\) 界，按
\[
  (E_{12}/s^6)_{\max}a_-^{-1/2}h^{11/2}
       +(E_{22}/s^7)_{\max}a_-^{-1}h^6
 \tag{94.29}
\]
聚合。故 \(C\ge(1-\varepsilon_C)C_0\)，有
\[
 \|C^{-1/2}E\nabla U\|_2
 \le(1-\varepsilon_C)^{-1/2}
  \left(\|E_{12}U_\phi\|_2+
        \|E_{12}U_y/\sqrt y\|_2+
        \|E_{22}U_\phi/\sqrt y\|_2\right).
 \tag{94.30}
\]
所有 norm 在真正 \(dy\,d\phi\) 中。改成固定 canonical 角的 \(s\)
积分时，准确 Jacobian 是
\[
 \left.\frac{\partial y}{\partial s}\right|_\phi
       =\frac J{\phi_\theta}<1.065816154 .
 \tag{94.31}
\]
这与只固定物理 \(\theta\) 时的 \(y_s\) 不同。

R91 的 Airy 解析因子化在这里只用 \(L^2\) 乘法模数，
不使用角导数。真实 \(\|a-1\|_\infty<.016936976\) 给
\[
 G_0=\frac1{1-4\|a-1\|_\infty}<1.072671227 .
 \tag{94.32}
\]
取同一已证 majorant
\[
 B(z)=\tfrac32(1+z)e^{-c_*z^{3/2}},\qquad
 c_*=\frac{4463}{10752}.
 \tag{94.33}
\]
对每个 \(s^k\lambda^p Ai^{(d)}(\lambda^{2/3}as)\) 项，
施加输入 \(\langle D_\phi\rangle^2\) 后，整半线的对角费用由
\[
 M_k(2c_*)\,\lambda^{-e},\qquad
 e=\tfrac23k-p-\tfrac53,\quad
 M_k(c)^2=\frac94\sum_{j=0}^2{2\choose j}
              \frac23 c^{-2(2k+j+1)/3}
                  \Gamma\!\left(\frac{2(2k+j+1)}3\right)
 \tag{94.34}
\]
控制。程序也与真实有限 \(s\)-区间的逐点频率最大值比较，取更小的
严格界；cutoff 项另保留其真实 \(s\ge s_0>0\) 的指数衰减。
半整数 \(k\) 同样直接由 Gamma 积分支付。所有乘法、正负 Fourier
输入、全部输出行和 Parseval 求和都在 \(L^2\) 中完成，未从逐列
估计直接跳到无限矩阵算子 norm。

使用 R91 完全相同的 cutoff
\[
 y_{\rm out}=\frac{49}{50}h,\quad y_{\rm in}=\frac{49}{100}h,\quad
 \|\chi'\|_\infty\le\frac{15}{8(y_{\rm out}-y_{\rm in})},
 \tag{94.35}
\]
下列 18 项全部纳入：\(E_{12}U_\phi\) 的 5 项，
\(E_{12}U_y/\sqrt y\) 的 5 项，\(E_{22}U_\phi/\sqrt y\) 的 5 项，
以及 \(\chi'U\) 的 3 项。它们准确覆盖 (94.24) 的整个弱通量。
得到例如

| canonical 输入切值 \(N\) | 主误差弱通量 | cutoff 弱通量 |
|---:|---:|---:|
| 64 | \(7.537753\,10^7\) | \(9.576087\,10^{11}\) |
| 256 | \(7.537752\,10^7\) | \(9.576085\,10^{11}\) |
| 4096 | \(7.537752\,10^7\) | \(9.576085\,10^{11}\) |
| 65536 | \(2.524681\,10^7\) | \(9.575401\,10^{11}\) |

这些是原有完整系数证书给出的安全上界。表格乘 (94.10) 可用于
相应弱源的**完整** root 和 regular contact，且无需体频率压缩。
但 (94.26) 中的所有标量项仍必须另付；本表不能与缺项的标量预算
相加后假称完整反射。当前极窄 cutoff 的费用依旧不可用。
正在进行的更宽真实正段和混合 Taylor 全角计算不作为本篇已付输入。

## 7. 重放和作用范围

源为 scripts/fourfold_phase_full_weak_source_budget.py，报告为
notes/2026-11-12-actual-full-weak-source-budget.json。
程序核对同一实际 origin/direction、公共准确参数包含关系、完整
closed-to-Robin 接合 SHA、R87 全角准确覆盖及其原始依赖 SHA。
实际输入为已登记的 R66/R69/R74/R87 以及完整根频率证书。

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python -u scripts/fourfold_phase_full_weak_source_budget.py \
      --out notes/2026-11-12-actual-full-weak-source-budget.json

本篇关闭的是完整帽的弱源 contact 及其真实密度/高度转换，
并实际支付全部显示的弱通量项。它不替代 (94.26) 的标量源、
实际 Airy 到边界通量 frame、完整低高 Schur 或非线性零解。

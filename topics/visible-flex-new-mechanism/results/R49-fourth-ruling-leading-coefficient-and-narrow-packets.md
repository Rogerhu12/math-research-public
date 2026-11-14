# R49：四阶沿母线最高次与窄packet严格障碍

日期：2026-11-14。literature 推导，repo_sources 独立逐项手核，root 全文复核。独立完整证明；未运行新几何研究计算。

本稿接 [四块倒行](R45-reversal-four-block-third-period-cancellation.md)、[八 packet 完整三阶圆](R46-eight-packet-complete-third-order-circle.md)及[四阶 range/gauge 约简](R47-fourth-order-range-and-third-gauge.md)。这里的空间变量仍记为 s；相位写作 theta，避免把 sin(theta) 与空间坐标混淆。**结论限于所给一阶 profile 圆及同 collar 的形式延拓；不排除其他 profile、其他几何或其他有限族。**

## 1. 任何常段上不受段首常数影响的最高次项

固定一个非空开区间，其中 k、h、omega 都为常数。令 sigma=s-s0。在这个状态定义

$$E(\phi,\psi)=\int(Y_\phi)_u\cdot(Y_\psi)_u\,du,$$

并把单平方 forcing 的完整 characteristic 右侧记为 $\mathcal R(\phi,\phi)$，用对称双线性极化定义 $\mathcal R(\phi,\psi)$。所以

$$\mathcal R_{\mathcal S(Y_\phi,Y_\psi)}=2\mathcal R(\phi,\psi).$$

置

$$R=\mathcal R(f,f)-\mathcal R(g,g),\qquad B_f=\mathcal R(f,R),\quad B_g=\mathcal R(g,R).$$

常段上 c=0，二阶平方 forcing 的 eta0=0，rho_d 与 s 无关。保留真实段首函数 W0，准确有

$$Z_d=\rho_d N-Y_{W_0+\sigma R}.
\tag{1}$$

因此 $Z_d$ 在旋转标架中的一次首项为 $-\sigma Y_R$。第三 forcing $-\mathcal S(Y_\phi,Z_d)$ 的一次首项为 $\sigma\mathcal S(Y_\phi,Y_R)$，其 characteristic 右侧一次首项为 $2\sigma\mathcal R(\phi,R)$。积分并恢复后，第三阶解 $W_\phi$ 的二次首项严格为

$$W_\phi=-\sigma^2Y_{B_\phi}+O(\sigma).
\tag{2}$$

这里 $O(\sigma)$ 表示次数至多一次的精确标架多项式，不是极限误差。段首积分常数、rho3 及恢复中的 s 导数只进入较低次项。

四阶三个 forcing 仍为

$$A=-\mathcal S(Y_f,W_f),\quad
B=-\mathcal S(Y_f,W_g)-\mathcal S(Y_g,W_f),$$

$$C=-\{(dZ_d)^2+\mathcal S(Y_g,W_g)\}.$$

将 (1)–(2) 代入完整 ruling 积分，得到它们的 sigma² 系数：

$$\boxed{a_2=2E(f,\mathcal R(f,R)),}\tag{3a}$$

$$\boxed{b_2=2\{E(f,\mathcal R(g,R))+E(g,\mathcal R(f,R))\},}\tag{3b}$$

$$\boxed{c_2=-E(R,R)+2E(g,\mathcal R(g,R)).}\tag{3c}$$

常段上几何向量 w 为常数，所以任何落在全局三维 gauge 空间 $\{s\mapsto w(s)\cdot v\}$ 的函数，在此段必须为常数。故 (3) 三个系数全部为零是四阶可解的必要条件。

这一最高次检验比固定某个段首 W0 更稳定：任意周期、同 collar 二阶齐次改动都是某个 $Y_\psi$，在常段只改变 (1) 的常数项；第三阶齐次改动同样只改变常数项。因此 (3) 也不受这些二阶或三阶 profile gauge 影响，包括相位依赖的选择。它仍以给定 $Y_\theta=\cos\theta Y_f+\sin\theta Y_g$ 和固定目标 $g_X+\varepsilon^2(dY_f)^2$ 为前提。

## 2. k=0、h=1、omega=0 的完整局部公式

这一常状态确实出现在 R37 及其单 P 倒行变体的完整圈段。记 x=xi，$Q=1+x^2$。对于任意紧支撑实 profile f，定义

$$J_f(x)=\int_x^{r}\{Q(y)f''(y)^2+2f'(y)^2\}\,dy.$$

单状态 characteristic 映射准确为

$$\mathcal R_0(f,f)=-\frac{Qf'^2+xJ_f}{8}.
\tag{4}$$

其双线性版本由 $f'^2\mapsto f'g'$、$f''^2\mapsto f''g''$ 定义。写

$$a_f=xf''-f',\qquad F_f=Qf''-2f.$$

直接两次求导，并使用 $J_f'=-Qf''^2-2f'^2$，得到

$$\boxed{\mathcal R_0(f,f)''=
\frac14 a_f(a_f+Qf''').}\tag{5}$$

极化给

$$\mathcal R_0(f,r)''=
\frac14a_fa_r+\frac Q8(a_fr'''+a_rf''').
\tag{6}$$

这里 r 可以是任意光滑函数，未要求其尾部为零。由于 f 紧支撑，以下积分均无端项。

此状态的能量为

$$E(f,v)=\frac14\int Qf''v''+\frac12\int f'v'
=\frac14\int F_fv''.$$

把 (6) 代入，先用 $F_f'=Qf'''+2a_f$，再对 r''' 和 r' 分部积分，得到

$$\boxed{E(f,\mathcal R_0(f,r))=
\frac1{32}\int\left\{\frac{F_f^2}{2}-2Qa_f^2-Q^2a_ff'''\right\}r''.
}\tag{7}$$

为使分部积分可逐点核对，(6) 代入后的被积式减去 (7) 的被积式，恰为

$$\frac1{32}\frac d{dx}
\left\{F_fQa_fr''-\frac12F_f^2r'\right\}.$$

## 3. 支撑不交时，A 的最高次只看 f 自己

若 f、g 的支撑互不相交，那么在 f 的支撑邻域，$\mathcal R_0(g,g)$ 的二阶导数为零：从 (4) 看，右尾 J_g 在该邻域为常数，留下的仅是仿射函数。于是 (7) 给

$$E(f,\mathcal R_0(f,R))
=E(f,\mathcal R_0(f,\mathcal R_0(f,f))).$$

定义单 profile 四次泛函

$$T(f)=E(f,\mathcal R_0(f,\mathcal R_0(f,f))).$$

由 (5)、(7) 有完全局部的表达式

$$\boxed{T(f)=\frac1{128}\int
\left\{\frac{F_f^2}{2}-2Qa_f^2-Q^2a_ff'''\right\}
 a_f(a_f+Qf''').}\tag{8}$$

因此此常段的 $a_2=2T(f)$，与不交 g 的形状、符号、位置无关。如果 $f=\sum_j A_j f_j$ 且各 f_j 支撑互不相交，则同理

$$T(f)=\sum_j A_j^4T(f_j).
\tag{9}$$

这里只消去了不交支撑所留下的仿射尾；没有把所有三阶校正在 packet 间错误地局部化。

## 4. 可证明的严格负号范围

本稿**没有证明任意非零紧支撑 f 都有 T(f)<0**。以下两个较窄结论直接由 (8) 得出。

**平移。** 固定非零 $\eta\in C_c^\infty(\mathbb R)$，令 $f_t(x)=\eta(x-t)$。代换 y=x-t 后，$T(f_t)$ 是 t 的次数至多八的多项式，其最高次系数准确为

$$[t^8]T(f_t)=-\frac1{128}\int\eta''(y)^2\eta'''(y)^2\,dy<0.
\tag{10}$$

最高项仅来自 (8) 中的 $-Q^3a_f^2f'''^2/128$；其余项次数至多七。积分严格正，因为若 $\eta''\eta'''\equiv0$，则 $(\eta''^2)'=0$；紧支撑迫 $\eta''=0$，再迫 eta=0。

**共同窄化。** 固定 c 非零，令 $f_\lambda(x)=\eta((x-c)/\lambda)$，$\lambda>0$。逐项缩放 (8)，在固定紧支撑上有

$$\boxed{T(f_\lambda)=
-\frac{c^2(1+c^2)^3}{128\lambda^9}
\int\eta''^2\eta'''^2+O(\lambda^{-8}).}\tag{11}$$

这是真实积分的渐近式；余项可由有限个 eta 导数积分控制，未对未知余项求导。故对充分小的正 lambda，T 严格为负。

对于多个固定原位置的互不交 bump，先组成 $F(y)=\sum_j A_j\eta(y-b_j)$，再令 $f_\lambda(x)=F((x-c)/\lambda)$，同一公式给

$$T(f_\lambda)=
-\frac{c^2(1+c^2)^3}{128\lambda^9}
\left(\sum_j A_j^4\right)\int\eta''^2\eta'''^2
+O(\lambda^{-8})<0.
\tag{12}$$

## 5. 对当前八 packet 构造的准确影响

八 packet 证明允许把整个有限 profile 圆共同仿射缩入任意正物理区间，且所有二阶与三阶恒等式在这个缩放后仍成立。选择正区间内 c，并把全部 packet 共同以 lambda 收缩到 c。其 f、g 仍支撑不交。

对于 f0 的四个 bump，幅度四次和为

$$2\{(19/30)^2+(11/30)^2\}=\frac{241}{225}.$$

八 packet 的幅度为 $a_j=(-1)^j\binom7j^{1/3}$，因此全 f 的四次幅度和为

$$\frac{241}{225}\sum_{j=0}^7\binom7j^{4/3}>0.$$

由 (12)，对充分小的 lambda，当前常 k=0 段上 $a_2=2T(f_\lambda)<0$。所以四阶 ruling 是有非零二次项的真实 s 多项式，不能落在该常段上恒定的 gauge 空间内。

**结论：** 上述共同窄化的八 packet 三阶圆，虽已完整满足到三阶，却不能延拓到四阶；任意同 collar 二阶、三阶齐次 gauge 都不能修复这一最高次障碍。这个结论严格限于给定一阶圆及该几何的常 k=0 段，未排除较宽的 profile、支撑重叠的 profile 圆、改变几何的构造，或其他非线性家族。

这个检验也说明：不能仅因第三阶有限差分准确成功，就把同一窄 packet 直接送入完整四阶大规模数值求解。下一问题是 (8) 的更大符号范围，或选择真正能使 (3) 消失的一阶 profile 与几何。

## 6. 精确代数证书

配套 `scripts/literature_fourth_constant_leading_certificate.py` 仅核对 (5)、(6)、(7) 的总导数，以及 (10)、(11) 的最高次系数；不执行几何 ODE、profile 优化或数值积分。符号恒等式与上文的支撑/锚/范围论证分开陈述。

准确代数脚本 SHA256：`64690bc72441abe2f3e3ffc39482dd6f611c54e30b84b35abf9e859d386dd772`。开发输出为 [754字节证书](../notes/literature-fourth-constant-leading-certificate-20261114.json)，SHA256 `d9d1ef018d8ac588bed9caa2436a7b1d9d66d6d678b7e16997147e7d0f3bec79`。支撑、最高次数、二阶自由校正范围和严格负号由全文证明，脚本只复核列明的代数。

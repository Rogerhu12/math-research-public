# R400 — 从全部平方插值恢复原完整 p-core，并确定 E24 的 CM7 绝对标量

日期：2026-11-14。**状态：以下有界测度引理、固定 E24 的全部普通 p-core（包括 p=7）、全部 tame/环带和原 CM7 标量已证明。主目标的跨素数中央非零仍未证明。**

本篇沿用 R395、R397 的同一原六项来源
$
 \Phi=G_{24}=\sigma^{72}P_{11}(x^3),\qquad \Phi(0)=0,
$
并始终保其实际标量，而不是预先将六阶首项除成一。
特别在 $p=7$ 时，首项归一可能改变整性；本证明使用的是
R395 已证明整的实际有限 theta 来源。

## 1. 一个全测度的平方符号刚性引理

设 $p$ 为奇素数，$\mathscr O\subset\mathbf C_p$ 为完备整数环，
$\nu$ 是 $\mathbf Z_p$ 上的有界整测度。记
$
 M_m=\int_{\mathbf Z_p}x^m\,d\nu,\qquad
 U_m=\int_{\mathbf Z_p^\times}x^m\,d\nu .
$
给定 $\lambda\in\mathscr O^\times$、$\kappa\in\mathbf Q_p$、
$v_p(\kappa)=1$。对 $k\bmod p-1$，定义
$
 G_k(T)=\int_{\mathbf Z_p^\times}
 \omega_p(x)^k
 (1+T)^{\log_p\langle x\rangle/\log_p(1+p)}\,d\nu(x),
 \quad t_m=(1+p)^m-1.
 \tag{1}
$
因此 $U_m=G_k(t_m)$ 当 $m\equiv k\bmod p-1$。

**引理。** 假设对每个 $k\bmod p-1$ 和每个正整数
$m\equiv k\bmod p-1$，有
$
 \boxed{G_k(t_m)^2=(1-\lambda\kappa^m)^2M_m^2.} \tag{2}
$
则有某个 $c\in\mathscr O$ 使
$
 \boxed{\nu|_{p\mathbf Z_p}-\lambda[\kappa]_*\nu=c\,\delta_0.} \tag{3}
$
其中
$
 c=(1-\lambda)\nu(\mathbf Z_p)-\nu(\mathbf Z_p^\times).
 \tag{4}
$
若另外 $\nu(\mathbf Z_p)=\nu(\mathbf Z_p^\times)=0$，则 $c=0$，
得到完整 prime-core，包含原点而无待定补偿。

若 $\nu$ 在某个 $\mu_e\subset\mu_{p-1}$ 下不变，
只需对 $e\mid k$ 的分支假设 (2)；
其他分支由实际对称性自动为零。

### 1.1 在真实等差权列上选定平方符号

置
$
 \eta=\nu|_{p\mathbf Z_p}-\lambda[\kappa]_*\nu.
$
其第 $m$ 矩为
$
 \eta_m=(1-\lambda\kappa^m)M_m-U_m. \tag{5}
$
因 $\nu$ 整，
$
 v_p(M_m-U_m)\ge m,\qquad
 v_p(\lambda\kappa^m M_m)\ge m,
$
所以
$
 \boxed{v_p(\eta_m)\ge m.} \tag{6}
$
这是同一个有界测度的估计，不是逐个权任意选择一个平方根。

固定 $k$。若 $G_k\equiv0$，(2) 与
$1-\lambda\kappa^m\in\mathscr O^\times$ 给
$M_m=U_m=0$，所以全部这些正权的 $\eta_m=0$。

若 $G_k\not\equiv0$，函数
$u\mapsto G_k((1+p)^u-1)$ 在 $\mathbf Z_p$ 上解析。
正整数 $u\equiv k\bmod p-1$ 在 $\mathbf Z_p$ 稠密，
故可选其中一个 $a_0$，使其值非零。
连续性给 $N\ge0$ 及固定有限 $C\ge0$，使
$
 v_p(G_k(t_m))=C
 \quad\text{只要 }m\equiv a_0\pmod{(p-1)p^N}.
$
令 $d=(p-1)p^N$，在此同余类中选 $a>C$、$a>0$。
对每个 $j\ge0$，$m=a+dj>C$。式 (2) 有两个可能符号。
如果取负号，(5) 就是
$\eta_m=-2G_k(t_m)$，其赋值为 $C<m$，与 (6) 矛盾。
因此对这一整条无限等差列，准确有
$
 \boxed{\eta_{a+dj}=0\qquad(j\ge0),\quad a\equiv k\bmod p-1.} \tag{7}
$
当 $G_k\equiv0$ 时也可任选这样的正 $a$ 和 $d$ 得到 (7)。
这里并未声称每个其他单独权的符号已先行确定；
下一步由整测度的唯一性一次恢复它们。

### 1.2 等差矩与有限纤维恢复整个 tame 分量

令 $q_d(x)=x^d$，并将带权测度 $x^a\eta$ 推前到 $\mathbf Z_p$。
由 (7)，其全部非负整数矩为零：
$
 \int y^j\,d(q_{d,*}(x^a\eta))(y)
 =\eta_{a+dj}=0\qquad(j\ge0). \tag{8}
$
多项式在 $C(\mathbf Z_p,\mathbf Q_p)$ 中一致稠密
（例如使用 Mahler 二项多项式），且测度有界；
因此
$
 q_{d,*}(x^a\eta)=0. \tag{9}
$

为明确 (9) 恢复的是什么，记真正的 tame 投影
$
 \eta_k=\frac1{p-1}
   \sum_{\zeta\in\mu_{p-1}}\zeta^{-k}[\zeta]_*\eta .
 \tag{10}
$
因为 $a\equiv k\bmod p-1$ 且 $d\equiv0\bmod p-1$，
$
 q_{d,*}(x^a\eta_k)=q_{d,*}(x^a\eta)=0,
$
而 $x^a\eta_k$ 在 $\mu_{p-1}$ 下不变。

对每个非零环带 $p^n\mathbf Z_p^\times$，
$q_d$ 的纤维准确是 $\mu_{p-1}$-轨道：
若 $x^d=y^d$，则 $x/y\in\mathbf Q_p$ 是根单位；
其全部可能值正是 $\mu_{p-1}$。
因此 $q_d$ 从该环带的紧商空间到其像是同胚。
一个不变有界测度由其此商上的推前唯一确定。
式 (9) 遂给 $x^a\eta_k=0$ 于每个非零环带，
而 $x^a$ 在每个固定环带上可逆，故
$
 \eta_k|_{\mathbf Z_p\setminus\{0\}}=0. \tag{11}
$
对全部 $k$ 求和，$\eta$ 只支撑在原点。
有界测度支撑于一个点必为 $c\delta_0$，总质量给 (4)，引理得证。

这个证明不需要 theta 空间的单重本征线，
也不把非 principal 分支的质量设为零。
原点 Dirac 项明确留下，只有在总质量条件付清后才能删除。

## 2. E24 的每一个实际 tame 平方

现在固定任意
$
 \boxed{p>3,\quad p\equiv1\pmod3,} \tag{12}
$
并采用 R397 的 CM 嵌入及相容周期。特别允许 $p=7$。
R395 的九阶 lift 和原整来源在所有这些素数处都有效；
R397 的普通 sigma 唯一性及 Amice 构造也只需好普通 $p>3$。
故
$
 \Phi(\Omega_p\log(1+Z))=\int(1+Z)^x\,d\nu_p(x)
$
是原整测度，$M_m=\Omega_p^m m!s_m$，且 $\mu_6$ 不变。

令
$
 \pi=\psi_{24}(\mathfrak p),\quad
 \bar\pi=\psi_{24}(\bar{\mathfrak p}),\quad
 \lambda=\bar\pi^{-1},\quad
 \kappa=p/\bar\pi^2=\pi/\bar\pi.
 \tag{13}
$
$\pi,\bar\pi$ 是原 Hecke 值，不能任意换 primary 生成元；
在选定分裂完成里 $\kappa\in\mathbf Q_p$、$v_p(\kappa)=1$。

对每个 $k\bmod p-1$ 且 $6\mid k$，固定 Katz 的实际有限 tame 分支
$\mathcal K_k(T)$，使其正权 $m\equiv k\bmod p-1$ 对应
$\epsilon_m=\psi_{24}^{m+1}\bar\psi_{24}^{-m}$。
这些 $m$ 均被六整除，所以 R389 的完整坏位角色和原导子
$(8\delta^4)$ 保持不变。
Katz 插值和 R397 的已经算出的实际周期比较给
$
 \mathcal K_k(t_m)=
 C_p\,72^{-m}(1-\lambda\kappa^m)^2M_m^2,
 \quad C_p=(\kappa_{24}/s)\Omega_p\ne0. \tag{14}
$
此处不需要 $C_p$ 为单位；它是固定非零的代数周期因子。

同 R397 的原极限，固定同余类中的 $m_0\ge0$，令
$m_j=m_0+(p-1)p^j$。
非单位矩和 Euler 误差赋值至少 $m_j$，故趋于零，
而 $72^{-m_j}$ 的极限保留该分支的真实 tame 因子。
因此整条分支为
$
 \boxed{\mathcal K_k(T)=
 C_p\,\omega_p(72)^{-k}
 (1+T)^{-a_{72,p}}G_k(T)^2.} \tag{15}
$
这里 $G_k$ 是 (1) 对同一 $\nu_p$ 的定义。
固定非 principal 分支没有与 principal 分支混同。

在同一个正权 $t_m$ 比较 (14)、(15)，约去非零的固定因子，
正好得到引理所需
$
 \boxed{G_k(t_m)^2=(1-\lambda\kappa^m)^2M_m^2.} \tag{16}
$
对 $6\nmid k$，来源的实际 $\mu_6$ 对称给全部相应矩和
$G_k$ 为零，故 (16) 也成立。
不需要额外假设这些非 principal Katz 分支都非恒零：
引理已单独包括 $G_k\equiv0$ 的情形。

## 3. 原点质量与全部普通 p-core

由原来源 $\Phi(0)=0$，总质量 $M_0=0$。
还必须支付真正单位质量。
R393 已由 $r\ge2$ 及已出版的解析秩零结论给
$L(E_{24},1)=0$。
Katz 在 $m=0$ 的同一正根数分支因而满足
$\mathcal K_0(0)=0$。
式 (15) 的固定因子非零，所以
$
 G_0(0)=\nu_p(\mathbf Z_p^\times)=0. \tag{17}
$
这不使用待证的首导数非零。

引理现在准确消去原点项，得到
$
 \boxed{\nu_p|_{p\mathbf Z_p}
 =\bar\pi^{-1}[p/\bar\pi^2]_*\nu_p.} \tag{18}
$
等价地，R300 的原完整算子
$
 T_p=\bar\pi[\bar\pi^2]_*\psi_p,\qquad
 \psi_p\nu=(x\mapsto x/p)_*(\nu|_{p\mathbf Z_p})
$
满足
$
 \boxed{T_p\nu_p=\nu_p.} \tag{19}
$
所有非负整数矩一次给出单 Euler 式
$
 \boxed{\int_{\mathbf Z_p^\times}x^m\,d\nu_p
 =\left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)
   \Omega_p^m m!s_m,\qquad m\ge0.} \tag{20}
$
它包括全部 tame，而不只是首个原中央权。

迭代 (18)，对真实归一环带 $p^n\mathbf Z_p^\times$ 有
$
 \mathcal M_k^{[n]}(u)=
 \bar\pi^{-n}\omega_p(\bar\pi)^{-2nk}
 \langle\bar\pi\rangle^{-2nu}\mathcal M_k(u),\quad n\ge0.
 \tag{21}
$
因此其原导数保留
$
 \mathcal M_k^{[n]\prime}(0)=
 \bar\pi^{-n}\omega_p(\bar\pi)^{-2nk}
 \bigl(\mathcal M_k'(0)-2n\log_p\bar\pi\,\mathcal M_k(0)\bigr).
 \tag{22}
$
只有 principal 的质量由 (17) 为零；
其他 tame 的质量及尺度对数均不删除。

## 4. p=7 的原 CM trace 绝对标量

令
$
 \gamma=3+\omega=(5+\delta)/2,\qquad N\gamma=7,
$
选择 $\mathfrak p=(\gamma)$ 的普通嵌入。
直接数 $E_{24}(\mathbf F_7)$ 得十三个点，所以 $a_7=-5$。
范数七且迹负五的两个根是 $-\gamma,-\bar\gamma$；
在 $\mathfrak p$ 赋值一的原值准确为
$
 \boxed{\pi=\psi_{24}(\mathfrak p)=-\gamma.} \tag{23}
$

R300 §2 的完整根单位平均和真实 division 迹比较对任何偶 degree $N$
成立，不依赖旧 degree34 的单重本征线。应用于这里的 $N=72$，
在同一 sigma frame 中有
$
 T_7\Phi=\frac{\bar\pi}{7}\,\mathscr M_\pi\Phi,\qquad
 \mathscr M_a(\sigma^{72}f)=\sigma^{72}
 \operatorname{Tr}_{[a]}
 \left[\left(\frac{r_{\bar a}}{r_a}\right)^{72}
 f\circ[\bar a]\right],
 \quad r_a=\sigma(az)/\sigma(z)^{Na}.
 \tag{24}
$
原完整测度已整，公式中的 $1/7$ 由整个平均承担；
这里没有假设首项归一后仍在七处整。

(19)、(23)、(24) 给
$\mathscr M_\pi\Phi=\pi\Phi$。
因 $72$ 偶且 $\Phi$ 偶，原 trace 满足
$\mathscr M_{-\gamma}\Phi=\mathscr M_\gamma\Phi$，所以
$
 \boxed{\mathscr M_\gamma\Phi=-\gamma\Phi.} \tag{25}
$
这个绝对标量由同一原 Schwartz 平方和整测度恢复，
没有从有限域样本猜测相位。
它在固定 CM homothety 下不变，可用于共同 $E_b$ frame 的准确
CM7 矩阵识别。

$p=7$ 的这一步不需要 R397 的全 Selmer 部分。
事实上 R397 在七处的主猜想假设也没有障碍：
ray 次数为 432，辅助因子中心 $-30$ 也是七单位；
但本篇只用已付的真实 Katz 插值、原质量和有界测度。

## 5. 后续接口与适用边界

R395 把实际来源放入
$
 \Phi=\sigma^{72}XQ_4(X)R_6(X),\qquad \deg R_6\le6.
$
式 (25) 现在给该同一七维候选空间中的原 CM7 方程及准确本征值。
仍须用真实有限迹或代数恒等式解出其指定线；
本篇没有从“某个向量满足同一本征值”预付唯一性。

(18) 同时可接 R376 的真实 theta 群球公式；
仍须保对应 degree72 frame、全部原周期和各个非 principal 质量。
全 core 和整个来源 primitive 不单独推出原中央导数非零。
主问题仍要求 R397 的有限证书在无穷多个不同素数命中，
或若干已经证明秩至少二的固定曲线之完整中央行在同一无限集合上联合非零。

## 依赖与出处

- [R395](R395-e24-six-actual-translates-fixed-divisor-and-square-normalization.md)：
  实际六项来源、所有好 $p>3$ 的原整性和真实复平方。
- [R397](R397-e24-original-ordinary-square-and-full-selmer-bridge.md)：
  原周期与阶乘、Katz 插值、反圆权参数；本篇将其同一极限逐个 tame 书写。
- [R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md) §2：
  偶 degree 的原完整根单位平均、division 迹及正式群比较。
- Katz 的已发表有限导子插值：
  A. Agboola、B. Howard，*Anticyclotomic Iwasawa theory of CM elliptic curves*，
  Ann. Inst. Fourier **56** (2006)，Theorem 2.1.1，
  [出版全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)；
  详细晶格周期见 F. Castella、X. Wan，*Perrin-Riou's main conjecture
  for elliptic curves at supersingular primes*，Math. Ann. **389** (2024)，
  Remark 2.2、Theorem 2.4，
  [出版全文](https://web.math.ucsb.edu/~castella/Perrin-Riou-print.pdf)。
- §1 的全测度平方刚性为本文直接证明；只用有界性、等差权列、
  多项式稠密和实际有限纤维，不使用额外未证的非消失或 Selmer 假设。

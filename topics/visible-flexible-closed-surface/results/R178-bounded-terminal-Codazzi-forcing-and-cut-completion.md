# R178 — 准确退化末切口的全角有界 Codazzi forcing 与后验补齐

本结果补齐 R173 完整消费者在退化 cut 上不能直接返回的第一阶 forcing 积分。它适用于 R172 的准确末格和 R170 原 $P\le6/5$ 尾域，与 R174 的可积角二阶估计互补。结论只用准确物理相位、保存的有限系数和全角不等式，不求新的 BVP、F/J 或 body，不给 cut 的径向 II 导数强行赋值。

## 1. 准确对象与结论

设准确物理端点为 $S$，保存末格左端为 $b$，保存数值标签为 $E$。写

$$
 \ell=S-b>0,\qquad \tau=S-s,\qquad
 \sigma(s)=b+(E-b)\frac{s-b}{S-b}.
\tag{1}
$$

整个末格满足 R172 的保护条件：材料角就是计算角 $u=\xi$，seed/coast/bump 均为零，R155 权恒为 1。背景二阶形式为

$$
 B(s,u)=\frac{\tau}{\ell}C_0(u)
           +\eta(s)T(a(s),u),
 \quad \eta(s)=S_5\!\left(\frac{\sigma(s)-c_w}{L_w}\right).
\tag{2}
$$

其中 $C_0=(C_n,C_m,C_l)$ 是实际保存的最后左行完整 Fourier 多项式，$c_w+L_w=E$ 作为准确有理恒等式核对，$0<E-b<L_w$，且 $S_5(z)=10z^3-15z^4+6z^5$。尾为

$$
 T(a,u)=\kappa(a\sin u)(\cos^2u,-\sin u\cos u,\sin^2u).
\tag{3}
$$

这里 $a,K$ 始终按物理 $s$ 求值，不能换成 $a(\sigma),K(\sigma)$。尾的准确几何常数是 $a_c=4/5,\ c=17/50,\ w=23/50$，实际16控制属于 R170 的八段局部 Bernstein 盒。

令

$$
 d=B_n-B_l,\quad r=(d,2B_m),\quad
 h=\sqrt{|r|^2+4K},\qquad
 (n,m,l)=\left(\frac{h+d}{2},B_m,\frac{h-d}{2}\right).
\tag{4}
$$

则 $G=nl-m^2-K=0$ 是准确代数恒等式。对严格内部定义

$$
 R_n=n_s-\frac{m_u}{a}-\frac{a_s}{a}(l-n),\qquad
 R_m=m_s-\frac{l_u}{a}+2\frac{a_s}{a}m,\qquad
 H=(-aR_n,aR_m,-aG).
\tag{5}
$$

**结论。** 从准确有限输入可计算非负有理常数 $H_0,H_{1/2},H_1,H_2$，在整个角圆及所有实际 $0<\tau\le\tau_0$ 上有

$$
 \|H(s,u)\|_2
 \le H_0+H_{1/2}\sqrt{\tau}+H_1\tau+H_2\tau^2.
\tag{6}
$$

允许 $\tau_0$ 取准确 $\ell$ 的有理上界；此时只消费与实际末格相交的部分。特别是任何长度不超过 $\varepsilon\le\tau_0$ 的真实末端子区间满足

$$
 \begin{aligned}
 I(\varepsilon)&:=
 \int_{\max(b,S-\varepsilon)}^{S}\|H\|\,ds\\
 &\le H_0\varepsilon+\frac23H_{1/2}\varepsilon^{3/2}
                  +\frac12H_1\varepsilon^2+\frac13H_2\varepsilon^3,\\
 J(\varepsilon)&:=
 \int_{\max(b,S-\varepsilon)}^{S}(S-s)\|H\|\,ds\\
 &\le\frac12H_0\varepsilon^2+\frac25H_{1/2}\varepsilon^{5/2}
                  +\frac13H_1\varepsilon^3+\frac14H_2\varepsilon^4.
 \end{aligned}
\tag{7}
$$

若实际区间更短，右侧仍为有效单调上界。以下给出全部常数和证明，不把有限点检查用作连续论证。

## 2. 准确物理相位给出的 $K_s$ 界

R174 已由当前准确三次 phase bridge 证明：设 $L_\phi$ 为准确段长，起相位为 $p_0$，

$$
 \Delta=p_0+\pi/2>0,\quad
 \theta(\tau)=\Delta(\tau/L_\phi)^2(3-2\tau/L_\phi),
 \quad a_s=-\cos\theta.
\tag{8}
$$

取准确有理 $\Delta_-\le\Delta\le\Delta_+$，要求
$\tau_0/L_\phi\le1/2,\ 3\Delta_+(\tau_0/L_\phi)^2\le1$。于是
$a_c\le a(s)\le a_c+\tau_0=:a_*$、$|a_s|\le1$。记

$$
 A(\tau)=\theta_\tau
 =\frac{6\Delta\tau}{L_\phi^2}(1-\tau/L_\phi),
 \qquad K=\frac{A\sin\theta}{a}.
\tag{9}
$$

R174 的准确常数 $k_-,k_+$ 满足

$$
 0<k_-\tau^3\le K(s)\le k_+\tau^3.
\tag{10}
$$

为明确支付所需的物理 $K_s$，对 (9) 关于 $\tau$ 求导：

$$
 K_\tau
 =\frac{A_\tau\sin\theta+A^2\cos\theta}{a}
       -\frac{A\sin\theta\,a_\tau}{a^2},
 \qquad K_s=-K_\tau.
\tag{11}
$$

在该区间，

$$
 |A_\tau|\le\frac{6\Delta_+}{L_\phi^2},\quad
 A\le\frac{6\Delta_+\tau}{L_\phi^2},\quad
 \sin\theta\le\theta\le\frac{3\Delta_+\tau^2}{L_\phi^2},
 \quad |a_\tau|\le1.
$$

代入 (11) 得

$$
 |K_s|\le k_{s,2}\tau^2,\qquad
 k_{s,2}=
 \frac{54\Delta_+^2}{L_\phi^4a_c}
 +\frac{18\Delta_+^2\tau_0}{L_\phi^4a_c^2}.
\tag{12}
$$

因此

$$
 \frac{|K_s|}{\sqrt K}
 \le C_K\sqrt\tau,\qquad C_K=\frac{k_{s,2}}{\sqrt{k_-}}.
\tag{13}
$$

程序使用 $\sqrt{k_-}$ 的严格有理下界计算 $C_K$ 的有理上界。这里的高阶标量公式只来自已声明的准确末 phase 多项式；没有对完整未知曲面新增全局 $C^3$ 假设，没有用数值插值导数替代准确相位导数。

## 3. 完整 raw 和尾的全角常数

设

$$
 \rho(s,u)=\frac{\tau}{\ell}(C_n-C_l,2C_m),\qquad
 e(u)=(\cos2u,-\sin2u),\qquad
 r=\rho+\eta\kappa(a\sin u)e.
\tag{14}
$$

由实际有限 Fourier 系数，在取绝对值前准确相减 $C_n-C_l$，用 R174 的系数绝对和得到有理 $B_0,B_1$，使

$$
 |\rho|\le B_0\tau,\qquad
 |\rho_s|\le B_0,\qquad
 |\rho_u|\le B_1\tau.
\tag{15}
$$

因此这个界保留 terminal raw trace gauge 的准确相消，不会把相同的 raw $n,l$ 大项分别估计后丢掉其差。

R170 的准确八段控制和 R174 的 degree-23 Bernstein 乘积/求导规则给出整个实轴上的

$$
 0\le\kappa\le Q_0,\qquad |\kappa_y|\le Q_1.
\tag{16}
$$

由于 $q^4(1-q)^4$ 的端点零阶和固定 collar，(16) 包括与零支的接口。允许全局 Bernstein 系数为负，实际非负性来自准确局部系数证书。本版明确核 $P\le6/5$，绝不把原 $Q_0\le4725/736$ 自动转给以后可能扩大的域。

取准确 $\ell_->0$ 满足 $\ell_-\le\ell$，令
$q_*=(E-b)/(\ell_-L_w)$。由 $S_5(1-z)=1-S_5(z)$，(2) 写为

$$
 \eta(s)=1-S_5(q_{\rm exact}\tau),
 \qquad q_{\rm exact}=\frac{E-b}{\ell L_w}\le q_*.
\tag{17}
$$

实际 $0\le q_{\rm exact}\tau\le(E-b)/L_w<1$，故

$$
 0\le\eta\le1,\qquad
 0\le\eta_s
 =30q_{\rm exact}^3\tau^2(1-q_{\rm exact}\tau)^2
 \le30q_*^3\tau^2.
\tag{18}
$$

利用 $|e|=1,\ |e_u|=2,\ |a_s|\le1,\ a\le a_*$，得到

$$
 \begin{aligned}
 |r|&\le Q_0+B_0\tau,\\
 |r_s|&\le B_0+Q_1+30q_*^3Q_0\tau^2
                =:S_0+S_2\tau^2,\\
 |r_u|&\le a_*Q_1+2Q_0+B_1\tau
                =:U_0+B_1\tau.
 \end{aligned}
\tag{19}
$$

这些是全部材料角上的界。R172 已逐定义核整末格 atlas 为恒等映射，当前区域恰有 $U_s=0,U_\xi=1$；区域外的 R173 消费者仍保留完整 $U_s/U_\xi$ 项。

## 4. 不在 cut 除零的正 trace 一阶估计

严格内部由 (10) 有 $h>0$。微分 (4) 得

$$
 h_u=\frac{r\cdot r_u}{h},\qquad
 h_s=\frac{r\cdot r_s+2K_s}{h}.
$$

注意 $|r|\le h$ 且 $h\ge2\sqrt K$。Cauchy–Schwarz 和 (13) 给出

$$
 |h_u|\le |r_u|,\qquad
 |h_s|\le |r_s|+\frac{|K_s|}{\sqrt K}
          \le S_0+S_2\tau^2+C_K\sqrt\tau.
\tag{20}
$$

这是直接点盒 $1/h$ 失去精度时可用的统一估计。它没有除以未知 $n$，没有使用错误的 $h\ge\kappa$，并包括 raw 与尾方向相消的位置。式 (20) 在开末格成立，上界有有限 cut 极限；并未因此给 $h_s$ 或 $II_s$ 在 cut 定义共同值。

从 (4)、(19)、(20) 得

$$
 \begin{aligned}
 |n_s|&\le S_0+S_2\tau^2+\tfrac12C_K\sqrt\tau,\\
 |m_s|&\le\tfrac12(S_0+S_2\tau^2),\\
 |m_u|&\le\tfrac12(U_0+B_1\tau),\\
 |l_u|&\le U_0+B_1\tau,\\
 |l-n|&\le Q_0+B_0\tau,\qquad
 |2m|\le Q_0+B_0\tau.
 \end{aligned}
\tag{21}
$$

尾上的零曲率弧不需要额外正 $n$ 条件。

## 5. 三条实际缺陷与显式 forcing 常数

由 (4) 直接算出

$$
 nl-m^2-K
 =\frac{h^2-d^2}{4}-m^2-K=0.
\tag{22}
$$

这是精确相消，不能把自然区间重复出现同一变量所生的包围宽当成真实 Gauss 误差。

将 (21) 代入 (5)，并用 $a\ge a_c,\ |a_s/a|\le1/a_c$，得到

$$
 \begin{aligned}
 |R_n|&\le N_0+N_{1/2}\sqrt\tau+N_1\tau+N_2\tau^2,\\
 N_0&=S_0+\frac{U_0}{2a_c}+\frac{Q_0}{a_c},&
 N_{1/2}&=\frac{C_K}{2},\\
 N_1&=\frac{B_1/2+B_0}{a_c},&N_2&=S_2,\\
 |R_m|&\le M_0+M_1\tau+M_2\tau^2,\\
 M_0&=\frac{S_0}{2}+\frac{U_0}{a_c}+\frac{Q_0}{a_c},&
 M_1&=\frac{B_1+B_0}{a_c},\qquad M_2=\frac{S_2}{2}.
 \end{aligned}
\tag{23}
$$

因为 $G=0$，有 $\|H\|_2\le a_*(|R_n|+|R_m|)$。因此 (6) 可取

$$
 \begin{aligned}
 H_0&=a_*(N_0+M_0),& H_{1/2}&=a_*N_{1/2},\\
 H_1&=a_*(N_1+M_1),& H_2&=a_*(N_2+M_2).
 \end{aligned}
\tag{24}
$$

全部常数由准确有限系数、有理 phase 常数及严格平方根端点组成。逐项积分得 (7)，完成全角连续结论的证明。

## 6. 对 R119/R125 的准确末端接续

给定真实固定材料角 frame/位置重建，在末端起点有已支付的算子误差和位置误差界
$\|D\|\le d_{\rm in},\ |C|\le c_{\rm in}$。R119 的 skew 能量式与 $C_s=D e_1$ 给出

$$
 \|D(S)\|\le d_{\rm in}+I(\varepsilon),\qquad
 \sup_{\rm terminal}|C|
 \le c_{\rm in}+\varepsilon d_{\rm in}+J(\varepsilon).
\tag{25}
$$

第二式的权来自交换三角积分：
$\int_{s_0}^S\int_{s_0}^s\|H(r)\|\,dr\,ds
=\int_{s_0}^S(S-r)\|H(r)\|\,dr$。

取 $\eta_*=(c_{\rm in}+\varepsilon d_{\rm in}+J(\varepsilon))/a_c$，R119 的该段相对 metric 上界为 $2\eta_*+\eta_*^2$。这只是条件接续：没有替前段提供 $d_{\rm in},c_{\rm in}$，没有构造或检查完整接缝与 reach。

在 R125 的语言中，可在最后剩余小区间选 $P=q=0$，精确剩余为 $H$，而 (7) 直接支付。此前各格的零端 primitive 和移动图项无需改变。过程不在 cut 点调用 $1/h$，也不要求 $II_{uu}$ 在 cut 一致有界。R174 另付真正 body 角两 jet 极限；R126 仍须消费实际两片的结果。

## 7. 实现和真实输入结果

纯常数消费者为 [fd2d_gc_terminal_forcing_majorant.py](../scripts/fd2d_gc_terminal_forcing_majorant.py)，主要 API：

- terminal_forcing_majorant：输入显式准确末格对象，返回 (12)–(24) 的准确有理上界；
- terminal_forcing_integrals：返回 (7) 和当前终端子区间的 sup；
- complete_R119_terminal：只在 caller 提供真实 $d_{\rm in},c_{\rm in}$ 后作 (25) 的代数接续。

它重新核原 $6/5$ 域证书、准确末 phase、保存 raw 末行和真实物理 $\ell$。source SHA256 为 a27e2d02d89cec782e3a40938fb6824542ccef7d6e478b5395b09869b219295d。

本次绑定是 dyadic30 场 3bceef937899fad65e512e56d3bd747a6d225b20301b64ed9d04582a4f6db981 和准确 profile packet a6215af63b98cc8409faf9dbb46c039f86c1ef9e9bc6fedacdd62514ba3dcb5a。实际执行块 fba2ec 真实 exit 0；内部耗时 0.12913172200205736 秒，峰 RSS 84812 KiB。没有会话长任务或新求解。

[报告](../notes/2026-11-12-fd2d-metric-dyadic30-terminal-forcing-R178-01-report.json) 与 [准确常数包](../notes/2026-11-12-fd2d-metric-dyadic30-terminal-forcing-R178-01-majorant.json.gz) 给出 $\tau_0$ 的严格上界约 0.001625000000001175，及显示值

$$
 (H_0,H_{1/2},H_1,H_2)
 \approx(2440.91723868,\ 1077.08884387,\ 23353.05707043,\ 18.58060118).
$$

所有正式端点保存为准确有理数；这些小数不是定义。一次必要实现对照在三种严格内部径向标签、三个角度上比较原完整区间 $H,K_s$ 与本结论，九点全部落在已证明的解析界内。连续证明不依赖这九点。

下表的显示小数来自准确有理上界：

| 末端长度上界 $\varepsilon$ | $I(\varepsilon)$ | $J(\varepsilon)$ |
| --- | ---: | ---: |
| 整准确末格的严格长度上界 | 4.04436094861 | 0.003302037501 |
| $2^{-20}$ | 0.002328519444 | $1.110390059\cdot10^{-9}$ |
| $2^{-30}$ | $2.273301746\cdot10^{-6}$ | $1.058590520\cdot10^{-15}$ |
| $2^{-40}$ | $2.220001919\cdot10^{-9}$ | $1.009540049\cdot10^{-21}$ |
| $2^{-50}$ | $2.167970035\cdot10^{-12}$ | $9.627721014\cdot10^{-28}$ |

整格粗界明显很大，不能据此宣称该候选已满足完整 metric 目标。其用途是在前面真实盒/primitive 已消费到某个准确内部 cut-off 后，用任意所需小的剩余长度补齐准确 $S$，并保留明确误差贡献。

## 8. 重做和仍未付项

在本课题目录使用未存在的新输出 stem：

~~~sh
PYTHONPATH=/workspace/scratch/fd2d-recovered-deps/python-flint-0.9.0 \
python scripts/fd2d-metric-terminal-forcing-check.py \
  --field notes/2026-11-12-fd2d-raw-bump-dyadic30-trial-back01-a01-accepted.npz \
  --profile-packet notes/2026-11-12-fd2d-metric-dyadic30-accurate-profile-rebind-02-packet.json.gz \
  --out-prefix notes/2026-11-12-fd2d-metric-dyadic30-terminal-forcing-R178-replay
~~~

本结果支付准确 cut-touch 的全角 forcing 上界与积分，不支付前面未完成场的全域 $H-P$、初始之后累计的实际 $D,C$、完整闭合、曲率/reach 或终极完成标准。它没有把有限求解器当前 residual 变成连续证书，也没有要求不存在的 cut 径向 II 导数。


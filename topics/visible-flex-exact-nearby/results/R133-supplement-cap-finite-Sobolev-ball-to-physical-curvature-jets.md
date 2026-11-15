# R133：有限 Sobolev 帽球到真实物理角的完整曲率 jets

2026-11-15，visible-exact-astra-0df9。

**本篇证明一个有限正则输入门。** 在已付完整实族
$|\delta|\le10^{-8}$ 的准确外端 $R=25/8$，令
$\widehat Y=\mathcal H z$，其中 $\mathcal H=(D\Psi_0)^{-1}$
是原固定物理角的完整微分逆。若
$$
 \|z\|_{\mathfrak M_{8212}}\le2^{-8388608},
 \qquad Q=Q_\delta+Y ,
 \tag{F.1}
$$
则 $Q$ 的真实物理角 $\theta=\Theta_Q(R,\varphi)$ 存在，且实际
nonmean 曲率输入 $\mathcal Z_Q=(C_Q-C_{\rm ref})_\perp$ 满足
$$
 \|\partial_\theta^q\mathcal Z_Q\|_{A_0(\theta)}
       <q!\,128^q\,2^{-36},\qquad 0\le q\le8192 .
 \tag{F.2}
$$
未知 $Y$ 可以有无限 Fourier 支持，且只假设 (F.1) 的有限正则性。
证明只沿真实角变换作有限链式法则，不给 $Y$ 作复角延拓。
完整 moving mean、相位 primitive 的常数和两个 physical curvature
mean 均保留。

本篇仅给真实 long 方程所需的曲率数据域；不宣称已构造附近 long
解、非线性匹配、全频逆或最终闭等距族。没有新数值运行。

## 1. 原输入的准确身份与范数

使用
[完整帽主体有限 Sobolev 球](R133-supplement-finite-Sobolev-nearby-cap-body-inverse-and-same-space-remainder.md)
C.1、C.7、C.10、C.19。该文件 SHA256 为
$730ffff4e641615aafdafdda12bb3b147bf227a6c4386b9d4165a7efb4ab7699$。
背景及完整方向仍为连续修补中心
$440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47$
和方向
$6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04$；
固定 $\eta_0$，整个帽上的原 $\nu$ bump 为零。

记 $x=\theta_0$ 为原固定物理角，$\varphi=\Phi_0(R,x)$。
帽号仅表示与这个已知 $\Phi_0$ 复合。所有圆周测度均归一化；
$A_0$ 是完整 signed Fourier $\ell^1$ 范数，$H^s$ 使用
$\langle n\rangle^s$、$n\in4\mathbb Z$。pair 范数为两分量范数之和。
原 $\mathfrak M_s$ 先取每个 Fourier 系数的径向 supremum，再求
加权平方和，故它确实支配同角中 $R$ 端的 $H^s$ 范数。

由 C.10 定义
$$
 Y_*:=2^{425987}\|z\|_{\mathfrak M_{8212}},
 \qquad
 2\|\widehat Y(R)\|_{H^{8196},{\rm pair}}\le Y_*,
 \qquad Y_*\le2^{-7962621}.
 \tag{F.3}
$$
完整 Fourier Cauchy--Schwarz 给
$$
 \|\partial_x^k\widehat Y(R)\|_{A_0,{\rm pair}}
 \le2\|\widehat Y(R)\|_{H^{k+1},{\rm pair}}
 \le Y_*,\qquad 0\le k\le8195 .
 \tag{F.4}
$$
这里没有把 $\sup_r\sum_n$ 与 $\sum_n\sup_r$ 交换，也未删除 even mean。

令 $\omega_0=\partial_x\Phi_0(R,x)$。
[固定基点保守源](R133-supplement-fixed-base-conservative-source-transport-and-nearby-cap-linearization.md)
P.8--P.10 给
$$
 \Pi_0 f=\langle\omega_0 f\rangle_x,\qquad
 \mathcal I_0\widehat f=\widehat{I_\varphi f},\qquad
 \|\Pi_0\|_{A_0\to\mathbb C}<2,\quad
 \|\mathcal I_0\|_{A_0\to A_0}<2 .
 \tag{F.5}
$$
$\mathcal I_0$ 保留原 moving-zero-mean primitive 的准确常数，
不是裸 $I_x$。

以下已知背景的正宽界来自
[完整实族固定角外图](R133-supplement-full-delta-fixed-angle-regular-graph-analytic-translation.md)
T.1--T.6、T.24：
$$
 5.8<|m_\delta|<8,\quad m_\delta<0,\quad
 \|\widehat v_\delta-m_\delta\|_{A_{1/128}}<2^{-25},
 \quad \|\widehat v_\delta\|_{A_{1/128}}<16,
$$
$$
 \|j_\delta-1\|_{A_{1/128}}<2^{-26},
 \qquad j_\delta=\omega_0\widehat v_\delta/m_\delta,
 \qquad \|\mathcal Z_\delta\|_{A_{1/128}(\theta_\delta)}
                                  <2\cdot10^{-12}<2^{-38}.
 \tag{F.6}
$$
最后一项是完整 joint norm：原两侧平移界相加，连同真实 full-$\delta$
曲率变化；不以单侧平移范数代替完整 Fourier 和。

还需已知 $\omega_0$ 的同宽界。T.1 所引原 S.20 endpoint 门为
$\|w_0\|_{A_{1/8}}<10^{-8}$，
$w_0=(v_0-m_0)/m_0$，以及
$\|\Phi_0(R)-{\rm id}\|_{A_{1/64}}<1.5\cdot10^{-11}$。
已知解析复合仍在 $1/8$ 域内，由
$\omega_0=(1+w_0\circ\Phi_0)^{-1}$ 的 Neumann 级数得
$$
                 \|\omega_0\|_{A_{1/128}}<2 .
 \tag{F.7}
$$
这是准确端点的已知系数结论，不是由 P.10 的零宽门推导未知正宽。

## 2. 整个真实线段的相位、signed mean 与正 Jacobian

用 $a\in[0,1]$ 表示状态线段参数，避免与 long 的径向坐标混同：
$$
 \widehat Q_a=\widehat Q_\delta+a\widehat Y,\quad
 v_a=\widehat v_\delta+a\widehat Y_2,\quad
 m_a=\Pi_0v_a=m_\delta+a\dot m,\quad
 \dot m=\Pi_0\widehat Y_2 .
 \tag{F.8}
$$
从 F.3--F.7，$m_a<0$、$|m_a|>3$、$|\dot m|<2Y_*$，
且 $\|v_a-m_a\|_{A_0}<1/4$。
原 normalized angle 的完整定义给
$$
 \tau_a(x)=\Theta_{Q_a}(R,\Phi_0(R,x)),\quad
 j_a=(\tau_a)_x=\omega_0v_a/m_a,\quad
 \eta_a=\partial_a\tau_a
 =\mathcal I_0\!\left(\frac{\widehat Y_2}{m_a}
                         -\frac{v_a\dot m}{m_a^2}\right).
 \tag{F.9}
$$
尤其
$$
 \Pi_0\eta_a=0,\quad
 (\eta_a)_x=\omega_0
       \left(\frac{\widehat Y_2}{m_a}
                         -\frac{v_a\dot m}{m_a^2}\right),
 \qquad \langle j_a\rangle_x=1 .
 \tag{F.10}
$$
式中 primitive 输入的 $\Pi_0$ 恰为零。
这同时确定真实相位常数，而不是任取一个 $x$-mean-zero 相位。

由 $j_a-j_\delta=
\omega_0\{a\widehat Y_2/m_a
-a\widehat v_\delta\dot m/(m_am_\delta)\}$ 及 F.3、F.6，
$$
 \|j_a-1\|_{A_0}<1/4,\qquad
            \tfrac12<j_a(x)<2 .
 \tag{F.11}
$$
因此每个 $\tau_a$ 都是同向、degree-one 的真实圆周坐标，
并保留四重周期。$m_a$ 的负号在所有恒等式中原样保留；
只在范数上界中使用 $|m_a|$。

## 3. 只到所需有限阶的 reciprocal 与 phase jets

对任意 $f$ 写 $f^{[k]}=\partial_x^kf/k!$。
本节只取 $k\le8194$，不是关于未知函数的无穷 Taylor 展开。
F.4、F.6--F.7 给
$$
 \|v_a^{[k]}\|_{A_0}\le32\,128^k,\qquad
 \|j_a^{[k]}\|_{A_0}\le64\,256^k .
 \tag{F.12}
$$
第二式用 $j_a=\omega_0v_a/m_a$、
$|m_a|^{-1}<1$ 及 $k+1\le2^k$（$k=0$ 取等号）。

Neumann 级数仅在零阶 $A_0$ 中使用：
$\|v_a^{-1}\|_{A_0}<2$、$\|j_a^{-1}\|_{A_0}<2$。
之后每一有限阶都用准确乘积导数恒等式
$$
 (f^{-1})^{[k]}
 =-(f^{-1})^{[0]}\sum_{i=1}^k f^{[i]}(f^{-1})^{[k-i]},
 \qquad k\ge1 .
 \tag{F.13}
$$
若 $\|f^{[i]}\|\le M D^i$ 且 $\|f^{-1}\|\le2$，这项归纳给
$\|(f^{-1})^{[k]}\|\le2\{(1+2M)D\}^k$：
将归纳上界代回 F.13 后使用有限几何和。
取 $(M,D)=(32,128)$ 与 $(64,256)$，得到
$$
 \|(v_a^{-1})^{[k]}\|_{A_0}\le2\,2^{14k},\qquad
 \|(j_a^{-1})^{[k]}\|_{A_0}\le2\,2^{16k}.
 \tag{F.14}
$$
实际乘子分别为 $65\cdot128<2^{14}$、
$129\cdot256<2^{16}$；没有未知复角求值。

F.9 的括号的 normalized $k$-jet 小于
$8Y_*128^k$。乘 F.7 后，
$(\eta_a)_x$ 的 normalized $k$-jet 至多为
$16Y_*(k+1)128^k\le16Y_*256^k$。
零阶 $\eta_a$ 另由 F.5 支付；正阶由 F.10 积分恒等式读取。
因此
$$
 \|\eta_a^{[k]}\|_{A_0}\le16Y_*256^k,\qquad
 \|(v_{a,x})^{[k]}\|_{A_0}\le2^{12}256^k .
 \tag{F.15}
$$
后一式来自
$(v_{a,x})^{[k]}=(k+1)v_a^{[k+1]}$，
故使用它时只允许 $k+1\le8194$。

## 4. 真实固定物理角的曲率差

准确 physical 曲率为
$$
 C_a(\theta)=v_a^{-1}(\tau_a^{-1}(\theta)).
$$
在固定 $\theta$ 微分，而不是固定 $x$ 微分，得到
$$
 \partial_a C_a=F_a\circ\tau_a^{-1},\qquad
 F_a=-v_a^{-2}\widehat Y_2
       +j_a^{-1}v_a^{-2}v_{a,x}\eta_a .
 \tag{F.16}
$$
第二项的正号来自 $(v_a^{-1})_x=-v_a^{-2}v_{a,x}$。
这正是完整 moving differential 的 good-curvature 分量；
若省去它就会丢掉真实角变化及其 mean 规范。

F.4、F.14--F.15 按 normalized jets 相乘。
第二项含五个因子 $j_a^{-1},v_a^{-1},v_a^{-1},v_{a,x},\eta_a$；
常数积为 $2^{19}Y_*$。
其弱分拆数 $\binom{k+4}{4}\le5^k$。
第一项的三个因子另完整相加。因此
$$
 \|\partial_x^kF_a\|_{A_0}
       \le2^{20}Y_*\,k!\,2^{19k},
                \qquad 0\le k\le8193 .
 \tag{F.17}
$$
系数和、全部误差以及零频都先在同一 $A_0$ Banach 代数中支付。

记 $D_a=j_a^{-1}\partial_x$。真实链式恒等式为
$$
 \partial_\theta^q(F_a\circ\tau_a^{-1})
                     =(D_a^qF_a)\circ\tau_a^{-1}.
 \tag{F.18}
$$
为明确有限阶组合费用，将 $(b\partial_x)^rF$ 完全展开。
每项有 $r$ 个 $b$ 因子，全部导数阶数之和为 $r$。
所有 Leibniz 系数非负，其总和恰为 $r!$：
代入 $b=F=e^x$ 后，
$(e^x\partial_x)^r e^x=r!e^{(r+1)x}$，且每个展开项有同一指数。
每项导数阶乘的乘积又不超过 $r!$。
F.14、F.17 遂给
$$
 \|D_a^rF_a\|_{A_0(x)}
      \le2^{20}Y_*\,2^{20r}(r!)^2,\qquad 0\le r\le8193 .
 \tag{F.19}
$$
这里只展开已经存在的有限导数；没有从有限 jet 上界推出角解析性。

## 5. 在实际物理测度中读取完整 Wiener jets

对于完整四重周期 Fourier 级数，
$\|g\|_{A_0(\theta)}\le2\|g\|_{H^1(\theta)}$。
真实换测度为 $d\theta=j_a(x)\,dx$；由 F.11，
$$
 \|\partial_\theta^q(F_a\circ\tau_a^{-1})\|_{A_0(\theta)}
 \le8\max_{r=q,q+1}\|D_a^rF_a\|_{A_0(x)} .
 \tag{F.20}
$$
这个读出保留归一圆周测度和独立 mean；没有将 $A_0$ 在任意
有限正则复合下的有界性当作免费输入。

当 $q\le8192$ 时，只需 $r\le8193<2^{14}$，于是
$r!\le2^{14r}$。由 F.3、F.19--F.20，
$$
 \|\partial_\theta^q\partial_a C_a\|_{A_0(\theta)}
 \le2^{425987+23+48\cdot8193}\|z\|_{\mathfrak M_{8212}}
 =2^{819274}\|z\|_{\mathfrak M_{8212}}
 <2^{1048576}\|z\|_{\mathfrak M_{8212}} .
 \tag{F.21}
$$
式中两端的 $\theta$ 是同一个数值圆周坐标；只有准确 inverse
$\tau_a^{-1}$ 随 $a$ 变化。因而可以在固定 $\theta$ 上沿真实
$a\in[0,1]$ 积分，得到
$$
 \max_{0\le q\le8192}
 \|\partial_\theta^q(C_Q-C_\delta)\|_{A_0(\theta)}
 <2^{1048576}\|z\|_{\mathfrak M_{8212}}
 \le2^{-7340032}.
 \tag{F.22}
$$
若后续统一账本采用 $2^{3145728}$ 的较宽常数，同一结论当然成立；
不需要为该宽放重新计算任何数据。

有限 buffer 的使用顺序是：F.20 多读一个物理导数，
F.16 中的 $v_x$ 再用一个 $x$ 导数，而 F.4 的 Sobolev-to-Wiener
读出再用一个导数。对 $q\le8192$，最高只需 $H^{8195}$；
F.3 使用 $H^{8196}$，故仍保留余量。
标准有限 Sobolev 乘法、逆函数及真实复合的光滑逼近，可将先对
光滑状态写出的恒等式延拓至 F.1 球；全部低阶 gap 一致为正。
这里不以光滑逼近假设未知状态解析。

## 6. nonmean 数据门与两个未删除的真实 mean

$C_{\rm ref}$ 为原径向参考，且 physical $P_\perp$ 在 $A_0$ 中收缩。
在完成 F.22 后才投影，结合 F.6 可得
$$
 \begin{split}
 \|\partial_\theta^q\mathcal Z_Q\|_{A_0}
 &\le q!\,128^q\,2^{-38}+2^{-7340032}\\
 &<q!\,128^q\,2^{-37}
  <q!\,128^q\,2^{-36},
                 \qquad 0\le q\le8192 .
 \end{split}
 \tag{F.23}
$$
特别这给出 root 所需的有限 translation-jet 输入球，
没有用无限阶或未知正宽范数代替它。

nonmean 投影不删除原完整匹配的两条 mean。准确换测度给
$$
 \langle C_Q\rangle_\theta=\frac1{m_Q},\qquad
 \langle B_Q\rangle_\theta=\frac{\overline u_Q}{m_Q},
 \quad
 m_Q=\Pi_0\widehat v_Q,\quad
 \overline u_Q=\Pi_0\widehat u_Q .
 \tag{F.24}
$$
其沿线段的变化是
$-\dot m/m_a^2$ 和
$\Pi_0\widehat Y_1/m_a-\overline u_a\dot m/m_a^2$，
继续作为真实 scalar 数据保留。
反射类中的 $B$ mean 若由原奇性准确为零，也只在该子空间作此读取。
F.23 本身对完整四重周期状态成立，未借奇性消去相位或 mean。

该证明只从已有 C 球与原真实 endpoint 证书推出有限 physical
curvature jets。外高度的 $\dot A^2$ 数据、附近真实 long 图、
weak conormal DN、其 independent affine sources 和最终 nonlinear
匹配仍须各自按原单位支付。

# R133：真实正帽在 r=3/2 的完整 q 向量及无限频率边界预算

**已证明（真实线性帽的有向数值包络，以及已证非线性帽的消费合同）。**
在同一真实目标度量的 $L=3/2\le r\le R=25/8$ 上，脚本实际完成了
全部 $m=4,8,\ldots,1024$ 的真实 regular 比值 $q_m(L)$ 包络。每个频率均经过
原证书的全部663个闭径向盒；原始无限 primitive、整个仿射参数区间和真正 R74
regular 尾误差全部保留。其余所有 $m\in4\mathbb N$ 另有统一严格界

$$0<q_m(L)<1.059751810294<\frac{53}{50}.
\tag{Q.1}$$

浮点向量同时给出，供完整有限主体选择近似 Robin 行；浮点值与真实 $q_m$ 的
逐模差额在同一接口中明确付费。本篇不把有限主体升级为 PDE 解，也不把真正
非线性帽的另一迹或 mean 清零。

## 1. 目标、方向及真正 regular 入口

沿用[原真实旋转正帽](R133-actual-rotational-positive-cap-and-Codazzi-Jacobi-graph.md)
及[完整径向解析筛选](R133-supplement-true-cap-radial-decay-and-growing-analytic-width.md)
的记号：

$$
g=E(r)\,dr^2+a(r)^2\,d\theta^2,\quad
\gamma=\frac{\sqrt E}{a}>0,\quad \beta=\frac{a'}a,
\quad C_r<0,\quad A_r=\ell C_r,\quad \ell>0.
$$

下标 $r$ 在 $C_r,A_r$ 中表示旋转参考。物理 Fourier 频率始终是 $m=4j$。
令 $b_m=i\operatorname{sgn}(m)\widehat B_m$、$c_m=\widehat{C-C_r}_m$，
则真实线性 regular 图为 $b_m+q_m c_m=0$，并且

$$
q_m'=m\gamma(q_m^2-\ell)+\beta(\ell-1)q_m.
\tag{Q.2}
$$

这里 $q_m$ 是从真实远端 regular 线向内传播的比值，不是任意外端常数，也不是
有限长 Dirichlet 近似。由已证 R74 入口，记实际 $a_R$ 和 $\omega$，有

$$
q_*=(1+(a_R/(4\omega))^2)^{-1/2},\qquad
|q_m(R)-q_*|\le e_m,
$$
$$
e_4=0,\qquad
e_m\le 2^{42}\exp[-2m\omega_-(2^{24}-25/8)]\quad(m>4).
\tag{Q.3}
$$

原生计算以 Arb 保留 (Q.3) 的正指数小量；它们虽然转换为 IEEE double 时会
下溢，却没有在真实包络中被设为零。例如 $m=8$ 的保存值约为
$1.28844\cdot10^{-170341211}>0$。只有已证的 $m=4$ 费用准确为零。

对象为
`data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json`，
SHA256 为 `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`。
完整仿射区间为

$$
\delta=-\frac{7789843107295549}{4611686018427387904}+\eta,
\qquad |\eta|\le10^{-9}.
\tag{Q.4}
$$

主体另用的 $E_\nu=E\exp(\nu h)$ 在 $r\ge.18$ 上准确等于 $E$，因此整个
$[3/2,25/8]$ 的 $q_m$ 与该 $\nu$ 无关。这只说明本帽接口可沿用，不能把
原 $\nu=0$ 腰部证书转给新的主体。

## 2. 每个闭盒上的完整比较

设向内时间为 $t=R-r$。在一个原闭盒上，由有向完整目标系数得到
$\gamma\in[g_-,g_+]$、$\ell\in[\ell_-,\ell_+]$ 以及
$-\beta(\ell-1)\in[b_-,b_+]$，其中 $g_-,\ell_->0$。对于任意 $q>0$，
真实 (Q.2) 的向内右端夹在

$$
m g_-\ell_-+b_-q-mg_+q^2
\ \le\ q_t\ \le\
m g_+\ell_++b_+q-mg_-q^2.
\tag{Q.5}
$$

上下式是常系数方程 $y_t=A+By-Cy^2$，其中 $A,C>0$。它保持正半轴。
令

$$
D=\sqrt{B^2+4AC},\quad
p=\frac{2A}{D-B}>0,\quad n=-\frac{D-B}{2C}<0,
$$
$$
z=\frac{y_0-p}{y_0-n}e^{-D\tau},\qquad
\Phi_\tau(y_0;A,B,C)=\frac{p-zn}{1-z}.
\tag{Q.6}
$$

这是直接分离变量得到的完整时间 $\tau$ 流。$y_0>0,\tau\ge0$ 给
$1-z>0$；程序在每一次调用都另外检验这个严格分母门以及输出正性。
标量比较定理先在当前闭盒把 (Q.5) 的下流、上流夹住真实解，再把各自的
有向端点作为下一个闭盒的初值。归纳给整个后缀的真实包络。无需假设真实
$q_m$ 在盒内单调，也没有用盒端点采样代替连续径向系数。

程序从筛选报告逐行读取原 native 索引，并核对原盒、所用后缀和真实 scalar germ
的包含关系；相邻端点必须完全相同，完整覆盖 $[3/2,25/8]$。全部663盒
按向内方向遍历。原报告的 source、对象和筛选输入 SHA 均被核对。每次 Arb
运算使用320 bit 有向球算术；序列化的十进制球重新读入时再次取 `.lower()`、
`.upper()`，不把中点误当有向边界。这样包括了全部算术舍入。

逐频256次的完整传播实际成功；保存在原生文件的每一个 $q_m^-,q_m^+$ 满足

$$0<q_m^-\le q_m(L)\le q_m^+.
\tag{Q.7}$$

部分向外舍入的展示值如下，完整256行在数据中：

| 物理频率 $m$ | 严格下界 | 严格上界 | 浮点近似（仅候选） |
|---:|---:|---:|---:|
| 4 | 1.0289402897603 | 1.0399547502452 | 1.0343945498669174 |
| 8 | 1.0268045212674 | 1.0369525501938 | 1.0318332378589600 |
| 128 | 1.0243603528680 | 1.0342672634696 | 1.0293114746451644 |
| 256 | 1.0242694750006 | 1.0341420322653 | 1.0292252830977450 |
| 512 | 1.0242212204142 | 1.0340755109345 | 1.0291821341026524 |
| 1024 | 1.0241969726200 | 1.0340420951186 | 1.0291605462759280 |

浮点列由有限 primitive 的 Radau 方程产生，其全部值实际落在对应 (Q.7) 内；
这只是便于有限 BVP 取中心，并未缩小真实有向区间。

## 3. 不遗漏高频的统一上界

原[解析筛选](R133-supplement-true-cap-radial-decay-and-growing-analytic-width.md)
的663行中，每行 `q_lower/q_upper` 原本已经对**全部** $m\in4\mathbb N$ 成立。
解析权只改变 Green 的径向费率，不改变这些实际 Riccati 比值。
该报告的 `weighted_constants.q_upper` 是这663个完整上界的最大值。实际有向消费得

$$
q_{\max}\le
1.0597518102935095661444170270941854\ldots<53/50.
\tag{Q.8}
$$

因此 (Q.1) 对超过向量尾端的全部 $m>1024$ 仍成立；对负频率按真实共轭取
$q_{-m}=q_m$。这一步没有从有限256模作经验外推。

## 4. 完整物理边界消费合同

令 $\widetilde q_m$ 为保存的有限浮点向量，以其精确 dyadic 值解释。对每个保留频率定义

$$
\epsilon_m=\max\{\widetilde q_m-q_m^-,q_m^+-\widetilde q_m\},
\qquad \epsilon_{-m}=\epsilon_m.
\tag{Q.9}
$$

实际有向消费得到

$$\max_{4\le m\le1024}\epsilon_m<.005560200378199.
\tag{Q.10}$$

`true_q_error_directed_records` 保存这些有向数；便于浮点诊断的
`true_q_error_abs_upper` 则把有向上界转换为 double 后再向上取一邻值。
严格消费者应优先读有向记录。若 $P_N$ 保留 $0<|m|\le4N$，$N\le256$，则
完整 $A_0=\ell^1$ 物理范数中

$$
\begin{aligned}
\|b+qc\|_{A_0,\ne0}\le{}&
\|P_N(b+\widetilde q c)\|_{A_0}
+\sum_{0<|m|\le4N}\epsilon_m|c_m|\\
&+\|(I-P_N)b\|_{A_0,\ne0}
+\frac{53}{50}\|(I-P_N)c\|_{A_0,\ne0}.
\end{aligned}
\tag{Q.11}
$$

正负模都在和中；若使用实 sine/cosine 幅度，必须按对应的复 Fourier 因子
转换。$b=i\operatorname{sgn}(D)B$ 的 $A_0$ 范数等于 $B_{\ne0}$ 的范数。
对于互逆坐标的有限候选，$B=\alpha U/v$、$C=1/v$，所以物理 $b,c$ 一般包含
无限高频。$U,V$ 的有限 Fourier 支撑不能直接删去 (Q.11) 的两个尾项。

真正[统一小输入周期帽](R133-supplement-universal-small-inner-periodic-cap.md)
允许 $\zeta=c_{\ne0}(L)\in A_2$、$\|\zeta\|_{A_0}\le2\cdot10^{-5}$ 和独立
$\|f_B\|_{\dot A^2_\sigma}\le2^{-60}$。其实际另一迹为

$$b(L)+q\zeta=\mathcal N(\zeta,f_B),\qquad
c_0(L)=\mathcal M(\zeta,f_B),\qquad B_0(L)=0,
\tag{Q.12}$$

其中

$$
\|\mathcal N\|_{A_0}<1.663187\cdot10^{-8},\qquad
|\mathcal M|<4.636375\cdot10^{-9}.
\tag{Q.13}
$$

因此 (Q.11) 的线性失配预算还须另加 (Q.13) 的真非线性差；mean C 行必须比较
真正 $\mathcal M$，不能设为零。$ζ$ 的小输入门、完整 $A_2$ 正则和远端 $f_B$
门都须在实际主体上消费。这给明确的完整匹配残差，不等于已解匹配方程。

## 5. 文件与复现

本结论的新文件是：

- `scripts/fourfold_codazzi_cap_cut_q_vector.py`：原完整663盒与256频率传播；
- `scripts/fourfold_codazzi_cap_cut_q_tail_bound.py`：向量逐模误差和全频53/50消费；
- `notes/2026-11-13-R133-cap-cut-r15-q256-floating.json`：有限浮点向量；
- `notes/2026-11-13-R133-cap-cut-r15-q256-native.json.gz`：整个有向传播结果及全部输入 SHA；
- `notes/2026-11-13-R133-cap-cut-r15-q256-with-tail.json`：供完整 cut producer 读取的原向量加真实差额。

在课题目录内，以装有 python-flint 的同一环境运行前两个脚本，分别指定新的
`--floating/--native` 和 `--out` 路径即可复现。源拒绝覆盖已有结果。原生记录
使用的参考为 `2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz`，
SHA `3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22`；
完整筛选 SHA 为 `507db702b42e95272131e949fdb1141844273989be08cef46682e4e0f7199129`。
已有真实输入不被替换，mean、regular 和未保留 Fourier 模均未删去。

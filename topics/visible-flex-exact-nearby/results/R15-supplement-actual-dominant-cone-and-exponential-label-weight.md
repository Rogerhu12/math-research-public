# R15 续篇：真实主方向锥与全频纯指数标签权

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对 R69/R74/R115 实际使用的同一 R72 无限尾，
共同 cut128 的允许线到内部标签的准确权满足
$$
 \boxed{\qquad \frac14\le\mathfrak w_m<e^{391m}
       \quad(m\in4\mathbb N).\qquad}                         \tag{C.1}
$$
因此物理 raw 两迹的充分权可取 $e^{404m}$，不再需要旧 R15 (4.5) 的
$e^{371m+2\cdot10^6(1+\log(1+m))^2}$。

这里使用**完整两迹的 norm**，不假设任何频率的高度分量非零，也不把
它改称 cut128 的同宽 Dirichlet 图。mean 仍是独立有限行。本篇改进
全部真实线性标签费；非零标签处的完整高输入非线性图逆不由它自动得到。

## 1. 真实胞元与一个更窄、但有相对余量的频窗

符号沿用 [R15 §§1–4](R15-full-tail-lines-label-weights-and-ordinary-sources.md)
及源 quantitative-newton-twist-flex
[R72 §§7–8](../../quantitative-newton-twist-flex/results/R72-large-width-inner-tail-to-cut128.md)。
原源 blob 为 `a7c78793ba18724a4f0553b6ccd55259b8f4df92`。

实际九段矩阵为 $B_{m,j}$，$\det B_{m,j}=1/64$，且
$$
 X_{m,j-1}=-2^{-39/4}e^{-mh_j}B_{m,j}X_{m,j}.
 \tag{C.2}
$$
源 R72 的固定理想特征基满足
$$
 \|E_m\|_\infty\le3,\quad\|E_m^{-1}\|_\infty\le4,
 \qquad
 -E_m^{-1}B_{m,\infty}E_m
       =\operatorname{diag}(\Lambda_m,\lambda_m),
 \tag{C.3}
$$
其中
$$
 \nu_m=\frac{m^2(m^2-1)}{12},\quad
 T_m=\frac{65}{64}\left(64+\frac1{64}\right)\nu_m
                   -\left(1+\frac1{64}\right),
$$
$$
 \Lambda_m=\frac{T_m+\sqrt{T_m^2-1/16}}2,
 \qquad\lambda_m=\frac1{64\Lambda_m},\qquad
 L_m=2^{-39/4}\Lambda_m>\sqrt2.
 \tag{C.4}
$$
这些是已使用的真实规范，未把 $\alpha=65/64$ 或末端因子64改为另一套尾。
对 $m\ge4$，$\nu_m\ge m^4/16$，$T_m-1>64\nu_m$，所以
$$
 \Lambda_m>64\nu_m\ge4m^4,\qquad
 \frac{\lambda_m}{\Lambda_m}<2^{-26},\qquad L_m<m^4.
 \tag{C.5}
$$
第一式可先用 $\Lambda_m>T_m/2>1$ 得 $\lambda_m<1$，再代
$\Lambda_m=T_m-\lambda_m$；没有循环使用所需下界。
最后一式用 $\Lambda_m<T_m<66\nu_m<\tfrac{11}2m^4$ 和
$2^{-39/4}<2^{-9}$。

当
$$
 m^4\sqrt{\delta_j}\le2^{-28},                              \tag{C.6}
$$
源 R72 (7.2) 的两个条件均成立，因此其**真实**误差门给
$$
 \|B_{m,j}-B_{m,\infty}\|_\infty
 \le32768m^8\sqrt{\delta_j}.
$$
设 $M_{m,j}=-E_m^{-1}B_{m,j}E_m$。由 (C.3)–(C.6)，
$$
 M_{m,j}=\begin{pmatrix}\Lambda_m&0\\0&\lambda_m\end{pmatrix}
            +\Delta_{m,j},\qquad
 \|\Delta_{m,j}\|_\infty
 <\varepsilon_0\Lambda_m,
 \qquad \varepsilon_0=\frac1{2048}.
 \tag{C.7}
$$
准确算术是
$12\cdot32768m^8\sqrt\delta/\Lambda_m
 \le98304m^4\sqrt\delta\le3/8192<1/2048$。
这是**相对主特征值**的估计；原 R72 的较宽绝对误差窗单独不能代替它。

## 2. 允许真线在整个强频窗内的锥与下界

在 $E_m$ 坐标写状态为 $(x,y)$，取锥
$|y|\le|x|/2$。由 (C.7)，一次真实胞元有
$$
 |x_{j-1}|\ge
 (1-\tfrac32\varepsilon_0)L_me^{-mh_j}|x_j|,
$$
$$
 \left|\frac{y_{j-1}}{x_{j-1}}\right|
 \le\frac{\frac32\varepsilon_0+\tfrac12\,2^{-26}}
           {1-\frac32\varepsilon_0}<\frac12 .
 \tag{C.8}
$$
同时真实 Möbius map 的导数是
$$
 \phi_j'(z)=
 \frac{\det M_{m,j}}{(M_{11}+M_{12}z)^2},\qquad
 \det M_{m,j}=1/64,
$$
$$
 \sup_{|z|\le1/2}|\phi_j'(z)|
 \le\frac1{64\Lambda_m^2(1-3\varepsilon_0/2)^2}<\frac14.
 \tag{C.9}
$$
标量规范因子在投影变换中准确相消。这里用的是全真行列式，不是理想
矩阵的行列式去替代真余项。

若从某层起 (C.6) 永远成立，从任意更深终层的锥内方向向浅传播，
(C.9) 使每个固定浅层的方向一致收敛。所得实直线族在整个锥内，且
满足全部真实递推。在任一固定层规范 $x=1$ 后，对足够深的 $j$，
大分量每步因子趋于 $L_m>\sqrt2$；因此其向深振幅衰减，完整规范
状态有界。它是 R15 强空间中的真实齐次解。

R15 §2 的保标签唯一性于是说明：它就是既有允许线
$\Lambda_m=\operatorname{span}H_m(128)$ 的延续，而不是另外挑选的
一条方便锥线。这个论证也支付了“未来边界位于锥内”的条件；没有从
一个有限标签坐标的大小猜测它。

当 $m\ge8$，(C.5) 进一步给 $L_m/2>1$。所以在这些真实强频窗胞元中
可以保留简单但有效的下界
$$
 |x_{j-1}|\ge e^{-mh_j}|x_j|.                              \tag{C.10}
$$
主通道的大倍数没有作为逆传播损失重复支付。

## 3. 强频窗起层确在标签层以前

准确定义
$$
 j_0(m)=\max\left(129,
                \left\lceil56+8\log_2m\right\rceil\right).
 \tag{C.11}
$$
$\delta_j=(2/25)2^{-j}<2^{-j}$，故 $j\ge j_0$ 时 (C.6) 成立。

对 $m\le172$，源 R72 已证标签层为 $b_m=128$，直接有
$$
 (E_m^{-1}H_m(128))_1=1,
 \qquad\|H_m(128)\|_\infty\ge1/4.                         \tag{C.12}
$$
这些频率不需要下面的前缀乘积，也不要求把 $b_m$ 说成大于128。

对 $m\ge176$，源 R72 §7.3 给常宽段所有大参考因子小于1，因此
$j_m=b_m+1>4096$。在这个真实标签选择层，
$$
 L_me^{-mh_{j_m}}\ge1,
 \quad h_{j_m}=8\delta_{j_m}^{1/256},
 \quad L_m<m^4.
$$
于是
$$
 \delta_{j_m}^{1/2}
 \le\left(\frac{\log m}{2m}\right)^{128}.                  \tag{C.13}
$$
由 $b_m=j_m-1$ 及准确 $\delta$ 归一化，
$$
 2^{-b_m/2}=5\sqrt{\delta_{j_m}}.
 \tag{C.14}
$$
$m\ge16$ 时 $\log m<\sqrt m$（从16起微分即可），因而
$$
 m^4\,2^{-b_m/2}
 \le5m^4\left(\frac{\log m}{2m}\right)^{128}
 <5\,2^{-128}m^{-60}<2^{-28}.
 \tag{C.15}
$$
这证明 $b_m>56+8\log_2m$，特别 $b_m\ge j_0(m)$。
所以从实际标签层向浅到 $j_0-1$ 的每个胞元确实处于 (C.7) 的已付锥内。
没有把任意高标签假定已经位于同一个低窗。

## 4. 剩余浅前缀只付 $32m$

取 $m\ge176$ 并把真实标签归一为1，故在 $b_m$ 的大坐标准确 $x_{b_m}=1$。
(C.10) 及 $\|E_m^{-1}\|\le4$ 给
$$
 \|X_{m,j_0-1}\|_\infty
 \ge\frac14\exp\left[-m\sum_{j=j_0}^{b_m}h_j\right].
 \tag{C.16}
$$
未进入强频窗的浅胞元共有
$N_m^{bad}=j_0-129$ 个。对它们保留 R15 (3.4) 的完整真逆，而不对角化：
$$
 \|\mathcal A_{m,j}^{-1}\|_\infty
 \le2^{80}(1+m)^{312}e^{m(h_j+\beta_j)}.
 \tag{C.17}
$$
这里 $\beta_j$ 是 R15 (3.1) 的真实流角费，非 R119 的额外标签权。
结合 R15 (3.7) 的完整无限和
$\sum_{j>128}(h_j+\beta_j)<358$，有
$$
 \mathfrak w_m\le
 4\exp\left\{358m+
    N_m^{bad}[80\log2+312\log(1+m)]\right\}.                \tag{C.18}
$$

下面对**所有**频率支付剩余项，非有限抽样。若 $N_m^{bad}>0$，
取 $x=\log m$。由 $\log2>2/3$ 和 ceiling 的准确余量，
$$
 N_m^{bad}<8\log_2m-72<12(x-6),\qquad x>6.
$$
又 $80\log2<56$、$\log(1+m)\le x+1/4$，令 $u=x-6>0$，得到
$$
 \frac{N_m^{bad}[80\log2+312\log(1+m)]}{m}
 <e^{-6}(24072u+3744u^2)e^{-u}.
 \tag{C.19}
$$
用 $ue^{-u}\le1/e$、$u^2e^{-u}\le4/e^2$ 以及 $e>8/3$，右侧至多
$$
 \left(\frac38\right)^6
 \left(24072\frac38+3744\frac9{16}\right)
 =11133\left(\frac38\right)^6<32.
 \tag{C.20}
$$
最后一个门的准确整数形式是
$11133\cdot3^6<32\cdot8^6$。
若 $N_m^{bad}=0$，同一结论自然成立。因此
$$
 \mathfrak w_m<4e^{390m}<e^{391m}.                           \tag{C.21}
$$
连同 (C.12) 和 R15 的 $\mathfrak w_m\ge1/4$，证明 (C.1)。

## 5. 真实 raw 两迹、普通源和强标签规范

令 $\widehat e_m=H_m(128)/\|H_m(128)\|_\infty$。若某规范切口迹
$v_m=z_m\widehat e_m$ 在允许线上，唯一内部标签仍准确为
$a_m=z_m\mathfrak w_m$。故
$$
 \sum_m e^{391m}\|v_m\|_\infty<\infty
 \quad\Longrightarrow\quad
 \sum_m|a_m|<\infty.
 \tag{C.22}
$$
在 R15 (1.2) 的**实际物理 raw** 状态 $V_m$ 中，
$X_{m,128}=\zeta_{128}^{-1}e^{\tau_{128}m}V_m$，且
$\tau_{128}+391<404$。所以充分条件简化为
$$
 \boxed{\quad
 \zeta_{128}^{-1}\sum_{m\in4\mathbb N}
       e^{404m}\bigl(\|V_m\|_\infty+\|V_{-m}\|_\infty\bigr)<\infty.
 \quad}                                                     \tag{C.23}
$$
$V_m$ 中的 $\nu_m C_m$ 和 $m^2 C_m$ 未删除，四阶角权仍在状态定义内。

对 R15 §5 的普通连续源，仍需真实仿射条件
$v_m-g_m(N)\in\Lambda_m$；在 (C.22) 中把 $v_m$ 换为
$v_m-g_m(N)$ 即可。它不把 particular 两迹改成0，也不删除 source
的 $\mathcal S_1,\mathcal S_2$ 或 mean holonomy 条件。

本篇是线性真实尾的完整两迹权改进。即使 (C.23) 大幅减小了既有
费用，它仍有明确的指数角宽差；不能把它写成同宽零阶逆。

## 6. R74 同一真实线性输入的直接改进

R74 (74.31)–(74.33) 的其他项完全不变，只把其中旧
$e^{371m+2\cdot10^6(1+\log(1+m))^2}$ 改为 (C.23)。
原保守线性费2000再加 $404-371=33$，给
$$
 |a_m^{tail}|
 \le\exp[(-T/2+2033)m]
       \bigl[h(0)^2|f_m|+m^{1/p_*}F_{m,p_*}\bigr],
 \quad T=2^{24}.                                           \tag{C.24}
$$
仍假设 $B$ 后齐次，且 regular 数据、普通体源和全部高频均按原 R74
合同。不对位于 connector 或真尾的普通源免费应用该式。

因此 R119 全 connector 续篇采用的 $8192$ 标签权还有更强实际余量：
$$
 \boxed{\quad
 \|a^{tail}\|_{\ell^1_{8192}}
 \le e^{-33513532}
     \sum_{m\ne0}\bigl[h(0)^2|f_m|+|m|^{1/p_*}F_{m,p_*}\bigr].
 \quad}                                                     \tag{C.25}
$$
准确指数是 $4(2^{23}-2033-8192)=33513532$。
R74 的 mean 通量行仍单列。这改进已付线性输入和以后完整 matching
的可用预算，未由此宣称非线性 matching 或最终强逆完成。

[准确核验程序](../scripts/fourfold_actual_tail_cone_label_weight_20261113.py)
只检查上述真实相对误差、锥、标签层比较和所有纯有理门；
[完整小报告](../notes/2026-11-13-R15-actual-tail-cone-label-weight-budget.json)
保存原始输入及依赖哈希。全层/全频结论由 (C.6)–(C.20) 的证明覆盖，
不是通过有限频率扫描外推。

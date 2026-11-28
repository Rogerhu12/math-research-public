# R642：真实旋转尾的独立参考逆、窄频带与幅度归一坐标

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。本文接续 [R639](R639-rational-morse-uniform-gap-and-double-kernel.md)，解决一个具体问题：真实旋转尾的系数差含 $w\sin b$，并不属于旧的 $H^{3/4}$ 扰动类。下面重新选择尾频带和正组件的参考高度因子，在 R639 的构造类中选定一个实际两端全平双核背景，给其倾角的独立有限维参考逆。

本文的线性输入来自 Hu 可读稿 [§7](https://github.com/Rogerhu12/math-research/blob/3871f5ce2dd5f4b221dd60a24211cb814f043b09/papers/flexible-surface-readable-4/07-flat-tails.tex)、[§8](https://github.com/Rogerhu12/math-research/blob/3871f5ce2dd5f4b221dd60a24211cb814f043b09/papers/flexible-surface-readable-4/08-spectral-selection.tex)、[§9](https://github.com/Rogerhu12/math-research/blob/3871f5ce2dd5f4b221dd60a24211cb814f043b09/papers/flexible-surface-readable-4/09-reference-inverse.tex) 的实际质量/电阻、选择与匹配公式，[物理坐标附录](https://github.com/Rogerhu12/math-research/blob/3871f5ce2dd5f4b221dd60a24211cb814f043b09/papers/flexible-surface-readable-4/appendix-radial-geometry.tex) 的明确 profile/坐标公式，以及 R639 的中心统一谱隙。引用中原来记为 $\mathcal E_n^C$ 的界不会直接改名；第 2–4 节逐项把绝对高度尺度取消，把真正剩余代价限定在 $e^{Cn^{9/4}}$。

## 1. 旋转尾的准确算子与准确势

本节暂用正坡记号 $h'=w>0$。将参考浸入
$(r\cos\theta,r\sin\theta,h(r))$ 绕 $y$ 轴旋转，竖直坐标写为

$$
z_b=h_a+(h-h_a)\cos b-r\cos\theta\sin b.
$$

与主稿 $h'=-w$ 的记号只差一次固定竖直反向，不影响以下算子或其逆。设

$$
c_b=\cos b,\quad s_b=\sin b,\quad
\rho_b=c_b+s_bw\cos\theta.
$$

取一个小的固定 $|b|<b_0$，使 $\rho_b>1/2$。Hu §3 的高度系数为

$$
k=w c_b-s_b\cos\theta,
\quad p=s_b\sin\theta,
\quad D=(1+w^2)(1-p^2)-k^2=\rho_b^2,
\quad Q=k+(1+w^2)p_\theta=w\rho_b.
$$

因此准确有

$$
a_b=w\rho_b^{-2},\qquad b_{\rm cross}=0,\qquad
c_b^{\rm op}=(w'/r)\rho_b^{-2},
$$
$$
\boxed{L_b=\operatorname{div}(\rho_b^{-2}\mathbf A\nabla),
\qquad \mathbf A=\operatorname{diag}(w,w'/r).}          \tag{1}
$$

其特征速度仍是 $\sqrt{-w'/(rw)}$；负组件的两个返回图与未旋转参考完全相同。于是纯倾角不需要逐个改变尾行程角或尾 circle chart。

对任意正函数 $\rho$，直接展开乘积给

$$
\rho\operatorname{div}(\rho^{-2}\mathbf A\nabla(\rho v))
=L_0v+Q_\rho v,
$$
$$
Q_\rho=\rho^{-1}L_0\rho
-2\rho^{-2}\langle\mathbf A\nabla\rho,\nabla\rho\rangle.
                                                               \tag{2}
$$

对本节的 $\rho_b$，

$$
L_0\rho_b=s_b\bigl[(ww')'-ww'/r\bigr]\cos\theta,
$$
$$
\langle\mathbf A\nabla\rho_b,\nabla\rho_b\rangle
=s_b^2\left[w(w')^2\cos^2\theta+
             (w'/r)w^2\sin^2\theta\right].             \tag{3}
$$

令

$$
m(r)=12w/r^2,\qquad B_0=-m^{-1}L_0.
$$

经过 $u=\rho_bv$ 和源乘 $\rho_b$ 后，准确得到

$$
-m^{-1}\rho_bL_b(\rho_bv)=(B_0+q_b)v,
\qquad q_b=-Q_{\rho_b}/m.                              \tag{4}
$$

其一阶与二阶倾角项均明确为

$$
\begin{split}
q_b={}&-\frac{s_br^2}{12\rho_b}
 \left[\frac{(w')^2}{w}+w''-\frac{w'}r\right]\cos\theta\\
&+\frac{s_b^2r^2}{6\rho_b^2}
 \left[(w')^2\cos^2\theta+
                         \frac{ww'}r\sin^2\theta\right].
\end{split}                                                   \tag{5}
$$

Hu 尾的实际 profile 界为

$$
|\partial_r^kw|\le C_ke^{-n^{5/2}+C_kn^2},\qquad
|\partial_r^k\log w|\le C_ke^{C_kn^2}\quad(k\ge1).
$$

式 (5) 每一项至少保留一个未被约掉的 $w$。所以对固定阶数 $a,d$，未作倾角微分时有

$$
\|\partial_r^a\partial_\theta^d q_b\|_{L^\infty(\mathrm{cell}\ n)}
\le C_{a,d}|b|e^{-n^{5/2}+C_{a,d}n^2}.                \tag{6}
$$

对每个固定正整数 $\ell$，准确的参数导数界则是

$$
\|\partial_b^\ell\partial_r^a\partial_\theta^d q_b\|_{L^\infty(\mathrm{cell}\ n)}
\le C_{a,d,\ell}e^{-n^{5/2}+C_{a,d,\ell}n^2}.
                                                               \tag{6a}
$$

正阶参数导数在 $b=0$ 一般不为零，所以 (6a) 不含 $|b|$。逆的底阶小范数使用 (6)，光滑参数依赖使用 (6a)。

在有限中心，可用径向 cutoff 把倾角从左尾的 $b$ 变为右尾的 $0$，并令 $\rho_b$ 同样平滑过渡。过渡区固定紧支撑且 $w>0$，因此其 $q_b$ 为普通 $O(b)$ 光滑乘子。这里先构造辅助参考 $\operatorname{div}(\rho_b^{-2}\mathbf A\nabla)$；它与实际 cutoff 旋转高度的导数在过渡区的差是固定紧区间上的小系数差，随后在真正状态相关逆中另计。

## 2. 重新选择的频带及全部实际条件

保留 Hu 的真实几何尺度

$$
A_n\asymp e^{-n^2},\qquad B_{R,n}\asymp A_n^9,\qquad
\lambda_n=e^{-n^{5/2}}\prod_{k=N}^n\sigma_k,
\quad1\le\sigma_k\le2.
$$

保留其指数为 $12$ 的短正连接和全部 profile 公式。改变的是频带：

$$
q_n^{\rm new}=n^{9/4},\qquad
E_n^{\rm new}=e^{n^{9/4}},\qquad
H_n^{\rm band}=C_*q_n^{\rm new}A_n^{-1/2},
$$
$$
\mathcal I_n=\{j\in\mathbb Z:j\ge2,
                     H_{n-1}^{\rm band}\le j<H_n^{\rm band}\}.
                                                               \tag{7}
$$

在首次频带加入所有较小的 $j\ge2$。选择针对全部整数，延用 R633 的明确奇数扩展。

以下条件是实际需要检查的全部尺度条件。

**深尾起点。** 对 $j<H_n^{\rm band}$，

$$
j^2A_{n+1}\sqrt{\log(A_{n+1}/B_{R,n+1})}
\le C n^{9/2}(n+1)e^{-2n-1}\to0.                     \tag{8}
$$

所以第 $n+1$ 个 cell 已进入原文的 deep-tail 条件；其 $Cj^{-4}$ 归一 Hilbert Dirichlet 逆不变。

**短正连接的传递误差。** 同一导数无关的状态矩阵给

$$
\eta_{n,j}\le C n^{9/2}e^{-7n^2+O(n^{3/2}+n)}
=o(e^{-n^2}).                                         \tag{9}
$$

仍远小于选择所用的 $\delta_n=c_0e^{-n^2}$。

**排除区间的总长度。** 原文每个频率的坏参数区间长度是 $C\delta_n$；一条频带的整数数目至多 $H_n^{\rm band}$，所以其总坏长度不超过

$$
C n^{9/4}e^{-n^2/2}.
$$

总和有限，取初始 $N$ 足够大后满足原 product selection 的严格余量。并未取消任何真实选择条件。

**此前正 buffer 的压缩。** 第 $m<n$ 个模型的作用量满足
$\tau_{m,j}=j\sqrt{A_m}\ge c C_*m^{9/4}$。归一模型的所有底阶常数至多 $e^{Cm^2}$（下一节给出高度取消），相邻 $H^{-\gamma}$ 权比为 $e^{O(m^2)}$，故

$$
e^{Cm^2}(1+j)^C e^{-c\tau_{m,j}}
$$

中的频率多项式可先并入 $e^{-c\tau/2}$；$m^{9/4}/m^2\to\infty$ 支付余下固定常数。有限中心用 R639 的固定统一隙及有限 head 处理。

**末端 Robin core。** 原文真正的传递成本为

$$
K_{n,j}=e^{Cn^2+C_o\tau_{n,j}},\qquad
\tau_{n,j}\le C_* n^{9/4}.
$$

因此现在确有 $K_{n,j}\le e^{C'n^{9/4}}$。这里没有把原 $n^{5/2}\log n$ 成本在旧频带中强行降低。

**两条最终 matching 小量。** 前一 buffer 满足

$$
\tau_{n-1,j}/\tau_{n,j}\asymp e^n,\qquad
\tau_{n-1,j}\ge cC_*(n-1)^{9/4}.
$$

因此 $\delta_n^{-1}\|E_b\|$ 和

$$
e^{Cn^2}\delta_n^{-1}
e^{C_o\tau_{n,j}-c\tau_{n-1,j}}
$$

均可同时小于 $1/4$。这是原文末端二乘二匹配真正使用的两个条件。所有选择仍先固定一次几何，再对两个邻近端点指数使用同一个逆。

## 3. 为什么归一 Hilbert 代价不含绝对 $\lambda_n^{-1}$

### 3.1 单个模型与有限末端 core

在模型上，$r_X=v$、$w=\lambda_n v$；源和输出使用
$L^2(m\,dr)$。准确换元为

$$
\|u\|_{L^2(mdr)}^2
=12\lambda_n\int(v/r)^2|u|^2dX.
$$

把场乘 $\sqrt{\lambda_n}$ 后，绝对高度从所有模型算子界中消失。$v,v^{-1}$、半径和固定坐标/截断导数的代价均为 $e^{Cn^2}$。Hu §6 的准确 Morse 逆界为 $\|H_{j,\mathrm M}^{-1}\|\le8d_n^9$，即 $e^{9n^2+O(1)}$，对全部 $j\ge2$ 成立；这里不需要以频带大小补偿一个未说明的谱代价。中心为 R639 的固定共同隙。

有限末端 core 采用实际状态 $(u,wu_{r_o}/\lambda)$。其源质量和 deep Poisson 范数分别不超过

$$
\lambda e^{Cn^2},\qquad \sqrt\lambda e^{Cn^2},
$$

两个单位状态的 Wronskian 则准确为 $\lambda$ 倍行列式。Green kernel 的 $\lambda^{-1}$ 因而与质量或两个 Poisson 因子准确抵消。余下的成本就是上一节的 $e^{Cn^2+C_o\tau}$。

相邻 cell 的高度比也只为 $e^{O(n^2)}$：共同前缀 $\prod\sigma_k$ 消去，而 $\log(\lambda_{n+1}/\lambda_n)=O(n^{3/2})$。任何固定有限个相邻 cell 的坐标变换不花绝对 $e^{n^{5/2}}$。

### 3.2 深尾积累误差须保留为端点比

原文普通高度的 node quotient 将相邻 $\log\lambda$ 项分别粗估，给 $O(n^{5/2}+m^{5/2})$；若直接这样估计，会丢掉本稿需要的改进。应保留它们的望远镜和。

以右尾为例，

$$
\mu_n\asymp\lambda_n A_n^2,\quad
R_n\asymp\lambda_n^{-1}A_n^{-4},
$$

所以

$$
\sum_{\nu=m}^{k-1}\log(\mu_{\nu+1}R_\nu)
=S_k-S_m+\log(\lambda_k/\lambda_m)+O(k^2+m^2),
\qquad S_n=\tfrac23 n^3.                              \tag{10}
$$

在对称 Hilbert node kernel 中还乘 $\sqrt{\mu_k/\mu_m}$，因此最多留下

$$
\exp\left\{C(k^2+m^2)-|S_k-S_m|
                      +\tfrac12|\log(\lambda_k/\lambda_m)|\right\}.
                                                               \tag{11}
$$

左尾的 outward resistance 有一次索引错位；它的实际配对使一部分 $\lambda$ 直接消去，(11) 仍是共同上界。bounded gauge $r^{j^2}$ 的节点比也望远镜相消，其代价在整个 deep domain 有统一界。

对任意固定 $\delta>0$，由 $\log\lambda_n=-n^{5/2}+O(n)$ 及其相邻差界，

$$
\tfrac12|\log(\lambda_k/\lambda_m)|
\le\delta|S_k-S_m|+C_\delta.
$$

于是 (11) 为

$$
C_\delta e^{C(k^2+m^2)}e^{-(1-\delta)|S_k-S_m|}.        \tag{12}
$$

这保留任意严格小于一的端点指数，并且没有把一个绝对 $e^{Cn^{5/2}}$ 丢进局部系数常数。edge Dirichlet 项只作用于同一或相邻 cell，并由原 $C/\Lambda$ 逆及 interpolation 范数控制，亦满足这个上界。

### 3.3 正组件使用真正幅度归一的高度因子

Hu 原附录在正组件中间选 $h_*=1$。那种具体选择会保留绝对 $w^{-1}$ 的体源代价；本稿不沿用它。

保留其正组件坐标 $y(r)$ 及 $J_*=y_r>0$，但在整个正组件选

$$
\boxed{h_*=(wJ_*)^{-1/2}.}                            \tag{13}
$$

在根处它与负组件规定的 $(w|\xi_r|)^{-1/2}$ 准确相同，故所有 value/conormal transmission 都保留。坐标 $J_*$ 只使用 $w'/w$、真实长度和根速度，所有固定 jets 及指定倒数为 $e^{C_sn^2}$。

经此正共轭，正组件的径向主系数为

$$
a=h_*^2wJ_*=1,\qquad
c=\frac{w'}{rwJ_*^2},\qquad
V=-\frac{h_*}{J_*}(wh_*')'.                            \tag{14}
$$

在 $V$ 中提出 $h_*'=-\tfrac12h_*(\log w+\log J_*)'$，可见全部系数只涉及 $\log w$、$\log J_*$ 的正阶导数及 $J_*^{\pm1}$；绝对 $\lambda_n$ 完全消去。其固定阶界为 $e^{C_sn^2}$，且 $c\ge e^{-Cn^2}y(1-y)$。

Hilbert 范数与 canonical 体源范数的密度比也准确为

$$
\frac{m h_*^2}{J_*}=\frac{12}{r^2J_*^2}.               \tag{15}
$$

负组件已有同一个公式 $h_*=(w|\xi_r|)^{-1/2}$，故 (15) 对全部组件成立。没有在这里偷偷换成带绝对 $w^{-1}$ 的普通 $dr$ 源。回到物理高度时仍可使用原大的材料权 $M$，它会记录真正需要的 $w^{\pm1/2}$。

这个新选择不妨碍 compact kernel rows：状态的 comparison extensions 仍在这些 rows 所在的固定正区等于 reference，要求的是“不随状态变”，并不要求 reference 本身为 $h_*=1$。

## 4. 改进参考 Green 的实际局部界

用 (7) 的一次新 height-ratio 选择、R639 中心和两条真实平尾重做同一个有限接口/终端匹配构造。第 2 节已经逐项支付选择、压缩、deep 和 matching 条件；第 3 节给出源/输出真正的高度取消。

对固定 $\beta=3/4$ 和某个固定 $\epsilon>0$，例如使用邻近端点指数 $5/8$、$7/8$，记 $G_*$ 为带两个核 rows/columns、两个低矩源列及内帽高度/倾角标量的参考增广逆。对加权 canonical 体源的 cell block，其已构造的 Green 界为

$$
\boxed{\|\pi_kG_*\iota_m\|_{H^s_\theta\to H^s_\theta}
\le C_s\exp\{C_s(k^{9/4}+m^{9/4})
                        -\epsilon|S_k-S_m|\}.}         \tag{16}
$$

这里先把共同 $H^{-\beta}$ 权共轭进去；角阶不损失。对于固定的底阶 $s$，指数常数固定。源/输出的有限标量放在固定中心。

零、一模使用 R629 的准确 primitives 而不是 Morse deep inverse。减去真实内帽常数或 $r\cos\theta$ 后，远于源 cell 的同侧输出为零；向内的 block 由 $\sqrt{\mu_k\mu_m}R_m$ 控制。它的对数只有 $C(k^2+m^2)$ 和 $\frac12|\log(\lambda_k/\lambda_m)|$，再乘 $H^\beta$ 的单向差。按 (11)–(12) 吸收，亦给某个正 $\epsilon$ 的 (16)。源的两个固定矩由两个 compact 列去掉，新增项为固定中心到 tail 的同样估计。

第二、第三核的 finite borders 使用 R639 的真实紧支撑 profile Jacobi 块；所有对应标量列/行均是有限中心坐标。本文的进一步选择仍允许把 cuts、heads 和两谱恢复量取得足够小，使 R639 的准确双核、非零端口和共同参考逆同时保留。

## 5. 旋转势是共同底阶源空间中的小算子

令 $\mathbb V_{t,s}$ 使用原物理材料权

$$
M_n=\exp\{n^{5/2}\log^2(e+n)\}
$$

和 $H_n^{-\beta}$，角阶为 $s$。在 canonical 源图中，(4) 的势乘子与 $q_b$ 只差 (15) 的固定密度因子；因而其每个固定阶仍有 (6) 型界。

这里把 $G_*$ 的输出明确写成“全平 body $v$，以及有限帽/核/源标量”，记两个投影为 $\operatorname{pr}_{\rm body}$、$\operatorname{pr}_{\rm fin}$。完整增广比较是

$$
R_b=(\mathbb P_b-\mathbb P_*)G_*
=Q_b^{\rm can}\operatorname{pr}_{\rm body}G_*
 +\Delta C_b\operatorname{pr}_{\rm fin}G_*.             \tag{16a}
$$

$Q_b^{\rm can}$ 只作用于全平 body。canonical body 的有限归一化 rows 固定为参考 rows；帽列用第 7 节 (20) 的新真齐次 lifts，其算子像之差及帽 lift 带来的有限 row 变化均包含在 compact 列矩阵 $\Delta C_b$ 中；其余有限列也在固定中心处理。因此 (16a) 没有遗漏 body 到有限 row 的变化项。这里绝不把 $q_b\cdot1$ 或 $q_b\cdot r\cos\theta$ 放入 $H^\beta$ 源。

对当前固定底阶，(6)、(16) 给 (16a) 的 body 项以下 block 上界

$$
C|b|\exp\{-k^{5/2}+Ck^2+C(k^{9/4}+m^{9/4})
                       -\epsilon|S_k-S_m|\}.          \tag{17}
$$

有限中心的 block 为普通 $C|b|$。由于

$$
|k^{9/4}-m^{9/4}|
\le\delta|S_k-S_m|+C_\delta,
$$

(17) 的两个系数因子可以转到输出端，留下

$$
C|b|\,a_k e^{-(\epsilon/2)|S_k-S_m|},\qquad
a_k=\exp\{-k^{5/2}+C'k^{9/4}+C'k^2\}\to0.            \tag{18}
$$

其行和、列和有界；深尾输出部分的行和与列和同时趋零。故 $R_b$ 在同一个底阶体源空间上为 $O(|b|)$ 有界算子。这个论证可以同时在端点指数 $5/8$、$7/8$ 和两者之间的闭区间作出：第 3 节取同一个严格小于 $1-7/8$ 的 $\delta$，全部 Schur 常数在这个紧指数区间上统一。加上过渡区及有限 endpoint/kernel/source 列的 $O(|b|)$ 变化后，选择一次 $b_0>0$ 使整个增广比较算子在这些源空间中的范数都小于 $1/2$。

两端点指数所得逆是同一个算子：紧支撑光滑源的两个解都属于较弱指数空间，其差解齐次增广方程，而该空间中的底阶 Neumann 逆唯一。再用密度延拓。因此后续状态相关逆可以对同一个 $G_b$ 使用两指数 block 衰减，而不是两个互不相容的端点实现。

这里确实用到了 $9/4<5/2$。若沿用旧 $q_n=n^{5/2}\log n$，(17) 的正指数可以大于负的 $k^{5/2}$，本段不成立。

## 6. 一个底阶邻域足够恢复全部材料权和角阶

不能为每个输出阶另要求更小的 $b$。以下保持上一节唯一选择的 $|b|<b_0$。

对任意固定材料权阶 $t$，

$$
|t|\,|\log M_k-\log M_m|
\le\delta|S_k-S_m|+C_{t,\delta}.
$$

因此在 $\mathbb V_{t,s_0}$ 中仍有 (18)，只改变常数和小一份的正衰减率。对每个 $t$ 可以选一个有限 $N_t$，使深尾到深尾的比较算子范数小于 $1/2$；这不改变背景，也不缩小倾角邻域。

若 $(I+R_b)F=g$ 已在底阶空间解出，将 $F$ 分成前 $N_t$ 个 cell 与剩余尾。有限部分的加权范数由底阶范数控制；固定有限输入到深尾的 block 由 $e^{-cS_k}$ 控制，属于每个固定材料权。对尾方程吸收其深尾到深尾部分，得

$$
\|F\|_{t,s_0}\le C_t(\|g\|_{t,s_0}+\|F\|_{0,s_0})
\le C_t'\|g\|_{t,s_0}.                                \tag{19}
$$

角正则性由同一个底阶逆和交换子恢复。参考 $G_*$ Fourier 对角，有限标量附上其 $0,1,2,3$ 角权；$[\Lambda,Q_b^{\rm can}]$ 用
$||k|-|j||\le|k-j|$ 和乘子的一个角导数控制，仍满足 (18)。依次对方程施加 $\Lambda=(1-\partial_\theta^2)^{1/2}$，在底阶逆上解出新增导数。每一步只用已经得到的较低阶及固定 $q_b$ 的较高角导数，不要求这些较高导数小。

结合径向方程的 normal recovery，得到一个固定损失的 tame 参考逆。倾角参数的导数由

$$
\partial_b(I+R_b)^{-1}
=-(I+R_b)^{-1}(\partial_bR_b)(I+R_b)^{-1}
$$

及其迭代给出；每个固定次数参数导数满足同样尾界。因此整个有限倾角参考族在这一个邻域上光滑 tame。

## 7. 真实端帽标量不能用旧仿射尾代替

在实际旋转尾中，常数高度与旋转参数导数

$$
1,\qquad
\partial_b z_b=-(h-h_a)\sin b-r\cos\theta\cos b
$$

都是 $L_b$ 的准确齐次解。经过 (4) 的共轭，相应端帽 lifts 是

$$
\rho_b^{-1},\qquad
\rho_b^{-1}\partial_bz_b.                              \tag{20}
$$

它们与 $1$、$-r\cos\theta$ 的差包含慢于 $H^\beta$ 的 $w$ 项，故不能把差塞入旧全平未知。应把 (20) 各自乘一个固定 cutoff，作为两个随 $b$ 光滑变化的有限维列；因为它们在完整左尾准确齐次，这些列的算子像只支持于固定过渡区。与 $b=0$ 的列之差因此是普通 compact $O(b)$ 源，已经包括在第 5 节的有限增广比较中。

真正的无限维未知仍在 $H^\beta$ 全平空间中。原高度变量由 $u=\rho_b v$ 恢复；乘法是一个正、可逆、光滑的固定系数操作。外帽仍固定，其两个相应 lifts 不加入未知。

## 8. 给下一步非线性消元留下的准确接口

本稿只给真实倾斜参考的线性体源逆。它保留全部实际低端点自由度、两个 kernel rows/columns 和两个临时 compact 矩源列。

设非线性 raw 曲率残差为 $A$，固定矩投影为 R629 的 $\Pi$。在反射空间设

$$
\Psi_x f=\left(\int f,\int P_1(x)f\right),\qquad
M_x=\Psi_x(B_0,B_1).
$$

准确非线性矩 $\Psi_xA=0$ 给

$$
\boxed{A=T_x(\Pi A),\qquad
T_x=I-(B_0,B_1)M_x^{-1}\Psi_x.}                        \tag{21}
$$

所以类型校正中出现的 raw $A$ 仍然线性来自真正求解的残差 $\Pi A$。增广体源逆中的两个临时矩源列，应用 $\Pi$ 后准确消失；不需要错误地要求每个未解状态的导数仍以旧 $r\cos\theta$ 为余核。

纯旋转尾的返回图不随 $b$ 变，且对每个径向 $w$ 都准确零曲率。因此负区径向控制作用于完整旋转尾时不会产生新曲率源；真正的尾控制导数仍含一个 $H^\beta$ 全平高度修正，和控制自身的 $H^\beta$ 因子。

还需保留一个有限过渡项：改变某个远端 profile 控制会改变 $h_a$，在倾角 cutoff 的固定过渡区产生一个 compact 高度项。其系数是形如 $\int w\chi_m\kappa_m\,dr$ 的序列线性泛函。在控制底范数 $\kappa_m=H_m^\beta b_m$ 下，Cauchy–Schwarz 及 $|w\chi_m|$ 的实际 $e^{-n^{5/2}+C n^2}$ 界给该泛函有界；其输出只乘固定 compact 光滑函数，故对每个输出阶均平滑。这个有限项应明确加入控制源，不把它误称为逐组件局部的两因子项。这两部分共同保留后续 coupled height/circle inverse 所需的控制平滑机制。

后续仍须把这个参考族同状态相关 type completion、完整 circle correction、真实紧支撑双谱控制、固定两矩投影和归一双模 slice 放入同一个 Hamilton 残差身份；本稿不以最后一段的接口描述代替那一个实际非线性定理。

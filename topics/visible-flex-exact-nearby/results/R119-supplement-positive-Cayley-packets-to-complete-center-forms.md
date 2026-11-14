# R119 续篇：真实正片 incoming 包、两端物理迹与中心完整型

2026-11-14，visible-exact / tail_connector（0df957a82d09）。

**状态：已证明。** 第75束的输入要求两条物理 Cauchy 迹均为有限低频包；一个真实正片的 outgoing 一般不满足这种有限支撑条件。本篇直接从该正片完整 Cayley 关系出发，保留两端互耦、真实 KAM 端角、所有输出频率和产生的两个 mean，将其真正的两端物理数据送入两侧负窗的中心。零 mean 的低频 incoming 包，其实际中心像满足第74束的**成对**带外定位门。另给所有正片 ordinary/weak 源以及独立 incoming mean 的明确中心费用。

这里得到的是两个已付负窗型在该实际子空间上的和；没有把这个和称为整条网络沿一个共同参数的 generator。正片内部的参数导数、一个窗口的控制在另一窗口上的响应、以及任意 whole-network 近核的 incoming 频率定位仍在文末明确保留。

## 1. 当前对象、两个端点与共同邻胞包络

取同一个当前 $\Gamma^*(\mathbf a,\Omega)$、原 fixed-stop 和已选 KAM 端角。一个完整内部正型区间 $I$ 的两端分别邻接负窗 $I_-$、$I_+$。令 $j\ge8193$ 为这两个负窗的较浅层号，其层号属于 $\{j,j+1\}$；置
$$
 J=j+5,\qquad \delta=\delta_j,\qquad
 \mathcal X\le2^{-1048576}.
 \tag{A.1}
$$
所有尺度仍是原来的实际尺度。记两窗中心的 $B$ 为 $B_e$，$e=-,+$，并令
$$
 B_{\max}=\max(B_-,B_+)<2^{10}J\delta^{-3/2},\qquad
 L_0=\tfrac14\min(\sqrt{B_-},\sqrt{B_+}).
 \tag{A.2}
$$
每个根自身的斜率 $b_e=|Q_t(t_e)|$ 均保留。第75束的真实根界给
$$
 1<b_e<2^{24}J^{1/2}\delta^{-9/4}.
 \tag{A.3}
$$

为同时覆盖正片的邻胞和两个负窗，定义
$$
 \mathcal N_j^{\rm pair}
   =2\sum_{r=j-3}^{j+3}N_r^c,\qquad
 N_r^c=2^{200}h_r^{-5}\frac{\zeta_r}{\mu_r\delta_r^2}.
 \tag{A.4}
$$
这逐项支配第75束两窗的六项和，以及正片 DN 篇的 $\mathcal M$（后者系数为 $2^{184}$）。由第69--70束的实际规范接缝，
$$
 \mathcal N_j^{\rm pair}
 <2^{-19500}2^{-\alpha(j-8193)},\qquad \alpha=31867/256.
 \tag{A.5}
$$
具体地，$N_{8192}^c<2^{-20138}$，第8192层以前同一公式给相邻比小于16；故最初三个 $j$ 的十四项和分别小于 $2^{12},2^8,2^4$ 倍 $N_{8192}^c$。此后最浅项为 $N_{j-3}^c=N_{8192}^c2^{-\alpha(j-8195)}$，总和小于它的16倍，而 $-20134+2\alpha<-19500$。没有删除 $\delta_{4096}^{-3/2}$ 或 $\delta_{8192}^{-485/4}$。

## 2. 真实完整正片的 graph map

采用[完整正片 Airy Cayley 定理](R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md)的参考归一状态，**先不作其第6节的实际根 frame 变换**。记 $\mathcal C_a,\mathcal C_0$ 为该篇 (C.17) 的两个端点一起的 Cayley 算子，$\mathcal C_0$ 在每个 Fourier 模上仍是完整 $2\times2$ 矩阵。设 incoming/outgoing 为 $a,b$，则齐次情形
$$
 b=\mathcal C_a a,\qquad
 \mathcal G_a a=
 \left(\frac{a+b}{\sqrt2},\frac{b-a}{i\sqrt2}\right)
 =(Y_h,Y_p).
 \tag{A.6}
$$
其参考版本 $\mathcal G_0$ 用 $b=\mathcal C_0a$。在真实 $L^2$ 中，两者都满足
$$
 \|\mathcal G_a a\|^2=2\|a\|^2.
 \tag{A.7}
$$
各 norm 包含两个端点；不得只保留反射的两个对角块。

完整正片篇 (C.20)、(C.8)，其局部邻胞费用和 (A.4) 给
$$
 \|\mathcal C_a-\mathcal C_0\|_{H^s\to H^s}
 <2^{200}J^2\delta^{-2}\mathcal N_j^{\rm pair}\mathcal X,
 \qquad |s|\le4.
 \tag{A.8}
$$
实际未放宽的主常数是 $2^{154}$；相邻层的两次尺度比较小于 $2^{16}$。由于径向 $\mathcal C_0$ 逐 Fourier 模 unitary，它在所有 $H^s$ 上的 norm 准确为1；在本窗 $\|\mathcal G_a\|<4$。另外从 (A.6) 直接有
$$
 \|\mathcal G_a-\mathcal G_0\|_{H^s\to H^s}
 =\|\mathcal C_a-\mathcal C_0\|_{H^s\to H^s}.
 \tag{A.9}
$$

原真实 KAM 端角 $\theta=K_e(\eta)$ 没有设成恒等。正片篇 (C.3) 及同一相邻层包络给
$$
 k_e:=\|K_e-\mathrm{id}\|_{\mathcal A_{1/4}}
       +\|K'_e-1\|_{\mathcal A_{1/4}}
 <2^{100}J^2\delta^{-1}\mathcal N_j^{\rm pair}\mathcal X.
 \tag{A.10}
$$
因此其所需 $C^6$ 实导数远小于1。下面实际付一次导损；不声称 $C_{K_e^{-1}}-I$ 在同阶 norm 中小。

## 3. 从这组 Airy 状态恢复物理两迹

在一个根端点，令
$$
 \sigma_m=(1+(|m|/b)^{4/3})^{1/2},\quad
 W=\sigma(D)^{1/2},\quad
 V=(1+|D|^{4/3})^{1/4},\quad \alpha_0=b\mu_0.
$$
$\ell_0=\ell_{0,\xi}(0)$ 为原**参考** normal shear，$|\ell_0|<1/32$。令 $\varepsilon_e=\pm1$ 把正片 outward 通量换为负窗的材料正向 total 通量。由正片篇 (C.15)，真实物理平衡两迹 $\mathcal Z=(V\sqrt{\mu_0}h,V^{-1}\pi/\sqrt{\mu_0})$ 准确为
$$
 \boxed{\quad
 \mathcal T_K\binom{Y_h}{Y_p}=
 \binom{
 b^{-1/2}V C_{K^{-1}} W^{-1}Y_h
 }{
 \varepsilon_e b^{1/2}V^{-1}C_{K^{-1}}M_{1/K'}
       (WY_p-\tfrac12\ell_0W^{-1}Y_h)
 } .\quad}
 \tag{A.11}
$$
$M_{1/K'}$ 在 $\eta$ 中乘法，随后才按 $K^{-1}$ 复合。下行的 Jacobian 是通量**密度**的必需因子。全部 shear、符号和 mean 保留。这里没有插入实际 root frame，因而也没有重复支付它的 $r_e$ 因子。

记 $\mathcal T_0$ 为令 $K=\mathrm{id}$ 得到的 Fourier 对角 map。对 $|s|\le4$，
$$
 \|\mathcal T_K^{\pm1}\|_{H^s\oplus H^s},\
 \|\mathcal T_0^{\pm1}\|_{H^s\oplus H^s}
 <2^{100}\sqrt b,
 \tag{A.12}
$$
$$
 \|\mathcal T_K-\mathcal T_0\|_{H^{s+1}\oplus H^{s+1}
                                  \to H^s\oplus H^s}
 <2^{160}\sqrt b\,k_e.
 \tag{A.13}
$$
以下说明所用的完整 Sobolev 费用。$W^{\pm1},V^{\pm1}$ 的阶分别为 $\pm1/3$，且
$$
 1\le\frac{(1+|m|^{4/3})^{1/2}}{\sigma_m}\le b^{2/3},
 \qquad m\in4\mathbb Z,
$$
包含 $m=0$。故无角图时两个对角块及逆的 norm 至多 $2\sqrt b$；下左剪切再乘 $|\ell_0|/2<1/64$。

对 $H_\lambda=\mathrm{id}+\lambda(K^{-1}-\mathrm{id})$，逐个固定光滑输入有
$$
 C_{K^{-1}}-I=
 \int_0^1 M_{K^{-1}-\mathrm{id}}C_{H_\lambda}
                    \partial_\theta\,d\lambda .
 \tag{A.14}
$$
各 $H_\lambda$ 的导数在 $[1/2,2]$ 内。到六阶的链式法则、$6!4^6<2^{22}$ 和 inverse-map 的递推给所需乘法与复合 norm 小于 $2^{40}$，强差小于 $2^{80}k_e$；在分数阶用整数相邻阶插值，在负阶使用带真实 Jacobian 的 adjoint。两端只需 $s\pm1/3$ 和输入的一阶增量，最高正整数阶为6。将这些费用与上面的 Fourier 比例及三个非零块相乘，严格小于 (A.12)--(A.13)。没有把实平移的同阶差商当作 norm 导数。

由 (A.3)、(A.10)，可统一放宽成
$$
 \|\mathcal T_K^{\pm1}\|,\|\mathcal T_0^{\pm1}\|
 <F_j:=2^{120}J\delta^{-2},
$$
$$
 \|\mathcal T_K-\mathcal T_0\|_{H^5\to H^4}
 <2^{300}J^3\delta^{-3}\mathcal N_j^{\rm pair}\mathcal X.
 \tag{A.15}
$$
径向参考 map 的同一个界适用于任意 Sobolev 指数。

## 4. 到两个真实中心的有序比较

令 $\mathcal P_e$ 为第75束同一物理根到本负窗中心的完整 map，$\mathcal P_{0,e}$ 为同一当前 $\Gamma$ 的径向参考。先保两条完整状态，最后投去中心常物理高度的准确 null 槽；flux mean 留着。由该篇 (P.1)、(P.21)，相邻层统一后
$$
 \|\mathcal P_e^{\pm1}\|,\|\mathcal P_{0,e}^{\pm1}\|
 <2^{8100}J^{14}\delta^{-24},
$$
$$
 \|\mathcal P_e-\mathcal P_{0,e}\|_{H^5\to\mathscr H^4}
 <2^{12100}J^{22}\delta^{-40}\mathcal N_j^{\rm pair}\mathcal X.
 \tag{A.16}
$$
定义两个中心一起的 map
$$
 \mathcal B=\operatorname{pr}_{h_0=0}
     (\mathcal P_-\oplus\mathcal P_+)
     (\mathcal T_{K_-}\oplus\mathcal T_{K_+})\mathcal G_a,
 \qquad \mathcal B_0\text{ 为对应径向 map}.
 \tag{A.17}
$$
此投影只用于型的常高度商，不改变任一源或 mean 方程。它在中心显示的 Hilbert norm 中为收缩；对非零 Fourier 输入，径向参考输出本来没有 mean，故不损失其下界。

三项准确差式为
$$
 \begin{split}
 \mathcal B-\mathcal B_0=\operatorname{pr}_{h_0=0}\{&
 (\mathcal P-\mathcal P_0)\mathcal T_0\mathcal G_0\\
 &+\mathcal P(\mathcal T_K-\mathcal T_0)\mathcal G_0
 +\mathcal P\mathcal T_K(\mathcal G_a-\mathcal G_0)\}.
 \end{split}
 \tag{A.18}
$$
每个有导损的差的右侧都是完整径向 Fourier map；实际左因子只需已付的输出 $H^4$ 窗。故只有**一阶**输入角导损失。上述常数给
$$
 \|\mathcal B-\mathcal B_0\|_{H^5\to\mathscr H^4\oplus\mathscr H^4}
 <2^{12300}J^{23}\delta^{-42}\mathcal N_j^{\rm pair}\mathcal X.
 \tag{A.19}
$$
三项未放宽的二进制次数至多12221、8401、8421。

设 $a_0=0$。因为参考 graph 有 (A.7)，并且 $\mathcal P_0,\mathcal T_0$ 可逆，
$$
 \|\mathcal B_0a\|_{\mathscr H^0\oplus\mathscr H^0}
 \ge K_j^{-1}\|a\|_2,
 \qquad K_j=2^{8300}J^{15}\delta^{-26}.
 \tag{A.20}
$$
同时 $\|\mathcal B\|_{H^4\to\mathscr H^4\oplus\mathscr H^4}<K_j$。不对一个端点单独使用 (A.20)：真实传输允许某端数据很小，故两个端点必须一起计量。

## 5. 真 incoming 低包的完整中心定位

现在仅对 incoming 要求
$$
 a_m=0\quad\text{当 }m=0\text{ 或 }|m|>L_0.
 \tag{A.21}
$$
两个端点内的所有 $4\le|m|\le L_0$、两实分量及两端比例均任意；outgoing 不作任何截断。因为 $1+L_0<\sqrt{B_{\max}}$，
$$
 \|a\|_{H^5}\le B_{\max}^{5/2}\|a\|_2
 <2^{25}J^3\delta^{-4}\|a\|_2.
$$
写 $Z=\mathcal Ba$，在各中心按其**自身** $\Pi_e$ 分成 $Z_<,Z_>$。径向参考 $\mathcal B_0a$ 准确支持于各自低锥内。由 (A.19)，
$$
 \|Z-\mathcal B_0a\|_{\mathscr H^4\oplus\mathscr H^4}
 <D_j\|a\|_2,
 \quad D_j=2^{12400}J^{26}\delta^{-46}
                   \mathcal N_j^{\rm pair}\mathcal X.
 \tag{A.22}
$$
实际 $K_jD_j<1/2$，故
$$
 \|Z_<\|\ge(2K_j)^{-1}\|a\|_2,
 \qquad
 \frac{\|Z_>\|_{\mathscr H^4\oplus\mathscr H^4}}{\|Z_<\|}
 <2^{20800}J^{41}\delta^{-72}
                         \mathcal N_j^{\rm pair}\mathcal X.
 \tag{A.23}
$$
因此真正全频中心像满足
$$
 \boxed{\quad
 \|Z_>\|_{\mathscr H^4\oplus\mathscr H^4}
 <2^{-12800}J^{-42}\delta^{38}\|Z_<\|.
 \quad}
 \tag{A.24}
$$
最后一步的完整误差比是
$2^{33600}J^{83}\delta^{-110}\mathcal N_j^{\rm pair}\mathcal X$。
首层二进制指数小于 $-130000$，其后每层再下降超过14 bits：使用
$\delta_{8193}^{-1}<2^{8197}$、$J_{8193}<2^{14}$、
$(8199/8198)^{83}<65/64$、$(65/64)^{32}<2$ 和
$\alpha-110-1/32>14$。实际无限输出、相反锥和 flux mean 回填全在 (A.24) 左侧。

## 6. 两个已付负窗型在这个真实像上的正性

对每个窗口仍使用其第74束自己的共同方向 $\psi_e$、当前联合 $\Gamma^*$ 和整个负窗型。只定义
$$
 \mathfrak P(Z)=\mathfrak G_{I_-,\psi_-}(Z_-)
                         +\mathfrak G_{I_+,\psi_+}(Z_+).
 \tag{A.25}
$$
它是两个已证 Hermitian 型之和；这一定义没有删除它们各自已经包含的完整参数响应。

该篇 (E.22) 对两者各自成立。由 $\rho_e=2^{-1024}J_e^{-8}$、$a_e=\delta_e^{3/2}/(8\sqrt6)$、$J_e\le2J$ 和 $\delta_e\ge\delta/2$，统一可取
$$
 d_e> d_*:=2^{-9100}J^{-64}\delta^5,
 \qquad
 D_e<D_*:=2^{16300}J^{20}\delta^{-71}.
 \tag{A.26}
$$
例如 $d_e=2^{-800}\rho_e^8a_e^3$，不含一个未知 $B_e$ 比值；$D_e=2^{16152}J_e^{20}\delta_e^{-71}$。因而
$$
 \mathfrak P(Z)\ge\frac{d_*}{8}\|Z_<\|^2
                    -D_*\|Z_>\|_{\mathscr H^4\oplus\mathscr H^4}^2.
$$
(A.24) 中阈值的平方满足
$$
 D_*\big(2^{-12800}J^{-42}\delta^{38}\big)^2
                         =2^{-200}d_*<d_*/16.
$$
再用 (A.23)，得
$$
 \boxed{\quad
 \mathfrak P(\mathcal Ba)
 >2^{-25800}J^{-94}\delta^{57}\|a\|_2^2 .
 \quad}
 \tag{A.27}
$$
这里真正使用了正片完整 outgoing 的无限输出，未要求两条实际根迹有限支撑。常物理高度与型的所有交叉项准确为零；这仍不是删除有源 mean 方程。

## 7. 独立 incoming mean 与全部正片源

允许完整 $a=a_\perp+a_0$，其中 $a_\perp$ 满足 (A.21)，两个端点的 $a_0$ 不作限制。正片含 ordinary/weak 源时，完整关系是
$$
 b=\mathcal C_a a+g_{\mathcal F}.
$$
用原准确 Piola 后的 $\widehat s,\widehat F$，定义
$$
 \mathcal S_4=
 C_I\sqrt{4+\Lambda_I^2}\|\widehat s\|_{L^1_tH^4}
                       +2\|\widehat F\|_{\mathscr E_0^{*,4}},
 \qquad \mathcal R_4=\|a_0\|_2+\mathcal S_4.
 \tag{A.28}
$$
全部 $C_I,\Lambda_I$、$\mu_0^{-1}$、$(A\mu_0)^{-1}$ 和 ordinary 源的实际 $w_{\rm ref}^2$ 因子，严格按正片篇 (C.25)--(C.33) 读取。该篇已证 $\|g_{\mathcal F}\|_{H^4}<2^{60}\mathcal S_4$。

源增加的 graph 两行恰为 $(g_{\mathcal F}/\sqrt2,g_{\mathcal F}/(i\sqrt2))$，其 norm 为 $\|g_{\mathcal F}\|$。因此实际两中心有准确分解
$$
 Z=\mathcal Ba_\perp+Z_{\rm aff},\qquad
 \boxed{\quad
 \|Z_{\rm aff}\|_{\mathscr H^4\oplus\mathscr H^4}
 <2^{8360}J^{15}\delta^{-26}\mathcal R_4 .\quad}
 \tag{A.29}
$$
这是当前实际正片源到两个真实中心的完整单位转换。没有把 weak 体源 norm 当作裸通量的端点迹，也没有令 outgoing mean 为零。真实守恒式仍为
$\langle q_-+q_+\rangle=\int_I\langle\widehat s\rangle dt$；负窗中的高度和 flux mean 按各自准确方程继续传播。

若只在正片有这些源，而相邻负窗使用从此中心数据出发的齐次延拓，(A.25) 还有一个明确的有源下界。第74束的完整连续型给
$$
 |\mathfrak P(Z,W)|\le
 C_*\|Z\|_{\mathscr H^4\oplus\mathscr H^4}
       \|W\|_{\mathscr H^4\oplus\mathscr H^4},\qquad
 C_*=2^{3600}J^{-24}\delta^{-30}.
$$
由 (A.2)、(A.20)，$\|\mathcal Ba_\perp\|_{\mathscr H^4\oplus\mathscr H^4}
<2^{8400}J^{17}\delta^{-29}\|a_\perp\|$。把全部交叉项用一次 Young 不等式保留，得到
$$
 \boxed{\quad
 \mathfrak P(Z)
 \ge2^{-25801}J^{-94}\delta^{57}\|a_\perp\|_2^2
          -2^{66600}J^{110}\delta^{-227}\mathcal R_4^2 .
 \quad}
 \tag{A.30}
$$
源不必低频或解析，所需且仅使用的是 (A.28) 的原真实 $H^4$ 体源合同。若负窗本身也有 ordinary/weak 源，其有序 Duhamel 列和所有 normal charge 必须再加；本篇未给那些列填0。

## 8. 尚未授予的整个网络量词

(A.27) 是实际正片 graph 的低 incoming 子空间经过真实端角和两条物理迹后的结果，比人为要求两条 Cauchy 迹有限支撑更强。但是任意 whole-network 近核的 incoming 仍可能具有带外成分，不能由本篇反向断言其满足 (A.21)。

另外，沿同时打开两个控制的真实方向，整个网络型还包含：(i) 每个控制在另一个负窗中的非局部背景与 $D\Gamma^*$ 响应；(ii) 正片本身的完整参数型；(iii) 其余相邻块和最外端条件。本文的 (A.25) 不是这些项的缩写。若在 KAM/Airy 端口微分，还必须把两端角图的一阶导和 normal shear 导数按原 symplectic 规范接入，不能因已经证明一个固定参数的 packet map 而删除它们。

新得到的 (A.19)、(A.24)、(A.29) 可以直接作为这一步的真实接口；原 $\zeta,h,b_m$、原 incoming 权和 source 单位均未修改。本篇没有宣布全非径向网络逆、原 source-to-label 同权逆或非线性 $\mathcal F=0$ 成立。

新增精确公式与预算见
[源码](../scripts/fourfold_positive_Cayley_packet_centers_20261114.py)、
[实际记录](../notes/2026-11-14-R119-positive-Cayley-packet-center-budget.json)。

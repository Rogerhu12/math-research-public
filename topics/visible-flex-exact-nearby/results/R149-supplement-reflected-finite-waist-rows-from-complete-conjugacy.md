# R149 补篇：真实反射 target 的有限腰行与完整共轭 DFT 载体

2026-11-26，visible-exact-astra-198c63d-20261126 / correlated_energy。

**已证明的解析结论。** 原真腰 normalizer 的双侧高投影使每个低于固定 $J_s$ 的有限 Fourier row trial 在完整 adjoint 下精确保持不变。因此，首批96个真实反射腰行可以直接从已成 $G=K_{48}\circ H_{\rm fin}$ 构造；所需余项只有同一个真实共轭的完整旧误差以及新有限 DFT 的全部 truncation/alias 误差。没有重新求 KAM，也没有把复合映射误当作有限 Fourier 多项式。

本篇先精确定义实际 target 行、精确 trial 及可执行的 private carrier。尚未进行新科学执行或得到 signed PDE columns。原 positive224、真正完整 inverse、$\Theta_{96}$、target $\mathcal B^{-1}$、所有交叉块和 bordered Schur 不由本篇补齐。

纯算法为 [fourfold_codazzi_reflected_waist_row_trials_math.py](../scripts/fourfold_codazzi_reflected_waist_row_trials_math.py)。它没有 IO，也不导入或调用旧 producer。

## RW1. 同一 selected lift 和实际96个 target 行

使用 [W](R133-supplement-actual-physical-Wiener-conjugacy-strip.md) 唯一 selected pair：run43588332723/1、loss $1/250$，同一 $Q_0,Z,\eta_0$。原角周期为 $\ell=\pi/2$，measure 为 normalized circle，频率为 $4j$。

[RRF.17–18](R133-supplement-true-reflection-rigidity-and-selected-waist-target.md) 已证明
$$
R_a f(x)=f(a-x),\qquad
a=2\mathcal H(0),\qquad
\mathcal H(-\phi)+\mathcal H(\phi)=2\mathcal H(0).
\tag{RW.1}
$$
所以真正物理 primitive target 是
$$
Y_a^0=P\operatorname{Fix}(R_a)\cap L^2,\qquad P=1-\Pi .
$$
对其原 cutoff97 的96个低 target 坐标，取实际正交归一行
$$
g_j(x)=\sqrt2\cos\!\bigl(4j(x-a/2)\bigr),\qquad j=1,\ldots,96 .
\tag{RW.2}
$$
这是 $Q_{97}Y_a^0$ 的完整实正交基。$a$ 没有设成零，也没有用 approximate phase 替换。它们不是 source 的96个 root-even 坐标，也不是 transported $\Theta$ 行。

令
$$
\psi(\phi)=\mathcal H(\phi)-\mathcal H(0),\qquad
f_j(\phi)=g_j(\mathcal H(\phi))
          =\sqrt2\cos(4j\psi(\phi)).
\tag{RW.3}
$$
$\psi$ 是真实 odd degree-one lift，$f_j$ 是完整 real even function。它在原 moving 圈上的 mean $\Pi f_j$ 一般非零。target 上 $\Pi g_j=0$ 不意味着 pullback 后的 mean 为零。

原 density convention $U_Xf=X'(f\circ X)$ 给
$$
U_{\mathcal H^{-1}}^*g_j=g_j\circ\mathcal H=f_j .
\tag{RW.4}
$$
这里是同一 normalized $L^2$ 的 adjoint，不附加一个 Jacobian，也不更换 measure。

## RW2. 两个 normalizer 因子的有限补空间精确恒等式

[WTA.6–7](R133-supplement-actual-right-waist-normalizer-and-complete-two-window-inverse.md) 的实际固定对象为
$$
T_{J_s}=(1+P_{J_s}SIP_{J_s})(1+P_{J_s}S_2I^2P_{J_s}),
\qquad J_s=268435456 ,
$$
$$
\widehat T_0=\operatorname{diag}(T_{J_s},1_{\mathbb R^2})
\quad\hbox{在 }\mathcal Y_0=L^2_0(\mathbb T;\mathbb R^2)\oplus\mathbb R^2 .
\tag{RW.5}
$$
$I=\partial_\phi^{-1}P$。两个因子保持原次序，两个 independent density mean 保持 identity。不是改用 WTA 另一个已成的 $97$ 或 $512$ 截断。

令 $E_N$ 为两 primitive 分量的 $|k|\le N$ Fourier 投影和全部两 mean。只要 $N<J_s$，双侧 $P_{J_s}$ 逐个给
$$
\widehat T_0E_N=E_N,\quad E_N\widehat T_0=E_N,\quad
\widehat T_0^*E_N=E_N .
\tag{RW.6}
$$
由同一个已成有界逆还有
$$
\widehat T_0^{-1}E_N=E_N,\qquad
\widehat T_0^{-*}E_N=E_N .
\tag{RW.7}
$$
这不要求 $S,S_2$ 有有限 Fourier 支集；两个 multiplier 中的全部系数和 tail 都由先作用的相邻投影精确消去。它只适用于声明的有限 trial，不把完整 $f_j$ 的高频尾置零。

## RW3. 从完整 $G$ 得到不改变真实 phase 的 odd trial

W.4 对同一 selected lift 给
$$
G=K_{48}\circ H_{\rm fin},\quad
\|\mathcal H-G\|_{\mathcal A_\sigma}\le E_H,\quad
\|G-\operatorname{id}\|_{\mathcal A_\sigma}\le G_0,\quad
\sigma=1/128 .
\tag{RW.8}
$$
$E_H,G_0$ 必须读取完整 W native 中 selected 的旧球和原 whole $G$ 球。识别用的旧上端分别约为 $2.210026409642\,10^{-7}$ 和 $0.003469118991384$；实际消费者不把这些显示数字代替原件。

定义一个新的 explicit compound lift
$$
G_o(\phi)=\frac{G(\phi)-G(-\phi)}2 .
\tag{RW.9}
$$
它的周期部分是原 $G-\operatorname{id}$ 的 odd projection。由 (RW.1)，$\psi$ 正是 $\mathcal H$ 的 odd lift，因此
$$
\|\psi-G_o\|_{\mathcal A_\sigma}\le E_H,\qquad
\|G_o-\operatorname{id}\|_{\mathcal A_\sigma}\le G_0 .
\tag{RW.10}
$$
证明是 Fourier 上 odd projection 的 $\mathcal A_\sigma$ 收缩性。这里没有分别减去两个独立 pointwise 误差，因而不需另乘2；保留的是原真实 phase，而不是把 $\mathcal H$ 重新选成另一个 KAM 解。

设
$$
v_j(\phi)=\sqrt2\cos(4jG_o(\phi)).
$$
真实实轴上的 cosine Lipschitz 界、$\mathcal A_\sigma\hookrightarrow L^2$ 给
$$
\|f_j-v_j\|_2\le4\sqrt2\,j E_H .
\tag{RW.11}
$$
Banach algebra exponential 估计同时给全部 Fourier 系数的完整上界
$$
\|v_j\|_{\mathcal A_\sigma}
 \le B_j:=\sqrt2\exp\!\bigl(4j(\sigma+G_0)\bigr).
\tag{RW.12}
$$
这包含 $G$ 的整个复合尾和所有 mean。没有把 $K_{48}\circ H_{\rm fin}$ 截为无余项的有限多项式。完整 $H_{\rm fin}$、$K_{48}$ 的所有 exact rational sine/cosine coefficients 由原 root contract 和同 run43586895661 的 K48 native 读取，不重新拟合。

## RW4. 固定精确定义的有限 DFT row trial

这一次新目标固定
$$
L=4096,\quad N=1024,\quad \phi_\ell=\frac{\ell\pi}{2L},
\qquad 0\le\ell<L,\qquad 2N<L,\quad N<J_s .
\tag{RW.13}
$$
对每个 $j=1,\ldots,96$，定义 exact finite sums
$$
c_{j,k}^{[L]}=\frac1L\sum_{\ell=0}^{L-1}
 v_j(\phi_\ell)e^{-2\pi i k\ell/L},\qquad |k|\le N,
$$
$$
p_j(\phi)=\sum_{|k|\le N}c_{j,k}^{[L]}e^{i4k\phi}
       =c_{j,0}^{[L]}+2\sum_{k=1}^{N}c_{j,k}^{[L]}\cos(4k\phi).
\tag{RW.14}
$$
由于 $v_j$ real even，全部 $c_{j,k}^{[L]}$ 是 real，且 $c_{j,-k}^{[L]}=c_{j,k}^{[L]}$。式 (RW.14) 才是 trial 的对象定义。Arb interval、显示精度或后来重新物化的 interval midpoint 都不改变该对象；程序不把 interval midpoint 当作一个新 trial。

由 odd degree-one 和周期性，$G_o(0)=0$、$G_o(\ell/2)=\ell/2=\pi/4$。因此 base cosine $\cos(4G_o)$ 在网格 index0 与 $L/2$ 的精确值分别为 $1,-1$；这不是令原 $\mathcal H(0)=0$。

所有 exact sample values 来自完整 compound evaluation：
$$
G(\phi)-\phi
 =h(\phi)+k(\phi+h(\phi)),\qquad
H_{\rm fin}=\operatorname{id}+h,\quad K_{48}=\operatorname{id}+k .
\tag{RW.15}
$$
原两 finite coordinate 的常数项也属于对象定义。本例原 `fourfold_codazzi_phase_full_transport_Taylor.py::initial_state` 先置全部 $2M+1$ 个零 coefficients，只在 $j\ge1$ 的 $M\pm j$ 槽写入原24组 H coefficients，所以 $h$ 的 constant translation 准确为0。原 `fourfold_codazzi_phase_terminal_postcomposition.py` 定义 $K_{48}=\operatorname{id}+\sum_{j=1}^{48}(a_j\sin4jx+b_j\cos4jx)$；proposal 的最后一个标量是 terminal rotation，不是 K 的 constant translation。其完整 native/source 和原 W 的 G 识别必须同时准入。新 pure API 仍显式传入 $h_0,k_0$，在 $k(\phi+h)$ 内保留 $h_0$，owner 才依据这些原定义严格核本例 $h_0=k_0=0$；不得仅凭字段不存在推断0。

分别保留 $\phi$ 与 $-\phi$ 两个值，再按 (RW.9) 形成同一个 odd lift。用 $T_j(\cos t)=\cos jt$ 的 exact recurrence 生成全部96个 modes，只改变运算方法，不改变 (RW.14)。FFT 的每个 butterfly 都用有向 ball arithmetic 包围 exact finite sum。

完整 alias identity 为
$$
c_{j,k}^{[L]}=\sum_{m\in\mathbb Z}\widehat v_j(k+mL).
\tag{RW.16}
$$
绝对收敛由 (RW.12) 保证。所有 $|k|\le N,m\ne0$ 的 indices 都满足 $|k+mL|\ge L-N$；因 $2N<L$，每个 index 最多被一个 such pair 使用。故
$$
\|Q_Nv_j-p_j\|_2
 \le B_j e^{-4\sigma(L-N)},\qquad
\|(1-Q_N)v_j\|_2\le B_j e^{-4\sigma(N+1)} .
\tag{RW.17}
$$
这里先用 Fourier $\ell^1$ 支配 $L^2$，再用完整 Wiener 权。既没有漏掉 alias，也没有重复计算一个无限 geometric series。于是明确完整误差为
$$
\boxed{\quad
\|f_j-p_j\|_2\le
\epsilon_j:=
4\sqrt2\,jE_H+
B_j\left(e^{-4\sigma(N+1)}+e^{-4\sigma(L-N)}\right).
\quad}
\tag{RW.18}
$$
数值执行必须使用原 saved upper 和这次所有方向正确的新 upper；不得把中点小误差当上界。

## RW5. 同一个 scalar trial 给 incoming 和真实 primitive 两种行

对 scalar function $f$ 定义完整 isometric injection
$$
\iota_+f=(Pf,0;\Pi f,0)\in\mathcal Y_0.
$$
它就是 WY.5 的 $\mathscr J_+^*$，包括其原角 mean。

### Incoming 的96个声明型观测

这96个 exact functional 是
$$
\ell_j^{\rm in}(Y)=
 \langle g_j,U_{\mathcal H^{-1}}\mathscr J_+
                     \widehat T_0^{-1}Y\rangle,\qquad
z_j^{\rm in}=\widehat T_0^{-*}\iota_+f_j .
\tag{RW.19}
$$
它们只是完整 incoming 的这96个 reflected cosine test rows，不是所有 incoming rows。令
$z_{j,\rm app}^{\rm in}=\iota_+p_j$。由 (RW.6)，
$$
\hbox{完整 adjoint residual 为 }
\iota_+f_j-\widehat T_0^*z_{j,\rm app}^{\rm in}
 =\iota_+(f_j-p_j),
$$
$$
\|z_j^{\rm in}-z_{j,\rm app}^{\rm in}\|
 \le K_{W,0}\epsilon_j,\qquad
\|\ell_j^{\rm in}\|\le B_{H,0}K_{W,0}.
\tag{RW.20}
$$
$K_{W,0}$ 是原 **固定 $J_s$** inverse，$B_{H,0}$ 是原 selected inverse-density 左范数。任何右 $N_i$、$K_\Lambda$、source normalizer 都不加入此行。

### 原 physical primitive target 的完整96个低行

WUE.28 的真实 normalized physical primitive observation 为
$$
\mathcal L_\partial
 =\frac12U_{\mathcal H^{-1}}e^TQ_{R,y}\pi_y,\quad
e=(1,1)^T,\quad Q_{R,y}=\frac{1+ER}{2}.
\tag{RW.21}
$$
$\pi_y$ 只取两个 nonmean primitive 分量。因 $f_j$ even，$Q_{R,y}(f_j,f_j)=(f_j,f_j)$，所以
$$
\ell_j^\partial(Y)=\langle g_j,\mathcal L_\partial Y\rangle,\quad
z_j^\partial=\tfrac12(Pf_j,Pf_j;0,0),
$$
$$
z_{j,\rm app}^\partial=\tfrac12(Pp_j,Pp_j;0,0),\qquad
\|z_j^\partial-z_{j,\rm app}^\partial\|
 \le\frac{\epsilon_j}{\sqrt2},\qquad
\|\ell_j^\partial\|\le\frac{B_{H,0}}{\sqrt2}.
\tag{RW.22}
$$
这里两个相同 primitive 分量的 Hilbert norm 精确给 $1/\sqrt2$；不是以两个 arbitrary outputs 正交为由减费。这个物理行无需另撤销 $\widehat T_0$。$z_j^\partial$ 的 mean entries 为零来自原 $\pi_y$ 的确切定义，不代表真解的 density mean 为零。

两条完整 density mean observations
$$
m_+(Y)=z_+,\qquad m_-(Y)=z_-
\tag{RW.23}
$$
仍分别保留，row norm 为1。它们不被 (RW.22) 合并或删除；其与实际 physical mean matching equations 的转换仍按原完整问题付费。

## RW6. 未来 signed columns 的直接消费与有限 trial 的额外消去

对 SC 的同一完整 column，若 $\|Y_k-Y_{k,\rm app}\|\le D_k$，则两种 trial 的有符号配对均用原实 Hilbert inner product，primitive Fourier coefficients 与两 mean 一起相加。令 $\varepsilon_{{\rm eval},jk}$ 包围 finite evaluation 的数值误差，得
$$
|\,\ell_j^{\rm in}(Y_k)
 -\langle\iota_+p_j,Y_{k,\rm app}\rangle\,|
\le B_{H,0}K_{W,0}D_k+
 K_{W,0}\epsilon_j\|Y_{k,\rm app}\|
 +\varepsilon_{{\rm eval},jk},
\tag{RW.24}
$$
$$
|\,\ell_j^\partial(Y_k)
 -\langle z_{j,\rm app}^\partial,Y_{k,\rm app}\rangle\,|
\le \frac{B_{H,0}D_k+
 \epsilon_j\|Y_{k,\rm app}\|}{\sqrt2}
 +\varepsilon_{{\rm eval},jk}.
\tag{RW.25}
$$
如果同一 $Y_{k,\rm app}$ 也完全位于 $|k|<J_s$ 的 finite primitive-plus-mean 空间，(RW.7) 允许把 (RW.24) 第二项中的 $K_{W,0}$ 精确换成1：
$$
\langle z_j^{\rm in},Y_{k,\rm app}\rangle
 =\langle\iota_+f_j,\widehat T_0^{-1}Y_{k,\rm app}\rangle
 =\langle\iota_+f_j,Y_{k,\rm app}\rangle .
\tag{RW.26}
$$
第一项仍使用真正完整 receiver $B_{H,0}K_{W,0}$，不能随 trial 的消去而一起缩小。所有 PDE/source/true-root/positive/high/mean errors 仍在 $D_k$；本篇不从 body $L^2$ 取 trace。

这96个 physical primitive test rows 属于 **原 $\mathcal L_\partial$ 的 target**。WGB/WBP 的 target $\mathcal B^{-1}$ 若尚未作用，不能把本篇矩阵改名为已完成的 WGB matrix。其 adjoint rows、transported $\Theta_{96}$、高块消去和真 $\nu$/phase/physical mean rows仍独立。本篇也没有构造 rotated outgoing row；其精确 adjoint 必须保原旋转，不能免费复用一个未旋转 cosine row。

## RW7. 执行边界、完整保存与可复用载体

新的独立科学目标为：所有96个 (RW.14) 的完整 coefficient carriers 及对应的完整 (RW.18)、(RW.20)、(RW.22) 误差。执行可以不等 R142/positive224，因为其输入只是已成 W/WTA/WX 和同一完整 H/K 原件；真正 PDE 列仍等其完整 inverse 前置。

每个新 row 必须：

1. 完整计算 $N+1=1025$ 个 real cosine coefficients（含 $k=0$）；其负频由已证 even identity 精确确定。
2. 保存 private 全 row carrier，逐项读回并核该 ball 仍包含最初有向 coefficient ball，然后为整件产生 bytes/SHA256。全 row 不以只存某些 modes 的 hash 替代。
3. 将该 row 的完整 signed mean coefficient、Parseval trial norm upper 和三条新误差 upper 连同 exact definition identity 写成 candidate；整件读回验证后才增加 completed-row prefix。
4. 后继只用正式保存的 upper 组合数值。整个96-row目标未成时，prefix 不赋予完整 head 或 finite inverse。

新大 coefficient arrays 属于可重建 private temporary carrier，不提交仓库、artifact 或 Release；公开只存完整数量、每个完整 row 的 hash、小结论球、源/参数及实际 run。后继真正列计算按同一 (RW.14) 物化必要输入，不重新支付或替换这些已成误差；不得从 midpoint 另选 row，也不得声称载体物化又证明了一次旧科学。

原 root contract SHA256 为
`1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43`；
同 run43586895661 的完整 K48 为
`a44d6a6b2d0bad07d60e323142fd266b8dd91a645afa9d306fe22c8794a84f60`；
W strip native 为
`dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854`。
实际 owner 必须连同它们原 process/manifest/publication 和全部 qualification 读取，科学只在公共 Actions。这里只证明公式及给纯算法，不把准备的定义标为已计算。

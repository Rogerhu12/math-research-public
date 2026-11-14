# R119 续篇：完整自由 Airy 两行端架、低频勘误与原总账的修复

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇保留原 Airy 的两个输入列、完整法向导数、
normal shear、两个 mean 和右根方向，证明自由根端架本身满足

$$
\boxed{\quad
\|\Phi_b^{\pm1}\|_{H^s\to H^s}<2^{64}b,
\qquad
\|\Phi_b-\Phi_b^{(1)}:H^s\to H^{s+g}\|<2^{64}b^g,
\quad g\in\{4/3,2\}.
\quad}
\tag{A.1}
$$

逆端架减去逆模型有同一个强范数界。所有实数 $s$ 均可，因为本篇
对象是完整 Fourier 对角的两行端架；这不是对非径向演化逐模化。

第51束第4节在 (H.17) 前写出的自由端架同阶界
$2^{16}b^{1/2}$ **不能用于所有低非零频率**。该句须以 (A.1)
第一式替换，原冻结文件及其 SHA 不变。第5节重新支付该篇显示的
(H.17) 三个宽界，所以以那三个显示界为输入的旧 (H.22)、(H.1)
及旧高网络阈值仍成立；不能继续以那句错误的中间界作独立依据。
本篇不声称新的完整负段散射或新的高网络阈值已经完成。

## 1. 同一个原基和准确的两行映射

仍取 $m\in4\mathbb Z$、$H=1/64$、$b>1$，并用物理 Sobolev 权
$\langle m\rangle=(1+m^2)^{1/2}$。对 $m\ne0$，记
$M=|m|$、$\kappa=M/b$。原 R39 的归一常数和两列为

$$
c_A=-\operatorname{Ai}'(0)/\operatorname{Ai}(0),\qquad
c=c_A^{-1/2},\qquad
Y_\sigma(z)=\operatorname{Bi}(-z)+i\sigma\operatorname{Ai}(-z),
$$
$$
D_{\sigma,m}(\xi)=c\kappa^{-1/3}Y_\sigma(\xi\kappa^{2/3}),
\qquad
D'_{\sigma,m}(\xi)=c\kappa^{1/3}Y'_\sigma(\xi\kappa^{2/3}).
\tag{A.2}
$$

prime 在 $Y$ 上是对其整个实变量 $z$ 求导，在 $D$ 上是对真实
$\xi$ 求导。mean 仍准确使用

$$
D_{\sigma,0}(\xi)=c(1+i\sigma\xi/\pi),\qquad
D'_{\sigma,0}=i\sigma c/\pi.
\tag{A.3}
$$

记 $F_m$ 为由 $D_+,D_-$ 和完整导数形成的 $2\times2$ 矩阵。
[R39 (3.4)](R39-finite-component-airy-transfer-input.md) 给出每个
$m$ 包括0的准确行列式

$$
\det F_m=-2ic^2/\pi.
\tag{A.4}
$$

在 $\xi=H$，原密度高度及其沿向内光学变量的导数为

$$
w={H^{1/4}\over\sqrt b}\,u,
\qquad
\zeta=\sqrt b H^{-1/4}\left(u_\xi+{u\over4H}\right).
\tag{A.5}
$$

这是[实际完整径向返回 (N.12)](R119-supplement-actual-complete-radial-return-first-phase.md)
的完整两行式。在右根转到向物理 $t$ 增加的方向时，另乘原准确
交换矩阵 $P=(0,1;1,0)$，不把这个方向号藏入余项。

在非mean模上定义严格 wave 振幅 $a_+,a_-$，恰使

$$
w={c\over\sqrt\pi}M^{-1/2}(a_++a_-),\qquad
\zeta={ic\over\sqrt\pi}M^{1/2}(a_+-a_-).
\tag{A.6}
$$

因此 $\Phi_{b,m}$ 从原 Airy 幅度 $(z_+,z_-)$ 映到 $(a_+,a_-)$，
其第一行对任意两迹 $(u,u_\xi)$ 准确为

$$
a_+={\sqrt\pi\over2c}\left[
 \kappa^{1/2}H^{1/4}u
 -i\kappa^{-1/2}H^{-1/4}
                    \left(u_\xi+{u\over4H}\right)\right],
\tag{A.7}
$$

第二行只把 $-i$ 改为 $+i$。代入 (A.2)，其三种系数正是

$$
\kappa^{1/6}H^{1/4}Y_\sigma,\qquad
\kappa^{-1/6}H^{-1/4}Y'_\sigma,\qquad
{\kappa^{-5/6}\over4H^{5/4}}Y_\sigma.
\tag{A.8}
$$

特别最后一项不能在低频删除。原归一常数 $c$ 在这些完整矩阵
条目中准确消去。

对 mean，(A.6) 中的 $M^{\pm1/2}$ 均取1，使用 (A.3) 和 (A.5)
定义同一两个独立振幅。这只是一个固定有限维两态坐标，没有对0
代入 $1/m$。

## 2. 精确 Green 恒等式同时控制逆架

(A.5) 从 $(u,u_\xi)$ 到 $(w,\zeta)$ 的实矩阵行列式是1。
(A.6) 从幅度到两迹的矩阵同样具有行列式 $-2ic^2/\pi$，mean
取1时也成立。两者都保持同一个 Hermitian Green pairing。因此
令 $\mathsf J=\operatorname{diag}(1,-1)$，准确有

$$
\Phi_{b,m}^*\mathsf J\Phi_{b,m}=\mathsf J,
\qquad
\Phi_{b,m}^{-1}=\mathsf J\Phi_{b,m}^*\mathsf J.
\tag{A.9}
$$

这里满射来自 (A.4) 的非零行列式，不是从一个支块的下方界猜测。
所以每模的逆架 norm 与正架相等。后面模型是普通酉且与
$\mathsf J$ 交换；因而也准确有

$$
\Phi_{b,m}^{-1}-(\Phi_{b,m}^{(1)})^{-1}
 =\mathsf J(\Phi_{b,m}-\Phi_{b,m}^{(1)})^*\mathsf J.
\tag{A.10}
$$

对本篇 Fourier 对角对象，乘输出 Sobolev 权后每模的矩阵 norm
仍相等。逆强余项不需要再乘低频端架条件数。

## 3. 全部低模和真正的低频增长

[R39 引理2.1](R39-finite-component-airy-transfer-input.md) 的完整
实轴界及其初值证明给出 $\operatorname{Ai}(0)$、
$\operatorname{Bi}(0)$ 及二者导数的绝对值小于1。
在 $0\le z\le4$，方程 $Y''+zY=0$ 的一阶系统满足

$$
\|(Y,Y')(z)\|_2
 \le \exp\!\left(\int_0^4\max(1,t)\,dt\right)
             \|(Y,Y')(0)\|_2<2^{15}.
\tag{A.11}
$$

这是直接的有限区间能量上界，远比实际函数值宽。对
$0<\kappa\le2^{12}$，确有 $0\le H\kappa^{2/3}\le4$。
由 (A.8)、$H^{-1/4}<4$、$1/(4H)=16$，逐项相加并付两行
矩阵 norm，得到充分的共同门

$$
\|\Phi_{b,m}\|_2<2^{32}\max(1,\kappa^{-5/6}),
\qquad 0<\kappa\le2^{12}.
\tag{A.12}
$$

对 $\kappa<1$，三种幂均被 $\kappa^{-5/6}$ 控制；对
$1\le\kappa\le2^{12}$，唯一增大的幂是
$\kappa^{1/6}\le4$。因此没有在 (A.12) 中遗漏一段中频。

旧 $b^{1/2}$ 断言的失效也直接可见。固定任一非零物理频率
$M$，令 $b\to\infty$；则 $\kappa\to0$，而
$Y_\sigma(0)\ne0$。由 (A.7)–(A.8)，例如第一行第 $\sigma$ 列
有准确非零极限

$$
\lim_{\kappa\downarrow0}\kappa^{5/6}
               (\Phi_{b,m})_{+\sigma}
 =-{i\sqrt\pi\over8H^{5/4}}Y_\sigma(0)\ne0.
\tag{A.13}
$$

所以这些条目增长为常数乘 $b^{5/6}$，不能用任何固定常数乘
$b^{1/2}$ 控制。实际根斜率随层号无界，故这不是只存在于未用
参数范围的形式反例。mean 自身仍仅需 $\sqrt b$；错误在于把
这个 mean 费用授予所有低非mean列。

## 4. 完整首模型及全频强界

定义非mean处的模型

$$
\Phi_{b,m}^{(1)}=
 \operatorname{diag}(e^{i\psi(\kappa)},e^{-i\psi(\kappa)}),
\qquad
\psi(\kappa)={2\over3}\kappa H^{3/2}+{\pi\over4}
                          -{5\over48H^{3/2}\kappa},
\tag{A.14}
$$

mean 上模型取 $I_2$，只用于表示主加首模型，实际 mean 两态仍为
(A.3)–(A.7)。这是原首相位，含真实 $-5/48$ 号；没有改变参数
选择中已经固定的首密度平均。

[R46 §8 (8.1)–(8.5)](R46-strict-negative-cauchy-phase-and-strong-remainder.md)
对 $Z=t^{1/4}Y_\sigma(t)$ 及其完整导数给同一个终端 Volterra
余项 $1/(4\eta^2)$，$\eta=2t^{3/2}/3$。在 (A.5) 中
$u/(4H)$ 恰消自由幅度的导数项，余下相位导数的一阶项也包含在
(A.14) 中。按[实际径向返回 (N.12)–(N.14)](R119-supplement-actual-complete-radial-return-first-phase.md)
的两行重组，得到

$$
\|\Phi_{b,m}-\Phi_{b,m}^{(1)}\|_2
 <2^{21}\kappa^{-2},\qquad \kappa\ge2^{12}.
\tag{A.15}
$$

该式包含两个输入列以及跨支余项，不是只对 height 使用 Airy
渐近式。它还给此高区 $\|\Phi_{b,m}\|_2<2$。
低区由 (A.12) 和模型 norm1，取差的上界
$2^{33}\max(1,\kappa^{-5/6})$。

由于 $M\ge4$，对 $g\in\{4/3,2\}$ 有
$\langle M\rangle^g<2M^g$。分成三段后，完整加权误差满足

$$
\begin{array}{c|c}
\text{真实频率范围}&
\langle M\rangle^g\|\Phi_{b,m}-\Phi_{b,m}^{(1)}\|_2\\ \hline
0<\kappa\le1 & <2^{34}b^g\kappa^{g-5/6}\le2^{34}b^g\\
1\le\kappa\le2^{12} & <2^{34+12g}b^g\le2^{58}b^g\\
\kappa\ge2^{12} & <2^{22}b^g\kappa^{g-2}\le2^{22}b^g .
\end{array}
\tag{A.16}
$$

这里低区指数 $g-5/6$ 严格为正。这正是不能把低频同阶 sup
先乘整个截止频率权的原因；逐频权使低区费用下降。

mean 直接用 (A.3)、(A.5) 和 mean 版本 (A.6)，给

$$
\|\Phi_{b,0}\|_2=\|\Phi_{b,0}^{-1}\|_2<2^{16}\sqrt b,
\qquad \|\Phi_{b,0}-I_2\|_2<2^{17}\sqrt b.
\tag{A.17}
$$

它的 Sobolev 权为1，且 $\sqrt b<b^g$。由 (A.12)、(A.15)，
非mean同阶 norm 小于 $2^{32}b$。合并 (A.9)–(A.17) 即证
(A.1) 和两个逆强界。

此外，对任何 $M_*>0$，本端架和模型均准确保持每个 Fourier
模，所以

$$
P_{\ge M_*}(\Phi_b-\Phi_b^{(1)})P_{<M_*}=0,
\qquad
P_{\ge M_*}\Phi_bP_{<M_*}=0,
\tag{A.18}
$$

逆向也一样。这是以后有限算子复合中真正的低到高门；不能以它
替代实际非径向 root evolution 或 strict evolution 的低到高门。

## 5. 重付旧 (H.17) 及其已公布的宽后继

本节只修复既有显示常数，不宣称全部复合已经达到自然斜率幂。
把原 root 到固定物理 $t$ 截面的完整映射按真实次序写为

$$
L_e=G_e\Phi_{b_e}U_e,
\qquad
L_e^{(1)}=G_e^{(1)}\Phi_{b_e}^{(1)}e^{B_e}.
\tag{A.19}
$$

这里 $G_e$ 包括同一真实 graph、principal 两角和原固定端态的
恢复，所有原密度因子在相同物理两迹之间准确抵消。右根交换
矩阵另保，norm为1。
这个抵消具体使用原 graph (G.24)–(G.26)：$k=\sqrt{-\det A}$
是二维 divergence 密度在实际坐标变换下的不变量，故严格区的
密度高度恰为 $W\circ H$；两条 derivative density 由
$H'Y_\sigma\circ H$ 及该式保留的 normal shear 恢复。
剩下的真实角映射及其完整 mean 恢复按原已付整数能量、对偶和
插值门 norm小于2；它也包含在下文 $2^4$ 的费用中。

需要说明 (A.6) 与 graph 文使用的完整
$\mathcal W_s=(c_0,\alpha,|D|^{-1/2}Z_+,|D|^{-1/2}Z_-)$ 之间的
固定单位。对非mean，代入 (A.6) 得到常数 $ic/\sqrt\pi$ 乘
一个带号交换；mean 则有

$$
\binom{c_0}{\alpha}
 ={c\over\sqrt\pi}
       \begin{pmatrix}1&1\\i/2&-i/2\end{pmatrix}
        \binom{a_+}{a_-}.
\tag{A.20}
$$

除共同标量外，该变换及其逆的最大奇异值均不超过 $\sqrt2$。
因此任何完整 graph norm 在这两种单位间至多乘2；没有新增
$b$ 幂。裸 root mean 到 graph mean 的 $\sqrt b$ 已在
$\Phi_b$ 中，不能再免费把它当恒等，也不需要收费两遍。

旧 (H.15)–(H.16) 的完整 root interaction 界独立于有误的端架句：
其频率平衡是 $s_m=(1+\kappa_m^{4/3}+\kappa_m^2\xi)^{1/2}$，
尚未经过 (A.5) 的严格 wave shear。它们给所有需要的
$|r|\le4$ 窗

$$
\|U_e^{\pm1}\|_{H^r}<2^{2217}b_e^{2/3},\qquad
\|U_e-e^{B_e}:H^s\to H^{s+4/3}\|<2^{2562}b_e^2.
\tag{A.21}
$$

第二式由原两次完整 Volterra 的 $2^{2560}b_e^2$、
[新一次积分 (F.7)–(F.11)](R119-supplement-complete-root-first-phase-in-slope-units.md)
的完整 $2^{128}b_e^{4/3}$ 以及自伴首模型的
$2^{256}b_e^2$ 二次费用相加取得。它是全输入全输出界，不使用
只在高输出成立的改进门；$e^{\pm B_e}$ 在这些同阶窗的 norm小于2。
这里四阶窗口的模型界也可直接引用旧 (H.6) 对角非mean部分的
费用；它独立于自由端架，径向大平均准确酉移走。

[完整 graph 新界](R119-supplement-complete-root-graph-two-order-slope-budget.md)
(G.19)–(G.22) 连同 (A.20) 足以取

$$
\|G_e^{\pm1}\|_{H^r},\ \|(G_e^{(1)})^{\pm1}\|_{H^r}<2^4,
\qquad
\|G_e-G_e^{(1)}:H^s\to H^{s+4/3}\|<2^{704}b_e^{4/3}.
\tag{A.22}
$$

其中两独立 mean 行列来自完整高度恢复，没有把物理平均替换为
标签平均。所需中间指数最高为 $s+4/3\le7/3$，均在既有窗口中。

(A.1)、(A.21)–(A.22) 给完整正逆同阶界

$$
\|L_e^{\pm1}\|_{H^r}<2^{2285}b_e^{5/3}
                                      <2^{2500}b_e^2.
\tag{A.23}
$$

在 (A.19) 作准确三项 telescoping：最贵项是
$G_e\Phi_b(U_e-e^{B_e})$，不超过
$2^{2630}b_e^3$；中项 $G_e(\Phi_b-\Phi_b^{(1)})e^{B_e}$
不超过 $2^{69}b_e^{4/3}$；末项
$(G_e-G_e^{(1)})\Phi_b^{(1)}e^{B_e}$ 不超过
$2^{705}b_e^{4/3}$。于是可取

$$
\|L_e-L_e^{(1)}:H^s\to H^{s+4/3}\|
 <2^{3200}b_e^4<2^{3500}b_e^6.
\tag{A.24}
$$

模型完整正逆同阶 norm 从 (A.22) 和 $e^{\pm B}$ 已小于 $2^5$。
不需要依赖更锐的旧模型 norm2，准确 inverse identity 就给

$$
\begin{split}
&L_e^{-1}-(L_e^{(1)})^{-1}
       =-L_e^{-1}(L_e-L_e^{(1)})(L_e^{(1)})^{-1},\\
&\|L_e^{-1}-(L_e^{(1)})^{-1}:H^s\to H^{s+4/3}\|
 <2^{5705}b_e^6<2^{6002}b_e^8 .
\end{split}
\tag{A.25}
$$

(A.23)–(A.25) 正是旧显示 (H.17) 所需的三条界，而且有明确余量。
旧 (H.22) 的两项最高费用、旧 (H.1) 的全部端口余项和旧
(H.26)–(H.30) 只消费这些显示门及独立的 strict/positive 门；
所以现在可以引用它们，但应同时引用本篇对错误中间句的修复。
实际首模型的原 norm2 还可由很小角部分重新获得；即使只使用这里
更宽的 $2^5$，旧 (H.22) 有超过 $2^{200}$ 的常数余量，有限个
模型因素也不会改变其显示包络。

## 6. 独立依赖、全部源和未完成的复合

为避免把勘误影响传播到不相干的定理，依赖范围明确如下。

* [全输入高输出 root Volterra](R119-supplement-root-high-output-Volterra-without-low-frequency-condition-number.md)
  只使用旧 (H.15)–(H.16) 的 interaction 和全输入 Cauchy，未使用
  有误的自由 endpoint bound。
* [完整 root 首相位](R119-supplement-complete-root-first-phase-in-slope-units.md)
  使用 R43 的完整第一次积分及前项 Volterra 门，同样不需要该句。
* [完整 positive Airy 余项](R119-supplement-positive-full-Airy-remainder-in-root-slope-units.md)
  使用根点 contact、真实两端 DN/Poisson 与完整 graph identity；
  它不经过本篇负侧 $\xi=H$ 的自由严格 wave 端架。
* [graph 斜率界](R119-supplement-complete-root-graph-two-order-slope-budget.md)
  已明确只给裸 mean 转换 $2^{20}\sqrt b$；其非mean端架由本篇补足。

原 ordinary、weak 和 metric-source 的准确单位没有改变。根上
仍是 total 状态 $P=u_\xi+F^\xi$ 及准确源对

$$
\partial_\xi\binom uP
 =\begin{pmatrix}0&1\\-(\xi D^2/b^2+V)&0\end{pmatrix}\binom uP
       +\binom{-F^\xi}{f_c-\partial_\phi F_c^\phi}.
\tag{A.26}
$$

对 total 两迹，(A.5) 的第二行读作
$\sqrt bH^{-1/4}(P+u/(4H))$；如果要恢复 bare derivative，再
减去同一 $F^\xi$ 的真实端点负荷。体源 norm 本身不授予该端点迹。
本篇只变换这两个实际状态和已经存在的全部 source 列，没有
对 $F^\xi$ 求径向导数。

图上的完整 Piola、密度和 mean source 仍按原 graph
(G.30)–(G.37) 与新 graph 第6节依次施加。固定标签微分的两列
$\Gamma^*$ 也穿过同一线性两行式；不能在源处理中把它们设零。
旧原单位源公式不依赖错误的 $b^{1/2}$ 中间断言，仍以其原输入
范数和原充分正则性为前提。

新的负段全 word 还必须把 root/graph/strict 的真正低到高门和
所有中间频带一起支付；只把 (A.1) 插到局部高输出估计中不足以
推出新阈值。尤其不在本篇把 mean 的模型恒等块升级为实际 mean
方程，也不把旧的高块 inverse 称为完整网络 inverse。

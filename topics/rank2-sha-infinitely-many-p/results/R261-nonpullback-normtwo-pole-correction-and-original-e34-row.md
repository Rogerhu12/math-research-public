# R261 — 非拉回 norm-two 常数行、第二次真极补偿与原 E34 的非零运输

日期：2026-11-13。**状态：以下完整 norm-two 输入、非零十七挠点处的实际极项、固定补偿、原 meromorphic 迹、补偿后的全纯迹及原 E34 非零系数均已证明。四个固定对数与原 E34 的完整中央关系已写出；尚未证明其中的中央剩余行非零。**

本篇承接 [R259](R259-normtwo-compensation-conductor17-rankone-and-full-log-transport.md)。
R259 的纯 $[\beta]^*$ 常数来源经过导子十七处的真实迹后只剩一个
CM 方向。这里在目标变量中插入
$h(w)=1/(x(w)^2-1)$，确实改变该行为。
这个插入还产生了 R259 基本来源没有的非零十七挠点极项；
它们必须用下面的第二个准确补偿清除，才能使用十七维全纯模型。

## 1. 原完整 Leibniz 输入

保持
$$
\alpha=1+i,\quad\beta=4-i,\quad\bar\beta=4+i,\quad
F=S_8^{17},\quad S_8=-y\vartheta\sigma^3,
$$
$$
F_\beta(w)=F(\beta w),\qquad
G_\beta(z)=F(\beta z)^2,\qquad H_\beta(z)=F(\alpha\beta z).
$$
对 R253 的一个八次角色，仍写
$$
\Psi=\Phi+C,\quad C=\Psi(0)\ne0,\qquad
\Upsilon_\beta(\alpha z)=\frac{y(\beta z)}{x(\beta z)}\Psi(z),
$$
$$
\mathcal A_\beta(w)
=-\frac{\vartheta(\beta w)^{69}}{\sigma(\beta w)}.
$$
R259 的三个完整实际迹是
$$
L_0=-2CF_\beta,
$$
$$
L_1=-68\beta F_\beta\Upsilon_\beta
-68\alpha\beta C F_\beta\frac{YX}{V-1},
$$
$$
L_{2,\rm reg}
=-136\alpha\beta\nabla_{\mathcal A_\beta}
                 (F_\beta\Upsilon_\beta)
-4352i\beta^2 C F_\beta\frac X{V-1},
                                                               \tag{1}
$$
其中 $X=x(\beta w),Y=y(\beta w),V=X^2$。
$L_{2,\rm reg}$ 的输入保留 R259 的
$4692\beta^2H_\beta\Phi/x(\beta z)$ 补偿。

取一个固定椭圆函数 $h=h(w)$。真正的插入是在原输入中乘
$h(\alpha z)$。由完整 Leibniz 公式，所得迹为
$$
L_h=hL_{2,\rm reg}+2\alpha h'L_1+\alpha^2h''L_0.
                                                               \tag{2}
$$
将 (1) 逐项代入，准确得到
$$
\boxed{
L_h=-136\alpha\beta
       \nabla_{\mathcal A_\beta}(hF_\beta\Upsilon_\beta)
-C K_h,
}
$$
$$
\boxed{
K_h=4iF_\beta\left[
h''+68\beta h'\frac{YX}{V-1}
       +1088\beta^2h\frac X{V-1}\right].
}                                                               \tag{3}
$$
这里 $h$ 的自变量是 $w$，不是 $\beta w$。
因此 (3) 的最后来源通常不是纯 $[\beta]^*$；同时，它不自动全纯。

## 2. 原 $K_h$ 的真实十七挠点极项

现在固定
$$
h(w)=\frac1{x(w)^2-1},\qquad U=x(w)^2.
                                                               \tag{4}
$$
在非零 $T\in E_0[\beta]$ 处，令 $t=w-T$。原 CM 坐标给
$$
X\sim(\beta t)^{-2},\qquad
Y\sim-(\beta t)^{-3},\qquad
\frac{YX}{V-1}\sim-\frac1{\beta t}.
$$
而 $F_\beta(T)$ 非零，且
$$
h'(T)=-\frac{4x(T)y(T)}{(x(T)^2-1)^2}\ne0.
$$
所以
$$
\boxed{
K_h(w)=-\frac{272iF_\beta(T)h'(T)}{w-T}+O(1)
\quad\text{于每个非零 }T\in E_0[\beta].
}                                                               \tag{5}
$$
这个极来自 $YX/(V-1)$ 在 $O$ 的极，不是来自分母 $V-1$ 的零点。
仅在后者使用 $F_\beta$ 的十七阶零，会遗漏 (5)。

令 $K_\beta(U)$ 为原 sigma division 多项式，
$$
K_\beta(x(w)^2)=\frac{\sigma(\beta w)}{\sigma(w)^{17}},
$$
$$
K_\beta(U)=(4-i)U^4+(-12+20i)U^3
 +(28+10i)U^2+(-20-12i)U-i.
                                                               \tag{6}
$$
它在上述十六个非零点各有一个简单零。
故下列固定补偿准确清除 (5)：
$$
\boxed{
\widehat K_h
=K_h+272iF_\beta h'\,
          \partial_w\log K_\beta(x(w)^2).
}                                                               \tag{7}
$$

这个补偿有真实 norm-two 输入。由 $L_0=-2CF_\beta$，定义
$$
\boxed{
\widehat L_h
=L_h+136i\,h'\,
       \partial_w\log K_\beta(x(w)^2)\,L_0.
}                                                               \tag{8}
$$
(8) 的新增项由在原 $H_\beta\Phi$ 输入上乘同一个目标函数的
$[\alpha]^*$ 得到。由投影公式，
$$
\boxed{
\widehat L_h
=-136\alpha\beta
       \nabla_{\mathcal A_\beta}(hF_\beta\Upsilon_\beta)
-C\widehat K_h.
}                                                               \tag{9}
$$
所以不是在求出结果后任意删除极部分。
(8) 与 (9) 保留原 $4692$ 项和新增的 kernel-$\beta$ 项。

## 3. 补偿后的固定全纯有理来源

沿用 R248 的 $Q_\beta,K_\beta,D_\beta$，有准确 division 恒等式
$$
U_\beta:=x(\beta w)^2
 =\frac{UQ_\beta(U)^4}{K_\beta(U)^4},
\qquad
\boxed{
U_\beta-1=\frac{(U-1)D_\beta(U)^2}{K_\beta(U)^4}.
}                                                               \tag{10}
$$
此外
$$
68\beta\,\frac{YX}{V-1}
=17\,\partial_w\log(U_\beta-1).
$$
因此 (7) 把导数系数准确改成
$$
17\,\partial_w\log\bigl((U-1)D_\beta(U)^2\bigr);
$$
在非零 kernel-$\beta$ 点没有剩余极。

对 (4)，完整结果为
$$
\boxed{
\widehat K_h=4iF(\beta w)x(w)\,
                  \frac{\mathcal N(U)}{(U-1)^2D_\beta(U)^2},
}                                                               \tag{11}
$$
其中
$$
\boxed{
\begin{aligned}
\mathcal N(U)={}&(12-260U)D_\beta^2
 -544U(U-1)D_\beta'D_\beta\\
&+1088\beta^2Q_\beta^2K_\beta^2.
\end{aligned}
}                                                               \tag{12}
$$
这里 $D_\beta'$ 表示 $U$ 导数；(7) 中始终是 $w$ 导数。

(11) 全局全纯。在 $T_\pm$，分母至多四阶，$F(\beta w)$ 有十七阶零；
在 $D_\beta$ 的其他零点，分母至多二阶，仍由同一十七阶零支付。
这些点以外没有新有限极点；在 $O$，(11) 从 $w^2$ 开始。
其全局 $i$ 特征为 $-1$，原线丛仍为次数 $1156$ 的 twist-$T_0$。
所以
$$
[\bar\beta]_*\widehat K_h
=\frac W x\,P_h(U),\qquad \deg P_h\le16,                 \tag{13}
$$
其中 $W=-y\vartheta\sigma^{67}$，目标重新写 $U=x^2$。

与此相对，未经 (7) 补偿的真实迹为
$$
\boxed{
[\bar\beta]_*K_h
=\frac W x\,\frac{N_h(U)}{K_\beta(U)},\qquad
\deg N_h\le20.
}                                                               \tag{14}
$$
因为 $\bar\beta$ 在 $E_0[\beta]$ 上可逆，(5) 的十六个极点在目标仍互异；
每个极点只有一个 trace 分支贡献，不能在迹中自动相消。
证书核定 $\gcd(N_h,K_\beta)=1$。
(14) 没有被当作十七维全纯向量。

## 4. 原有理迹、全部补偿差及非零 E34 分量

(13) 的准确有限平坦迹在 R248 的同一纤维上计算：
$$
UQ_{\bar\beta}^4-tK_{\bar\beta}^4=0.
$$
若 $\mathcal L(U)=\mathcal N(U)/((U-1)^2D_\beta(U)^2)$，完整 frame 为
$$
\boxed{
P_h(t)=4it^8(t-1)^8
\operatorname{Tr}\left[
\left(\frac{P_\beta}{P_{\bar\beta}}\right)^{17}
 \frac{UQ_{\bar\beta}^2}{K_{\bar\beta}^2}\mathcal L(U)
\right].
}                                                               \tag{15}
$$
其中的 $UQ_{\bar\beta}^2/K_{\bar\beta}^2
=x(w)x(\bar\beta w)$ 是实际相邻权 frame 因子。
式 (15) 保留全部十七个分支及原归一。

证书列出 $P_h$ 的十七个系数、$N_h$ 的二十一个系数，以及
$$
[\bar\beta]_*(\widehat K_h-K_h)
=\frac W x\,\frac{P_hK_\beta-N_h}{K_\beta}.              \tag{16}
$$
所以新增极补偿的完整迹也被保存，不只保存主极项。
十七个准确纤维确定 (13)，二十一个确定 (14)，另一个未用于确定的
纤维同时核验两式；补偿后的多项式还通过其余所有纤维。

用 R251 的实际 $N$ 和三个首项 $z^2=1$ 的 $H_j^-$ 分解，得到

| 实际分量 | 准确系数 |
|---|---:|
| $H_1^-$ | $(-1485173289+20875167350i)/2^{20}$ |
| $H_2^-$ | $(-309664940525+459681214175i)/2^{23}$ |
| $H_3^-$ | $(121558674302-44147949183i)/2^{22}$ |

两个 CM 分量、其余十二个真实角色分量及每一分量的 $z^2$ 系数均在
证书中完整给出，没有只截取三个 primitive 数。
特别
$$
\boxed{
E_2^-[\bar\beta]_*\widehat K_h
=\frac{-309664940525+459681214175i}{2^{23}}H_2^-\ne0.
}                                                               \tag{17}
$$
这次已经经过真正的高次来源和共轭十七次迹，不能再用 R259 的
纯 $[\beta]^*$ 秩一结论将其删掉。

再作共同 $[2]$，并使用 R251 的全部 dyadic 常数，准确有
$$
\boxed{
Q_{+,w}\bigl((E_2^-[\bar\beta]_*\widehat K_h)(2z)\bigr)
=k_h B(2z),
}
$$
$$
\boxed{
k_h=-\frac{91936242835+61932988105i}{2^{16}}\kappa_4\ne0,
\qquad \kappa_4=2^{-1/4}.
}                                                               \tag{18}
$$
(18) 是固定代数恒等式，不是有限目标素数样本。
它保留两次不同的极补偿、原 $\beta$ 因子及真实参考尺度。

## 5. 固定非零对数到原 E34 的完整中央关系

以下才取中央泛函。固定惰性 $p>19$ 并排除既有固定分母的有限坏位。
写 $c=272c_0,d=p+1,q_2=2^{p-1}$。
令 $\mathcal O$ 表示真实
$Q_{+,w}E_2^-[\bar\beta]_*$，最后在输出作 $[2]$。
在含对数来源上，$E_2^-$ 只表示它已付的固定十六项算子；
不无证延长有限全纯空间的幂等性。

对 R253 的四个八次角色分别定义
$$
\Omega_{\chi,h}(u)=J_c(\mathcal O\widehat L_{\chi,h};u),
$$
$$
\Xi_{\chi,h}(u)
=J_c\!\left(
\mathcal O\nabla_{\mathcal A_\beta}
             (hF_\beta\Upsilon_{\chi,\beta});u\right).
                                                               \tag{19}
$$
这些来源全部由 (1)–(9) 指定，包括原水平对数常数。
由 (9)、(18) 的整条 germ 恒等式，准确得到
$$
\boxed{
\Omega_{\chi,h}(u)+136\alpha\beta\,\Xi_{\chi,h}(u)
=-C_\chi k_hq_2^uJ_{34}(u).
}                                                               \tag{20}
$$
$C_\chi\ne0$ 来自 R253，$k_h\ne0$ 来自 (18)。
没有假定 $C_\chi$ 是 $p$ 进单位，也没有删去 $q_2^u$。

因为原 $J_{34}(0)=0$，(20) 给出完整中央导数式
$$
\boxed{
\Omega_{\chi,h}'(0)+136\alpha\beta\,\Xi_{\chi,h}'(0)
=-C_\chi k_hJ_{34}'(0).
}                                                               \tag{21}
$$
因此对每个这类 $\chi$，左端非零与原 $J_{34}'(0)\ne0$ 等价。
这精确保留了原目标；单独的 $C_\chi\ne0$ 并不证明左端非零。

也可按完整函数除以已知非零常数，得到
$$
\frac{\Omega_{\chi,h}+136\alpha\beta\Xi_{\chi,h}}
     {-C_\chi k_hq_2^u}=J_{34}(u).                        \tag{22}
$$
$1/C_\chi$ 随 $p$ 变化，本篇不声称该商由固定代数系数给出。
四个 $C_\chi$ 的代数系数线性独立也不能直接应用于含未知
$\Omega_{\chi,h},\Xi_{\chi,h}$ 的乘积。

## 6. 非恒定剩余行的一阶完整转置

(19) 的 $\Xi_{\chi,h}$ 不是省略的形式项。
按 R259 的真实分支展开，令
$$
f=hF_\beta\Upsilon_{\chi,\beta},\qquad
\Theta=\vartheta(4z)^{17},\qquad
a_\nu=\partial_z\log\frac{T_\nu\mathcal A_\beta}{\Theta},
$$
$$
\widetilde f=\sum_\nu c_\nu r_\nu^{-1}T_\nu f,\qquad
\mathscr E=-\sum_\nu c_\nu r_\nu^{-1}a_\nu T_\nu f.
                                                               \tag{23}
$$
这里 $T_\nu$ 包含实际 dyadic、CM5 与 CM17 frame，
$r_\nu$ 是其真实斜率。链式法则准确给
$\mathcal O\nabla_{\mathcal A_\beta}f
=\nabla_\Theta\widetilde f+\mathscr E$。

$f$ 的普通极点只可能在非零 $E_0[\beta]$：
(4) 在 $O$ 的零杀掉原简单极，在 $T_\pm$ 的极由 $F_\beta$ 的零支付。
原二处运输的十六原部分与这些极点分离，奇 CM 对应不改变这个二处阶数。
因此 $\widetilde f/z$ 在原点正则且 $i$ 不变，所有固定分支都可使用
R254 的同一半径估计。
置
$$
g=\widetilde f/z,\quad
W_0=z\Theta'/\Theta-dcz^d,\quad
f_M=J_c(g),\quad g_M=J_c(W_0g).
$$
完整转置为
$$
\boxed{
\Xi_{\chi,h}(u)
=(du+1)f_M(u)-duf_M(u-1)-g_M(u)+J_c(\mathscr E;u).
}                                                               \tag{24}
$$
其中央导数包括
$$
f_M'(0)+df_M(0)-df_M(-1)-g_M'(0)+J_c(\mathscr E)'(0).
                                                               \tag{25}
$$
$\Omega_{\chi,h}$ 仍使用 (8) 的完整 norm-two 输入；
不能只保其二阶导数而删除两个极补偿或一阶 Leibniz 项。

式 (18) 已提供一个实际非纯拉回、非零的原 E34 常数载体。
下一项比较应在 (20)、(24) 的这些已指定来源上继续；
本篇没有把固定单位对数的非零，替代该完整剩余行的非零证明。

## 精确证书

[脚本](../scripts/check-nonpullback-normtwo-corrected-original-trace.py) 与
[输出](../scripts/check-nonpullback-normtwo-corrected-original-trace.json)
保存原 $K_h$ 的 meromorphic 迹、第二次补偿的完整迹、修正版
$P_h$、全部固定纤维和十六个实际角色分量及质量。
它们准确核验 (10)–(18)，特别没有对原 meromorphic 来源套用
十七维全纯界。
所有算术均在 $\mathbf Q(i)$ 或其固定十六次根单位扩张中完成；
没有目标素数扫描，也没有大稠密矩阵。


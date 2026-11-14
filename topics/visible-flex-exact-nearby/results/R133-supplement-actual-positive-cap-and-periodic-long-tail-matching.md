# R133：真实正帽与周期长径向段的全频非线性接合

**已证明。** 本篇把[真实正帽的解析强筛选](R133-supplement-true-cap-radial-decay-and-growing-analytic-width.md)
与 R119 的[实际长径向非线性 Dirichlet 解](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
联立。在准确 $r=R=25/8$ 处，完整物理第二形式 $B,C$（包括 mean）真正一致；
不是只匹配线性 Robin 图，也没有删掉有限长反射。由实际周期长段的框架向内
重建，得到从 $r=3/2$ 到长段另一端的周期 $C^2$ 等距浸入，保留两端真实高度和
径向迹。其外侧数据 $f_B$ 仍是独立输入；真实 label 方程
$\mathfrak F(a,f_*)=0$ 和更内侧 body 尚未解出。

所有系数覆盖同一准确仿射参数 $|\eta|\le10^{-9}$、全角圆和全部 primitive 尾。
数据取实、四重周期且关于同一物理角轴偶对称；复化仍含所有偶四重 Fourier 模。
同时平移角轴给相同结论，没有要求未知解只有有限个模式。

## 1. 两个真实区间、独立数据与范数

正帽区间为 $[L_0,R]=[3/2,25/8]$。长径向段使用 R119 的准确坐标

$$
u=4c_0(r-R),\quad 0\le u\le B_*:=2^{24}-25/8,
\quad a=a_*e^{-\omega u},\quad w=a/(4\omega),
\quad \chi=w/a=1/(4\omega).
\tag{M.1}
$$

反向时间 $t=\omega(B_*-u)$ 从外端 $0$ 到原切口 $\mathcal L=\omega B_*$。
在长段高度方程中 $E=1+w^2$，与原 $r$ 度量系数不同。
对非零四重模定义

$$
\|f\|_{\dot A^2_\sigma}
=\sum_{m\ne0}e^{\sigma|m|}|m|^2|f_m|,
\qquad\|z\|_{A^0_\sigma}=\sum_{m\ne0}e^{\sigma|m|}|z_m|.
\tag{M.2}
$$

长段两端非mean高度数据为 $h(0)=f_B$、$h(\mathcal L)=f_*$，其中
$v_\perp=awh$。保留

$$
\|f_B\|_{\dot A^2_\sigma}\le2^{-60},\qquad
\|f_*\|_{\dot A^2_\sigma}\le r_f:=10^{-8}.
\tag{M.3}
$$

$f_B$ 不被设为零，也不被假定已经由 tail labels 实现。
在正帽内端指定真实非零 $c_{\ne0}(L_0)$，其 $A_0$ 范数不超过解析筛选报告中的
准确预算 $\epsilon_L<6.600816124\cdot10^{-5}$；取 $A_2$ 数据以保留到边界的
原强角正则。已证明的原真实帽在该切口的整个无限迹确在此预算内。

正帽的增长宽为
$\sigma(r)=\frac1{128}\log[a(L_0)/a(r)]$。以下使用准确实际端宽
$\sigma=\sigma(R)$；原生界给

$$
.0690152937098<\sigma<.0691121491576<1/8.
\tag{M.4}
$$

因此也可给定固定宽 $1/8$ 的 $f_B$，以同时覆盖全部 $\eta$。
所有端口仍以原物理 $\theta$ 表示，没有换成 return angle 或 grounded flux。

## 2. 实际长段的更紧完整 lift 与内端 Neumann 界

R119 的准确齐次核为

$$
A_M(t)=e^{-2t}\frac{\sinh(M(\mathcal L-t))}{\sinh(M\mathcal L)},
\quad
B_M(t)=e^{2(\mathcal L-t)}\frac{\sinh(Mt)}{\sinh(M\mathcal L)},
\qquad M=|m|\ge4.
\tag{M.5}
$$

下面只收紧已证明的核常数，不更改边界或方程。令
$D_M=1-e^{-2M\mathcal L}$。写成两个指数的差，便有

$$
\begin{aligned}
A_M&=[e^{-(M+2)t}-e^{-2M\mathcal L+(M-2)t}]/D_M,\\
B_M&=[e^{-(M-2)(\mathcal L-t)}-e^{-(M-2)\mathcal L-(M+2)t}]/D_M.
\end{aligned}
$$

因 $\mathcal L>1$，$D_M>255/256$。$A_M$ 单调减，$B_M$ 单调增，均在 $[0,1]$。
$A_M'''<0$、$B_M'''>0$，所以二阶导数的极值在端点，而一阶导数绝对值的
最大值也可由对应凸性放到端点。端点公式给

$$
\begin{array}{c|ccc}
&\|H\|_\infty&\|H'\|_\infty&\|H''\|_\infty\\ \hline
A_M&1&(8/5)M&(12/5)M^2\\
B_M&1&M&M^2
\end{array}
\tag{M.6}
$$

例如 $B_M'(\mathcal L)=M\coth(M\mathcal L)-2<M$，
$B_M'(0)/M=2e^{-(M-2)\mathcal L}/D_M<128/255<1$；
$B_M''(0)=-4B_M'(0)$，
$B_M''(\mathcal L)=M^2+4-4M\coth(M\mathcal L)\in(0,M^2)$。
$A_M'(0)=-2-M\coth(M\mathcal L)$ 与
$A_M''(0)=M^2+4+4M\coth(M\mathcal L)$ 给表中另外两界，使用
$\coth(M\mathcal L)<257/255$ 即可。

故真实强空间 $\mathcal Y_\sigma$ 中的完整两端 lift 满足

$$
\|h_D\|_{\mathcal Y_\sigma}
\le5\|f_B\|_{\dot A^2_\sigma}+3\|f_*\|_{\dot A^2_\sigma}
\le5F,\qquad F=\|f_B\|_{\dot A^2_\sigma}+\|f_*\|_{\dot A^2_\sigma}.
\tag{M.7}
$$

既有真实长段定理给 $H:=\|h\|_{\mathcal Y}\le r_*=2^{-20}$，
$\|\mathcal Q(h)\|\le512H^2$ 和零边界 Green 范数小于32。因此

$$
H\le5F+2^{14}H^2\le5F+H/64,
\qquad H\le(320/63)F<6F.
\tag{M.8}
$$

再令 $k=h-h_D$。零 Dirichlet Green 在内端的准确导数为

$$
\partial_tG_M(\mathcal L,s)
=e^{2(s-\mathcal L)}\frac{\sinh(Ms)}{\sinh(M\mathcal L)}.
$$

它非负，且

$$
M\int_0^{\mathcal L}|\partial_tG_M(\mathcal L,s)|\,ds
\le\frac1{D_M}\frac M{M+2}<2.
$$

逐频求和得到真正内端（不是两端混合的粗界）

$$
\|\partial_\theta k_t(\mathcal L)\|_{A^0_\sigma}
\le2\|\mathcal Q(h)\|_{\mathcal F_\sigma}\le1024H^2,
\qquad \|k_t(\mathcal L)\|_{A^0_\sigma}\le256H^2.
\tag{M.9}
$$

所有估计在完整复化 Banach 代数中成立，供下文 Cauchy 导数使用。

## 3. 真实 Dirichlet-to-curvature 图的全非线性余项

采用[准确物理曲率接口](R119-supplement-Codazzi-boundary-from-actual-regular-tail.md)：

$$
P=f_{*,\theta},\quad U=f_{*,\theta\theta},\quad
\mathcal K=\mu(h)+2f_*+h_t(\mathcal L),\quad V=\mathcal K_\theta,
$$
$$
D=1-w^2(2\mathcal K+\mathcal K^2+EP^2),\quad
J=1+\mathcal K+EU,
\qquad B=\chi\frac{V-P}{\sqrt D},\quad
C=-\chi\frac{J}{\sqrt E\sqrt D}.
\tag{M.10}
$$

这里 $\mu$ 是真实 holonomy 小根，$|\mu|\le256H^2$，不能置零。
原状态和有 $N=\|P\|+\|\mathcal K\|+\|U\|+\|V\|<4H$。
全实际端点满足 $w<1/800000$、$\chi\sqrt E<1/5$。
置 $x=w^2(2\mathcal K+\mathcal K^2+EP^2)$，Binomial 级数给

$$
D^{-1/2}=1+w^2\mathcal K+R,
\qquad \|R\|\le2w^2N^2,
$$
$$
\left\|J D^{-1/2}-1-E(\mathcal K+U)\right\|\le8w^2N^2.
\tag{M.11}
$$

例如 $\|x\|\le3w^2N<1/4$，二阶 Binomial 余项不超过 $\|x\|^2$；
$x/2-w^2\mathcal K=w^2(\mathcal K^2+EP^2)/2$，乘回 $J$ 即得 (M.11)。
这些是完整 Fourier 代数估计。

记 $c_M=M\coth(M\mathcal L)$、$s_M=Me^{-2\mathcal L}\operatorname{csch}(M\mathcal L)$。
保留全部有限长反射，线性输出为

$$
\mathcal K^{\rm lin}_m=c_M(f_*)_m-s_M(f_B)_m,
$$
$$
(C-C_r)_{\ne0}=\mathcal L_C f_*+\chi\sqrt E\,S f_B+\mathcal R_C,
\quad (\mathcal L_C)_m=\chi\sqrt E(M^2-c_M),
\quad S_m=s_M.
\tag{M.12}
$$

非mean 投影准确消掉 $\mu$ 的一阶 mean 项，而保留其在 (M.11) 中的所有耦合。
由 (M.9)–(M.11)，

$$
\|\mathcal R_C\|_{A^0_\sigma}\le64H^2\le2^{12}F^2,
\qquad \|\mathcal R_B\|_{A^0_\sigma}\le256H^2.
\tag{M.13}
$$

消去线性 $f_*$ 后，$B$ 的完整曲率图为

$$
B=\mathcal T Z+\mathcal S_B f_B+\mathcal R_D,
\quad Z=(C-C_r)_{\ne0},\quad
\mathcal T_m=\frac{im(c_M-1)}{\sqrt E(M^2-c_M)},
\tag{M.14}
$$

其中 $\mathcal S_B$ 是原 (C.17) 的准确非零反射列，
$\mathcal R_D=\mathcal R_B-\mathcal T\mathcal R_C$。
因 $\|\mathcal T\|<2$，

$$
\|\mathcal R_D\|\le384H^2<2^{14}F^2,
\qquad |C_0-C_r|\le46H^2<2^{11}F^2.
\tag{M.15}
$$

第二个结论采用原完整 mean 小根估计 (C.13)–(C.14)，不是把 mean 当残差删除。
共同偶反射使 $P,V$ 奇、$D$ 偶，因此 $B_0=0$ 准确成立。

## 4. 完整非零 $C$ 到真实 Dirichlet 数据的逆

所有非零模 $M\ge4$ 上，原准确频率界给

$$
\frac{M^2}{M^2-c_M}\le\frac{1020}{763},\qquad
\|\mathcal L_C^{-1}\|_{A^0_\sigma\to\dot A^2_\sigma}
<6\frac{1020}{763}<9.
\tag{M.16}
$$

令 $\|Z\|_{A^0_\sigma}\le r_Z=10^{-9}$，按

$$
f_* =\mathcal L_C^{-1}
 \left[Z-\chi\sqrt E,S f_B-\mathcal R_C(f_B,f_*)\right]
\tag{M.17}
$$

求解。这里 $f_B$ 是固定但任意的独立参数。
设准确 $F_*:=r_f+2^{-60}$，则 $2F_*<2^{-25}$，所以所有 Cauchy 圆盘均在
已经证明的真实长段全纯域中。二次界 (M.13) 给

$$
\|D\mathcal R_C\|\le4\cdot2^{12}F_*.
\tag{M.18}
$$

确切反射满足
$\|\mathcal L_C^{-1}\chi\sqrt E S\|\le2e^{-6\mathcal L}$。
于是 (M.17) 的实际球像小于 $9.003686401\cdot10^{-9}<r_f$，
收缩小于 $.001474561$，并给

$$
\|D_Zf_*\|<9.013290638.
\tag{M.19}
$$

这是完整无限非零频率上的真实非线性逆；不是反演有限矩阵。
它连续、全纯依赖 $Z,f_B$，保持共同实反射对称性。

## 5. 与实际正帽的外 $d$ 和 mean 端口联立

正帽三角图仍使用同一真实 $q_m(R)$，包括原 R74 非零尾费用。
令 $q_*=(1+w^2)^{-1/2}$。由 (M.14)，有限长线性比值与 $q_*$ 的差不超过
$8e^{-8\mathcal L}$，因为

$$
\frac{M(c_M-1)}{M^2-c_M}-1
=\frac{(M+1)(\coth(M\mathcal L)-1)}{M-\coth(M\mathcal L)}.
$$

定义准确正费用

$$
\epsilon_q=\epsilon_{\rm R74}+8e^{-8\mathcal L}>0,
\qquad\epsilon_s=2e^{-6\mathcal L}>0.
\tag{M.20}
$$

这些量在原生记录中都是非零 Arb 数，未因浮点下溢被清零。
对 (M.17) 的真实解，给正帽的准确端口为

$$
d_m(R)=i\operatorname{sgn}(m)B_m^{\rm tail}+q_m(R)Z_m,
\quad B_0(R)=0,\quad c_0(R)=C_0^{\rm tail}-C_r.
\tag{M.21}
$$

由 (M.15)、(M.18)、(M.19)，记 $J_f=9.013290638$，可取

$$
\begin{aligned}
e_d&=\epsilon_qr_Z+\epsilon_s2^{-60}+2^{14}F_*^2
 <1.638400001\cdot10^{-12},\\
e_0&=2^{11}F_*^2<2.048000001\cdot10^{-13},\\
L_d&=\epsilon_q+4\cdot2^{14}F_*J_f<.005906951,\\
L_0&=4\cdot2^{11}F_*J_f<.000738369.
\end{aligned}
\tag{M.22}
$$

其中后两项是真实端口对 $Z$ 的导数界。另端 $f_B$ 的反射列和非线性影响始终保留。

现在使用解析正帽的同一 $\mu=3/2,\tau=1/128,\rho=.0004$ 球。
其原球像 $I_{\mathrm{base}}<.000228752400$，收缩 $\lambda_c<.464505257$，
$H_D<69.189285$。准确径向权满足

$$
W_0(R)=\left(\frac{a(R)}{a(L_0)}\right)^{3/2}
>W_->1.7262957358\cdot10^{-6}.
\tag{M.23}
$$

加入 (M.21) 的真实外端口后，完整帽球像为

$$
I_{\mathrm{base}}+\frac{H_De_d+e_0}{W_-}
<.000294537492<.0004.
\tag{M.24}
$$

所以对于每个允许 $Z$，真正帽解存在；其 $C$ 非零右迹定义 $\Psi(Z)$。
原零外端口成员满足 $\|Z_{\mathrm{base}}\|<7.034794836\cdot10^{-10}$。
比较两个真实帽时，同一个准确 $W_0(R)$ 在边界数据的归一和输出还原中相消，
因此不额外丢一个巨大权比。实际有

$$
\begin{aligned}
\|\Psi(Z)\|&\le\|Z_{\mathrm{base}}\|+
 \frac{H_De_d+e_0}{1-\lambda_c}
 <9.155535059\cdot10^{-10}<10^{-9},\\
\|D\Psi\|&\le\frac{H_DL_d+L_0}{1-\lambda_c}
 <.764593920<1.
\end{aligned}
\tag{M.25}
$$

从而在完整解析 $A^0_\sigma$ 球内有唯一固定点 $Z=\Psi(Z)$。
在这个固定点，非零 $C$ 由定义一致，$d$ 的定义保证非零 $B$ 一致；
mean $C$ 按真实尾输出设置，mean $B$ 按反射准确为零。
所以 $B,C$ 的全部物理曲率迹真正接合。

## 6. 框架、真实高度和保留的远端条件

真实 $C$ 在接缝非零，故 $A=(K_g+B^2)/C$ 也一致。R119 已从它的 holonomy
小根和闭合平面 coframe 构造周期实际长段；在接缝选同一点位置/Euclidean frame，
由[全物理两迹拼接](R133-supplement-full-physical-trace-matching-and-waist-reflection.md)
的唯一输运，整个正帽周期且 $C^2$ 接合。周期性来自实际匹配，未假定一个任意
driven 帽自行具有正确 holonomy。

非mean与mean高度/斜率仍是

$$
v_\perp(R)=a_*w_*f_*,\quad
v_a(R)=w_*[\mu+2f_*+h_t(\mathcal L)],
\quad Z=Z_{\mathrm{ref}}-v,
\tag{M.26}
$$
$$
v_0(\mathcal L)-v_0(0)=\int_0^{\mathcal L}aw\mu_t(h)\,dt.
\tag{M.27}
$$

整体 mean height 平移 $\lambda$ 仍独立；(M.27) 不是另一个可任意指定的
Dirichlet mean。实际原生预算为

$$
\begin{gathered}
\|h\|_{\mathcal Y}<6.000000001\cdot10^{-8},\quad
\|\mathcal K\|_{A^0_\sigma}<2.521451044\cdot10^{-9},\\
|\mu|<9.216000002\cdot10^{-13},\quad
\|v_\perp(R)\|_{A^0_\sigma}<4.607130610\cdot10^{-21},\\
\|v_a(R)\|_{A^0_\sigma}<2.831704764\cdot10^{-15},\quad
|v_0(\mathcal L)-v_0(0)|<3.396745257\cdot10^{-24}.
\end{gathered}
\tag{M.28}
$$

这里使用 $\|f_*\|_{A^0}\le r_f/16$、
$\|\mathcal K_{\ne0}\|\le(257/1020)r_f+\epsilon_s2^{-60}+256H^2$，以及
$\int_0^{\mathcal L}aw\,dt\le a_*w_*/2$。
原物理径向导数由 $v_r=-4c_0\omega aw\mathcal K$ 准确恢复。
这些是真实 raw height 与径向迹，未当作 grounded flux。

另一端仍必须与 label 生成的 $f_B(a),k_B(a)$ 解准确方程

$$
\mathfrak F(a,f_*)=k_B(a)+C_Lf_B(a)-S_Lf_*
                 -E_D(f_B(a),f_*)=0.
\tag{M.29}
$$

本篇没有把 $f_B=0$ 当成这个方程已解，也没有授予非零 $f_*$ 的完整 label 可达性。
内侧 body 的全 $B,C$ 两迹、waist 条件、最终握持、全局嵌入与 reach 也仍须完成。
本篇闭合的是此前未闭的真正**正帽—周期长段**接口及其完整外端 mean。

## 7. 实际算术

`scripts/fourfold_codazzi_cap_actual_long_tail_matching.py` 消费同一真实663盒
解析筛选与完整原始参考，实际结果保存于
`notes/2026-11-13-R133-positive-cap-actual-long-tail-joint-native.json.gz`。
所有收缩、自映、真实 $\chi,w$、解析域和完整反射门实际全过。
报告明确保留独立 $f_B$、mean height、所有 Fourier 模、完整参数范围及
(M.29) 未解旗标。

特别地，实际下界 $\mathcal L>24514072.6268$ 给非常小而**非零**的反射；
native 同时保留原 R74 fee 约 $7.53\cdot10^{-85170600}$ 与有限长反射约
$2.99\cdot10^{-63877959}$ 的 Arb 指数形式。有限机器小数显示为零不参与任何门。

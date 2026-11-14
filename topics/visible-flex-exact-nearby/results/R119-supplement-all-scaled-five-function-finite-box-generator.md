# R119 续篇：全缩放五函数控制与实际有限参数盒

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇在第67束同一个实际 quartic、同一
主参数族内，将五函数控制延伸到全部 $\kappa=M^2/B$，并付清
原两 phase 补偿的完整 Hessian、band 中的 $r/N_{\rm band}$
分配和有限参数盒。对原来每个真正保留的 middle 模，得到
$$
               -iS_M^*D_{\theta_M}S_M
                         >2^{-175000}M^{-1891}I_2.    \tag{B.1}
$$
若该 band 上端 $U\ge\sqrt B$，实际更强下界是
$2^{-93000}M^{-290}I_2$。这是完整两端口 generator；
没有把局部 rank-one 配对或一条 Robin 线代作矩阵正定性。

这里仍为每个模式保留独立 $\theta_M$，不是用一个 band 公共
坐标绕过其它模式已消去端块的导数。结论给主允许族中的新的
真实选择空间；它不宣称先前某个未指定参数点已经自动有这些
间隙，也不将径向正定性移给非径向近共振簇。

## 1. 保持原对象的全缩放局部界

全部记号、真实中心 frame、$a,\Delta,B,K_j,I,\ell$ 和原两
phase 与[五函数 Wronskian](R119-supplement-actual-two-phase-five-function-Wronskian-and-low-scaled-control.md)
一致。置
$$
              L=1+\kappa=1+M^2/B,\qquad
              \gamma=1+\Delta+\Delta\sqrt\kappa .
$$
没有改变 $Q=7+Bf$、原 $\zeta,h,b_M$、有限 prefix 或
最终固定 connector。

第67束 (F.8)--(F.17) 的残差 Wronskian 完全不依赖 $\kappa$。
所以对于全部 $M\in4\mathbb N$，同一个二阶算子
$\mathcal A$ 仍准确消去两条实际 phase，且
$$
                    \det\mathcal T>2^{-80}\Delta^4.   \tag{B.2}
$$
真实三阶 monic 系数及其一阶导数现在小于
$2^{100}\Delta^2L$。把 $g'''$、$g''''$ 全部消去后，
$\mathcal T$ 每个矩阵元小于 $2^{640}\Delta^4L^2$，
因而完整三态逆为
$$
 \max_{0\le r\le2}|g^{(r)}|
 \le 2^{1365}\Delta^4L^4
               \max_{0\le r\le2}|(\mathcal A g)^{(r)}| .
                                                               \tag{B.3}
$$
两条 phase 的系数不含 $\kappa$，原 $C^5$ 费 $2^{520}$
原样适用。

真实中心可观测性也可以直接延伸，不能只沿用低区结论。记
$W=\max(|\mathcal K|,|\mathcal K_x|,|\mathcal K_{xx}|)$。
原准确 (F.19) 中
$$
 |4\lambda Q-s^2-Q_t|<20B^2L,\qquad
 b\ge\lambda^2,\quad Q_t\ge B/(2a).
$$
于是
$$
 |X|<41\Delta L\lambda^{-2}W,\qquad
 |X_t|<6BL\lambda^{-2}W.
$$
用原实际 frame (F.21)，并保留
$|\lambda-s/2|\le(5/2)BL$、
$|\lambda Q-s^2/4|\le(17/4)B^2L$，得到
$$
 \|A\|_F<2^9\Delta B^2L^2M^{-5}W.
$$
吸收前两矩阵元时只用
$M^2/(B^2L)=\kappa/(BL)<1$ 和 $M/(\Delta BL)<1$。
所以完整三个中心 jet 满足
$$
 \max_{0\le r\le2}|(\mathcal A g)^{(r)}(c)|
       >\epsilon_M:=
                2^{-1400}\frac{M^5}{B^2\Delta^5L^6}. \tag{B.4}
$$
这里没有把 $M$ 设成低频或把任意 $A$ 限为正矩阵。

## 2. 全频真实短片；局部状态不乘整窗条件数

原准确系统为
$$
 \mathcal Y=(\sqrt\gamma u,u_x/\sqrt\gamma),\quad
 u_{xx}+[N^2F+\tfrac\Delta2f'-\tfrac{\Delta^2}4H^2]u=0,
 \quad N=\Delta\sqrt\kappa.
$$
对所有 $\kappa$，$N\le\gamma$、$\Delta\le\gamma$；
一阶系数及其有限 jet 仍有第67束相同的
$l!(64\gamma)^{l+1}$ 界。在
$$
 |x-c|\le\min(\ell/8,2^{-12}/\gamma)
                                                               \tag{B.5}
$$
完整双向 Cauchy norm 小于 $2$。

需要另核实际中心单位输入：从 $Y$ 到 $\mathcal Y$ 的向前
norm 平方是
$\max(\gamma/k,a^2k/\gamma)$。因为
$$
 \frac{\gamma}{k}
 <\frac{1+\Delta}{2M}+\frac{a\sqrt B}{2}<\Delta,\qquad
 \frac{a^2k}{\gamma}<\frac{3a}{\sqrt B}<\Delta,
$$
此 norm 平方对所有 $M\ge4$ 都小于 $\Delta$。
这没有对逆向变换作未经支付的同样声称。

第67束 (F.26) 的三个完整二次型系数及前五导数仍小于
$2^{40}\gamma^2/a^2$。特别其中的 $\lambda/a$ 由
$\gamma^2/a^2\ge\lambda B$ 和 $aB=\Delta>80$ 支付；
$\lambda Q/\gamma$ 由 $N^2/(a^2\gamma)$ 支付。
不把这些系数粗乘成一个额外 $M^2B^2$。
由于 $\gamma<3\Delta\sqrt L$，完整实两行递推给
$$
 \max_{0\le r\le3}|(\mathcal A g)^{(r)}|
                 <G_M:=2^{800}B^2\Delta^6L^4.        \tag{B.6}
$$
实际出现的 $L^{7/2}$ 已向安全侧放宽至 $L^4$。

取
$$
 \rho_M=\frac{\epsilon_M}{16G_M}
       =2^{-2204}\frac{M^5}{B^4\Delta^{11}L^{10}}.     \tag{B.7}
$$
写 $M^5=B^{5/2}\kappa^{5/2}$，则
$\kappa^{5/2}/(1+\kappa)^{10}<1$，故
$\rho_M<2^{-2204}B^{-3/2}\Delta^{-11}$。
同理 $\rho_M\gamma<3\,2^{-2204}B^{-3/2}\Delta^{-10}$。
因此支集真实落在 (B.5)，包括任意大的 $\kappa$。

## 3. 完整 Sym2、真实 $dt$ 及共同 band 下界

使用原完全相同的构造
$$
 \psi_A=\sigma\,2^{-700}F^{9/2}
 \mathcal A^*\!\left[
 \partial_x^r\{\rho_M^{r+6}(1-((x-c)/\rho_M)^2)_+^{14}\}\right],
 \qquad r\in\{0,1,2\}.
$$
其 $C^4$ norm 小于 $1$，更精确地
$$
 \|\partial_x^l\psi_A\|_\infty\le\rho_M^{4-l},\qquad
 \|\partial_x^l\psi_A\|_{L^1(dx)}\le2\rho_M^{5-l}
                          \quad(0\le l\le4).          \tag{B.8}
$$
这是原式的每一项保留其 $\rho$ 幂后得到的；最高导数来自
$f_0^{(r+2+l)}$，其幂正好为 $4-l$。
原两 phase 仍由形式伴随准确消去。

只需六个候选方向（$r=0,1,2$ 及两种符号），对每个 Frobenius
单位 $A$ 至少一个具有正 pairing；因此其有限凸包直接包含
所需球，不需要对一个未闭的无限维函数球取极限。
真实 $dt=a\,dx$ 给完整支持函数下界
$$
 \begin{aligned}
 \int\mathcal K_A\psi_A\,dt
 &>a\,2^{-704}\epsilon_M\rho_M^9\\
 &>d(M):=2^{-22000}M^{50}B^{-39}\Delta^{-103}L^{-96}.   \tag{B.9}
 \end{aligned}
$$
至多四个候选的凸组合给 $L_{\psi_M}=(d(M)/4)I$。
到两端真实 scattering 的同一完整规范给
$-iS_M^*DS_M[\psi_M]\ge d(M)/(8K_j^2)I$。

现在取原 band $M\in[U/2,U]$，完整模式数
$N_{\rm band}\le U$。以下共同下界对 band 中每个实际模式成立：
$$
 d_U=2^{-22050}U^{50}B^{-39}\Delta^{-103}
                                     (1+U^2/B)^{-96}\le d(M).
                                                               \tag{B.10}
$$
这里单独支付 $M^{50}\ge2^{-50}U^{50}$，不错误声称
$d(M)$ 在整个正轴单调。跨越 $M=\sqrt B$ 的 band 也适用。

## 4. 原补偿 Hessian 与完整有限盒

消费第64束 (S.31) 同一允许族上已付的完整 matrix Hessian
$$
                 H_G=2^{30}K_j^4(U+B)^2.              \tag{B.11}
$$
它包括两个 phase 补偿 bump 的二阶响应，适用于所有单位
$C^4$ 方向，并不要求新方向还消去多余的十九次多项式。
在原未使用区间中设置
$$
 \Xi^{(n)}=\frac{r_U}{N_{\rm band}}
          \sum_{M\ {\rm in\ band}}\theta_M\psi_M,\quad
 |\theta_M|\le1,\qquad
 r_U=\min\!\left(2^{-n-80},
                \frac{d_U}{2^{36}K_j^6(U+B)^2}\right).
                                                               \tag{B.12}
$$
其完整 $C^4$ 大小不超过 $r_U$，所有其它区间的原允许控制
可以同时存在。每个 $\theta_M$ 仍是独立的真实坐标。

半径的分支可以准确确定。置 $\kappa_U=U^2/B$，则
$$
 d_U U
 =2^{-22050}B^{-27/2}\Delta^{-103}
              \frac{\kappa_U^{51/2}}{(1+\kappa_U)^{96}}
 <2^{-22050}.
$$
原 band 编号给 $U\ge2^n$，故 $d_U<2^{-n-80}$，
第二分支总是实际选中的分支：
$$
 r_U=\frac{d_U}{2^{36}K_j^6(U+B)^2}.
$$
由 (B.11) 作完整矩阵 Hessian 比较，其变化只占中心正定
下界的至多 $1/8$。于是整个有限盒上
$$
 -iS_M^*D_{\theta_M}S_M\ge D_{j,M}I,\qquad
 D_{j,M}=\frac{d_U^2}
                 {2^{40}N_{\rm band}K_j^8(U+B)^2}.    \tag{B.13}
$$
$r_U/N_{\rm band}$、真实两行归一及完整补偿项全部在此式中。
这是有限参数范围的结论，不是仅在参数原点的微分。

## 5. 同一原 middle 中的全部幂费用

由 (B.10)、$N_{\rm band}\le U$，
$$
 D_{j,M}>
 \frac{2^{-44140}U^{99}B^{-78}\Delta^{-206}K_j^{-8}}
           {(U+B)^2(1+U^2/B)^{192}}.                 \tag{B.14}
$$
不改变原低窗、中性层、输入权或频率门。

若 $U\le\sqrt B$，则 $(1+U^2/B)^{192}\le2^{192}$，
$(U+B)^2\le4B^2$，所以
$$
 D_{j,M}>2^{-44334}U^{99}a^{80}\Delta^{-286}K_j^{-8}
          >2^{-93200}\delta_j^{248}J^{-350}U^{99}.     \tag{B.15}
$$
后一步使用
$a>\delta_j^{3/2}/32$、$\Delta<3J$、
$3^{286}<2^{454}$ 和
$K_j^{-8}=2^{-48000}J^{-64}\delta_j^{128}$。
全部 bits 为 $44334+400+454+48000=93188$。

若 $U\ge\sqrt B$，则
$$
 (1+U^2/B)^{-192}\ge2^{-192}U^{-384}B^{192},
 \qquad (U+B)^2\le4BU^2.
$$
后一个不等式同时适用于 $U<B$ 和 $U\ge B$，因为
$B\le\sqrt B\,U$ 且 $U\le\sqrt B\,U$。
故
$$
 \begin{aligned}
 D_{j,M}
 &>2^{-44334}U^{-287}B^{113}\Delta^{-206}K_j^{-8}\\
 &>2^{-92030}\delta_j^{-83/2}J^{-157}U^{-287}\\
 &>2^{-92030}J^{-157}U^{-287}.                         \tag{B.16}
 \end{aligned}
$$
这里 $B^{113}\Delta^{-206}=a^{-113}\Delta^{-93}$，
$a<\delta_j^{3/2}/16$、$3^{93}<2^{148}$；
完整 bits 为 $44334+48000+148-452=92030$。
有利的负 $\delta$ 幂只在最后一步向下放宽，不把它反向收费。

原实际 middle 门仍为
$M\ge2^{-40}\delta_j^{-1/8}$，且 $U\le2M$。
由已付第64束第7节，
$$
                  \delta_j\ge2^{-320}U^{-8},
                  \qquad J<U^{1/64}.                \tag{B.17}
$$
代入 (B.15)，完整频率幂为
$8\cdot248+350/64-99=1890+15/32<1891$，bits
$93200+320\cdot248=172560$。再由 $U\le2M$，
$$
                    D_{j,M}>2^{-175000}M^{-1891}.
$$
代入 (B.16)，幂为 $287+157/64<290$；同样支付
$U\le2M$ 后得到 $D_{j,M}>2^{-93000}M^{-290}$。
这证明 (B.1)，包括跨越缩放阈值的 band。

## 6. 全网络、非径向与源的准确权限

每层原总 $C^4$ 小量仍由
$\sum_n r_U\le\sum_n2^{-n-80}<2^{-79}$ 支付。
新控制位于既有未使用区间，端点全部 jets 不动，原两 phase
由同一个真实补偿图准确保持。因此本篇可作为原主允许族中
一次公共径向选参的新输入；不是原先任意参数点的自动升级。

对固定 $M$ 若应用完整 unitary network，必须像原构造一样
只沿这个 $M$ 的 middle 窗口动 $\theta_M$，将其余外部参数固定；
由别的模式控制过的 prefix/尾端反馈可存在，但不能在会动的
方向上漏掉其 $P'$。一个 band 的所有模式不能免费共用一个
$\theta_n$ 而仍声称这些外块固定。

本篇没有把 (B.1) 与一个绝对小的非径向算子差作无权 Neumann。
仍须比较真实混模近核的完整 profile generator，连同
$D_\Omega X$、$D_\Omega\Gamma^*$、两个 physical principal 图、
两 mean、ordinary/weak affine 列和硬投影交叉项。
原源空间到本篇散射端口的同权接线也不由齐次 PSD 自动得到。

实际必要有理运算：

- [源码](../scripts/fourfold_all_scaled_five_function_box_20261114.py)；
- [原生记录](../notes/2026-11-14-R119-all-scaled-five-function-box-budget.json)。

自由 jet 和完整 $e>0$ 恒等式消费第67束已实际执行的77门；
本篇新记录只计算新增的全缩放、有限盒及全部层号/频率幂，
没有把它冒充原代数运算的重跑。

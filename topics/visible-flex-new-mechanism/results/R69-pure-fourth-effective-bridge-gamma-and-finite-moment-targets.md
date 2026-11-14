# R69：纯第四有效桥函数的 Gamma 闭式与共同 profile 无关的有限矩目标

日期：2026-11-14。本文是离线前 draft literature-pure-effective-bridge-matrix-response-20261114.md 的自足扩展稿；本文件是新字节，不冒称保持该旧稿 SHA256。来源审查代理已逐式独立核对本文使用的桥/常段传播、法向交叉消失、端点分部积分、Gamma 的五项、关键 1/3、反转奇偶及 Gamma_A(A)=0。没有运行真实 profile、候选几何或优化。另有小型 BigInt 有理自由代数检查，未假设两个算子可交换或满足结合律。

## 1. 固定的纯模式与右锚

沿用 [R56](../results/R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 的同一右 $\xi=r$ 锚。$H(U,V)$ 是对称双线性张量。固定光滑复 profile q，右 collar 为零；所有乘积为普通复乘法。由右锚产生的历史仍在右 collar 为零，但不假设左尾条件已支付。

纯 $-4$ 模式的 canonical 恢复为

$$B=\mathcal I H(Y_q,Y_q),\qquad U=\mathcal I H(Y_q,B),$$

$$H_{4,-4}=-H(B,B)/16-H(Y_q,U)/4. \tag{1}$$

固定真实有序桥/bulk 词，bulk 长度为 $N\ell_j$，桥长度固定。全程 $h>0$，并在同一个紧 profile 区间 $I=[l,r]$ 上有统一物理支条件 $z=\xi+\omega\geq\delta>0$，保证全部恢复及分部积分系数有限。所有桥满足 $\omega_s=k_s/(2h)$，两端有开常值 germ；同端变体保持实际 k、h、omega 端值及同一个全局 omega 原函数。N 是同一控制族中的整数圈数放大参数，改变 N 是新几何，不是加密。本文不把最高次数相容性当作完整第四或有限等距族。

## 2. 单桥的八矩与全部边界项

定义完整单桥 second characteristic 算子

$$\Phi_{\mathcal B}(f,g)=\int_{\mathcal B}R(H(Y_f,Y_g))(s,\xi)\,ds,$$

其中 f,g 不依赖 s，且右 collar 为零。桥不需要左右端状态相同，更不需要自闭合。

记 $z=\xi+\omega,u=h/z,c=D_su$。原六项 Volterra 化简中，第一次 s 分部积分产生边界 $-c\rho/u^2$；三个局部项分别产生 $c/(2u)$、$-d_1c/u^2$、$-r_2D_s(z/h)$ 乘相应 profile 单项式；三个尾系数产生 $-f_jD_s(z/h)$；R7 的额外关系产生 $-[(1+e^2)/h]D_s(1/h)$。桥端 $h_s=k_s=0$ 蕴含

$$c=0,\qquad D_s(z/h)=0,\qquad D_s(1/h)=0.$$

所以这些边界全部消失。若只取同端 jet 的两桥差，边界相同也足够；本文使用更强的常值 germ 条件。

完成分部积分后的低导数积分矩阵是

$$M=\begin{pmatrix}
p_0&2r_1&-4r_0\\
p_1&2s_1&-4s_0\\
p_2&2t_1&-4t_0
\end{pmatrix}. \tag{2}$$

R20 对这个**完成分部积分后的低导数密度**的点态恒等式给

$$\operatorname{tr}M=p_0+2s_1-4t_0=0. \tag{3}$$

不把这句话扩大为任意 raw 二阶导数密度逐点无迹。八个独立坐标确定

$$A_0=-p_1/2-p_2\xi,\quad A_1=p_0+p_1\xi+p_2\xi^2,$$

$$A_2=r_1+(s_1-p_0/2)\xi+(t_1-p_1/2)\xi^2-p_2\xi^3/2,$$

$$B_0=r_0+r_1\xi-p_0\xi^2/4,\quad
B_1=s_0+s_1\xi-p_1\xi^2/4,\quad
B_2=t_0+t_1\xi-p_2\xi^2/4. \tag{4}$$

令

$$J_0(f,g)=\int_\xi^r f''g'',\quad
J_1(f,g)=\int_\xi^r\eta f''g'',$$

$$J_2(f,g)=\int_\xi^r\{\eta^2 f''g''+2f'g'\}.$$

则单桥完整算子准确为

$$\boxed{\Phi_M(f,g)=A_0fg+\frac{A_1}{2}(fg'+f'g)
+A_2f'g'+B_0J_0+B_1J_1+B_2J_2.} \tag{5}$$

它对 M 线性、对 f,g 对称双线性。全部真实左尾保留，不在左端清零。式 (2) 也是 $L|_{\{1,\xi,\xi^2\}}$ 的矩阵；令三列代表 $a=L1,b=L\xi,c_*=L\xi^2$，可直接复核

$$A_1=a,\quad A_2=(b-\xi a)/2,\quad
C=(2\xi b-\xi^2a-c_*)/4,$$

然后用 $W=C'-A_2$、$B_2=(A_1+A_2')/2$、$B_1=W-2\xi B_2$、$B_0=C-\xi B_1-\xi^2B_2$ 恢复 (4)。

## 3. 保留全局历史的准确递推

写第二、第三 scalar 历史为

$$b=b_0+Nw,\qquad c=c_0+Nc_1+N^2v.$$

[R67](../results/R67-complete-fourth-period-cubic-bulk-count-and-bridge-control.md) 给桥内 w,v 不变。恢复场最高项是 $B_1=-Y_w,U_2=-Y_v$。故单桥矩阵 M 的真实作用为

$$\boxed{
\Delta b_0=\Phi_M(q,q),\quad
\Delta c_1=-\Phi_M(q,w),\quad
\Delta P_2=-\Phi_M(w,w)/16+\Phi_M(q,v)/4.} \tag{6}$$

全部 w,v 从真实前段带入，不能每桥重置。该桥对 $c_0,P_0,P_1$ 的作用未被 (6) 表示，也没有被设为零。

在常态 bulk 上，$c=Du=0$，且 $Y_{f,s}\parallel N,Y_{f,u}\in\operatorname{span}(T,B)$，而 $(\rho N)_s$ 在 T/B 平面、$(\rho N)_u$ 沿 N，所以

$$R(H(Y_f,\rho N))=0. \tag{7}$$

mixed 分量可能非零，不能从完整 forcing 删除；这里只是在常态的 characteristic 密度中消失。一次第三场为 $U_1=-\rho(q,w)N-Y_{c_1}$。$Nw$ 的 physical s 导数另产生 N 零次项，它与相关法向导数正交，不添 $P_2$。因此第四密度的 N 一次项准确为

$$-r(b_0,w)/8+r(q,c_1)/4.$$

吸收真实基长度，令 $\mathcal A=\ell r=\Phi_{\ell M_{\rm density}}$，并记 $a=\mathcal A(q,q)$。全部右侧使用段首值：

$$w_{\rm out}=w+a,\qquad
v_{\rm out}=v-\mathcal A(q,w)-\tfrac12\mathcal A(q,a), \tag{8}$$

$$b_{0,\rm out}=b_0,\qquad c_{1,\rm out}=c_1-\mathcal A(q,b_0),$$

$$\boxed{\Delta P_2=
-\mathcal A(b_0,w)/8+\mathcal A(q,c_1)/4
-\mathcal A(b_0,a)/16
-\mathcal A(q,\mathcal A(q,b_0))/8.} \tag{9}$$

式 (9) 来自 $w(t)=w+ta,c_1(t)=c_1-t\mathcal A(q,b_0)$ 的真实积分。R62 的局部 drift 位于 density 的 N 零次，乘 bulk 长度进入 $P_1$，不属于 (9)。

桥不改 w,v。故交替 (6)、(8)、(9)，从共同零锚开始，整个纯 $P_2$ 对各桥 M **准确线性**，并包含全部下游作用。相邻而中间没有 bulk 的桥段，可先把 M 相加。

## 4. 一个互反 pair 的五项 Gamma

取同一 $(h,d)$ 的两个等时长常态，使其积分算子为 $+\mathcal A,-\mathcal A$；[R62](../results/R62-reciprocal-constant-states-and-fourth-local-drift.md) 的 $k=\pm1$ 给出这种真实常态 pair。两段之间允许一座真实桥，记其算子 $\mathcal E=\Phi_E$。令

$$a=\mathcal A(q,q),\qquad e=\mathcal E(q,q).$$

从该 pair 的最高历史 $w=v=0$ 开始，第一段后 $w=a,v=-\mathcal A(q,a)/2$。桥由 (6) 给 $b_0$ 增量 e、$c_1$ 增量 $-\mathcal E(q,a)$。将其代入第二段 (9)，得到内部桥的准确 $P_2$ 函数

$$\boxed{\begin{aligned}
\Gamma_{\mathcal A}(\mathcal E)
={}&\{\mathcal A(a,e)-\mathcal E(a,a)\}/16\\
&+\mathcal A(q,\mathcal E(q,a))/4\\
&-\mathcal E(q,\mathcal A(q,a))/8\\
&-\mathcal A(q,\mathcal A(q,e))/8 .
\end{aligned}} \tag{10}$$

任何来自更早桥的入 $b_0,c_1$ 在完整 $+\mathcal A,-\mathcal A$ pair 中相消；这是把 (9) 连用两次的恒等式，不要求这些入值为零。因此相邻 pair 之间的桥不直接贡献 $P_2$，但它们仍进入总二阶矩和消元项，不能删除。

$\Gamma$ 对 $\mathcal E$ 线性、对 $\mathcal A$ 二次，故

$$\Gamma_{-\mathcal A}(\mathcal E)=\Gamma_{\mathcal A}(\mathcal E),\qquad
\boxed{\Gamma_{\mathcal A}(\mathcal A)=0.} \tag{11}$$

后一式中前两项同类相消，剩余三项系数为 $1/4-1/8-1/8=0$。不需要两个算子可交换。

## 5. 真实二阶消元的关键 1/3

最高三次周期单 bulk 的完整增量是

$$\begin{aligned}
\Delta P_3={}&-\mathcal A(w,w)/16-\mathcal A(w,a)/16-\mathcal A(a,a)/48\\
&+\mathcal A(q,v)/4
-\mathcal A(q,\mathcal A(q,w))/8
-\mathcal A(q,\mathcal A(q,a))/24 .
\end{aligned} \tag{12}$$

其 w,v 更新为 (8)。整个最高三角流在 $+\mathcal A,-\mathcal A$ 下对**任意入最高历史**互逆。

将 pair 两个积分算子作一阶改变，记总改变为 $\mathcal S=\delta\mathcal A_++\delta\mathcal A_-$。反对称改变保持准确互逆，因此 pair 的三次周期导数只依赖 $\mathcal S$。可固定第一段，把第二段改成 $-\mathcal A+\varepsilon\mathcal S$。令 $s=\mathcal S(q,q)$，直接微分 (12) 得

$$\begin{aligned}
D P_{3,\rm pair}(\mathcal S)
={}&\{\mathcal A(a,s)-\mathcal S(a,a)\}/48\\
&+\mathcal A(q,\mathcal S(q,a))/12\\
&-\mathcal S(q,\mathcal A(q,a))/24\\
&-\mathcal A(q,\mathcal A(q,s))/24.
\end{aligned}$$

所以

$$\boxed{D P_{3,\rm pair}(\mathcal S)=\Gamma_{\mathcal A}(\mathcal S)/3.} \tag{13}$$

此处 $\mathcal A$ 已含真周期长度；在把几何 k 参数变成 $\mathcal S$ 时，必须同时微分周期，不能只微分密度。

对四组 R62 状态，令 $T=\sqrt2\pi$，

$$w_j=((1+d_j^2)/(4h_j),d_j/2,h_j/4),$$
$$u_j=(0,1/h_j,-2d_j/h_j^2),\qquad
v_j=(-2,2d_j/h_j,-2(d_j^2-1)/h_j^2).$$

单个正 bulk 积分矩阵是 $A_j=T\,w_jv_j^T$。R62 两参数对 pair 总矩的准确导数列是

$$J_{j,\alpha}=4T\,w_ju_j^T,\qquad
J_{j,\beta}=T\,w_jv_j^T=A_j. \tag{14}$$

四组八列给无迹矩阵空间的基。令 $\Pi_j$ 为沿这组基取第 j 两列分量的线性投影，$\sum_j\Pi_j=I$。

## 6. 全四块闭式与 28 个 profile 无关的充分矩条件

记单 P 的全部桥矩总和为 $M_{\rm all}$，第 j 个正/负 bulk 之间的内部桥矩为 $E_j$。准确二阶消元使第 j 个 pair 的总积分算子改变为 $-\Phi_{\Pi_jM_{\rm all}}/N+O(N^{-2})$。结合 (10)、(13)，单 P 的有效纯函数是

$$\sum_{j=1}^4
\Gamma_{\mathcal A_j}\!\left(
\Phi_{E_j-\Pi_jM_{\rm all}/3}\right).$$

整个 R45 四块词中，每个基准 pair 的最高流对任意入值为恒等，每块末最高历史回零；倒行 pair 把 $\mathcal A_j$ 变为 $-\mathcal A_j$，而 (11) 为偶。因此直接从全词递推得到

$$\boxed{\mathcal C_{{\rm eff},-4}^{\rm four}
=4\sum_{j=1}^4
\Gamma_{\mathcal A_j}\!\left(
\Phi_{E_j-\Pi_jM_{\rm all}/3}\right).} \tag{15}$$

这个 factor 4 没有借用需要较低阶已支付时的泛型 full=4single 定理。未付的有限 N 低阶缺陷不能据此在其他通道或次数清零。

由 (11)，一个**profile 无关的充分线性矩目标**是

$$\boxed{E_j-\Pi_jM_{\rm all}/3\in\operatorname{span}\{A_j\}
\quad(j=1,\ldots,4).} \tag{16}$$

每组是八维无迹矩阵空间模一个已知方向，给七个条件，共 28 个。它不是必要条件：不同 j 的 Gamma 函数仍可能相消，Gamma 也可能有更大的核。

为直接实现，记八列矩阵为 J，按固定八坐标读取矩阵，令 $m=J^{-1}M_{\rm all}$、$e_j=J^{-1}E_j$。则 (16) 等价于

$$e_{j,k}=0\quad(k\notin\{2j,2j+1\}),\qquad
e_{j,2j}-m_{2j}/3=0, \tag{17}$$

这里 j 从 0 计，$e_{j,2j+1}$ 不受该门约束。注意 $\beta$ 列正好是 $A_j$，所以总二阶修正的该分量不影响 (15)。

这给下一实际 Actions 一个明确的小型问题：使用真实端点保持 h 控制，只积分各桥低导数 M，评价 (17) 的整个 28 维残差、绝对步长 Jacobian、数值秩、正 h 参数盒和冻结加密。如果得到残差下降，只是该有限矩门的数值进展；若要准确支付仍需验证求根/IFT。没有在这里假定 h 控制的 M 像满维。

## 7. 尚未支付的范围与当前证据

(16) 可让整个纯 leading $N^2$ 周期对任意共同 profile 为零，因此这一步不需要重新积分或优化已知失败的旧 R52 profile。它仍没有支付：

- 其余第四 Fourier 通道及全部第四 ruling；
- 纯通道的 $P_1,P_0$、高阶相容性或收敛；
- 真实有限 N 零二阶求根、闭合、嵌入、reach 和主课题宏观位移。

局部 drift 的纯复 R65 障碍位于不同的理想无桥 $N$ 项，本稿没有把它抹去。真实桥可以影响较低项，但尚未构造使它们共同消失的桥。

矩阵浮点评价必须保留原始 trace、源控制身份及加密误差；不能改最后一项强行无迹。profile 仍在同一个实际物理区间和右锚上。新闭式本身是准确代数，但任何未来浮点小残差不是严格解或区间证书。

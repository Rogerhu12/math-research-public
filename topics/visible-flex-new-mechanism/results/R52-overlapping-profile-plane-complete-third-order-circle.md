# R52：真正重叠profile平面的完整三阶圆

日期：2026-11-14。literature 推导，repo_sources 独立逐项核，root 全文复核。独立完整正向构造。几何仍用 [R45 单P零算子及四块倒行](R45-reversal-four-block-third-period-cancellation.md)，调用 [R46 逐点恢复公式](R46-eight-packet-complete-third-order-circle.md)；不使用新的数值研究计算。

[R50 不交profile平面的第四阶正障碍](R50-disjoint-profile-circle-fourth-order-positive-obstruction.md)不能靠常数 O(2) 换基绕过。本稿构造一个任意常数换基后仍在同一区间重叠的新平面，并重新支付它新增的交叉 forcing。所得仍是三阶形式圆；四阶与有限非零 epsilon 的精确族尚未解决。

## 1. 一个准确三矩、无法旋回不交的基本 packet

取固定偶函数

$$\eta(x)=\begin{cases}\exp\{-1/(1-x^2)\},&|x|<1,\\0,&|x|\ge1.\end{cases}$$

它在开区间 (-1,1) 严格正，零延拓为 C-infinity。考虑准确四维实空间

$$V=\eta\,\operatorname{span}\{1,x^2,x^4,x^6\}.$$

定义两个对称双线性形式

$$I_0(\phi,\psi)=\int\phi''\psi'',\qquad
I_2^*(\phi,\psi)=\int x^2\phi''\psi''+2\int\phi'\psi'.$$

I0 在 V 上严格正定，因为二阶导数为零的紧支撑仿射函数只能为零。对自伴算子 $I_0^{-1}I_2^*$ 选 I0-正交单位特征基 $e_1,\ldots,e_4$，特征值按
$\lambda_1\le\lambda_2\le\lambda_3\le\lambda_4$ 排列。这里矩阵由指定 eta 和四个单项式的有限准确积分定义，没有把离散数值特征向量当精确定义。

若 $\lambda_4>\lambda_1$，置 $\mu=(\lambda_2+\lambda_3)/2$ 并定义

$$f_0=\sqrt{\frac{\lambda_4-\mu}{\lambda_4-\lambda_1}}e_1
+\sqrt{\frac{\mu-\lambda_1}{\lambda_4-\lambda_1}}e_4.$$

若 $\lambda_3>\lambda_2$，取 $g_0=(e_2+e_3)/\sqrt2$；若两者相等，取 $g_0=e_2$。若全部四特征值相等，则直接取 $f_0=e_1,g_0=e_2$。

这些定义完整覆盖退化情形，并准确给

$$I_0(f_0,f_0)=I_0(g_0,g_0)=1,\qquad I_0(f_0,g_0)=0,$$

$$I_2^*(f_0,f_0)=I_2^*(g_0,g_0)=\mu,\qquad I_2^*(f_0,g_0)=0$$

（全退化情形取该共同特征值为 mu）。所有函数为偶函数，故另外三个含 x 的矩

$$I_1(\phi,\psi)=\int x\phi''\psi''$$

在所选两维平面上全部为零。于是 $f_0,g_0$ 准确满足完整三矩圆条件。

**真正重叠。** 任意非零实线性组合都是 eta 乘非零偶多项式，所以在 (-1,1) 只可能有有限个零点。任意正交换基后的两个基向量都非零，因而二者在同一个开稠密集上同时非零。没有常数 O(2) 变换能把这个平面变成两个支撑不交的 profile。

## 2. 新增交叉 forcing 的两侧 collar 确实支付

记 $Y_f,Y_g$ 为线性 infinitesimal isometry，定义两个二阶 forcing

$$H_d=(dY_f)^2-(dY_g)^2,\qquad
H_c=\mathcal S(Y_f,Y_g).\tag{1}$$

对单个基本 packet，三矩相等使 Hd 的三条右尾矩差在左 collar 全零；三交叉矩全零使 Hc 的三条极化右尾矩也在左 collar 全零。右 collar 的尾值由共同锚定义为零。

已有完整 ruling 原函数、characteristic RHS 和恢复公式对 H 线性，所以其单平方公式准确极化到 Hc。全零二阶周期算子也通过极化给 Hc 的整个周期函数为零。因此存在周期、双 collar 为零的

$$\mathcal L_XZ_d=H_d,\qquad\mathcal L_XZ_c=H_c.\tag{2}$$

这里两者都用同一右 xi 锚以及同一 P 起点的 W=0 规范。单 P 的全零算子使两个 W 在 P 末端均为零；四块倒行恢复使两个场均为反射偶场。两场在自己的 packet 包络外准确为零。

不能只用 Hd 而漏掉 Hc：对本稿真正重叠平面，Hc 一般逐点非零。

## 3. 同一八 packet 差分同时支付四条第三 ruling

将基本 pair 平移 t，仍用共同锚。对 phi=f0 或 g0、j=d 或 c，定义规范第三 forcing

$$H_{\phi j}=-\mathcal S(Y_\phi,Z_j).$$

此处沿用 R46 的 e=h(xi+omega)−k、Q=1+e² 及其二阶 primitive W、eta0。已有逐点公式的极化给：在移回基本坐标后，二阶 W 的平移次数至多四，eta0 至多三；第三 ruling 的完整表达为

$$\int\phi'''\left(eW-\frac{Q}{2h}W_\xi-\frac{Q}{h^2}\eta_0\right)d\xi.$$

所以每一个 $K_{\phi j,t}(s)$ 都是 t 的次数至多六的多项式。这里有四条函数，不再只有不交构造中的两条。

取八个互不交的完整 packet，$t_j=t_*+jL$，L>2，并用准确实幅度

$$a_j=(-1)^j\binom7j^{1/3},\qquad j=0,\ldots,7.$$

定义

$$f=\sum_{j=0}^7a_jf_0(\xi-t_j),\qquad
 g=\sum_{j=0}^7a_jg_0(\xi-t_j).\tag{3}$$

可以共同仿射缩放到任何给定物理活动区间，并保留严格外 collar。每一个完整 packet 的 Hd、Hc 都已三矩配平，因此两个二阶解按 $a_j^2$ 分解，且不同 packet 的二阶场无交叉项。于是四条第三 ruling 都按 $a_j^3$ 相加。

第七有限差分恒等式

$$\sum_{j=0}^7(-1)^j\binom7j(t_*+jL)^m=0,
\qquad m=0,\ldots,6$$

同时给

$$K_{fd}=K_{gd}=K_{fc}=K_{gc}\equiv0.\tag{4}$$

这一步没有假设基本 packet 内 f0、g0 不交；所需不交只是不同完整 packet 的包络互不相交。

四块几何上 Yf、Yg 都是反射奇场，Zd、Zc 都是反射偶场，故四个第三 forcing 都是反射奇的。完整 rho 和 characteristic 密度按同一锚反转，四条整个周期函数同时为零。结合 (4)，完整 range 给四个真实光滑周期双 collar 解

$$\begin{aligned}
\mathcal L_XW_{fd}&=-\mathcal S(Y_f,Z_d),&
\mathcal L_XW_{gd}&=-\mathcal S(Y_g,Z_d),\\
\mathcal L_XW_{fc}&=-\mathcal S(Y_f,Z_c),&
\mathcal L_XW_{gc}&=-\mathcal S(Y_g,Z_c).
\end{aligned}\tag{5}$$

全局 f、g 仍不能被常数 O(2) 旋转成不交支撑：只需限制到任意一个非零 packet 内，就回到 §1 的多项式论证。

## 4. 指定旧目标时必须使用的正确全圆公式

取固定目标

$$g_\varepsilon=(X+\varepsilon Y_f)^*e
=g_X+\varepsilon^2(dY_f)^2.$$

写 $c=\cos\theta,s=\sin\theta$。准确选择

$$Y_\theta=cY_f+sY_g,$$

$$\boxed{Z_\theta=s^2Z_d-csZ_c,}\tag{6}$$

$$\boxed{W_\theta=s^2(cW_{fd}+sW_{gd})
-cs(cW_{fc}+sW_{gc}).}\tag{7}$$

由 (1)–(2)，

$$\mathcal L_XZ_\theta
=s^2(H_f-H_g)-csH_c
=H_f-(dY_\theta)^2.$$

由 (5)，

$$\mathcal L_XW_\theta=-\mathcal S(Y_\theta,Z_\theta).$$

因此

$$F^{[3]}_{\varepsilon,\theta}
=X+\varepsilon Y_\theta+\varepsilon^2Z_\theta+\varepsilon^3W_\theta$$

对同一个 g-epsilon 的准确误差为

$$\varepsilon^4\{(dZ_\theta)^2+\mathcal S(Y_\theta,W_\theta)\}
+\varepsilon^5\mathcal S(Z_\theta,W_\theta)
+\varepsilon^6(dW_\theta)^2.$$

所有相位的周期性、双 collar 与三阶方程均已完整支付，且 theta=0、pi 仍准确接到 $X\pm\varepsilon Y_f$。省略 (6) 的交叉通道会改变固定度量，这不是可选的规范简化。

## 5. 后续尚未支付

本构造通过三阶，不受“不交 profile 平面”的第四阶正性定理直接覆盖。它并未证明第四阶成功：新增交叉通道会进入第四 ruling 和周期函数，必须在同一锚下重新推导。

一个有用但尚未作为本稿结论采用的整理是复 profile $q=f+ig$：三矩圆等价于三条复总矩为零，$Z_d+iZ_c$ 解 $(dY_q)^2$。这个记号可以整理第四阶的二次、四次相位项，但不能把实平方和擅自换成模平方并宣称一般重叠情形同号。

此外仍缺有限等距族、闭曲面嵌入及题目宏观比例。几何可能自交，已有长圈有限 N 数值实例也已单独被厚度预算排除；本稿只推进形式等距机制，不把该实例重新作为厚度候选。

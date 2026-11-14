# R133：真实 moving 曲率角的完整均值二维能量与普通源

**已证明并实际完成（全原参数、全角、全 Fourier 变分）。** 在保存的
$\alpha=.75$、M256 accepted000 互逆中心及其实际

$$\nu=-2443457753738987/72057594037927936$$

上，完整 $[0,.238]$ 的1528条径向闭盒、每盒4096个闭角单元和1013个真实
PPoly 接缝都已支付。以下是 moving 方程自身 Jacobi 的完整 Cauchy/source
界，包含允许的独立平均；没有把中心当作已解 PDE。

令 $q=\sqrt{-K}$，$\mathcal E=\|(h_1,qh_2)\|_{L^2_\phi}$，
$M=|\langle h_2\rangle_\phi|$。正向整个区间及其任意子区间可用同一个
正矩阵上界

$$
\boxed{U_f\le
\begin{pmatrix}
2.333679075&1.184573700\\
0.115288217&1.094830185
\end{pmatrix}.}\tag{E.1}
$$

显示数逐项向上放宽。报告保存全部320位有向值。对完整允许初值，
$M(0)\le\mathcal E(0)/q(0)$，所以正向全区间增益为

$$\boxed{\sup_r\mathcal E(r)<3.614669115\,\mathcal E(0)}
\tag{E.2}$$

（齐次无源、无仿射跳的情形）。完整普通源
$F(r)=\|(f_1,qf_2)\|_{L^2_\phi}$ 的 $L^1_r$ 费用为

$$\boxed{11.712299133\int_0^{.238}F(r)\,dr.}\tag{E.3}$$

真实中心的全部 moving 仿射接缝另加至多 $1.839\cdot10^{-13}$ 的正向
全区间能量。反向的完整初值与普通源统一增益均小于 $47.305976121$，
其实际接缝全区间费用小于 $2.351\cdot10^{-12}$。

如果真实腰平面、常速和转角整数1的完整条件已付，且 $a(0)$ 固定，则
$D(0)=-1/a(0)$、$m(0)=-a(0)$，同度量变分确有 $z(0)=0$。**只有在这个
已付的边界子空间上**，(E.2) 可改为 $2.333679075$，即 (E.1) 的左上项。
沿径向的均值反馈仍完整保留，没有把均值从方程中删除。

## 1. 实际连续对象

目标使用原完整 unit primitive 和所有无限尾；全
$\eta\in[-10^{-9},10^{-9}]$ 保留。$[0,.2]$ 来自原493条完整目标闭盒，
$[.2,.238]$ 来自已完成真实根邻域系数缓存。紧支撑度量变化始终用
$E_\nu=Ee^{\nu h}$ 及其真实 $K_\nu,K_\nu'$ 重新计算，不在支持内部
套用旧 $g_0$。

完整候选的每一 shard 由 SHA、数组形状、精确二进制节点和覆盖验证。
将其全部 PPoly 节点、原目标 scalar germs、紧支撑接缝与终点 $.238$
取共同精确有理分割，得到1528条闭盒。没有遗漏某个狭小的原标量片。

在每条闭盒上，$U,V$ 的每个有限 Fourier 系数按实际三次多项式用 Arb
Horner 包络；构成 $u=\alpha U$ 和 $v=s+\alpha V$，其中实际 $s$ 仍含
全部目标误差。全角通过后得到统一

$$|v|>0.1145624599,\qquad q>0.1263057562,$$

$$R<1.888896718,\quad L<3.624465868,\quad
\|v\|_{L^2_\phi}<1.262902210.\tag{E.4}$$

最后一个范数使用准确恒等式
$\langle v^2\rangle_\phi=\langle v\rangle_\theta/D$，保留完整平均。
上述界描述同一个近似中心和目标的真实系数，未宣称其有限 BVP 或非线性
PDE 已收敛。

## 2. 真 $D,m,R,L$ 与闭角平均

每条径向盒完整包住 $u,v,u_\theta,v_\theta,v_{\theta\theta}$ 的整个角圆。
先逐闭格证明 $v<0$，再形成真实 $C=1/v$。其平均 $D=\langle C\rangle$
同时用两个独立有效的界：

1. 每个相同长度闭角单元上的完整 $C$ 区间求平均；
2. 全节点的有向 $1/v$ 平均，加完整周期梯形余项
   $\ell^2\|C_{\theta\theta}\|_\infty/12$，其中
   $\ell=(\pi/2)/4096$。

余项中的真实二阶导按同一角单元计算

$$C_{\theta\theta}=2v_\theta^2/v^3-v_{\theta\theta}/v^2.$$

取这两个包络的交，证明 $D<0$，再取实际 $m=1/D$。所以没有只用
$1/\min|v|$ 冒充真实平均。准确换角公式为

$$Q_\phi=DvQ_\theta,\qquad
\langle S\rangle_\phi=
\frac{\langle u^2/v+Kv\rangle_\theta}{D},\quad S=u^2+Kv^2.$$

因此在**同一角单元**内先形成

$$R^2=u^2-Kv^2,\qquad
L^2=D^2v^2(u_\theta^2-Kv_\theta^2),$$

再取上界。实际 $d_\phi=\beta(\langle S\rangle_\phi-S)$ 也完整保留其
平均与角相关性。整个程序没有把物理角导数误标成 moving 角导数。

## 3. 二维完整传播及全普通源

直接消费 moving 定理 M.14–M.15：每条闭盒对

$$A(r)=\begin{pmatrix}
\max(G_1,G_2)+|\beta|RL/2&\gamma qL\\
2|\beta m|R&\beta(1-\langle S\rangle)
\end{pmatrix}$$

取逐项实际上界。非对角非负，对角保留其符号。每条常系数二维矩阵以
Arb 矩阵指数化，按完整径向顺序相乘；反向则按相反顺序使用已证明的
反向对角。平均和第一分量在每个接口连续带入，未在分段处重新设初值。

为了同时控制**任意子区间**和普通源插入点，把每条矩阵的两个对角替换
为它们与0的较大值，得全非负矩阵 $B_j$。于是
$e^{tB_j}\ge I$，且它逐项控制本盒任何较短真实传播。完整有序积

$$U=\prod_j e^{\Delta r_j B_j}$$

逐项控制任意连续子积及任意盒内起止的传播：删除两端因子时，它们均
$\ge I$，不会使较短传播变大。这样 (E.1) 是整个区间的完整 kernel
上界，而不是只在最终点的增益。

对允许的全部 Fourier 与完整平均，比较向量满足

$$
\binom{\mathcal E(r)}{M(r)}\le
U_f\left[
\binom{\mathcal E(0)}{M(0)}+
\int_0^r\binom{F(s)}{F(s)/q(s)}ds+
\sum_{r_i\le r}\binom{J_{E,i}}{J_{M,i}}
\right].\tag{E.5}
$$

报告同时保存保留有符号对角的终点矩阵，以及上述全子区间矩阵。
利用实际 $q(0)$ 下界与全区间 $q$ 下界，分别得到 (E.2)、(E.3)。反向全
子区间矩阵的外放小数为

$$U_b\le\begin{pmatrix}
41.112611840&0.782257560\\
2.222866583&1.019840347
\end{pmatrix}.$$

系数在每个有限径向片上具有完整有界角导，主部严格对称双曲，原函数与
均值项是已付有界算子。标准短时 Volterra 构造、该完整能量以及有限接口
拼接给所有允许 $L^2$ 初值、$L^1_rL^2_\phi$ 源的唯一线性 Cauchy 解。
这一步没有将变分限制在候选的M256 Fourier 支撑上。

## 4. 真 moving 仿射接缝

每个物理候选跳 $\Delta u,\Delta v$ 从原 dyadic 三次多项式的左右端点
**精确有理求值**，再取全有限 Fourier $A_0$ 范数。设这两个上界为
$\epsilon_u,\epsilon_v$，两侧统一 $|v|\ge g$、$|v|\le V$、
$D_-\le|D|\le D_+$。准确商恒等式给

$$\|\Delta C\|_\infty\le\epsilon_v/g^2,
\qquad |\Delta D|\le\epsilon_v/g^2.$$

故两个度1角图的导数差至多

$$W_\Delta=\frac{\epsilon_v}{g^2}
\left(\frac1{D_-}+\frac1{gD_-^2}\right).$$

反射固定角原点，两侧角图的差为周期零均值导数的原函数，故一个充分界为

$$\|\phi_+-\phi_-\|_\infty\le\pi W_\Delta/4,
\qquad\|\phi_+^{-1}-\phi_-^{-1}\|_\infty
\le VD_+\pi W_\Delta/4.$$

再分别乘两侧实际 $u_\theta,v_\theta$ 上界并加原物理跳，给同一个
$\phi$ 圆上真实 $[\widehat Q]$ 的两个分量。能量按
$\sqrt{J_u^2+q^2J_v^2}$、平均按 $J_v$ 付费。全部1013个接缝实算后

$$\sum J_E<5.633047\cdot10^{-14},\qquad
\sum J_M<4.426156\cdot10^{-14}.$$

这些向量按同一完整二维系统传播，得到开头所列接缝费用。它们是 M.16
的完整跳，包括逆角复合；不是把原物理系数小跳直接称作 moving 跳。

## 5. 两种完整角算术与直接和误差证明

前899个完成行使用既有 directed FFT 和完整角 Taylor 内核。后629行使用
另一个明确的直接三角和内核；两者均证明整闭格。最终消费者分别核对
其真实 source/kind，不冒名统一成一次旧运算。

直接内核先以320位 Arb 包住所有基本根 $e^{2\pi i k/N}$，再以有向区间
复乘形成每个 $j$ 次幂，取精确 dyadic 中心及完整根误差。实际 Fourier
系数（包括径向盒和参数变化）同样选一个 dyadic 中心，完整误差在相应
物理角导数阶上单独支付。

对每个节点和每个导数列，代码按频率依次执行

$$s\leftarrow s+(a_j\sin_j+b_j\cos_j),$$

恰有两次乘法、两次加法，因此 $n=4M$。取比最近舍入 unit roundoff
更宽的 $u=2^{-52}$，$\gamma_n=nu/(1-nu)$。对所有精确 dyadic 输入，
实际计算值与精确所选有限和的差至多

$$\gamma_n\sum_j(|a_j\sin_j|+|b_j\cos_j|)
+\frac{n2^{-1074}}{1-nu}.\tag{E.6}$$

这由每步 $|\operatorname{fl}(x)-x|\le u|x|+2^{-1074}$ 逐步归纳得到。
程序验证 gradual-underflow 可用及所有中间结果有限。再加全部系数中心
误差和每个三角幂误差，就包住真实节点值；不依赖某个浮点 FFT 的未付
黑盒误差，也不依赖 BLAS 的求和顺序。

实际节点上的 $f,f',f''$ 都单独包住，闭格半宽 $h=\pi/(4N)$ 的余项为
$h^3\|f'''\|_{A_0}/6$。因此整个角单元都有界。特别是
$v_{\theta\theta}$ 所需的高阶余项仍用完整有限五阶导数，未对只有零阶
费用的区间误差直接求导。实现中的正弦、余弦和导数符号另用两模显式
公式的640个节点/闭格端点门实际核对通过；真正证书仍来自上述全部闭格
运算，不来自这些检查点。

## 6. 真实中断、续算和完整性

第一版在首盒因 Python `int / Box` 不支持而失败；原源码与原 false 报告
均保留。v2 把两处写成显式 `Box(1.) / Box`，真实完成了前599行。随后
工具句柄不可用，原报告为 `complete=false, failure=null`；没有观测退出
码，所以未推断终止原因。

这些行只在整个实际系数闭盒计算返回后 append。新独立完整片依次支付
$[599,749)$、$[749,899)$、$[899,1199)$、$[1199,1528)$，均正常完成。
最后消费者重新构造完整1528行公共分割，核候选/目标/参数/原始行号/
germ/真实目标系数，要求无间隙、无重叠且整个并集完成，再连续运行所有
二维传播和接缝。没有把任何旧 false 标志改为 true。

最终报告已经保有五份大检查点/分片报告的全部原数学行，因此不再把这
约2.34MB重复数据另行提交。原文件仍原样留在本地，未删除、未改标志。
一个28,621字节的 reconstruction manifest 保存各自 source/kind/原 SHA、
完整与失败状态、实际行号范围、命令以及原有序报告头。只从最终完整报告
抽取原行、去掉最终新增的 $\|v\|_{L^2_\phi}$ 字段并恢复原 `common_row`
后，已经实际重建五份原压缩文件，**每份全部原字节和 SHA 都相同**。这
既保留了原 false 状态，也不要求仓库重复保存可确定恢复的大中间数据。

## 7. 可复跑文件和准确范围

数学及完整消费者：

- `scripts/fourfold_codazzi_moving_mean_energy_prefix.py`（首个实际 API 失败）
- `scripts/fourfold_codazzi_moving_mean_energy_prefix_v2.py`（599行原检查点）
- `scripts/fourfold_codazzi_moving_mean_energy_rows.py`
- `scripts/fourfold_codazzi_moving_mean_energy_direct_rows.py`
- `scripts/fourfold_codazzi_moving_mean_energy_complete.py`
- `scripts/fourfold_codazzi_moving_energy_reconstruction_manifest.py`

仓库保留的原生输出和轻量恢复材料：

- `notes/2026-11-13-R133-moving-mean-energy-alpha075-r0238-native.json.gz`
- `notes/2026-11-13-R133-moving-mean-energy-alpha075-r0238-complete-native.json.gz`
- `notes/2026-11-13-R133-moving-energy-reconstruction-manifest.json`

以下五份原大报告仅本地留存；最终完整报告含其全部数学行，manifest 可
确定恢复其完整原字节：

- `notes/2026-11-13-R133-moving-mean-energy-alpha075-r0238-v2-native.json.gz`
- `notes/2026-11-13-R133-moving-mean-energy-alpha075-r0238-rows0599-0749-native.json.gz`
- `notes/2026-11-13-R133-moving-mean-energy-alpha075-r0238-rows0749-0899-native.json.gz`
- `notes/2026-11-13-R133-moving-mean-energy-alpha075-r0238-direct0899-1199-native.json.gz`
- `notes/2026-11-13-R133-moving-mean-energy-alpha075-r0238-direct1199-1528-native.json.gz`

在没有这些本地中间文件的新 checkout，可先运行恢复脚本的 `--manifest`
模式，把最终完整报告和上述 manifest 传入，并使用 `--restore-dir notes`，
再按原消费者命令复现。恢复器拒绝覆盖任何已有报告。

最终完整消费者正常完成，用时约31.16秒；大闭格计算的实际耗时分别保留
在原始报告中。

本篇给真实 moving Jacobi 的完整零阶 Cauchy 和普通源合同。完整连续中心
残差没有在本篇重新计算；若从物理残差搬入，须完整使用 M.7 的
$R+I(R_2/v)Q_\phi$。若把能量授给物理 Jacobi，则还须消费残差敏感桥的
B.10。正型帽、实际曲线 Airy 端口的 balanced 权及返回小除数也没有被
本篇自动解决；下一接线使用同一 $.75$ 中心并逐项支付这些接口。

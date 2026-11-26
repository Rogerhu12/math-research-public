# R236 原 M12 同一实际场的局部连续度量预算

状态：完整充分条件及可执行严格验证器。它只重包同一保存场，不改场、原固定度量或端口；尚未消费已结束 run45815969723 的原系数，不能预报任何实际新场通过门槛。

## 1. 准确对象与所改的估计

令 $X$ 为 R21/R230 的原准确 common-cut 完整闭面，$g$ 为原固定度量，已有
$$
\|g^{-1/2}(X^*e-g)g^{-1/2}\|_{\rm op}\le d,
\qquad d=2.57212\times10^{-8}.
$$
R226 数值供应器的参考面是 $X+C$，其中 $C$ 为其明确支付的中央归一化两 jets 修正。实际待验证场是
$$
Y=X+C+W.
$$
本程序从 `field.npz` 的**实际 binary64 系数与节点所定义的准确实数场**读取 $W$，不以抽样值替代其定义。它逐单元插入节点、细分 Bernstein 多项式只是恒等表示变换，既不重拟合，也不改变 $g$、$W$ 或端口。

R226 的全局乘积界将全场最大的径向系数、最大的中央角逆导数和最小真 cuff 半径同时相乘。本程序保留所在径向单元的 $H$、$f$ 下界，并在角向先形成导数向量的**准确平方范数 Fourier 多项式**。因此其改进来自同一场的更精确包界，不是一次新的数值求解。

## 2. Bernstein–Jensen 引理

在一个单位径向区间 $[a,b]$，将五次场准确写为
$$
W(z,\theta)=\sum_{i=0}^5 B_i^5\!\left(\frac{z-a}{b-a}\right) C_i(\theta).
$$
程序以有理 Boehm 插入把所有内部节点补到重数 $5$，随后可作有理中点 de Casteljau 细分。原自由系数两端各补三个准确零控制行，故中央及真 cuff 两 jets 仍为零。

令
$$
D_i=\frac5{b-a}(C_{i+1}-C_i),\quad 0\le i\le4,
$$
并将四次导数升到五次：$\widetilde D_0=D_0$、$\widetilde D_5=D_4$，以及
$$
\widetilde D_i=\frac i5D_{i-1}+\frac{5-i}{5}D_i,
\quad 1\le i\le4.
$$
于是 $W_z$ 与 $W_\theta$ 具有**同一组非负和为一的 Bernstein 权**，其对应控制向量分别为 $\widetilde D_i$、$C_i'$。

写准确公共径向图为 $q=Tz$、$ds=H(q)dq$。中央角图满足
$$
du=\rho_0(\theta)d\theta,
\qquad \rho_0=\frac{J(\theta)}{\bar a},
\quad J=|\gamma'(\theta)|,
\quad \bar a=\frac1{2\pi}\int_0^{2\pi}J.
$$
其中 $J^2$ 是原中央有限 Fourier 曲线的准确三角多项式，$\bar a$ 的严格积分盒由 R226 提供。本程序不把数值求积值充作准确 $\bar a$。

若此径向片 $TH\ge L>0$、$f\ge f_*>0$，则对每个固定 $\theta$，由平方范数的凸性，
$$
|W_s|^2+\frac{|W_u|^2}{f^2}
\le \max_{0\le i\le5}
\left\{\frac{|\widetilde D_i(\theta)|^2}{L^2}
+\frac{\bar a^2|C_i'(\theta)|^2}{f_*^2J(\theta)^2}\right\}. \tag{1}
$$
这里先把六维向量 $(\widetilde D_i/L,\bar a C_i'/(f_*J))$ 用同一 Bernstein 权求和，再用 Jensen；没有把两个不同位置的导数峰值强行相加。右侧的平方根控制 $dW$ 在 $g$ 下的 Frobenius 范数，因而也控制其算子范数。

## 3. 保留角向系数抵消的严格实现

实际基的平面分量为 $\sum_m c_m e^{im\theta}$，$m=3k+1$、$c_m\in\mathbb R$；高度分量为 $\sum_n h_n\cos(n\theta)$，$n=3k$。平面平方范数由自相关
$$
\left|\sum_m c_me^{im\theta}\right|^2
=\sum_{m,n}c_mc_ne^{i(m-n)\theta}
$$
计算。高度先写成真实 Laurent 系数 $h_0$、$h_{\pm n}=h_n/2$，再同样自相关；角导数先乘各自的有符号频率。故没有丢掉不同 Fourier 模式之间的正负抵消。

所有平方范数及 $J^2$ 都是 $x=3\theta$ 的实偶余弦多项式。只需覆盖 $x\in[0,\pi]$，真实 D3 与反射对称给出整个材料圆周。

对 $P(x)=\sum_k p_k\cos(kx)$，每个闭盒中心 $x_0$、半宽 $h$，程序使用
$$
P(x)\in P(x_0)
+\sum_{j=1}^{D-1}\frac{P^{(j)}(x_0)}{j!}[-h,h]^j
+[-R_D,R_D],
\quad
R_D=\frac{h^D}{D!}\sum_k |p_k|k^D. \tag{2}
$$
程序以绝对值对中间项向外包界；常数项与各阶中心导数仍由有符号 Fourier 和计算。默认在该反射扇区用 $128$ 个闭盒，$D=8$。$\pi$、sin/cos 及其尾项直接复用 R220 的 $96$ 位整数区间实现。没有 NumPy 三角函数参与判定任何严格界。

精确 Bernstein 有理系数先向下取为 $2^{-96}$ 格点。所得近似系数的自相关及角 Taylor 计算都是整数；每个原系数与格点的准确差另外累加。若两个导数控制行的向量误差界分别为 $\epsilon_z,\epsilon_\theta$，则在 (1) 平方根后加
$$
\epsilon_z/L+
\bar a_{\rm hi}\epsilon_\theta/(f_*J_{\min}).
$$
这包括所有系数离散误差。$J^2$ 自身格点化的 Fourier $\ell^1$ 误差也从每个角盒的下界中扣除，随后可与原准确 $J_{\min}^2$ 下界取最大值。

## 4. 完整径向图及原固定度量

在 prefix，$H=1$。上、下两段原 profile 都有 $f\ge1$。准确 bridge 从 $1$ 单调降到准确 $c$，且 $|f_s|\le1$，因此在任意 prefix 片上可取
$$
f_*\ge\max\{c,1-\max(0,q_{\rm hi}-s_p)\}.
$$
若片完全在 $s_p$ 之前，直接取 $f_*=1$。跨越 prefix/tail 的片保留两侧下界的最小值。

尾端严格使用 R223 的同一图
$$
r=c-hR(t),\quad t=(q-S)/h,\quad h=c-r_{\rm cuff},
$$
$$
R(t)=kt-\frac b2t^2+(6a+3b/2)t^3
 +(-8a-3b/2)t^4+(3a+b/2)t^5,
$$
其中 $k=2/\sqrt5$、$a=1-k$、$b=28h/(25c)$。每片的准确 $t$ 范围使用严格 $S$ 盒；$R'$ 的局部 Bernstein 控制给下界，且
$$
H=R'(t)\sqrt{1+w(r)^2}\ge R'(t)>0.
$$
$R$ 单调，故片上 $f=r\ge c-hR(t_{\rm hi})$。与 R223 已证的全域 $r\ge r_{\rm cuff}$ 合取，防止向外区间舍入将准确终点误写为更小半径。这里**不需要重新求尾背景、下载历史 blob 或增加任何 tail query**。

## 5. 度量转移与中央修正

设 (1) 给片上 $\|dW\|_g\le p_W$。R226 给中央修正 $C$ 的准确导数预算 $p_C=\|C_s\|+\|C_u\|$；仅在该片与首 ramp 支撑相交时才加上它，此处 $f\ge1$。令 $p=p_W+p_C$，则
$$
\|g^{-1/2}(Y^*e-g)g^{-1/2}\|_{\rm op}
\le d+2(1+d)p+p^2. \tag{3}
$$
证明是将 $DY=DX+D(C+W)$ 代入完整 Gram 恒等式，并用 $\|DX\|_g\le\sqrt{1+d}\le1+d$。程序仍未利用 $DX$ 与 $dW$ 的方向性抵消，其输出明确记录 `source_cross_Gram_cancellation_used=false`。若 (3) 尚过宽，下一层应确实消费源的方向信息；不能把有限点 metric 替代 (3)。

该结论覆盖完整半面及原真 cuff；下半面对称，固定封帽保持原界。R234 已证明的完整相位作用将同一度量算子界传到全部时间。此处不重证 reach、held 或 E(3) 非全等，也不把新的连续有限误差界写成精确等距存在或第 5 条的加密趋零。

## 6. 实现、真实核验与实际消费边界

源码 `scripts/6a65-m12-local-bernstein-angular-metric-budget.py` SHA-256 为 `f69035fe51642d30f2a1a5079c3e67f36c8cb05257df89be650cb5b015327db9`。独立代数与另名人工场的完整核验入口真实两阶段 exit0，合计23.096秒；该人工场新metric界2.1965895e−6，程序如实给false。完整命令、源身份和标量回执见[执行记录](../notes/2026-11-26-6a65-local-bernstein-angular-metric-budget.md)。

下一显式 whole h job 保留428元、全部原观察、R226/全源几何/完整STL，只新增本验证器消费本次实际field/grid/result；报告严格核同场SHA。重新生成输入不计为新的加密改善，真实新界须等消费者自然退出。此定理没有消除第5条或强幅度缺口。

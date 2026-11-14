# R89：同一尾方程的 Fourier 乘积 Jacobian 与完整变分流

状态：**已证明的有限求积代数恒等式；已实现可选完整变分流。** 原尾端 Jacobian 的逐角点、逐矩阵元乘积投影，可以改成六组离散 Fourier 矩及 Toeplitz/Hankel 型装配。非线性角 root、状态 RHS、物理背景、边界条件和径向 RK 网格均不改。实数算术下两种装配逐项相等；浮点差异和实际计时列于第 7 节。

这是提高同一几何加密计算效率的中间结果，不是新的尾解，也不支付闭面等距或收敛标准。作者 Astra-visible-flex-78718bd0，2026-11-10；编号由根分配，按根 README §13 直接登记。

## 1. 原方程与有限求积

固定物理 cell 的尺度 $\mu>0$、方向 $\varepsilon\in\{-1,1\}$。在径向参数 $x$ 处，令 $r,w>0$、$W=w^2$、$E=1+W$、$r_x=dr/dx$。取整数间隔 $m$、频率 $\ell_j=mj$，令

$$
c_0=1,\quad c_j=\sqrt2\cos(\ell_j\theta),\quad
s_j=\sqrt2\sin(\ell_j\theta)\quad(1\le j\le M),
\qquad
\langle f\rangle_N=\frac1N\sum_{n=0}^{N-1}f(2\pi n/N).
\tag{1}
$$

使用原引擎已有条件 $N>4mM$，所以基的离散正交关系成立。下文乘积恒等式本身对任意 $N$ 成立，不把有限求积替换成连续积分。

前 $2M$ 个状态分量是 $Q_j,\pi_j$，另两个是平均高度扰动 $h_0$ 和背景平均高度 $h_{\rm bg}$。沿用 [R86](R86-geometric-momentum-prolongation.md) 的原变量：

$$
\begin{aligned}
q&=\frac{r^3}{\sqrt2w},&
P&=-q\sum_{j=1}^M\ell_jQ_js_j,&
P_\theta&=-q\sum_{j=1}^M\ell_j^2Q_jc_j,\\
L&=\sum_{a=0}^M\lambda_ac_a,&
K&=L-P_\theta,& U&=K_\theta-P,\\
S&=1-WP^2,&
D&=1-W(2K+K^2+EP^2),&d&=\sqrt D,\\
A&=1+L+WP_\theta=1+K+EP_\theta.
\end{aligned}
\tag{2}
$$

只在原 root 接受的 $S,D,A>0$ 分支讨论。程序继续使用原先更强的数值 floor。角连接、通量、尺度为

$$
\omega=\frac{1+W(1+K)P_\theta/S}{d},\qquad
\phi=\frac{(1+K)U}{Sd},\qquad
\tau=\frac{\varepsilon\sqrt{12}\mu}{\sqrt2r^4W},\qquad
b=\frac{A}{D^{3/2}}-1.
\tag{3}
$$

原 root 满足

$$
\left\langle c_a\frac{\omega-1}{W}\right\rangle_N
=
\begin{cases}0,&a=0,\\\tau\pi_a,&1\le a\le M.\end{cases}
\tag{4}
$$

其 $\lambda$ Jacobian 为

$$
B_{ab}=\left\langle c_a\frac{A}{D^{3/2}}c_b\right\rangle_N
=\delta_{ab}+\langle c_ab c_b\rangle_N .
\tag{5}
$$

正权和离散正交性使 $B$ 正定。新实现直接调用原 root，直接使用它已经组好的 $B$；没有另求 root 或改其 Gram 装配。

记

$$
\sigma=\frac{r_x}{r},\qquad
\kappa=\frac{\varepsilon\sqrt2r^3r_xW}{\sqrt{12}\mu},
\qquad \kappa\tau=\sigma .
\tag{6}
$$

原状态方程是

$$
\begin{aligned}
(Q_i)_x&=\sigma\left((\ell_i^2-4)Q_i+
                         \frac{\sqrt2w}{r^3}\lambda_i\right),\\
(\pi_i)_x&=4\sigma\pi_i+\kappa\ell_i\langle s_i\phi\rangle_N,\\
(h_0)_x&=r_xw\lambda_0,\qquad (h_{\rm bg})_x=r_xw .
\end{aligned}
\tag{7}
$$

原 split-flux 实现先把 $\phi=U+(\phi-U)$ 的线性项按正交性直接计算，以减小舍入损失。新实现调用同一个 split RHS，保留这项求值方式。

## 2. 全部基乘积由有限 Fourier 矩给出

对任意角点实值 $f$，定义

$$
C_f(k)=\langle f\cos(km\theta)\rangle_N,\qquad
S_f(k)=\langle f\sin(km\theta)\rangle_N,\quad0\le k\le2M,
\tag{8}
$$

并延拓 $C_f(-k)=C_f(k)$、$S_f(-k)=-S_f(k)$。以 $CC_f,SS_f,CS_f,SC_f$ 分别表示 $\langle c_ifc_j\rangle_N$、$\langle s_ifs_j\rangle_N$、$\langle c_ifs_j\rangle_N$、$\langle s_ifc_j\rangle_N$，则完整公式是

$$
\begin{aligned}
CC_f(0,0)&=C_f(0),\\
CC_f(0,j)&=\sqrt2C_f(j),\quad CC_f(i,0)=\sqrt2C_f(i),\\
CC_f(i,j)&=C_f(|i-j|)+C_f(i+j) &&(i,j\ge1),\\
SS_f(i,j)&=C_f(|i-j|)-C_f(i+j) &&(i,j\ge1),\\
CS_f(0,j)&=\sqrt2S_f(j),\\
CS_f(i,j)&=S_f(i+j)+S_f(j-i) &&(i,j\ge1),\\
SC_f(i,0)&=\sqrt2S_f(i),\\
SC_f(i,j)&=S_f(i+j)+S_f(i-j) &&(i,j\ge1).
\end{aligned}
\tag{9}
$$

**证明。** 逐点使用

$$
\begin{aligned}
2\cos a\cos b&=\cos(a-b)+\cos(a+b),\\
2\sin a\sin b&=\cos(a-b)-\cos(a+b),\\
2\cos a\sin b&=\sin(a+b)+\sin(b-a),\\
2\sin a\cos b&=\sin(a+b)+\sin(a-b),
\end{aligned}
$$

乘 $f$ 并作同一个有限平均。指标为 $0$ 的行直接用 $c_0=1$。证明不要求 $f$ 为三角多项式，也不要求奇偶性。即使 $f$ 有任意高频或 aliasing，两种有限求积仍相等；这里没有先截断 $f$ 再相乘。

## 3. 六个权函数与 root 的完整微分

固定 $r,w$，令

$$
\begin{aligned}
F_P&=\frac{EP\omega}{D}
+\frac{2W(1+K)P_\theta P}{S^2d},\\
F_T&=-\left(EP_\theta+
  \frac{W(1+K)(WP^2+2K+K^2)}S\right)D^{-3/2},\\
C_K&=\frac U{Sd}+\phi\frac{W(1+K)}D,\\
C_U&=\frac{1+K}{Sd}-1,\\
C_P&=\phi\left(\frac{2WP}S+\frac{WEP}D\right).
\end{aligned}
\tag{10}
$$

加上式 (3) 的 $b$，只需六组矩

$$
S_{F_P},\ S_{C_K},\ C_{F_T},\ C_{C_U},\ C_{C_P},\ C_b,
\qquad 0\le k\le2M.
\tag{11}
$$

下面完整核清微分。把 $L,P,T=P_\theta$ 暂视为独立变量，$K=L-T$。对式 (3) 微分可得

$$
\partial_P(\omega/W)
=\frac{2W(1+K)TP}{S^2d}+\frac{EP\omega}{D}=F_P.
\tag{12}
$$

又由 $D+W(1+K)^2=ES$、$D-S=-W(2K+K^2+WP^2)$，

$$
\begin{aligned}
\partial_T(\omega/W)
&=\frac{(1+K-T)D-(S+W(1+K)T)(1+K)}
        {SD^{3/2}}\\
&=-\frac{EST+W(1+K)(2K+K^2+WP^2)}{SD^{3/2}}=F_T,\\
\partial_L(\omega/W)
&=\frac{TD+(S+W(1+K)T)(1+K)}{SD^{3/2}}\\
&=\frac{1+K+ET}{D^{3/2}}=\frac A{D^{3/2}}.
\end{aligned}
\tag{13}
$$

这也证明了式 (5)。把 $K,U,P$ 暂视为独立变量，则

$$
\delta\phi=C_K\delta K+(1+C_U)\delta U+C_P\delta P.
\tag{14}
$$

实际程序保留原先消减稳定的两式：

$$
C_U=\frac{K+(1-D)/(1+d)+WP^2d}{Sd},
\tag{15}
$$

以及令 $a=A-1=L+WP_\theta$、$v=1-D$ 后的

$$
b=a+(1+a)\operatorname{expm1}
             \left(-\frac32\operatorname{log1p}(-v)\right).
\tag{16}
$$

式 (15) 中 $(1-D)/(1+d)=1-d$，分子为 $1+K-Sd$，故等于式 (10)；式 (16) 等于 $AD^{-3/2}-1$。

将状态变分记为 $(\delta Q,\delta\pi)$。由 root 微分得

$$
B\delta\lambda
=\tau(0,\delta\pi)
-\left\langle c(F_P\delta P+F_T\delta P_\theta)\right\rangle_N,
\tag{17}
$$

其中

$$
\delta P=-q\sum_j\ell_j\delta Q_js_j,\qquad
\delta P_\theta=-q\sum_j\ell_j^2\delta Q_jc_j.
\tag{18}
$$

分离精确的线性对角响应，

$$
\Delta\lambda_a=\delta\lambda_a
-\tau\mathbf1_{\{a\ge1\}}\delta\pi_a.
\tag{19}
$$

所有 $2M$ 列可一次求解 $B\Delta\Lambda=H$，右端为

$$
\begin{aligned}
H_{a,Q_j}
&=q\{\ell_jCS_{F_P}(a,j)+\ell_j^2CC_{F_T}(a,j)\},\\
H_{a,\pi_j}&=-\tau CC_b(a,j),
\quad 0\le a\le M,\quad1\le j\le M.
\end{aligned}
\tag{20}
$$

第二行使用
$B(\delta\lambda-\tau(0,\delta\pi))=-\tau(B-I)(0,\delta\pi)$。
因此无需对微小的 $B-I$ 另作浮点矩阵减法；原稳定表达式 (16) 直接提供其权函数。

## 4. 通量微分及全部 Jacobian 行

定义 $M\times(M+1)$ 和 $M\times M$ 矩阵

$$
\begin{aligned}
\mathcal L_{i,0}&=SC_{C_K}(i,0),\\
\mathcal L_{i,j}&=SC_{C_K}(i,j)-\ell_jSS_{C_U}(i,j),\\
\mathcal Q_{i,j}
&=q\left[-\ell_j\{SS_{C_P}(i,j)+(\ell_j^2-1)SS_{C_U}(i,j)\}
+\ell_j^2SC_{C_K}(i,j)\right].
\end{aligned}
\tag{21}
$$

这里 $1\le i,j\le M$。为验证完整性，使用

$$
\delta K=\delta L-\delta P_\theta,\qquad
\delta U=(\delta L)_\theta-\delta P_{\theta\theta}-\delta P.
$$

从式 (14) 分出线性项 $\delta U$，剩余恰为

$$
C_K\delta L+C_U(\delta L)_\theta
+(C_P-C_U)\delta P-C_U\delta P_{\theta\theta}
-C_K\delta P_\theta.
\tag{22}
$$

$\delta\lambda_0$ 系数为 $C_K$；
$\delta\lambda_j$ 系数为 $C_Kc_j-\ell_jC_Us_j$，
投影到 $s_i$ 给出 $\mathcal L$。
对 $\delta Q_j$ 则有
$\delta P_{\theta\theta}=-\ell_j^2\delta P$，
再代入式 (18) 即得 $\mathcal Q$。全部 $P,K,U$ 依赖均已包括。

对状态列 $c$，记

$$
\begin{aligned}
T_{i,c}={}&-\ell_i\Delta\Lambda_{i,c}
+\begin{cases}\mathcal Q_{i,j},&c=Q_j,\\
               \tau\mathcal L_{i,j},&c=\pi_j,\end{cases}\\
&+\sum_{a=0}^M\mathcal L_{i,a}\Delta\Lambda_{a,c}.
\end{aligned}
\tag{23}
$$

线性通量的 $Q$ 响应是
$-q\ell_i(\ell_i^2-1)\delta Q_i$。
其 $\pi$ 响应 $-\ell_i\tau\delta\pi_i$ 与式 (7) 中的
$4\sigma\pi_i$ 合并后，得到全部 $2M+2$ 行：

$$
\begin{aligned}
J_{Q_i,c}
&=\sigma\left[
(\ell_i^2-4)\mathbf1_{\{c=Q_i\}}
+\frac{\sqrt2w}{r^3}
 \{\Delta\Lambda_{i,c}+\tau\mathbf1_{\{c=\pi_i\}}\}\right],\\
J_{\pi_i,c}
&=(4-\ell_i^2)\sigma\mathbf1_{\{c=\pi_i\}}
-\kappa\ell_i^2(\ell_i^2-1)q\mathbf1_{\{c=Q_i\}}
+\kappa\ell_iT_{i,c},\\
J_{h_0,c}&=r_xw\Delta\Lambda_{0,c},\qquad J_{h_{\rm bg},c}=0.
\end{aligned}
\tag{24}
$$

平均高度不反作用于形状方程；若需要完整方阵，两个额外输入列均为零。

**代数结论。** 用式 (9) 和六组矩 (11) 组成式 (20)、(21)，以原 $B$ 求解 $\Delta\Lambda$，最后代入式 (23)、(24)，与原逐角点直接累积所有乘积的 analytic Jacobian 完全相等。即便程序只把 root 解到有限容差，这两套代数公式对同一个输入 root 行仍相等；这里没有把该有限容差 root 当成精确解，也没有声称求了“Newton 停止程序”的算法微分。

## 5. 复杂度与完整变分流

原乘积部分逐角点累积 $O(M^2)$ 个矩阵元，成本 $O(NM^2)$。新方法积累六组各 $2M+1$ 个矩，为 $O(NM)$，再以式 (9) 在 $O(M^2)$ 内装配。三角表在引擎创建时预生成。

整个引擎并不因此降为 $O(NM)$：非线性 root 的原 $B$ 装配仍在，批量 Cholesky/多右端及变分矩阵乘法仍有 $O(M^3)$ 成本。因此完整运行收益不能由乘积块的阶数直接推断。

原联合系统为

$$
y_x=f(y,x),\qquad \Phi_x=J(y,x)\Phi,\qquad
\Phi(0)=\begin{pmatrix}I_{2M}\\0\\0\end{pmatrix}.
\tag{25}
$$

新 flow 保留原 RK4 的四个状态/变分子阶段、末步加权、矩阵乘法三层循环顺序，以及实际 profile 的 integrationBreakpoints 形成的 cusp-aware 网格，只替换每个阶段的 $J$ 计算。实数算术下 $f,J$ 相同，因此四个子阶段递推相同；对所有步归纳，离散状态映射和变分均相同。

浮点时三角恒等式的不同求值及加法重排会产生舍入差，不保证 Jacobian 或变分矩阵逐位相同，也不把一次短段比较升级为全 DN 误差界。

## 6. 可直接选择的完整实现

- [局部 Jacobian](../scripts/78718-tail-fourier-product-jacobian.mjs)：六组矩、全部装配、原 $B$ 的批量 Cholesky；不自行启动求解。
- [完整变分 flow](../scripts/78718-tail-fourier-product-flow.mjs)：保留原 RK/变分循环的引擎包装。
- [可选实际 worker](../scripts/78718-prefix-tail-geometric-fourier-worker.mjs)：在创建原 DN 后保持各共享 engine 的对象身份，只替换局部 Jacobian 与完整变分入口。cutJets 等闭包仍引用同一 engine 对象。

原 root、split RHS、无 Jacobian 的 RK、分支 floor、Newton 接受规则、完整 DN response、物理配置检查及 R86 暖启动均保留。新 worker 的 ready 元数据把 tailJacobian 标为 fourier-product-moments-v1。后端选择不进入物理配置；它交给主数值线作为显式可选 tail-jacobian 模式，当前原 M15 worker 没有改动。

原公式来自 source-root 的 general_root_tail_momentum.mjs、
f6tail_fast_momentum.mjs、f6tail_momentum_split_flux.mjs、
f6tail_fast_split_flux_engine.mjs，以及当前题
[split factory](../scripts/db6f-prefix-tail-trial-split.mjs)、
[DN core](../scripts/db6f-prefix-tail-trial-core.mjs)。
本文已经展开全部公式；数学结论不依赖把源码检查当成证明。

## 7. 已实际完成的有限比较

输入为主 M15 的首个真实 N512 尾响应
2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz，
SHA256 为
a88f0a8eaff38a6fca9576550ef04d538c8b8d1fe55715df6d0439f27801c919。
依 R86 保持 Q/L 升到 M22，仍取 N512。这只是固定旧尾的几何初猜，不是已解出的 W22。

### 7.1 十个实际节点的局部比较

[benchmark 脚本](../scripts/78718-tail-fourier-product-benchmark.mjs)
检查节点 0、16、31、34、40、72、144、288、576、864，每点预热后各计时 20 次。
实际 6bb428/session90311 → 08cfb7，已观察自然 exit0。
[标量报告](../notes/2026-11-10-78718-tail-fourier-product-benchmark-01.json)
为 5279 bytes。

- 十点状态 RHS 最大绝对差全部为零。
- 各点原/新耗时之和的比为 1.8589934268，单点约 1.10 至 3.29；不是完整 DN 加速比。
- Jacobian 最大绝对差约 $4.56348\times10^{-8}$，出现在带很大单位缩放的条目，不能省略这个绝对差。
- 形状逐行尺度差最大 $1.58626\times10^{-12}$，平均高度行最大 $6.88217\times10^{-14}$。

尺度差的准确口径如下。设
$s_Q=\max(10^{-250},\max_j|Q_j|)$、
$s_\pi=\max(10^{-250},\max_j|\pi_j|)$，
每行报告

$$
\frac{\sum_c|J^{\rm old}_{ic}-J^{\rm new}_{ic}|s_c}
{\max(10^{-300},\sum_c|J^{\rm old}_{ic}|s_c)},
\qquad
s_c=\begin{cases}s_Q,&c=Q_j,\\s_\pi,&c=\pi_j.\end{cases}
\tag{26}
$$

这只是明确的比较口径，不是自动的全局误差估计。

### 7.2 一个真实短 stage 的同 RK 比较

[short-flow 脚本](../scripts/78718-tail-fourier-product-short-flow.mjs)
对 stage31、rawCell0、rawSegment5，从同一个暖启动节点出发，用原 32 步、原 profile 分别运行原/新完整变分流；没有运行 shooting 或 BVP。

[短段报告](../notes/2026-11-10-78718-tail-fourier-product-short-flow-01.json)
为 1101 bytes，SHA256
ba796fb001d571fc57bd734b1efe3f463a427e2576df30e8646cb6c80f609594。

|指标|实际值|
|---|---:|
|原完整变分 flow|570.30884 ms|
|新完整变分 flow|407.770803 ms|
|本次耗时比|1.39860146|
|末状态最大绝对差|0|
|末变分矩阵最大绝对差|$2.51457\times10^{-8}$|
|原变分矩阵最大绝对值|$4.33479\times10^6$|
|按式 (26) 同口径的末变分逐行差|$3.40514\times10^{-13}$|

两者 minA、minD、最大 root 相对残差相同，分别约为
0.9074023013、0.9999189739、$2.60444\times10^{-15}$。

观察范围：启动为 9c7cde/session16862；末次工具输出因上下文截断未见，随后实际 poll 为 Unknown process id。报告由脚本完成所有比较后写出，已在 1f004e 中实际读取。不补造未读到的自然 exit 回执，也不因此重复整段或增加流程。

## 8. 对主问题的作用

R85、R86 已定位旧有限 M 的遗漏频率误差，给出保持一 jet 的升频暖启动。本结果降低同一个有限非线性系统的变分装配成本，帮助真正高模联解。角求积和频率截断误差不会因本加速消失。主 M/W 计算能否收敛、全径向/全角 metric 上界、闭合接缝及最终全时刻条件，仍由真正的新图和相应连续计算回答。

## 9. 延伸：同一 root 的 Gram 矩阵也用有限乘积矩装配

第 1–7 节的第一版保留原 root 的全部 Gram 装配。根随后指出这里仍有 $O(NM^2)$ 的主要成本，因此另做本节可导入工厂，不覆盖第一版 worker 或正在运行的源。

对每次 Newton 中的同一个 $L,Q,r,w$，令

$$
\beta_k=\langle b\cos(km\theta)\rangle_N,\qquad0\le k\le2M.
\tag{27}
$$

式 (5)、(9) 立即给出完整 Gram 矩阵

$$
\begin{aligned}
B_{00}&=1+\beta_0,\\
B_{a0}=B_{0a}&=\sqrt2\beta_a\quad(1\le a\le M),\\
B_{ab}&=\delta_{ab}+\beta_{|a-b|}+\beta_{a+b}
                         \quad(1\le a,b\le M).
\end{aligned}
\tag{28}
$$

这是对原矩阵的逐项恒等式，不引入新的 $N$、正交规则或滤波。原代码先初始化单位阵，再逐角点累积 $bc_ac_b/N$；新代码先积累式 (27)，再对同一单位阵加入式 (28) 的对应项。所有残差投影、消减稳定的 $b$、分支检查、Newton 线搜索、容差、回退规则和初值保持原样。实数算术下 $B$ 相同，因此 Cholesky 解、每次迭代、线搜索比较及最终停止条件都相同。浮点时不要求这些分支判断永远逐位一致，下文仅报告实际观察。

这个变化把每次 Gram 积累从 $O(NM^2)$ 改为 $O(NM+M^2)$。原残差计算本来是 $O(NM)$，Cholesky 仍是 $O(M^3)$；没有把整个 Newton 宣称为线性成本。

实现采用两个新模块：

- [78718-tail-fourier-root-momentum.mjs](../scripts/78718-tail-fourier-root-momentum.mjs)：原 momentum 引擎的另名派生，只改 import、导出名、预计算 cosine 表，以及上述 Gram 积累。其余 root、初始化和状态函数保留。
- [78718-tail-fourier-root-split-engine.mjs](../scripts/78718-tail-fourier-root-split-engine.mjs)：导出 createFourierRootSplitFluxEngine(options)。它把新 root 传给原 split RHS，再组合第 5 节的完整变分 flow；支持原 cuspAwareFlow 包装，保留原不支持 legacy flowRawCell 的接口行为。

新工厂返回完整引擎，供后续 worker 选择，不另复制一份 DN worker。第 6 节原先可选的 Jacobian-only worker 仍可原样使用。

### 9.1 已实际完成的合并版比较

[root benchmark 脚本](../scripts/78718-tail-fourier-root-benchmark.mjs)
使用第 7 节同一输入、同一 M22/N512、同十个节点和每点 20 次计时，再对同 stage31 的原 32 步执行一段完整变分 flow。真实 51e8fe/session79263 → 39f2fa，已观察自然 exit0；全程 7.908 秒，没有 DN 或 BVP。

[完整标量报告](../notes/2026-11-10-78718-tail-fourier-root-benchmark-01.json)
为 16181 bytes，SHA256
6b5c3621950521265cb5f06ffc01c4eaea6de3417a622036bd9827e582f5727f，
并记录四个新模块的实际字节身份。

|指标|本次实际结果|
|---|---:|
|十点 root 总计耗时比|1.79777357|
|十点完整 Jacobian 总计耗时比|3.13842551|
|十点 root 的最大 $\lambda$ 绝对差|$6.93890\times10^{-17}$|
|十点 root 的最大 $\lambda$ 最大范数相对差|$1.43718\times10^{-16}$|
|十点 $B$ 的最大范数相对差|$5.15819\times10^{-15}$|
|十点状态 RHS 最大绝对差|$7.62992\times10^{-15}$|
|十点 shape Jacobian 逐行尺度差最大值|$1.59677\times10^{-12}$|
|同段原/新完整 flow 耗时|652.865735 / 236.830453 ms|
|同段完整 flow 耗时比|2.75667984|
|同段末状态最大绝对差|$6.93890\times10^{-18}$|
|同段末变分矩阵最大绝对差|$2.49711\times10^{-8}$|
|同段末变分 shape 逐行尺度差|$3.43901\times10^{-13}$|

十点的 Newton 次数逐点相同。短段两者 minA、minD、最大 root 相对残差仍完全相同，数值见第 7.2 节。原短段变分矩阵最大幅度约 $4.33479\times10^6$，所以同段绝对差和尺度差应一起看。

第 7 节和本节是不同实际计时，各自使用同一轮原/新比较；不能拿跨轮的毫秒值当稳定的硬件基准。实测只表明这些实际输入上的有效收益及舍入差，不给未来全部 Newton 轨道的运行时间或误差保证。数学上原物理方程、有限求积和边界残差仍未改变。


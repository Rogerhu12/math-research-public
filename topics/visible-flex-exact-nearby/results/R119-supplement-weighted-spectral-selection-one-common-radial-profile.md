# R119：真实完整中频网络的带权谱平均与一组无限公共参数

2026-11-14，visible-exact / root。

**状态：已证明；24项新的精确有理门实际全部通过。** 对同一个 fixed-stop 径向家族，下面选出一次
外 bump 参数 $t$ 和全部相位保持 compact 参数，使每个实际
$M\in4\mathbb N$ 的 retained middle 网络同时可逆。
其逆满足窗口各自的双侧局部角宽界，原 $h_j,\zeta_j$ 不变。

这里“完整”指该固定频率的真实左 prefix、所有 retained middle
窗口、正段 cross、右无限 low 尾及全部 affine 数据。
本篇未把双侧端口权直接称为原 $\mathcal X_\beta$ 同宽物理源逆，
也未将径向结论移植到非径向混模或最终 nonlinear $\mathcal F$。

## 1. 每个频率保留哪些真实窗口

固定第53束同一真实径向 chart、基准浅层 $\Gamma^0$、fixed-stop
connector 和原两个 bump 曲线。只有第8193层以后的 compact
控制变化；同层两补偿 bump 精确保两个 phase。

记
\[
 A_j=2^{-40}\delta_j^{-1/8},\quad
 T_j=2^{65536}(j+5)^{204}\delta_j^{-320},\quad
 \delta_j=(2/25)2^{-j}.
\]
对 $M\in4\mathbb N$、$M\ge A_{8193}$，定义
\[
 \mathcal I_M=\{j\ge8193:A_j\le M\le T_j\},\quad
 n_M=|\mathcal I_M|,\quad d_M=2n_M .
 \tag{W.1}
\]
这是非空的有限连续整数区间。两阈值均严格递增，且
$A_{j+1}<T_j$；取最后一个 $A_j\le M$ 的 $j$ 即证非空。
并有
\[
        n_M<8\log_2M+321,\qquad M>1024.                \tag{W.2}
\]

把这些窗口之前的整个真实径向问题，从其原实允许线正向传播，
准确得到第一个 retained 端口上的实允许线。前缀中的 high 段
只是被准确消元，没有被设为零，也没有用一个近似稳定方向替换。
之后的真实无限 low 尾按第53束 C.24--C.48 给另一条允许线和
完整 affine 位移。其非零性来自二阶唯一性及真无限尾强解。

两条线可为竖直线；使用完整 unitary reflection，不除高度。
所有 positive 段、根、接缝、外物理两迹及源均准确保留。
因此上一网络定理给 $d_M$ 维酉矩阵
\[
 (I-U_M)x_M=g_M,\qquad U_M=P_M\bigoplus_{j\in\mathcal I_M}S_{j,M}.
 \tag{W.3}
\]
不同 $M$ 的切口可以不同；这是同一个 profile 的精确消元。

## 2. 同一个无穷参数盒

在每层 $j$，只给其实际有限中频窗 $[A_j,T_j]$ 分配原 $I_n$。
每个 dyadic band 的右端为 $U$，其实际正四倍频率数为 $N\le U$。
使用
[完整二次型正定方向](R119-supplement-all-quadratic-phase-preserving-positive-scattering-control.md)
的 $\psi_{j,M},d_{j,n},r_{j,n}$，准确设置
\[
 \Xi_j=\sum_n\frac{r_{j,n}}{N_{j,n}}
                  \sum_{\substack{M\ {\rm in\ that\ band}\\
                                   A_j\le M\le T_j}}
                         \theta_M\psi_{j,M},
 \qquad -1\le\theta_M\le1.
 \tag{W.4}
\]
一个频率 $\theta_M$ 同时控制且仅控制自己的所有
$j\in\mathcal I_M$。每层方向在实际已固定的小区间中心构造，
不依赖其它频率或层的后续参数。每层的 $C^4$ 总和小于 $2^{-79}$，
真实补偿保持在原 $2^{-64}$ 复域内部。

尽管每层实际只有有限个 band，参数总数为可数无穷。
(W.4) 与原真实尾图的产品拓扑连续性给同一个实际完整 profile。
原完整 mean 和高度积分继续定义，不能因 phase 固定而删除它们。

条件固定其它全部 $\theta_{M'}$ 以及 $t$ 时，改变 $\theta_M$
只改变 (W.3) 的 retained negative windows。
左 prefix、右无限余尾、所有 positive 段和端口单位对这个坐标
固定。因此 $P_M$ 对 $\theta_M$ 固定。
这正是固定 connector 的用途；不对一个未经证明连续的
good-$t$ 选择函数求导。

上一正定定理给整个盒上
\[
 G_M:=-iU_M^*\partial_{\theta_M}U_M\ge D_M>0,\qquad
 D_M=\operatorname{diag}_{j\in\mathcal I_M}(D_{j,M}I_2),
\]
\[
 D_{j,M}=\frac{r_{j,n}d_{j,n}}{16N_{j,n}K_j^2}
                  >e^{-2^{-800}Mh_j},\qquad
 \|G_M\|<2^{-33}<1/8 .
 \tag{W.5}
\]
这些下界不依赖其它参数的数值。没有将某个旧共振态继续用于新的
profile，也没有要求彼此 eigenphase 之间有正间距。

## 3. 有限酉路径的带权谱平均

本节先证明实际消费的有限维引理。设 $U(\theta)$ 是
$[-1,1]$ 上的真实解析酉路径，维数 $d$，且
\[
 -iU^*U'\ge D>0,\qquad\|-iU^*U'\|\le1/8,\qquad
 a=\lambda_{\min}(D).
\]
取任意 $M\ge4$，令
\[
 \varepsilon=(128dM^2)^{-1},\quad \xi=a\varepsilon,\quad
 L=1+\log(512dM^2/a),\quad \mathcal T=128dM^2L .
 \tag{W.6}
\]

有限维自伴局部 logarithm 给连续展开的 eigenphase $\phi_k$，
它们在 crossing 处可按通常的有限维解析分支读取；几乎处处
\[
 a\le\phi_k'=\langle v_k,(-iU^*U')v_k\rangle\le1/8,
 \qquad \langle v_k,Dv_k\rangle\le\phi_k'.
 \tag{W.7}
\]
crossing 的一阶分裂是在该 eigenspace 上限制同一个 Hermitian
generator，故同一下界仍适用。这里从未对单个 eigenphase
使用含邻谱分母的二阶导数。

每条 phase 在整个参数区间的变化至多 $1/4$。
令 $E_0$ 是至少一条 eigenphase 满足
$|1-e^{i\phi_k}|<\xi$ 的参数集合。
对应角弧半宽小于 $2\xi$，一条这样的单调分支至多穿越一个
完整 $2\pi$ 近邻弧，所以
\[
 |E_0|\le4d\varepsilon,\qquad
 {\mathbb P}(E_0)\le1/(64M^2),                         \tag{W.8}
\]
概率为 $[-1,1]$ 上的归一 Lebesgue 测度。

在其补集上 $R=(I-U)^{-1}$ 存在。完整谱分解及 rank-one 范数给
\[
 \|D^{1/2}RD^{1/2}\|
 \le H(\theta):=
   \sum_k\frac{\langle v_k,Dv_k\rangle}{|1-e^{i\phi_k}|}.
\]
重根处任选相应正交基即可，结论连续。
使用 (W.7) 作真实变量代换，每条 phase 的积分至多
\[
 \int_{\substack{-\pi\le s\le\pi\\|1-e^{is}|\ge\xi}}
                \frac{ds}{|1-e^{is}|}
 \le\pi\log(\pi/\xi)<4\log(4/\xi).
\]
这里用了 $|1-e^{is}|\ge2|s|/\pi$ 及
$|1-e^{is}|\le|s|$。所以
\[
 \int_{[-1,1]\setminus E_0}H(\theta)\,d\theta<4dL .
 \tag{W.9}
\]
Markov 不等式与 (W.6) 得
\[
 {\mathbb P}\{E_0\ \text{or}\ \|D^{1/2}RD^{1/2}\|>\mathcal T\}
                  <\frac1{32M^2}.                    \tag{W.10}
\]

关键是 $\lambda_{\min}(D)$ 只进入 logarithm；
没有将每个窗口的正定量都换成最小值后支付其指数倒数。
这也没有使用随机矩阵假设，或以一批有限 samples 代替谱平均。

## 4. 一次产品选择兼容所有频率与新 good-$t$

给全部 $\theta_M$ 取独立均匀概率，给 $t\in[0,1]$ 取均匀概率。
对每个固定 $M$，条件固定所有其它坐标和 $t$，(W.5)--(W.10)
直接适用。Fubini 因而给同一个全产品概率中的坏集上界。

正四倍频率的全部坏集之和严格小于
\[
 \sum_{M\in4\mathbb N}\frac1{32M^2}
 <\frac1{256}.                                        \tag{W.11}
\]
包括了比 (W.1) 更大的频率集，所以上界安全。

对每一个实际 $\Xi$，新 fixed-stop 定理又给真正新允许线的闭
好参数集 $G_\Xi^{\rm fixed}\subset[0,1]$，
\[
             |G_\Xi^{\rm fixed}|\ge1-83/16384 .
\]
这是对每个 fibre 的结论；不是假设存在共同的 good-$t$ 区间。
再用 Fubini，联合好集的概率至少
\[
                 1-\frac1{256}-\frac{83}{16384}
                    =1-\frac{147}{16384}>0.            \tag{W.12}
\]
故存在**同一个** $(t,\{\theta_M\})$，所有 $M$ 同时满足
\[
 I-U_M\ {\rm invertible},\qquad
 \|D_M^{1/2}(I-U_M)^{-1}D_M^{1/2}\|\le\mathcal T_M .
 \tag{W.13}
\]

所有图和线在真实产品拓扑下连续；竖直允许线用 reflection 表示，
无坐标极点。加入 (W.8) 的闭分离条件并把 (W.13) 写成非严格界，
这些好条件及新 good-$t$ 集形成非空紧集。
如需一个准确单值指定，可按 $t,\theta_{M_1},\theta_{M_2},\ldots$
次序逐个取此紧集上的最小坐标；嵌套紧集得到一个确定的实际点。
这不是声称已经数值枚举了无限参数数组。

选好以后 $t$ 固定。没有改 shallow 前缀、没有重停 connector，
也没有把 phase-preserving compact 选择换成逐模不同的 metric。

## 5. 每个窗口自己的角宽支付完整逆

对 (W.13) 的同一个选择，令
$a_M=\min_{j\in\mathcal I_M}D_{j,M}$。
由 $h_j<8$ 及 (W.5)，
\[
                     -\log a_M<M .
\]
(W.2) 在 $M\ge1024$ 给 $d_M<M$。
于是
\[
 1+\log(512d_MM^2/a_M)<2M,\qquad
                     \mathcal T_M<256M^4.             \tag{W.14}
\]
例如 $\log M\le M/8$ 在 $M\ge1024$ 已成立且此后改进。

对任一 active $j$，真实 $M\le T_j$ 给
$\log M<2^{10}(j+5)$。令 $J=j+5$，则
\[
 \log\mathcal T_M<8\log2+4\log M<2^{13}J
                          <2^{-803}Mh_j .
 \tag{W.15}
\]
最后一个严格界正是上一结论在 $j=8193$ 验证并向后递减的
$2^{50-61j/512}<2^{-803}$，没有重新扩大原角宽。

定义保留端口上的对角权
\[
 W_M=\operatorname{diag}_{j\in\mathcal I_M}
                              (e^{2^{-800}Mh_j}I_2).
\]
(W.5)、(W.15) 给
$W_M^2\ge\mathcal T_M D_M^{-1}$。因此 (W.13) 准确推出
\[
 \boxed{\quad
 \|W_M^{-1}(I-U_M)^{-1}W_M^{-1}\|\le1
       \quad\text{for every }M\in4\mathbb N,\ M\ge A_{8193}.
 \quad}                                                    \tag{W.16}
\]
这是双侧各窗口的局部小宽度，而不是按最坏窗口收取全体费用。
未更改 $\zeta_j$ 或原低频径向源权。

## 6. 源、mean 与尚未完成的全空间接线

(W.16) 作用于完整端口方程 (W.3)。
$g_M$ 继续包括 negative 全两态源、所有 positive DN affine、
原两端边界数据、被消去 high 前缀与真实 infinite-low 余尾的全部源。
weak 源使用 total flux；要求 bare flux 的地方另给真实 $F^t$
端迹。ordinary 密度、所有 frame Jacobian 和正段 shear 均未删除。

$m=0$ 保留独立高度及真 mean 电阻/通量积分。
低于 $A_{8193}$ 的有限频率不由 (W.16) 重新定量；
它们须使用同一个 fixed-stop 对象的原 full low/head、D0 或
其它完整有限门，不能因为集合有限便赋予一个未算的小常数。

(W.16) 也没有自动给
$e^{M\tau_j}/\zeta_j$ 在不同径向端口之间的映射界。
要取得原 $\mathcal X_\beta$ 同宽内部 Green，仍必须将真实
source-to-port、所有被消去部分的重建、原逐层标签单位与
(W.16) 按完整次序连接。对非径向问题，真实 principal 的端角、
两mean、root/Airy、positive cross 和所有 metric/source 导数
也仍须合并。

所以本篇完成公共径向 profile 和它的完整 middle 谱分母，
并保每个窗口自己的小角宽预算；
它没有据此宣称整个非径向 BVP、$\nu$ scalar 或 nonlinear
$\mathcal F=0$ 已经完成。


## 7. 实际执行与复现

源码：[fourfold_weighted_spectral_common_radial_profile.mjs](../scripts/fourfold_weighted_spectral_common_radial_profile.mjs)。
完整原生报告：[2026-11-14-R119-weighted-spectral-common-radial-profile-rational.json](../notes/2026-11-14-R119-weighted-spectral-common-radial-profile-rational.json)。
本次实际执行完整V8算术核，24项严格有理门全部通过；无限频率、谱平均和产品参数的量词由正文证明，未用随机采样代替。
源码SHA256：472782cb59a7519e59acb29fdce6beb3b61d30de06da51d3f9df679174daa2c9。

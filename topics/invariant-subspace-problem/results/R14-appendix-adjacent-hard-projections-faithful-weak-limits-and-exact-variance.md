# R14 附录：相邻硬谱投影的一致性、满支撑弱极限与精确方差

日期：2026-11-13（UTC）。normal_resume_1cf 推导，Astra-ISP-1cf8c51d 独立复核。
状态：已证明；补充[硬谱截断主稿](R14-appendix-hard-spectral-cutoffs-adjacent-quantiles-and-noncompactness.md)，不改变普通 ISP 的完成状态。

## 1. 准确设置与相邻质量引理

保持实际 $H=L^2(\mathbb Z_2,\mu)$、$A=M_wU$、$(Ug)(y)=g(y-1)$，
$w>0$ 几乎处处且有界。记
$$
W_n(y)=\prod_{j=0}^{n-1}w(y-j).
$$
固定 $\|f\|=1$、$0<\theta<1$，采用开、闭两种准确端点：
$$
\lambda_n=\inf\{t\ge0:\|\mathbf1_{\{W_n^2\le t\}}f\|>\theta\}>0,
$$
$$
P_n=\mathbf1_{\{W_n^2\le\lambda_n\}},\qquad
R_n=\mathbf1_{\{W_n^2<\lambda_n\}},
$$
$$
s_n=(I-R_n)f,\qquad t_n=A^*P_{n+1}f.
$$
这些是指标乘法投影，且
$\|R_nf\|^2\le\theta^2\le\|P_nf\|^2$。

主稿第4节已经证明：沿任意
$\lambda_{n_\nu+1}/\lambda_{n_\nu}\to0$ 的子列，
$$
\|P_{n_\nu+1}f\|^2\longrightarrow\theta^2.                 \tag{1.1}
$$
为明确本附录的依赖，证明只需如下短论证。
给 $\varepsilon>0$，由 $w>0$ 几乎处处、Haar 平移保测度和
$|f|^2$ 积分的绝对连续性，选固定 $\delta>0$，使所有 $n$ 都有
$$
\int_{\{w(y-n)<\delta\}}|f|^2\,d\mu<\varepsilon.
$$
若低闭谱质量超过 $\theta^2+\varepsilon$，
递推 $W_{n+1}(y)=W_n(y)w(y-n)$ 就给
$\lambda_n\le\lambda_{n+1}/\delta^2$，与最终比值小于 $\delta^2$ 矛盾。
结合阈值下界即得 (1.1)。此处没有预先抹去阈值原子。

## 2. 相邻谱投影及所选子列

固定下述相邻分位数比值趋零的子列 $n_\nu$。
记
$$
r_\nu=\lambda_{n_\nu+1}/\lambda_{n_\nu}\to0,\qquad
\mathcal P_\nu=\{W_{n_\nu+1}^2\le\lambda_{n_\nu+1}\},\qquad
\mathcal R_\nu=\{W_{n_\nu}^2<\lambda_{n_\nu}\}.
$$
对应的乘法投影仍为 $P_{n_\nu+1}$、$R_{n_\nu}$。

### 2.1 任意固定目标：两个投影在该目标上趋于一致

真实递推
$$
W_{n+1}(y)=W_n(y)w(y-n)
$$
给准确集合包含
$$
\mathcal P_\nu\setminus\mathcal R_\nu
\subseteq
\{y:w(y-n_\nu)^2\le r_\nu\}.                              \tag{2.1}
$$
右侧的 Haar 测度等于 $\mu\{w^2\le r_\nu\}\to0$。
由 $|f|^2$ 积分的绝对连续性，令
$$
a_\nu=\int_{\mathcal P_\nu\setminus\mathcal R_\nu}|f|^2\,d\mu,
\qquad
b_\nu=\|P_{n_\nu+1}f\|^2,\qquad
c_\nu=\|R_{n_\nu}f\|^2,
$$
则 $a_\nu\to0$。第1节的相邻质量引理给 $b_\nu\to\theta^2$，而阈值定义给
$$
b_\nu-a_\nu\le c_\nu\le\theta^2.
$$
故 $c_\nu\to\theta^2$，并且
$$
\begin{aligned}
\|(P_{n_\nu+1}-R_{n_\nu})f\|^2
&=\int_{\mathcal P_\nu\triangle\mathcal R_\nu}|f|^2\,d\mu\\
&=c_\nu-b_\nu+2a_\nu\longrightarrow0.
\end{aligned}
$$
因此对任意固定单位目标都有
$$
\boxed{
\|(P_{n_\nu+1}-R_{n_\nu})f\|\to0,\qquad
\|R_{n_\nu}f\|^2\to\theta^2,\qquad
\|s_{n_\nu}\|^2\to1-\theta^2.
}                                                       \tag{2.2}
$$
本小节不假设 $f$ 几乎处处非零，也不把 (2.2) 直接提升为算子强收敛。

### 2.2 满支撑目标使对称差在 Haar 测度下也趋零

以下额外假设
$$
f(y)\ne0\quad\text{几乎处处}.                            \tag{2.3}
$$
这是本节从加权目标结论升级为全空间算子结论的关键条件。

对任意可测集合 $D$ 和 $\delta>0$，
$$
\mu(D)\le\mu\{|f|\le\delta\}
+\delta^{-2}\int_D|f|^2\,d\mu.
$$
以 $D=\mathcal P_\nu\triangle\mathcal R_\nu$ 使用 (2.2)，
先令 $\nu\to\infty$，再令 $\delta\downarrow0$；
(2.3) 给
$$
\mu(\mathcal P_\nu\triangle\mathcal R_\nu)\to0.            \tag{2.4}
$$
指标乘子一致有界，故对每个固定 $g\in L^2$ 再用 $|g|^2$ 积分的绝对连续性，得到
$$
P_{n_\nu+1}-R_{n_\nu}\longrightarrow0\quad\mathrm{SOT}.    \tag{2.5}
$$
同时 $\mu(\mathcal P_\nu)-\mu(\mathcal R_\nu)\to0$。

### 2.3 第二次真实递推给渐近平移不变性

另一个端点的准确递推是
$$
W_{n+1}(y)=w(y)W_n(y-1).
$$
令 $\mathcal R_\nu^+=\{y:y-1\in\mathcal R_\nu\}$，
其乘法投影为 $UR_{n_\nu}U^*$。
和 (2.1) 相同，有
$$
\mathcal P_\nu\setminus\mathcal R_\nu^+
\subseteq\{y:w(y)^2\le r_\nu\},
$$
所以这个差集的 Haar 测度趋零。
又 Haar 平移不变性给
$\mu(\mathcal R_\nu^+)=\mu(\mathcal R_\nu)$，
而 (2.4) 已付 $\mu(\mathcal R_\nu)-\mu(\mathcal P_\nu)\to0$。
由此
$$
\begin{aligned}
\mu(\mathcal P_\nu\triangle\mathcal R_\nu^+)
&=2\mu(\mathcal P_\nu\setminus\mathcal R_\nu^+)
 +\mu(\mathcal R_\nu^+)-\mu(\mathcal P_\nu)\\
&\longrightarrow0.
\end{aligned}
$$
同样的固定 $L^1$ 控制给
$$
P_{n_\nu+1}-UR_{n_\nu}U^*\longrightarrow0\quad\mathrm{SOT}.
$$
联合 (2.5)，得到
$$
R_{n_\nu}-UR_{n_\nu}U^*\longrightarrow0\quad\mathrm{SOT}. \tag{2.6}
$$

### 2.4 遍历性确定全部 WOT 极限

每个 $R_{n_\nu}$ 都是指标乘法投影。
任意 WOT 收敛子列的极限仍为乘法算子 $M_a$，其中 $0\le a\le1$。
(2.6) 使 $M_a=UM_aU^*$，即 $a(y)=a(y-1)$ 几乎处处。
二进 odometer 平移遍历，故 $a$ 是常数。

由 (2.2)，
$$
\langle R_{n_\nu}f,f\rangle\to\theta^2.
$$
而 $\|f\|=1$，所以该常数只能是 $\theta^2$。
有界单位球的 WOT 紧性及极限唯一性遂给整个所选子列的结论
$$
\boxed{
R_{n_\nu}\longrightarrow\theta^2I,\qquad
P_{n_\nu+1}\longrightarrow\theta^2I
\quad\mathrm{WOT}.
}                                                       \tag{2.7}
$$
第二式还用了 (2.5)。
没有声称这些投影强趋于非投影 $\theta^2I$。

因此
$$
\boxed{
s_{n_\nu}\rightharpoonup(1-\theta^2)f,\qquad
t_{n_\nu}\rightharpoonup\theta^2A^*f.
}                                                       \tag{2.8}
$$

### 2.5 两条序列的精确方差缺口

由 (2.2)、(2.8)，
$$
\boxed{
\|s_{n_\nu}-(1-\theta^2)f\|^2
\longrightarrow\theta^2(1-\theta^2).
}                                                       \tag{2.9}
$$
第二条不能把 $A^*$ 当作等距算子。
准确计算是
$$
\|t_{n_\nu}\|^2
=\|M_wP_{n_\nu+1}f\|^2
=\int P_{n_\nu+1}w^2|f|^2\,d\mu
\longrightarrow\theta^2\|A^*f\|^2.                       \tag{2.10}
$$
最后一步对固定 $L^1$ 函数 $w^2|f|^2$ 使用 (2.7)；
等价地，在 WOT 中以固定向量 $wf$ 测试。
联合 (2.8)，得到
$$
\boxed{
\|t_{n_\nu}-\theta^2A^*f\|^2
\longrightarrow\theta^2(1-\theta^2)\|A^*f\|^2>0.
}                                                       \tag{2.11}
$$

特别，原真空 $f=1$ 满足 (2.3)，故这些精确极限适用。
对具有正测度零集的目标，只保已经证明的 (2.2) 及主稿的一般非紧性；
本节没有为这类目标无证宣称相同的全空间 WOT 标量极限。


## 3. 推导的实际范围

本附录的证明只用到有界正权、保测度的可逆遍历变换、有限测度下的绝对连续性，
以及所选相邻分位数比值趋零。因此，对标准概率空间上任何满足这些条件的
$A=M_wU$，同一证明成立。这里仅作已展示证明的范围说明，
不声称任意给定权或目标都自动提供这样的子列。

主稿对任意固定目标的强非紧性还使用原 Haar 权的稀层计数；
本附录对满支撑目标则给出准确的弱极限及方差。
对具有正测度零集的目标，当前全空间弱标量极限仍未证明。

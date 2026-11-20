# λ.002 新软启动真实 quintic 的连续全角非均值桥范围

**状态：已证明并实际执行这一组件的精确有理证书。不是完整 R59 证书，mean 原函数、背景积分差和公共 \(C^2\) 定义仍列明。**

输入为新软启动 \(q=.06,\lambda=.002,\tau=1,S=.5,b=.2\) 的同一完整 lift 物理场：

- run SHA-256：be83041236a3832194d52aae6b21569e2e463b67548e4b0b0b1b8cd683f323a1；
- physical SHA-256：a0d00429c4a6aac10165b07a4d8048dfe08aad4d3afda0dcbad7c4b30ab5bd5f。

该场原完整 metric 诊断约 \(3.1932\times10^{-5}\)，仍未达门；本文没有改它的 profile、core、任何系数或 mean provider，也没有调用求解器。

## 1. 被包围的精确对象

在计算角 \(\psi\) 中，保存的有限 Fourier 扰动写成

\[
G(s,\psi)=q\big((R+iT)e^{i\psi},Z\big),
\]
\[
R=Y_0+\sum_{j=1}^M Y_{R,j}\cos(m_j\psi),\quad
T=\sum_{j=1}^M Y_{T,j}\sin(m_j\psi),\quad
Z=\sum_{j=1}^M Y_{Z,j}\cos(m_j\psi),\quad m_j=3j.
\]

每个 \(Y\) 是该实际 physical 文件内的分段五次多项式。binary64 系数被读取为精确 Fraction；没有把节点之间的值替成线性插值。桥上原 exact-lift 窗口已经恒为零，不在这里截掉任何仍活动的核心参考。

角图仍是同一

\[
\theta=\psi-e(s)\sin(3\psi)/3,\quad
\rho=1-e\cos3\psi,\quad v=\theta_s/\rho.
\]

\(e(s)\) 由实际冻结三次 spline 与原截止五次多项式相乘得到。
源中的 spline 系数和尺度同样作为精确有理数。将物理 quintic、角图 spline、
截止点的所有分段合并，共得到 316 个径向闭区间。

在每段上，将各 \(Y,Y',Y''\) 和 \(e,e',e''\) 的精确多项式变换到 Bernstein 系数。
区间最小、最大值由 Bernstein 凸包给出。所有加减乘除和比较都是 Fraction；
平方根的上界用整数平方根后向上取到 \(10^{-15}\) 网格，而非依赖浮点根。

角方向始终用有限 Fourier 系数绝对值和，故覆盖整个圆周。这里没有连续角范围由 512 点 FFT 外推的问题，也没有径向采样遗漏。

## 2. 材料链式法则与参考权重

由角图的上述范围，源严格使用

\[
\rho\ge1-\|e\|,\quad |v|\le\frac{\|e'\|}{3\rho_{\min}},
\]
\[
|v_\psi|\le\frac{\|e'\|(1+\|e\|)}{\rho_{\min}^2},\quad
|v_s|\le\frac{\|e''\|}{3\rho_{\min}}+
\frac{\|e'\|^2}{3\rho_{\min}^2},\quad
|\rho_\psi|\le3\|e\|.
\]

对全部角度的 \(G,G_\psi,G_{\psi\psi},G_s^{\rm comp},
G_{s\psi}^{\rm comp},G_{ss}^{\rm comp}\) 分别使用极坐标基下的向量三分量绝对值和；
然后代入完整材料公式

\[
G_s=G_s^{\rm comp}-vG_\psi,\qquad G_\theta=G_\psi/\rho,
\]
\[
G_{ss}=G_{ss}^{\rm comp}-2vG_{s\psi}^{\rm comp}
+v^2G_{\psi\psi}+(vv_\psi-v_s)G_\psi,
\]
\[
G_{s\theta}=
(G_{s\psi}^{\rm comp}-v_\psi G_\psi-vG_{\psi\psi})/\rho,\qquad
G_{\theta\theta}=G_{\psi\psi}/\rho^2-G_\psi\rho_\psi/\rho^3.
\]

以 R59 的端点保持正仿射拉回 \(s=s_b+c\xi\) 测量这些导数。
R59 已执行的精确端点直接蕴含参考长度
\(L\in(.93014,.93125)\)；用本次真实桥区间的精确长度比较，证得

\[
.999<c<1.001.
\]

参考半径使用较保守但完全解析的
\(a_{\rm ref}\ge \max(.299,1-\xi)\)，以及 \(|a_{\rm ref}'|\le1\)。
因此本证书不用查询或近似参考半径积分，也没有重跑 R59 的背景积分。

记本非均值项的参考单位范数为

\[
G_1^2=|G_\xi|^2+|G_\theta|^2/a_{\rm ref}^2,
\]
\[
G_2^2=
|G_{\xi\xi}|^2+
2\left|\frac{G_{\xi\theta}-(a_{\rm ref}'/a_{\rm ref})G_\theta}
{a_{\rm ref}}\right|^2+
\left|\frac{G_{\theta\theta}+a_{\rm ref}a_{\rm ref}'G_\xi}
{a_{\rm ref}^2}\right|^2.
\]

## 3. 实际严格结果

全部 316 个径向区间及整个角圆周同时满足

\[
\|G\|_\infty\le
\frac{24955138686671}{10^{15}}
=.024955138686671,
\]
\[
\|G_1\|_\infty\le
\frac{33482969124167}{2\cdot10^{14}}
=.167414845620835,
\]
\[
\|G_2\|_\infty\le
\frac{1350943253810923}{10^{15}}
=1.350943253810923.
\]

角图的统一下界超过 \(.8598784\)。这个下界也是精确 Fraction 比较的结果。
\(G_0,G_1\) 的最坏包围发生在桥首段
\([.4945773692800001,.4952323306287287]\)，
\(G_2\) 最坏包围发生在紧随其后的区间。

这些数比逐点值更宽，原因是三角不等式和 Bernstein 包围；
它们具有连续径向和全角意义，不是新的采样表。

## 4. 与完整 R59 窗口之间仍缺的量

实际总扰动还包含径向背景与精确参考之差，以及同一高度 mean 的零模。
取参考入口高度为实际既定入口 mean，则桥内高度差为

\[
H(\xi)=\int_{s_b}^{s_b+c\xi}M_{512}(s)\,ds-h_{\rm ref}(\xi),
\]

其中 \(M_{512}\) 必须是原完整 field、原固定角节点规则下的同一 mean velocity。
入口以前的原函数由此严格相消；\(H(0)=0\)，但不能据此将 \(H'\) 或 \(H''\) 置零。

本组件的严格结果给出了 R59 备选窗口 \((.13,.2,3.8)\) 中很宽的剩余预算。
仍须支付：

1. 同一完整 field 的桥内 \(M_{512}\) 与其导数范围，包含材料角图链式项；
2. 原 source 积分与精确参考的零、一、二阶差量及公共坐标尺度；
3. 实际入口绝对 mean \(z_0\in[.35,.51]\)；
4. 对分别舍入的 PPoly 和 spline 系数采用哪一个公共 \(C^2\) 定义，并把该定义的任何调整加入余量。

证书覆盖每段两侧的多项式极限，未将分别舍入系数在接点“极小”的 jet 差自动称为精确 \(C^2\)。最终共享 jet 方案可沿用 R23/R56 的明确构造，但其改动必须计算，不能只引用名字就视为已付。

## 5. 已执行源与命令

[证书源](../scripts/resume_m3/certify_r59_nonmean_fourier_ranges.py) SHA-256：

    41b7340ea7c3fa951f31171c7d847ee2633843c63572a7a5cf9aaa33145b1d5a

实际完整输出 SHA-256：

    1b75c27b70d4e6fa095c287b1907f2d8e432adf38842749f3da1319bd59d1ad1

命令：

    python geometry-work/certify_r59_nonmean_fourier_ranges.py \
      --source-run m3-work/newg-wide-lambda0p002-tau1-linear/run.json \
      --physical m3-work/newg-wide-lambda0p002-tau1-linear/physical.npz \
      --support-dir math-research-public/topics/visible-flex-held-10pct/scripts/resume_m3 \
      --out geometry-work/newg-lambda0002-r59-nonmean-certificate.json

实际 exit 0。发布后源位于 scripts/resume_m3；可重算数组及输出未入库。

# R186：只增大第七个紧支撑系数即可严格消去晚段正曲率岛

**状态：已证明。** 下面给出当前 b075 准确物理度量的一条明确新设计：
保持准确 base、前六个 bump 系数和全部 supports 不变，只把第七个系数提高到
binary64 数 0.027，或原参数上限 0.08 以内的任何更大值。
在 R182 的整个晚段闭支撑上，新 $a_{ss}>11/10000$、新 $K<-11/10000$。
这是一维物理度量结论，不是新闭曲面、body 或 BVP 解。

## 1. 准确对象与已有证据

当前原点是
notes/2026-11-12-fd2d-raw-bump-dyadic34-trial-damped-back01-a01-accepted.npz，
133721 B，SHA256
b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f。

准确 profile 是 [R171](R171-accurate-radial-profile-and-one-sided-Arb-jets.md)
及 [R175](R175-exact-bump-polynomial-ranges-and-current-curvature-bands.md)
的同一 base/七系数定义；本状态的准确 rebind 已由
[R182](R182-signed-disjoint-trace-windows-on-certified-positive-K-bands.md) 绑定。
base 候选 SHA256 为
7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1。

记准确半径

$$
a_{\rm old}(s)=a_{\rm base}(s)+\sum_{j=1}^{7}\delta_j\psi_j(s).
$$

由 [R166](R166-exact-round-prefix-and-complete-increment-equations.md) §1–2，
base 全域有 $|a_{{\rm base},s}|\le1$：保留 Hermite 片由严格 Bernstein
速度包给出，之后 phase 片满足 $a_{{\rm base},s}=\sin\phi$。
这里不声称加入七个 bump 后仍有 $|a_{{\rm old},s}|\le1$。

本结果使用 R182 已证明的两份数据：

- 小报告 notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-report.json，
  12198 B，SHA256
  44d3d9318ffa7b70f7bcc59cebf81df09e72b9c37562c05e1410cdb65b627a68。
- 连续行包 notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-rows.json.gz，
  124843 B，SHA256
  d7f990bcef75ec30311e23d3cf92dadf5736f871f141dd3f7fa62071f7793095。
  本次不重新读取或传送二进制。下文的首盒半径上端点来自执行环境失联前
  已实际读取的 late_negative 第 0 行，工具输出标识为 1da6f9；其余小报告
  已通过文本接口再次读取。

晚段闭区间 $I=[A,D]$ 的准确端点为

$$
A=\frac{801077783718527}{562949953421312},\qquad
D=\frac{6507701461550367}{4503599627370496}.
$$

十进制显示是 $[1.423,1.445]$；准确对象始终是这两个保存 dyadic 端点，
没有把显示值另换成十进制有理数。

R182 全连续证书给出

$$
K_{\rm old}(s)\le
\frac{852552185}{8589934592}<\frac1{10}
\qquad(s\in I)
$$

及全域正半径下界

$$
a_{\rm old}\ge
\frac{18103121383342981011}{23058430092136939520}>0.
$$

首个连续盒包含 $A$，其半径上端点给出

$$
a_{\rm old}(A)\le A_0
=
100232046176162410354410926399048739012901711058992158435288592685611452460697
\cdot2^{-256}
<\frac{865621}{10^6}.
$$

## 2. 第七个 bump 的完整区间二导下界

第七个紧支撑为 $[L_7,R_7]$，其中

$$
L_7=\frac{4581889784524941}{4503599627370496},\qquad
R_7=\frac{3307833529335461}{2251799813685248}.
$$

令 $W=R_7-L_7$。在该区间内部

$$
\psi_7(s)=1024q^5(1-q)^5,\qquad q=\frac{s-L_7}{W};
$$

外部为零。因在两端有五阶零点，这个紧支撑函数为 $C^4$，且
$0\le\psi_7\le1$；后一结论由 $q(1-q)\le1/4$ 立即得到。

其准确二导为

$$
\psi_7''(s)
=\frac{10240}{W^2}
q^3(1-q)^3(9q^2-9q+2).
\tag{1}
$$

设

$$
q_L=\frac{A-L_7}{W},\qquad
q_R=\frac{D-L_7}{W}.
$$

准确有理比较给出 $1/2<q_L<q_R<1$，
其显示值分别为 0.8981969207962324、0.9469137557523886。
多项式 $9q^2-9q+2$ 在 $[q_L,q_R]$ 上递增且为正。
对式 (1) 的每个正因子分别取下界，可得整个闭区间上的统一下界

$$
\psi_7''(s)\ge
B_*=
\frac{10240}{W^2}
q_L^3(1-q_R)^3(9q_L^2-9q_L+2)
>\frac{32}{5}.
\tag{2}
$$

最后不等式由下述实际 BigInt 消费者作准确整数交叉乘法核定；
$B_*$ 的显示值是 6.407184818317281，不以该显示值作证明。

前六个紧支撑均已在 $A$ 之前结束。它们最右的端点为

$$
\frac{6107222740134427}{4503599627370496}
<
\frac{6408622269748216}{4503599627370496}=A.
$$

故在 $I$ 上，前六个 bump 的值及所有存在的导数都恒为零。

## 3. 原半径及原二导的保守下界

原第七个系数准确为

$$
d_0=\frac{1836789295023669}{144115188075855872}>0.
$$

在 $I$ 上使用 base 的 Lipschitz 界以及 $0\le\psi_7\le1$：

$$
\begin{aligned}
a_{\rm old}(s)
&=a_{\rm old}(A)
 +a_{\rm base}(s)-a_{\rm base}(A)
 +d_0(\psi_7(s)-\psi_7(A))\\
&\le A_0+(D-A)+d_0
<\frac{901}{1000}.
\end{aligned}
\tag{3}
$$

这一步明确支付了 bump 的变化，未把 base 的导数界误用到扰动后的半径。

结合原正半径、$K_{\rm old}<1/10$ 和
$K_{\rm old}=-a_{{\rm old},ss}/a_{\rm old}$，得到

$$
a_{{\rm old},ss}>-\frac{901}{10000}
\qquad\hbox{在整个 } I.
\tag{4}
$$

## 4. 明确的合法系数射线及连续负 K 结论

令

$$
d_*={\rm binary64}(0.027)
=\frac{7782220156096217}{288230376151711744},
$$

而原上限是

$$
d_{\max}={\rm binary64}(0.08)
=\frac{5764607523034235}{72057594037927936}.
$$

准确比较给出

$$
d_0<d_*<d_{\max},\qquad d_*-d_0>\frac{57}{4000}.
\tag{5}
$$

**定理。** 对每个准确实数 $d\in[d_*,d_{\max}]$，只把第七个系数改为 $d$，
定义

$$
a_d=a_{\rm old}+(d-d_0)\psi_7.
$$

则原全域正半径下界保持，且整个 $I$ 上

$$
a_{d,ss}>\frac{11}{10000},\qquad
0<a_d<1,\qquad
K_d=-\frac{a_{d,ss}}{a_d}<-\frac{11}{10000}.
\tag{6}
$$

**证明。** 因 $d\ge d_0$ 且 $\psi_7\ge0$，逐点有 $a_d\ge a_{\rm old}>0$，
故原全域半径下界直接保持。由 (2)、(4)、(5)，

$$
a_{d,ss}
=a_{{\rm old},ss}+(d-d_0)\psi_7''
>
-\frac{901}{10000}
+\frac{57}{4000}\frac{32}{5}
=\frac{11}{10000}.
$$

另一方面，与 (3) 同理，

$$
a_d(s)\le A_0+(D-A)+d
\le A_0+(D-A)+d_{\max}<1.
$$

最后将正的二导下界除以 $0<a_d<1$，得到 (6)。∎

因此 binary64 的 0.027 已是一个明确可计算的合法充分 witness。
更大的原域内系数同样满足结论。它不声称是 89 盒比值最大值给出的最小充分
阈值，更不声称是最优物理设计。

## 5. 哪些部分保持准确不变

第七个支持左端 $L_7$ 大于中段窗口右端
$4458563631096791/4503599627370496$（显示 0.99），也在旧 coast 之后。
因此 coast、中段窗口上的 $a$ 及其全部已声明导数完全不变；
原 middle-only 连续正 K 证书不受本次系数变化影响。

其支持右端 $R_7$ 恰等于原 protected terminal start，
显示 1.4689731783581288。在该端点及其右侧，$\psi_7$ 和一至四导数均为零。
故原受保护末窗的度量、$K$、准确 cut 半径及参数化定义保持相同。

这并不意味着从中央积分到末端的实际 frame、位置或 seam 自动相同；
真实 body 与拼缝仍须随新 g 计算。非圆曲面能否满足全域等距、曲率、
reach 和幅度要求也未由本标量定理解决。

R182 的 late positive-K 窗及其正 K 线性行不能同时当作这个新负 K 设计的
约束。应明确选取 middle-only 等仍有效的表示/域，或者使用适合新度量的
另一明确表示。R182 充分窗口从来不是原课题的必要条件。

## 6. 实际执行、源和复做

独立源：

[scripts/fd2d-metric-delta7-island-removal-rational.mjs](../scripts/fd2d-metric-delta7-island-removal-rational.mjs)，
8335 B，SHA256
394af7bde86078a6fd5d63a810a233795d6c0c179ebb801af2b01d1aedfe515a。

实际报告：

[notes/2026-11-12-fd2d-metric-delta7-island-removal-R186-01-report.json](../notes/2026-11-12-fd2d-metric-delta7-island-removal-R186-01-report.json)，
9268 B，SHA256
baf198106aad071c85d4afc027169eacfb4a2b3a62cd3438734e8c201412ed75。

本次在 executor unavailable 时，**真正执行了 functions 的 V8 BigInt 程序**。
20 项全部准确有理比较完成；没有 OS 子进程，因此不虚构 Python/Node 的 exit code。
同源代码可在恢复后的终端直接复做：

    node scripts/fd2d-metric-delta7-island-removal-rational.mjs

所有断言只用 BigInt 约分、整数运算和交叉比较；Number 只用于解码明确的
原 binary64 常数及十进制显示，不参与证明判断。完整准确分数均保存在报告中。

除了清楚的 $11/10000$ 统一余量，实际准确有理计算还给出：

- 使用 (4) 的保守原二导界及完整 $B_*$：新二导下界显示为
  0.0012325868611415514。
- 使用已存准确原 $K$ 上界和式 (3) 的完整半径有理上界：
  新二导下界显示为 0.00197112497350252。

这些只是同一已证明不等式的更紧有理结果，不是新 profile 采样。
本次没有读取大数组，没有求新 F/J、BVP、body、ODE 或新 Arb 盒。

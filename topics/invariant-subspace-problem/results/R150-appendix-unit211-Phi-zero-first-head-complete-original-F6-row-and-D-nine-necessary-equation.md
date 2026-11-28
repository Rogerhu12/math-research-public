# Phi=0 第一原头图：同一三生成元中的完整 F6 行与新的原 D 九次必要式

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 新结果

仍在第一原二次头非零图上，保同一点 $(u,Q,\lambda,T,z)$，其中 $z=Qt$。原三均值给出的三生成元是
$$
v=(1,T,z)^{\mathsf T}.
$$
本次加入完整原矩关系
$$
F_6=M K^2-4m^2D^3=0
$$
并由同一个真实 $M_T$ 约化为三系数行 $r_6$。使用新固定三行
$$
r_{\mathrm{N1}},\quad r_{T^2z},\quad r_6
$$
返回原物理量 $D$，得到新的必要多项式
$$
P_9(u,Q,\lambda)=0.
$$
其参数分次为 $(73,41,9)$，恰有 17389 项。

这是同一原图上的额外必要条件。它与此前 $(39,20,6)$ 的 $P_6=0$ 同时成立，但本稿没有计算或预设两式的 gcd，也没有把任何新首项当作单位。第一原头零曲线和所有 $\lambda$ 首项零权点仍保留。

## 2. 原矩关系的完整系数

记
$$
\begin{gathered}
m=u-\ell,\quad \delta=1-Q,\quad
M=\ell(2u-\ell Q)-u^2,\\
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\\
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell T A_2+2T^3.
\end{gathered}
$$
写 $F_6=\sum_{j=0}^6 a_jT^j$，完整系数为
$$
\begin{aligned}
a_0&=M\ell^4B_3^2-4m^2\ell^3A_2^3,\\
a_1&=-6M\ell^3A_2B_3,\\
a_2&=(9M+12m^2)\ell^2A_2^2,\\
a_3&=4M\ell^2B_3,\\
a_4&=-12(M+m^2)\ell A_2,\\
a_5&=0,\qquad a_6=4(M+m^2)=4\ell^2(1-Q).
\end{aligned}
$$
最后一个等式来自真实权恒等式 $M+m^2=\ell^2(1-Q)$。其首项为已付原权单位。本次源完整乘回这组系数与原 $MK^2-4m^2D^3$，没有用某个模投影替代 F6。

## 3. 为什么三系数行属于同一个原理想

令 $q_1,q_2,q_3$ 是原 $R_2/(2\rho),W_4,O_8/\rho$ 三个二次式。既有第一头图用真实二次头矩阵的伴随矩阵得到
$$
T^2=\tau_2v,\qquad Tz=\tau_{11}v,\qquad z^2=\tau_{02}v
\quad\bmod(q_1,q_2,q_3),
$$
并支付全部九个原系数身份。记
$$
M_T=\begin{pmatrix}0&1&0\\ \tau_2\\ \tau_{11}\end{pmatrix},
\qquad
M_z=\begin{pmatrix}0&0&1\\ \tau_{11}\\ \tau_{02}\end{pmatrix}.
$$
这里的每个条目只含原权单位和命名的第一头分母。

从 $e_0=(1,0,0)$ 开始，定义行向量
$$
p_0=e_0,\qquad p_{j+1}=p_jM_T.
$$
由真实关系 $M_Tv-Tv\in(q_1,q_2,q_3)^3$ 归纳得
$$
p_jv-T^j\in(q_1,q_2,q_3).
$$
因此
$$
r_6=\sum_{j=0}^6a_jp_j
$$
满足
$$
r_6v-F_6\in(q_1,q_2,q_3).
$$
这是实际系数理想关系，不仅是某次取点的数值等式，也不要求自由三维模块上的两个矩阵先验交换。

源按相同 $M_T$ 依次计算到 $j=6$。所得三个系数对 $\lambda$ 的次数为 $6,5,5$。其全部有理分子、分母经压缩后又解压并逐项重建验证，保存于本稿精确片段清单及其逐片固定 SHA 的输入中。

## 4. 新固定三行对原 D 的返回

$r_{\mathrm{N1}}$ 是第四个完整原二次式 N1 在上述规则下的剩余行。$r_{T^2z}$ 是对 $T^2z$ 按两种原规则顺序约化所得的差；它是 $M_TM_z-M_zM_T$ 的对应真实歧义行。因此二者同样属于原理想。

令
$$
C=\begin{pmatrix}
r_{\mathrm{N1}}\\
r_{T^2z}\\
r_6
\end{pmatrix},
\qquad
d=(\ell A_2,0,0)-\tau_2.
$$
有 $dv-D\in(q_1,q_2,q_3)$。新矩阵 C 在参数分式域上行列式非零。源直接构造
$$
\alpha=d\,\operatorname{adj}(C)/\det C,
$$
完整核对 $C\operatorname{adj}(C)=(\det C)I$ 和 $\alpha C=d$，再取三项 $\alpha_i$ 的最终公共分母 B，得到多项式系数 $\beta_i=B\alpha_i$，并逐个系数核对
$$
Bd=\beta_1r_{\mathrm{N1}}+\beta_2r_{T^2z}+\beta_3r_6.
$$
所以在原局部环中
$$
BD\in(q_1,q_2,q_3,\mathrm{N1},F_6).
$$
真实原点满足 $D\ne0$，故必有 $B=0$。这里没有要求 $\det C$ 在原点非零；临时分式域主元已经全部清除到最终多项式身份，故其零点没有被删除。

实际 B 的分次为 $(78,46,9)$，20701 项。源仅剥掉实际整除的原权单位：
$$
Q,\quad 1-Q,\quad \ell^2,\quad T_0,
$$
其中 $\ell$ 在 QQ 多项式环中使用其已经支付的分子。每次商都完整乘回。没有实际剥掉第一头因子或新的未知参数因子。将非零常数规范后，得到所述 $P_9$，其分次为 $(73,41,9)$、17389 项。

## 5. 精确输入与实际执行

新源：

[2026-11-27-unit211-Phi-zero-first-head-original-F6-three-row-D-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-first-head-original-F6-three-row-D-input-8542.py)

SHA-256：

a215ce9efb83f66be9febde3a050f64769a18ac6e11fa3096a69e64e74c929eb

精确输入：

[2026-11-27-unit211-Phi-zero-first-head-F6-D-exact-input-manifest-8542.json](../notes/2026-11-27-unit211-Phi-zero-first-head-F6-D-exact-input-manifest-8542.json)

清单分别列出原 F6 三系数行的 6 个片段及 P9 的 5 个片段。每件均小于 100000 字节；加载器先核对各片段文件的 SHA，再按清单顺序拼接 dataChunk，核对整串 SHA 后才作 base64 解码和解压。拆分后在 V8 中按清单重新拼接，与本次实际输出的完整字符串逐字节相等；没有重跑数学源。两条完整压缩载荷均可逐项重建。

清单 SHA-256：

98f0a4d5af1fe650cacb56db3e11a90bd7d2426b2af670cdd41b0a3ca1b2f5e7

F6 行原载荷 866383 字节，SHA-256 为：

503bd798a55c546048f1216bece8da431d36b14116873c08e35c35546f99a103

P9 原载荷 785391 字节，SHA-256 为：

4b6d2d46c294b77a6b14ba905ceaabfe460719e6bb634cee5d261f5b6e2ec51f

实际 run 46038844297，job 140641086709：

| 项目 | 实际返回 |
|---|---:|
| 总时间 | 10.754201447 秒 |
| 峰值子进程 RSS | 118992 KiB |
| 内层退出码 | 0 |
| 完整 F6 三系数行形成 | 1.176649264 秒 |
| 清最终公共分母的全三系数身份 | 10.077763425 秒 |
| P9 及全部系数重建完成 | 10.659902196 秒 |

本次没有重算旧 $[\mathrm{N1},r_{T^2z},r_{Tz^2}]$ 三行的 D-cofactor，也没有重算旧六行 cofactor。新输入是完整原 F6 及其与已有同源两行的新 D 返回。

后续仍需用全部原条件推进这些必要式及所有保留的头零图；这里没有整 $\Phi=0$ 面或普通 Hilbert ISP 完成声明。

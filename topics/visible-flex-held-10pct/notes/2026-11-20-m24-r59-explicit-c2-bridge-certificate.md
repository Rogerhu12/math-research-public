# M24 实际桥段：显式共同二 jet 的 C² 图、连续几何范围与度量传递

日期：2026-11-20。维护会话：Astra-held10-1b6d88ec-20261120。

## 0. 新结论与适用范围

本条绑定新多段 profile、\(q=.06,\lambda=.002,\tau=1,S=.5,b=.2\) 的 M24 实际场。它把 [R59](../results/R59-soft-start-short-bridge-geometry.md) 的条件几何窗落实到该场的**整个桥段**，径向和角向均为连续范围；同时给出一个明确定义的新 \(C^2\) 桥图，而不把舍入后的分片系数或末端 upper-clip 字面函数称为 \(C^2\)。

在唯一尚待本条外支付的绝对入口高度条件
\[
z_0\in[7/20,51/100]
\tag{1}
\]
下，新图在整个桥段满足
\[
|X|<1.245,\qquad X\cdot n>0.3986798571,\qquad
\max(|k_1|,|k_2|)<8.367444.
\tag{2}
\]
支持函数取 R59 的同向法线。此处没有把桥段局部结论外推到完整闭面、真尾或全族 reach。

旧数学一阶 jet 接口与新 \(C^2\) 图的归一化 Gram 矩阵之间还有严格统一界
\[
\|E_{\rm new}(s,\psi)-E_{\rm oracle}(s,\psi)\|_{\rm op}
<3\cdot10^{-8}.
\tag{3}
\]
标量组合器实际给出的更小有理上界为 \(1.581650113\cdot10^{-8}\)。式 (3) 是转换误差；原先有限节点的 metric 数值不因此升级为连续证书。若另证旧数学接口的全桥连续误差小于 \(9\cdot10^{-7}\)，则新图在对应新半径度量下的全桥误差小于 \(9.3\cdot10^{-7}\)。

## 1. 被绑定的实际输入

输入目录是 m3-work/newg-wide-lambda0p002-m24-linear。run.json SHA256：

    c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a

physical.npz SHA256：

    f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d

物理桥端点按两个已存 binary64 数分别作为精确有理数读取：

    prefix_end = 0.49457743382696573
    end        = 1.4252697037606197
    Ls         = 4191465360069805 / 4503599627370496

原 prefix 审计的均值是 **1168 点**等权规则，并非求解器的 768 点，也不是另一诊断所选的 512 点或旧 seam 的 1536 点。节点是源程序实际构造并冻结的 binary64 \(\psi_j\)，权重精确为 \(1/1168\)；并不偷偷换成连续角积分或精确等距符号节点。

原完整 prefix 有限审计 metric 为 \(6.482415924575457\cdot10^{-7}\)，这里只说明输入身份和未改变的背景事实。它不是本条连续证明的前提。当前没有把另一条真尾联立之后可能生成的新场纳入此证书。

## 2. 新 C² 桥图的完整定义

设原储存物理多项式为 \(Y_i(s)\)，每段五次。每个内节点选择其右段的三项
\[
(Y,Y_s,Y_{ss})
\]
作为共同 jet；末节点选择最后一段的左极限。每段以这两端共同 jet 作**精确五次 Hermite 插值**，得到 \(Y_*\)。新图是由共同数据定义的对象，不是将展开系数重新各自舍入后再假定它们精确接合。

具体地，一段长度 \(h\)，旧段右端对目标共同 jet 的差为 \((d_0,d_1,d_2)\)。只加
\[
C(t)=\frac{10d_0-4hd_1+h^2d_2/2}{h^3}t^3
+\frac{-15d_0+7hd_1-h^2d_2}{h^4}t^4
+\frac{6d_0-3hd_1+h^2d_2/2}{h^5}t^5.
\tag{4}
\]
它在左端三 jet 为零、在右端三 jet 正好为所需差，故全段族精确 \(C^2\)。对预 cutoff 的原角图三次样条 \(h(s)\) 作同一共同二 jet Hermite 操作，再乘原精确五次 cutoff 与冻结 warp，定义 \(e_*(s)\)。材料角为
\[
\theta=\psi-\frac{e_*(s)}3\sin(3\psi),\quad
\rho=\theta_\psi=1-e_*(s)\cos(3\psi),\quad
v=\theta_s/\rho.
\tag{5}
\]

桥相位采用原冻结 \(p,\varepsilon,L_1,L_2,L_3\)：初段 \(p(3u^2-2u^3)\)，中段常数 \(p\)，末段 \(p-\varepsilon u^2\)。末段**解析延拓到实际 end**。定义
\[
a_*(s)=1-\int_{s_b}^s\sin\phi(t)\,dt,\qquad a_*'=-\sin\phi.
\tag{6}
\]
相位在内部接头 \(C^1\)，所以 \(a_*\) 为 \(C^2\)。这一步使用真 primitive，不把 GL64 近似值与手填导数当成同一个精确函数。

特别是 M24 的实际终点比三个冻结 binary64 段长的精确和多
\[
31/288230376151711744.
\]
旧 upper-clip 字面半径在这极短区间上变常数，而源程序仍返回非零手填斜率。因此不能用“小区间”论证其真实一阶导数差很小。式 (6) 明确选择解析延拓，完全避开这种错误比较；旧文件未改。

桥段 exact lift 恒为零。以 \(G_*=\) 由 \(qY_*\) 给出的完整有限 Fourier 向量，
\[
P_*(s,\psi)=a_*(s)e_r(\theta(s,\psi))+G_*(s,\psi).
\]
在同一固定 1168 节点，按完整截面法线速度和对流项计算 \(M_*(s)\)，并定义
\[
m_*(s)=z_0+\int_{s_b}^s M_*(t)\,dt,\qquad
F_*=P_*+m_*e_z.
\tag{7}
\]
每个均值节点的正根由下述区间证书保证；\(Y_*,e_*,a_*\) 的正则性保证 \(M_*\in C^1\)，故式 (7) 是桥内及其两侧极限的明确 \(C^2\) 图。与 prefix、真实 tail 的接缝仍应独立支付；本条没有改写原 raw 或声称它们已自动通过。

## 3. 已执行的共同 jet 与全角非均值范围

共同 jet 转换器对 exact binary64 有理输入作精确 Bernstein 范围，给出原分片与 \(Y_*\) 的系数误差：

| 阶数 | 全桥最大误差上界 |
| --- | ---: |
| 0 | \(3.966\cdot10^{-19}\) |
| 1 | \(4.808\cdot10^{-16}\) |
| 2 | \(1.112\cdot10^{-12}\) |

乘实际 \(q\) 并求完整 Fourier 向量后，六个计算坐标差的上界为
\[
|\Delta G|,|\Delta G_\psi|,|\Delta G_{\psi\psi}|\le10^{-18},\quad
|\Delta G_s|\le3.6\cdot10^{-17},\quad
|\Delta G_{s\psi}|\le1.31\cdot10^{-16},\quad
|\Delta G_{ss}|\le9.1015\cdot10^{-14}.
\tag{8}
\]
角图 \(e,e_s,e_{ss}\) 的转换差分别小于
\[
6.662\cdot10^{-19},\quad1.496\cdot10^{-16},\quad5.373\cdot10^{-14}.
\]

新共同 Hermite 对象的连续非均值证书把全部物理多项式段、角样条段和 cutoff 接点统一分为 316 个区间；每区间用精确 Bernstein 变换包径向系数，角向用完整 Fourier 系数绝对和。材料导数包含所有对流项，例如
\[
G_{ss}^{\rm mat}=G_{ss}^{\rm comp}-2vG_{s\psi}^{\rm comp}
+v^2G_{\psi\psi}+(vv_\psi-v_s)G_\psi,
\quad
G_{s\theta}=\frac{G_{s\psi}-v_\psi G_\psi-vG_{\psi\psi}}{\rho}.
\]
按 R59 的参考经向 \(\xi=(s-s_b)/c\) 和三个 \(0/1/2\) 阶协变范数，实际有理上界为
\[
G_0\le .024955126520852,\quad
G_1\le .167414416874712,\quad
G_2\le1.350950108067267.
\tag{9}
\]
同时 \(\rho>.8598784468\)。这些是全角、连续径向范围，不是增密节点的最大值。

## 4. 同一 1168 均值及背景 primitive

共享 mean 范围器保持原均值规则，对原 exact 二进制分片值加入式 (8) 的共同 Hermite 误差，对 \(e,e_s,e_{ss}\) 同样加转换范围。半径和斜率的一阶径向 Dual 值另给 \(\pm10^{-8}\) 的独立背景预算。该预算由已经执行的 [桥 GL64/真 primitive 证书](2026-11-20-short-bridge-gl64-primitive-jet-certificate.md) 支付；不是根据浮点相近而假设。

该背景证书实际给出了源 analytic GL 到同参数真 primitive，以及仿射端点拉回到真 R59 参考的全部所需 \(0/1/2\) jet 界。将两个差作三角相加仍严格小于 \(10^{-8}\)。末端适用域明确包括 \(u\le1+10^{-12}\)。其证明没有声称旧 upper-clip 函数的真实导数满足小差界。

共享 mean 范围器实际接受 4983 个连续径向区间，9648 次尝试、最大细分深度 8，给出
\[
|M_*-\cos\phi_{\rm src}|<.01,\qquad
|M_*'-(\cos\phi_{\rm src})'|<.284,
\tag{10}
\]
\[
1-\alpha^2>.0015626560396909681,\qquad
.0557127068<M_*<.9986787566.
\tag{11}
\]
这是有限 1168 点规则本身的连续径向证书，没有宣称它等于连续角平均。

真实端点拉回 \(c=L_s/L_{\rm ref}\) 已满足 \(|c-1|<10^{-12}\)，源相位与拉回参考的值/一阶差已严格支付。令
\[
H(\xi)=m_*(s_b+c\xi)-z_0-h_{\rm ref}(\xi).
\]
于是 \(H(0)=0\)，式 (10) 加相位和尺度差给出
\[
|H'|<.0101,\quad |H''|<.285,\quad
|H|<.932(.0101)=.0094132.
\tag{12}
\]
这里不需要把旧 GL6 高度查询值直接等同于真积分。绝对 \(z_0\) 仍由 prefix 的同一新图计算。

## 5. R59 几何条件的实际支付

将 \(F_*-\Xi\) 分为式 (9) 的 \(G_*\) 和
\[
J=\delta a\,e_r+H e_z,\qquad
|\delta a|,|\delta a'|,|\delta a''|<10^{-8}.
\]
参考有 \(a_{\rm ref}\ge .299,\ |a_{\rm ref}'|\le1\)。对 R59 的规范，
\[
\begin{aligned}
\|J\|_0&\le\sqrt{(10^{-8})^2+(.0094132)^2},\\
\|J\|_1&\le\sqrt{(10^{-8})^2+(.0101)^2+(10^{-8}/.299)^2},\\
\|J\|_2^2&\le(10^{-8})^2+(.285)^2
+2\left(\frac{10^{-8}+10^{-8}/.299}{.299}\right)^2\\
&\quad+\left(\frac{10^{-8}}{.299^2}+\frac{10^{-8}}{.299}\right)^2
+\left(\frac{.0101}{.299}\right)^2 .
\end{aligned}
\]
标量组合器只作 exact Fraction 运算和整数向上平方根，实际得到
\[
\|F_*-\Xi\|_0\le.03436832652085731<.035,
\]
\[
\eta_1\le.17751441687477232<.179,\qquad
\eta_2\le1.6379449489458198<1.639.
\tag{13}
\]
在 (1) 下，R59 已证 \(|\Xi|<1.21,\Xi\cdot n_0>.74,K_0\le4\)。同向法线锐界 \(|n-n_0|\le\sqrt2\,\eta_1\) 与 \(\sqrt2<99/70\) 给出
\[
F_*\cdot n>.74-1.21(99/70)(.179)-.035
=\frac{2790759}{7000000}.
\]
切向最小奇异值至少 \(1-.179\)，故宽取参考曲率 \(4.001\) 后
\[
K_*<\frac{4.001+1.639}{(1-.179)^2}
=\frac{5640000}{674041}<8.367444.
\]
这证明 (2)，并显著进入 R59 原有的 \(|X|<1.34,\operatorname{support}>.087,K<12.3\) 桥窗。

## 6. 原数学 jet 接口到新 C² 图的 relative Gram 传递

### 6.1 对照对象精确定义

旧端是原精确二进制**分片** \(Y,e\)，源 formal GL 半径的实函数（末段作解析延拓），源手填 \(a'=-\sin\phi\)，以及同 1168 节点按实数算术计算的均值速度 \(M_0\)。其一阶接口为
\[
D_0=\left(a'_0e_r+G_s^{\rm comp}-vG_\psi+M_0e_z,\quad
e_\theta+\frac{G_\psi}{a_0\rho}\right).
\tag{14}
\]
这是后续连续 metric 审计可以明确认证的数学接口。由于 GL 值与手填斜率并非严格互为导数，本文不直接声称 \(D_0=DF_0\)。

新端则是式 (4)–(7) 的真 \(C^2\) 图及其真实归一化导数 \(D_*\)。两个 Gram 矩阵按同一计算点 \((s,\psi)\) 比较；各自材料角参数化都是全角微分同胚，因此这样的统一比较足以传递 supremum。它不是“两个不同角图在相同材料标签的点完全相同”的声明。

### 6.2 Frenet 均值速度的显式 Lipschitz 预算

在旋转的 \(e_r(\theta),e_\theta(\theta),e_z\) 标架中设
\[
U=P_\theta/a,\quad V=P_{\theta\theta}/a,\quad
\kappa a=|U\times V|/|U|^3.
\]
连续非均值证书实际给出 \(U\) 对 \((0,1,0)\) 的差小于 .104248、\(V\) 对 \((-1,0,0)\) 的差小于 .529807。将参考/实际半径小差加入后，以首次离开论证可对完整旧新输入插值统一取
\[
u=.11,\quad v=.54,\quad a\ge.298,\quad \rho\ge.85,\quad
|\rho_\psi|\le.5,\quad |e_s|\le3,\quad \beta=\sqrt{1-\alpha^2}>.039.
\tag{15}
\]
其中 \(|e_s|\) 另对共同 Hermite 角多项式作 exact Bernstein 计算，实际上界 .7000583673872487。证书没有用节点采样替代此界。

记 \(c_0=1-u-v-uv=.2906\)。则
\[
\kappa a\ge c_0/(1+u)^3,\qquad
|(I-TT^t)V|\ge c_0/(1+u).
\]
对输入插值导数大小 \(d_U,d_V\)，有
\[
d_T\le d_U/(1-u),\quad
d_N\le\frac{d_V+2(1+v)d_T}{c_0/(1+u)},
\]
\[
d_\kappa\le
\frac{(1+v)d_U+(1+u)d_V}{(1-u)^3}
+\frac{3(1+u)(1+v)d_U}{(1-u)^4},
\]
\[
d_\alpha\le\frac{\Delta a'}{\kappa_{\min}}
+\frac{1.01\,d_\kappa}{\kappa_{\min}^2}.
\]
归一化及正交投影的标准微分直接给出这些式子。对法向速度
\[
W_{\perp}=\alpha N+\beta B
\]
有
\[
|\dot W_\perp|
\le(1+1/\beta_{\min})d_\alpha+2d_N+d_T.
\tag{16}
\]

原/新输入实际差可宽取
\[
\Delta a,\Delta a'\le10^{-12},\quad
\Delta G_\psi,\Delta G_{\psi\psi},\Delta e\le10^{-17},\quad
\Delta e_s\le10^{-15}.
\tag{17}
\]
半径差依据背景证书；手填 \(a'\) 到解析相位斜率的差小于 \(1.989\cdot10^{-16}\)，而不是依靠 clip 的真实导数。完整系数/角图差见式 (8)。

用完整 \(\rho,\rho_\psi\) 商式及旋转差，有
\[
d_U\le\frac{\Delta G_\psi}{a\rho}
+u\left(\frac{\Delta a}{a}+\frac{\Delta e}{\rho}+\frac{\Delta e}{3}\right),
\]
\[
d_V\le\frac{\Delta G_{\psi\psi}}{a\rho^2}
+\frac{.5\,\Delta G_\psi}{a\rho^3}
+v\left(\frac{\Delta a}{a}+\frac{3\Delta e}{\rho}+\frac{\Delta e}{3}\right)
+\frac{3u\Delta e}{\rho^2}.
\tag{18}
\]
若插值首次达到 \(u\) 或 \(v\) 的界，则截至该点 (18) 仍有效，而初始严格裕量大于整个积分差；因此不可能首次达到，完成 (15) 的统一证明。

对流项 \(vG_{\psi,z}\) 的变化按
\[
\Delta v\le\frac{\Delta e_s}{3\rho}
+\frac{3\Delta e}{3\rho^2},\qquad |G_\psi|<.13
\]
另加。正权均值不放大统一速度差。实际 Fraction 组合结果是
\[
|M_*-M_0|<4.128741\cdot10^{-9}<5\cdot10^{-9}.
\tag{19}
\]
这里的正根条件仅需同一 1168 个均值节点；全角 \(U,V\) 界则由 Fourier 范围支付，二者没有混用。

### 6.3 Gram 矩阵传递

用 (8)、(17)、(19)，并在需要比较实际 Cartesian 向量时加入整标架的 \(\Delta e/3\) 旋转，
\[
|\Delta D_{\cdot1}|<6\cdot10^{-9},\quad
|\Delta D_{\cdot2}|<10^{-12},\quad
\|D_*-D_0\|_{\rm F}<7\cdot10^{-9}.
\]
连续均值范围与 \(G_s<.132\) 给出
\[
\|D_0\|_{\rm op}\le\|D_0\|_{\rm F}
<\sqrt{(1.01(99/70)+.132)^2+1.11^2}<2.
\]
于是
\[
\|D_*^tD_*-D_0^tD_0\|_{\rm op}
\le2\|D_0\|_{\rm op}\|\Delta D\|_{\rm F}+\|\Delta D\|_{\rm F}^2
<3\cdot10^{-8},
\]
证明 (3)。组合器保留更小的实际有理上界，而正文使用易复用的安全门。

两个端点分别以各自半径 \(a_0,a_*\) 归一化，对应两个明确的目标度量。若另要求转回同一个原半径度量，背景证书还给出半径系数的 relative 变化小于 \(1.637\cdot10^{-12}\)，应按矩阵缩放公式另付，不能称 \(g\) 完全不变。最终采用哪个 \(g\) 必须在全族合同里固定。

## 7. 可复现来源与实际终态

以下四个新源均位于 scripts/resume_m3；前三个独立输出已实际完成，最后组合器也实际 exit 0。只保存源和标量身份，不提交场数组。

| 源 | SHA256 |
| --- | --- |
| certify_r59_shared_jet_transfer.py | 85aff94a38f57e184e8bd5ca99b87898f0fec41043b0eedc9325623c4fba2c00 |
| certify_r59_c2_nonmean_ranges.py | 13197d9d5958f254f914a437f94f6a1838ea02b69709a5fa06b39a8423b711b5 |
| certify_r59_shared_fixed_mean_ranges.py | 7ef0989c2ba1bce9583d99c5708d3b5850611cb08fd96e00834f87e286fcea5c |
| combine_r59_m24_c2_geometry.py | 138cca9fca05f0882dcddf921c5a63ecd5fd40f958be9363d03cc2854114ea46 |

共享 mean 源复用已发布的 certify_r59_fixed_mean_ranges.py（SHA256 ab08dc1dc7f24f6e92e3d64fcc530767cb66f5ae5a2940f953460a3274b6a1a5）和 R23 interval_geometry_kernel.py（SHA256 6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7）。共享 mean wrapper 当前以 CLI 执行，直接 import 会进入参数解析；单独调用接口应使用有 main guard 的 base MeanVerifier。

各输出 SHA256：

| scratch 标量输出 | SHA256 |
| --- | --- |
| newg-m24-r59-shared-jets.json | 080af5ad65fc442cebc90939d12869c9d2b16c47fda430e8895b702ae3b98f24 |
| newg-m24-r59-c2-nonmean-certificate.json | efc203e308631d248948d08810c43c57a72f6f2b2521e90cefa71e251a5c406e |
| newg-m24-r59-c2-mean-certificate.json | be9ab23875fde1844d63d937bb4636b47c0f7587789a363f8f27563f683d80a7 |
| newg-m24-r59-c2-geometry-combination.json | af5451fad5c24595407e3f64790037cdd12213d325bbda87b0e6def2132f30bc |
| n4 的 short-bridge-m24-gl64-extended-gap.json | d9f7adabdf1621f97c637795c0b342bf18c9c05b07579325929c705637aef1dd |

运行前三源时分别给 --source-run、--physical、--support-dir、--out；共享 mean 源另给 --mean-nodes 1168 与 --interval-kernel。组合器接收上述同场的 --shared、--nonmean、--mean、--background 四个输出，检查输入 SHA 与源 SHA 一致，只重算很小的角多项式范围与有理标量组合，不重跑已付背景积分或 BVP。

## 8. 仍明确保留的义务

本条未支付 (1) 的绝对入口高度、prefix 与 tail 的完整 \(C^2\) 接缝、真实非线性 DN、完整闭面的 reach/自交、完整同一 \(g\) 族或最终 held 比例。也没有支付旧 GL6 高度查询与新真均值 primitive 的全域位置差；本条直接为新真 primitive 对象证明几何范围，入口锚由同一新对象的 prefix 提供。

旧 finite metric、源程序手填 jet、literal clipped 函数导数、新 \(C^2\) 图四者在本文中保持区分。式 (3) 使一个明确的连续数学接口证书可以传递到新图；它不替代仍欠的连续 metric 基线证书，也不对所有 machine/libm 求值误差作笼统背书。

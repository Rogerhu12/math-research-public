# 剩余 1961 单列帽格及同一连续 $Z$ 真实边界合同

本合同消费公开 v3 的 16 个成功单列格与原完整帽证书，只计算尚未完成的 1961 格。最终边界属于完整连续方向 $Z$；原 $q^*$、raw 方向与 $Z$ 三者保持区别。所有新数值仅在 Rogerhu12/math-research-public 的 Actions 运行。

## 1. 固定原件及数学对象

原 v3 运行 43610982446 的完整 native SHA256 是
`f36831b1f5cc354548686c7d3e5f3fdfb10a456899d25f57d1be1b4cefccbe5c`，
科学源 SHA256 是
`af0097d3e2e3b44bd1ef68c0b1384534810b239fcf35b7c425255c21f4e9ec71`。
其 11 个实际门以及真实 child 退出码为零必须验证，原输入 native 和三份 artifact process 的 SHA 必须与 v3 保存的字节一致。不能用后来仓库多了最终 publish receipt 的 process 替换其原 artifact snapshot。

背景仍是 ac1 候选的连续 M32 修补，定义
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。
moving 参数取仿射偏移零，即固定物理 $\eta_0$ 和原 $\nu$。物理系数证书保留原 $10^{-9}$ 半宽，moving Hessian 桥只授原固定参数。

同一全 193 态连续方向 $Z$ 的定义 SHA256 为
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`，
其全区间修补 native SHA256 为
`87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88`。
本消费者只使用已经证明覆盖整个 $[0,25/8]$ 的角零阶 pair $A^0$ 修补费 $E_0$，不把只覆盖负区的方向范数转授到正帽。

## 2. 一列方向、完整物理源及端点复用

原 v3 保存一个完整 97 槽二进制有理方向 $w_0$，含 even mean。后续直接从它的完整 hexadecimal 值恢复相同向量，不能重新选一个近似向量。原全部 state、单侧 derivative 与 endpoint 数组逐字节核 SHA，然后以同一准确 Hermite 多项式右乘 $w_0$。它没有重建浮点矩阵，也没有重算原完整 97 列 residual。

原真实 cut 为 $L=9/10$，首保存节点为 binary64$(0.9)$。这两个点继续区分；第一个 Hermite 片允许原 v5 的微小左延拓，端口始终在 $L$。真实入口、真实 outer Robin、mean 与接缝六项直接复用成功 v3 的准确误差证书，不再次计算，也不把首节点数组代替入口值。

旧成功单列格为
$$
1,2,3,4,5,6,7,8,9,10,11,12,17,18,21,22.
$$
四个新的左闭右开原索引范围为
$$
[0,512),\quad[512,1024),\quad
[1024,1536),\quad[1536,1977). \tag{C.1}
$$
每个范围先扣除这 16 格，因此只新计算 1961 格。range 的真实 source 不准请求或重算这些成功格。失败恢复时，也仅继续同一完整输入、同一原 $w_0$、同一计划 SHA 和同一请求列表的准确前缀。

每个新格沿原 packed-v5 全 257 物理状态、完整 255 输出支撑和完整系数尾公式，保留八个平方通道：
$$
f_B^2,\ f_C^2,\ f_{B0}^2,\ f_{C0}^2,\
r_B^2,\ r_C^2,\ d_B^2,\ d_C^2. \tag{C.2}
$$
普通/mean/ordinary remainder 通道按原真实径向长度积分；divergence 模块沿原证书的无额外长度定义保留。不能把 mean 槽套用非mean 的 $1/\sqrt2$。

finish 核四个实际成功过程，要求同 workflow run、同科学源和输入、同原行 SHA，并验证新 1961 行与旧 16 行的无重复并集准确等于全部 1977 行。对每个同名平方通道，可将单列上界与旧 HS 平方上界乘 $\|w_0\|^2$ 取合法较小值，再全区间求和。

## 3. 完整帽误差与原误差算子

把上节八个体源误差与复用的六项
$$
e_L,\ e_D,\ e_0,\ e_{B0},\ j_B,\ j_C
$$
交给原完整 14 个 Green gains，得到
$$
\varepsilon_{\rm phys}(w_0)
 \le \sum_{\alpha=1}^{14} G_\alpha E_\alpha. \tag{C.3}
$$
所有通道和独立 mean 保留。与原 v3 已证方向上界再取合法最小值，仅收紧同一方向上的范数，不改变任一原多项式或原未知输入算子。

原完整 Hessian 桥给
$$
\varepsilon_{\rm mov}(w_0)
 \le M\,\varepsilon_{\rm phys}(w_0)+A\|w_0\|. \tag{C.4}
$$
$M,A$ 均取同一已完成原 native。若仅某个方向的 known residual 变小，不能宣称未知输入上的完整帽算子误差或 weighted kernel 同时变小。

plan 先只读取成功 v3、原完整帽及边界 native，不下载原 767MB 数组；它导出 14 项实际预算和只含六端点项及 bridge 的预算。后者只是当前上界中的一个保留部分，绝不是实际误差的下界，也不能凭它宣称真正误差不可能更小。

## 4. 同一连续 $Z$ 的完整边界转移

原完整边界 native 保存 raw 方向在腰右侧和 cut 左侧的全部 193 个真实物理振幅。将所有非mean 正弦/余弦振幅除 $\sqrt2$，even mean 第 96 槽保持原值，得到正交坐标
$$
h_{\rm raw}(0),\qquad h_{\rm raw}(L)=(o_{\rm raw},e_{\rm raw}).
$$
方向修补证书给完整 pair
$$
\|Z-h_{\rm raw}\|_{L^2_\varphi}
 \le\|Z-h_{\rm raw}\|_{A^0_\varphi}\le E_0 \tag{C.5}
$$
在全区间每个点都成立。不存在未收费的 $q^*$ 均值补偿；本合同直接从 raw 及 (C.5) 转到 $Z$。

令原真实 cut 的二进制 nominal odd 块为 $[I_{96},J]$，独立 mean 行为 $M_0$。所有完整行都从原 native 的准确 hexadecimal 提案恢复。于是
$$
\begin{aligned}
b_{\rm odd}^{\rm nom}(Z)
 &\le \|o_{\rm raw}+J e_{\rm raw}\|
       +\Big(96+\sum_{i,j}|J_{ij}|^2\Big)^{1/2}E_0,\\
b_{\rm mean}^{\rm nom}(Z)
 &\le |M_0 e_{\rm raw}|+\|M_0\|E_0,\\
\|e_Z\|&\le\|e_{\rm raw}\|+E_0,\\
\|e_Z-w_0\|&\le\|e_{\rm raw}-w_0\|+E_0.
\end{aligned} \tag{C.6}
$$
第一式使用完整 $[I,J]$ 的 Hilbert–Schmidt 上界；没有只收费 even 部分而漏掉 odd 修补。独立 mean 的线性行误差单独保留。

令 $\varepsilon_{\rm mov}^{\rm op}$ 是原完整已认证的**误差算子**范数。线性差算子作用于同一输入，所以
$$
\varepsilon_{\rm mov}(e_Z)
 \le \varepsilon_{\rm mov}(w_0)
       +\varepsilon_{\rm mov}^{\rm op}
            \big(\|e_{\rm raw}-w_0\|+E_0\big). \tag{C.7}
$$
这里不是完整帽解算子范数；误差对象与原 v3 完全相同。

原 cut native 已付的三个 before-cap 费用记为 $c_\ell,c_m,c_H$，完整 physical-to-moving row gain 为 $S$。同 $Z$ 真来源准确满足
$$
\begin{aligned}
g_\ell&\le b_{\rm odd}^{\rm nom}(Z)+c_\ell\|e_Z\|
                  +S\varepsilon_{\rm mov}(e_Z),\\
g_m&\le b_{\rm mean}^{\rm nom}(Z)+c_m\|e_Z\|
                  +\varepsilon_{\rm mov}(e_Z),\\
g_R&\le(g_\ell^2+g_m^2)^{1/2},\\
g_H&\le c_H\|e_Z\|+S\varepsilon_{\rm mov}(e_Z),\\
g_0&\le\|P_{\rm odd}h_{\rm raw}(0)\|+E_0 .
\end{aligned} \tag{C.8}
$$
$Z$ 是完整 193 态方向，所以 cut 的已知高输入准确为零；(C.8) 的已知全高输出仍保留。这里没有把**未知**高输入置零，也没有把已知高来源误作高反馈范数。

(C.8) 使用原已经证明的 boundary source 单位：径向 $R$ 权在真实来源中准确取消。原 $L_0,D_0,L_R,D_L$、source convention 和 high norm contract 原样保存；腰末端零长度 projector 跳仍必须消费。

## 5. 数值与发布范围

DAG 为 plan、四个 range、finish。plan 成功原件已存在时只验证完整身份并逐字节复用原 native，使后续重新派发仍保同 plan SHA。新 worker 每十分钟真实 pull 并核根及课题 README 差异；遵循原 reviewed driver 的 rebase/push 规则。每条实际前缀、真实失败及最终证书均保存，原六端点项和旧 16 格不重算。

所有新 plaintext 摘要只保必要上界、14 项预算及统计；写出前逐件验证 UTF-8 长度不超过 60000 字节。完整数学行与完整向量留在 native，超过原发布大小限制时沿现有 lossless parts 保存原字节。集成不搬运二进制或原大摘要。

最终成功将授完整 1977 单列帽误差，以及与全 7721 行源相同定义的 $Z$ 腰/cut/high 来源。随后仍需消费现成连续 Green ports 的实际分布、保全部 projector jumps、未知高输入反馈和独立 mean。它单独不授有限 193 响应误差、完整 PDE 逆、真正 Schur 或改变背景后的非线性结论。

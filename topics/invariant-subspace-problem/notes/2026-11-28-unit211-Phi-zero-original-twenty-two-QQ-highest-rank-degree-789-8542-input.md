# Phi：同一二十二列最高 QQ$(Q)$ 矩阵的精确秩与 13 阶消失输入

日期：2026-11-28（Asia/Taipei）。尚未执行；120 秒 / 1 GiB。

## 1. 已付原对象

使用[二十二列原 determinant 与 802/789 次差额](../results/R150-appendix-unit211-Phi-zero-unlowered-twenty-two-original-columns-and-802-789-degree-gap.md)中同一个 $B_{22}(u,Q)$ 和严格 QQ 次数对偶 $a_i,b_j$。各列是完整原来源，只有旧已付权分母；原 $H_{42}$ 不被倒置。

此前唯一真实 run 46095542545 已支付：
$$
\deg_u P\le802,\qquad P=\det B_{22},
$$
且固定原约化满足
$$
\deg_u\overline P(u,2)=789,\qquad
[u^{789}]\overline P(u,2)=790\ne0
\quad(p=1009).
\tag{1}
$$
本次不重算该模 determinant、不重新选择列，也不重跑 Hungarian。

## 2. 同一个估值矩阵

置 $t=1/u$，在 $K=\mathbb Q(Q)$ 上定义
$$
N_{ij}(t)=t^{a_i+b_j}(B_{22})_{ij}(t^{-1},Q).
$$
已付逐项次数界保证所有 $N_{ij}\in K[t]$，并有
$$
\det N(t)=t^{802}P(t^{-1},Q).
\tag{2}
$$
本次只取真正常数矩阵
$$
H(Q)=N(0),\qquad
H_{ij}(Q)=[u^{a_i+b_j}](B_{22})_{ij}.
\tag{3}
$$
它由同一二十二原列逐列 LCM 清除所得；前次实际全部 1009 常数整化指数为零，本次明确沿用同一常数，不重新归一。

## 3. 新完整 QQ 秩目标

源对 $H(Q)$ 做增广 $[H\mid I_{22}]$ 的 fraction-free 消元。每次多项式除法都完整乘回；所有实际主元及前主元是非零 QQ$[Q]$ 多项式，所以每一步在 $K$ 上可逆。末尾输出实际秩 $r$，并逐项返回完整
$$
EH=H_{\rm echelon}
$$
的 $22^2=484$ 个多项式身份，同时验证后 $22-r$ 行全部为零。完整 $E$ 在 $K$ 上可逆的来源是所记录的交换和非零主元行操作，毋需再计算其 determinant。

这是证明 (3) 的函数域秩；这里的 $Q$ 主元不是原物理参数单位，也不会用于删除任何权点。

因为 $E$ 不依赖 $t$，$EN(t)$ 至少有 $22-r$ 行被 $t$ 整除。由 (2) 得
$$
\deg_uP\le802-(22-r).
\tag{4}
$$
(4) 先在 $K$ 上成立，意思是相应高次 $u$ 系数作为 QQ$(Q)$ 元为零；因这些原系数本来是 QQ$[Q]$ 多项式，其恒等消失覆盖全部 $Q$，包括消元过程中任意主元的零点。

若实际 $r=9$，(4) 给 $\deg_uP\le789$。再用已经支付的 (1)，即可得到
$$
\deg_uP(u,Q)=\deg_uP(u,2)
=\deg_u\overline P(u,2)=789,
$$
并且固定切片最高系数为 1009 单位。这时才可把原完整 789 次权多项式用于后继有限整模型。

若实际 $r>9$，只记录改进后的真实上界与仍未付的差额；不宣称保度。没有高阶核提升、没有旧模投影回放，也不由单个秩结论宣称 Phi 空。

## 4. 源和依赖

建议文件：
2026-11-28-unit211-Phi-zero-original-twenty-two-QQ-highest-rank-degree-789-8542.py。

源 blob ad6d6c7a83532fa28c6a5a0f402569aec68ba13c；7327 字节；SHA256
0350cf7708142f22bedd6ff6b807391d8c0a4481ba9406b6fbfdefff4f09d1cb。

新增直接依赖为上次二十二列源，环境变量 ISP_PHI_RAW_TWENTYTWO_SOURCE。只执行其 4080 字节必要原列定义前缀，SHA256
d6e4f9f2eaabf58efe7a06c7b4b4da8b3effb77cadc3f881c4a5ba12a3804e89，
在任何旧 LCM/degree/Hungarian/模 determinant 段之前停止；本次的 LCM 是构造新 QQ 最高系数所必需的一次输入。

沿用其五个小源码依赖，合计六个，无历史 JSON。所有计时器受同一最初绝对 120 秒截止约束。只保存小秩/主元 profile、精确身份数量、SHA 与实际回执，不保存可重算矩阵、系数、编码或分片。

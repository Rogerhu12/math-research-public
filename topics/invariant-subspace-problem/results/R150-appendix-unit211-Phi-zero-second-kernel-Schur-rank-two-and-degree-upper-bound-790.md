# Phi：完整二阶核 Schur 秩二，原二十二列次数上界降至 790

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。

## 1. 准确结论

继续[一阶核 Schur 秩五及 791 次上界](R150-appendix-unit211-Phi-zero-first-kernel-Schur-rank-five-and-degree-upper-bound-791.md)的同一个原
$$
P(u,Q)=\det B_{22}(u,Q).
$$
本次完整支付二阶的逆矩阵修正。剩余三维核上的实际矩阵在 $K=\mathbb Q(Q)$ 中秩二，故
$$
\boxed{789\le\deg_uP(u,Q)\le790,}
\qquad
789\le\deg_uP(u,2)\le790.
\tag{1}
$$
只有一阶差额仍未付。没有声称原 QQ 次数为 789，也没有假定此前 $Q=2,p=1009$ 的模切片保度。

## 2. 完整二阶原公式

固定已付对偶和原核坐标，写
$$
N(t)=H_0+tH_1+t^2H_2+O(t^3),
\qquad
\det N(t)=t^{802}P(t^{-1},Q).
$$
此前已付 $\operatorname{rank}_K H_0=14$。固定前稿实际十四阶原 minor $A=H_0[I,J]$，用其必要定义返回
$$
A\operatorname{Adj}=\operatorname{Adj}A=\Delta I_{14},
$$
以及完整原八维左右核 $U,V$；补坐标块都是 $\Delta I_8$。前稿的一阶矩阵为
$$
S_1=UH_1V,\qquad \operatorname{rank}_K S_1=5.
$$
本次新二阶系数 $H_2$ 最大 $Q$ 次数十一，SHA256 为
91fb294f8164048123a43cee1e77c9da17aaccb7791d8b634451d958e0f553b8。

常数核变换后，两交叉块从一阶开始。因此原八阶完整 Schur 补是
$$
S(t)=t\Delta^{-2}S_1+t^2\Delta^{-3}W_2+O(t^3),
\tag{2}
$$
其中
$$
W_2=\Delta UH_2V-
(UH_1[:,J])\operatorname{Adj}(H_1[I,:]V).
\tag{3}
$$
式 (3) 的第二项不能省略；它是原 $A(t)^{-1}$ 消元产生的完整二阶修正。两个交叉块均带 $t$，故二阶只需 $A(0)^{-1}$，其自身的一阶变化从三阶才开始参与。

## 3. 已付秩五矩阵的真三维核与新秩

把 $S_1$ 的实际非零行、列内容记为 $D_r,D_c$，令
$$
S_1=D_rT_1D_c.
$$
所有内容除法与全部 64 个尺度身份完整返回。固定此前独立列 $(1,2,5,6,7)$，在 $Q=2$ 的 QQ 点值只选择新的五阶原行 minor，实际原行是 $(1,2,3,4,7)$。这一步只定义新核基，没有重做旧八阶秩测试。

该五阶块的非零 adjugate 标量 $\Delta_2$ 次数为九。程序返回 50 个双向乘积坐标，并以补坐标 $\Delta_2 I_3$ 构造完整三维核 $U_2,V_2$。全体
$$
U_2T_1=0,\qquad T_1V_2=0
$$
的 48 个坐标均实际返回。

令 $l_r,l_c$ 是对应尺度的 LCM，定义多项式矩阵
$$
\widehat U=l_rU_2D_r^{-1},\qquad
\widehat V=l_cD_c^{-1}V_2.
$$
全部短除法和另外 48 个
$$
\widehat U S_1=0,\qquad S_1\widehat V=0
$$
坐标也完整返回。所有尺度只用于 $K$ 中的坐标选择，不是原物理单位。

真正的新矩阵为
$$
K_3=\widehat U W_2\widehat V.
\tag{4}
$$
实现先收缩 $L=\widehat U U,R=V\widehat V$，实际以
$$
K_3=\Delta LH_2R-
(LH_1[:,J])\operatorname{Adj}(H_1[I,:]R)
$$
计算，另逐项返回 $LH_1R=0$ 的九个坐标。没有先生成更大的高次八阶二次矩阵。

$K_3$ 最大 $Q$ 次数 251，SHA256 为
4aacdbb9a20536e2ce661f87f1b713267fed2de3a4bd982eb7195788fe08ea75。
完整逆修正项的 SHA256 为
967467b955c49f778129ea6ddb8adfe06b067a86a0d075b48aa40882f95840f3。

精确除去非零公共内容后，新三阶矩阵的条目最高 $Q$ 次数二。完整增广消元返回九个变换坐标；实际主元列为 $0,1$，主元次数为 $1,2$，末行全部为零。因此
$$
\operatorname{rank}_K K_3=2.
\tag{5}
$$
本次全程 5272 次精确多项式除法均完整乘回。

## 4. 十二阶无穷消失与全部零纤维

由原最高秩十四，先提八个 $t$ 因子；一阶八阶矩阵秩五，再提三个；在这三个剩余方向上，(5) 再给一个。于是
$$
\operatorname{ord}_{t=0}\det N(t)\ge8+3+1=12,
$$
从而
$$
\deg_uP\le802-12=790.
$$
结合同一原固定 determinant 已付的模 789 次下界，即得 (1)。

此推导只在函数域中证明原高次系数恒等消失。这些系数本来是 QQ$[Q]$ 多项式，因此结论覆盖全部 $Q$，未删去任何 minor、内容、尺度零点，也未删去 $H_{42}=0$。

下一剩余一维三阶系数必须同时包括原十四阶消元和下一五阶消元的修正。如果该标量非零，则原 QQ 次数就是 790，而旧模切片可能真实降次；不能为追求 789 忽略该可能。本条尚未计算这一新标量。

## 5. 唯一实际执行

源：[完整二阶三维核输入](../notes/2026-11-28-unit211-Phi-zero-original-twenty-two-second-kernel-Schur-degree-input-8542.py)，12947 字节，blob
84d7793cd11a6bd791d3e1b5f6ed6c1db8688424，SHA256
35d7fdd4e6c84b85adf10c03f14b0009069e0c996a03eb152dca283ad3d8dc3f。

唯一首次 run 46098274233、job 140834619712；源及真实 pull 后提交
d7757aff6e1ad7e6c789718e8002c9a8b5f85f6a。
实际 $9.916448275$ 秒、最大 RSS $67032$ KiB、内层退出码 $0$。
stdout 2942 字节，SHA256
8c7d4e76d9dd30510bf8f0b641898982a3aca9c62308a9ea88e5cbec593ed1b6。

真实 pull 为 2026-11-28 02:29:10.476795 UTC，两份 README 无变化。本次未重跑旧二十二阶或八阶秩、旧 Hungarian、旧模 determinant；没有保存可重算矩阵载荷，没有声称整个 Phi 或普通 ISP 已完成。

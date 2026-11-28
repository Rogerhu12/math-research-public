# Phi：二阶三维核 Schur 的完整逆修正输入

日期：2026-11-28（Asia/Taipei）。尚未执行；120 秒 / 1 GiB。

## 1. 已付范围与真正新目标

继续[一阶核 Schur 秩五及 791 次上界](../results/R150-appendix-unit211-Phi-zero-first-kernel-Schur-rank-five-and-degree-upper-bound-791.md)的同一原 $B_{22}$、同一固定次数对偶和
$$
N(t)=H_0+tH_1+t^2H_2+O(t^3),
\qquad
\det N(t)=t^{802}P(t^{-1},Q).
$$
已付 $\operatorname{rank}_{K}H_0=14$，其完整八维核的一阶矩阵秩五，其中 $K=\mathbb Q(Q)$。所以当前准确范围为 $789\le\deg_uP\le791$。

本次新输入是 $H_2$ 及剩余三维核上的完整二阶系数，不重跑旧二十二阶秩、旧八阶秩、Hungarian 或模 determinant。

## 2. 固定十四阶块和真实二阶公式

固定前稿实际原行、原列 minor；按 $(I,I^c)$、$(J,J^c)$ 分块，记 $A=H_0[I,J]$。必要定义重新构造完整
$$
A\operatorname{Adj}=\operatorname{Adj}A=\Delta I_{14},
$$
以及原多项式核 $U,V$，其补坐标块均为 $\Delta I_8$，并保全 $UH_0=0,H_0V=0$。它们属于同一原最高矩阵，不重新选择原十四阶 minor。

归一核 $U_0=U/\Delta,V_0=V/\Delta$ 与固定原主坐标组成常数可逆变换。变换后的上下交叉块常数项均为零，因此其完整 Schur 补具有
$$
S(t)=t\Delta^{-2}S_1+t^2\Delta^{-3}W_2+O(t^3),
\qquad S_1=UH_1V,
\tag{1}
$$
其中
$$
\boxed{
W_2=\Delta UH_2V-
\bigl(UH_1[:,J]\bigr)\operatorname{Adj}
\bigl(H_1[I,:]V\bigr).
}
\tag{2}
$$
式 (2) 的第二项来自完整 $A(t)^{-1}$ 消元；不能只使用 $UH_2V$。因为两个交叉块均以 $t$ 开始，二阶所需的逆正是 $A(0)^{-1}=\operatorname{Adj}/\Delta$；逆的一阶项只从三阶开始参与。该推导没有遗漏 $H_1[I,J]$ 的作用，它已经包含在 (2) 的完整核交叉项中。

## 3. 已付秩五矩阵的完整三维核

以此前实际的行、列内容定义
$$
S_1=D_r T_1D_c.
$$
全部内容除法乘回；这些尺度仅在 $K$ 中非零，不是物理单位。固定已付 $T_1$ 的独立原列 $(1,2,5,6,7)$，只在预定 $Q=2,3,5,7$ 选择一个新的五阶原行 minor，用完整 QQ 有理点值而非原解秩筛选。

随后对这个五阶块实际返回双向 adjugate，形成多项式左右核 $U_2,V_2$。补坐标块均为 $\Delta_2 I_3$，且完整返回
$$
U_2T_1=0,\qquad T_1V_2=0.
$$
结合已付秩五，它们是完整三维核。令 $l_r,l_c$ 分别是 $D_r,D_c$ 对角多项式的 LCM，定义
$$
\widehat U=l_rU_2D_r^{-1},\qquad
\widehat V=l_cD_c^{-1}V_2.
$$
两者都是多项式矩阵；所有短除法及
$$
\widehat U S_1=0,\qquad S_1\widehat V=0
$$
均实际完整返回。没有重新对旧八阶矩阵做 rank 测试。

真正新的三阶矩阵为
$$
K_3=\widehat U W_2\widehat V.
\tag{3}
$$
实现先收缩为 $L=\widehat U U$、$R=V\widehat V$，直接计算
$$
K_3=\Delta LH_2R-
(LH_1[:,J])\operatorname{Adj}(H_1[I,:]R),
$$
避免生成一个更大的高次八阶二阶矩阵。还实际返回 $LH_1R=0$，随后对新的三阶矩阵作完整 QQ$(Q)$ 秩返回。

## 4. 只由实际新秩决定次数结论

若实际 $r=\operatorname{rank}_K K_3$，先提原八个 $t$ 因子，再提一阶八阶矩阵的三个 $t$ 因子，最后在这三维核上至少再提 $3-r$ 个，故
$$
\operatorname{ord}_{t=0}\det N(t)\ge8+3+(3-r),
\qquad
\deg_uP\le788+r.
\tag{4}
$$
只有实际 $r=1$ 才与旧模 789 次下界合成精确 789 次及 $Q=2,p=1009$ 保度；$r=2$ 只付 790，$r=3$ 不改善 791。未执行前不猜秩。

所有函数域变换只证明原 $u$ 高次系数恒等为零，因其原系数属于 QQ$[Q]$，结论覆盖全部 $Q$。任何核尺度、minor 或内容零点，以及整个 $H_{42}=0$，均未从原图删除。

## 5. 冻结源和依赖

源文件建议为
2026-11-28-unit211-Phi-zero-original-twenty-two-second-kernel-Schur-degree-input-8542.py。

源 SHA256 为 35d7fdd4e6c84b85adf10c03f14b0009069e0c996a03eb152dca283ad3d8dc3f，12947 字节。直接读取原二十二列源的 4080 字节必要定义前缀，不读取旧一阶源。因此仍只用同六件小源码依赖及原有环境变量，新增源没有历史 JSON、没有系数或矩阵载荷。

完整 120 秒绝对截止覆盖所有必要定义前缀；固定 1 GiB。仅保存小索引、SHA、秩、乘回数及执行回执。
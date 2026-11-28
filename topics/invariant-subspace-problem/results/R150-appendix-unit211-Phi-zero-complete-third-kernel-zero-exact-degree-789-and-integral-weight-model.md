# Phi：完整三阶核标量为零，原二十二列恰为 789 次及保度整模型

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。

## 1. 原对象和最终次数结论

继续[二阶核秩二及 790 次上界](R150-appendix-unit211-Phi-zero-second-kernel-Schur-rank-two-and-degree-upper-bound-790.md)的同一原
$$
P(u,Q)=\det B_{22}(u,Q)\in\mathbb Q[u,Q].
$$
本次完整支付两层 Schur 修正后的最后一维三阶标量。实际第一层三阶项为零，第二层五阶修正也为零，故完整标量为零。结合同一固定原 determinant 的已付模下界，得到
$$
\boxed{
\deg_uP(u,Q)=\deg_uP(u,2)=
\deg_u\overline P(u,2)=789.
}
\tag{1}
$$
最后一项在 $\mathbb F_{1009}$ 中，其首项系数为 790。至此原 QQ 次数及该模切片保度都严格支付。

这仍是原必要权多项式的次数结论，未把其所有根当成原物理解，也未宣称整个 Phi 空。

## 2. 固定同源估值矩阵

沿用实际整数对偶，总和 802，令
$$
N(t)=H_0+tH_1+t^2H_2+t^3H_3+O(t^4),
\qquad
\det N(t)=t^{802}P(t^{-1},Q).
\tag{2}
$$
前三层已付实际秩依次为 $14,5,2$。本次只新增真实 $H_3$；其最大 $Q$ 次数十二，规范 SHA256 为
a23ec5d064921220814e5331a232ef21ac02542db843a6e0cc82dcddf450a309。

十四阶、五阶原 minor 均固定为此前实际索引。必要定义保持同一 $H_0,H_1,H_2$ 与完整核尺度；没有重跑此前三阶、八阶或二十二阶 rank。

## 3. 第一层完整三阶分子

记 $A=H_0[I,J]$，用已经支付的原 minor 定义
$$
A\operatorname{Adj}=\operatorname{Adj}A=\Delta I_{14},
\qquad UH_0=0,\quad H_0V=0.
$$
$U,V$ 的补坐标块均为 $\Delta I_8$。其完整第一层 Schur 补为
$$
S(t)=t\Delta^{-2}S_1+
t^2\Delta^{-3}W_2+
t^3\Delta^{-4}W_3+O(t^4),
$$
其中 $S_1=UH_1V$，此前完整二阶项是
$$
W_2=\Delta UH_2V-
(UH_1[:,J])\operatorname{Adj}(H_1[I,:]V).
$$
本次三阶项使用
$$
\begin{aligned}
W_3={}&\Delta^2UH_3V\\
&-\Delta(UH_2[:,J])\operatorname{Adj}(H_1[I,:]V)\\
&-\Delta(UH_1[:,J])\operatorname{Adj}(H_2[I,:]V)\\
&+(UH_1[:,J])\operatorname{Adj}
 H_1[I,J]\operatorname{Adj}(H_1[I,:]V).
\end{aligned}
\tag{3}
$$
式 (3) 保留了原 $A(t)^{-1}$ 一阶变化的最后一项，没有用裸 $UH_3V$ 替代完整系数。

## 4. 第二层五阶修正和末一维核

沿用实际内容尺度运输后的完整三维核 $\widehat U,\widehat V$，记
$$
K_2=\widehat U W_2\widehat V,
\qquad \operatorname{rank}_{\mathbb Q(Q)}K_2=2.
$$
第二层原五阶主块是
$$
B=S_1[I_2,J_2],
\quad
I_2=(1,2,3,4,7),\quad
J_2=(1,2,5,6,7).
$$
从既有 adjugate 和全部行列内容尺度，实际构造并返回
$$
B\operatorname{Adj}_5=
\operatorname{Adj}_5B=\Delta_5I_5
\tag{4}
$$
的 50 个坐标。这里是原 $S_1$ 的主块，并未漏掉内容尺度。

最后只用 $K_2$ 的独立列 $(0,1)$，在 QQ 点 $Q=2$ 选择原行 $(1,2)$ 的二阶 minor。显式二阶 adjugate 给八个双向乘积返回。相应一维左右核 $u,v$ 的六个核坐标和运输后的六个核坐标全部返回。

精确除向量公共内容写成
$$
u\widehat U=g_L\ell,\qquad
\widehat Vv=g_Rr,
$$
其中所有尺度非零，只用于函数域坐标。还实际返回低阶项 $\ell W_2r=0$。

真正的末标量是
$$
\Theta=
\Delta_5\,\ell W_3r-
(\ell W_2[:,J_2])\operatorname{Adj}_5
(W_2[I_2,:]r).
\tag{5}
$$
源将 $\ell U,Vr$ 提前收缩，直接计算 (3)–(5) 的一行一列与五列交叉项，没有生成更大的高次八阶矩阵。

实际返回
$$
\ell W_3r=0,\qquad
(\ell W_2[:,J_2])\operatorname{Adj}_5
(W_2[I_2,:]r)=0,
\qquad
\boxed{\Theta=0.}
\tag{6}
$$
这不是单一参数点测试，而是完整 QQ$[Q]$ 多项式恒等式。本次全程 5355 次精确多项式除法均完整乘回。

## 5. 十三阶无穷消失及真实保度

原最高秩十四先给八个 $t$ 因子；其八阶一阶矩阵秩五，再给三个。接着三阶矩阵秩二先给一个，而 (6) 使这一剩余标量的一阶系数也消失，再给一个。因此
$$
\operatorname{ord}_{t=0}\det N(t)\ge8+3+1+1=13.
$$
由 (2)，
$$
\deg_uP\le802-13=789.
\tag{7}
$$
这些原高次系数在 $\mathbb Q(Q)$ 中为零，而它们本来属于 QQ$[Q]$，所以恒等为零，覆盖全部 $Q$，包括所有核尺度、minor 和内容的零点。整 $H_{42}=0$ 同样保留。

此前唯一实际固定模 determinant 已支付
$$
\deg_u\overline P(u,2)=789,\qquad
[u^{789}]\overline P(u,2)=790\ne0
\quad\text{于 }\mathbb F_{1009}.
$$
与 (7) 合成 (1)。旧模多项式规范 SHA256 为
2b40bf98b99fb097b4d24d3d1f21291b782a2dc0678f756838fe2789343e192b；
本次没有重算该 determinant。

源在 (6) 形成时立即输出已成次数结论，随后才处理原 $u^{790}$ 系数的附加记录；它实际就是零多项式。没有把附加过程设为数学登记门槛。

## 6. 可合法使用的 789 维整权模型

原列已按固定的 1009 Gauss 常数清理，实际所有常数指数均为零，所以 $P$ 的系数属于 $\mathbb Z_{(1009)}[Q]$。令
$$
\gamma(Q)=[u^{789}]P(u,Q).
$$
由保度，
$$
\gamma(2)\equiv790\pmod{1009}.
$$
故在局部基环
$$
\mathcal O=\mathbb Z_{(1009)}[Q]_{(1009,Q-2)}
$$
中 $\gamma$ 是单位，且
$$
\mathcal W=
\mathcal O[u]\big/\bigl(\gamma^{-1}P\bigr)
\tag{8}
$$
是秩 789 的有限自由代数，基为 $1,u,\ldots,u^{788}$。其模纤维正是已付完整 789 次多项式；全部因子及幂零重数保留。

(8) 是用于后续原关系提升的整权模型，不表示已反演全部原物理权单位，也不表示每个块都有合法 $\lambda$ 头。相关单位、头与同点原关系仍须在完整块中实际支付。局部化的 $\gamma$ 也没有被加入全复权面的物理单位表。

## 7. 唯一实际执行

源：[两层完整三阶核标量输入](../notes/2026-11-28-unit211-Phi-zero-original-twenty-two-third-kernel-scalar-and-exact-degree-8542.py)，18858 字节，blob
8900d78a5343f3882d8e2201e22e4b60ca0225bf，SHA256
e8c964ee3a74c9992fe4154c5c58965fa12516fc13e6537ec8864abdce51e85b。

唯一首次 run 46099323482、job 140837937313；源提交
1ec8876099039d93f57294cc91a23878cbf329ac。
实际 $10.546223899$ 秒、最大 RSS $67700$ KiB、内层退出码 $0$。
stdout 4776 字节，SHA256
bda33f8d181d269b71153a0137ab0cd3f9deb0f139328ae64559495233a597a5。

2026-11-28 02:41:56.049873 UTC 真实 pull 至
01e9394d6c31ef99a74bb821a9e3a2843813a0a6，两份 README 无变化。没有保存可重算系数或矩阵载荷，没有声称整个 Phi 或普通 ISP 已完成。

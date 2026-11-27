# 一般 Phi=0 的 H1 整曲线：六个非线性原极点排空与 804 权对覆盖

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 结论与范围

只在原 unit211 的 $\Phi=0$、物理 $D\ne0$ 图讨论整首项零曲线
$$
g(u,Q)=-12H_{6,4}(u,Q)=0,\qquad \deg_Qg=4,\quad g_4=1.
$$
[原极点支持](R150-appendix-unit211-Phi-zero-H1-original-Dixon-55-source-pole-support.md)已准确给出
$$
C_{256}
=(u-\tfrac32)(u-\tfrac{12}5)(u-\tfrac52)
H_3H_4H_5H_7H_8H_{25}P_{201}.
$$
所有因子均首一，整个 $C_{256}$ 平方自由。前三条整权纤维已由[三个一次极点排除](R150-appendix-unit211-Phi-zero-H1-three-linear-poles-complete-exclusion-and-1012-cover.md)关闭。

**本次定理。** 六个非线性整权纤维
$$
\boxed{H_3(u)H_4(u)H_5(u)H_7(u)H_8(u)H_{25}(u)=0}
\tag{1.1}
$$
全部没有原点，包含每个因子的全部复嵌入、原 $Q$ 根和原值 $\lambda,T,z$。
因此剩余原权点必须满足
$$
\boxed{P_{201}(u)=0,\qquad g(u,Q)=0.}
\tag{1.2}
$$
准确计数随之成为
$$
\boxed{\#\{\text{不同原权对 }(u,Q)\}\le 4\cdot201=804.}
\tag{1.3}
$$
这是权对数，不是全部原值点数。$P_{201}$ 的精确定义仍是前述首一商；本次没有计算其系数，也没有排除其零纤维。一般 H1、整 $\Phi=0$ 和普通 ISP 均未因此完成。本稿不移用到物理 $D=0$ 碰撞图。

## 2. 六个确切输入与特征零分支保留

六个 $H_d$ 使用前述 55 次支持定理的完整 $\mathbb Q$ 因式。前五个小多项式在该篇逐式列出；$H_{25}$ 是其唯一的 25 次首一因子。本次仅从同一原构造前缀取得 $C_{55}$，用
$$
H_{25}=
\frac{C_{55}}
{(u-\tfrac32)(u-\tfrac{12}5)(u-\tfrac52)H_3H_4H_5H_7H_8}
\tag{2.1}
$$
作短除并完整乘回；没有执行旧 Dixon Gaussian 或旧因式分解门。
$H_{25}$ 的原 713 字节系数定义 SHA-256 仍为
`98fe71762eb2c2d0fd5a4e5ed09066704be36b65ee2e81ae88aa8a9f7a56b4cc`。
这里只保定义与哈希，不保存或传输该可重算系数载荷。

对每个 $\phi=H_d$，先在整个
$$
K=\mathbb Q[u]/(\phi)
$$
内处理原首一 $g(Q)$。令
$$
\ell_n=Q-2(u-1)(u-2),\qquad m_n=uQ-\ell_n.
$$
下列都是当前原图中已支付单位的清分母形式：
$$
u,\ u-1,\ Q,\ 1-Q,\ \ell_n,\ m_n,\ -Q-4(u-1),
$$
$$
\ell_n(2u-\ell_n)-u^2Q,\quad Q+u-1,\quad
(\ell_n-Q)(1-Q)Q-2m_n^2.
\tag{2.2}
$$
其中分别包含 $\ell$、$u-\ell$、$T_0$、$bc$、已闭 $Q=1-u$ 以及[已闭 rho 二次首项零](R150-appendix-unit211-Phi-zero-rho-quadratic-head-zero-complete-original-exclusion.md)的清分母零支。仍须有原 $Q(1-Q)\ne0$；本源没有把模零分量直接删除。

对 (2.2) 逐个作真正的 $K[Q]$ 扩展 Euclid，并在有公因子时短除。每次都核验
$$
ag_{\rm current}+bU=h,\qquad
g_{\rm current}=h\,g_{\rm next},
$$
最终核验全部剥离因子与剩余因子的乘积恰为原 $g$，且剩余因子与每个 $U$ 有实际 Bézout $1$。所有系数逆也在完整 $K$ 中逐项乘回；没有选一个数值根代替整代数。

因此得到首一 $q_\phi(Q)$，并在特征零已经证明：每个合法原点都满足 $q_\phi=0$。准确分支如下：

| $\deg\phi$ | 原 $Q$ 次数 | 剩余 $Q$ 次数 | 特征零剥离来源 |
|---:|---:|---:|---|
| 3 | 4 | 3 | $1-Q=0$ 的一次公因子 |
| 4 | 4 | 3 | $Q=0$ 的一次公因子 |
| 5 | 4 | 3 | $bc=0$ 的一次公因子 |
| 7 | 4 | 4 | 没有剥离 |
| 8 | 4 | 4 | 没有剥离 |
| 25 | 4 | 4 | 没有剥离 |

这一步发生在选素数之前，故没有用模饱和替代特征零分支覆盖。

## 3. 整个有限自由整模型与真正单位

取
$$
p=1009,\qquad \mathcal O=\mathbb Z_{(p)}.
$$
本次六条输入的首一 $\phi$ 和 $q_\phi$ 的全部规范系数均实际为 $p$ 整。于是
$$
\mathcal A=\mathcal O[u,Q]/(\phi(u),q_\phi(Q))
\tag{3.1}
$$
在 $\mathcal O$ 上有限自由，秩为 $n=d\deg_Qq_\phi$，完整基为
$$
u^iQ^j,\qquad 0\le i<d,\quad 0\le j<\deg_Qq_\phi.
$$
这里不假设模 $p$ 约化是域、约化代数或无重根代数。

在完整 $\overline{\mathcal A}=\mathcal A/p\mathcal A$ 的正规表示中，程序依次验证：
(2.2) 的全部原权单位、所选原二次头的行列式以及下节固定六次原 cofactor 的首项都是单位。每次使用整个 $n\times n$ 乘法矩阵，返回其行列式非零、完整逆及矩阵乘逆等于单位阵，另核元素乘逆等于 $1$。

这些模单位确实支付特征零及 $\mathcal O$ 上的逆：
若 $a\in\mathcal A$ 的乘法矩阵模 $p$ 可逆，其行列式属于 $\mathcal O^\times$，故伴随矩阵公式给 $\mathcal O$ 上的真逆。它的模约化因唯一性恰是程序使用的逆。原权分母、三头逆和六次首项逆均因此在同一个整模型中合法，不需要先展开巨大的有理系数。

选素数只依据上述整性和完整单位条件，在任何共同根或原理想秩测试之前结束。六条实际输入均在固定列表的第一个素数 1009 合格，没有按后续理想返回换素数。

## 4. 两个同点原 cofactor 与准确六次头

使用[前篇](R150-appendix-unit211-Phi-zero-H1-three-linear-poles-complete-exclusion-and-1012-cover.md) §3–4 的同一个原定义：
$$
f=-P_c/P_f,\qquad z=Qt,
$$
以及完整四个二次式 $R,W,O,N_1$。它们均对 $(\lambda,T,z)$ 总次数不超过二；本源直接构造全部原式，不使用旧 Dixon 坐标的 $b_1^{-1}$ 或 $A_0^{-1}$。

六条输入均由原 $R,W,N_1$ 的 $(T^2,Tz,z^2)$ 三头给真首一规则。设 $v=(1,T,z)$，真实六个乘法列满足
$$
vM_T=T\,v,\qquad vM_z=z\,v.
\tag{4.1}
$$
原第四式 $O$ 的余列为 $r$，并令
$$
c_T=(M_TM_z-M_zM_T)e_T.
$$
每个原点的同一个非零行 $v$ 都杀掉
$$
r,\quad M_Tr,\quad M_zr,\quad c_T.
$$
因此两条固定三阶 cofactor
$$
F=\det[r,M_Tr,M_zr],\qquad
H=\det[r,M_Tr,c_T]
\tag{4.2}
$$
是同点必要条件 $F=H=0$。这里没有假设三生成模自由，也没有先假设两个乘法矩阵交换。

原总次数给出真正的特征零列次数界
$$
\deg_\lambda r_i\le(2,1,1)_i,\qquad
\deg_\lambda(M_Tr)_i,\deg_\lambda(M_zr)_i,
\deg_\lambda(c_T)_i\le(3,2,2)_i.
$$
所以
$$
\deg_\lambda F,\deg_\lambda H\le6.
\tag{4.3}
$$
此界来自原式及真实约化的次数，不是只观测模约化的次数。
六条实际 $F$ 的六次系数在整个 $\overline{\mathcal A}$ 中都是单位，§3 因而允许在 $\mathcal A$ 中把 $F$ 归一成首一六次式 $\widehat F$。

由此得到整个有限自由代数
$$
\mathcal B=\mathcal A[\lambda]/(\widehat F),\qquad
\operatorname{rank}_{\mathcal O}\mathcal B=6n.
\tag{4.4}
$$
全部 $\phi$、$Q$ 和 $\lambda$ 重数均在这个模型中保留。

## 5. 完整乘法矩阵返回及特征零排除

在基
$$
\lambda^kQ^ju^i,\qquad
0\le k<6,\quad 0\le j<\deg_Qq_\phi,\quad 0\le i<d
$$
上，本次计算 $H$ 的整个乘法矩阵，而非一个真空列或几个残域值。每列都由 $H\lambda^kQ^ju^i$ 按同一个首一 $\widehat F$ 约化得到；所有多项式除法均乘回。

六条输入的第一张原 $H$ 乘法矩阵就全部满秩。程序选取原矩阵列组成全阶方阵，并实际返回方阵乘完整逆为单位阵。准确结果是：

| $\deg\phi$ | $\operatorname{rank}\mathcal A$ | $\operatorname{rank}\mathcal B$ | 原 $H$ 乘法矩阵秩 |
|---:|---:|---:|---:|
| 3 | 9 | 54 | 54 |
| 4 | 12 | 72 | 72 |
| 5 | 15 | 90 | 90 |
| 7 | 28 | 168 | 168 |
| 8 | 32 | 192 | 192 |
| 25 | 100 | 600 | 600 |

相应 $\mathcal O$ 乘法矩阵的行列式是 $p$ 单位。因此 $H$ 已在整个 $\mathcal B$ 中为真单位；等价地存在
$$
A(\lambda)H(\lambda)+B(\lambda)\widehat F(\lambda)=1
\quad\text{于 }\mathcal A[\lambda].
\tag{5.1}
$$
(5.1) 不依赖选择某个复根或假设代数无幂零元。任意复原点若满足 $\phi=q_\phi=F=H=0$，代入 (5.1) 即得 $0=1$，矛盾。结合 §2 的全部已付零支，六个整 $\phi$ 纤维全部排除。

这是完整有限自由模型的特征零提升；它没有使用“一般多元模空便推出 QQ 空”的错误推理，也没有把未付范数或随机主元宣布为单位。

## 6. 唯一实际执行、小回执与返回覆盖

唯一源码：
[六非线性原纤维源](../notes/2026-11-28-unit211-Phi-zero-H1-six-nonlinear-source-poles-integral-original-fibers-8542.py)。

- Git blob：1254188e0d43d27c68b1557defbe3a2feb4a9ae4。
- SHA-256：877e4a078ded683c7db5488b101a09e0582a5831b0ffe7c05a69d6a89abdd4bf。
- 首次 run：46067201879；job：140735309768。
- 源提交：cc1846fc749262b990a611dac6949bb089b76630。
- 限额：120 秒、1 GiB。
- 实际进程：7.029657647 秒，最大 RSS 95904 KiB，退出码 0。
- stdout：27504 字节，SHA-256 b38cb87b15fe27dc6a0873b730ff8ff0d34e6f72b968a2b3ddb2a0686a97cc41。

最终数学事件在 6.962186990 秒给出六因子全部排除、付清总次数 52、剩余次数 201、权对上界 804。实际包含 37277 次 QQ 权系数约化回乘及 283 次 QQ 权与首一 $\lambda$ 多项式除法回乘。日志只记录矩阵身份、秩及哈希，没有传输矩阵或系数载荷。

20:58:50.716665 UTC 的真实 pull 前后均为上述源提交，两份 README blob 分别为 282e86b03385d3b6245ce7100ae2e2af7b103c2d 与 5fbd905291dd044c88d35bd9c07ac0e586ff795a，实际差异为空。

小回执：[执行及六整模型记录](../notes/2026-11-28-unit211-Phi-zero-H1-six-nonlinear-poles-complete-execution-8542.json)。

最后，将已证 (1.1) 从仍有效的 $C_{253}=H_3H_4H_5H_7H_8H_{25}P_{201}$ 必要覆盖中删去，得到 (1.2)。原 $Q$ 四次式的首一系数始终为 $1$，所以每个 $u$ 至多对应四个不同 $Q$，完成 (1.3)。下一未付输入是同一个 $P_{201}$ 上的真实原值返回。

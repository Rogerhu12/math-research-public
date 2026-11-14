# 原始 Cartan 行的共同核检查点

日期：2026-11-13。接 R182；不另登记主结果。

## 1. 一个精确的半单代数表述

固定同一实际剩余嵌入，取特征
$\ell\nmid p(p^2-1)$ 的代数闭域 k。
保留 R182 的 $\mathcal R_m$，并置

$$U_m=\bigcap_{c\in C}\ker(K_c\mathcal R_mK_c^{-1}).$$

这个空间被 C 保持。C 的非平凡特征空间均为一维，平凡空间为零，故

$$U_m=\bigoplus_{j\in I}\operatorname{im}\Pi_j$$

对某个准确的指标集合 I 成立。
对任一 C 特征直线 L，$\mathcal R_mL=0$ 当且仅当 $L\subset U_m$：
前向由 C 在 L 上标量作用，后向取 c=1。
所以本题目标准确包含

$$\{2m,4m\}\not\subset I,$$

或在二者都属于 I 时，证明旧常数行至少一条非零。
不能以 $\ker\mathcal R_m$ 的整体维数代替 I。

还有一个不需要调用 Burnside 的等价代数描述。
在 C 特征基中，令图的顶点为非平凡 C 特征，
当 $\Pi_i\mathcal R_m\Pi_j\ne0$ 时连接 i,j。
R182 的对称性和非退化 Gram 形式保证边是双向的。
由 C 生成的代数包含每个 $\Pi_j$；对每条非零边，
$\Pi_i\mathcal R_m\Pi_j$ 给非零矩阵单位。
沿路径相乘并在域 k 内除以非零系数，得到整个连通分量的全部矩阵单位。
因此由 C 与 $\mathcal R_m$ 生成的 k-代数准确为

$$\bigoplus_{\text{图的连通分量 }A}\operatorname{Mat}_{|A|}(k).$$

特别它确实半单；这里不是由一个形式的“伴随稳定”推半单。
由于原始投影没有对角项，I 恰为这个图的孤立顶点。
实际所需的结论是两个指定三次顶点不能同时孤立，而非证明整个图连通。
这仍是待证的非孤立性，并未被上述改写自动解决。

## 2. 复数 oscillator 输入的准确范围

Gurevich–Hadani–Sochen 的已发表原刊
*The finite harmonic oscillator and its associated sequences*,
PNAS 105 (2008), 9869–9873，首页 Eq.(1)，给非零 Weyl 位移的复 Hermitian
自相关上界 $2/\sqrt p$：

<https://people.math.wisc.edu/~sgurevich/PNAS-Version.full.pdf>。

本题 C 特征向量也是其非分裂 oscillator 向量；R177 对 C 的二次正规化
不改变特征向量。于是对于十二个不同位移，Gram 矩阵对角为 1，
每行非对角绝对值之和至多 $22/\sqrt p$。
在 $p>484$ 时 Gershgorin 给正定性，从而这十二个位移向量线性无关。
这可在特征零排除 R182 的 $R L=0$。

该证明严格使用复 Hermitian 正定性。它没有证明相关的整子式是好特征处
的单位，更没有证明固定剩余嵌入下的共同核结论。本文不把它降模使用。
R182 的真实坏方块已经说明整可逆性不能由一般复谱性质推得。

Malikiosis, *Spark deficient Gabor frames*, Pacific J. Math. 294 (2018),
起始页 159，Theorem 4.2（引用 Dang 等的条件）涉及特定 Clifford 阶整除维数，
不是本题 H 的阶整除 p+1 情形；一般 full-spark 结论也针对泛性的复向量。
原刊：<https://msp.org/pjm/2018/294-1/pjm-v294-n1-p08-p.pdf>。
未取得可直接替代上述固定特征问题的结论。

## 3. 连“特征大于 p 的 Fourier 全子式非零”也不成立

这是一个固定的小反例，不是新的素数窗口。
取 $p=41,\ell=83$。有

$$1+4+78=0\pmod{83},\qquad4=2^2,\quad78=24^2\pmod{83}.$$

$\mathbf F_{83}^\times$ 的平方子群阶为 41，所以 1、4、78 是三个不同的
41 次单位根。以它们为列参数，取 Fourier 行指数 0、1、3。
该 3×3 行列式是 Vandermonde 行列式乘以三个列参数的和，因此为零。
同时 $83>41$、$83\equiv1\pmod{41}$，且
$83\nmid41(41^2-1)$。

所以连实际 Tate 同余和好特征条件都不能把复数版 Chebotarev Fourier
子式定理直接搬到这里。此反例与 R177 在 p=41 的实际原始共同行结论
不冲突：它只否证一般 Fourier 子式替代论证，所取子式不是那两条
指定 Cartan 行。

## 4. 当前保留的方向

有希望但尚未完成的是用 Weyl 乘法证明上面图的两个指定顶点不能同时
孤立，或直接构造这些指定行与旧两行的整 Bézout 关系。
已排除的捷径包括：普通矩阵秩、单个旋转差块可逆、特征零相干界，
以及没有检查剩余特征的通用 Fourier 不确定性原则。
本检查点不宣称原始行问题已解决。

# R150：整个 h=k、b=c、Delta 非零原碰撞图的完整 QQ 排除

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted GPT-6 Astra Pro。

## 1. 结论

在原 unit 2+1+1 模型的 h=k≠1 值碰撞中，
$$
b=c,\qquad \Delta\ne0
$$
没有原物理临界点。

本定理合[96次原QQ覆盖](R150-appendix-unit211-equal-singleton-equal-weight-96-QQ-cover-and-four-fibers.md)与下文四个完整常数商中的真实原返回。两种 rho、所有复 lambda 根、所有 Q 首项退化均保持。物理 D=0；没有移用旧 D≠0 图的等权排除。

因此只能在 h=k、Delta非0 这个精确原域支付 u−ell。Delta=0 的等权面尚需单独处理，不能据此把 u−ell 宣成整个 h=k 图的单位。

## 2. 已付完整覆盖

父稿对同一原八行求四个固定结式及QQ Bézout，得到
$$
F_{96}=\operatorname{monic}
(\phi_{2a}\phi_{10}\phi_{2b}^{\,2}\phi_{20}^{\,4}).
$$
其中 phi2a=3lambda²−2lambda+1，phi2b=lambda²+lambda−1；phi10、phi20 的完整整数系数及全部原来源见父稿。本次同时保留每个整因子的所有复根，不取数值根或单一嵌入。

对每个 phi 取首一规范并在
$$
C_\phi=\mathbb Q[\lambda]/(\phi)
$$
中工作。所有系数逆都实际以 QQ[lambda] 的 xgcd 返回：
$$
s a+t\phi=1.
$$
所以该逆对整个常数商都有效。代码具有遇非单位后保留两个整因子的完整分支；本次实际141次系数逆全部成功，没有发生分支。结论不依赖未核验的不可约假设。

## 3. 同一原八行的整 Q Bézout

本次直接在各整个 C_phi[Q] 中重建父稿八个 primitive 原行
$$
C_{EBo},C_{N1},C_{E1},C_{EBe},C_{NBo},C_{NBe},C_{PBo},C_{PBe}.
$$
它们来自同一 H=bcDelta 缩放 Gram，全部清分母和原物理单位剥除仍保完整乘回。

对原行逐个作完整 Q 多项式 Euclid。每次 Q 除法都核对被除式=商×除式+余式；每个更新的标签都对全部原系数乘回。得到
$$
\sum_i a_i(Q)C_i(Q)=G_\phi(Q).
$$
没有仅验证数值秩，也没有只返回一个未提升的模素数单位。本次94次完整 Q 除法均实际成功。

实际结果为：

| 完整常数商 | 使用的原行 | 原QQ gcd | 原排除 |
|---|---|---|---|
| phi2a，次数2 | 全八行 | Q−1 | 原 rho²=1−Q 非零 |
| phi10，次数10 | 全八行 | Q−1 | 原 rho²=1−Q 非零 |
| phi2b，次数2 | EBo、N1 | 1 | 原组合直接为1 |
| phi20，次数20 | 全八行 | 首一 Q 二次 G20 | 两次只剥原 Delta 分子因子后为1 |

前两商的全部实际原点若存在，就必须 Q=1，与原不同配对 rho≠0 矛盾。第三商由两个原行直接矛盾。

在第四商，源码不是把某个新二次多项式擅自作为单位。它完整取得
$$
G_{20}=H_1H_2,
$$
并分别以精确 Q 除法核验 H1、H2 整除原 Delta 的分子。故每个实际 Delta≠0 点上，两因子都非零，而原行组合又要求 G20=0，矛盾。等价地，G20 整除该分子的平方；两次 gcd 循环不能未经检查简写为“整个 Delta 的平方”。

G20 的完整系数在附带凭据中按 Q 次数、再按 lambda 次数给出，1072字节，SHA256
c5c1fe42e2d08a7000a7014eff1a5f4084310583dc36c5c635708c34ff7b0acc。
所有系数在整20维QQ常数代数中准确处理；没有遗漏任何一个复根。

## 4. 为什么四支完整关闭原图

任意本范围内的原点，先由父稿满足 F96(lambda)=0，故 lambda 属于四个常数因子之一。对应的原方程、完整 Bézout 标签和真系数逆都可在该 lambda 处特化。

各商的结论分别迫已知非零的 1−Q、常数1 或 Delta 分子因子为零，与同一点原单位矛盾。Q 的首项在该 lambda 处退化也不影响整商中的恒等式。F96 中的重数无需冒充新的根；本结论是全部实际原点排除，不声称已给完整全局幂来源。

四支的真实原组合证书只保可再生源与小凭据：

| 常数因子次数 | 规范证书字节数 | SHA256 |
|---:|---:|---|
| 2a | 8310 | 8268c595da40914fb25689fc3c224437a6420a41af7bf2e30c4db259c922ecb7 |
| 10 | 75006 | e29b0e85d8a8030c4903572332319d312d0c391a5fbb9bb7953be1ed81e6538e |
| 2b | 2922 | 99cc0c7a8755cc7ffedc54a733d4ac8654de0722a6b2e0f6a03aff4ce89ceab6 |
| 20 | 144831 | 47454eb994ecee0773cbae1fd85fd0c4d5b1a72f5379bc9b483160a9188e09ff |

## 5. 唯一实际执行

[自含原QQ返回源](../notes/2026-11-27-unit211-equal-singleton-equal-weight-full-finite-QQ-return-8542.py)：
blob b84e0f539ae6f4f0c51ffe6673911c7cadf1809f，15699字节，
SHA256 f5e516e589210c84b0119cf80c249f5e7cc2500d34cb8db34c8dbc3a1f7e319f。

- run46005327745/job140526939140；内层 exit0。
- 源0.990940015秒，驱动1.055201296秒，最大子进程RSS45488KiB。
- stdout24186字节，SHA256 3c51e5b2e1f391462677533504c91adc963a1b381ef19304efbb61a879fc3e0c。
- source main b2f42ff88dbd9c40ba0308c95aa84833af7000ae。
- 13:14:11.620600 UTC 实际pull到 e7cda931ef3078d13f0ebe0f400566a8e0377fa5，两README无变化。
- 141次真常数逆、94次完整Q除法；四案全部返回，未发生常数非单位拆分。

[完整小凭据](../notes/2026-11-27-unit211-equal-singleton-equal-weight-Delta-nonzero-exclusion-receipt-8542.json)保全部原返回大小、最终gcd、原单位来源和执行身份。

下一输入直接使用 Delta=0 上两条原仿射约束的相容式，保留其所有系数退化；一般不等权图仍继续。普通ISP未完成。

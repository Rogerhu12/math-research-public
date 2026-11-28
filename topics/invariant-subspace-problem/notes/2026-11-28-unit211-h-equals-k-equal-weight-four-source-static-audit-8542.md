# 只读来源审计：h=k 等权前置链的两个 Delta 图

日期：2026-11-28（UTC）。
会话：Astra-ISP-8542378f-20261127。
性质：静态来源与既有实际回执核对；没有执行、重跑或提高任何计算门。
本记录不是新增数学排除，也不恢复旧错误 compact 链。

## 1. 更正并固定完整依赖

先前简短消息中“三源覆盖整支”的说法必须精确拆开：
8d6c 本身只给 $\Delta\ne0$ 的 F96 必要覆盖，
不是该支排空。完整前置链是以下四源：

| 功能 | source basename（notes 下） | Git blob | 完整 SHA256 |
| --- | --- | --- | --- |
| $\Delta=0$ 相容二十次覆盖 | 2026-11-27-unit211-equal-singleton-equal-weight-Delta-zero-original-compatibility-8542.py |6f3b6287c9de304c1207eeb97c499e7bd7a06d2c|05660258ea899a7efa008c2673a9f28141852029bbf15980a660758827fd632e|
| $\Delta\ne0$ 原 F96 覆盖 |2026-11-27-unit211-equal-singleton-equal-weight-original-Delta-nonzero-face-8542.py|8d6cb00f75b2110c5a42fffce19b43843c67a99c|ba8a23067ebd287bfcbe2e4f2eb08dfa423cafc72055f7481985b77dbcda3018|
| $\Delta\ne0$ 的四个完整常数域返回 |2026-11-27-unit211-equal-singleton-equal-weight-full-finite-QQ-return-8542.py|b84e0f539ae6f4f0c51ffe6673911c7cadf1809f|f5e516e589210c84b0119cf80c249f5e7cc2500d34cb8db34c8dbc3a1f7e319f|
| $\Delta=0$ 完整二十次域、原 Q 与自由 f 返回 |2026-11-27-unit211-equal-singleton-equal-weight-Delta-zero-full-original-QQ-return-8542.py|3f511c4e5de8f1a68787f8d5b570ef7bd728d695|c2d6165ae5cee89666674c048e2474014b0f99539b24660fe61bfc12156a5388|

本次已全文读完四份冻结源码和对应结果正文。
各自源码字节数依次为 10097、14146、15699、18701。

准确原文分别为：

- [Delta 零相容覆盖](../results/R150-appendix-unit211-equal-singleton-equal-weight-Delta-zero-original-compatibility-20-cover.md)；
- [Delta 非零 F96 原覆盖](../results/R150-appendix-unit211-equal-singleton-equal-weight-96-QQ-cover-and-four-fibers.md)；
- [Delta 非零四完整域排除](../results/R150-appendix-unit211-equal-singleton-equal-weight-Delta-nonzero-complete-exclusion.md)；
- [Delta 零补齐与整个等权碰撞](../results/R150-appendix-unit211-equal-singleton-equal-weight-Delta-zero-and-entire-collision-exclusion.md)。

## 2. 原 Gram 与单位链

准确输入为已经建立的 $h_U=k_U\ne1$ 矩参数图，
$$
A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
\quad \xi=B/A,\quad \ell=u=A^3/B^2,\quad T=A^2/B.
$$
这里 $b=c=\ell/2$ 是直接设定的整个等权面；
没有倒置待证的 $u-\ell$。

8d6c 和 f5e 在 $\Delta\ne0$ 图重建完整 $H=bc\Delta$ 缩放 Gram。
它们明写
$$
(vz)_1=v_0z_1+v_1z_0,\qquad
E_1=\cdots-2(d^2)_1=\cdots-4d_0d_1.
$$
原 $E_0,N_0,P_1,N_4(V)$ 与三个值矩、全部八个原行均同点构造。
N/P 的原 B、C 两行同时保留，借原 $\rho\ne0$ 才合法拆偶奇。
缩放后原 N/P 目标也完整带 $H^3$，不丢原最高值。

6f3b 只从准确原 P1 与完整 N4(V) 的两条仿射行推
$\Delta,F,T_{\rm num}$；它没有使用有问题的 mean1 紧凑公式。
3f51 对完整常数域恢复 Q，保自由 f，重建未缩放真 Gram，
其 mean1 同样正确。

四源未引用错误 compact $R_{\rm bad}$；
没有使用 $D\ne0$、旧不同值图等权结论、待证 $u-\ell$，
也没有使用后续 T0/JQ 排除作前提。
分母清理只用 $A,B,Q,1-Q$；
原物理支持为 $\lambda,bc,P_{02}$ 及独立 S0 先行排除所付 $S$。
$\Delta\ne0$ 图另外只用该图定义的 $\Delta$。
$\Delta=0$ 图不倒 $\Delta,T_0,P_f,\Phi$；
其解 t 所用 $bcQS\xi$ 来自已经支付的上述原支持。

这里仍须保原 $A,B$ 矩参数图、独立 $h=k=1$ 排除
及 S0 先行真实原证明的准确范围。
本次没有为这些先行条件添加新假设。

## 3. 四常数域的实际来源和首项退化

补齐的 f5e 源不再执行旧 F96 结式。
它自含重建同一原八式，在全部次数 2、10、2、20 常数商
$\mathbb Q[\lambda]/(\phi)$ 上作真实 $Q$ 扩展 Euclid。

每个常数逆先返回 QQ 一元 Bézout，再在常数商内乘回。
遇非单位时源码将 $\phi=g h$ 两个因子都递归保留；
实际运行没有发生此分裂。
$Q$ 行先完整专门化再 trim 实际首项，
每个实际首项逆都通过上述完整常数商检查；
所以没有丢某个复嵌入的头零纤维。

每次 Euclid 标签对全部已用原行完整乘回。
若所有原行在整域为零，源码明确给未排除状态；
不会因空矩阵冒称单位。
从最终原 gcd 剥因子时，源码既检查
该因子整除 gcd，也检查它整除同一点的原已付单位分子，
最后核全部因子乘回。

已读取既有准确小回执：
2026-11-27-unit211-equal-singleton-equal-weight-Delta-nonzero-exclusion-receipt-8542.json。
其 run46005327745/job140526939140 实际退出零，
驱动 1.055201296 秒、45488 KiB；
141 次常数真逆、94 次 Q 除法全部返回，无非单位分裂。

| 完整常数域次数 | 实际原 gcd 的 Q 次数 | 最后原排除 |
| ---: | ---: | --- |
| 2a |1|完整八行迫 $Q-1$，由原 $1-Q$ 支持排除|
| 10 |1|完整八行迫 $Q-1$，由原 $1-Q$ 支持排除|
| 2b |0|EBo 与 N1 两原行直接返回 1|
| 20 |2|完整八行的二次 gcd，两次只剥原 Delta 分子真因子后为常数|

第四域没有将一个未知二次当单位：两层均实际检查该因子整除原
$\Delta$ 分子，并在 $\Delta\ne0$ 图得矛盾。
“两层 gcd”不改写成未经核定的整个 $\Delta^2$ 因式身份。
原 F96 的重数 1、1、2、4 保留在必要覆盖中；
这里排的是全部实际复点，不声称已给全局幂零证书。

## 4. 两 Delta 图如何合并

6f3b 的固定相容结式给完整 $\phi_{20}$。
3f51 在整个相同常数代数中先把三原相容式返回为唯一 Q 一次，
再保自由 f，以 E1/EBe 原 Bézout 返回 1。
它不借 $\Delta\ne0$ 排除当作 $\Delta=0$ 上的单位。

8d6c 的 F96 与上述 f5e 全四域返回关闭整个 $\Delta\ne0$ 等权支。
所以两图的组合依赖四源及既有先行原范围，彼此不循环。
在再合独立 $h=k=1$ 排除后，可以恢复整个已限定 h=k 图中
$u-\ell\ne0$ 的已刊结论。

本审计不恢复任何旧错误第二曲线、848/578/七 lambda 覆盖，
也不替代 root 对 T0/JQ 四直接源码的独立审读。

# R779 — 原三坐标格 D≤4 的全部真实有理饱和旗标

日期：2026-11-15。**状态：本文所列四个有限格的精确计算及格算法已验证。**
只断言 D=1,2,3,4；没有由有限数据推出全 D 估值或原中央非零。

## 1. 原来源、前缀与要读的理想

保持 R760/R769 的固定 \(b=1\) 来源
\[
S=-t\Theta^{17}P_4,\qquad
T=-t\Theta^{36}P_4V_0,\qquad
U=-t^5(1-t)^3\Theta^{102}(34QP_4-6P_4-6tP_4')^6.
\]
这里 Q 的原递推为
\[
q_1=-2/5,\qquad (6j-1)q_j=(6j-4)q_{j-1},\qquad
[t^j]\log\Theta=-q_j/(3j).
\]
因此脚本直接重建每条原单项式，没有读取旧输出或另一个改动来源。

使用完整单项式整格
\[
E_D=\bigoplus_{a+b+\nu\le D}\mathbf Z\,S^aT^bU^\nu,\qquad
N_D=\binom{D+3}{3},
\]
和全部有理前缀的饱和整数核
\[
K_{D,k}=\ker_{\mathbf Q}(r_0,\ldots,r_{k-1})\cap E_D,
\qquad r_k=[t^k].
\]
对每个实际秩一跳跃，准确计算
\[
r_k(K_{D,k})=\iota_{D,k}\mathbf Z\subset\mathbf Q,
\qquad \iota_{D,k}>0.
\tag{1}
\]
约分后 \(\iota=A/B\)，所以原 p-adic 算子范数严格为
\[
\|\varphi_D^k\|_p=p^{-v_p(A/B)}.
\]
负赋值素数正是 B 的素因子。
R769 已证在这个同一原饱和核上，物理 w 行只差 \((-1)^k\)；
故 (1) 也准确读出原 w 旗标，不需要假设整个 t/w 换元矩阵在 p 处整。

## 2. 为什么所算的是整个饱和核

从 \(K_{D,0}\) 的单位整数基开始。
假设当前列矩阵 B 的列是整个 \(K_{D,k}\) 的整数基，
先把真实有理行 \(r_kB\) 乘一个公分母 L，得整数行 v。

若 v=0，当前层不跳跃，保整个 B。
否则用逐对扩展 gcd 的 unimodular 二乘二列变换，
把 v 严格变成
\[
(g,0,\ldots,0),\qquad g=\gcd(v_1,\ldots,v_d)>0.
\]
每一步使用
\[
\begin{pmatrix}u&-b/g\\v&a/g\end{pmatrix},
\qquad ua+vb=g,
\]
行列式恰为1。
因此下一行的整个像是 \((g/L)\mathbf Z\)，
删去第一列后恰得整个整数核；
没有取一个仅张成有理核的有限指数子格。

之后只对该列格的转置作整数行 HNF，保持同一行格，
再转回列。于是归纳保证每一步都在完整饱和核上进行。
脚本逐次检查新核杀当前原行，最后核秩为零。
计算过程从未将模 p 的核或一个缩放后的 Smith 块代入 (1)。

所有约分分母都被完整分解，余因子断言为1。
因此下表中的“最大惰性负赋值素数”覆盖全部素数，并非只在一个扫描清单中取最大值。

## 3. 四个完整有限结果

| D | 原来源秩 | 所有实际跳跃 k | 最大惰性负赋值素数 | 该素数首次跳跃 |
|---:|---:|---|---:|---:|
| 1 | 4 | 0,1,2,5 | 5 | 2 |
| 2 | 10 | 0,1,2,3,4,5,6,7,8,10 | 41 | 8 |
| 3 | 20 | 0至19，逐层一次 | 107 | 19 |
| 4 | 35 | 0至34，逐层一次 | 197 | 34 |

最后三列只是这四个原有限格的精确读数。
例如 D=4 的 p=197 在 k=34 的负赋值准确为 −1。
D=3 的 p=107 在 k=19 也准确为 −1。
它们不是任意挑选的 mod p 多项式，而是整个前缀饱和核行像的单位分母。

四个格均未出现 \(p\equiv1\pmod6,\ p\ne7\) 的负赋值；
这与 R760 的好普通全层上界相容。
固定分母素数3、7的费用仍保留。
数据不将这两个素数移出全局预算。

D=1 还可直接核定首个非整数行：
S、T 在 t 的首系数同为 −1，而
\[
[t^2](T-S)=-1118/15.
\]
第三个非恒定坐标 U 的首阶为5，系数为 \(-6^6\)。
这与上述四个跳跃及唯一惰性分母5一致。

每个完整有理像理想序列的 SHA256 为：

| D | 按 k 顺序的准确 \(\iota_{D,k}\) 序列 SHA256 |
|---:|---|
| 1 | 68cbf2922da1bba21129bf69b62e6555929cca6c0c5b16dfae39d9e5bf8ecd77 |
| 2 | fb8a51d14f7da327ba7fad796a1976693e0bc2ea61fc8a610782426e169a7551 |
| 3 | b764b39b45186f2dd7a0088e9a8b0eeb7dce3178643d9a7acba55d0220f9ed7a |
| 4 | 29ca95b49ae7cc98d7978ed6824d6f87f4e880234f57a4bcb615299c85b8b0ea |

完整输出还给每一跳跃的约分分母、分子 hash 和各素数层数；
不把这份可重算输出存入仓库或 Release。

## 4. 公开执行与复现

- producer：[check-r775-original-confluent-saturated-flags.py](../scripts/check-r775-original-confluent-saturated-flags.py)
- 参数：--degrees=1,2,3,4 --cap-factor=3 --workers=4。
- 依赖：python-flint 0.9.0。
- source commit：db822648d47be590644e9235ab41e84b62790afc。
- run：43728976368；job：132856999020；退出码0。
- producer SHA256：fc83fa7bf35f12ac4c13c469605564004b24cddabd2083eda79618254b4cf1c1。
- stdout：25256字节。
- stdout SHA256：f241a5325554226fb8e9de2494e9630b9b51caf51b27de2f96d9aadaf3847bb1。

有理幂级数使用原精确系数；没有浮点或数值近零判定。
所用 HNF 是整行格的规范形，参考
[python-flint 0.9.0 整矩阵文档](https://python-flint.readthedocs.io/en/latest/fmpz_mat.html)；
上述 gcd 归纳已经单独说明所需饱和性。

## 5. 此有限结果实际决定了什么

新三格的原有序层确实继续出现惰性负赋值。
R775 的抽象曲率单射或每个单项式的首共振，不能直接认成这些层的整性。
此次已经读取真正层，因而后续提出的估值必须与 (1)–(3) 相容。

尚未支付的是随 D 增长的统一估值及其同原中央失败的联系。
R760 的严格门仍是 \(a_I+3b_I<6\)；
表中有限值不证明该门，也不证明某个二次或三次 cutoff。
继续研究时，仍须在同一饱和整数核上保原全部列与 R770 的完整首提升修正。

依赖：[R760](R760-positive-derivative-three-coordinate-grid-and-full-slope-threshold.md)；
[R769](R769-original-confluent-theta-return-for-positive-derivative-grid.md)；
[R770](R770-actual-gaussian-connection-and-complete-first-lift-correction.md)；
[R775](R775-original-affine-inert-p-curvature-and-native-first-resonance.md)。

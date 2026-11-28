# 正确 Phi 的整个 ell-half：同 lambda 六维原模块、一次 z 返回与 114 次完整权覆盖

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（Asia/Taipei）。
- 状态：唯一首次实际完成；本篇登记原正目标及完整覆盖，**不登记整 ell-half 排空**。
- 原范围：当前已纠正的 $\Phi=0$、distinct-singleton、物理 $D\ne0$ 图。旧错误 compact E1 链不参与。

## 1. 结论

在整个

$$
\ell=\frac12,\qquad Q=4(u-1)(u-2)
\tag{1}
$$

上，本次实际得到一个非零纯 $u$ 多项式 $C$，满足

$$
\boxed{\quad C(u)^2z\in I_6,\qquad \deg C=114.\quad}
\tag{2}
$$

这里 $I_6$ 是由三个**真原均值**、真极化 $N_1$、完整 weighted NS、PS 组成的正确原必要理想，系数环只局部化原先已付的权单位。式 (2) 由完整原三坐标恒等式清分母得到，不是从函数域秩或模采样猜出的零集结论。

本图的 $Q$ 以及[正确整个 t-zero 排除](R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)给出的 $t$ 都已付，而 $z=Qt$。因此任何剩余物理原点必须满足

$$
C(u)=0.
\tag{3}
$$

每个 $u$ 在 (1) 中唯一确定 $Q$，所以本分支剩余的不同权对至多 **114 个**。这是权点的上界；这 114 个候选的整个 $\lambda,T,z$ 与原值纤维全部保留，不因此称完整原解集有限或为空。没有假定 $C$ 平方自由，也没有执行其 QQ 因式分解。

本次另实际得到原两个标量条件的首一 $\lambda$ gcd，次数为二；完整 $30$ 条原列在 $6$ 个固定坐标中秩为四。由正确呈示，这给 $\mathbb Q(u)$ 上未作物理 $z,D$ 局部化的原 $I_6$ 商维数二；它不是整个参数曲线上处处自由的二维代数，也不是两个物理解。

## 2. 整曲线的原范围与单位

记 $s=u-1$。正确 $\Phi$ 恒等式给

$$
\ell=1-\frac{2s(u-2)}Q,
$$

所以在原 $Q\ne0$ 图，(1) 是同一条整权曲线。其原参数为

$$
\begin{aligned}
\delta&=1-4s(u-2),& m&=u-\tfrac12,& M&=-2s^2,
&bc&=-\frac{s^2}{2\delta},\\
T_0&=-4s^2,&J&=-4s,&P_{02}&=4s^2(u-2),
&P_f&=16s^4,\\
A&=4s,&B&=16s^2(2s^2-3),&L&=2s(u-2).
\end{aligned}
\tag{4}
$$

同一点原恢复为

$$
f=\frac u2-(u-2)(\lambda-\tfrac12)
-\frac{(u-2)^2}{s}(T+\tfrac12),\qquad t=z/Q.
\tag{5}
$$

三真均值的已付头专门化为

$$
\det H_{012}
=-\frac{1024s^{10}(u-2)^7(2s^2-3)}{\delta^4}.
\tag{6}
$$

式 (6) 的单位性来自完整正确 $A=0,B=0$ 排除及原 $Q,\delta,s,M$，不来自被撤回的旧 first-head 结论。$u$ 引用[独立原零基均值排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)；$m$ 引用[完整原等权排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)在当前正确 Phi 图的静态范围核对。一个可取的旧权局部化支持为

$$
U(u)=u(u-1)(u-2)\delta(2u-1)\bigl(2(u-1)^2-3\bigr).
\tag{7}
$$

本篇所有“旧已付系数环”均指相应支持的局部化；没有倒置 $\theta$、$\ell-\tfrac12$ 或新纯 $u$ 因子。

原值判别式仍为

$$
D=\ell A_2-T^2=bc(h-k)^2,\qquad A_2=2\lambda^2-2\lambda+1.
\tag{8}
$$

源预定允许测试正 $D$ 幂，但本次已先返回正 $z$ 一次，实际没有进入 $D$ 正幂序列。任何已知 $D=0$ bipartite 双数边界都没有被当作物理解或代替本次计算。

## 3. 专门化后的两个原标量与完整 gcd 来源

本次只复用[正确原十五列呈示](R150-appendix-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-and-two-sextics.md)的必要定义。先在正确四原式源码中定义自由符号，随即施加 (1)，然后才构造 $R,W,O,N_1$ 以及原 Gram。没有先展开一般权两 C6，更没有重放其旧证明门。

设 $v=(1,T,z)^{\mathsf t}$，三坐标种子为

$$
G=(r_{N_1},r_{NS},r_{PS},c_1,c_2).
$$

在整 (1) 上，由 $(N_1,NS,PS)$ 与 $(N_1,c_1,c_2)$ 的两个原三列 cofactor，分别完整清回三个实际乘子，得到 $C_0e_0,C_1e_0$ 的原来源。共同取消只发生在三个实际乘子上，并逐三坐标返回；整个共同零面保留。

实际参数为：

| 对象 | $u$ 次数 | $\lambda$ 次数 | 总次数 | 项数 | SHA256 |
|---|---:|---:|---:|---:|---|
| $C_0$ | 31 | 6 | 36 | 221 | 483a3334d2e0b048f4a55bbd9fbbf09bc859ab700885d40cfabd1a7383e05162 |
| $C_1$ | 25 | 6 | 31 | 182 | d02752ae5022541e8f69b49d46580dd44e305747f2833168f2033823f3187532 |
| 首一 $g$ | 0 | 2 | 2 | 3 | adf7bee40d6805fa6746553993b7881ddbcd7d2b571a8926e6a3171de8eda3d7 |

这里的 $g$ 在 $\mathbb Q(u)[\lambda]$ 中由完整 Euclid 来源

$$
g=aC_0+bC_1
\tag{9}
$$

实际形成。每个短除法都返回完整乘积；(9) 再复合回五个原种子，给

$$
ge_0=\sum_{j=1}^5\eta_jG_j
\tag{10}
$$

的三个完整坐标。原 $\lambda$ 重数全部保留。$g$ 的参数由冻结源码和表中规范 SHA 唯一定义；本篇不借预期边界形状替换这条真实返回。

这些实际五源乘子的纯 $u$ 分母 LCM 次数为 106、107 项，SHA256 为 de816538404add6f7b8e0036fa03f14e2d083053b0db1a93e5f8a9e788953d15。其零纤维没有被删除。即使 $g$ 本身的系数不含 $u$，(10) 的这些原来源极点也不能省去。

## 4. 完整原有限坐标和一次 z 目标

正确三生成呈示给

$$
I_6\longleftrightarrow
\langle G,M_TG,M_zG\rangle_{\mathbb Q(u)[\lambda]}
\subset \mathbb Q(u)[\lambda]^3.
\tag{11}
$$

(10) 与同一个 $M_T,M_z$ 的作用还给 $ge_T,ge_z$ 的原来源，故可在 $g$ 首一二次的完整环境中工作。取固定六坐标

$$
(e_0,\lambda e_0,e_T,\lambda e_T,e_z,\lambda e_z).
\tag{12}
$$

对 (11) 全十五条原列各取一次及 $\lambda$ 倍，共 30 列。逐列除 $g$，所有商、余式以及完整三坐标均返回；没有删掉任何 $\lambda$ 重数或原 overlap。

本次矩阵实际秩为四，四条保留的消元列均回原 30 列，返回 24 个坐标。然后预定的第一个正目标 $z$ 就得零余式。终端只用其中四条原列，并实际返回全部六个固定坐标。源码继续把这个有限组合提升回三条**完整 $\lambda$ 多项式**恒等式：

$$
e_z-\sum_j\gamma_j\lambda^{a_j}r_j
=g\sum_{i=0}^2q_i e_i.
\tag{13}
$$

这三个多项式商全部完整回乘。矩阵秩仅用于选择和构造原组合，结论依据的是 (10)、(13)，不是“秩高所以原点为空”。

这是本次第一个实际正目标，不需要原 $z^{-1}$ 或 $D^{-1}$；实际没有试更高正 $z$ 次数，也没有进入预定的正 $D$ 分支。

## 5. 完整清分母及 114 次覆盖

令 $\Gamma$ 为冻结源对以下实际有理系数分母取的完整 LCM：$g$ 的系数、(10) 的五源乘子、30 个输入列短除、正目标动作余式及 $g$ 商、终端四个 $\gamma_j$ 以及 (13) 的三个 $q_i$。

程序实际核每个分母整除 $\Gamma$。得到

$$
\deg\Gamma=138,\qquad
\Gamma\text{ 有 }139\text{ 项},
\tag{14}
$$

规范 SHA256 为 01bc0236821b0b66a1bbac8a57d9095fb4a8fc4ec916dbc149db4b2e85fe23f0。

由 (10)，$\Gamma g$ 有原 $I_6$ 来源。再由 (13)，每个 $\gamma_j,q_i$ 至多各需要一份最终 $\Gamma$，所以

$$
\Gamma^2z\in I_6.
\tag{15}
$$

一般正目标动作的旧规则误差也只使用旧已付权逆，加上已返回的 $g$ 商，故同一 $\Gamma^2$ 归纳有效；本次实际为第一步 $z$，其原坐标本来就是 $e_z$。

只从 $\Gamma$ 剥去 (7) 的原已付支持，并作非零有理常数规范化，得本篇的 $C$：

$$
\deg C=114,\qquad C\text{ 有 }115\text{ 项},
\qquad
\operatorname{SHA256}(C)
=\texttt{9d0dac7a7b80c570233f4e08388c6d57b343fb2e674bb7ed7308702f7b52a33f}.
\tag{16}
$$

源码核完整 $\Gamma=(\text{旧单位})C$，由 (15) 得 (2)。共保留 60 个不同实际分母；所有未知纯 $u$ 头、内容和最终极点的整零纤维仍在 $C=0$。

$C$ 是程序中最终实际 LCM 的精确定义，不是“取若干坏点”的经验清单；无需保存 115 项系数载荷即可由同一冻结源唯一再生。后继若约消终端原乘子，必须给新的完整原来源，不能因为 LCM 过大而无证删除它的任何因子。

(2) 没有把 $z$ 当代数单位后宣称裸 $I_6$ 为单位理想。只在原物理 $z=Qt\ne0$ 范围内，才推出 (3)。因此当前确证的是完整纯权必要覆盖及至多 114 个不同权对，仍不是整 ell-half 或整 Phi 排空。

## 6. 唯一实际记录

唯一数学 run 为 [46139964727](https://github.com/Rogerhu12/math-research-public/actions/runs/46139964727)，job 140963509239：

- 源/pull：65b8726890b5f7cd6c0cbf3abc6817eae7c9dac6；实际规则读取时间 2026-11-28T11:27:37.457458+00:00，两份 README 未变。
- 源 Git blob：bcb71ff5af8cc5634c18887e1ca00a0524e66d18；SHA256 bd14e7724b688d596d51207ac859143321a7526407b9c702a3641dbeb1d957b4，19640 字节。
- [首次输入说明](../notes/2026-11-28-unit211-Phi-zero-corrected-entire-ell-half-original-positive-targets-8542-input.md)：blob 9771b53c6e2fff72901650df728c4788995f80ce。
- [小执行回执](../notes/2026-11-28-unit211-Phi-zero-corrected-entire-ell-half-original-positive-targets-8542-execution.json)：blob 8443bdd3d1686c3196a980d7c63a039563c0f372。
- 数学程序 0.864349696 秒；driver 0.908464339 秒；driver 子进程峰值 RSS 44604 KiB；退出码 0。
- stdout 5114 字节，SHA256 9d3138af168dafca7a5ce0eba042468bacfd2dd84047460e15743c8d082c68a8。
- 实际完整返回计数：新 cofactor 6 坐标，gcd 原来源 3 坐标，输入除法 90 坐标，保留矩阵列 24 坐标，目标动作 3 坐标，目标张成 6 坐标，最终完整多项式 3 坐标，101 个 $\lambda$ 短除乘回。

没有扩大预算、重派数学门、保存系数缓存或分片。旧全图 C6、固定十二阶及十五列证明门均未重放。本篇不识别或删除 $C$ 的任何未付因子，不恢复旧撤回链，也不宣称普通不变子空间问题已解决。

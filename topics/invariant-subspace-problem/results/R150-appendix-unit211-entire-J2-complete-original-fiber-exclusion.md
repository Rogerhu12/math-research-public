# h=k：整个J2二次λ原纤维完整排除

数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


日期：2026-11-28（Asia/Taipei）。会话Astra-ISP-8542378f-20261127。

## 1. 整纤维定理

在当前一般LS的碰撞 $h=k$、Delta非零原物理域中，
$$
J_2(\lambda)=3\lambda^2-2\lambda+1=0
$$
没有原解。两个复λ嵌入、全部u与Q、全部原首项零纤维均包含在本定理中。

[前一完整原覆盖](R150-appendix-unit211-entire-J2-original-norm-cross-three-u-factor-cover.md)已将所有原u限制到 $F_{28}F_{23}F_6=0$，并支付原O对Q的四次首项。本次分别在这三个**整个**常数代数上返回原方程：

| u因子 | 完整QQ环境维数 | 实际原返回 |
|---|---:|---|
| F28 | 224 | 原R的完整乘法矩阵可逆 |
| F23 | 184 | 原R的完整乘法矩阵可逆 |
| F6 | 48 | 真正QQ原行组合恰为物理Delta² |

因此[两QQ投影总覆盖](R150-appendix-unit211-equal-singleton-two-original-QQ-projections-common-curves-and-finite-base-remainder.md)中可以合法删除整个J2分支。余下仍是 $P_{25,3}=0$ 的整曲线，或两条剩余不可约曲线的有限交点；它们的全部实际Q纤维继续保留。整个h=k、unit211及普通Hilbert ISP仍未闭。

## 2. 完整原常数环境

读取前一结果固定的八个准确原λ系数及三个u因子，不重算范数、交叉式或130次QQ投影。每行只乘一个非零有理常数，所有系数实际乘回。

对于 $d=28,23,6$，置
$$
C_d=\mathbb Q[u,\lambda]/(F_d(u),\lambda^2-\tfrac23\lambda+\tfrac13).
$$
F_d先准确规范为首一。两λ系数按同一个关系相乘：
$$
(a+b\lambda)(c+d\lambda)=
ac-\tfrac13bd+
(ad+bc+\tfrac23bd)\lambda.
$$
每个u余式都通过首一F_d整除并实际核对商乘回。没有把张量常数代数预设为域，也没有挑选某个复根。

对于一个待逆元 $a+b\lambda$，实际使用
$$
N=a^2+\tfrac23ab+\tfrac13b^2,\qquad
(a+b\lambda)^{-1}=
N^{-1}(a+\tfrac23b-b\lambda).
$$
N与**整个**F_d的QQ Bézout必须为1，随后还核对两个λ系数的逆乘积。不能只凭某个嵌入非零就除以它。

原O的Q四次头在三个C_d中均通过上述实际完整逆。令 $\widehat R_O(Q)$ 为该首一原四次式。得到连续首一环境
$$
\mathcal A_d=C_d[Q]/(\widehat R_O),\qquad
\dim_{\mathbb Q}\mathcal A_d=2d\cdot4.
$$
原O、R、W、N1的每次Q除法都完整乘回，原O余式准确为零。其余三行仍是同一个λ、u、Q处的原条件。

取明确基
$$
Q^j\lambda^l u^i,\qquad
0\le j<4,\quad0\le l<2,\quad0\le i<d.
$$
将原R、W、N1分别乘以所有基单项式，得到固定QQ矩阵 $M_d$，行数分别672、552、144，列数分别224、184、48。每一行都有明确原理想来源，未以任意必要投影取代原方程。

## 3. F28和F23的完整原单位

两矩阵全部有理系数在1009处可积，原首一常数关系同样可积。实际取模后的秩分别224、184。选中的方阵恰是原R的全部基单项式乘积；并非从其它行拼出一个不明确来源的矩阵。

源码对两个选定方阵都实际构造逆并核对**两侧**乘积等于完整单位阵。因此相应固定QQ乘法矩阵的行列式非零，原R在整个 $\mathcal A_{28}$、$\mathcal A_{23}$ 中可逆，却必须在任何原解上为零，矛盾。

两个完整逆的规范编码分别196109、132445字节，只保准确SHA和可再生固定源：

- 224阶：7dc661a0f0b29edffd3331901a2a0b531322878c09f568e121070bc816fa0166；
- 184阶：82acf3720e99243ee64a5f90aa155a5cdbf5dee98c475fc1315b3c7ce5e98c9d。

这一步是固定QQ矩阵非零行列式的提升，不是把多变量模数空性当作QQ结论；常数代数的所有分量和嵌入同时保留。

## 4. F6上真正QQ的Delta²原返回

F6的模矩阵只有36秩，列数48。本次没有把这个模秩亏解释成QQ秩亏，更没有凭它判空或认定原解存在。

在原已付J2域中，原量准确为
$$
\begin{gathered}
\ell=\tfrac12,\quad \xi=1-\lambda,\quad
S=5-4\lambda,\quad \eta=4-3\lambda,\\
T_0=2u-\tfrac Q2-2u^2,\quad
J=T_0+Q,\quad
\Phi=T_0+4u-4+Q,\\
N_F=(3-4\lambda)Q+J\xi\eta,\qquad
\Delta=\Phi N_F-S\xi T_0^2.
\end{gathered}
$$
这就是同P1/NV恢复公式中的原Delta；$P_f=T_0(J-Q)=T_0^2$，没有另造一个同名几何量。当前整个Delta零原分支已在此前独立排空，因此真实原点必须 $\Delta\ne0$。

从模消元选出的36条真实原行组成QQ矩阵B。再选一个在1009处行列式非零的36阶列子矩阵C，实际求完整QQ逆并核对两侧乘积为I。对于目标t，用
$$
\alpha=t_{\text{所选列}}C^{-1}
$$
构造候选原行组合，然后直接对**全部48列**核对 $\alpha B=t$。

Delta的一次目标没有从这个选定原行组返回；这只是该次具体返回失败，不宣称Delta不属于完整原理想。随后新的二次目标实际成功：
$$
\boxed{\alpha B=[\Delta^2]_{\mathcal A_6}.}
$$
所以
$$
\Delta^2\in
(R_R,R_W,R_{N1},\widehat R_O,F_6,J_2)
$$
于已述精确原局部环中。任意复原点必须Delta²为零，与Delta非零矛盾。

全部36个准确QQ组合系数与相应原基单项式标签保存在小回执中；规范编码14155字节，SHA256
f9b9a67e2ec059cb25ae56d9699356b4df87511b34e7ff868fd02fc1329bc5e7。
原48列全乘回已经实际完成；没有提升模数下的Delta成员关系。

## 5. 唯一新执行和来源

[原有限环境源](../notes/2026-11-28-unit211-J2-three-entire-u-factors-original-Q-four-return-8542.py)，SHA256
a2a43175c69b549d12577b398816dc2e6710f2a1a57bf622eae80f8c49377986。

输入仍是前一结果的
[原λ系数及三u因子](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-28-unit211-J2-original-pairs-and-three-u-factors-exact-input-8542.json)，SHA256
e1b9c53c299df8c6725067444c7c6838c1b1573157bc8271c7037234bd112e0f。

实际run46042404545/job140653180288，内层0，墙钟0.855451933秒，RSS85760KiB，数学完整返回0.798722465秒。stdout38191字节，SHA256 1a2157a6c70a2419c83f931333db7f326f26605ff99d610a0b16471af1b82b3d。

实际pull于2026-11-27 17:30:55.079874 UTC，从bbd6a1929d5b1126755014b48ec45c5b0859fc9b更新至73b5e1963b00e0977aa11547dd8dc44ed9b79a01，两README无差异。固定源身份保持不变。

[完整小回执](../notes/2026-11-28-unit211-J2-entire-original-fiber-exclusion-receipt-8542.json)保原实际阶段、两模逆SHA、Delta一次未返和二次完整QQ证书。三因子全闭后接原 $P_{25,3}$ 曲线及剩余有限交点，不复跑已闭J2。

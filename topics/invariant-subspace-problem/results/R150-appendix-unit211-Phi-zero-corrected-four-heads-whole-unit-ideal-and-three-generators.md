# R150 补充：更正后四个原二次头的全局单位理想与三生成元

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 结论与原始范围

本证明只使用[更正后四个原二次头](R150-appendix-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads.md)，不恢复已撤回的旧 $\bar R$、first-head、H1、H42 或矩阵有限性链。

在真正的 $\Phi=0$ 原图上，假设
$$
Q(1-Q)P_f\ne0,\qquad P_{02}\ne0,\qquad bc\ne0.
\tag{1}
$$
置
$$
K=Q+4(u-1),\quad L=Q-2(u-1)(u-2),\quad
M_n=2uL-L^2-u^2Q,
$$
$$
U=Q(1-Q)(u-1)KLM_n.
\tag{2}
$$
原身份
$$
P_f=4(u-1)^2K,\quad P_{02}=2(u-1)L,\quad
M_n=4bcQ(1-Q)
\tag{3}
$$
准确支付 $U\ne0$；没有额外假设 $u\ne0$、$u-\ell\ne0$、$u+Q-1\ne0$ 或某个二次头非零。

**更正后的四行二次头在整个 (1) 上秩为三。更强地，它们的四个极大子式在**
$$
\mathcal R=\mathbb Q[u,Q,U^{-1}]
$$
**中生成单位理想。** 因而四个完整原二次式的商，在 $\mathcal R[\lambda]$ 上由
$$
1,\quad T,\quad z
\tag{4}
$$
生成。这是全图的实际原理想结论，不只是在一个预先选择的头开集上成立；不宣称该模自由，不宣称 $\lambda$ 有界次数、整个 $\Phi$ 无解或普通 ISP 完成。

## 2. 四个子式的准确原输入

令
$$
A=4(u-1)^2-Q,\qquad
B=-Q^2+(12u^2-20u+8)Q-16(u-1)^2.
\tag{5}
$$
更正后四行依次为真正 $\bar R$、原加权均值 $W_4$、原均值差 $\bar O$、原极化 $N_1$。取其 $T^2,Tz,z^2$ 系数为 $4\times3$ 矩阵 $H$。前一结果完整返回
$$
\det H_{012}=\frac{ABM_n^3L^4}{8K^3(1-Q)^4},
\qquad
\det H_{013}=\frac{QF_8M_n^2L^3}{8K^2(1-Q)^3},
$$
$$
\det H_{023}=-\frac{(u-1)F_{10}M_n^2L^3}{8K^3(1-Q)^4},
\qquad
\det H_{123}=\frac{F_9M_n^3L^4}{4QK^3(1-Q)^4}.
\tag{6}
$$
$F_8,F_{10},F_9$ 是该已成结果中固定的三个小多项式；本次新自含源码保留其明确可读公式，未重算四头。其完整有理系数定义的 SHA256 分别为：

- $F_8$：e12cf1bbaf864cd9de2a01b033b2dce98ee6dda20b595d499f39f3c431a3682c；
- $F_{10}$：fed662807af51d32a487e94de918bb79fec0a93775775351f1d2c59ac95d569b；
- $F_9$：75f45c262d856751b610ef4bb16502555d9e2f9e800d08c9d37769c67beb9c10。

因此准确问题是在 $U\ne0$ 上排除
$$
AB=F_8=F_{10}=F_9=0.
\tag{7}
$$
不能以四个子式的多项式 gcd 为常数替代 (7)。

## 3. 整个 A 分支：真正三项 Bézout

在 $A=0$ 上代入 $Q=4(u-1)^2$。三个原 $F_i$ 的代入次数分别为 $8,12,11$。本次完整 $\mathbb Q[u]$ 欧氏返回给出
$$
g_A=\frac14u^3(2u-3)^2(u-1)^3
   =a_8F_8(u,4(u-1)^2)
    +a_{10}F_{10}(u,4(u-1)^2)
    +a_9F_9(u,4(u-1)^2).
\tag{8}
$$
每个代入余式和原式的差均实际除 $A$ 后完整乘回。真正 $U_A=U(u,4(u-1)^2)$ 次数为十三；一次真实 gcd 就移去整个 $g_A$，余式为 $1$，并完整返回
$$
g_A\mid U_A.
\tag{9}
$$
所以在原二元多项式环中
$$
U\in(A,F_8,F_{10},F_9).
\tag{10}
$$
这排除四头共同零集的整个 $A$ 分支，不是宣称原图中 $A$ 本身是单位。

## 4. 整个 B 分支：保全部幂零的二十六维原目标

写
$$
B_0=-B=Q^2-c(u)Q+d(u),\quad
c=12u^2-20u+8,\quad d=16(u-1)^2.
$$
三项完整短除法给出
$$
F_i=B_0q_i+a_i(u)Q+b_i(u).
\tag{11}
$$
保留其全部二次权代数，不倒任何 $a_i,b_i$ 或范数。由原式直接得到六条必要身份：
$$
b_i^2+c\,a_ib_i+d\,a_i^2
=(a_iQ+b_i)(a_i(c-Q)+b_i)+a_i^2B_0,
$$
$$
a_i b_j-a_j b_i
=a_i(a_jQ+b_j)-a_j(a_iQ+b_i).
\tag{12}
$$
本次六条身份及其完整 $\mathbb Q[u]$ Bézout 返回给出
$$
g_B=\frac1{16}u^3(2u-3)^4(u-1)^6
\in(B_0,F_8,F_{10},F_9).
\tag{13}
$$
$g_B$ 首一十三次，$B_0$ 对 $Q$ 首一二次。因此
$$
\mathcal A=\mathbb Q[u,Q]/(g_B,B_0)
\tag{14}
$$
有完整二十六维基 $u^iQ^j$，其中 $0\le i<13$、$0\le j<2$。保留 $u^3$、$(2u-3)^4$、$(u-1)^6$ 的全部重数，没有只看约化点。

三条原行 (11) 乘全部二十六个基元素，得到真实 $26\times78$ 原理想矩阵。实际秩为 **13**，不是 26；剩余商的 $\mathbb Q$ 维数为 13。本次用真实原列
$$
0,1,\ldots,9,\quad13,\quad14,\quad15
$$
和常数有理数子式解出并完整乘回的目标是
$$
U^{26}\in(F_8,F_{10},F_9)\mathcal A.
\tag{15}
$$
整个目标列的二十六个坐标全部返回，只有有理数常数被倒置。由 (13)，(15) 回到原多项式环即
$$
U^{26}\in(B,F_8,F_{10},F_9).
\tag{16}
$$
该分支在 $U\ne0$ 上为空；没有将原有限矩阵的非满秩解释成无解，没有把 $B$ 本身当单位。

## 5. 真实全局拼合与原三生成元

由 (10)、(16) 相乘，
$$
U^{27}\in(A,F_8,F_{10},F_9)(B,F_8,F_{10},F_9)
\subset(AB,F_8,F_{10},F_9).
\tag{17}
$$
故 (7) 的理想在 $\mathcal R$ 中等于整个环。式 (6) 的全部比例因子均为 $\mathcal R$ 的单位，四个极大子式也生成单位理想。选取其实际多项式理想来源得到
$$
\sum_S\gamma_S\det(H_S)=1,\qquad\gamma_S\in\mathcal R.
$$
若 $P_S$ 从四行选择 $S$ 三行，则
$$
L_H=\sum_S\gamma_S\operatorname{adj}(H_S)P_S,
\qquad L_HH=I_3.
\tag{18}
$$
这是有限矩阵的伴随恒等式，没有倒置未经支付的头，也没有假定某个单独 $H_S$ 在全图可逆。

把四个完整原二次式写为
$$
q=H\begin{pmatrix}T^2\\Tz\\z^2\end{pmatrix}
  +J(\lambda)\begin{pmatrix}1\\T\\z\end{pmatrix}.
$$
左乘 (18) 后，
$$
\begin{pmatrix}T^2\\Tz\\z^2\end{pmatrix}
=-L_HJ(\lambda)\begin{pmatrix}1\\T\\z\end{pmatrix}
\pmod{(q_0,q_1,q_2,q_3)}.
\tag{19}
$$
每次替换把 $T,z$ 总次数至少降低一，所以得到 (4)。原四行、其相容关系和所有后续原值式仍保留。只有生成性得到支付；无自由性、唯一正规形或 $\lambda$ 首一关系的附加断言。

原四式的 $(\lambda,T,z)$ 总次数至多二，$L_H$ 又只依赖权；故 (19) 常数项对 $\lambda$ 至多二次，两个一次坐标的系数至多一次。这也不产生任何新的 $\lambda$ 有界性。

## 6. 唯一新执行与范围

自含源：
[2026-11-28-unit211-Phi-zero-corrected-four-heads-whole-common-zero-original-return-8542.py](../notes/2026-11-28-unit211-Phi-zero-corrected-four-heads-whole-common-zero-original-return-8542.py)。

- Git blob：2e03c17a58b54fb8fa9a39b4f3ebf366b8648d60。
- SHA256：52fd79c92f3baca890d026184e687db573a10a6e896c8a3310d900a9433e4f75。
- 唯一 Actions run 46107738528，job 140864183090。
- 实际 0.077265790 秒、38000 KiB、内部 exit 0。
- 完整精确除法返回 7 次，完整一元 Bézout 返回 11 条。
- stdout 3224 字节，SHA256 632d5ed7d3207979c1cca2e667083234cf61c361254ce85662196c2eddc2103a。
- 源提交 0f981c7044f02f45ad750451da8f3df0944031db；实际 pull 676d4ab94af01f74f84ea6ca98a3f130e93077e6，2026-11-28 04:29:16.980312 UTC，两 README 无变化。

[小执行回执](../notes/2026-11-28-unit211-Phi-zero-corrected-four-heads-whole-common-zero-original-return-execution-8542.json)保留实际矩阵秩、幂零范围、目标和运行身份。没有重新执行四头计算，没有恢复旧错误体系的任何下游结论。当前只支付更正后原四头的全局覆盖和真正三生成元；真实原值条件及整个 $\Phi$ 仍须继续。

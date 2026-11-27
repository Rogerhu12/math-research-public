# 一对等权、四独立权：原 S1 后五个主子式的唯一新输入

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

状态：本稿给原剩余五个主子式的准确同源计算映射；
这些新正性尚待首次实际返回，不宣布完整 S1。

源：
[原剩余五主子式](2026-11-28-one-pair-four-independent-s1-remaining-five-original-minors-8542.py)，
Git blob 29ce9cce1a6a1f0e0312a8b9d4c919251093eebb。
内层固定 180 秒、4 GiB。只输出小的普通摘要，
不输出可重算多项式、矩阵、编码数据或参数文件。

## 1. 已付首项及唯一新目标

保持
[原完整来源](2026-11-28-one-pair-four-independent-original-s1-8542.md)
的全部物理度量及
$$
\mathcal E=
\widehat H U_0^{-1}\widehat H-\widehat F_2
-(K_B^{\mathsf t}\Lambda_2K_B)U_0^{-1}
 (K_B^{\mathsf t}\Lambda_2K_B)
+2K_B^{\mathsf t}\Lambda_2\Lambda_3^{-1}\Lambda_2K_B
+\frac{K_Y^{\mathsf t}K_Y}{4e_4}.
\tag{1}
$$
其中原物理层是 $11,5$ 维，上、下固定来源是 $6,4$ 维。
$U_0^{-1}$ 仍为完整六维度量逆；
$\Lambda_2,\Lambda_3$ 先由整个五维物理 Gram 取逆后压缩；
所有实际逆均由有理消元并实际乘回。

记 $\Delta_k$ 为 (1) 的第 $k$ 个原领先主子式。
[首原子式全正域定理](../results/R271-appendix-one-pair-four-independent-first-s1-minor-all-positive-weights.md)
已经证明
$$
\Delta_1>0
$$
在
$$
x_1\ge x_2\ge x_3\ge x_4>0
$$
全部成立，包括所有重权边界。

本次**不再次测试 $\Delta_1$ 的任何权序域**。
它只作为形成后续 Schur 来源必需的已付首枢轴。
唯一新目标为
$$
\Delta_2>0,\quad\Delta_3>0,\quad\Delta_4>0,\quad
\Delta_5>0,\quad\Delta_6>0.
\tag{2}
$$

## 2. 原 Schur 关系及实际分母

源码先形成完整对称原矩阵 (1)，然后按需作对称有理 Schur 消元。
每一阶段只递归形成当前领先块需要的条目并缓存；当前子式证书尚未通过前，
不消元后来才用到的行。其准确递推是
$
s_0(i,j)=\mathcal E_{ij},\qquad
s_{h+1}(i,j)=s_h(i,j)-\frac{s_h(i,h)s_h(h,j)}{s_h(h,h)}.
$
第 $k+1$ 个枢轴为 $s_k(k,k)$。
这只改变有限有理恒等式的求值顺序，不改变原子式或其正性来源。
在有理函数域中，前 $k$ 个枢轴的乘积准确为原 $\Delta_k$；
所得每个式子都作有理 gcd 约简。
这不预设新枢轴在正域为正；(2) 正是待证内容。

所有枢轴作为有理函数均不恒为零，因为全等正权处
原 S1 为正定。若未知正域中某个中间枢轴有零，
消元的有理身份仍在非零开域成立，并在约简后等于原领先行列式。
约简后的分母因此整除 (1) 的原 Gram 分母乘积的某个幂，
没有新加入的正域零点。
在全等权点确定这一分母的方向，就能准确测试同向分子。

源码不会用一个未证正的枢轴直接推出后续正性。
每个新 $\Delta_k$ 必须取得下面完整的五域证书。

## 3. 同一五域与固定有理平方来源

沿用
[五组权序的完整覆盖](2026-11-28-one-pair-four-independent-s1-first-minor-five-chambers-8542.md)：
$A,B,C,D\ge0$，容量二组占 $k=0,\ldots,4$。
令 $(U,V,W,Z)=(P_U,P_V,P_W,P_Z)/\tau$，其中 $\tau\ge1$。
每个新同向分子 $n$ 按其实际次数 $d$ 作齐次化，
准确代换为
$$
p_k=n^{\mathrm h}(P_U,P_V,P_W,P_Z,\tau)
=\tau^d n(P_U/\tau,P_V/\tau,P_W/\tau,P_Z/\tau).
\tag{3}
$$
旧首子式是次数 28；本稿不把这个次数预设给 (2)。

对每个 $p_k$，先逐项判断精确系数。
若出现负项，使用
[已付有理平方身份](2026-11-28-one-pair-four-independent-s1-first-minor-remaining-chambers-squares-8542.md)：
$$
aX^{e+d}-\beta X^e+cX^{e-d}
=aX^r\left(X^{(e+d-r)/2}
-\frac{\beta}{2a}X^{(e-d-r)/2}\right)^2,
\quad 4ac=\beta^2,
$$
$$
r=\min(e+d,e-d).
\tag{4}
$$
方向各分量只在 $\{-2,-1,0,1,2\}$ 中，
每域至多 32 个平方；常数项始终保留。
$a,c$ 不超过原当前正项预算，所以每步不会制造新负系数。

全部负项支付后，必须在整个有理多项式环中实际检查
$$
p_k=\text{全系数非负余式}+\text{已付平方和},
$$
而且余式常数必须严格正。
源码只打印前 3 个平方示例、总平方数、完整乘回状态、
余式项数/符号/常数和 SHA-256，禁止输出扩展系数表。

若当前域的固定配方不能完成，立即准确返回 INCONCLUSIVE，
不计算同一主子式的后续域或后续原主子式。
这既不是原 $\Delta_k$ 的反例，也不是原 S1 的反例。
若发生资源边界，也只登记已经形成的实际结果，不增加界或重放同门。

## 4. 只有全部新目标完成才允许的结论

若 (2) 的五个原主子式在五个闭域全部取得证书，
合已付 $\Delta_1>0$，Sylvester 判据才给同一完整六维 $\mathcal E>0$。
再由 [原输入的完整群约化](2026-11-28-one-pair-four-independent-original-s1-8542.md)，
$$
9=6+3,\qquad 5=4+1,
$$
另外的 pair-singlet 部分由既有一般出生一 S1 支付，
才可得这一原六位权族的完整九维 S1。

即使全部成功，也没有计算原 S2，
不会自动得到新增第七位的完整联合来源。
同一实际 $W$ 的费用、$K_\infty=M$ 和 $N=M$ 均未由本稿支付。

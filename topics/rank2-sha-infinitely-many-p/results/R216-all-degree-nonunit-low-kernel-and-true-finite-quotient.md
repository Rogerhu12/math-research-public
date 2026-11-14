# R216 — 任意原次数的非单位低核与真实有限商

日期：2026-11-12。**状态：同一个原源的全次数、全深度有限像分解及删 $C$ 商已证明。低阶扭目标完整保留；没有得到中央净收益或无穷素数非零。**

[R214](R214-quadratic-pair-tail-recursion-and-deleted-c-image.md) 的单位 Schur 分裂要求 $r>2D$。本篇移除这个大小条件，但不把非单位主块当成可逆矩阵：准确的余目标是一个具有明确低阶扭部分的有限模。所有源仍是原 $E_D$。

## 1. 全深目标与无需除法的原源分解

取惰性素数 $p=4r-1\ge19$、任意整数 $D\ge2$，置
$$
 O=\mathbf Z_p,\qquad E_D=O[A,C]_{\le D},\qquad C=B-A,
 \qquad v_0=-22\in O^\times.
$$
使用 [R215](R215-full-depth-faber-transport-and-first-cross-band-carry.md) 的实际全深权
$$
 e_j=\begin{cases}
 0,&h=\lfloor j/r\rfloor=0,\\
 h+\lfloor(h-1)/(p-1)\rfloor,&h\ge1.
 \end{cases}
 \tag{1}
$$
它单调、超可加，且原全部行
$$
 J_j(P)=p^{e_j}[w^j]P(A(w),C(w))
 \tag{2}
$$
对所有 $P\in E_D$ 都在 $O$ 中。

令 $v=\sqrt{C/v_0}$，并用原函数定义
$$
 \alpha(v)=A(w(v))=u(C)+v\beta(C),\qquad C=v_0v^2,
 \quad u(0)=0,\quad\beta(0)=1.
$$
对同一输出 $H(v)$，写唯一的双分量表示
$$
 H(v)=U_H(C)+\alpha(v)V_H(C),\qquad
 \mathscr H(H)=\binom{U_H}{V_H}.
 \tag{3}
$$
第 $2b$ 行读取 $p^{e_{2b}}[C^b]U$，第 $2b+1$ 行读取
$p^{e_{2b+1}}[C^b]V$。

R214 §10 的目标整性证明使用
$$
 A(w)/w,\ C(w)/(v_0w^2),\ v(w)/w,\ w(v)/v,\ \alpha(v)/v
 \in\mathscr B_e,
$$
以及
$$
 v_p([C^b]u)\ge-e_{2b-1},\qquad
 v_p([C^b]\beta^{\pm1})\ge-e_{2b}.
 \tag{4}
$$
这部分证明没有使用 $r>2D$。因此从 (2) 到 (3) 的全部有限前缀，仍是同一个整单位下三角目标变换。**只有低源分裂的单位性需要重新处理。**

设
$$
 K_D=\langle C^b:0\le b\le D\rangle_O
 \oplus\langle AC^b:0\le b\le D-1\rangle_O,
 \qquad \ell=2D+1.
$$
原单项式直接给整直和
$$
 \boxed{\quad E_D=K_D\oplus A^2E_{D-2}.\quad}
 \tag{5}
$$
这里不以 $\partial_A^2$ 的右逆作为源截面；当 $D\ge p$ 时，
$(a+1)(a+2)$ 未必为单位，不能除去它。本篇始终使用无除法的乘法截面 $Q\mapsto A^2Q$。

## 2. 原完整矩阵的准确非单位块

固定 $k>\ell$，保留全部原行 $0\le j<k$。将 $K_D$ 的列按它们唯一的双分量行排序，原矩阵准确成为
$$
 J_{D,<k}\sim_O
 \begin{pmatrix}
  \Lambda_D&F_{D,k}\\
  0&G_{D,k}
 \end{pmatrix},\qquad
 \Lambda_D=\operatorname{diag}(p^{e_0},\ldots,p^{e_{\ell-1}}).
 \tag{6}
$$
$F$ 和 $G$ 是同一原 $A^2E_{D-2}$ 的低行与高行，全部整。

其系数可直接用原二次关系计算。置
$$
 T=2u,\qquad N=u^2-\frac C{v_0}\beta^2,\qquad
 M(C)=\begin{pmatrix}0&-N\\1&T\end{pmatrix},
 \qquad\binom{U_a}{V_a}=M(C)^a\binom{1}{0}.
 \tag{7}
$$
则 $U_2=-N=C/v_0+O(C^2)$、$V_2=T$，而列
$Q=A^aC^b\in E_{D-2}$ 的完整余矩阵为
$$
 H_{j,(a,b)}=
 \begin{cases}
 p^{e_{2m}}[C^{m-b}]U_{a+2},&j=2m,\\
 p^{e_{2m+1}}[C^{m-b}]V_{a+2},&j=2m+1.
 \end{cases}
 \tag{8}
$$
$F=H_{<\ell}$，$G=H_{\ell,\ldots,k-1}$。式 (8) 虽可能用到非整的 $T,N$ 系数，整个归一条目由 (2)–(4) 已证明整。

在小 $p$ 段，$\Lambda_D^{-1}F$ 通常只在 $\mathbf Q_p$ 中。不能据 (6) 删除低行，或将 $A^2Q$ 减去该低行多项式后仍称为原整源截面。

## 3. 任意精度下的真正余目标

固定精度 $N_0\ge1$。下标 $N_0$ 表示精度，与 (7) 的形式级数 $N(C)$ 区分。
令
$$
 b_j=\begin{cases}
 \min(N_0,e_j),&0\le j<\ell,\\
 N_0,&\ell\le j<k,
 \end{cases}
 \qquad
 \mathcal T_{D,k,N_0}=\bigoplus_{j=0}^{k-1}O/p^{b_j}O.
 \tag{9}
$$
零指数的直和项为零模。将 (8) 的第 $j$ 行约化到
$O/p^{b_j}O$，定义同一个原源上的映射
$$
 \overline H_{D,k,N_0}:E_{D-2}\longrightarrow\mathcal T_{D,k,N_0}.
 \tag{10}
$$

**定理 3.1（完整有限像分解）。** 记
$\mathcal L_{N_0}(J)$ 为原 $J$ 模 $p^{N_0}$ 的像长度，则
$$
 \boxed{\quad
 \mathcal L_{N_0}(J_{D,<k})
 =\sum_{j<\ell}(N_0-e_j)_+
   +\operatorname{length}_O\operatorname{im}\overline H_{D,k,N_0}.
 \quad}
 \tag{11}
$$
更强地，实际有限像有短正合列
$$
 0\longrightarrow\operatorname{im}(K_D)
 \longrightarrow\operatorname{im}(J_{D,<k})
 \longrightarrow\operatorname{im}\overline H_{D,k,N_0}
 \longrightarrow0.
 \tag{12}
$$
这里的三个像都在同一模 $p^{N_0}$ 问题中定义。

**证明。** 模 $p^{N_0}$ 的完整目标是 $(O/p^{N_0})^k$。
$K_D$ 的像由 (6) 给出：第 $j<\ell$ 个坐标为
$p^{e_j}O/p^{N_0}O$，其余坐标为零。除去这个真实子模后，目标恰为 (9)，且 $A^2Q$ 的诱导像正是 (10)。因为 $K_D$ 本来包含在原源中，商映射在原像上的核准确为 $\operatorname{im}(K_D)$，给 (12)。取长度即得 (11)。$\square$

这不是把低扭项当作独立新源。对给定的同一个 $Q$，能够选择
$K\in K_D$ 使 $J(K+A^2Q)\equiv0\pmod{p^{N_0}}$，准确当且仅当
$$
 \overline H_{D,k,N_0}(Q)=0.
 \tag{13}
$$
低部条件是 $F_j(Q)\in p^{\min(N_0,e_j)}O$；高部条件是
$G(Q)\in p^{N_0}$。它们不能各自在不同的 $Q$ 上满足后再合并。

如需普通模 $p^{N_0}$ 的矩阵计算，可以将 (9) 的第 $j$ 项整嵌入
$O/p^{N_0}$，映射为乘 $p^{N_0-b_j}$。因此实际余矩阵就是
$$
 \bigl(p^{N_0-b_j}H_{j,*}\bmod p^{N_0}\bigr)_{j<k}.
 \tag{14}
$$
嵌入对有限模是单射，所以 (14) 准确保留像长度及循环列商。

较短前缀 $k\le\ell$ 也有同一个公式：只保留已经出现的 $k$ 个核列，
其余核列在这个目标中为零；(11) 的求和上限改为
$j<\min(k,\ell)$，(9)–(14) 不变。这给全部有限前缀，而不只给高尾已经出现的情形。

## 4. 原删 C 门仍降到余源的常数列

尽管较高低行不再是单位，当前 $p\ge19$ 给 $e_2=0$。
第 $2$ 行因而仍可以准确读取原 $C$ 系数。
从 (7) 的递推可得
$$
 U_2=C/v_0+O(C^2),\qquad U_a\in C^2\mathbf Q_p[[C]]\quad(a\ge3).
$$
故对任意原 $Q\in E_{D-2}$，
$$
 [C]\,\mathscr H(A^2Q)_U=Q(0,0)/v_0.
 \tag{15}
$$
在原分解 $P=K+A^2Q$ 中，$A^2Q$ 的原 $C$ 系数为零，故 $P_C=K_C$。
如果 $JP\in p^{N_0}$，第 $2$ 行精确给出
$$
 \boxed{\quad P_C\equiv-Q(0,0)/v_0\pmod{p^{N_0}}.\quad}
 \tag{16}
$$

记 $\overline H^{\setminus1}$ 为删去原常数 $Q=1$ 列的 (10)。
定义
$$
 a_{N_0}=\operatorname{length}\operatorname{im}\overline H
          -\operatorname{length}\operatorname{im}\overline H^{\setminus1}.
 \tag{17}
$$
则准确有
$$
 \boxed{\quad
 \{P_C:P\in E_D,\ JP\in p^{N_0}\}=p^{a_{N_0}}O,
 \qquad
 a_{N_0}=\mathcal L_{N_0}(J)-\mathcal L_{N_0}(J^{\setminus C}).
 \quad}
 \tag{18}
$$

证明：在有限模 $\mathcal T/\operatorname{im}\overline H^{\setminus1}$ 中，常数列的循环像长度为 (17)，其准确阶为 $p^{a_{N_0}}$。所以存在同一个其他余列组合，使 (13) 成立的常数系数 $Q(0,0)$，恰组成 $p^{a_{N_0}}O$。式 (16) 乘一个单位后给原 $P_C$ 的同一理想；所有 $p^{N_0}$ 倍数也可由原 $C$ 列加入，不改变前缀条件。第二式也可直接对原 $C$ 列应用同一个循环商论证。

被删的余常数列现在必须完整记录为
$$
 \overline H(1)=
 \left(
   p^{e_{2m}}[C^m](-N),\quad
   p^{e_{2m+1}}[C^m]T
 \right)\quad\text{分别按 (9) 约化}.
 \tag{19}
$$
当 $r>2D$ 时全部低扭项为零，(19) 退化为 R214 的双高尾列。
在小 $p$ 段，不能只保留那一双高尾；同一列的低扭坐标也属于待证的实际商阶。
对上述较短前缀，这一证明在 $k\ge3$ 时照样成立；若 $k\le2$，
原 $C$ 列尚未出现，直接有 $a_{N_0}=0$。

## 5. 满秩时，全部最大子式的分解不需要非整消元

设 $J_{D,<k}$ 在 $\mathbf Q_p$ 上有满列秩 $M_D=(D+1)(D+2)/2$。
于是 $G$ 对余源 $E_{D-2}$ 有满列秩。记 $\delta(J)$ 为所有非零 Smith 指数之和，也即全部最大子式所生成理想的赋值，则
$$
 \boxed{\quad
 \delta(J_{D,<k})=\sum_{j<\ell}e_j+\delta(G_{D,k}).
 \quad}
 \tag{20}
$$
证明不使用 $\Lambda_D^{-1}F$：一个非零最大子式必须含每个低行，
因为 $K_D$ 的每个列只在其对应低行非零。保留这些低行后，子式矩阵是块上三角，行列式就是
$\det\Lambda_D$ 乘所选高行的 $G$ 子式。反过来每个 $G$ 最大子式均如此出现，给准确的理想等式。

因此有限精度的低扭耦合与满秩最大子式的作用不同。式 (20) 不能用来删除 (10) 中控制原像格的低扭条件；它也不单独给删列后的相对最大子式。

## 6. 明确的低扭预算与不能免费迭代的部分

实际低扭目标长度为
$$
 \tau_{p,D,N_0}=\sum_{j=0}^{2D}\min(N_0,e_j).
$$
由 R173/R215 的 $e_j\le4pj/(p^2-1)$，
$$
 \boxed{\quad
 \tau_{p,D,N_0}\le
 \min\left\{N_0(2D+1),\frac{4p}{p^2-1}D(2D+1)\right\}.
 \quad}
 \tag{21}
$$
只有 $p\le8D-1$ 时它才可能非零。跨所有当前惰性素数加权，得到
$$
 \sum_p\tau_{p,D,N_0}\log p=O(D^2\log D),
 \tag{22}
$$
常数不依赖精度 $N_0$。这里用
$\sum_{p\le x}(\log p)/p=O(\log x)$；按二进区间及二项式给出的
$\sum_{p\le x}\log p=O(x)$ 即可证明该上界。

但 (22) 不是一个已经迭代完成的全次数收益。再次将余源按
$E_{D-2}=K_{D-2}\oplus A^2E_{D-4}$ 分开时，准确式是
$$
 \mathscr H(A^2Q)=M^2\mathscr H(K_{D-2})
                   +M^4\mathscr H(Q'),
 \tag{23}
$$
仍须在 (9) 的同一个有限目标中使用。较低 $F_{D-2}$ 经 $M^2$ 进入高行的卷积没有消失。R214 的整 $\mathcal R_{D-2}$ 截面在当前范围可能不存在；不能把 (23) 无证换成只有旧高尾 $G_{D-2}$ 的递推。

新的具体问题是：在 (10)、(19) 的实际有限模中，原中央条件能否提高常数列的商阶，或对 (20) 的高尾最大子式给出有方向的增益。低扭成本已明确，收益本身仍未证明。

## 7. 已有 p19 原样本的非单位校准

[精确 BigInt 脚本](../scripts/check-nonunit-low-kernel-quotient.js)
只复用此前的 $p=19,D=4,k=15$ 原样本，附
[完整输出](../scripts/check-nonunit-low-kernel-quotient.json)。
此时 $r=5\le2D$，所以确实不能使用 R214 的低单位分裂。
准确低权为
$$
 (e_0,\ldots,e_8)=(0,0,0,0,0,1,1,1,1).
$$
脚本从原 $P,Q$ 的有理级数重新取平方根和反演，比较完整原矩阵与双分量矩阵；同一窗口内 $s\leftrightarrow w$ 的整下三角运输已支付。还直接复现先前真实饱和前缀值
$0^7,(-1)^7,-2$，未用它们倒推余矩阵。

| 精度 $N_0$ | 原像长度 | 低核像长度 | 实际余商像长度 | 删常数后的余商 | 原 $a_{N_0}$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 9 | 5 | 4 | 3 | 1 |
| 2 | 24 | 14 | 10 | 8 | 2 |
| 3 | 39 | 23 | 16 | 13 | 3 |

每行都准确满足 (11)、(18)。全矩阵 Smith 为 $0^9,1^6$，高尾 $G$ 为 $0^4,1^2$，故 (20) 给
$$
 6=4+2.
$$
在这一个样本中，低扭行恰未进一步增加余商像长度；这不证明一般情况下可以删掉它们。没有扩大素数样本，也没有认证该素数满足原完整中央双零。

本篇将大 $p$ 的单位 Schur 接口推广成全次数的精确有限商接口。它完整支付原源、原归一、低扭目标及删列身份，保留真正需要研究的高尾与低扭耦合。

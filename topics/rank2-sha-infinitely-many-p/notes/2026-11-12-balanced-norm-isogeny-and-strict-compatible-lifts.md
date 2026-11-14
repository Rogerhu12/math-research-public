# 平衡范数同源的实际自对偶与严格兼容 Kummer 提升

日期：2026-11-12。这里只核对 R113 上一个具体的配对算子和
指定 Heegner 点的有限同源下降行为；不把此消失结论扩大到
反圆分 Iwasawa 塔的 Bockstein 或 $p$ 进高度。

固定 R113 的实际循环扩张 $L/F$，$[L:F]=p$ 为奇素数，
$\tau$ 为生成元。令
$$
B=\operatorname{Res}_{L/F}E,\qquad A=\ker(N:B\to E),
\qquad s=(p-1)/2,\qquad \delta=\tau^s(\tau-1).
\tag{1}
$$
实际点为 $Q=Q_{p,\ell}\in A(F)$，并已知其 $\delta$-Kummer
类在唯一分歧位 $\lambda\mid\ell$ 为零。这个严格条件来自
R100/R113 的实际 Heegner 局部关系，不是新添的假设。

## 1. 不除 p 的自对偶算子

$B$ 的乘积主极化给
$$
A^\vee=B/E_{\rm diag},\qquad
\lambda_A:A\longrightarrow A^\vee,\quad x\longmapsto[x].
\tag{2}
$$
$\delta:B\to B$ 的核恰是 $E_{\rm diag}$，像恰是 $A$，故
下降为同构
$$
\bar\delta:A^\vee\xrightarrow{\sim}A,
\qquad \iota=\bar\delta^{-1}:A\xrightarrow{\sim}A^\vee.
\tag{3}
$$
这可以在分裂坐标中直接证明。约定
$\tau(x_j)_j=(x_{j+1})_j$，指标模 $p$。对
$y=(y_j)\in A$，先令 $z=\tau^{-s}y$，再取
$$
r_0=O,\qquad r_j=\sum_{h=0}^{j-1}z_h\quad(1\le j<p).
\tag{4}
$$
因为 $\sum z_h=O$，$(\tau-1)r=z$。于是
$\iota(y)=[r]$。换起点只改一个对角常数，所以该公式对循环
Galois 作用等变，下降到 $F$。它只含整数加法，没有选择
一个全局 $p$-除点。其逆明确为 $[r]\mapsto\delta r$。

由 (2)–(3)，
$$
\lambda_A=\iota\delta.                            \tag{5}
$$
乘积极化下 $\tau$ 的伴随是 $\tau^{-1}$，因 $2s+1=p$，
平衡算子满足 $\delta^\dagger=-\delta$。所以
$$
\delta^\vee\lambda_A=-\lambda_A\delta,
\qquad \delta^\vee\iota=-\iota\delta,
\qquad \boxed{\iota^\vee=-\iota}.                 \tag{6}
$$
最后一式由 $(\iota\delta)^\vee=\lambda_A$ 及前一式得到；
在阿贝尔簇同态群中可消去同源。故 (3) 是反对称自对偶，
不能把它称为主极化。

若采用通常 Cassels–Tate 反对称约定，则
$$
B_\iota(x,y)=\langle x,\iota y\rangle_{A}
\qquad(x,y\in\Sha(A/F))
$$
是**对称**配对，且
$$
B_\iota(\delta x,y)=-B_\iota(x,\delta y).
\tag{7}
$$
这是由对偶函子及 (6) 得出的实际符号，不是把一般交替矩阵
套到一个没有给定极化的范数一簇。

## 2. 严格局部条件给出全部有限层的实际局部除点

在 $F_\lambda$，$L/F$ 全分歧次数 $p$，剩余特征为
$\ell\ne p$，而 $E$ 好约化。将 $A(F_\lambda)$ 看作
$$
\{R\in E(L_\lambda):N R=O\}.
$$
循环群在剩余域上作用平凡，故 $\delta A(F_\lambda)$
约化为零；而任意 $R\in A(F_\lambda)$ 的约化满足
$p\bar R=O$。

记 $M_1$ 为上述群中约化为零的子群。$\delta$ 在 $M_1$
上是双射。确实，令
$$
D_\tau=\sum_{j=1}^{p-1}j\tau^j,
\qquad (\tau-1)D_\tau=p-N.
$$
由于 $p$ 是 $\ell$-进单位，$[p]$ 在 $E$ 的正式群上可逆。
对 $R\in M_1$，定义其唯一正式群点
$$
Z=[p]^{-1}D_\tau\tau^{-s}R.                       \tag{8}
$$
$pNZ=0$，正式群没有 $p$ 挠点，故 $NZ=0$；并且
$\delta Z=R$。同理 $\delta$ 在 $M_1$ 无核。
因此
$$
\delta A(F_\lambda)=M_1,
\qquad \delta^r A(F_\lambda)\supset M_1
\quad(r\ge1).                                   \tag{9}
$$
若需要完整局部商，R113 的局部大小及约化满射给
$A(F_\lambda)/\delta A(F_\lambda)\simeq E(k_\lambda)[p]$。
本篇只需 (9)。

实际严格条件 $\kappa_\delta(Q)_\lambda=0$ 意味
$Q\in\delta A(F_\lambda)$。由 (9)，$Q\in M_1$，故
$$
Q\in\delta^r A(F_\lambda)\qquad\text{对每个 }r\ge1.
\tag{10}
$$
这一步的 $[p]^{-1}$ 仅用于剩余特征为 $\ell$ 的局部正式群；
没有据此构造一个全局整数点。

## 3. 指定 Q 在全部严格有限下降层中兼容提升

对每个 $r\ge1$，取实际全局 Kummer 类
$$
q_r=\kappa_{\delta^r}(Q)
 \in H^1(F,A[\delta^r]).
$$
在每个 $v\ne\lambda$，它属于通常 $\delta^r$-Kummer 局部格；
在 $\lambda$，由 (10) 它为零。因此
$$
q_r\in\operatorname{Sel}^{\lambda=0}_{\delta^r}(A/F),
\qquad
\delta^{r-1}q_r=q_1=\kappa_\delta(Q).             \tag{11}
$$
等式可从一个 $\delta^r$-除点的边界 cocycle 直接核对，
与 R113 的 $E[p]$ 坐标识别相容。

所以，若一个有限同源下降配对的左根定义为
$$
\operatorname{im}\bigl(
\operatorname{Sel}^{\lambda=0}_{\delta^r}(A/F)
\xrightarrow{\delta^{r-1}}
\operatorname{Sel}^{\lambda=0}_{\delta}(A/F)\bigr),
$$
则它对**当前指定的** $q_1$ 必为零。这是具体兼容提升 (11)
给出的结论，连严格位也已保留；不只是说普通 Cassels–Tate
配对杀 Mordell–Weil 像。

另一方面，$q_1$ 仍完全可能非零：Kummer 类能提升到全部
有限系数层，不等于 $Q$ 在 $A(F)$ 中可被 $\delta$ 除。
故 (11) 没有证明或否定目标
$Q\notin\delta A(F)$。寻找非零配对时，必须使用不同于这类
有限下降提升障碍的算术输入，例如一个真实的环类塔
Bockstein 或相应高度；本篇不声称这些更大的配对也为零。

## 输入与范围

- [R113 的实际范数同源及局部格](2026-11-12-norm-one-isogeny-and-actual-selmer-obstruction.md)：
  $A$、实际 $Q$、$E[p]$ 坐标及严格局部关系。
- [R106 的平衡增广规范](2026-11-12-dihedral-augmentation-sign-and-norm-lines.md)。
- 对偶和通常 Cassels–Tate 函子性采用 Milne（2006），
  *Arithmetic Duality Theorems*, 2nd ed., I §§3、6；
  [作者全文](https://www.jmilne.org/math/Books/ADTnot.pdf)。
  本篇真正使用的自对偶算子、局部逆及兼容类均已在 (3)–(11)
  直接构造。

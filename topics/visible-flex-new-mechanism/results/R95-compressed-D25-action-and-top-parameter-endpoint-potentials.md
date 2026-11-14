# R95. 第25阶真实幂尾的压缩 action 与最高参数端势

日期：2026-11-14。完整结果适用于 m=8 的 D25，使用真实零初值 histories、常 scalar 端芽和完整 M=0。公开运行 43639240317 已准确验证七组系数、完整原 DAG 回代及最高两次参数幂的端势；因此该 period 关于 c 的次数至多8。未证明第8次及以下系数为零、非零或同号，也没有将此 m=8 实际恒等式外推到一般 m。

## 1. 记号与真实 ODE

沿用 [R92](R92-pure-fourth-next-tail-quadratic-action.md) 的 $C,D,f$：

$$
z=c+\omega,\quad e=hz-k,\quad Q=1+e^2,\qquad
C=\frac{KQ}{8h},\quad D=\frac{Ke}{4},\quad f=\frac{Q}{8h^2}.
$$

其中 $c$ 是常参数，$\omega_s=k_s/(2h)$，$K=K_0+\lambda_s$。下标 $c$ 表示保持真实几何固定的参数偏导。记 $b=b_0,d=d_1$，则

$$
b_s=A C,\qquad d_s=xC_c+yD,\qquad J_s=D,
\qquad
A=\frac{3136}{13},\quad x=-\frac{2304}{13},\quad y=-\frac{608}{13}.
\tag{1}
$$

三者初值皆零。完整 $M=0$ 及常 scalar 端芽给三者末值也零。特别是

$$
d=\frac{x}{A}b_c+yJ=-\frac{36}{49}b_c-\frac{608}{13}J.
\tag{2}
$$

此式由 (1) 微分和共同初值推出，不是把三个独立符号强行合并。

原已验证 action 写成

$$
\mathcal A=L_0+L_b b+L_JJ+L_dd
+Q_{bb}b^2+Q_{bJ}bJ+Q_{bd}bd+Q_{Jd}Jd+Q_{dd}d^2.
\tag{3}
$$

原表无 $J^2$ 项。$L_0$ 的 1375 项与 $L_b$ 的 146 项始终完整保留。

## 2. 已通过原式逐组检验的短系数表

定义

$$
\gamma_J=\frac{589589}{900},\quad
\gamma_d=\frac{491959}{5760},\quad
t_J=\frac{1520519}{225},\quad
t_d=\frac{2923193}{7200}.
$$

以下短式已由公开 Actions 对完整原始系数组逐项验证：

| 系数 | 准确表达式 |
|---|---|
| $L_J$ | $A\gamma_J f_s C$ |
| $L_d$ | $A\gamma_d f_s C$ |
| $Q_{Jd}$ | $t_J C$ |
| $Q_{dd}$ | $t_d C$ |
| $Q_{bJ}$ | $-6485479C_c/1350-1334333D/1350+\gamma_J f_{ss}$ |
| $Q_{bd}$ | $-5156021C_c/8640-5607251D/43200+\gamma_d f_{ss}$ |
| $Q_{bb}$ | $169(C_{cc}-5D_c+17hK/20)/480$ |

最后一个 17 项小组也可写成

$$
Q_{bb}=169\left(-\frac{C_{cc}}{200}
+\frac{3D_c}{800}+\frac{17kQ}{9600h}\right).
\tag{4}
$$

两种写法等价，因为直接微分 $C=KQ/(8h)$、$D=Ke/4$，利用 $K_{cc}=2k$，得到

$$
C_{cc}-2D_c=\frac{kQ}{4h}-\frac{hK}{4}.
\tag{5}
$$

消费器对表中每一行单独计算“公开系数减候选式”的准确 Laurent 多项式，报告所有零与非零项；不是只检查一组样本或哈希。本次七行全部准确为零；完整差式与未丢项的 action 都在原始证书中保留。

## 3. 新端势与完整余项

令

$$
F_2=f_s b(\gamma_JJ+\gamma_dd)
+\frac{b}{A}(t_JJd+t_dd^2).
\tag{6}
$$

使用真实 ODE (1)，第一项的导数同时支付 $f_{ss}bJ,f_{ss}bd$ 及纯 $J,d$ 线性组；第二项的导数支付 $Jd,d^2$ 组。由这些准确等式，完整结果是

$$
\begin{aligned}
\mathcal A-D_sF_2={}&L_0+b\widetilde L_b
+\frac{169}{480}b^2\left(C_{cc}-5D_c+\frac{17}{20}hK\right)\\
&+b(C_c+2D)\left(\frac{217217}{1350}J
-\frac{8281}{43200}d\right),\\
\widetilde L_b={}&L_b-f_s\{\gamma_JD+\gamma_d(xC_c+yD)\}.
\end{aligned}
\tag{7}
$$

$F_2$ 两端为零，因此 (7) 与原 action 的积分相同。$L_0$ 和 $\widetilde L_b$ 未被删除、未被假设为全导数，也没有在本稿得到符号结论。公开完整证书已把 (7) 连同 R92 已付端势、原始第一积分商一起回代原始 D25 DAG，所有真实 history 和 RHS 保留。

另令 $B=b/A$，则 $B_s=C$。用 (2)，(7) 的全部二次部分恰为

$$
\mathcal Q=\mathfrak m\left[
B^2\left(C_{cc}-5D_c+\frac{17}{20}hK\right)
+\frac25 B(B_c+5J)(C_c+2D)\right],
\qquad \mathfrak m=\frac{169A^2}{480}.
\tag{8}
$$

这一步只重写真实 parameter family。没有将 $B_c$ 与 $B$ 视为可独立选择的控制。

## 4. 最高两个 $c$ 幂的准确端势

写

$$
C=\sum_{j=0}^{4}C_jc^j,\quad D=\sum_{j=0}^{3}D_jc^j,
\quad B=\sum_{j=0}^{4}B_jc^j,\quad J=\sum_{j=0}^{3}J_jc^j.
$$

真实系数 ODE 是 $B_j'=C_j$、$J_j'=D_j$，初值皆零。由 $K$ 的二次式直接得

$$
C_4=\frac{kh}{8},\quad D_3=2C_4,\quad J_3=2B_4,
\quad [c^1](hK)=8(D_2-C_3).
\tag{9}
$$

因此

$$
\begin{array}{ll}
[c^2](C_{cc}-5D_c+17hK/20)=-56C_4/5,
&[c^3](C_c+2D)=8C_4,\\
[c^1](C_{cc}-5D_c+17hK/20)=-4(C_3+4D_2)/5,
&[c^2](C_c+2D)=3C_3+2D_2.
\end{array}
\tag{10}
$$

将 (10) 代入 (8)，只用最高两项 $B_4c^4+B_3c^3$ 与 $2B_4c^3+J_2c^2$，逐项得

$$
[c^{10}]\mathcal Q
=\frac{168\mathfrak m}{5}B_4^2C_4
=D_s\left(\frac{56\mathfrak m}{5}B_4^3\right),
\tag{11}
$$

$$
\begin{aligned}
[c^9]\mathcal Q
={}&\mathfrak m\{16B_4^2C_3+8B_4^2D_2
+32B_4B_3C_4+16B_4J_2C_4\}\\
={}&D_s\{\mathfrak m(16B_4^2B_3+8B_4^2J_2)\}.
\end{aligned}
\tag{12}
$$

两势均含 $B_4^2$，故完整 $M=0$ 所给的 $B_4(0)=B_4(L)=0$ 已足支付端项。公开 consumer 已将三个真实系数 primitive $B_4,B_3,J_2$ 作为有明确 RHS、零初值的辅助历史加入，仅检查这些最高系数；不能以任意独立 state 代替它们。

原已公开 action 的 $L_0$ 最高 $c$ 次数为 8，$L_b$ 最高为 4。$f_s$ 对 $c$ 至多一次、$xC_c+yD$ 至多三次，故 $\widetilde L_b$ 仍至多四次。因此，完整 D25 period 关于 $c$ 的次数至多 8。消费器已对这两项次数界逐项核验。**这个次数界不证明 $c^8$ 消失，不证明整个 D25 period 为零或同号。**

## 5. 公开原式证据与剩余范围

实际运行：[43639240317](https://github.com/Rogerhu12/math-research-public/actions/runs/43639240317)，来源提交 af5d4aa7f1ca8c0f8bceb08c430f8bda203aa5f6；消费器 literature_pure_tail_action_compress.py 的 SHA256 为 f7ed0471d659c95eca183604648057ea2522b0ed1766235b9a9da57c867c52f4。实际10.928123297秒，峰值RSS98.5546875MiB；没有重编forcing或评价几何路径。

[完整实际报告](../notes/actions-43639240317-1-pure_tail_action_compress/pure-tail-action-compressed.json)为8091字节、SHA256 05b3cf0a593733a29948d920d73937c1f61bb11e14f43430cae6570aa58fb8e0。报告保留上一级报告与原始DAG身份。全部七组系数差、五个压缩后分组差、新端势、真实I0的导数/初值、三个真实primitive RHS、最高参数幂及fresh原DAG回代都准确为零。

[完整证书](../notes/actions-43639240317-1-pure_tail_action_compress/pure-tail-action-compressed-certificate.json.gz)压缩60213字节，SHA256 5e464bc26a874656b3e0b7548c44d6fe24a88a4e554981967b55675242005e7d；解压567045字节，SHA256 25a3499e6c8392b62f83678d357a3850e8f26ab4c15acdf7bf57595397a52136。[可读系数](../notes/actions-43639240317-1-pure_tail_action_compress/pure-tail-action-compressed-expressions.json)65186字节、SHA256 c7af820608cfc46aca843a68a58a1f83e5462a968d9f30a75560354fb01b0453。15个源真实history保留，三个新增参数系数primitive有各自真实ODE，不作为独立控制。

压缩action共有1605项、五组：常数1375项，b线性139项，Jb与bd各37项，b²为17项。源常数局部项完全保留；新线性项的139项来自明确端势代换，未被丢弃。最高参数系数的原函数已单独给出，零端代换也准确为零。

接下来须研究剩余c8及以下完整period，并遵守[R93](R93-zero-matrix-geometric-energy-and-frame-length.md)、[R97](R97-zero-matrix-paths-require-nonconstant-h.md)的真实几何积分约束。非零action密度、有限项数或正能量下界都不自动给period符号。P0、逐s第四ruling、全部更高阶/收敛及完整可弯闭面的几何门仍未完成。

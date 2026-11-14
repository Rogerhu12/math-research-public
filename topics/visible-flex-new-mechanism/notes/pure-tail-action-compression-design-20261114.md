# D25 三 primitive action 的端势压缩与最高参数幂

日期：2026-11-14。这里消费已经公开的 m=8 D25 action；不重编 R56 forcing，不求任何几何路径，不将非零密度解释为非零 period。

输入为 `actions-43637739532-1-pure_tail_next_reduce/pure-tail-next-action.json` 及其完整 `pure-tail-next-action-certificate.json.gz`。原实际运行已证明 R92 的三 primitive 二次正规形和完整原 DAG 回代；本稿提出更短的系数表示并给出它成立后的端势推论。尤其两个 218 项线性组仍须由新公开 consumer 逐项归零验证，不能把人工开发测试当成该实际恒等式的证明。

## 1. 记号与真实 ODE

沿用 [R92](../results/R92-pure-fourth-next-tail-quadratic-action.md) 的 $C,D,f$：

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

## 2. 待公开原式核的短系数表

定义

$$
\gamma_J=\frac{589589}{900},\quad
\gamma_d=\frac{491959}{5760},\quad
t_J=\frac{1520519}{225},\quad
t_d=\frac{2923193}{7200}.
$$

从公开系数表识别出的短式为：

| 系数 | 候选准确表达式 |
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

消费器对表中每一行单独计算“公开系数减候选式”的准确 Laurent 多项式，报告所有零与非零项；不是只检查一组样本或哈希。任何一行失败都会使 `verified_complete_action_compression=false`，保留完整差式及未丢项的 action。

## 3. 新端势与完整余项

令

$$
F_2=f_s b(\gamma_JJ+\gamma_dd)
+\frac{b}{A}(t_JJd+t_dd^2).
\tag{6}
$$

使用真实 ODE (1)，第一项的导数同时支付 $f_{ss}bJ,f_{ss}bd$ 及纯 $J,d$ 线性组；第二项的导数支付 $Jd,d^2$ 组。表中等式成立时，完整结果是

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

$F_2$ 两端为零，因此 (7) 与原 action 的积分相同。$L_0$ 和 $\widetilde L_b$ 未被删除、未被假设为全导数，也没有在本稿得到符号结论。新公开证书把 (7) 连同 R92 已付端势、原始第一积分商一起回代原始 D25 DAG，所有真实 history 和 RHS 保留。

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

两势均含 $B_4^2$，故完整 $M=0$ 所给的 $B_4(0)=B_4(L)=0$ 已足支付端项。新 consumer 将三个真实系数 primitive $B_4,B_3,J_2$ 作为有明确 RHS、零初值的辅助历史加入，仅检查这些最高系数；不能以任意独立 state 代替它们。

原已公开 action 的 $L_0$ 最高 $c$ 次数为 8，$L_b$ 最高为 4。$f_s$ 对 $c$ 至多一次、$xC_c+yD$ 至多三次，故 $\widetilde L_b$ 仍至多四次。因此，若表中候选式全部验证，完整 D25 period 关于 $c$ 的次数至多 8。消费器将这两项次数界也逐项核验。**这个次数界不证明 $c^8$ 消失，不证明整个 D25 period 为零或同号。**

## 5. 实现和公开命令

独立源码：`scripts/literature_pure_tail_action_compress.py`。它只导入旧冻结系数工具，不修改旧 producer、回执或输出。

```bash
python topics/visible-flex-new-mechanism/scripts/literature_pure_tail_action_compress.py \
  --report topics/visible-flex-new-mechanism/notes/actions-43637739532-1-pure_tail_next_reduce/pure-tail-next-action.json \
  --certificate topics/visible-flex-new-mechanism/notes/actions-43637739532-1-pure_tail_next_reduce/pure-tail-next-action-certificate.json.gz \
  --out "$VISIBLE_OUT/pure-tail-action-compressed.json" --max-seconds 240
```

研究入口核公共 Actions/repository、准确输入压缩与解压字节、输入完整模型与源身份。每条候选、真实 ODE、原第一积分、新端势、最高两参数幂和 fresh 原始 DAG 回代分别报告。输出完整 gzip 证书及不超过 95 KB 的可读系数组；可读截断只影响展示，完整式仍在证书中。

人工 `--check-only` 只使用小型制造多项式：参数偏导、拒绝擅自微分 history、精确序列化、最高系数真实 ODE、故意错误 $K_1$ 的拒绝。没有读取实际研究输入，没有运行实际 action 化简。研究结果以随后公共回执为准。

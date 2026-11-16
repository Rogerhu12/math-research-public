# 原参数模完整来源权七的秩 947 与 Bell 饱和边界

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

## 1. 已付输入与本页结论

本页只使用同一合法剩余映射 $p=127,d\mapsto100$ 下已经完成的原多项式模型、五十列压缩和三十条首层乘法来源。没有新的大矩阵运行，也不把有限域选元提升为特征零选元。

令

$$B=\mathbb F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5],
\qquad \operatorname{wt}(y_i)=1,\quad\operatorname{wt}(w_i)=2,$$

$$F=\bigoplus_{a=0}^{9}B e_a,
\qquad (\operatorname{wt}(e_a))_{a=0}^{9}=(0,2,2,2,2,2,4,4,4,4),$$

并记 $b=\sum_{i=0}^{5}y_iw_i$。模次数按系数参数权与 $e_a$ 的权相加。所有十二参数均保留。

已付五十原列由以下四组组成：

| 原列组 | 数量 | 模权 |
|---|---:|---:|
| 六条均值列 $Y_j$ | 6 | 5 |
| 保留交换子 $C_\ell$ | 20 | 6 |
| 保留交换子 $D_\ell$ | 14 | 8 |
| Bell 列 $(b-1)e_a$ | 10 | 最高权 $3+\operatorname{wt}(e_a)$ |

前三组严格齐次。令它们生成的齐次子模为 $G\subset F$，并令

$$L_0=G+(b-1)F.$$

本页证明，按第 2 节定义的完整来源权界：

$$\dim_k L_0^{\langle\le7\rangle}=917,$$

$$\dim_k\left(L_0^{\langle\le7\rangle}
 +\operatorname{span}_k\{V_{ij}:0\le i<5,\ 0\le j<6\}\right)=947,
\qquad V_{ij}=N_iY_j.$$

因此三十新列在**完整来源权不超过七的旧像**的商中独立，而不仅在先前选取的 282 列前缀的商中独立。这里的完整性指五十原列的全部合法有界参数乘子，不能换成 $L_0\cap F_{\le7}$；后者允许高权来源相消，尚未由本页穷尽。

依据为 [原三十条均值首层来源与完整权七秩 312](R150-appendix-original-thirty-mean-images-and-complete-weight-seven-rank312.md) 和 [原参数种子五十列与完整有限域模等价](R150-appendix-original-parameter-seeds-fifty-and-complete-field-module-equivalence.md)。三十条新列各自的原十八来源仍是

$$m^{\mathsf T}V_{ij}=A^{\mathsf T}\tau_{ij},
\qquad \tau_{ij}=u_i\sigma_j-S_iY_j,$$

其中 $m^{\mathsf T}N_i=u_i m^{\mathsf T}-A^{\mathsf T}S_i$、$m^{\mathsf T}Y_j=A^{\mathsf T}\sigma_j$ 已逐原多项式实际验证。

## 2. 来源权界的定义

记 $B_d$ 为权恰 $d$ 的参数齐次空间，$B_{\le d}=\bigoplus_{r=0}^{d}B_r$；负下标表示零空间。对于来源权上界 $D$，定义

$$G^{\langle\le D\rangle}
=\sum_{j=0}^{5}B_{\le D-5}Y_j
+\sum_{\ell=1}^{20}B_{\le D-6}C_\ell
+\sum_{\ell=1}^{14}B_{\le D-8}D_\ell,$$

$$L_0^{\langle\le D\rangle}
=G^{\langle\le D\rangle}+(b-1)F_{\le D-3}.$$

这就是逐原列取所有合法参数单项式乘子的像；Bell 列使用其最高权 $3+\operatorname{wt}(e_a)$。定义限制的是每个原来源项的最高权，不是相消后的输出权。

由于 $G$ 的原生成元齐次，

$$G^{\langle\le D\rangle}
=\bigoplus_{d\le D}G_d=G\cap F_{\le D}.$$

但是 $L_0$ 还含非齐次的 Bell 关系，不能由此把 $L_0^{\langle\le D\rangle}$ 与 $L_0\cap F_{\le D}$ 等同。

对原 116 列而言，十条权四的 $e_0$ 交换子已逐原十坐标验证为零，其余被删除权六交换子的已付表达式只使用均值列的权一倍数和保留权六交换子，严格保持模权；权八交换子在来源权七下没有合法乘子。因此原 116 列在同一权界下的**像**也等于上述五十列的有界像。原 116 列自身的来源系数空间含额外关系，本页不把它的全部列称作独立的 917 列。

## 3. 完整齐次部分：344 与 374

十二参数的权计数由

$$\dim_k B_d=
\sum_{r=0}^{\lfloor d/2\rfloor}
\binom{r+5}{5}\binom{d-2r+5}{5}$$

给出。所需完整列表为

| $d$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $\dim B_d$ | 1 | 6 | 27 | 92 | 273 | 714 | 1715 | 3816 | 8007 | 15938 | 30381 |

在来源权七下，$G$ 只可能贡献下列三个齐次部分：

| 输出模权 | 全部合法原来源 | 列数 |
|---|---|---:|
| 5 | $Y_j$ | 6 |
| 6 | $y_aY_j$ 与 $C_\ell$ | $36+20=56$ |
| 7 | $qY_j$，$q\in B_2$；以及 $y_aC_\ell$ | $162+120=282$ |

已付完整 $7754\times312$ 矩阵的 312 列独立，包括权七的全部 282 旧列和全部三十条 $V_{ij}$。于是权七旧列独立。

权六列表乘以固定 $y_0$ 后，逐列进入权七列表中的不同原列；所以权六若有常数关系，就会给权七列表的关系，迫其系数全零。权五列表乘 $y_0^2$ 同理独立。这也给出低两阶的独立性，不需要新消元。

不同模权的齐次空间为直和，故

$$\dim_k G^{\langle\le7\rangle}=6+56+282=344.$$

三十新列全为权七，已付 312 独立性进一步给

$$\dim_k\left(G^{\langle\le7\rangle}
+\operatorname{span}_k\{V_{ij}\}\right)=6+56+312=374.$$

## 4. 完整 Bell 部分：573 维及交零

来源权七所允许的全部 Bell 系数向量是 $c\in F_{\le4}$。其完整维数为

$$\dim_kF_{\le4}
=\dim B_{\le4}+5\dim B_{\le2}+4\dim B_{\le0}
=399+5\cdot34+4=573.$$

对任意非零 $c\in F_{\le4}$，取其最低非零模权 $r\le4$。因为 $b$ 的权为三，$(b-1)c$ 的模权 $r$ 部分恰为 $-c_r\ne0$。因此：

1. 映射 $c\mapsto(b-1)c$ 在 $F_{\le4}$ 上单射；
2. 其任何非零像具有不超过四的最低模权；
3. 第 3 节的齐次部分及三十新列均无模权小于五的项，所以它们与此 Bell 像的交为零。

故有真正的 $k$ 线性直和

$$L_0^{\langle\le7\rangle}
=G^{\langle\le7\rangle}\oplus(b-1)F_{\le4},$$

以及加入三十列后的同样直和。于是完整有界旧像维数 $344+573=917$，加入后维数 $374+573=947$。

全部不超过七的输出坐标数为

$$\dim F_{\le7}
=6644+5\cdot1113+4\cdot126=12713.$$

所以完整有界旧来源列表的 $12713\times917$ 矩阵秩恰 917，追加三十列后的 $12713\times947$ 矩阵秩恰 947。这两项由已付分级矩阵和上述直和证明推出；**没有实际构造或运行这两个新矩阵**。

## 5. 总来源权十的准确条件

现在令 $V\in F_7$ 为任意权七齐次向量，特别可取三十条 $V_{ij}$ 的任意常数线性组合。则

$$V\in L_0^{\langle\le10\rangle}
\quad\Longleftrightarrow\quad bV\in G_{10}.$$

证明如下。若 $V=g+(b-1)c$ 的来源权不超过十，则 $g\in\bigoplus_{d\le10}G_d$、$c\in F_{\le7}$。按模权对三的余数分解；由于 $b$ 权三，只需保留与 $7$ 同余的部分。$G$ 的最小权为五，故该部分写成

$$V=g_7+g_{10}+(b-1)(c_1+c_4+c_7).$$

比较权一、四得 $c_1=c_4=0$；比较权七、十得

$$V=g_7-c_7,\qquad 0=g_{10}+bc_7.$$

因此 $bV=g_{10}+bg_7\in G_{10}$。反之，若 $bV=g_{10}\in G_{10}$，则

$$V=g_{10}-(b-1)V$$

就是来源权不超过十的完整旧来源表达。两个方向只使用原列和参数多项式，不倒置 $b$。

$G_{10}$ 的完整原来源列表为

$$B_5\{Y_j\}\ \cup\ B_4\{C_\ell\}\ \cup\ B_2\{D_\ell\},$$

共

$$6\cdot714+20\cdot273+14\cdot27=10122$$

列。其完整输出数为

$$\dim F_{10}=30381+5\cdot8007+4\cdot1715=77276.$$

若将全部三十个 $bV_{ij}$ 加作目标，完整矩阵尺寸是 $77276\times10152$。这只是准确的后继接口；**本页没有启动或完成该矩阵，也没有预填其秩或任何目标成员结果**。

## 6. 未截断成员性仍是所有 Bell 幂的条件

更一般地，对齐次 $V\in F_7$ 和整数 $q\ge0$，同一逐权比较给

$$V\in L_0^{\langle\le7+3q\rangle}
\quad\Longleftrightarrow\quad b^qV\in G_{7+3q}.$$

必要性可在分次商 $F/G$ 中看清：若 $\overline V=(b-1)\overline c$，只保留权模三余一的部分，从权一、四开始比较，到权七得到 $\overline c_7=-\overline V$，后续递推

$$\overline c_{7+3r}=-b^r\overline V.$$

来源权界给 $c$ 的最高权不超过 $4+3q$，最高下一层迫 $b^q\overline V=0$。$q=0$ 时没有权七系数，直接给 $\overline V=0$。充分性由精确多项式身份

$$V=b^qV-(b-1)(1+b+\cdots+b^{q-1})V$$

给出；$q=0$ 时右侧只取 $V$。

任何多项式来源只有有限权，故对齐次权七向量有

$$V\in L_0
\quad\Longleftrightarrow\quad
\text{存在 }q\ge0\text{ 使 }b^qV\in G.$$

这说明完整未截断问题是 $G$ 对 $b$ 的饱和问题。已经证明的来源权七独立性只排 $q=0$；未来若权十检验不成员，也只再排 $q=1$。它们均不能单独排除更高幂，不能由此宣称 $L_0+\sum BV_{ij}$ 严格大于 $L_0$，也不能代替单位来源或稳定闭包的完整门。

## 7. 原执行身份与范围

本页唯一使用的新秩事实来自已经完成的三十来源计算，主源为：

~~~text
notes/2026-11-16-r150-original-mean-first-frontier127-789f.py
blob 049028bbcfa486e8335d589c203d7cf682c4d7ac
18470 bytes
SHA256 810904a2c797b08493ed377c069abd75018e0a0df8035cb700baad80616bea1e
~~~

其真实 binding 为 `9502b11bf94390e8833cdc236a1ad85746d9823f9f4fe1e62de60f1932434bfd`，完整 raw 为 25766 bytes / SHA-256 `20405495e04e812ddd06366e1edd300f4cf7d612ccc959eeadb836a9323594ea`，执行身份见 `notes/r150-original-parameter-module-execution-789f/local-20261116-original-mean-first-frontier127-180.json`。

本页只是对既有完整原来源和真实秩的代数推论，不增加计算完成声明。所有独立性与维数均在指定有限域系数映射下；原特征零来源提升、完整 Bell 单位来源和未截断稳定闭包仍各有独立的实际验证门。

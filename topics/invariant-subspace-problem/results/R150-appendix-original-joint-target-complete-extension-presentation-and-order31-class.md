# R150：原共同目标模的完整参数呈示与恰为 31 阶的非裂扩张类

作者：ChatGPT（AI），literature_audit。日期：2026-11-16。

本篇在已完成的原共同模上，仅使用其真实有限坐标、完整关系格和真实参数作用。一个 $0.103240044$ 秒的整数 HNF 小计算确定了剩余扩张类；没有再次求解原来源矩阵。结合已付整自由格和根一、根二全部扭子，得到完整 $D[s]$ 模呈示。

## 1. 原模与本次结论

仍置 $p=31$、$D=\mathbf Z_{(31)}$、$R=D[s]$、$x=s-2$，沿原十七方程及全部 6188 个来源记

$$
M=\sum_{j=2}^{10}R[t_j],\qquad S=M\cap C[p^\infty],
\qquad B=h_*M,\qquad h=\frac{h_*}{3125}.
$$

$h$ 首一，次数为二十三。[完整系数扭子定理](R150-appendix-original-joint-target-complete-coefficient-torsion-length35.md)已付

$$
S=S_1\oplus S_2,\qquad S_1=R/(p,s-1),
$$

$$
S_2\simeq_D(D/p^2)^7\oplus D/p^4\oplus(D/p^5)^2\oplus D/p^6.
$$

本次小计算得到

$$
\boxed{S_2/hS_2\simeq_D(D/p)^5\oplus(D/p^2)^3.}
$$

原 $b_2=[h_*t_2]$ 在此商中的类非零，且恰有阶 $p$。这个类同时是 primitive 的模 $p$ 类，因而

$$
\boxed{S_2/B\simeq_D(D/p)^4\oplus(D/p^2)^3,\qquad
S/B\simeq_D(D/p)^5\oplus(D/p^2)^3.}
$$

以下给出完整参数模的非规范直和与确切呈示：

$$
\boxed{
M\simeq_R (R/(s))^2\oplus R/(p,s-1)\oplus E_2,
\qquad
E_2=\frac{Rf\oplus S_2}{R(hf-b_2/3125)},\quad f=[t_2].}
$$

其最后一个正合列

$$
0\longrightarrow S_2\longrightarrow E_2\longrightarrow R/(h)\longrightarrow0
$$

**不分裂**。它在 $\operatorname{Ext}^1_R(R/(h),S_2)$ 中的类恰被 $p$ 杀死。这里陈述的是参数模扩张；此前作为 $D$ 模的自由／扭子分裂并没有被误作 $R$ 分裂。

## 2. 原 $t_2$ 确实给整的二十三维循环自由格

[整自由格资格](R150-appendix-original-joint-target-primitive-integral-free-lattice.md)已给

$$
F_M\simeq_R R/(s)\oplus R/(s)\oplus R/(h).
$$

另一个已实际完成的[原自由循环格审计](../notes/2026-11-16-r150-original-free-target-cyclic-lattice-audit-789f.py)保留全部 225 个原 Krylov 列，并核出原 $t_2$ 的前二十三个自由 Krylov 列模 $31$ 的秩恰为二十三。该审计的实际身份见[执行记录](../notes/2026-11-16-r150-original-free-target-cyclic-lattice-local-execution-789f.json)。它只对这个实际原目标作以下使用，不将另外目标的模 $31$ 秩预填为二十三。

令 $U=R\overline{t_2}\subset F_M$。由 $h\overline{t_2}=0$、已付有理最小多项式恰为 $h$，以及上述整单位子式，

$$
U\simeq_R R/(h)
$$

是 $F_M$ 中饱和的 $D$ 直和项。$F_M/U$ 是秩二的 $D$ 自由模。在有理数域上 $sF_{M,\mathbf Q}=sU_{\mathbf Q}$。又因 $h(0)=0$，$U/sU\simeq_D D$，所以

$$
U\cap sU_{\mathbf Q}=sU.
$$

故 $sF_M\subset sU$。对 $F_M/U$ 的两个 $D$ 基提升，分别减去 $U$ 内的适当元素，可以使其真被 $s$ 杀死。这证明可取

$$
F_M=U\oplus W,\qquad W\simeq_R(R/(s))^2,
$$

并使 $U$ 的生成元就是原 $t_2$ 的自由像。

## 3. 两个 $s$ 轴和根一扭子的真实分裂

$S$ 的模 $31$ 参数支撑只有根一、根二，因此 $s$ 在完整有限 $D$ 模 $S$ 上可逆。该逆可由参数作用的一个多项式表示，故它保持所有相关 $R$ 子模。

对上一节 $W$ 的任意基元，取原 $M$ 中一个提升 $m$。因其自由像被 $s$ 杀死，$sm\in S$；减去 $s^{-1}(sm)$ 后便得到一个真被 $s$ 杀死的提升。两个提升独立，于是

$$
M\simeq_R(R/(s))^2\oplus E,
\qquad 0\longrightarrow S\longrightarrow E\longrightarrow R/(h)\longrightarrow0.
$$

取原 $f=[t_2]$。它与 $S$ 生成 $E$，并有真实关系

$$
hf=b_2/3125.
$$

这唯一自由商关系已足给完整呈示。确切地，若 $af+z$ 在 $E$ 中为零，投到 $R/(h)$ 得 $a=hv$；再代入得 $z=-v b_2/3125$，恰是这一关系的 $R$ 倍数。因为 $h$ 在 $R$ 中非零，该商仍将 $S$ 单射保留，不增加隐藏扭子关系。

已付 $x^2B=0$，而 $x$ 在根一主分量上为单位，所以 $B_1=0$。特别是 $b_2$ 的根一分量严格为零。于是上述关系完全位于 $Rf\oplus S_2$，$S_1$ 从 $E$ 中真实分裂，得到 §1 的完整直和公式。

## 4. 带已付具体矩阵的有限 $R$ 呈示

[根二完整计算](R150-appendix-original-joint-target-root-two-torsion-length34-and-eight-generators.md)保存了二十六个真实扭子生成元，完整 $D$ 关系矩阵 $K$ 和真实参数作用矩阵 $X$，均为 $26\times26$。这里 $X$ 表示 $x=s-2$ 的作用。全部关系与 $XK$ 在原十四个不变量因子坐标中逐项乘回为零；完整格指数也已核实。因此

$$
S_2\simeq_R\operatorname{coker}\bigl[K\ \ (s-2)I-X\bigr].
$$

设 $\delta\in p\mathbf Z_{31}$ 为 $h_*(2+X_0)$ 的简单 Hensel 根，写

$$
h_*(2+X_0)=(X_0-\delta)q(X_0).
$$

这里 $q$ 在根二完成分量上为单位。只在这个完成分量中，记 $f_2$ 为原 $f$ 的投影并定义 $u=(x-\delta)f_2$。它的自由像为零，故属于 $S_2\otimes_D\mathbf Z_{31}$；由 $p^6S_2=0$，这个有限模自然识别为原 $S_2$。以下 $u$ 的二十六个坐标通过该识别读取；不要求 $\delta\in D$，全局关系仍使用原 $h$。小审计完整核了

$$
b_2=q(X)u,
$$

并以已付原 $b_2$ 的全部十四个真实坐标作独立比较。

取

$$
c=3125^{-1}q(X)u
$$

的任意模 $p^6$ 整坐标提升。因 $p^6S_2=0$，不同提升给同一个真实元素。所需完整呈示可写成明确的 $27\times53$ 矩阵

$$
\boxed{
E_2\simeq_R\operatorname{coker}
\begin{pmatrix}
0&0&h\\
K&(s-2)I-X&-c
\end{pmatrix}.}
$$

这给出整参数作用和自由／扭子耦合，不只是 $D$ 不变量因子表。$K,X,u$ 以及计算 $c$ 的全部输入都来自已实际完成的完整小坐标文件；本篇没有用模 $31$ 的参数矩阵替代高 $31$ 位作用。具体数学数组留在临时计算目录，源码和全部输入身份可复算该呈示。

## 5. 实际整数格指数与扩张类阶

令 $A_S$ 为十四个真实扭子轴上二十六个生成元的坐标矩阵。所有计算在已确定的真实环境

$$
T_2\simeq_D D/p\oplus(D/p^2)^4\oplus(D/p^3)^2
\oplus(D/p^4)^4\oplus(D/p^5)^2\oplus D/p^6
$$

中进行。对任意列族 $V$，将其整提升与环境关系对角列 $p^{e_i}e_i$ 一起作整数 HNF，其格指数精确给出 $\ell_D\langle V\rangle$。依次使用 $p^kV$ 得到全部循环因子。

对商 $S_2/H$，实际计算使用

$$
\ell_D\bigl(p^k(S_2/H)\bigr)
=\ell_D\langle p^kA_S,H\rangle-\ell_D\langle H\rangle.
$$

这里 $H=A_Sh_*(2I+X)$。计算还以双向格指数核了

$$
h_*S_2=(x-\delta)S_2,\qquad
B=h_*S_2+Db_2.
$$

得到如下实际数据：

| 有限模 | 完整 $D$ 指数 | 长度 |
|---|---|---:|
| $h_*S_2=hS_2$ | $1^7,3,4,4,5$ | 23 |
| $S_2/hS_2$ | $1^5,2,2,2$ | 11 |
| $D[b_2]\subset S_2/hS_2$ | $1$ | 1 |

第一商的逐次 $p$ 像长度为 $11,3,0$。原 $b_2$ 类的对应长度为 $1,0$；以 $u$ 模 $(x-\delta)S_2$ 计算得到完全相同的阶。

此外，完整关系与参数作用已给

$$
u\notin pS_2+xS_2.
$$

由于 $q$ 为单位，$b_2$ 在 $S_2/hS_2$ 的模 $p$ 商中也非零。一个阶 $p$ 且模 $p$ 非零的元素，在有限 $D$ 模中张成一个 $D/p$ 直和项。将它从 $(D/p)^5\oplus(D/p^2)^3$ 商去，便得到 §1 中 $S_2/B$ 的完整类型；再加 $S_1=D/p$ 得到 $S/B$ 的类型。

## 6. 非裂性与恰一层的系数扩张缺口

由 $0\to R\xrightarrow{h}R\to R/(h)\to0$，

$$
\operatorname{Ext}^1_R(R/(h),S_2)\simeq S_2/hS_2.
$$

本篇 $E_2$ 的类是 $[b_2/3125]$。其精确阶是 $p$，所以扩张不分裂，且乘 $p$ 后的扩张类为零。等价地，存在 $v\in S_2$ 使

$$
hv=p\,b_2/3125,\qquad h(pf-v)=0,
$$

但不存在将原自由生成元本身提升为被 $h$ 杀死的截面。该结论没有在 $D$ 中除以 $p$，也没有改变原目标。

实际最少生成元 $d_R(S_2)=d_R(M_2)=8$ 提供一致的交叉检查：这个 primitive 非零扩张类消去一个 Nakayama 生成元；若直接把自由线与 $S_2$ 分裂，局部最少生成元会是九。

小计算另得到 $S_2/Rb_2$ 的类型为 $2^7,4,4,5$、长度二十七；此处 $Rb_2=Db_2+Dxb_2$，全部两列均保留。因而作为 $D$ 模，

$$
M/R[t_2]\simeq_D D^2\oplus D/p\oplus(D/p^2)^7
\oplus(D/p^4)^2\oplus D/p^5.
$$

这仍不以一个目标的循环模替代整个共同模；它是完整共同呈示的另一个可复算商。

## 7. 实际来源和身份

只读源码为 [original joint M extension audit](../notes/2026-11-16-r150-original-joint-m-extension-class-audit-789f.py)，执行身份为 [extension local execution](../notes/2026-11-16-r150-original-joint-m-extension-class-local-execution-789f.json)。

| 对象 | 身份 |
|---|---|
| 审计源码 | 7015 bytes；SHA256 `2dc6fe86e0d7494326a79228ee33aed3ecea19c8dc0d9fa1f2a00da5df1ec718` |
| 完整根二呈示输入 | 16797 bytes；SHA256 `46cb736d61e85daf6af0a4476ffa857c98b06f84d8c6e149b6180ce054d14a5c` |
| 完成父回执 | 10067 bytes；SHA256 `18085ddfc8be6d691c87588ed6ee03a5470f1996588cea0fc0d08f4ca97ce0bf` |
| 父绑定 | `4d3f5dbf2bd02328ba5e7cea47641cd2c21cdc6467950eaee97c2b22d4864222` |
| 实际小输出 | 1795 bytes；SHA256 `f66a9c105c99416515dab6f498a1fcb949ee985e071a20267b246dfabaea1634` |
| 执行 | 2026-11-16 UTC，本地只读；退出零；0.103240044 秒 |

本次重算完整小关系、参数作用、Hensel 因子、原 $b_2$ 运输和全部相关整数格指数；不重复原大求解，不借尚未支付的有理或整数来源作结论。原无穷维 ISP 与其它 Bell 支路不由本篇的有限原目标模呈示自动解决。

根代理另以[独立相对整数格审计](../notes/2026-11-16-r150-original-joint-m-independent-extension-relative-lattice-audit-789f.py)复核本篇关键扩张：直接把原 $h_*$ 代入完整 $2I+X$，不用 Hensel 因子生成 $h_*S_2$；分别求环境内的完整整数格基，构造并逐项乘回相对格的包含矩阵，再作整数 Smith。它独立得到上列 $S_2/hS_2$、$S_2/B$、$S_2/Rb_2$ 的全部类型；原 $b_2$ 在关系格基中的准确分母给阶恰 $31$，在 $pS_2+hS_2$ 格中的分母再次给 primitive 门。实际退出零，用时 $0.042022612$ 秒。源码 5331 bytes，SHA256 `34166331a40236728da142794d4c50f136cab702b3826ffe96b7e0b4ba4be062`；临时输出 948 bytes，SHA256 `f443448b600526ca836b92fd7663b09f83d7edc3f3e4c785b70ac23bc82bf95a`。这里只保存[执行身份](../notes/2026-11-16-r150-original-joint-m-independent-extension-relative-lattice-execution-789f.json)，不保存数学数组。

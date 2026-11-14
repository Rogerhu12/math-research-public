# R1：已引用反例与完整 ISP 的分离；尾部在有限支撑扰动下的保持

**状态：已证明的中间结论。** 本文件不解决完整 Hilbert ISP，不声称下列初等观察具有文献新颖性。

会话：Astra-ISP-b382c564。日期：2026-11-12（UTC+8）。

## 1. 可分解模型已经具有普通约化子空间

设 $(X,\mu)$ 是概率空间，存在 $0<\mu(E)<1$ 的可测集 $E$，$K\ne0$ 是 Hilbert 空间。设 $x\mapsto S_x\in B(K)$ 是本质一致有界的强可测算子场，在

$$H=L^2(X,\mu;K)$$

上定义 $(Sf)(x)=S_xf(x)$。则

$$H_E=\{f:f=0\text{ a.e. on }X\setminus E\}$$

是非零真闭 $S$-约化子空间。

**证明。** $P_Ef=\mathbf1_E f$ 是正交投影，$P_ES=SP_E$。$E$ 及其补集都具有正测度，因此分别取常向量乘其示性函数可知 $P_E\ne0,I$。由 $P_E=P_E^*$ 对交换关系取伴随，亦得 $P_ES^*=S^*P_E$。证毕。

特别地，2026 年 *Backward intertwiners and a transitive commutant* 的模型

$$H_0=L^2(\mathbb Z_2;\ell^2(\mathbb Z)),\qquad
(Sf)(x)=S_xf(x),\qquad S_xe_j=\beta_j(x)e_{j+1}$$

仅由这一形式就具有上述非平凡约化子空间；无需使用该文最困难的纤维不变格分类或超不变子空间结论。可取 $E=2\mathbb Z_2$，其 Haar 测度为 $1/2$。

该文讨论的“没有超不变子空间”要求子空间同时不变于**全部**与 $S$ 交换的算子。这与上述结论相容：$P_E$ 与 $S$ 交换，并不使 $P_EH$ 自动不变于交换子的其他所有元素。

## 2. 尾部、有限支撑扰动与单生成子代数

仍设 $K=\ell^2(\mathbb Z)$，并设 $S_xe_j=\beta_j(x)e_{j+1}$，权有界。对 $h\in\mathbb Z$ 记

$$M_h=L^2\!\left(X;\overline{\operatorname{span}}\{e_j:j\ge h\}\right),\qquad P_h=P_{M_h}.$$

则每个 $M_h$ 是非零真闭 $S$-不变子空间。

**证明。** $P_h$ 是按坐标截断的有界正交投影，故其像闭。常场 $e_h$ 属于其像，而常场 $e_{h-1}$ 属于其正交补，两者非零。$S$ 只把第 $j$ 坐标移到 $j+1$，故 $S M_h\subset M_h$。证毕。

更一般地，对任意 $F\in B(H)$，只要

$$F M_h\subset M_h,$$

则 $M_h$ 也是 $S+F$ 的不变子空间。以下是两个可直接检验的充分条件：

1. $F=u\otimes v$，即 $Fz=\langle z,v\rangle u$（内积对第一变量线性），且 $v\in M_h^\perp$；此时 $F|_{M_h}=0$。
2. $\operatorname{Ran}F\subset M_h$。

若 $F=\sum_{k=1}^r u_k\otimes v_k$，并且所有 $v_k$ 在整数坐标方向的支撑都有共同有限上界，则取更大的 $h$，条件 1 对每一项成立。因此，向模型加入任意这样有限坐标支撑的有限秩扰动，仍不能得到完整 ISP 的反例。类似地，若所有 $u_k$ 的支撑都有共同有限下界，则条件 2 给出一个不变尾部。

这里的“有限坐标支撑”是对 $\ell^2(\mathbb Z)$ 指标的限制，并不要求 $L^2(X)$ 方向有限维；也没有声称一般有限秩或紧扰动都保持一个尾部。

此外，令 $\mathcal A=\operatorname{Alg}_{\rm WOT}(S,I)$。则每个 $A\in\mathcal A$ 都保持每个 $M_h$。

**证明。** 多项式 $p(S)$ 保持 $M_h$。若网 $p_i(S)\to A$ 于 WOT，对 $x\in M_h$、$y\in M_h^\perp$，

$$\langle Ax,y\rangle=\lim_i\langle p_i(S)x,y\rangle=0.$$

因此 $Ax\in M_h$。证毕。

所以，在这个 $S$ 的多项式或其 WOT 闭包中选择单个算子，不能把其传递交换子所给出的**多算子**结论转成完整 ISP 反例。

## 3. 有限因子的标准表示中，因子外的不变投影可以显式构造

设 $(\mathcal M,\tau)$ 是带忠实正规归一化迹的有限 von Neumann 代数，$a\in\mathcal M$ 非中心。令 $H=L^2(\mathcal M,\tau)$，$L_a,R_a$ 分别为左乘、右乘 $a$。则

$$K_a=\ker(L_a-R_a)$$

是 $L_a$ 的非零真闭不变子空间，并且其正交投影 $P_{K_a}$ 不属于左乘代数 $L(\mathcal M)$。

**证明。** 在稠密子空间 $\mathcal M\subset H$ 上，

$$\|ab\|_2\le\|a\|\,\|b\|_2,\qquad
\|ba\|_2\le\|a\|\,\|b\|_2.$$

第二式利用迹性；因此左右乘都唯一延拓为有界算子，且由稠密性保持 $L_aR_a=R_aL_a$。其差的核闭，且 $1\in K_a$，所以非零。又有

$$(L_a-R_a)L_a=L_a(L_a-R_a),$$

所以 $L_aK_a\subset K_a$。若 $K_a=H$，则对每个 $b\in\mathcal M$ 都有 $ab=ba$，与非中心性矛盾。

若 $P_{K_a}=L_b$，由于 $1\in K_a$，有 $b=L_b1=P_{K_a}1=1$，从而 $P_{K_a}=I$，亦矛盾。证毕。

在有限因子中，非零拟幂零元素 $a$ 必非中心：中心只有标量，而非零标量的谱半径非零。因此此命题适用于 README 所述有限因子拟幂零例子的标准表示。即使没有因子**内部**的非平凡不变投影，$B(L^2(\mathcal M,\tau))$ 中仍有上述不变投影。

还可更直接取任意非平凡投影 $p\in\mathcal M$：右乘正交投影 $R_p$ 与每个 $L_a$ 交换，给出普通约化子空间 $L^2(\mathcal M)p$。这同样不要求不变投影属于指定的左乘因子。

## 4. 文献定位与尚未做到的事

- OpenAI, *Backward intertwiners and a transitive commutant*, 2026-09-27，固定提交 `1581d4cbdd69a0faf34b2089614fe2a814316a6a`；Theorem 1.1 给出模型，§6.1 明确列出普通不变尾部。[原文及源文件](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026)。
- OpenAI, *Invariant-projection counterexamples for every irrational rotation*, 2026-09-27，同一提交。[原文](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026)。本文件不依赖其反例定理，仅证明适用于有限因子标准表示的一般命题。
- [Lean 范围说明](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/293.md) 与 `ComparatorChallenges` 中的陈述须区分；本会话没有运行或声称运行这些结果的完整 Lean 证明。

尚未得到：一般 $T$ 的非平凡不变子空间，或一个没有这种子空间的算子。特别是一般无界坐标支撑的有限秩扰动，以及将 $S$ 与其后向交换算子混合后的单算子，不由上面的尾部论证覆盖。

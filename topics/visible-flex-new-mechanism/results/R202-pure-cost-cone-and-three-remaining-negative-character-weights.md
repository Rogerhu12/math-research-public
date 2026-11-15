# R202：真实 pure 成本闭锥及仅剩的三个负字符权

日期：2026-11-15。**完整纸面定理，无新研究计算。** root 推导，tail_cost 独立核对闭包、商表示与排除范围。使用 [R127](R127-positive-affine-character-of-the-fourth-cost-cone.md)、[R145](R145-true-curvature-reflection-and-even-positive-characters.md)、[R188](R188-no-nonzero-positive-affine-character-at-weight-minus2.md)、[R190](R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md) 和 [R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md)。

R196 已严格分离完整 canonical 成本闭锥；R201 又证明其已知正字符无法从任何 universal pure 输出恢复。因此，完整成本与 pure 成本的正性问题必须分别处理。本稿给后者一个准确的有限权判据，不重复已完成的完整权零正性，也不宣称 pure 成本闭锥已等于全空间。

## 1. 真实对象及不能省去的闭包

采用 R105/R127 的同一 canonical 目标、共同右锚、零传入标量历史与完整相位成本。固定一个 scalar 常值 germ、首末 frame 为 I，定义

$$
\mathcal S=\{V_B:B\text{ 是实际有限同端口路径， }M_B=T_B=0\},
\qquad U=\operatorname{span}_{\mathbb R}\mathcal S,
$$

$$
A=\operatorname{cone}(\mathcal S),\qquad C=\overline A\subset U.
\tag{1}
$$

所有闭包均在有限维真实算子空间中取。令

$$
\pi:U\longrightarrow P:=\pi(U),\qquad \pi V=V_{-4},
$$

其中右边保留整个 universal 单 profile 四次算子，不是一个预选 profile 或有限幂尾的评价。定义

$$
\boxed{C_{\rm p}:=\overline{\operatorname{cone}(\pi\mathcal S)}
=\overline{\pi A}=\overline{\pi C}.}
\tag{2}
$$

最后一个等号须证明：由 $A\subset C$ 得 $\pi A\subset\pi C$；若 $x\in C$，存在 $a_n\in A$ 趋于 x，连续线性映射给 $\pi a_n\to\pi x$，故 $\pi C\subset\overline{\pi A}$。两边再取闭包即得 (2)。本稿**没有**假定闭凸锥的线性像 $\pi C$ 本身闭。

由于 $\operatorname{span}\mathcal S=U$ 及 $\pi$ 到 P 满射，

$$
\operatorname{span}C_{\rm p}=P.
\tag{3}
$$

因此其正对偶锥

$$
C_{\rm p}^*=\{\ell\in P^*: \ell(C_{\rm p})\ge0\}
$$

是 pointed：若 $\ell$ 与 $-\ell$ 同在其中，$\ell$ 在 $C_{\rm p}$ 及其线性 span P 上都为零。

## 2. 纯投影与完整仿射表示相容

正仿射 profile 输运只改变共同坐标、jets 与右原函数，不改变相位 Fourier 槽。因此它与取 $-4$ 模式交换。R105/R127 的真实作用下降为 P 上的可逆作用：

$$
\pi\mathsf P_{H,d}=\mathsf P^{\rm p}_{H,d}\pi,
\qquad H>0, d\in\mathbb R.
\tag{4}
$$

由 C 的仿射不变性和 (2)，

$$
\mathsf P^{\rm p}_{H,d}C_{\rm p}=C_{\rm p}.
\tag{5}
$$

令 $D_H^{\rm p}=\mathsf P^{\rm p}_{H,0}$，$T_d^{\rm p}=\exp(dN_{\rm p})$。完整有限 Laurent 表示下降给

$$
P=\bigoplus_\sigma P_\sigma,\qquad
P_\sigma=\pi(U_\sigma),\qquad
D_H^{\rm p}|_{P_\sigma}=H^\sigma,
\qquad N_{\rm p}P_\sigma\subset P_{\sigma-1}.
\tag{6}
$$

特别地 $\pi N=N_{\rm p}\pi$。R190 给 U 的真权支撑在 $[-9,3]$，P 的支撑是其子集。

R145 的真实曲率反号在算子上等于 Laurent 表示于 $H=-1$ 的代数 involution $\mathsf S$；它保持输入颜色和全部相位槽。故它也与 $\pi$ 交换，P 上的 involution 在权 $\sigma$ 上为 $(-1)^\sigma$，并保持 $C_{\rm p}$。这里不把右锚改成左锚，不把真实 h 取负，也不以 profile 镜像代替已付的真实几何反号。

C 的端口无关性传到 (2)，所以 $C_{\rm p}$ 同样不依赖选取的 scalar germ。与 R127 一样，这一 universal 闭锥没有附加统一总长、控制盒、reach 或预给窄物理区间的限制。

## 3. 对偶的准确拉回与下降

$\pi$ 满射给一个单射

$$
\pi^*:P^*\hookrightarrow U^*,\qquad \ell\longmapsto\lambda=\ell\pi.
$$

其像准确是 $\operatorname{Ann}(\ker\pi)$。由 (2)，

$$
\boxed{\pi^*(C_{\rm p}^*)=C^*\cap\operatorname{Ann}(\ker\pi).}
\tag{7}
$$

一方向显然：若 $\ell\ge0$ 于 $C_{\rm p}$，则 $\ell\pi\ge0$ 于 C 且杀掉 $\ker\pi$。另一方向，若 $\lambda\in C^*$ 且 $\lambda|_{\ker\pi}=0$，可准确定义 $\ell(\pi u)=\lambda(u)$；这与原像选择无关，在 $\pi C$ 上非负，有限维连续性使它在闭包 $C_{\rm p}$ 上非负。

由 (4)，拉回保持单一真权和平移不变性。反之，对一个杀掉纯核的完整仿射字符，其唯一下降的 $\ell$ 也有相同权并满足 $N_{\rm p}^*\ell=0$。

令 $R=\mathcal R_8$ 为完整响应空间。[R120](R120-G-lineality-of-the-closed-fourth-cost-cone.md) 给 $R\subset C\cap(-C)$。因此

$$
\pi R\subset C_{\rm p}\cap(-C_{\rm p}),
\qquad \ell(\pi R)=0\quad(\ell\in C_{\rm p}^*).
\tag{8}
$$

(7) 是本稿区别 pure 正性与完整正性的关键。完整正字符非零并不足以给 pure 正字符；它必须先准确消掉整个 $\ker\pi$。

## 4. 真子锥必有单权平移不变的正字符

若 $C_{\rm p}\ne P$，闭凸锥分离给 $0\ne\ell_0\in C_{\rm p}^*$。可以直接在 (3)、(5)、(6) 上应用 R127 的证明。为明确没有遗漏商上的步骤，复述如下。

先对 $\ell_0$ 作真权分解，令 m 是最高非零权。利用 $H\to+\infty$ 的正归一极限，得到非零单权 $\ell_m\in C_{\rm p}^*$。再取最大的 j，使

$$
\nu=(N_{\rm p}^*)^j\ell_m\ne0.
$$

$N_{\rm p}$ 幂零，所以 $N_{\rm p}^*\nu=0$。两向平移 $d\to\pm\infty$ 的最高项分别给 $\nu$ 和 $(-1)^j\nu$ 为正泛函；pointed 性迫 j 为偶数。因此 $\nu\in C_{\rm p}^*$ 非零，且它的最后真权是 $a=m+j$，不是仍写作 m。

于是

$$
\nu\circ\mathsf P^{\rm p}_{H,d}=H^a\nu,
\qquad \nu(C_{\rm p})\ge0,
\qquad \nu\ne0.
\tag{9}
$$

其完整拉回 $\lambda=\nu\pi$ 非零，是 U 上同权的真实正仿射字符，杀掉 R 及 $\ker\pi$。所有已有的**完整**正字符排除定理因此适用于它。

## 5. 逐项排除及剩余权

R190 的支撑与 R145 的真实反号首先把 (9) 的权限制为

$$
 a\in\{-8,-6,-4,-2,0,2\}.
$$

奇权的排除也可直接看出：若 a 奇，则对 $z\in C_{\rm p}$，其反号像仍在锥中，但 $\nu(\mathsf S_{\rm p}z)=-\nu(z)$，故 $\nu$ 在整个锥及 P 上为零，矛盾。

还可排除三个偶权。

- **权 $+2$。** R190 的完整原式结论是 $U_2=R_2$。拉回 $\lambda$ 杀 R，又只支持权2，故恒零。
- **权 $-2$。** R188 已排除了该权的全部非零完整正仿射字符；拉回 (9) 正是其定义范围。
- **权 $0$。** R201 已证明 $\pi U_0=\pi R_0$，维数为3。对每个 $u\in U_0$ 可取 $r\in R_0$ 使 $\pi u=\pi r$，于是 $\lambda(u)=\nu\pi u=\nu\pi r=0$。单权拉回因此在整个 U 上为零。这里不需要重新求完整 H0，也不需要再检验权零 action。

得到

$$
\boxed{C_{\rm p}\ne P\quad\Longrightarrow\quad
\text{存在权 }a\in\{-8,-6,-4\}\text{ 的非零 pure 正仿射字符。}}
\tag{10}
$$

等价地，存在一个这三个权之一的非零完整正仿射字符 $\lambda$，并且 $\lambda|_{\ker\pi}=0$。

反方向也成立：任一这样的完整字符按 (7) 唯一下降为非零 $\nu\in C_{\rm p}^*$，所以 $C_{\rm p}$ 不可能等于整个 P。因此本稿完整结论为

$$
\boxed{
C_{\rm p}=P
\quad\Longleftrightarrow\quad
\text{权 }-8,-6,-4\text{ 均不存在杀掉}\ker\pi
\text{ 的非零完整正仿射字符。}
}
\tag{11}
$$

本稿没有决定这三个权的任一个是否存在这样的字符。

## 6. R196 的严格正性为什么不能替代 (11)

[R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md) 的权零字符 $\lambda_+$ 确实对每个非空真实零矩成本满足严格正性公式

$$
\lambda_+(V_B)=L+\int (h_s/h)^2\,ds>0.
$$

这使完整 C 为真子锥。R201 同时构造了真实向量 $H\in U_0$，使

$$
\pi H=0,\qquad\lambda_+(H)=1.
$$

所以 $\lambda_+$ 不属于 (7) 的右边，不能下降到 P。两项结论完全相容：一个线性投影可能丢掉完整锥的分离方向。上述 H 只是真实线性 span 中的向量，未声称它本身由一条实际成本路径实现。

[R199](R199-faithful-monotone-step-for-the-complete-universal-pure-space.md) 的新单调末 step 对整个 P 忠实，但仍不能恢复 $\ker\pi$ 中已经丢掉的量。因此 faithful step 也不能把 $\lambda_+$ 变成 pure 障碍；其准确必要门仍是 universal pure 成本为零。

## 7. 对下一实际子问题的限定

对每个候选权，可以先考虑纯投影的平移头部

$$
H^{\rm p}_a=P_a/(\pi R_a+N_{\rm p}P_{a+1}).
\tag{12}
$$

任何 (9) 必须在相应头部上给非零泛函。若能证明某个 (12) 为零，就直接排除该权，不必重做完整正性。若头部非零，仍须在完整真实路径上检验正性，不能把有限查询对偶或单个 profile 上的符号当作正字符。

R201 已付的是**整个**权零 pure 像等于响应像，不只是一个尾项。相同类型的新原式成员问题可以消费已有完整原呈示；应只处理未付的 pure 投影，复用已证的关系，不重新编译已完成的完整空间。

此外，即使某个非候选权的 pure 像已在响应像内，它仍可能有助于实际构造中的全函数匹配；“不可能有正字符”和“已给出全部响应的准确有限参数实现”是不同问题。当前权−2存量呈示的新pure成员门属于后者的准备工作，不是重做 R188。

## 8. 与真实 hook 路径的关系及尚欠事项

若 B 仅满足 M0、同端口/frameI，而第三算子为 $T_B=\kappa\mathfrak H$，不能直接用 (1) 的定义宣称其成本在 U。R83/R84 的真实倒行给 $T_{B^{\rm rev}}=-T_B$、$V_{B^{\rm rev}}=V_B$；两块零矩使传递交叉项消失，故

$$
M_{BB^{\rm rev}}=T_{BB^{\rm rev}}=0,
\qquad V_{BB^{\rm rev}}=2V_B.
$$

因此 $V_B\in A\subset C$，其 pure 成本属于 $C_{\rm p}$。这只证明锥归属，不把正半倍当作实际控制操作，也不把真倒行当负第四成本。即使 (10) 存在一个非零正字符，要据此排除某个具体 B，仍须另外证明它在该 B 上严格为正；非负本身不足以排除零 pure。

最后，若将来 (11) 的右边全部排除，只得到闭凸锥 $C_{\rm p}=P$。它不自动提供一个非空有限词的准确 pure 零成本，不提供成本逆元，不提供固定总长/控制盒/共同窄 I 内的可达性，也不支付独立二阶 gauge 下的全区间 period/ruling、第五阶以上、同 g 的收敛、闭嵌入、全时间 reach 或 README 的宏观幅度门。零向量本来就在凸锥中，不能把它冒充所需的非平凡实际几何。

# 第 25 阶前的准确结构：R88 余因子、正交余场与理想互反对

日期：2026-11-14。本稿是 R85/R88 后续的纸面结构记录，不给一般真实闭环的第四符号，也不把理想无桥模型当作可直接拼接的真实路径。没有在本地编译、展开或求值第 25 阶研究目标。

## 1. R88 的原式差有一个明确纯几何因子

沿用 R88 的记号，$p=2m-3,r=3m-6,n=4m-9$，并令

$$I_0=u_0+\frac{a_{mp}}{2a_{mm}}b_0^2,
\qquad f=\frac{Q(s,c)}{8h^2},$$

$$\mathcal C=\frac{KQ}{8h},\quad\mathcal D=\frac{Ke}{4},\quad
E_{mr}=(mr-a_{mr})\partial_c\mathcal C
+\left(\frac{a_{mr}}{n+1}-mr\right)\mathcal D.$$

如果暂时不把零初值给出的 $I_0=0$ 代入，R88 同一推导实际上得到

$$\boxed{[t^{n+1}]\widetilde W_{4,s}
-\partial_s(\alpha_m b_0^2b_1+\beta_m b_0u_1)
=I_0\left(\frac{E_{mr}}4+\frac{mr}{8}f_{ss}\right).} \tag{1}$$

这里仍使用真实 ODE 的 $I_0'=0$。核对方法不需要新的 forcing 展开：R88 式 (12) 用 $u_0=-a_{mp}b_0^2/(2a_{mm})+I_0$ 时多出 $E_{mr}I_0/4$；从正交规范转回原 completed scalar 的势另外多出 $(mr/8)f_sI_0$。对它取真实导数即得 (1)。

对 $m=8$，该纯几何因子明确是

$$\boxed{18f_{ss}-\frac{3456}{23}\partial_c\mathcal C
-\frac{1299}{46}\mathcal D.} \tag{2}$$

所以公开结构消费程序的首一除法并非没有目标的拟合：若一般原式身份成立，其商应准确等于 (2)。原始所有状态仍保留；只有已证第一积分及其零初值允许最终消去。

## 2. 正交余场第一次进入再下一阶

取 R88 的两个动态输入 $Y_{a(s)t^i},Y_{b(s)t^j}$，置 $\ell=i+j-3$，并记

$$P_0=\frac{a_{ij}Q(s,c)}{8h}ab,\qquad
v=(1,0,e),\qquad w=(-e,0,1),\quad N=(0,1,0).$$

由准确恢复式，$P=P_0t^\ell+\cdots$，$B=O(t^{\ell+1})$，而
$\psi-W=\lambda P_0t^\ell+\cdots$。因此 R88 正交余分子的首项是

$$\boxed{P_0\left\{z_0N+\frac{e_s(s,c)}{hQ(s,c)}w_0\right\}t^\ell.} \tag{3}$$

其方向也可写为

$$z_0N+\frac{e_s}{hQ}w_0
=\frac1h\left(\nabla_s v_0-\frac{v_0\cdot\nabla_sv_0}{Q}v_0\right),$$

因为 $\nabla_s v_0=(0,hz_0,e_s)$。这是移动正交架中的协变导数，不是对物理分量遗漏框架转动的普通微分。

R88 已用正交性证明该余场不进入前两阶。其导数和两个余场的配对则确实可能从 $t^{i+\ell-1}$ 起进入。应用于 pure 第四链，对应第 $n+2=4m-7$ 阶；$m=8$ 就是第 25 阶。这个阶数结论没有给该项的整体符号，也没有证明其中某个单独平方不能被其他完整 forcing 补偿。

首轮实际完整 DAG 的只读依赖记录也与此相容：第 25 阶根只引用第二的 $t^{13},t^{14},t^{15}$ 三个真实 histories 以及第三的 $t^{18},t^{19},t^{20}$ 三个 histories。第 26、27 阶各再增加一对。此记录仅是已发布图的依赖读取，不是系数化简或周期独立性的结论。

## 3. 理想互反对的首项准确在第 25 阶，而不是第 27 阶

这里纠正前期讨论中一处阶数口算：R65 两个二次因子的最低项来自**局部 $(q'')^2$**，不是尾积分 $A_q$。取 R65 的准确标准化情形 $h=1,d=0$、$c>1$，令

$$t=c-x,\qquad q(x)=A_0t^m\quad(m\ge8)$$

于一个右尾上成立，右方外延零。设 $L=x^2-1,Q=1+x^2$。R65 给

$$\left(\frac{\mathcal P[q]}L\right)'
=\frac{P_1[q]P_2[q]}{64L^2},\qquad
\mathcal P[q](c)=0.$$

其中 $(q'')^2$ 在 $P_1,P_2$ 的系数分别是 $LQ$ 和 $xLQ$；$A_q=O(t^{2m-3})$ 比这些局部项高一阶。故

$$P_1=A_0^2L(c)Q(c)m^2(m-1)^2t^{2m-4}+O(t^{2m-3}),$$

$$P_2=A_0^2cL(c)Q(c)m^2(m-1)^2t^{2m-4}+O(t^{2m-3}).$$

用唯一右锚积分，得到准确首项

$$\boxed{\mathcal P[q](x)=
-\frac{A_0^4\,c(c^2-1)(1+c^2)^2m^4(m-1)^4}
{64(4m-7)}t^{4m-7}+O(t^{4m-6}).} \tag{4}$$

对单位实幅 $A_0=1$，该系数严格负。若两个理想常态各有相同正时长 $T_0$，R65 的 pure 谐波 period 是 $T_0\mathcal P[q]/16$，因此再乘 $T_0/16$。复幅时保留普通四次方，不把它改成 Hermitian 模四次方。

这说明 R85/R88 已自动消去的 $4m-9,4m-8$ 后，下一阶确实可能非零；它也准确校正了把理想对误估为到 $4m-5$ 才出现首项的说法。

## 4. 不能从 (4) 推成一般真实环的结论

(4) 的两常态属于 R65 的**无连接桥理想模型**。真实桥有自己的低阶 histories、局部第四贡献和共同端点条件，不能从两个常态中删去。即使后续真实路径总 $M=\mathcal T=0$，也没有由 (4) 证明它的第 $4m-7$ 系数同号。

下一步应对已经发布的第 25 阶完整 DAG 使用真实 RHS、准确端零势与已有第一积分作等价约简；若留下历史项或局部几何密度，要保其全部系数与端项。非零 density 不等于非零 period，独立 formal states 也不等于可独立选择的真实闭路径数据。

来源：[R65](../results/R65-reciprocal-pure-fourth-drift-complex-uniqueness.md)、[R85](../results/R85-pure-fourth-leading-tail-is-an-exact-derivative.md)、[R88](../results/R88-pure-fourth-subleading-tail-is-an-endpoint-potential.md)，以及 [首轮实际 tail 报告](actions-43635287277-1-pure_tail_period/pure-tail-period.json)。

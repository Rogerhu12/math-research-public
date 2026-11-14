# R92：pure 第四再下一幂尾的三 primitive 二次正规形

日期：2026-11-14。状态：**已证明，一般 $m\ge8$ 的纸面正规形**。本稿给出指定的真实端点势与唯一辅助积分，将 pure 第四第 $4m-7$ 阶的全部第三 histories 准确移除。剩余三变量 action 的具体几何系数由同一 R56 原式定义，公开结构消费程序另负责完整导出；固定 $m=8$ 的计算不代替下面的一般证明。本稿不证明该 action 的符号，也不把非零密度当成非零 period。

## 1. 原始对象与可支付的端点势

沿用 R85/R88 的同一有限光滑真实路径 $s\in[0,L]$，$h>0$、$\omega_s=k_s/(2h)$、首末为常值 scalar germs；固定共同物理右尾 $t=c-\xi$，全路径 $c+\omega$ 有正下界。原第二、第三 histories 取零传入值。取单位尾 $q=t^m$，$m\ge8$，并置

$$p=2m-3,\quad r=3m-6,\quad n=4m-9.$$

记 completed 第二系数为 $b_j=[t^{p+j}]\widetilde W_2$，第三系数为 $u_j=[t^{r+j}]\widetilde W_3$。目标是原第 $n+2=4m-7$ 密度

$$D_2=[t^{n+2}]\widetilde W_{4,s}.$$

以下仍使用真实 ODE、零传入 histories 和常值 scalar 端芽。若整条路径的二阶矩阵 $M=0$，则所有 $b_j$ 的两个端值为零。第一积分

$$I_0=u_0+\frac{a_{mp}}{2a_{mm}}b_0^2=0$$

来自真实 RHS 与初值，不能作为无条件的独立状态代换。

继续记

$$A=a_{mm},\qquad f=\frac{Q(s,c)}{8h^2},\quad
\mathcal C=\frac{KQ}{8h},\quad\mathcal D=\frac{Ke}{4},$$

$$E_{ij}=x_{ij}\partial_c\mathcal C+y_{ij}\mathcal D,
\quad x_{ij}=ij-a_{ij},\quad
y_{ij}=\frac{a_{ij}}{i+j-2}-ij.$$

## 2. 最高两个 histories 的确定性移除

最高第三系数 $u_2$ 只通过 $Y_{u_2t^{r+2}}$ 的最低项进入 $D_2$，其系数是 $a_{m,r+2}\mathcal C/4$。最高第二系数 $b_2$ 与 $b_0$ 的直接配对系数是 $-a_{p,p+2}\mathcal C/8$。

第三 RHS 本身只依赖第二 histories，不依赖任何第三 history。因而定义

$$\beta_2=\frac{a_{m,r+2}}{4A},\qquad
\alpha_2=\frac{\beta_2a_{m,p+2}-a_{p,p+2}/8}{2A},$$

$$F_{\rm top}=\alpha_2 b_0^2b_2+\beta_2b_0u_2, \tag{1}$$

则 $D_2-D_sF_{\rm top}$ 不再含 $u_2,b_2$。这里 $b_0'=A\mathcal C$，而 $u_2'$ 的最高第二项是 $-a_{m,p+2}\mathcal C b_2$；正是这些准确最高项决定 (1)，不是任意势的拟合。

正交余场从本阶开始有真实贡献，但其首项不含 $b_2,u_2$，因此不改变这一最高系数消元。它的贡献全部保留在余密度中。

## 3. 一个真实、端点受 M=0 控制的辅助 primitive

定义

$$J'=\mathcal D,\qquad J(0)=0. \tag{2}$$

它是由同一真实几何唯一决定的积分，不是可任意指定的新自由控制。

为什么 $M=0$ 支付 $J(L)=0$？矩阵为零是完整二阶 profile 算子为零，因而 R85 的最低关系对物理小区间中每个右端 $c$ 都给

$$\int_0^L\mathcal C(s,c)\,ds=0.$$

在同一有限光滑路径下对 $c$ 微分，得到 $\int\partial_c\mathcal C=0$。R88 的第二下一系数满足

$$d=b_1-\frac{m^2}{2}f_s,
\qquad d'=E_{mm}.$$

常值端芽使 $f_s$ 在两端为零；$M=0$ 又使 $b_1$ 两端为零。因此 $\int E_{mm}=0$。因为

$$y_{mm}=-\frac{m^2(3m-5)}{2(2m-3)}\ne0,$$

可推出 $\int\mathcal D=0$，即 $J(L)=0$。

这里使用的是完整 $M=0$，不能只凭某一个固定右尾的一个数值末值为零而对 $c$ 微分。

## 4. 次高第三 history 的准确移除

在 $D_2-D_sF_{\rm top}$ 中，$u_1$ 的准确系数是

$$\frac14E_{m,r+1}+\frac{m(r+1)}8 f_{ss}. \tag{3}$$

这来自 R88 动态幂公式对指数 $(m,r+1)$ 的下一项，再从正交 scalar 转回原 completed scalar。该次的 $u_1',u_1''$ 已由原第三 RHS 表示，它们只依赖第二 histories，所以不再贡献 $u_1$ 本身。

设

$$\lambda_0=\frac{x_{m,r+1}}{4x_{mm}},\qquad
\lambda_1=\frac14\left(y_{m,r+1}
-\frac{x_{m,r+1}}{x_{mm}}y_{mm}\right),$$

$$\lambda_f=\frac{m(r+1)}8-\frac{m^2}2\lambda_0.$$

由于 $b_1'=E_{mm}+m^2f_{ss}/2$，准确有

$$D_s(\lambda_0b_1+\lambda_1J+\lambda_ff_s)
=\frac14E_{m,r+1}+\frac{m(r+1)}8f_{ss}.$$

所以

$$F_{\rm mid}=(\lambda_0b_1+\lambda_1J+\lambda_ff_s)u_1 \tag{4}$$

消除 (3)。其导数的另一项完整保留在新余密度中。$M=0$ 和常值端芽使 (4) 的前一因子在两个端点为零；不要求 $u_1(L)=0$。

对 $m=8$，这些固定有理数是

$$\alpha_2=\frac{6591}{8960},\quad\beta_2=\frac{247}{280},$$

$$\lambda_0=\frac{4199}{4608},\quad
\lambda_1=\frac{45353}{3600},\quad
\lambda_f=-\frac{1463}{144}. \tag{5}$$

## 5. 准确三角正规形与期望输出

最后只用已证 $I_0=0$ 消去 $u_0$。这样

$$D_2=D_s(F_{\rm top}+F_{\rm mid})+\mathcal Q_s(b_0,d,J),
\qquad d=b_1-\frac{m^2}{2}f_s, \tag{6}$$

其中 $\mathcal Q_s$ 是三个真实第二 primitives 的次数至多二的多项式，系数由有限几何 jets 与右端 $c$ 决定。它可以有线性项和纯几何常项，不能先称为正或负二次型。

次数论证来自原 R56 三角结构：第四 forcing 对第二 scalar 至多二次、对第三 scalar 至多一次；第三 RHS 对第二 scalar 至多一次；第二 RHS 不含 histories。式 (1)(4) 的真实导数以及 $u_0=-a_{mp}b_0^2/(2A)$ 均不会把余式提高到三次。辅助 $J$ 只出现在 (4) 的导数余项中，故其依赖也必须准确保留。

三个余变量由同一几何驱动：

$$b_0'=A\mathcal C,\qquad
d'=x_{mm}\partial_c\mathcal C+y_{mm}\mathcal D,
\qquad J'=\mathcal D,$$

且在完整 $M=0$ 时全部为零端值路径。于是原始周期系数准确变成

$$\boxed{[t^{4m-7}]V_4
=\int_0^L\mathcal Q_s(b_0,d,J)\,ds.} \tag{7}$$

式 (7) 仍需真实 $h,k,\omega$、共同物理域和端点约束。不能把 $b_0,d,J$ 当作任意独立函数来判断可达的正负；也不能因某个未积分系数非零就宣布 period 非零。

式 (6) 也明确规定了余式的构造：从完整原 density 减去两个指定势的真实导数，以已证 $I_0=0$ 代换 $u_0$，再将 $b_1$ 写成 $d+m^2f_s/2$。这给一个准确有限表达式；没有借用未完成的 Volterra word 独立性，亦没有先选择某个几何路径。

独立公开消费程序会直接读首轮已发布完整 DAG，逐项检查最高 histories 消除、已证第一积分除法、(6) 的准确回代及二次次数，并把 $\mathcal Q_s$ 的全部具体系数保存为压缩证书。它不重新编译 forcing、不置内部状态为端值。此计算的作用是原式交叉核与系数导出；本稿的一般 $m$ 结论由上述三角结构、明确系数和端点证明成立，不以固定 $m$ 的运行结果作为证明前置。

**严格范围。** (7) 是一个真实 period 的等价积分表示。它不是新的零成本环，不证明 $\mathcal Q_s$ 正定、负定或非零，不证明三条零端路径可任意独立指定。完整 $M=0$、共同物理区间和真实几何关系缺一不可。完整第三总算子 $\mathcal T=0$ 并非本系数约简所需条件；其他第四谐波、更高幂和完整 $P_0$ 仍未支付。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R85](R85-pure-fourth-leading-tail-is-an-exact-derivative.md)、[R88](R88-pure-fourth-subleading-tail-is-an-endpoint-potential.md)。


实现及公开命令见[独立结构消费说明](../notes/pure-tail-third-history-elimination-20261114.md)。首轮实际结构是[完整 tail 报告](../notes/actions-43635287277-1-pure_tail_period/pure-tail-period.json)，第 25 阶没有因旧可读文件省略而被解释为零。

## 6. 已完成的固定 m=8 原式导出

公开 Actions [43637739532](https://github.com/Rogerhu12/math-research-public/actions/runs/43637739532)，source 09bbfd75df20e48dca2938e5728943984b4ba963，已完整完成14.309952249秒，峰值RSS122.14453125 MiB。没有重编forcing或求值一条新几何路径。原14条历史加唯一真实J共15条全部保留，指定端势移除全部第三及最高第二历史；真实第一积分导数/初值、完成坐标往返以及fresh原DAG恒等式均准确为零。

剩余action共有2172个规范单项，确为三坐标总次数2；非零分组为常项1375项，J与d各218项，b0为146项，Jb0与b0d各38项，Jd与d平方各61项，b0平方17项，没有J平方项。这些分组是完整几何系数的记录，既不是正负号证明，也不是周期不为零的证书。它们为后续在真实驱动约束下作准确分部积分和符号研究提供输入。

| 公开文件 | 字节 | SHA256 |
|---|---:|---|
| [pure-tail-next-action.json](../notes/actions-43637739532-1-pure_tail_next_reduce/pure-tail-next-action.json) | 5070 | 7ccacc20eff6c30df0414c9d93bd54c80f1cbdb513a9b6d189b219834d08a3c7 |
| [pure-tail-next-action-expressions.json](../notes/actions-43637739532-1-pure_tail_next_reduce/pure-tail-next-action-expressions.json) | 84841 | d2e4bb4bfe53d6e5908066b681c61c64b7b3f85f9cba2ca8c94233a5961d10df |
| [pure-tail-next-action-certificate.json.gz](../notes/actions-43637739532-1-pure_tail_next_reduce/pure-tail-next-action-certificate.json.gz) | 52538 | a9ac0330f49df738aebab8c85f845ed0aedb3f3063a80603afcdcf4b09d58092 |

完整压缩证书解压581665 B，SHA256 f3094ac25e631978ff129795128e8207edded409d78c8851a5f07c42c8db358d，保留全部系数与扩展DAG。可读展开84841 B的省略标记只影响人读版本，完整结构没有丢项。一般m的定理由前文纸证给出，本次m=8导出不扩大为完整第四符号或主课题完成。

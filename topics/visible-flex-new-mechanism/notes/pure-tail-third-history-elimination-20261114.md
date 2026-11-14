# 再下一幂尾的三角约简：移除全部第三 histories

日期：2026-11-14。独立纸面正规形；准确系数由另建的公开 DAG 消费程序检验和输出。这里不给余下 action 的符号，不把非零密度当成非零 period。

## 1. 原始对象与可支付的端点势

沿用 R85/R88，取单位尾 $q=t^m$，$m\ge8$，并置

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

独立公开消费程序将直接读首轮已发布完整 DAG，逐项检查最高 histories 消除、已证第一积分除法、(6) 的准确回代及二次次数，并把 $\mathcal Q_s$ 的完整系数保存为压缩证书。它不重新编译 forcing、不置内部状态为端值，也不把形式消元失败当作一般不存在结论。具体 action 系数与其任何符号判断以这一步实际输出和后续证明为准。

来源：[R56](../results/R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R85](../results/R85-pure-fourth-leading-tail-is-an-exact-derivative.md)、[R88](../results/R88-pure-fourth-subleading-tail-is-an-endpoint-potential.md)。

## 6. 独立公开消费入口

新增 `scripts/literature_pure_tail_next_reduce.py`，导入原 tail 编译器的系数代数及 R88 消费器的字节绑定、节点重建和准确首一除法，不调用任何 `forcing_range` 或研究编译函数。输入仍是首轮已发布的完整结构，而不是可读输出中被省略的系数。

```bash
python topics/visible-flex-new-mechanism/scripts/literature_pure_tail_next_reduce.py \
  --check-only --out "$VISIBLE_OUT/pure-tail-next-development.json"
python topics/visible-flex-new-mechanism/scripts/literature_pure_tail_next_reduce.py \
  --report topics/visible-flex-new-mechanism/notes/actions-43635287277-1-pure_tail_period/pure-tail-period.json \
  --structure topics/visible-flex-new-mechanism/notes/actions-43635287277-1-pure_tail_period/pure-tail-period-structure.json.gz \
  --out "$VISIBLE_OUT/pure-tail-next-action.json" --max-seconds 240
```

程序只新增一条明确记录的实际 ODE $J'=\mathcal D$，所以总 genuine histories 从 14 变为 15。原始 14 条既不重置也不更换。减去 (1)(4) 的真实导数，再除去已证第一积分后，程序检查剩余状态只属于原第二前两条与这个辅助 $J$；任何意外的高阶状态都会原样保留、标记正规形未通过，而不是删去。

随后把原 raw 第二坐标准确改写为 $(b_0,d,J)$，保存双向替换并重新代回原多项式。独立 memo 表再从原 DAG 的密度、势导数与第一积分展开，要求完整 action 身份为准确零。只有这些都通过且总次数至多二，主报告才给 `verified_three_primitive_quadratic_normal_form=true`。

完整压缩证书包含扩展 DAG、原/新增 state RHS、端点势根、第一积分商、每个 history 单项式的全部几何系数。另有低于 95KB 的可读系数；任何截断明确标记，完整数据不丢。非零 action 仍不作为非零 period 或符号证明。

本地只跑人工三角 ODE 制造的准确 action，覆盖真实导数/初值、首一约简、完成坐标往返、fresh 回代，以及故意加入一条第三 history 后必须拒绝正规形的负例。没有读取实际 tail 结构作研究代数。

# Phi 两条原权曲线的真实下界与完整 639 次模型

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）  
范围：当前 unit211、$\Phi=0$、物理 $D\ne0$ 图。  
状态：$T_0$ 曲线十四阶、$\ell$ 曲线二十一阶的完整 QQ 下界已付；两次唯一运行均在 120 秒时停止，未完成精确目标，原门冻结。

## 1. 完成的结论及保留的边界

仍以 $F=\det C_{22}\in\mathbb Q[u,Q]$ 表示原 729 次缩减权多项式，令
$$
\phi_T=Q+4u-4=-T_0,\qquad
\phi_\ell=Q-2(u-1)(u-2)=Q\ell.
$$
本次完成
$$
\phi_T^{14}\mid F,\qquad
\phi_\ell^{21}\mid F
\quad\text{于 }\mathbb Q[u,Q].
\tag{1.1}
$$
准确次数范围仅为
$$
14\le\operatorname{ord}_{\phi_T}F\le16,\qquad
21\le\operatorname{ord}_{\phi_\ell}F\le25.
\tag{1.2}
$$
这里没有声称十六阶或二十五阶已经完成。

结合[精确 $u^4$ 因子](R150-appendix-unit211-Phi-zero-exact-u-four-factor-and-complete-integral-weight-model-725.md)和[真实 $(u-1)^{30}$ 下界](R150-appendix-unit211-Phi-zero-u-minus-one-thirtieth-factor-695-model-and-frozen-memory-boundary.md)，得到唯一多项式 $F_2$：
$$
F=u^4(u-1)^{30}
   (Q+4u-4)^{14}
   \bigl(Q-2(u-1)(u-2)\bigr)^{21}F_2,
\tag{1.3}
$$
且
$$
\deg_uF_2=\deg F_2(u,2)
=\deg\overline{F_2}(u,2)=639.
\tag{1.4}
$$

四个因子都是互不相伴的不可约首一因子（两个对 $u$ 首一、两个对 $Q$ 首一），故在 $\mathbb Q[u,Q]$ 中两两互素。它们的有限交点不会妨碍 (1.3)。所有这些因子也已是原物理权单位；这里只剥已经实际证明的 QQ 幂次。

## 2. 两条完整原横截面

在第一条曲线上取
$$
t=\phi_T,\qquad Q=4-4u+t,
$$
在第二条曲线上取
$$
t=\phi_\ell,\qquad Q=2(u-1)(u-2)+t.
$$
二者都是整个多项式环的可逆坐标替换，不是单点特化。系数域均为 $K=\mathbb Q(u)$。

工作词典序把原 $Q$ 放在第一变量，使相应 $\phi$ 是原生多项式短除中的首一除式。每次运行先完成 $484$ 个原曲线常数项的整式返回。需要后继轮时才构造完整高阶输入：

- $\phi_T$ 使用模 $t^{17}$ 的全部系数；
- $\phi_\ell$ 使用模 $t^{26}$ 的全部系数。

两次运行各自完成 $484$ 个首一高阶短除返回和 $484$ 个反向坐标平移返回。没有执行其他横截面或重复旧行列式、旧模分解、旧无穷核门。

## 3. 每轮原行变换与实际下界

每轮的增广行消元及后续选中原行替换均在 $K$ 上可逆。每个实际主元非零；完整行内容只作为系数域标量约除，不称物理单位。每轮先后返回旧增广关系和替换后的实际关系，共 $968$ 个坐标。

若出现 $r$ 条零常数行，则对其全部已保留系数逐项除 $t$，并完整返回系数移位。当前精度 $N$ 每轮减一，累计提取次数 $e$ 增加 $r$，始终满足初始目标所需的
$$
e+N\ge17\quad\text{或}\quad e+N\ge26.
\tag{3.1}
$$

### 3.1 整 $T_0=0$ 曲线

| 轮次 | 输入精度 | 输入累计次数 | 实际秩 | 零行数 | 输出累计次数 | 输出精度 |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 17 | 0 | 11 | 11 | 11 | 16 |
| 2 | 16 | 11 | 19 | 3 | 14 | 15 |

两轮完成 $1936$ 个常数变换坐标和 $308$ 个零行截断返回。第二轮完整阶段在源计时 $53.759156602$ 秒输出，下一常数矩阵 SHA256 为
`cfccc8f7a841904faaf367a9c59d3e376d6595e1cf452cc71fbee0d09719570f`。
所以 $\operatorname{ord}_{\phi_T}F\ge14$ 已经完整证明。

### 3.2 整 $\ell=0$ 曲线

| 轮次 | 输入精度 | 输入累计次数 | 实际秩 | 零行数 | 输出累计次数 | 输出精度 |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 26 | 0 | 11 | 11 | 11 | 25 |
| 2 | 25 | 11 | 17 | 5 | 16 | 24 |
| 3 | 24 | 16 | 17 | 5 | 21 | 23 |

三轮完成 $2904$ 个常数变换坐标和 $462$ 个零行截断返回。第三轮完整阶段在源计时 $27.101247081$ 秒输出，下一常数矩阵 SHA256 为
`b7d42dbe7918f18d486d57b35c5628d6735ec98664dd861139856002a46af86b`。
所以 $\operatorname{ord}_{\phi_\ell}F\ge21$ 已经完整证明。

这些下界先在 $K[Q]$ 中成立。两条 $\phi$ 均对 $Q$ 首一，故全部整除自动还到 $\mathbb Q[u,Q]$，保留所有系数域主元为零的复 $u$ 纤维。未完成的后继轮不影响以上已付下界，也不提供任何额外阶数。

## 4. 整性、保度与剩余分量

原 $F$ 的系数在 $1009$ 整。连续的首一因子短除保持整性，故 $F_2$ 也在 $1009$ 整。新增两个因子的总 $u$ 次数是
$$
14+2\cdot21=56,
$$
所以从已付 695 次模型得到 639 次。

在 $Q=2$ 时，这两个因子的 $u$ 最高系数贡献
$$
4^{14}(-2)^{21}\equiv201\pmod{1009}.
$$
因此
$$
[u^{639}]\overline{F_2}(u,2)
=702\cdot201^{-1}\equiv636\ne0.
\tag{4.1}
$$
这给 (1.4) 的真实 QQ 次数与模保度。令
$$
\mathcal O=\mathbb Z_{(1009)}[Q]_{(1009,Q-2)},\qquad
\gamma_2(Q)=[u^{639}]F_2,
$$
则 $\gamma_2$ 是 $\mathcal O$ 的单位，
$$
\mathcal O[u]/(F_2/\gamma_2)
\tag{4.2}
$$
是完整秩 $639$ 的有限自由权模型。

$\phi_T$ 的原模分量尚余两重；$\phi_\ell(u,2)$ 的两个不同模根各尚余四重；$u-1$ 仍余此前未支付的九重。其余原单位坏块与首项坏块也全部保留。不得将任何这些模重数删除，或把局部好块当作整个特征零商。

本条不排除尚未支付的 $\lambda,T,z$ 纤维，不宣称整 Phi 或普通不变子空间问题完成。

## 5. 两次唯一执行与冻结记录

源和输入：

- [整 $T_0=0$ QQ 源](../notes/2026-11-28-unit211-Phi-zero-reduced-original-matrix-local-T-zero-extraction-8542.py)及[输入说明](../notes/2026-11-28-unit211-Phi-zero-reduced-original-matrix-local-T-zero-extraction-8542.md)；
- [整 $\ell=0$ QQ 源](../notes/2026-11-28-unit211-Phi-zero-reduced-original-matrix-local-ell-zero-extraction-8542.py)及[输入说明](../notes/2026-11-28-unit211-Phi-zero-reduced-original-matrix-local-ell-zero-extraction-8542.md)；
- [两条已成下界及失败边界小凭据](../notes/2026-11-28-unit211-Phi-zero-T-ell-partial-orders-639-execution-8542.json)。

| 项目 | $T_0$ | $\ell$ |
|---|---|---|
| Run | [46103274354](https://github.com/Rogerhu12/math-research-public/actions/runs/46103274354) | [46103275741](https://github.com/Rogerhu12/math-research-public/actions/runs/46103275741) |
| Job | 140850296441 | 140850301932 |
| 内层退出码 | $-14$ | $-14$ |
| 驱动时间 | 120.074850915 秒 | 120.053103015 秒 |
| 最大 RSS | 286808 KiB | 303344 KiB |
| 源 blob | `eeae1ca81f477a93c539e22faef3a463324d9cfd` | `b77cd836795dfc94db6be25b3daad96555e1e41d` |
| 源提交 | `6675ad500a18a84dca4c2fe0ea5fecf45355eb83` | `4fe19dd455732e2e12814bff1d38939279a2bb0f` |
| stdout 字节 | 15553 | 21576 |

$T_0$ 源 SHA256：
`332fc4d176a3395441e3ed651ee2917890081345b023d5596138ee7946a14a17`；stdout SHA256：
`9004b3d714e0b83c27c2d2324f9df75ca4e95199f1c9b2bb2661a47a1eb37447`。

$\ell$ 源 SHA256：
`1ec0b3548a85eefaac21e56996aede30dde88bad19ea56a1a76f6f7323540283`；stdout SHA256：
`2ecb36ce755ad9714fb86bfe5add106d55960bfa730d61fb56d42c13149e7233`。

两次真实 pull 均更新到
`ec002c824f27d2bd2d39961aae5b87a51d9355d2`，
分别为 2026-11-28 03:31:52.478372 和 03:31:55.035738 UTC；两份 README 均无差异。

两次源均受 120 秒 / 1 GiB 原限界约束，计时信号终止后整门冻结。不增加时限、不缩短截断后重跑、不把未返回的秩或阶数当作结论。下一工作使用不同的真实数学输入；已经完成的 QQ 下界与 (1.3) 可立即登记。

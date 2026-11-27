# R150：整个剩余等权图的原四二次、三次 overlap 与六生成元

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**已证明。** 一般等权 $b=c=m/2$ 图在此前已完整排除的 $T_0=0$ 支之外，四条原二次式给出全域有效的六条首一规则，任意原有限变量单项式均返回为 $1,x,y,t,y^2,yt$ 的组合。所有新分母均为已付原单位，三次步骤没有新未付零面。这里证明六生成元，不断言商模自由，不把该结果当作整个等权分支排空。

## 1. 独立原有限变量与支付范围

使用[整个等权 $T_0=0$ 排除](R150-appendix-unit211-equal-weights-T0-zero-complete-original-exclusion.md)中的独立有限 $x,y,t$ 原 Gram，保留
$$
r^2=1-Q,\quad X=x+ry,\quad Y=x-ry,\quad P_{02}=m(m-1)(2m+3Q-4).
$$
原单位包含 $m(m-1)Q(Q-1)P_{02}\ne0$。新已完整排除的原支为
$$
T_0=-mJ=0,\qquad J=2m+Q-2,
$$
故 $J$ 也是已付单位。没有借用某个 $v$ 或 $y$ 坐标图来删除有限变量。

原同一 Gram 及 Frobenius 迹产生 mean $E_1^{\rm raw},E_{Be}^{\rm raw},E_{Bo}^{\rm raw}$，以及
$$
F_N=P_{02}N_{\rm pol}-4LJ_{\rm germ}.
$$
这里 $L=P_{02}\lambda$、$J_{\rm germ}$ 是原 germ 值，不能与权参数 $J$ 混淆。采用四个规范化原必要式
$$
F_0=2E_1^{\rm raw},\quad F_1=2E_{Be}^{\rm raw},\quad
F_2=E_{Bo}^{\rm raw},\quad F_3=2F_N/m^2.
$$
源只剥原已付因子，全部整除因式乘回；四式关于 $x,y,t$ 的总次数都为 2。其完整系数由已提交的原 affine Gram 源再生，不读取样本或缓存替代模型。

## 2. 四个首一二次规则的完整原组合

按 $(x^2,xy,xt,y^2,yt,t^2)$ 排列二次项，取四原式的列 $(0,1,2,5)$ 得矩阵 $M$。完整行列式为
$$
\delta_2=\det M=-16m^2(m-1)^2J^2.
\tag{2.1}
$$
新的 cofactor 计算直接核全部 16 个
$\operatorname{adj}(M)M=\delta_2 I_4$ 条目。由已付单位，合法定义
$$
(q_0,q_1,q_2,q_3)^{\mathsf T}
=\delta_2^{-1}\operatorname{adj}(M)
(F_0,F_1,F_2,F_3)^{\mathsf T}.
\tag{2.2}
$$
四个首项依次是 $x^2,xy,xt,t^2$；剩余二次项只有 $y^2,yt$，以及低次项 $x,y,t,1$。每一规则的完整原组合都实际乘回。

系数环先仅局部化
$\mathbb Q[m,Q,m^{-1},(m-1)^{-1},J^{-1}]$；
以整数多项式分子及这三个单位的分母指数保存系数。每一步约去的因子均有精确整除乘回，未通过有理化删除零面。

## 3. 四个真实三次组合

采用总次数优先，随后 $x>t>y$ 的次序。对
$$
yq_0-xq_1,\quad tq_0-xq_2,\quad
tq_1-yq_2,\quad tq_2-xq_3
\tag{3.1}
$$
用四二次规则依次降首项，得到 $\sigma_0,\ldots,\sigma_3$。
每条约化保留并实际全多项式乘回
$$
\sigma_i=\sum_{j=0}^3 A_{ij}F_j.
\tag{3.2}
$$
四条分别用了 15、15、12、15 个约化步骤。各 $\sigma_i$ 的三次项只有 $y^3,y^2t$，其他项属于六个生成元。

全部六个三次头 $2\times2$ 子式都已实际计算并返回。关键是第 0、2 行：写
$$
\sigma_0=a y^3+b y^2t+\text{低次},\qquad
\sigma_2=c y^3+d y^2t+\text{低次},
$$
其完整原子式为
$$
\delta_3=ad-bc=\frac{8(m-1)Q(Q-1)^2}{J}.
\tag{3.3}
$$
其他五个子式可能有附加因子，本证明不求逆它们。式 (3.3) 的分子仅含已付单位，因此没有新的三次首项零支。

## 4. 两条首一三次规则与全域六生成元

合法定义
$$
q_4=\frac{d\sigma_0-b\sigma_2}{\delta_3},\qquad
q_5=\frac{-c\sigma_0+a\sigma_2}{\delta_3}.
\tag{4.1}
$$
源以 $\delta_3^{-1}=J/[8(m-1)Q(Q-1)^2]$ 实际乘回为 1，
并核六规则所有首项列及完整原组合。故 $q_4,q_5$ 的首项分别为 $y^3,y^2t$，其余项只含 $1,x,y,t,y^2,yt$。

六个首项 $x^2,xy,xt,t^2,y^3,y^2t$ 的补单项式恰为这六项。每次用对应首一规则消去可除首项，均在上述良序中严格下降，故必停止。规则的原组合身份说明，每个单项式与其六项返回之差都在原四二次式理想中。

因此在
$$
R=\mathbb Q[m,Q,m^{-1},(m-1)^{-1},Q^{-1},(Q-1)^{-1},J^{-1}]
$$
上，$R[x,y,t]/(F_0,F_1,F_2,F_3)$ 由六项生成；另局部化原 $P_{02}$，或再加入原 $N_S,P_S$ 及其他必要关系，生成性仍成立。

本证明不要求六项线性独立，也不要求不同约化顺序给唯一余式；后续须保真实乘法、重叠差以及同一点的原 $N_S/P_S$，不能预设自由六维代数。

## 5. 新实际接口与准确执行

任一 $x,y,t$ 乘六生成元都可返回，并同步保留原四二次式的完整组合，从而提供实际原有限乘法的六列必要矩阵。不同返回顺序的差仍须保留，整个等权参数纤维尚未排空。

本页没有调用旧 600 秒未决 QQ Gröbner 门。新源为：

- [独立原 Gram](../notes/2026-11-27-unit211-equal-weight-original-affine-quadratics-8542.js)。
- [四二次 cofactor 与四三次组合](../notes/2026-11-27-unit211-equal-weight-paid-quadratic-and-cubic-rules-8542.js)，SHA-256：6be9a19267932784cb5a675079cea59f2175ed5a13d911101e1e445be9963b24。
- [全域六规则](../notes/2026-11-27-unit211-equal-weight-global-six-generator-rules-8542.js)，SHA-256：93ecc617f3dba9a7e37da86d3169a90ce9c910a3e613e64a5cc271d80f7711b6。
- [实际回执](../notes/2026-11-27-unit211-equal-weight-global-six-generator-execution-8542.json)。

这些 JavaScript 文件是 Function body。先由原 Gram 源取得 affine；第一新源以参数 (affine,"quadratic") 得 quad，再以 (affine,"overlap",quad) 得 cubic；第二新源以 (affine,"six",quad,cubic) 得六规则。三段在纯 V8/BigInt 中真实完成，分别为 0.333、6.503、2.165 秒；全部精确原组合成功。没有 OS 子进程，退出码不适用，RSS 未暴露。只保存源、参数、哈希和小回执。

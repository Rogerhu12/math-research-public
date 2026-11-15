# R323 — 从有效有限 cut 两 jet 包围显式选择 R300 的统一短窗

作者：AI（/root，GPT-6 Astra Pro）。日期：2026-11-15。  
范围：准确有理区间上的构造定理及直接可实现参数公式；本篇没有实际147输出，没有计算 cut、构造实际场或支付新的尾 DN。

## 1. 已有输入与本结论的用途

[R300](R300-continuous-nine-control-scalar-family-and-cut-calibration.md)给出准确 core、两段三次速度过渡、常速 coast 和同一连续尾目标的 cut 三次 collar。其一般有效选窗结论要求真正可计算实数名称。这里处理更具体的情形：已经取得一组**有严格余量的有限有效包围**，则无需将它冒作任意精化 oracle，可以直接构造一组对整盒统一有效的 dyadic 短窗。

同一准确 core 在原端点 $L_0>0$ 的 jet 为 $(A,V,B_A)$，原 binary cut 的准确有理数为 $R$。假设

$$
R>0,\qquad \gamma=A-R>0,\qquad |V|<1.
$$

core jet 必须由原共享节点准确多项式取得，不能用独立四舍五入的末点代替。完整 core 的 $a>0,|a'|<1$ 及内部 $C^2$ 仍由其完整原件/域证书负责；只有端点满足上述条件不支付整个 core。

输入三个有限闭区间共同包含同一声明 C 在原 cut 的 $E_0,E_1,E_2$，并已证明 $\underline{\boldsymbol E_0}>1$。不要求每个盒中任意三元组来自同一根选择，但真实共同三元组必须被包含。准确 collar 数据为

$$
v=-E_0^{-1/2},\qquad b=-\frac{E_1}{2E_0^2},\qquad
q=\frac{E_2}{2E_0^{5/2}}-\frac{E_1^2}{E_0^{7/2}}.
$$

使用向外有理区间运算及有效平方根包围得到 $\boldsymbol v,\boldsymbol b,\boldsymbol q$。要求实际所得速度盒严格满足

$$
-1<\underline{\boldsymbol v}\le\overline{\boldsymbol v}<0.
$$

这包括对本次平方根包围的真实检查；不能仅凭理论 $E_0>1$ 就忽略当前有限包围是否已经证明它。定义

$$
M=\min\{-\overline{\boldsymbol v},\,1-|\boldsymbol v|_{\max}\}>0,\qquad
B=|\boldsymbol b|_{\max},\qquad Q=|\boldsymbol q|_{\max},\qquad T=1+B+Q.
$$

所有端点与 $M,B,Q,T$ 都是当前有限包围中的准确有理数。它们是选择参数的保守数据，不替换准确目标中 $E_0,E_1,E_2$ 的语义叶。

## 2. 一个严格向下的 dyadic 选择

对正有理数 $x=N/D$，取既约正整数分子分母。令 $\operatorname{bl}(n)$ 表示正整数的二进制位数，并定义

$$
n=\max\{1,\operatorname{bl}(D)-\operatorname{bl}(N)+1\},\qquad
\Theta(x)=2^{-n}.
$$

由 $D<2^{\operatorname{bl}(D)}$ 和 $N\ge2^{\operatorname{bl}(N)-1}$ 得
$D/N<2^{\operatorname{bl}(D)-\operatorname{bl}(N)+1}$。若最大值取第二项，立即有 $\Theta(x)<x$；若取1，则 $D/N<2$，同样有 $1/2<x$。因此

$$
0<\Theta(x)<x.
$$

这只需要有限整数位数和移位，不含数值探测、深根迭代或无界的科学批次。显式程序可以另核严格比较；该比较核的是参数公式，不能被记成原 nonlinear trial 的接受。

## 3. collar 宽度与严格端点包围

本次明确选 $\kappa=1/2$。置

$$
x_d=\min\left\{1,\frac{\gamma}{8T},\frac{R}{8T},\frac{M}{8T}\right\},
\qquad d=\Theta(x_d).
$$

按 R300 的**同一准确表达**形成

$$
R_B=R-vd+\frac{bd^2}{2}-\frac{qd^3}{6},\qquad
V_B=v-bd+\frac{qd^2}{2},\qquad
B_B=b-qd.
$$

令 $\boldsymbol R_B,\boldsymbol V_B,\boldsymbol B_B$ 为把先前三个盒代入这些式子的普通向外区间结果。由于 $d<1$ 和 $|\boldsymbol v|_{\max}<1$，该区间计算本身满足

$$
|\boldsymbol R_B-R|_{\max}
\le d+\frac{Bd^2}{2}+\frac{Qd^3}{6}
\le Td<\frac{\min(\gamma,R)}8.
$$

故

$$
\underline{\boldsymbol R_B}>\frac{7R}8>0,\qquad
D_-:=\underline{A-\boldsymbol R_B}>\frac{7\gamma}8>0.
$$

并且

$$
|\boldsymbol V_B-\boldsymbol v|_{\max}
\le Bd+\frac{Qd^2}{2}<\frac M8.
$$

这里差式表示同一代入的扰动；不通过对两个独立完整区间作差来抵消依赖。上述三角界直接针对 $-bd+qd^2/2$。因此

$$
1-|\boldsymbol V_B|_{\max}>\frac{7M}8>0.
$$

定义准确有理量

$$
F=|\boldsymbol B_B|_{\max},\qquad
m_A=\min(1-|V|,1-\kappa),\qquad
m_B=\min(1-|\boldsymbol V_B|_{\max},1-\kappa).
$$

两者均严格正。collar 原来的两个充分条件同时成立：

$$
d<\frac\gamma2,\qquad Bd+\frac{Qd^2}{2}<\frac M2.
$$

特别地，整个 collar 的准确速度仍严格向内且在 $(-1,0)$ 内；其半径从正的 $R_B$ 连到正 cut $R$。不向自然 $R_{\rm out}$ 外延，也不重归一化 cut 或 warp。

## 4. 两个过渡窗与 coast 的正长度

令 $A_2=|B_A|$，选择

$$
x_e=\min\left\{
1,\frac{D_-}{8},\frac A4,\frac{\underline{\boldsymbol R_B}}4,
\frac{m_A}{1+A_2},\frac{m_B}{1+F},
\frac{D_-}{8(2+A_2+F)}
\right\},\qquad e=\Theta(x_e).
$$

明确设第一、最后过渡宽度都为 $e$，没有对旧模型的宽度作隐式修改。则

$$
2e<\frac{D_-}2,\qquad e<\frac A2,\qquad
e<\frac{\underline{\boldsymbol R_B}}2,
$$

以及

$$
\frac4{27}eA_2<\frac{m_A}2,\qquad
\frac4{27}eF<\frac{m_B}2.
$$

最后两式也包括 $A_2=0$ 或 $F=0$；分母写成 $1+A_2,1+F$，没有零除或分支漏项。它们正是 R300 两段三次速度的严格余量条件。

按原准确积分定义

$$
I_A=\frac e2(V-\kappa)+\frac{e^2}{12}B_A,\qquad
I_B=\frac e2(-\kappa+V_B)-\frac{e^2}{12}B_B,
$$

$$
L_C=\frac{A-R_B+I_A+I_B}{\kappa}.
$$

因为 $|V|<1$、$|\boldsymbol V_B|_{\max}<1$、$0<\kappa<1$ 和 $e<1$，两个积分盒满足

$$
|I_A|_{\max}+|I_B|_{\max}
\le e(2+A_2+F)<\frac{D_-}{8}.
$$

所以直接区间代入所得 coast 长度也有严格下界

$$
\underline{\boldsymbol L_C}>
\frac{7D_-}{8\kappa}>0.
$$

这里没有把累计半径重设成旧 $a_0$。准确恒等式仍为
$A+I_A-\kappa L_C+I_B=R_B$，从而接上同一 collar。

综上，给定上述有限严格输入后，$d,e,e$ 同时支付 factory 中全部11个 R300 构造充分条件。程序仍可按原逐项条件记录原区间和布尔值，以发现实现或输入不符；这不是新的 native/BVP 门。

## 5. 保留全 core、全九控制及实际域责任

本结论只选择构造宽度。准确 core 的每个共享 seam、完整域以及第一支持仍必须保留。第一支持可明确沿用原 PrefixControls 的 binary64 运算结果 $(.05L_0,.30L_0)$，其存储宽度是实际 right-left 字；只有当前准确端点比较真正满足 $0<l<l+w<L_0$ 才能使用。它不同于默认 CompleteProfile 的另一支持选择，不能混名。

第二支持是第一过渡段，第三支持是所构造的准确 coast。每个支持仍有 degree6、degree7、degree8 的三个完整 bump，保全部九个明确系数。原数值搜索末参数可作为新族初猜；不同支持/基底下的当前域必须重新计算，不能借旧域证书。这个参数公式不把后六个系数清零，也不把九参数全部替成基底。

若准确 core 本身全域严格可行，则 R300 结构定理给基底及零附近的开可行族；这不声称给定九个旧非零系数就在该邻域。实际 factory 仍分别遍历完整基底与给定九参数的闭域，保全部未访 stack、未决叶和严格余量。域遍历资源耗尽不是不存在性结论。

新准确定义仍保三个真实语义叶和它们的联合来源。数值 profile 可公开记录中点近似，但三个中点不必来自同一尾根；同一材料 $u$ 下的准确径向 metric 仍是 $L_*^2du^2$，不能用数值长度代替。

## 6. 失败与有效性边界

如果实际 cut 点不合法、完整点包围未完成、速度盒不能证明 $-1<v<0$，或者真实 core 端点未满足 $A>R,|V|<1$，本公式的前提尚未支付。必须返回原缺口和有限数据，不能自动重写 cut、丢弃原尾片、改变根族或以旧 J 补新 C 的响应。

本定理没有保证任意输入 oracle 会终止，也没有说任意粗盒最终可接受。它的断言是：**对已经具有这些严格余量的具体有限有效盒，参数公式有限、明确，并统一满足相同的构造条件。** 即使公式的 dyadic 宽度在 binary64 中太短而无法形成不同节点，准确构造与数值可表示性仍是两项责任；后者应据实际数值编译记录，不能通过截宽改变准确定义。

全部有理/区间计算与实际源码运行只在本公开仓库 Actions。后续实际147须保原 v3 全源/1440片/六 primitive/点及whole查询和全部身份，完成同job读取后再清理可重算 raw。本篇不是实际147运行结果，没有新C尾线性J/非线性响应、完整闭面、metric $10^{-6}$ 或几何比例完成结论。

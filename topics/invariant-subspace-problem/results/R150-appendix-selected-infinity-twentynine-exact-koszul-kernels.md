# R150 附录：所选支撑内 29 条真有理 Koszul 核及旧 23 核的成员性

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

**状态：原整数完整核验已完成。** 本次准确得到所选支撑内标准 Koszul 空间的特征零维数 29，包含此前 23 条真核，因此新增六个真独立方向。同一所选无穷远矩阵的有理秩区间收紧为 $4318$ 至 $4325$。没有把余下七个方向认作已存在的真核。

## 1. 同一原来源问题

沿用原整数 $A_\infty\in\mathbb Z^{4367\times6188}$、同一 4354 个原来源 $J$、同一 4354 个输出 $I$，记
$$
C_0=A_{\infty,*,J},\qquad B_0=A_{\infty,I,J}.
$$

令 $\Phi$ 为 1632 个标准来源
$$
a(f_j e_i-f_i e_j),\qquad i<j,\quad a\in\{1,m_0,\ldots,m_{10}\}.
$$
[187 列头映射的实际单射证据](R150-appendix-physical-infinity-linear-multiples187-and-koszul1632-injection.md) 已给出 $\Phi$ 在 $\mathbb Q$ 上单射，且原恒等式 $A_\infty\Phi=0$ 成立。

置 $O=\Phi_{J^c,*}$。因此
$$
\mathcal K_J=\operatorname{im}_{\mathbb Q}\Phi\cap\mathbb Q^J
=\Phi(\ker_{\mathbb Q}O).
$$
这是原来源的支撑交，不是输出商中的相消条件。

## 2. 实际运行和精确求解

实际执行记录：

| 项目 | 实际值 |
|---|---|
| run | 43679903558 |
| step | koszul-exact-rational-support |
| 执行源提交 | f7147419a96024d50121cec3d577c0f2cf5fd5d9 |
| 数学时间 | 33.71132376800051 秒 |
| 进程总时间 | 33.847712049999245 秒 |
| 状态 | completed，exitCode 0 |

[实际小记录](../notes/r150-infinity-remote-session-789f/43679903558-koszul-exact-rational-support.json) 为 36171 B，SHA256 为
$96c185135915ddc324d75b470038fd1a472c650fca6a34e5de7749f54af1b032$。
临时完整主回执为 18271 B，SHA256 为
$1615d967b7e004803e82b8a057d106d0de7617788a5e573ed65d04f48f1aa47f$。
本次数学 binding 为
$10890e55000e9e0554b2488f333b899dbf224421e5bf091adc24d396348cc6a4$。

使用 [精确求解源码](../notes/2026-11-15-r150-koszul-exact-rational-support-solve-789f.py) 与 [完整接口证明](../notes/2026-11-15-r150-koszul-exact-rational-support-solve-interface-789f.md)。原整数准备保留全部 1834 个外支撑方程；去掉恒零行后，核心为 1808 行、1632 列。此前的一、二支撑精确消元没有发现可剥变量，故本次没有借用未经证明的简化。

从模 31 选元取原整数的 1603 阶单位子块，精确求解其 29 列有理图。随后完整计算全部 1834 行原外支撑残量，而非只核所选子块。原来源系数核的结果为
$$
\operatorname{rank}_{\mathbb Q}O=1603,\qquad
\dim_{\mathbb Q}\ker O=29.
\tag{2.1}
$$
所有求解均在原整数/有理数中进行；模 31 RREF 只用于选择一个真正可逆的原整数子块。

## 3. 完整原式门槛全部通过

对于精确系数核的每一列 $c_a$，程序清分母，形成完整整数来源
$$
v_a=\Phi c_a\in\mathbb Z^{6188},\qquad 1\le a\le29.
$$
每一列都实际验证：

- 全部 1834 个未选来源系数为零；
- 使用原 17 式整数模型乘回，全部 4367 个输出严格为零；
- 完整 36 个规范自由来源坐标被保留。

29 个来源的完整自由像在 $\mathbb Q$ 上秩为 29。结合 $\Phi$ 单射及 (2.1)，得到
$$
\boxed{\dim_{\mathbb Q}\mathcal K_J=29.}
\tag{3.1}
$$

可重建的主要临时数据身份为：

| 原临时文件 | 字节数 | SHA256 |
|---|---:|---|
| exact-koszul-source-coefficient-basis.json.gz | 1670175 | b2421f22d40ed376302982f049fa63a35f811ab9899604abc58c964e3a4a2808 |
| exact-selected-koszul-free36-image.json.gz | 29488 | 24f4cbd8ca7c39d5c6280159b71cf8fc85fd9811a1dc9bc6f8bdeb50a977f249 |

各列完整来源及原乘回的文件身份也在小回执中逐项保存。按根 README 的数据规则，这些可由已提交源码和参数重建的大数据只存在于当前运行临时目录；长期保留的是源码、运行号、参数、小回执和哈希。

## 4. 旧 23 条真核现在严格落入 Koszul 空间

此前 23 条真有理核的完整规范自由坐标为已付的 23 个标准轴。本次实际核得
$$
\operatorname{rank}_{\mathbb Q}
\bigl(\operatorname{free}(v_1),\ldots,\operatorname{free}(v_{29}),
e_{j_1},\ldots,e_{j_{23}}\bigr)=29.
\tag{4.1}
$$
因此这 23 个轴都包含在新真核的自由像中。

还须把自由坐标的包含还原为来源的包含。原非自由 4318 列的同一模 31 单位子块在 $\mathbb Q$ 上可逆；因此，一个支撑在 $J$ 内的真核若 36 个自由坐标全零，则整个来源为零。也就是说，完整自由坐标在所选真核空间上单射。

对每个旧核，(4.1) 给出一个新 Koszul 核与它具有相同自由坐标；两者之差是真核且自由坐标为零，故两者相等。于是
$$
\boxed{\operatorname{span}_{\mathbb Q}
\{\text{此前 23 条真核}\}\subset\mathcal K_J.}
\tag{4.2}
$$
这补上了先前仅比较模 31 自由轴时尚未支付的特征零成员性。它不依赖重新计算旧 23 条原乘回。

## 5. 真新增维数及仍未闭合的范围

由 (3.1)、(4.2)，本次在旧真核空间之外确实新增六个独立有理方向。全部 29 条核均属于 $\ker C_0$，故
$$
\boxed{
4318\le\operatorname{rank}_{\mathbb Q}B_0
\le\operatorname{rank}_{\mathbb Q}C_0
\le4354-29=4325.
}
\tag{5.1}
$$

标准 Koszul 的所选支撑交现已完整算完；在这个固定族内不能再寻找第 30 条独立所选真核。若原所选常块最终秩为 4318，则尚需七个超出该标准 Koszul 空间的方向；(5.1) 本身不证明这七个方向存在。

此前模 31 的前 29 个自由坐标描述仍是有限域结果。本次没有无核验地将有理自由像写成相同坐标子空间；这里使用的特征零结论是完整秩 29、旧 23 轴的精确包含，以及原来源的完整乘回。

本条不增加原 $31$ 进精度，不继续 LLL 候选扫描，不据此宣布 $D$ 的无穷远完整 Smith 厚度或最高系数为 31 单位。原特征零目标成员性和课题总体完成条件仍须继续。

# R150 补充：正确 Phi 的整 B 曲线与原六乘二呈示

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 原范围与完整有理图

保持正确原 unit211 的 $\Phi=0$、全部原均值和 N/P 值条件，并保持
$$
Q(1-Q)P_fP_{02}bcD\ne0.
$$
本条只处理新的正确三均值首项因子
$$
B=-Q^2+(12u^2-20u+8)Q-16(u-1)^2=0.
\tag{1}
$$
不继承已撤回的旧 compact E1 或其任何首项单位。

令 $s=u-1$。原 $\Phi$ 恒等式给
$$
P_f=4s^2(Q+4s),\qquad
P_{02}=2s\ell Q,
$$
所以 $s$ 非零。用真实原坐标
$$
x=\frac{Q}{4s}
$$
代入 (1)，精确得到双向恢复
$$
u=\frac{(x+1)^2}{3x},\qquad
Q=\frac{4(x^2-x+1)}3.
\tag{2}
$$
反向代入同时返回 $B=0$ 与 $Q=4sx$。因此所有当前原点都由有限的 $x$ 覆盖，没有丢失一个“无穷参数”纤维。

设
$$
F=x^2-x+1,\quad H=2x-1,\quad \beta=5x-1,\quad
J=7x^2-4x+1.
$$
本次完整返回
$$
1-Q=-\frac{H^2}{3},\qquad
\ell=\frac{(x+1)\beta}{6x^2},\qquad
bc=\frac{(x+1)^2J}{36x^4}.
\tag{3}
$$
所以仅从原参数单位便有
$$
U_B=xF(x+1)H\beta J\ne0.
\tag{4}
$$
例如 $F\ne0$ 来自 $Q\ne0$，$\ell\ne0$ 来自 $P_{02}\ne0$，故 $x+1$、$\beta$ 非零；最后 $J\ne0$ 来自 $bc\ne0$。没有使用新的头因子支付 (4)。

另一个正确三均值因子满足
$$
A=4s^2-Q=-\frac{4sH(x+1)}{3x},
\tag{5}
$$
故在本条整 $B=0$ 上自动非零。(5) 不要求先使用另行完成的整 $A=0$ 排除。

## 2. 正确四原式及实际新三次首项

原恢复仍是
$$
\begin{gathered}
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J_0=2u(1-u)+\ell Q,\\
G=\lambda P_{02}+(u-1)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,\quad f=-P_c/P_f,\\
z=Qt,\qquad v_n=J_0f-G+bc\,z.
\end{gathered}
\tag{6}
$$
这里 $J_0$ 与 (3) 的二次式 $J$ 区分。四条原式是正确的
$$
F_0=\overline R_{\rm true},\quad F_1=W_4,\quad
F_2=\overline O,\quad F_3=N_1.
$$
它们的完整定义来自[正确四原头源码](../notes/2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py)，只执行原定义前缀，并在其中代入 (2)。没有重跑旧头测试或任何旧消元。

以
$$
v=(1,T,z),\qquad m=(T^2,Tz,z^2)
$$
分写 $F_i=L_i v+H_i m$。三条均值的头行列式在整 (1) 为零。本次选择原行 $F_0,F_1,F_3$；其头矩阵 $H_*$ 的行列式 $h$ 非恒零，除 (4) 的整因子和非零有理常数后，精确只剩
$$
\boxed{H_3(x)=11x^3-18x^2+6x-1.}
\tag{7}
$$
其头全部零纤维 $H_3=0$ 保留，不由“选到了非零多项式”将它排除。

在 $H_3\ne0$ 上，用完整伴随矩阵身份
$$
\operatorname{adj}(H_*)H_*=H_*\operatorname{adj}(H_*)=hI
$$
得到三条真规则
$$
m_i-r_i v=\sum_j(H_*^{-1})_{ij}F_j.
\tag{8}
$$
未选原行 $F_2$ 的完整余式为
$$
F_2-\sum_j\tau_jF_j
=p_0(\lambda)+(a\lambda+b)T+(c\lambda+d)z,
\tag{9}
$$
其中 $\deg_\lambda p_0\le2$，$a,b,c,d$ 都只依赖 $x$。每个 (8)、(9) 的全多项式等式已返回。

## 3. 新二次斜率与精确二列模型

定义
$$
\Delta=ad-bc.
$$
这里 (9) 的系数 $b,c$ 仅为临时符号，不是原权重。本次真实因式分解表明：$\Delta$ 的分母只含 (4) 和 (7)，分子去掉 (4) 后只剩
$$
\boxed{C(x)=23x^2-11x+2.}
\tag{10}
$$
在 (7)、(10) 的补图，令
$$
p_0=A_\lambda\lambda^2+B_\lambda\lambda+C_\lambda,\qquad
\omega=aT+cz+A_\lambda\lambda+B_\lambda.
$$
这里下标表示 (9) 的三个纯权系数。原 (9) 与此定义精确恢复
$$
T=\frac{(c\lambda+d)\omega-A_\lambda d\lambda+cC_\lambda-dB_\lambda}{\Delta},
$$
$$
z=\frac{-(a\lambda+b)\omega+A_\lambda b\lambda+bB_\lambda-aC_\lambda}{\Delta}.
\tag{11}
$$
两个原等式均完整乘回，不倒任何 $\lambda$ 多项式。

将 $(aT+cz)^2$ 用 (8) 还原，得到对 $\omega$ 首一的二次式
$$
q(\omega)=\omega^2+q_1(\lambda)\omega+q_0(\lambda).
\tag{12}
$$
$q_0,q_1$ 的 $\lambda$ 次数至多 $2$，且 (12) 是三条所选原式代入 (11) 后的完整线性组合。写这些代入式为 $\widetilde F_i$，再令
$$
\ell_i=\widetilde F_i-
[\omega^2]\widetilde F_i\,q,\qquad i\in\{0,1,3\}.
\tag{13}
$$
每条 $\ell_i$ 对 $\omega$ 至多一次。由 (12) 的原组合和 (13) 的完整除法，
$$
(\widetilde F_0,\widetilde F_1,\widetilde F_3)
=(q,\ell_0,\ell_1,\ell_3).
\tag{14}
$$
在首一二次代数
$$
S=\mathbb Q[x,U_B^{-1},H_3^{-1},C^{-1},\lambda][\omega]/(q)
$$
内，任一元素由 $1,\omega$ 生成。因此完整原四式理想的二列关系正由
$$
\ell_0,\ \omega\ell_0,\ 
\ell_1,\ \omega\ell_1,\ 
\ell_3,\ \omega\ell_3
\tag{15}
$$
给出，$\omega\ell_i$ 每次都用同一个 (12) 完整约化。这个精确呈示不假设最终商是自由模，也没有把裸矩阵的零空间当成完整原理想。

(7)、(10) 的整零纤维仍保留；本条不声称整 $B=0$ 已排空，不声称 $\lambda$ 已满足首一有限关系，也不倒原 $D$。

## 4. 真实执行状态与已经完成的数学部分

[唯一首次源](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-rational-original-six-by-two-8542.py)：

- blob a15cbf3a0bd940fc9ba7f4c292bf19b0948c7b22；
- SHA256 f027f52d63a345ce89b05ecbce7276093256eaf5a4b0ff9bf59da0e123a5f835；
- run 46112526572，job 140879029009；
- 真实耗时 0.093598010 秒，RSS 40240 KiB，**退出码 1**。

完整日志显示：最后一次调用摘要打印函数之前，(2)–(15) 的所有等式检查、全部系数分母支持检查均已通过。源码已经运行到最后的 JSON 打印调用；失败原因准确是
$$
\texttt{TypeError: Object of type fmpz is not JSON serializable}.
$$
即 FLINT 整数用于最后次数摘要时没有转成 Python 原生整数。此前 (7)、(10) 和完整三条规则、第四条原迹已经实际输出；最后的六行次数摘要没有成功输出，不为它编造数值。

[小回执](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-rational-original-six-by-two-execution-8542.json)保留退出码 1 与原 stdout 身份。本条的精确呈示由完整原定义、上列代数证明和已走完的断言共同给出；没有把失败进程改记为退出码 0，也不因最后打印故障重跑整段已完成的数学计算。

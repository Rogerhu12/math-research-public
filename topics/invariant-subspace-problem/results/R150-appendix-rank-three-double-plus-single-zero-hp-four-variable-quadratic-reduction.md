# R150 附录：零 Hp 二重加单点层的四变量二次孤立源等价归约

日期：2026-11-26（UTC）。Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明以下等价归约；特征零排除仍未完成。** 这是[原有理重建第 7 节](R150-appendix-rank-three-double-plus-single-zero-hp-finite-source-rational-reconstruction.md)十二条必要式的完整等价降维。它没有把必要式当成完整梯度，也没有声称其参数集为空。

沿用 S*、J0、Es=s²−sx+z、Ns、qpair、Δ、L2、Zn 及 Q=4e³−1、D=2e³+1−12e⁴。令 d=w−s≠0，且
$
S_*(s+\delta)=J_0\delta+U\delta^2+V\delta^3+W_4\delta^4+L\delta^5.
$
于是
$
C_3=U+dV+d^2W_4+d^3L,\quad
B_0=B_*(s)=V+dW_4+d^2L,\quad B_1=B_*'(s)=W_4+dL,
$
$
B_w=B_*(w)=V+2dW_4+3d^2L,\qquad dB_0+U=C_3.
\tag{1}
$
特别在原 C3=0 层，B0=−U/d，未除以 U 或任何新系数。

原核另有准确整除
$
N_s=E_s^2Q_n,\quad k(s,s+d)=-d^2q_s(s+d),\quad
W_0=E_s d\,W_{\rm red}.
\tag{2}
$
其中 W0=k∂sNs−2Ns∂sk。前三者均由原多项式构造逐项检验。令
$
q_w=q_s(s+d),\quad
c_0=1-2e,\quad H_0=Q+6e,\quad R_e=2e^3+1,\quad E_s'=2s-x.
$
所有以下多项式都在 s,d,x,z,e 中，Zn 与 L2 均代入 w=s+d。

## 七个原必要多项式

保留 J0/Es=0、C3=0，另外五式准确为
$
\begin{split}
H_2={}&(H_0E_sW_4+3c_0U)d^2\\
&+(2H_0E_sV+3c_0E_s'U)d
+12e(e^2+1)E_sU=0,
\end{split}
\tag{3}
$
$
N_2=c_0^2U^2Z_n
-25600e(1-e)q_{\rm pair}Q_nE_s^4d^2=0,
\tag{4}
$
$
G_{\rm jet}=3e^2W_{\rm red}^2
+2R_e\Delta q_{\rm pair}b_sQ_nd^2q_w^2=0,
\tag{5}
$
$
G_{\rm single}=2e^2Q L_2+D\Delta q_{\rm pair}d^2q_w=0,
\tag{6}
$
$
G_{\rm derivative}
=W_{\rm red}U+c_0Q_nd^2q_wB_1E_s+c_0Q_ndq_wUE_s'=0.
\tag{7}
$
(3) 与 (4) 关于 d 都至多二次。后者用到 Z=DH EV 的系数向量只关于 w 一次，所以固定双线性型给出的 Zn 关于 w 至多二次；不需要展开大系数数组。

## 原单位与全部方向的证明

只局部化原来已经非零的乘积
$
\Pi=s(s-2)(s+6)d\,\Delta q_{\rm pair}E_sQ_nq_w.
\tag{8}
$
它与 bs·Δ·qpair·Ns·k 的非零条件完全等价，只去掉重复幂和非零常数。加入一个变量 n 与 nΠ−1=0 是该原物理开集的准确方程；没有额外假定源或重构系数非零。

原十二式先给 (1)—(2)。最高 w 条件原为
$
G_w=H_0E_sB_w+3c_0B_0E_w=0,\quad
E_w=E_s+E_s'd+d^2.
$
完整多项式身份
$
dG_w+H_2=3(H_0E_s+c_0E_w)C_3
\tag{9}
$
给 (3)，并且在 C3=0、d≠0 时也给逆向。

消去原 Θ* 后的范数是
$
c_0^2B_0^2Z_n-25600e(1-e)q_{\rm pair}Q_nE_s^4=0.
$
乘 d² 并使用 dB0=C3−U，差正好为 c0²C3(C3−2U)Zn，故与 (4) 双向等价。

原喷射尺度清分母后为
$
3e^2W_0^2+2R_e\Delta q_{\rm pair}b_sN_sk^2=0.
$
只除已付的 Es²d² 得 (5)。原单点比例直接给 (6)。

原最高 s 一次式在消掉 q、Θ* 后为
$
c_0N_sk(B_1E_s-B_0E_s')+W_0B_0E_s=0.
$
除 Es²d，再乘 −d，使用 (1)，得到 (7)；相差的整个项是
−[c0Qndq_wEs′+Wred]C3，所以也双向等价。

反向，假设七式及 Π≠0。由 (5)，Wred≠0，因为其右侧其他因子均为已付单位；(4) 则使 U、Zn 非零。恢复
$
\Lambda=\frac{\Delta q_{\rm pair}}{4e^2N_s},\quad
\Xi=\frac e{q_{\rm pair}N_s},\quad
h=1/k,\quad
q=-\frac{4bN_sk}{W_0},\quad
\Theta_*=\frac{c_0B_0}{2eE_s}.
$
这些分母都已支付。上述双向身份及 (5)—(6) 逐项恢复原十二条式，所以没有丢掉降次或零领先项纤维。G9 的不可约性确保所用 e、b、Q、1−e、1−2e 等常数都是原九次域中的单位。

因此这七式加 nΠ−1 可用于原十二式的精确算术门；若它们不为空，仍须接原全部 N 与最高式系数，不能由必要归约提前宣称完整临界点或排除。

## 实际算术推进与准确边界

[自含生成源](../notes/2026-11-26-h21-all-finite-reduced-quadratic-modular-347c.py)在公开 run `45807166646`、job `139865351533`，使用 Python 3.12.14、python-flint 0.9.0、SymPy 1.14.0、Singular 4.4.1，确实生成上述七式和一个原单位逆关系，并在模 `1031`、`e=700` 下算得单位 Gröbner 基。源 SHA-256 为 `239dcd58040be9d580e08e8ccb5f89eaecdbc7574f1320b257d2bbb12c668ba5`；生成的八式输入 SHA-256 为 `b0b06b219217a50f6b5308aa22aede0a48b9ddf1e19e45a55d3b244ee666ccec`。源报告总时141.946249秒，驱动142.446723秒、峰值491264 KiB、exit0；单独 Singular 输出的 SHA-256 为 `6e31a44f763f4d6b35e323fd62cc8d49b16adcd07d489798b145beb89f942454`。

这些模数据只决定后续提升方向。模理想为单位不自动推出九次域 $\mathbb Q[e]/(G_9)$ 或复数原系统为单位；必须另给特征零恒等式。同期直接十二加二十七式门在180秒界内未返回，仍为未决，没有用退出码0冒称数学成功。[本批小回执](../notes/2026-11-26-original-jet-fibers-execution-347c.json)区分每条真实返回；不保存可重新生成的系数数组或完整运行日志。

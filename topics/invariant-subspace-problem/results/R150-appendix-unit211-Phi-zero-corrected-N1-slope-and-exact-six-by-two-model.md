# R150 补充：正确 Phi 原 N1 的单一残留斜率曲线与精确六乘二呈示

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 原范围和完整结论

本条从更正后真正 dual 乘法的四个原二次式出发，只使用
$$
\Phi=0,\qquad Q(1-Q)P_fP_{02}bc\ne0.
$$
令
$$
s=u-1,\quad K=Q+4s,\quad L=Q-2s(u-2),\quad
M_n=2uL-L^2-u^2Q,
$$
$$
U=Q(1-Q)sKLM_n,
$$
$$
A=4s^2-Q,\qquad
B=-Q^2+(12u^2-20u+8)Q-16s^2.
\tag{1}
$$
原 $P_f=4s^2K$、$P_{02}=2sL$、$M_n=4bcQ(1-Q)$ 支付 $U$。本条保留整 $AB=0$，在 $AB\ne0$ 上得到原 $N_1$ 的准确余式
$$
n=p_0(\lambda)+(a_s\lambda+b_s)T+(c_s\lambda+d_s)z,
\qquad
p_0=A_s\lambda^2+B_s\lambda+C_s.
\tag{2}
$$
其中所有带下标的系数仅依赖 $u,Q$。

真正斜率
$$
\Delta=a_sd_s-b_sc_s
$$
完整因式返回为
$$
\boxed{\Delta=
\frac{2sLM_nG(u,Q)}{(1-Q)KAB^2}.}
\tag{3}
$$
$G$ 的双次数为 $(18,10)$，136 项；其完整定义是 (2)、(3)，由原三均值和原 $N_1$ 唯一重建。实际系数 SHA256 为 e51ea8f50e4ba032d936bb77a05f36c79af8c7eb23b62ca63eaf15b73a117a1c。

因此在当前原 $UAB$ 图，只有 $G=0$ 是新的斜率零支。实际因式输出中的另一个双次数 $(4,2)$ 因子恰为
$$
\begin{aligned}
-M_n={}&4u^4-20u^3-3u^2Q+40u^2+10uQ-40u\\
&+Q^2-8Q+16,
\end{aligned}
$$
已经由原 $bcQ(1-Q)$ 支付，不能另记一条未付斜率曲线。另一个因子 $2u^2-6u-Q+4=-L$ 同样已付。

在 $UABG\ne0$ 上，原四式理想有下述精确六乘二表示，而不是仅相同零点或一个必要矩阵。整 $AB=0$、整 $G=0$ 继续保留；本条没有排除它们。

## 2. 原三均值规则与 N1 来源

在
$$
R=\mathbb Q[u,Q,U^{-1},A^{-1},B^{-1},G^{-1}]
$$
中，令 $F_0,F_1,F_2$ 分别为更正后的真实 germ 组合 $\overline R$、原加权均值 $W_4$、原差均值 $\overline O$。它们在基
$$
1,T,z,T^2,Tz,z^2
$$
中的系数都由原 $E_0/N_0/P_1$ 图直接构造。

三行二次头 $H$ 的精确行列式为
$$
\det H=\frac{ABM_n^3L^4}{8K^3(1-Q)^4}.
\tag{4}
$$
以完整 adjugate 恒等式求逆，得到三条真实关系
$$
m_i-r_i\cdot(1,T,z)
=\sum_{j=0}^2(H^{-1})_{ij}F_j,
\qquad (m_0,m_1,m_2)=(T^2,Tz,z^2).
\tag{5}
$$
本次全部左、右逆及三条原组合都完整返回。用 (5) 消去原极化 $N_1$ 的三个二次项，返回 (2)，并给出
$$
N_1-n=\sum_{j=0}^2\theta_jF_j.
\tag{6}
$$
故四式理想严格等于 $(F_0,F_1,F_2,n)$。这不要求三生成元模块自由，也未加入完整 N/P 的其他条件。

## 3. 唯一原坐标变换与首一二次

以下 $\omega$ 是新形式坐标，不是原值向量的 germ $w=\lambda-1-T$。定义
$$
\omega=a_sT+c_sz+A_s\lambda+B_s.
\tag{7}
$$
(2)、(7) 的唯一逆为
$$
T=\frac{(c_s\lambda+d_s)\omega-A_sd_s\lambda+c_sC_s-d_sB_s}{\Delta},
$$
$$
z=\frac{-(a_s\lambda+b_s)\omega+A_sb_s\lambda+b_sB_s-a_sC_s}{\Delta}.
\tag{8}
$$
本次把 (8) 代回 (2)、(7)，两个完整原式均为零。只倒 (3) 的当前明确原图单位，没有另一个规范头或值判别式分母。

把 $(a_sT+c_sz)^2$ 用三条 (5) 降次，再用 (8)，得到
$$
q_\omega=\omega^2+\beta_1(\lambda)\omega+\beta_0(\lambda),
\qquad \deg_\lambda\beta_0,\deg_\lambda\beta_1\le2.
\tag{9}
$$
若 $\widetilde F_i(\omega)$ 是 $F_i$ 代入 (8) 的准确二次式，则存在本次实际返回的三个原权系数 $\eta_i$，使
$$
q_\omega=\sum_{i=0}^2\eta_i\widetilde F_i.
\tag{10}
$$
这解释了 (9) 的首一性来源；不是另加一条仅数值相合的二次关系。

## 4. 精确六乘二模块

令 $\gamma_i=[\omega^2]\widetilde F_i$，并定义
$$
\ell_i=\widetilde F_i-\gamma_iq_\omega
=r_{i0}(\lambda)+r_{i1}(\lambda)\omega.
\tag{11}
$$
由 (10)、(11)，有完整理想等式
$$
(\widetilde F_0,\widetilde F_1,\widetilde F_2)
=(q_\omega,\ell_0,\ell_1,\ell_2).
\tag{12}
$$
在首一代数 $S=R[\lambda,\omega]/(q_\omega)$ 中，$S$ 作为 $R[\lambda]$ 模由 $1,\omega$ 自由生成；这是只对单个首一二次的事实，不是说加入原关系后的商仍自由。

理想 $(\ell_0,\ell_1,\ell_2)\subset S$ 作为 $R[\lambda]$ 模，恰由
$$
\ell_0,\ \omega\ell_0,\ \ell_1,\ \omega\ell_1,\ \ell_2,\ \omega\ell_2
\tag{13}
$$
生成。因为每个 $S$ 系数都唯一写成 $a+b\omega$，(13) 保留全部倍数，不只必要的有限几行。每个实际 $\omega$ 倍行在基 $(1,\omega)$ 下是
$$
(-\beta_0r_{i1},\ r_{i0}-\beta_1r_{i1}).
\tag{14}
$$
本次三个 (11)、三个 (14) 及 (10) 均完整乘回。

因此原四式商精确为两生成元、六条模关系的余核。实际六行的两个 $\lambda$ 次数依次为
$$
(4,4),(6,6),(4,4),(6,6),(4,4),(6,6).
$$
原二次的三个系数 $\lambda$ 次数是 $(2,2,0)$。所有 90 次参数分母除法都返回原乘积，支持严格包含于 (1)、(3) 的已声明开图。

这不是一个关于 $\lambda$ 的首一有限模型；尚未得到纯权非零必要曲线或原图空性。完整 N/P 值条件还须在同一原呈示中继续加入。

## 5. 唯一实际执行

[源码](../notes/2026-11-28-unit211-Phi-zero-corrected-N1-slope-six-by-two-original-model-8542.py)：

- blob fd9d3d01d4f036cd2e6c9fa07bd31d3f41bd6824；
- SHA256 ca5334ebeee6b671156c473349cfc7acfc49adc7007f5c214ebd8fc22aa4024d；
- 8656 字节；唯一依赖为正确四头源 SHA256 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7 的必要定义前缀；
- run 46110462941 / job 140872622742；
- 源和实际 pull 均为 7b4089933991daf22ec0261fa2510ca07aecb069；
- 2026-11-28 05:05:14.045582 UTC 实际 pull，两 README blob 未变；
- 1.946327612 秒、75596 KiB、内层退出 0；
- stdout 4044 字节，SHA256 1749086af8ef304ec81a76f3c38659addd9857c17bbf698b0f2de0e211ba0c4e。

[实际小回执](../notes/2026-11-28-unit211-Phi-zero-corrected-N1-slope-six-by-two-original-model-execution-8542.json)记录全部阶段。此源没有执行旧错误 first-head、旧 Gaussian/结式，亦未重跑正确共同四头的排除计算。它只再生本条需要的四个正确原式，随后执行上述新的斜率及精确呈示目标。

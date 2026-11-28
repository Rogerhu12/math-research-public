# 正确 Phi：三个真实首项合成后仅保至多 392 个例外权点

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：已成原结论的纸面推论，无新执行。** 当前正确 $\Phi=0$、两个 singleton 谱值不同、物理 $D\ne0$ 图上，原两条 $\lambda$ 六次与新的全图 t 六次至少有一个可首一化，除非权点属于一个至多 $392$ 点的集合。这个数字只界定尚未由这些首项证明有限纤维的例外权支持；不界整个原图的几何点数，也不排除这 $392$ 个权点的任何纤维。

## 1. 同一原权环与三个实际头

引用[两个正确原六次头的 434 权支持定理](R150-appendix-unit211-Phi-zero-corrected-two-sextic-heads-434-common-weights.md)，以及[完整六原乘子与 H28](R150-appendix-unit211-Phi-zero-corrected-whole-t-sextic-six-original-multipliers-and-H28.md)。两者均来自纠错后的真双数乘法。

取共同已付权环
$$
\mathcal A_*=\mathbb C[u,Q,
 (uQ\delta sK_wLM_nABm(2\ell-1))^{-1}],
$$
$$
\begin{aligned}
&s=u-1,\quad\delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\quad\ell=L/Q,\quad m=u-\ell,\\
&M_n=2uL-L^2-u^2Q,\quad
A=4s^2-Q,\quad
B=-Q^2+(12u^2-20u+8)Q-16s^2.
\end{aligned}
\tag{1}
$$
旧正确 $\lambda$ 模型实际分母仅用 $Q\delta sK_wLM_nAB$；额外的 $u$ 来自整个同一原图的独立零基点 mean 排除。$A,B$ 的整个正确零支已闭。新 t 模型只用 $uQ\delta sK_wLM_n(2\ell-1)$；$m$ 由独立真等权来源已付，加入共同环不会删掉当前任何原物理点。所有这些均为纯权单位，不含新首项或物理 D 范数。

两套几何坐标通过[全 t 参数原恢复](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)的仿射变换相接：
$$
\lambda=\frac{Jf-QV+bcQt-sT_0}{P_{02}},\qquad
T=-\ell+\frac{T_0(f-V+bct)}{P_{02}},\qquad z=Qt.
\tag{2}
$$
固定 t 时，$(f,V)\mapsto(\lambda,T)$ 的行列式为 $-P_f/P_{02}^2$，它是 (1) 中的单位。因此这些原六式及头模型在同一原系数范围比较，不把两个不同局部图的付款互相借用。

令 $h_{\rm NP},h_{\rm ov}$ 为旧两个正确原 $\lambda^6$ 头，$h_t$ 为新原 $t^6$ 头。其实际完整分解在 (1) 中给
$$
h_{\rm NP}=U_{\rm NP}H_{31},\qquad
h_{\rm ov}=U_{\rm ov}H_{14},\qquad
h_t=U_tH_{28},\qquad U_i\in\mathcal A_*^\times .
\tag{3}
$$
旧头中的额外 u 因子已由全图 u 单位吸收。这里 $H_{14}$ 指 **旧 corrected lambda-overlap 六次头**，并非新 N1 斜率的 $H_6H_8$。

| 原剩余头 | 总次数 | $(\deg_u,\deg_Q)$ | 准确规范 SHA256 |
|---|---:|---:|---|
| $H_{31}$ | 31 | $(28,17)$ | 55f47b10ee1ed5d8f256fb729e92b52e66312911c479e17fdddb25a3fac7ca35 |
| $H_{14}$ | 14 | $(13,8)$ | 7ef7a4a7f2d14f3e13f9dbdca25d93af1b7f5e2465cf688e0763293dedb38d05 |
| $H_{28}$ | 28 | $(26,15)$ | 49c4eef279d2593cbf0355dcac116dbfb6505fa5e785866f3cc02fb2a595de49 |

$H_{28}$ 的完整 QQ 因式仅一个不可约因子、重数为一；上述标量归一不影响不可约性。这里仍不称它绝对不可约。

## 2. 不需新 gcd 的严格 392 界

因为 $H_{28}$ 在 $\mathbb Q[u,Q]$ 不可约，而非零 $H_{14}$ 的总次数仅为 14，
$$
\gcd_{\mathbb Q[u,Q]}(H_{28},H_{14})=1.
\tag{4}
$$
这是已成 QQ 因式和严格次数的直接后果，无需执行新的 gcd 门。

(4) 使理想 $(H_{28},H_{14})$ 没有高度一素理想：否则在二元多项式 UFD 中会有一个非恒定共同因子。故该商是零维有限型 QQ 代数，因而有限维。将其忠实平坦扩张到 $\mathbb C$ 后仍为有限维代数，所以两条曲线没有共同复曲线分量；这里不把二元 gcd 一误作单位理想。

齐次化后也不产生共同无穷远直线分量，因为两者各按真实总次数齐次化，均不被齐次化变量整除。平面 Bézout 因此给其不同复交点数，乃至完整有限交长度，上界
$$
28\cdot14=392.
\tag{5}
$$
定义真正的三头共同零权集
$$
E_*=\{H_{31}=H_{14}=H_{28}=0\}
       \cap\operatorname{Spec}\mathcal A_*.
$$
它包含在 (5) 的有限交中，所以
$$
\boxed{\ \#E_*\le392.\ }
\tag{6}
$$
这是三头合成后对旧 $434$ 例外权支持的收紧，不是对整个原系统方案长度的计算。

## 3. 例外外的有限性与仍保留的原纤维

在 $E_*$ 外至少一个真实头非零。若 $H_{31}$ 或 $H_{14}$ 非零，已成原 $\lambda$ 六次及三生成性给
$$
\lambda^j(1,T,z),\qquad 0\le j\le5
$$
十八个必要生成元；若 $H_{28}\ne0$，新全图 t 六次及真三均值给
$$
t^j(1,f,V),\qquad 0\le j\le5
$$
十八个必要生成元。各断言均针对尚未反演几何 D 的必要代数，且不要求自由。

因此 $E_*$ 外各固定权点的相应原几何纤维有限；再施加物理 $D\ne0$ 或其它原值条件不增加纤维维数。不能据此声称 D 局部化后仍有限于整个权环。$E_*$ 上的全部 $\lambda,t$ 降阶、整参数纤维、所有重根以及后续原条件继续保留。

本文没有新运行、模点测试或系数载荷。使用的既成实际来源分别是 run 46132787438 的两个正确 lambda 头、run 46150593405 的全六原乘子和 H28；没有重放它们的因式或原组合门。普通 ISP 与整个正确 Phi 均未由 (6) 排空。

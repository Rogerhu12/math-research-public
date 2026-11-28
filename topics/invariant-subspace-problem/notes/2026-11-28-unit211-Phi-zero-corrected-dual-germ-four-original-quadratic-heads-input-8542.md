# 更正原二重点均值后的 Phi 四个二次头：新输入

日期：2026-11-28（Asia/Taipei）。源为 `2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py`，SHA256 `5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7`，7656 字节，自含，无文件依赖。首次预算 120 秒、1 GiB。只生成新的四个二次头，不执行任何旧投影、Gaussian、行列式门或旧头零排除。

## 真实原式

本输入仅使用新七变量整数证书
`2026-11-28-unit211-corrected-dual-germ-compact-original-identities-8542.js`
（SHA256 `a7f1db4305a58c2e733c573158f746d5b4adc312090472de25e472c96ddfeaae`）
实际返回的正确 $\overline R$ 与独立 $W_4,O,N_1$。旧紧凑 $E_1$ 的错误及隔离见对应 correction-and-dependency-quarantine 笔记。

在 $\Phi=0$ 上
$$
\ell=1-\frac{2(u-1)(u-2)}Q,\qquad
\delta=1-Q,\quad m=u-\ell,\quad
M=\ell(2u-\ell Q)-u^2,\quad bc=\frac{M}{4\delta}.
$$
保留 $Q\delta P_f\ne0$ 的原坐标图，定义
$$
T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q,\quad
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,
$$
$$
P_f=T_0(J-Q),\quad G=\lambda P_{02}+(u-1)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,\quad f=-P_c/P_f.
$$
这些是原 $E_0/N_0/P_1$ 的恢复；不使用错误 $E_1$。随后
$$
v_n=Jf-G+bc\,z,\qquad n_n=Q(T_0+4uf)-2v_n,\qquad z=Qt.
$$
正确的第一行是
$$
\boxed{\overline R=
4Q(f-u)(v_n-Qf)+bc\,z^2
+z(4bc\,uQ-\ell v_n)
+\frac{m}{2\delta}z n_n.}
$$
后三行由已纠正证书独立核过的 $W_4,O_{\mathrm{compact}}/\rho$ 和真实 $N_4$ 极化构造，源码逐项列出。它们不因第一行更正而改变；全部原恢复仍须在明确原坐标图内解释。

## 本次确切目标

每行按 $(1,T,z,T^2,Tz,z^2)$ 完整重建并返回，得到真实 $4\times3$ 二次头 $H$。对四种三行选择分别算完整 $3\times3$ 行列式，其分子、分母及因式分解全部乘回。所有系数分母只允许已声明的
$$
Q(1-Q)(u-1)(Q+4u-4)
$$
支持，因为 $P_f=4(u-1)^2(Q+4u-4)$。这只说明指定坐标图内的来源，不据此排除任何尚未独立支付的零面。

若四个极大子式都为零，则确切记录头秩至多二，绝不沿用旧三生成元。若其中非零，则仅在相应真头开图可以重新研究三生成元；本次不宣布该头已全图成为单位。四分子的 gcd 不等于它们完整共同零集，程序明写该区别。任何 $m,u+Q-1,2\ell-3$、旧 H1、H42、$C_5^*$ 或旧 583 模型均未作为单位或输入使用。

输出只保完整小因式、次数、项数、SHA 和实际回乘状态。尚未执行，不预称某个头非零或其零图关闭。

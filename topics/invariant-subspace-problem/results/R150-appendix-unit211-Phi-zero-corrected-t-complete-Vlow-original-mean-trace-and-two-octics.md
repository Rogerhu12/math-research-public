# 正确 Phi：完整 Vlow 的 t 原三生成来源与两条真实八次关系

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：唯一首次实际返回成功。** 当前正确 $\Phi=0$、两个 singleton 谱值不同、物理 $D\ne0$ 图上，完整孤立值条件的原清分母式 $V_{\rm low}$ 在真实 $(t,f,V)$ 中总次数为 5，且有普通原均值身份
$$
V_{\rm low}=r_V(1,f,V)^t+\nu_V(\mathcal R,E_{B,e},E_{B,o}),
\qquad
\deg_t r_V=(5,4,4).
\tag{1}
$$
从 $(N_1,NS,V_{\rm low})$ 和 $(N_1,PS,V_{\rm low})$ 得到两条全原必要八次 $C_{8,N}$、$C_{8,P}$，分别总次数 71、75。它们的整个首项零纤维仍保留；没有全权首项单位或排空结论。

这次输入新增完整 $N_4(V_{\rm phys})$ 来源，不是再次投影旧 weighted 六式。实际依据为 run [46151922972](https://github.com/Rogerhu12/math-research-public/actions/runs/46151922972)、job 141000216528，内层 exit 0；见[小执行回执](../notes/2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542-execution.json)。

## 1. 原系数范围和完整孤立值来源

沿[真全 t 参数三均值](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)，置
$$
s=u-1,\quad\delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\quad\ell=L/Q,\quad m=u-\ell,
$$
$$
M=M_n/Q=\ell(2u-\ell Q)-u^2=4bc\delta .
$$
本次只使用原已付权环
$$
\mathcal A=\mathbb Q[u,Q,
 (uQ\delta sK_wLM_n(2\ell-1)m)^{-1}].
\tag{2}
$$
其中 $2\ell-1$ 来自整个正确 ell-half 排除，m 来自[完整真等权来源静审](../notes/2026-11-28-unit211-Phi-corrected-equal-weight-m-unit-static-provenance-8542.md)。斜率 $\Delta$、$H_6,H_8,H_{28}$、任何新首项以及 D 都未反演。

记
$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3,\qquad
w=\lambda-1-T,\quad W_1=T_0/2+2uf.
$$
原恢复为
$$
\lambda=\frac{Jf-QV+bcQt-sT_0}{P_{02}},\qquad
T=-\ell+\frac{T_0(f-V+bct)}{P_{02}},\qquad
A_1=2f-2V+2bc\,t.
\tag{3}
$$
它们对 $(t,f,V)$ 仿射，分母只在 (2)。

[九自由变量的完整 scaled N4 三式](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)给
$$
\ell^2N_4(V_{\rm phys})=Z_0+Z_1\sigma+Z_2\sigma^2,
\tag{4}
$$
其中 $V_{\rm phys}=(1,w,h,k)$ 是孤立值向量，$V=bX+cY$ 则是 Gram 均值，不能混淆。设 $c_\lambda=3-2\lambda$，准确三个系数为
$$
\begin{aligned}
Z_0={}&\ell^2A_1+4\ell^2(1-2\lambda)f+2\ell fD
 +2\ell uw(\ell c_\lambda+T)\\
&+2V(\ell^2+\ell c_\lambda T+T^2)+2bc\,t(T^2-\ell^2),\\
Z_1={}&2(\ell c_\lambda+2T)(uV-\ell W_1)
 -2\ell Mw+4bc\,mTt,\\
Z_2={}&2[(u^2-\ell^2Q)V-2m\ell W_1-\ell Mf-bcMt].
\end{aligned}
\tag{5}
$$
这里 $\rho^2=\delta$，
$$
h=1+(T+m\sigma)/\ell-\rho\sigma,\qquad
k=1+(T+m\sigma)/\ell+\rho\sigma .
$$
两条原 shifted moment 误差给 $q=M\sigma^2-D$、$H=K-2mD\sigma$。因此
$$
V_{\rm low}=DZ_0+\frac{KZ_1}{2m}+\frac{D^2Z_2}{M}
\tag{6}
$$
具有完整原身份
$$
V_{\rm low}
=D\ell^2N_4(V_{\rm phys})
 +\frac{Z_1H}{2m}-\frac{DZ_2q}{M}.
\tag{7}
$$
(7) 也见[正确完整 I10 原来源](R150-appendix-unit211-Phi-zero-corrected-individual-NP-full-NV-I10-and-two-decics.md)。本次保 (5) 的全部三个系数，没有用一个分量、Phi 倍数或 W 特域的 f 消失公式替代它。D 只正乘；在完整物理原方程下 $V_{\rm low}=0$。

## 2. 真实五次及普通原均值乘回

由 (3)、(5)，按 $(t,f,V)$ 总次数有
$$
\deg D=2,\quad\deg K=3,\quad
(\deg Z_0,\deg Z_1,\deg Z_2)=(3,2,1),\quad
\deg V_{\rm low}\le5 .
\tag{8}
$$
首次运行实际给 $V_{\rm low}$ 总次数恰为 5。这里没有把权次数混入原几何次数，也没有用 $\lambda=1$ 的最高函子替代原值。

完整原式的分子 11783 项，分母为纯权 140 项；原最高五次分子 3623 项。其准确 profile 分别为
$$
\begin{aligned}
&{\rm num}(V_{\rm low}):
\texttt{d480bee064e223238ab69eee31d93d6eff5cabc9301c6defa7d62a8d062db988},\\
&{\rm top}_5:
\texttt{d099a754840ad408466f6560fbabde2d8f6119ed2a0e6b8f36f08c53e169a05a}.
\end{aligned}
$$
这些是完整原对象的身份，不保存可重算系数载荷。

令 $F=(\mathcal R,E_{B,e},E_{B,o})$。其正确二次头行列式
$32uQ(2\ell-1)/M^2$ 在 (2) 中为单位，故有三条真实首一规则。源码只再生这些已成必要定义；新的十八步普通降次对 $V_{\rm low}$ 逐次累积 **三条原均值乘子**，最后展开并返回 (1) 的完整普通多项式身份。

实际三坐标为：

| 坐标 | t 次数 | 分子 $(\deg_u,\deg_Q)$ | 分子项数 | 分子 SHA256 |
|---|---:|---:|---:|---|
| $r_{V,0}$ | 5 | $(39,23)$ | 3274 | baa8cd4b46098d259783d15a7012b550bdb2a29bee95c12912e0b9a5e5c4aee7 |
| $r_{V,f}$ | 4 | $(37,22)$ | 2412 | 9e6cb8870a5c0853b910076ba0c2bd0f6059338f53b302ead34889237ceec108 |
| $r_{V,V}$ | 4 | $(36,21)$ | 2249 | 8e60199f7e082e438cad0c4d324811a2fc70163562429f7b162382397ead1cbe |

三个实际均值乘子的 $(t,f,V)$ 总次数均不超过 3，所有分母都只含 (2)。完整普通返回保证 (1) 不依赖三列自由、乘法结合或唯一正常形假设。

## 3. 两个真正新三行 cofactor

已成原参数定义给
$$
r_Ne=N_1-\eta F,\qquad
r_{NS}e=NS-\tau_{NS}F,\qquad
r_{PS}e=PS-\tau_{PS}F,\qquad e=(1,f,V)^t.
\tag{9}
$$
本次只按既成九个分子 SHA 再生它们和必要原迹，未重做旧 centered 模型、weighted pair 或全六终端门。

分别取
$$
(r_0,r_1,r_2)=(r_N,r_{NS},r_V),\qquad
(r_N,r_{PS},r_V).
$$
定义两列 cofactor 的三个实际乘子
$$
\begin{aligned}
\mu_0&=r_{1,f}r_{2,V}-r_{1,V}r_{2,f},\\
\mu_1&=r_{2,f}r_{0,V}-r_{2,V}r_{0,f},\\
\mu_2&=r_{0,f}r_{1,V}-r_{0,V}r_{1,f}.
\end{aligned}
\tag{10}
$$
清三乘子实际纯权分母后，只约除 **全部三个乘子的共同因子**，再完整乘回所有三坐标。两个共同内容实际均为常数一。所得
$$
\sum_{i=0}^2\widehat\mu_i r_i=(C_{\rm raw},0,0).
\tag{11}
$$
只剥 $C_{\rm raw}$ 分子中旧已付权因子、运输同一尺度到三乘子后，第二次完整返回规范多项式 $C_{8,N}$、$C_{8,P}$。

三行次数为 $(2,1,1),(3,2,2),(5,4,4)$，所以 determinant 的 t 次数上界为八；这次两个实际次数均达到八。数据为：

| 必要原式 | $(\deg_u,\deg_Q,\deg_t)$ | 总次数 | 项数 | 规范 SHA256 |
|---|---:|---:|---:|---|
| $C_{8,N}$ | $(60,36,8)$ | 71 | 11329 | 7be3f86635bb87c309fc15c6b386303624c0ca951e8578dce37d490fc925d3ea |
| $C_{8,P}$ | $(64,38,8)$ | 75 | 12661 | 5d36181cbdf2fec8a58faea9dae5688cbd00e7a3c2430b74e5e9ace407ca4b5b |

两个未规范原标量的实际分母相同，双次数 $(2,4)$、总次数 5、10 项，SHA
95745ff4a78cfa74c3e5d5f95aa2ba34b2743cc7bfb077e22c18de0d72b7448b；
全部只含原已付权。

令 $G_0=N_1$，$G_1=NS$ 或 PS，$G_2=V_{\rm low}$，并令相应迹为 $\tau_0=\eta,\tau_1=\tau_{NS/PS},\tau_2=\nu_V$。由 (1)、(9)、(11)，准确原来源为
$$
C=\sum_{i=0}^2\widehat\mu_iG_i
 -\left(\sum_{i=0}^2\widehat\mu_i\tau_i\right)F .
\tag{12}
$$
所以
$$
C_{8,N},C_{8,P}\in I_7:=I_6+(V_{\rm low})
\tag{13}
$$
于整个当前权环成立。实际计算返回三坐标及新的完整普通 Vlow 迹；(12) 合并已成原迹即可，不冒称另行实展了巨大七原乘子。

## 4. 新首项与所有零纤维仍保留

实际 t 头为：

| 原头 | $(\deg_u,\deg_Q)$ | 总次数 | 项数 | SHA256 |
|---|---:|---:|---:|---|
| $[t^8]C_{8,N}$ | $(60,30)$ | 63 | 1135 | c3308082837a31eb7f495da4ea41e422a950f977ffc9eaca0158aa90b1edf1bb |
| $[t^8]C_{8,P}$ | $(64,32)$ | 67 | 1275 | c7ce415c3c2eebf5cba7673e78dad2d467a2cbb9b405418df26121c83e6c9fc0 |

本次没有对这些头作因式或单位理想测试，也没有取它们的逆。所有新头零面、旧 $H_6,H_8,H_{28}$ 零面以及原单项系数降阶纤维均包含在 (12)、(13) 中。辅助 I7 不被宣称为完整物理系统的充分条件。

完整五次来源和最高部分保留供后续真正射影条件使用；当前两个非零八次只增加必要条件，不由多项式非零推整个原图空，不给新有限点数，也不缩减已成 392 例外权支持。

## 6. 唯一实际身份

[源](../notes/2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542.py)与[冻结输入](../notes/2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542-input.md)均已保存。

- 源 Git blob dec77452e4631b4370e72d1b9491da01e35547b3；17124 字节。
- 源 SHA256 0800a0f6ba0cad4cc4ddc7a592525c198bcc213bfa36df568ec0e9301b8f4335。
- 唯一 run/job 46151922972 / 141000216528，attempt 1；内层 exit 0。
- 源提交 53649d1575a460810c42229e6b9fdad16e3e5158；实际 pull c3e2f5d48781f6a9850afa9d36c724299bae4406。
- 规则读取 2026-11-28T13:54:34.219627+00:00；两 README 未变。
- driver 3.755020568 秒；数学 3.674368506 秒；峰值 58964 KiB。
- stdout 8502 字节，SHA256 ce4bdebf8e91e25ab10fb62ff80df040f32775b7787e57d835631969f8b14c7f。
- 十八步新 Vlow 普通降次、一个完整原均值身份、三个新坐标、两次 cofactor 共六坐标和规范化后的六坐标均返回；184 次精确除法乘回。

自含零依赖，固定总 120 秒 / 1 GiB；无大系数载荷、缓存或分片。未重跑旧 weighted scalar、全六终端、H28 或旧 corrected lambda 十次证明门；旧错误 compact 链保持撤回。普通 ISP 仍未由本文完成。

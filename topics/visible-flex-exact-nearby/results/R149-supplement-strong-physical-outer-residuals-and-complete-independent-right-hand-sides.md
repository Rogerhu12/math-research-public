# OHR：同一 selected 的强物理 Robin 与两列真实外端、普通体源

固定原 $Q=Q_0+\delta_*Z,\nu=\nu_0+\delta_*$，$R=25/8$ 和同一许可物理 height 背景 $\|f_B\|_{\dot A^2_\sigma}\le2^{-60}$、$\sigma\ge1/16$。以 $f_i$ 表示 Newton 或 $q_\nu-Z$ 的已知普通源，用 OA.2、NP.15 的负号取相应真实 Robin 和独立物理 mean 残差 $r_i,m_i$。此处给这两个给定的源算出强边界大小及沿正区所有独立注入的费用。下文的 $v_i$ 是同一完整 high inverse 对已知 high 源与这两个物理残差的 particular 解。所有其它源、height 方向、根稳定量、head、原跳及全局行继续在线性分解的其余部分求解。

| 实际量及其单位 | Newton 上界 | $\nu$ proposal 上界 |
|---|---:|---:|
| $\|r_i\|_{H^{1/6}_\theta}$ | $10^{-14}$ | $1.21\,10^{-11}$ |
| 强正图第 4 槽的独立外端注入 | $2.2\,10^{-13}$ | $2.55\,10^{-10}$ |
| $v_i$ 的原强 frame 体、collar sup 与根补支的每一项 | $3.2\,10^{-13}$ | $6.0\,10^{-10}$ |
| 全 high 的 $\|v_i\|_{L^2([r_*,R];L^2)}$ | $8.0\,10^{-13}$ | $1.51\,10^{-9}$ |
| 全 $\|P_Lf_i+B_{LH}v_i\|_{L^2([r_*,R];E_L)}$ | $7.051\,10^{-8}$ | $2.958\,10^{-5}$ |
| 含实际 $v_i(R)$ 返回的物理 charted-right97 独立数据 | $9.0\,10^{-15}$ | $6.31\,10^{-11}$ |

## 同一真实角图的六分之一阶边界值

Newton 的 [OA.1](R141-supplement-actual-selected-physical-outer-residual-values.md) 第一球记 $n$。原 O.2 的基准先在完整 $A^0$，O.7 的偏移在 $L^\infty$，O.9 及 O.11 在 $L^2$。故其正预算 O.12 本身已控制 $\|r_N\|_2$。用它的原完整球读回。原 moving 非均值 $\|u\|_{A^0}<2\,10^{-12}$，$\|v_\perp\|_{A^0}<10^{-11}$，$|m|>5.84$，$J=\theta'=1+v_\perp/m$。已知 $Q$ 的频率至 $384$，设 $C=.172$。对实际物理函数 $B\circ\theta=u/v$，
$$
 \|B_\theta\|_\infty\le384 C\|u\|_{A^0}
 (1+C\|v_\perp\|_{A^0})/(1-\|v_\perp\|_{A^0}/5.84).
$$
原 $\mathcal Z=P_{\ne0}(v^{-1}\circ\phi)$ 有整球 $Z_1\ge\|\mathcal Z_\theta\|_{A^0}$。长段 DN 的真实平移协变给 $\partial_\theta d=D_{\mathcal Z}d[\mathcal Z_\theta]+D_{f_B}d[(f_B)_\theta]$。它在完整含正负 Fourier 模的空间成立；先平移再微分允许反射轴同时平移。两个线性主乘子连续交换 $\partial_\theta$，各自范数至多 1。取 [实际 DN](R133-supplement-actual-full-real-delta-outer-and-positive-high.md) 的 $L^2$ 两个整行 $T,U$，于是
$$
 \|r_N\|_{H^1}\le n+\|B_\theta\|_\infty+(1+T)Z_1+16 U2^{-60}<2\,10^{-10}.
$$
Fourier 平方和 Hölder 插值给 $\|r_N\|_{H^{1/6}}^6\le n^5\|r_N\|_{H^1}<10^{-84}$。整个 $d$ 是非线性外图；此处取它在原实际值的角导。没有把该值当作某个 DN 的范数。

对参数列使用相同外图的解析逆角。写 $t=1/32$、$s=1/64$、$(\xi,\zeta)=Z(R)$。原 43615531666/1 完整边界给 $\|\phi-\mathrm{id}\|_{A_s}<t-s$，故每个 $g$ 都有 $\|g\circ\phi\|_{A_s}\le\|g\|_{A_t}$，由各 Fourier 指数的代数范数级数即得。取 $U_0=1.646\,10^{-9},V_0=9.616\,10^{-9}$ 为 $u,v_\perp$ 的原 $A_{1/8}$ 界，$C=(.172)>1/(5.84-V_0)$。原 exact 193 endpoint 的 $A_t$ 方向球给 $X=2.31\,10^{-11}$、$Y=1.35\,10^{-10}$ 分别支配 $\xi,\zeta$，后者含非零原确切均值 $m_Z$。在同一角，NP.10 给
$$
 \|\dot\phi\circ\theta\|_{A_t}\le P=C(Y+|m_Z|V_0/5.84)/4 .
$$
使用 $u_\phi,(v_\perp)_\phi$ 从 $1/8$ 到 $1/32$ 的 16 倍费用、以及 [NP.11](R145-selected-nu-proposal-positive-source-and-outer-rows.md) 全部 inverse-angle 项，可取
$$
 D_B=CX+U_0C^2Y+(16U_0C+16U_0V_0C^2)P,\qquad
 D_C=C^2Y+16V_0C^2P
$$
支配 $\dot B,\dot C$ 的物理 $A_s$。$\langle k\rangle\le1+|k|\le(3/2)^6e^{6s|k|}$，故 $H^{1/6}$ 嵌入费仅 $3/2$，去均值在物理 Fourier 空间收缩。令 $T_6$ 是原全 DN 的 $H^{1/6}$ 行。于是 $\|r_\nu\|_{H^{1/6}}\le(3/2)[D_B+(1+T_6)D_C]<1.21\,10^{-11}$。两物理 mean 残差仍分别由 OA、NP 给出，$|m_N|<2.048247\,10^{-19}, |m_\nu|<4\,10^{-18}$。

## 正图把物理 RHS 送回全部 193 行

对 Newton 和 $\nu$ 各自令 $R_6=\|r_i\|_{H^{1/6}}$，$R_-=\|r_i\|_{H^{-5/6}}$，$M=|m_i|$。$H=\|P_H f_i\|_{L^2_rH^{1/3}}$ 由 [NHT](R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md) 给 $1.17560\,10^{-19}$ 与 $1.254870\,10^{-9}$。$B_i=e_R^+R_6+e_C^+M$，其中 $e_R^+,e_C^+$ 是同一 43615531666/1 原 strong exterior 的 ordinary Robin 和独立 mean 输出球。未知 height 另有该图的 $e_F^+$ 列。给定的 $v_i$ 在线性分解中恰由 $P_Hf_i$ 与两外行驱动；该 particular 在根的稳定坐标与其独立 jump 坐标确为零。$P_H f_i$ 在 collar/body 两段的平方和至多 $H^2$。由 [强正根实际图](R133-supplement-actual-full-real-delta-positive-high-root-to-regular-graph.md) 完整原行的第 2、3 槽 Euclidean 范数及第 4 槽得
$$
 S_i=.182H+1.439 B_i,\qquad C_i=.459H+3.62 B_i .
$$
$S_i$ 同时支配 body $Z$、collar $Z$ 的 sup 及根补支；$C_i$ 支配整个 high 的普通原态 $L^2$。这是强正图的实际输出，含全部 $|j|\ge97$。$L_*=\max(58/5,L_b)$ 是原完整 raw high-to-low 乘法范数。此处有完整普通原态可取 $\|B_{LH}v_i\|\le L_*C_i$，无 $H^{-1}$ 转普通的导损。加 [NA](R141-supplement-actual-complete-positive-Newton-source.md)、NP 的真实 low source 即得表中 low 体源。

令 $y_i=P_H(v_i)_2(R)$。真实物理 Fourier 频率 $N\ge388$ 处 Airy frame 第二行为 $N^{-1/6}(p_N+g_N)^{-1/2}(Z_s+Z_u)$，符号相位为等距，$p_N(R)>1/8,g_N(R)>0$。取 $H^{-5/6}$、用 $\sqrt2\sqrt8=4$，在同一真实端点得 $\|y_i\|_{H^{-5/6}}\le(4/388)S_i=:Y_i$。这是从完整原 trace 到 WOB，未从 $L^2_r$ 制造迹。

记 $\mathcal P(u,v)=((\Theta_j u_j)_{j=1}^{96},\Pi v)$，$\Theta_j=\langle4j\rangle^{-5/6}$。对底端 physical 行中的直接 affine 以及 $v_i$ 的 high 回边，准确 signed 右数据为
$$
 d_i=\mathcal P\{\mathcal B_{R,p}(0,r_i,m_i)+\mathcal B_R^H y_i\}.
$$
两项在 even 非均值槽各为零，故原 hybrid 的 $+13v_j/80$ 对这项无另加贡献。只给该 RHS 分量指定 height 方向零；实际 height 列仍同时走两条外路。由 [WOB.4、7](R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md) 原有 $B_a,C_a,\mu_C,E_-,\mu_-$，得到原参考输入单位的
$$
 |d_i|^2\le (B_aR_-+C_aM+E_-Y_i)^2+(\mu_CM+\mu_-Y_i)^2 .
$$
先做 nonmean 到 $H^{-5/6}$ 的真实物理投影，不出现把这项先变 raw 后再整体放大的 $\langle384\rangle^{5/6}$。独立 mean 未乘 $\Theta$。原实际 $R_-$ 为 OA 球与 NP 的 $9\,10^{-12}$。这样同时接回普通体源和 right97。它们是同一 $v_i$ 的相关输出，后继不能把两者任意赋为独立 signed 向量，更不能把范数当系数；取有向包含时允许保守的包含集。

在 [NRO.6](R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md) 及 NHT 的 selected 基点负窗预算内，另付已知 $\nu$ 物理外源的高端贡献至多 $(25.95\cdot9.00002+2.85\,10^{-6})1.439B_\nu$。故在保留完整 low 根与 head 反馈、其它根稳定/跳、实际 height、waist、holonomy 等原端口时，已分出的负体源、正侧高体源和已知物理外行的高迹部分合计 $<1.769\,10^{-5}$。同一高外源经 body 反馈到 low 后再返回的部分仍通过真正的 low 方程求解。这里没有得到未分项的总 $X,v$，也没有据此给全负窗 $.005$ 或真实非线性求解赋数。

完整有理验证入口为 [强物理 RHS reader](../scripts/fourfold_codazzi_selected_physical_outer_strong_rhs.py)。它对上述新组合只用小的完整已成记录，不重新生产任何端点、whole high graph、旧外图或旧源。

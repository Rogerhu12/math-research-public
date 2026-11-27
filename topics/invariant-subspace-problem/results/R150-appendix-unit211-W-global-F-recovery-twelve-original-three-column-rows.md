# R150：全余 W 的共同 F 消去、十二条完整原三列行与两个新参数约束

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

本次已把同一个原 F 的全域恢复实际送回整个原系统：原首一 qF 的代入条件没有丢失，六条 Gram/weighted 原式、r2、R6、个别 N/P 以及完整 N4(V) 共十二条行，均在同一个首一 S 三次环境中返回。全部三个真实乘法列也已完成。随后两个包含新原 NS 和完整 NV 的固定三行余子式给出 lambda 次数 9、13 的必要参数约束。

这是全当前 W 图的原三列输入及两个必要式；尚未排空 W。其参数首项整零面全部保留。

## 1. 已付共同恢复与原环境

[整个 G36 排除及共同 F 恢复](R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md)使三个原 F 一次行的共同权行列式 DeltaB 在当前 W 域处处非零。沿用
$$
R_i=A_i(S)+B_i(S)F,\qquad
\sum_i\omega_i B_i(S)=\Delta_B,
$$
得到
$$
F_p(S)=-\sum_i\frac{\omega_iA_i(S)}{\Delta_B},\qquad
F_{\rm lin}=F-F_p,\qquad \deg_S F_p\le2.
$$
此次实际核回全部三个系数列和
$$
\sum_i\omega_iR_i=\Delta_BF_{\rm lin}.
$$
Fp 的完整系数规范编码共 22916 字节，SHA256
a9ab8d63a70e8718bb9a7b17d0d0756ac58fdb107dea9ca1b35110cdf44f5e08。
它有三个 S 系数，其分子对 (e,k,lambda) 的最大分次为 (13,17,2)。所有分母只来自已经支付的原因子及本次显式使用的 G36。

原规则仍是[首一 T 三次与 F 二次](R150-appendix-unit211-W-global-monic-T-three-F-two-and-six-column-environment.md)
$$
q_F(F,S)=F^2+p(S)F+q(S),\qquad
q_3(S)=S^3+\beta_2S^2+\beta_1S+\beta_0.
$$
取 R 为当前已付系数局部化环，含 e,k,lambda。R[S]/(q3) 是自由三维的原首一环境；进一步加原方程所得商不假设自由，也不把 lambda 当作已消去的权参数。

冻结源本身仍写明确 G36!=0 补图，且不在源码内调用 G36 整排除作为运行门。第 1 段引用的独立完整定理使这个补图覆盖当前全部原点；这不改变原运行的准确作用域。

## 2. 精确原消去恒等式，特别保 qF(Fp)

对于任何原多项式 P，先采用已有首一 qF、q3 的确定约化，实际返回
$$
P=\overline P+t_Fq_F+t_3q_3.
$$
然后对 F-Fp 作首一除法，再对同一个 q3 作首一除法。此次逐条实际核回完整身份
$$
P=P_3(S)+T_Fq_F+T_3q_3+T_L(F-F_p),
\qquad \deg_SP_3\le2.
\tag{1}
$$
没有分别为不同原式选择 F 或 S。

qF 自身必须单独处理。若把 qF 先在旧二次环境中约成零就直接删除，将失去新 Fp 的必要条件。本次另外实际构造
$$
q_F(F,S)=Q_3(S)+U_3q_3+U_L(F-F_p),
\tag{2}
$$
并把 Q3 作为十二条行的第一条保留。它恰是 qF(Fp,S) 对 q3 的余式。

更一般地，因为 F-Fp 已由原行产生，先作 R[F,S] 到 R[S] 的代入映射，其核正是 (F-Fp)；随后再加 q3 及其余原像，所以全原商在当前单位局部化中准确同构于所有原式在 Fp 处取值后的 S 商。式 (1)、(2) 给出本次使用的实际原组合；这一等价不允许省略 Q3 或任何完整个别值条件。

## 3. 完整个别 N/P 与整个 N4(V)

保留六条原
$$
E_1,E_{Be},E_{Bo},N_1,N_S,P_S,
$$
以及原 q4 的二次余式 r2 和同值矩条件
$$
R_6=MK^2-4m^2D^3,\qquad m=u-\ell.
$$
这里
$$
D=\ell(2\lambda^2-2\lambda+1)-T^2,\quad
K=\ell^2(4\lambda^3-6\lambda^2+3\lambda-1)
 -3\ell T(2\lambda^2-2\lambda+1)+2T^3,
\quad M=4bc(1-Q).
$$

当前 W 原域原两值互异，D 非零的适用范围保留。源码不用 D 的逆；它采用已证明的较低 D 次必要式。为明确个别值没有被 weighted 行替代，写 d=1-Q、A0=1+T/ell，并令 n_b、p_b 是同一个原第二单点的 N4、P2 对 rho 的奇系数。两条实际返回为
$$
N_{\rm low}
=Dn_b+\frac{2\lambda P_{02}}mKA_0
 +\frac{4\lambda P_{02}m}{\ell M}D^2,
$$
$$
P_{\rm low}
=Dp_b+\frac{3P_{02}}{2m}KA_0^2
+\frac{P_{02}(3m^2/\ell^2+d)}{2mM}KD
+\frac{6P_{02}m}{\ell M}A_0D^2.
$$
它们来自原同值坐标 s=K/(2mD)、Ms^2=D 的完整奇部；与保留的 NS、PS、R6 和当前已付单位共同恢复个别偶部。这里不把它们外推到 D=0 的 h_U=k_U 碰撞域。

完整原 V 写成 V0+sV1。直接从原 N4 的全部二次型定义取得
$$
N_4(V_0+sV_1)=Z_0+Z_1s+Z_2s^2,
$$
其中 Z1 由完整极化差返回。源实际构造的第十二行是
$$
V_{\rm low}
=DZ_0+\frac{KZ_1}{2m}+\frac{D^2Z_2}{M}.
$$
在同一个 R6 条件下，它对应完整 N4(V) 的 D 清分母返回，既不是选取一个 weighted trace，也不是用 Phi 倍数偷换原式。

以上所有新乘法均在真正的首一 S 商中逐步完成，每次核回乘积与 q3 倍数。原 n_b、p_b、Z0、Z1、Z2 在进入该商之前也分别按 (1) 返回其完整原迹。

## 4. 十二条真实三列行

所有行都在 (1,S,S^2) 中逐系数返回，只剥已经支付的公共内容和清除已付分母。下表记录每条原有理系数行的分子最大分次；不是把分母或未付首项忽略后的自由秩断言。

| 原行 | 分子最大分次(e,k,lambda) | 规范编码字节 | SHA256 |
|---|---:|---:|---|
| original_qF_substituted | (33,43,6) | 716379 | 12340462eaa0321957b522fb3f07607039aa14c1074ebf4ca76e17db69d423f4 |
| E1 | (22,29,4) | 157692 | 921b08968fcfc18cfa08d2896407b265d23ca6b49c5d76a85f3e121d050987e4 |
| EBe | (24,31,4) | 203257 | 71cfc08440b6c17fbb48f9856aabd2a4e05aa7760e5b51cdf75c2200066ae7cb |
| EBo | (25,32,4) | 224955 | 7c97d59e8cf10c8e90239d6e96bb4383fd1cf7e8e906762fb6ce1ba3753bfab6 |
| N1 | (27,32,4) | 223558 | 5dfc91eea3464bf664e5b70b7224cb69713f9aa2654ddea1dd8a698538db82fe |
| NS | (35,48,6) | 902446 | d6b36b3311ed6f7c2455230c1d6d875bb450e3bc75eddfe6dcc2e9a49a59fcef |
| PS | (35,47,6) | 875840 | 9ccc217ad50c5dd2a0a7d8ca73ec6ab92de1861999de1bbbfb3d8b50cf04f0a1 |
| r2 | (14,16,6) | 83829 | 71f7e3dfc8b2fc62118dcf2558a7e57d70406692050edc53c06b4a788682688a |
| R6 | (28,30,10) | 661124 | f34dab4c99d57a06c98c46d8be60aecb200848e738f389b8f81b00d305190616 |
| D_linear_individual_N_odd | (43,56,10) | 2671091 | 20f6f98e53a6448e70399dc540bee99db0658b612526a1f7f6b2d31937692928 |
| D_linear_individual_P_odd | (46,59,10) | 3114985 | e88e2a53841e02d77245a74c4426a0294a212ff10ab77595eb2a5746d3144ad8 |
| D_linear_entire_original_N4_V | (35,43,10) | 1498298 | 400b27028a5a29e6baf0eb42fdbbc61891e1263c8e6d3a85f84b66db5a82c33e |

真实乘法列为
$$
S\cdot1=S,\qquad S\cdot S=S^2,\qquad
S\cdot S^2=-\beta_0-\beta_1S-\beta_2S^2.
$$
三条身份均实际按原 q3 核回。十二行和三乘法列的完整系数编码共 11349137 字节，SHA256
77481feb6106849a6d43f8f10516a5cc5042f368bdfb55ae67dbf4195d268c3b。
这些可重算的有理矩阵系数未作为大缓存保存。

整个构造实际完成 31 次新首一 S 约化乘回。每条原迹的独立字节数和 SHA 均保存在小回执，而不是只凭“环境维数为三”就宣称原条件已经等价。

## 5. 两个包含新完整原行的参数约束

取按上一节合法清理后的三系数行，分别组成
$$
\mathcal M_{NS}=
\begin{pmatrix}[E_1]\\[E_{Be}]\\[N_S]\end{pmatrix},
\qquad
\mathcal M_{NV}=
\begin{pmatrix}[E_1]\\[E_{Be}]\\[V_{\rm low}]\end{pmatrix}.
$$
对任一矩阵的三行 a,b,c，以最后两列的叉积 gamma 实际核回
$$
\gamma^{\mathsf T}\mathcal M=(C,0,0).
$$
因此每个原点均使 C=0，依据是同一个非零真值列 (1,S,S^2)^T；并不要求三列在最终原商中线性独立。

完整原列乘回后，只剥已付因子和非零有理内容，得到两个必要多项式：

| 原来源 | 原 cofactor 分次 | 仅剥已付后分次 | 剩余项数 | 剩余总次数 |
|---|---:|---:|---:|---:|
| E1,EBe,NS | (75,107,11) | (61,83,9) | 35250 | 124 |
| E1,EBe,完整 NV | (76,102,15) | (64,83,13) | 52885 | 131 |

二者的剩余准确系数 SHA256 分别为
987853f281f1e309d2372fb0c259eb581343e29a305806cebe2fee28ee74d56b、
6a40967b49ca634b511d3b1a50c20548314ae6223705ef3baed3d3a8524210d2。

其 lambda 首项再剥已付权因子后仍分别为 (e,k) 次数 (51,69)、(50,64) 的非恒定多项式，项数 2435、2274，SHA256 分别为
25e4fed1206c7fee1f2e5d22271e3b76d197aeab0626889c24cedc09e1da891c、
ae9a34c8db8e078a24e94f96e773d32eab7677ae8a6507579eb45429a54cf86b。
它们没有被支付为单位；全部首项整零面保留。

本稿不由两个多变量 gcd、单个非零 cofactor 或参数抽样推出空性，也尚不把它们称为整 W 的有限权点覆盖。

## 6. 准确的输出保存边界与唯一实际运行

源：[2026-11-28-unit211-W-G36-nonzero-full-original-three-column-return-8542.py](../notes/2026-11-28-unit211-W-G36-nonzero-full-original-three-column-return-8542.py)。

- blob：c827df2325c3573688f4ec1170c0754fad4e791f。
- SHA256：8430b819844aeecf8bd02619f8724e5c9ab75cad3a7c8c601b943cf515f79351。
- run/job：46054146284 / 140692444426。
- source commit：bb4e251d040f00a2b7838f91a6f526b4542588b2。
- 内层 exit 0，24.650824419 秒，峰值 218236 KiB。
- 十二行及三乘法列于 17.240806483 秒已完整返回；两新 cofactor 于 24.579512317 秒完成。
- stdout：18147 字节，SHA256 c835b06d29ee579a87d2db58074ee32114ccdf2f233c2dfe1f24a9311159ea58。
- 总预算 180 秒、4 GiB。

真实 pull 于 2026-11-27 19:05:20.092816 UTC 从 bb4e251d040f00a2b7838f91a6f526b4542588b2 更新至 19e776ccc88a4a2710c589e468b54bcf58c1034d，两 README 无变化；冻结源身份保持上列 SHA。

此次源仅在单个参数多项式规范编码不超过 8192 字节时打印其全系数。第 5 节两条实际参数多项式分别为 1667402、2656341 字节，所以当前归档保确定性源、全部原定义、完整乘回回执、尺寸和 SHA；没有声称准确大参数载荷已经保存。另有输出增强草稿 9105be21… 未执行，不能据它补写本次真实输出或重派旧 cofactor。

[小回执](../notes/2026-11-28-unit211-W-global-F-twelve-original-three-column-receipt-8542.json)保存所有实际数学标记和全部原迹 SHA。源码只再生 f5、505、394、af928、00c08 的原构造前缀，没有重跑这些旧完整参数门。后续转两条实际原二次之间更低度的 S 一次组合，完整保留新首项零面；本次已完成的原三列结果不等待那个后续输入。

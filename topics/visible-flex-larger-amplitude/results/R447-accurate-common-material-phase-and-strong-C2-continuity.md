# R447：准确共同材料相位、同一闭目标与全时间强 C² 连续

作者：ChatGPT /root/amplitude（AI 协作）。日期：2026-11-16。

本文承接 [R443](R443-common-material-angle-pullback-and-fixed-closed-target.md)，把实际相位公式、固定帽拼接、题目要求的全时间强 $C^2$ 连续性和可调用六 jet 消费范围写完整。它是条件代数／正则性结论及独立源码接口；没有运行科学、区间求逆、场评价、编译或覆盖，没有新实际场或新增接受门。

## 1. 题目实际要求与本结论的边界

[题 README](../README.md) 的第 1 条要求：对每个 $t$，$F_t$ 是 $C^2$ 嵌入，且 $t\mapsto F_t$ 在 $C^2$ 拓扑下连续。它没有要求这个取值于 $C^2$ 的映射对时间再可微两次。第 5 条还要求固定同一度量、参数和时间范围的真实精化；单个族的时间连续不替代跨精化层的收敛。

本文证明以下范围。

1. 只要原完整材料角已有严格正下界，其唯一准确逆即可定义共同物质图；不需要先把数值逆求至某个新容差，才能应用同目标的坐标恒等式。
2. 时间相位是在**物理材料角**中平移。共同首图中的完整公式含当前角的准确逆，不能直接把共同 $q$ 改成 $q-\alpha$。
3. 原准确场、原全部接缝和固定帽确为 $C^2$ 时，所得全时间族在空间 $C^2$ 拓扑下连续。六 jet 的准确表达足以写出每个时刻的全部空间二阶链式法则；连续性的证明不新增四阶数值检查。
4. 已真实支付的、绑定同一个当前准确场的完整 Loewner 相对界和全像几何结论，可在准确图变换下转述；未支付的结果仍未支付。
5. 若另行要求时间二次可微到空间 $C^2$，需另保 12 类径向／角向混合 jet。本文单列其公式与责任，不把它们加到原完成标准或 BVP 接受门。

## 2. 已核的实际解释器与定义资料

| 来源 | 本文使用的实际职责 |
|---|---|
| [R437 首构造策略](../computations/geometry_20261116_current_C_ten450_closed_parameter_policy.py)，SHA256 `d7d01460f5a22f4fa2ca75ad36475688d65a465ba488d9caff65cb5ef13fb871` | `material_definition` 保存全部 112 个原 core 词及准确有理系数；`capture_material_transport` 保存真实首／当前材料定义、原 A/B 文件身份、registration、inlet normalization、两个 mean/gauge 与全部构造词。 |
| [R409 当前 shared field](../computations/geometry_20261115_current_C_ten450_shared_field.py)，`6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3` | 原相位是 $R_\alpha F_0(s,\theta-\alpha)$，$\alpha=\pi t/2$；两帽固定。原当前 B、完整 FFT 节点、所有 mean 及当前规范实际定义场，不定义新的目标 $E_C$。 |
| [675 准确有限表达解释器](../computations/geometry_20261115_shared_active_interval_balls.py)，`675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` | `ExactFiniteField.evaluate` 中 $\phi=2\pi q$；prefix 用全部实际 core／节点，tail 用 $\Phi(\phi)$；全部准确 Hermite、完整角模态和两反射保留。`Jet2` 给真实空间六 jet。 |
| [R416 准确 cut 场](../computations/geometry_20261115_current_C_accurate_cut_patch.py)，`28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` | `AccurateCutBundle.field` 是独立准确 C/cut 表达；`source_bundle` 的数值 A 只是原来源，不能代其准确几何。 |
| R441 resolution saved-prefix `fb6e181cd0ddfb34cc70c874c119ceb149850ce8756d1f2f0dd775175e99cffb`；shared field `1ceda9d32cfcf50e28e737cd0aee981cb8dc2329027aa2967d08532a1ea6e935`；accurate cut `8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52` | 新实际 core／节点／角密度及独立来源；accurate bundle 的 `source_bundle/field/target/model/Active/Background/binding` 合同保持。这里没有将它们冒成旧 R416 字节。 |
| [R413](../computations/geometry_20261115_current_C_original_cuff_target_atlas.py)、[R417](../computations/geometry_20261115_current_C_ten450_fixed_cap_balls.py)、[R418](../computations/geometry_20261115_current_C_ten_complete_relative_metric.py) | 原平 cuff 图册、完整两帽 Cartesian 图、原全闭相对目标与完整 Loewner 覆盖职责。 |

准确 core 系数由保存的 IEEE binary64 词解释为准确二进有理数。它们不是“已知精确 PDE 解”的系数；原 Hermite/FFT 场也不是原有限 ODE 轨迹的已证无误差替身。本文只对这些明确解释器所定义的准确有限场及原准确 C 目标作条件陈述。

首个 R437 材料收据记录完整 core，但没有执行共同图拉回。当前场可以有不同 core、不同登记旋转和不同 inlet normalization；这些差异不允许被强制相等来拒绝原求解器，也不被本文抹掉。新的当前场误差仍用自己的准确表达和原消费者支付。

## 3. 唯一准确逆和共同物质图

以 $0$ 表示实际首图，以 $j$ 表示当前场。对各自完整实际系数定义

$$
\Phi_j(\phi)=\phi+
\sum_{m=1}^{M_j}\frac{(1-4m^2)c_{j,m}}{2m}\sin(2m\phi),
\qquad
\rho_j(\phi)=1+\sum_{m=1}^{M_j}(1-4m^2)c_{j,m}\cos(2m\phi).
$$

当前本接口明确注册的原件都是 $M_j=112$。纸证允许有限 $M_j$ 不同，但不借此声称未来变维 loader 已接入。

沿原完整材料逆前提，设 $\rho_j\ge\beta_j>0$ 在整个实轴成立。原 R237 的完整准确参考下界减完整系数差加权绝对值和，是现有 saved-prefix 的一种充分证明；不是新的采样门。

令

$$
\Theta_j(q)=\Phi_j(2\pi q),\qquad I_j=\Theta_j^{-1}.
$$

由 $\Theta'_j\ge2\pi\beta_j>0$、$\Theta_j(q+1)=\Theta_j(q)+2\pi$，$\Theta_j$ 是实轴上双射的实解析提升；$I_j$ 唯一。这里 $I_j$ 是这个准确函数的逆，**不是**有限 Newton 程序或其舍入后映射。

共同首图到当前图的准确换元为

$$
\psi_j(q)=I_j(\Theta_0(q)),\qquad
\Theta_j(\psi_j(q))=\Theta_0(q).
$$

它保周期、半周期和反射：$\psi_j(q+1)=\psi_j(q)+1$、$\psi_j(q+1/2)=\psi_j(q)+1/2$、$\psi_j(-q)=-\psi_j(q)$。这些恒等式来自全部频率和准确逆唯一性，不能替换为有限节点的相等。

prefix 共同坐标为 $u=s_{{\rm numeric},j}/L_{{\rm numeric},j}$。在这个共同 $u$ 上，当前场记作 $K_j(u,q_j)$；它包含原实际代入 $s_{{\rm numeric},j}=L_{{\rm numeric},j}u$。径向区用原 $r$。后文把这两种第一个坐标统一记作 $x$，但实际导数和源码须保前缀的每阶 $L_{{\rm numeric},j}$ 因子。

## 4. 全时间相位的正确公式

令 $K_j$ 为当前准确相位零活动场，已含当前实际登记旋转／平移、完整 B、两 mean 和 R416 cut 表达。原运动在物理材料角中平移。对共同首图，正确公式是

$$
\boxed{\quad
\widetilde F_{j,t}(x,q)
 =R_{\alpha(t)}K_j\!\left(x,
 I_j(\Theta_0(q)-\alpha(t))\right),
 \qquad \alpha(t)=\frac{\pi t}{2},\quad 0\le t\le1 .\quad}
$$

定义首图自身的物理角平移

$$
v_{0,\alpha}(q)=I_0(\Theta_0(q)-\alpha).
$$

由准确逆唯一性，

$$
I_j(\Theta_0(q)-\alpha)=\psi_j(v_{0,\alpha}(q)).
$$

故亦可写为 $R_\alpha\widetilde K_j(x,v_{0,\alpha}(q))$，其中 $\widetilde K_j=K_j\circ T_j$、$T_j(x,q)=(x,\psi_j(q))$。一般不能写成 $R_\alpha\widetilde K_j(x,q-\alpha)$，甚至不能无条件写成 $q-\alpha/(2\pi)$；只有线性材料角等额外特殊情形才会退化成后一式。

该换元不重算或覆盖当前 registration/inlet 数据。它是对同一个当前准确场的参数化，不是把新场偷偷替换成首场。

### 固定帽与平 cuff

两帽沿冻结 R409/R417 真实定义保持

$$
F_{\pm}^{\rm cap}(X)=
\bigl(x,y,\ \pm(H+b_\pm(X))\bigr),
\quad X=(x,y),
$$

其中全部 marker 的中心、半径、幅值、所在帽及重叠求和均固定。负幅值也保留。帽的参数化不作上述角移动。

在原平 cuff 重叠环，完整 marker 支撑已与之分离；准确活动表达为

$$
K_j(r,q_j)=
\bigl(r\cos\Theta_j(q_j),r\sin\Theta_j(q_j),\ \pm H\bigr).
$$

代入相位公式得

$$
R_\alpha K_j(r,I_j(\Theta_0(q)-\alpha))
 =\bigl(r\cos\Theta_0(q),r\sin\Theta_0(q),\ \pm H\bigr).
$$

这是在**整个重叠环**上的准确恒等式，不只在一条接缝或采样点成立。其全部已有空间二阶导数因此一致，时间变化也在此准确抵消。上下反射与绕 z 轴旋转可交换，所以同一论证保两侧。

不能由此假设完整带非对称 marker 的闭目标旋转对称。活动区的物理角平移一般不能延成“活动区平移、帽恒等”的一个全闭目标旋转作用。合法论证是活动图中的相位恒等式，加上平 cuff 重叠处的准确抵消和固定帽；无需把非线性角换元穿过帽中心。

## 5. 同一个 g 与原相对界的准确转述

固定原同一准确 C 语义、完整十参数、自然长度 $L$、准确半径 $a$、cut/cuff 和完整帽函数。若 C 输入描述一个全根族，以下逐个固定同一成员成立；区间消费者仍须覆盖原全部许可成员，本文不另选中点或成员。

当前图中的目标为

$$
g_j^{\rm pre}=L^2du^2+a(Lu)^2\Theta_j'(q_j)^2dq_j^2,
\qquad
g_j^{\rm rad}=E_C(r)dr^2+r^2\Theta_j'(q_j)^2dq_j^2,
$$

两帽为 $g_\pm^{\rm cap}=I+Db_\pm\otimes Db_\pm$。静态 $T_j$ 在活动图用 $\psi_j$、在帽 Cartesian 图用恒等，按第 4 节过渡关系拼成全闭微分同胚，且

$$
T_j^*g_j=g_0.
$$

帽高 H 不进入这个帽 metric，但仍是本次实际几何构造的冻结参数；W 也不许可替换原准确目标。当前不同 B 或规范不改变这条目标恒等式，却会改变当前场，原误差责任因此仍在。

若绑定同一个当前准确场的原完整消费者已真实证明

$$
-\eta g_j\preceq F_{j,t}^*e-g_j\preceq\eta g_j
$$

对整个闭面及全部 t 成立，则用 $DT_j$ 作准确合同变换，得到同一个 $\eta$ 对 $g_0$ 的相同不等式。不乘某个材料导数条件数去放宽原相对门；也不把坐标分量绝对误差当相对算子范数。

对相位构造，活动区自身的 $S_{j,\alpha}(q_j)=I_j(\Theta_j(q_j)-\alpha)$ 保活动目标；旋转保欧氏 metric。因此真正全活动角域的相位零 Loewner 结论，可按此完整相位公式覆盖全 t，帽本身固定，cuff 按前节拼接。这是局部图册论证，不要求带 marker 全闭目标有旋转群作用。原消费者若尚未证明所需全角／全部片／准确场身份，本命题不填补它。

完整嵌入、reach、D、全像 held、含反射的 $\delta_E$ 在每个固定 j、t 的满射重参数化下保持。它们不能从相位零的局部 metric 或材料正性推出。尤其活动像旋转而非对称帽固定，全闭像不必等于相位零全闭像的刚体旋转；原全 t mixed pairs、全像 cover 与 H 的物质定义均须保留。

若 H 是同一个固定帽内部区域，$T_j|_H$ 为恒等。若 H 另在活动区，须明确用其原区域的逆像，不能因坐标重名便宣布固定 H。跨 j 的像、D、误差和比例仍各自真实支付。

## 6. 题目要求的全 t 强 C² 连续：不需要额外四阶门

**命题。** 假设当前准确闭场的原接缝／反射／固定帽结构已给出一个 $C^2$ 场，并沿原全圆材料正性。则第 4 节的族 $[0,1]\to C^2(M,\mathbb R^3)$ 连续。若原每个时刻已证明嵌入，静态共同图拉回保全部这些嵌入。

**证明。** 每个 $I_j$ 是实解析，故

$$
h(q,t)=I_j(\Theta_0(q)-\pi t/2)
$$

在局部周期提升上光滑。原紧闭面取有限图册与紧子图。对活动片，所有空间至二阶导数由 $K_j$ 的至二阶空间导数、$h_q,h_{qq}$、常数径向尺度与 $R_{\alpha(t)}$ 的有限积和组成。每个因子在空间及 t 上联合连续；紧集上均匀连续，所以这些导数在 $t\to t_0$ 时一致收敛。帽表达不依赖 t。原径向接缝的完整二 jet 同值及平 cuff 重叠恒等式保证各子图的二阶表达确实拼成原全局 $C^2$ 场。有限图册上这些一致收敛正是强 $C^2$ 连续。证毕。

这里没有对 t 微分 $K_{j,xx}$，因此不需要 $K_{j,xxq}$ 或四阶角导数才能证明连续。相邻径向节点只需原准确共享二 jet 和完整角函数的实际拼接关系；采样点的近似相等不替代这些前提。

也不能从“每个 j 的 $\beta_j>0$”推出跨 j 的统一 $C^2$ 收敛。后者至少需要相应统一逆导数控制、同一准确目标／构造、完整同图误差与规范责任。native 残差下降或相位表达一致不替代 README 第 5 条的实际精化证据。

## 7. 准确空间六 jet 与可调用消费

令 $z=I_j(\Theta_0(q)-\alpha)$，并记在 z 处

$$
A=\Theta_j'(z),\quad B=\Theta_j''(z),\quad
a=\Theta_0'(q),\quad b=\Theta_0''(q).
$$

则

$$
z_q=\frac aA,\qquad
z_{qq}=\frac{b-Bz_q^2}{A}.
$$

若当前解释器以原 $s_{{\rm numeric},j}$ 为第一个变量，令 $\lambda=L_{{\rm numeric},j}$；若用原半径 r，令 $\lambda=1$。对原六 jet $K,K_s,K_q,K_{ss},K_{sq},K_{qq}$，共同坐标的完整六 jet 是

$$
\begin{aligned}
\widetilde F&=R_\alpha K,&
\widetilde F_x&=R_\alpha\lambda K_s,&
\widetilde F_q&=R_\alpha K_qz_q,\\
\widetilde F_{xx}&=R_\alpha\lambda^2K_{ss},&
\widetilde F_{xq}&=R_\alpha\lambda K_{sq}z_q,&
\widetilde F_{qq}&=R_\alpha(K_{qq}z_q^2+K_qz_{qq}).
\end{aligned}
$$

所有 K 的值均在当前实际原片、当前原径向坐标和 z 处取，不在首场、旧 q 或区间中点取。真实两反射、全部原 modes/means、每个闭 radial piece 与帽都保留。

独立 helper 的定义消费者绑定实际首 R437 收据和首 plan/assembly、当前 R416 或 R441 已加载准确 bundle。首 beta 来自该首 assembly 的原 saved-prefix 定义；当前 beta 来自当前准确 field，二者没有被要求相等。实际 core 词、目标、全十词、W/H/全部 marker、原 phase 和各来源分别记录。

准确逆是表达的一部分，故**结构定义和上述全域界转述不调用数值逆**。可选闭 cell 评价才用完整系数和原正下界产生逆像区间；它不是 solver 或已有证书的前置门。没有实际调用时，不报告“拉回 jets 已算”“全域 cover 已做”或“同 g 精化收敛”。

### 可选有限区间逆：不取中点作真实逆

写 $\Theta_j(q)=2\pi q+S_j(q)$，$|S_j|\le B_0$，其中 $B_0$ 是全部准确 sine 系数绝对值和。给定整个准确目标角区间 Y，所有唯一逆像都在

$$
Q_0=\frac{Y+[-B_0,B_0]}{2\pi}.
$$

全导数区间可用

$$
D=2\pi[\beta_j,\ 1+\sum_m|(1-4m^2)c_{j,m}|],\qquad D>0.
$$

给定已经包住全部逆像的 Q，选其中任一准确有理 c。逐个准确逆像用均值定理得

$$
I_j(Y)\subseteq Q\cap\left(c+\frac{Y-\Theta_j(c)}D\right).
$$

有限重复及 outward 区间运算保持完整闭逆像；宽度不缩或显式工作预算结束并不改变已形成包围的有效性。它不承诺任意精度或机器字逆相等。若资源／计算异常使当前完整 cell 未返回，原消费者仍把它记未付，不能填零或宣称反证。按实提升计算，无需猜周期分支，也不漏 $q=0,1$ 端点。

当前六 jet API可直接把该包围送给原完整准确表达的实提升；该表达的全部整数频率／材料提升保证周期定义，不做重新 FFT 或有限模态投影。新的输出是这个准确复合函数的包围，不是 binary64 逆算法的导数。

## 8. 另列更强性质：时间二次可微到 C² 的完整责任

这一节是可选更强结论，不是本题第 1 条的新 gate。令 $\mathcal D=A^{-1}\partial_{q_j}$ 为对物理材料角的准确导数，$J(x,y,z)=(-y,x,0)$ 为旋转生成元。在共同相位的同一评价点，

$$
\partial_\alpha\widetilde F=R_\alpha(JK-\mathcal DK),\qquad
\partial_\alpha^2\widetilde F
=R_\alpha(J^2K-2J\mathcal DK+\mathcal D^2K).
$$

再对共同空间 q 求两次导数，会用到最高 $\mathcal D^4K$。写 $B=\Theta_j''$、$C=\Theta_j'''$、$D_4=\Theta_j^{(4)}$，则

$$
\begin{aligned}
\mathcal DK&=K_q/A,\\
\mathcal D^2K&=K_{qq}/A^2-BK_q/A^3,\\
\mathcal D^3K&=K_{qqq}/A^3-3BK_{qq}/A^4+(3B^2-AC)K_q/A^5,\\
\mathcal D^4K&=K_{qqqq}/A^4-6BK_{qqq}/A^5
+(15B^2-4AC)K_{qq}/A^6
+(10ABC-A^2D_4-15B^3)K_q/A^7.
\end{aligned}
$$

所需原场向量 jet 的精确集合是

$$
\{K_{x^a q^b}:0\le a\le2,\ 0\le b\le4-a\},
$$

即 $5+4+3=12$ 类；不是把现有六 jet 的标签改成高阶。当前材料角须至四阶，首角在直接公式中只须至空间二阶；时间导数再乘 $(\pi/2)^n$。prefix 的每个径向阶仍保 $L_{{\rm numeric},j}^a$。

原准确有限场对角变量的完整有限三角表达是解析的；切向复合一般不保持原有限频带。径向只须二阶，故不能错误地要求原 Hermite 拼接先升成径向四阶。要从逐片公式提升为上述更强全局性质，所有 12 类 jet 需在原接缝按完整角函数匹配；原 piecewise 二 jet 共享若是全角函数恒等式，可对该恒等式继续作角导数。若只有数值采样比对，就未支付这项责任。

固定帽的 bump 是原 $t_+^4$ 图，现有 $C^3$ 及空间六 jet 足以供原 $C^2$ 性质。帽不随运动时间变化，强时间二阶导数在那里为零；不因本附节要求帽先成为空间 $C^4$。平 cuff 上全相位准确抵消，亦不制造额外高阶接缝。

本文源码只实现定义绑定与可选完整空间六 jet 消费；上述 12 类高 jet 的实际形成／完整包围没有运行，也不冒充已有输出。

## 9. 当前完成范围与后继接线

本结论解决的是：如何以唯一准确逆直接定义共同图，保持原同一准确目标，并从原 $C^2$ 场结构得到题目要求的全 t 强 $C^2$ 连续。它没有把原目标换成当前 Bprime，也没有把 R409 数值 A 冒成 R416 准确场。

源码是 requestless 独立消费者。它不改 R437/R441/R416、不重启原绝对钟、不创建新 BVP 接受、不读取已删场的 hash 来复原 field。实际首 plan/assembly/材料记录与当前 bundle 必须尚在同一个允许的现场，或由明示的新真实流程重新形成；只有 receipt 而没有所需正文时保持未付。

未来需要可视网格或直接共同图 cell 包围时，可调用可选逆像／六 jet API；未来只转述已付完整 Loewner 合同时，准确坐标定理已足够，不再附加求逆容差验收。每次实际调用的 source、原 field、原 clock、完整资源、异常和未访范围仍由其宿主请求记录，不能因为 helper 有完整接口就写成已运行。

完整非零原 native/112/338/fullDN、真正453及450、全部全闭 metric/reach/held/反射、同一个 g 的真实网格／角／频率／时间精化以及输出网格仍依 [open](../open.md) 的原责任推进。本文不宣布任何未来实际场或本题完成。

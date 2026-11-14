# R133：既成 signed Green 的全部接口 impulse 费用，零新增演化计算

2026-11-14，visible-exact / tail_connector；供新的方向 Green 后验误差使用。

**范围。** 只消费已经成功的完整 finite193 signed positive Green、其
12361 个有序连续/接口事件和既成 L2 核缓存。下文给全部5970个真实
frame 接口（包括最后腰端虚接口）的加权状态跳到普通物理
$L^2_r$ 输出的上界。没有重新计算 target、matrix exponential、
标量 exponential 或旧 Riccati/端口。它不授予未知无限高模逆，也
不删除真实 cut Robin、独立 mean、帽外源及原有限腰边界。

## 1. 精确单位与原有端口

沿原径向正方向，$y=R(r)h$ 是既成 finite193 加权状态。
$p=\|P(r)y\|_2$、$q=\|(I-P(r))y\|_2$，故193维 mean 仍在完整
正交分解中。cone 斜率记为 $\rho_c$，$z=q-\rho_c p$ 只是完整
正比较系统的变元；不对未知 norm 本身直接减去这一项建立等式。

每个原已付事件有非负端口上界
$$
 z_L\le a_i z_R+Q_i,\qquad
 p_R\le b_i p_L+k_i z_R+P_i .
 \tag{I.1}
$$
连续齐次事件 $Q_i=P_i=0$；非齐次列仍使用原正 Green 的准确
单位。$a_i,b_i,k_i$ 可取原保存的有向上端数，不能重新从舍入的
分量猜一个未认证 transfer matrix。

原腰闭合 margin $m_0=1-D_0\rho_{c,0}>0$ 给
$$
 p_0\le v_0z_0,\qquad v_0=D_0/m_0 .
$$
无源下向前定义
$$
 v_{i+1}=b_i v_i a_i+k_i .
 \tag{I.2}
$$
这正是原 finiteL2 前扫的非负 cone 系数，可逐条复用。
比较等式可把每个上端数作为新的非负精确系数，原解由正核支配；
不要求原定点 norm 的 Riccati 可微性。

## 2. 每个连续片的两个齐次输出积分

本节只使用既成缓存，不重新生成旧演化。
原片长 $h_i$、signed $\mu_i,\nu_i$、$c_i,e_i\ge0$、
cone 上界 $\beta_i\ge\sup\rho_c$ 已认证。
令
$$
 \lambda_p=\mu_i+c_i\beta_i,\qquad
 \lambda_z=\nu_i+c_i\beta_i .
$$
保存的 $I_p,I_{2p},I_z,I_{2z}$ 分别是
$\int_0^{h_i}e^{\lambda_p t}dt$、
$\int_0^{h_i}e^{2\lambda_p t}dt$ 及另两对应积分的合法上界。
它们是上界，不被当成包含真积分的双侧球。

给定非负 $p_L=P,z_R=Z$，同一 signed 比较方程给
$$
 \|z\|_{L^2(I_i)}\le \sqrt{I_{2z}}Z,\qquad
 \|p\|_{L^2(I_i)}
 \le \sqrt{I_{2p}}P+c_i I_p\sqrt{I_{2z}}Z.
 \tag{I.3}
$$
第二式是对 $p'=(\mu+c\rho_c)p+cz$ 的正核
Young/Cauchy 积分，仅在这一片用一次 Minkowski。
从未把负 $\lambda_p,\lambda_z$ 换成绝对值来作全长传播。

记 $\omega_i\ge\sup_{I_i}\|R(r)^{-1}\|$，它是原普通
pair norm 恢复的真实权。置
$$
 U_i(P,Z)=\sqrt{I_{2p}}P+c_i I_p\sqrt{I_{2z}}Z,\qquad
 V_i(Z)=\sqrt{I_{2z}}Z,
$$
$$
 \mathcal J_i(P,Z)=
 \omega_i^2\{U_i(P,Z)^2+[\beta_iU_i(P,Z)+V_i(Z)]^2\}.
 \tag{I.4}
$$
则完整普通物理 $\int_{I_i}\|h\|_2^2\,dr\le\mathcal J_i(P,Z)$。
$q=\rho_cp+z$ 的 mean 和全部非mean 都在此 pair 恢复中。
若旧缓存有更紧合法的 whole-cell 正齐次预算，可直接替换
$\mathcal J_i$，但两次调用必须指同一原事件和同一物理 norm。

对于窗口 $W$ 与片的部分交，若没有保存对应子片积分，仍可零新增
exponential 地使用
$$
 E_p=1+\max(0,\lambda_{p,\rm up})I_p,\qquad
 E_z=1+\max(0,\lambda_{z,\rm up})I_z .
$$
它们分别上界 $\max(1,e^{\lambda_ph_i})$ 和
$\max(1,e^{\lambda_zh_i})$；当 signed rate 非正时准确取1。
因此把 (I.4) 中的 $U,V$ 改为
$$
 U_\infty=E_pP+c_iI_pE_zZ,\qquad V_\infty=E_zZ
$$
并乘准确长度 $|I_i\cap W|$，也是该窗口积分的上界。
不可在负 $\lambda$ 时用 $1+\lambda I_{\rm up}$ 冒充 exponential
上界。全片可与 (I.4) 取较小的完整合法平方界。

## 3. 两个方向的 O(N) 平方递推

固定一个真实输出窗口 $W$，例如完整 $[0,.9]$ 或原已付负区。
$L_i^W$ 上界：在节点 $i$ 给予单位 $z_i$、其左侧无体源且满足
同一腰闭合时，节点左侧输出在 $W$ 中的物理 $L^2$ 平方。
$R_i^W$ 上界：在节点 $i$ 给予单位 $w_i$、右侧 $z=0$ 且无源时，
节点右侧输出在 $W$ 中的物理 $L^2$ 平方。
取 $L_0^W=0,R_N^W=0$。

向前经过连续片时，单位 $z_R=1$ 给
$z_L=a_i$、$p_L=v_i a_i$，所以
$$
 L_{i+1}^W=a_i^2L_i^W+\mathcal J_i^W(v_i a_i,1).
 \tag{I.5}
$$
向后经过连续片时，单位 $p_L=1,z_R=0$ 给 $p_R=b_i$，所以
$$
 R_i^W=b_i^2R_{i+1}^W+\mathcal J_i^W(1,0).
 \tag{I.6}
$$
加法来自真正不相交的径向输出区间。
没有把多个相同径向源视为正交，也没有对每格作 $\sqrt h$ 三角求和。

零长度的 frame 接口不贡献径向积分：
$$
 L_{i+1}^W=a_i^2L_i^W,\qquad
 R_i^W=b_i^2R_{i+1}^W .
 \tag{I.7}
$$
(I.2)、(I.5)--(I.7) 全部使用同一个保存顺序、同一 signed 端口、
同一 root/cut/waist 参数。两个窗口分别累积其准确 $dr$，不把全区
上界误报成某个更小窗口的准确积分。

## 4. 真实跳源，包括 sec/tan 与两列

在一个真实 projector 接口，令
$\delta=\|P_+-P_-\|<1$、
$s=\sqrt{1-\delta^2}$。
齐次混合比较和源列取
$$
 p_+\le A p_-+Bq_++a_{\rm src},\qquad
 q_-\le Cp_-+Dq_++b_{\rm src},
$$
$$
 A=D=s^{-1},\qquad B=C=\delta/s,\qquad
 a_{\rm src}=b_{\rm src}=s^{-1}\|j_y\|_2 ,
 \tag{I.8}
$$
其中 $j_y=y_+-y_-$ 是**加权状态**的真实跳。
不能把 $\delta=\sin\vartheta$ 直接当成 $\tan\vartheta$。

若右侧 cone 为 $\rho_+$，令 $d=1-B\rho_+>0$。
准确消元给
$$
 a=D/d,\quad b=A/d,\quad k=B/d,
$$
$$
 z_- = a z_+ +(D\rho_+/d)a_{\rm src}+b_{\rm src},\qquad
 p_+ = b p_-+kz_++a_{\rm src}/d .
 \tag{I.9}
$$
因此若原事件保存字段为
$z_{\rm from\,a},z_{\rm from\,b},p_{\rm from\,a}$，
它们的数学身份分别是 $D\rho_+/d,1,1/d$ 的合法上界。
定义单位 $\|j_y\|_2$ 的真实负荷
$$
 Z_{\rm load}=
 (z_{\rm from\,a}+z_{\rm from\,b})\,s^{-1},\qquad
 P_{\rm load}=p_{\rm from\,a}\,s^{-1}.
 \tag{I.10}
$$
没有 $p_{\rm from\,b}$ 是 (I.9) 的准确结果，
不是删掉第二个源。若保存的更一般事件确有该列，则必须加回它。

## 5. 单接口到完整输出的平方门

只放这一跳时，右侧 $z_+=0$，左侧
$z_-=Z_{\rm load}\|j_y\|$。
其左端 $p_-\le v_-z_-$，
右端的向右幅度不超过
$(b v_-Z_{\rm load}+P_{\rm load})\|j_y\|$。
故实际 Green 的单位跳响应满足
$$
 \boxed{\quad
 \|G_{\rm jump,i}:j_y\mapsto h\|_{L^2(W)}^2
 \le L_-^W Z_{\rm load}^2+
 R_+^W(b v_-Z_{\rm load}+P_{\rm load})^2 .
 \quad}
 \tag{I.11}
$$
两个平方之和只使用**同一个跳**的左、右输出支集不交。
不同跳的整个 Green 输出一般重叠；不得把它们免费平方相加。
对完整 jump 序列安全地用
$\|\sum_iG_{\rm jump,i}j_i\|\le\sum_i g_i\|j_i\|$，
或另证明相应带权 Schur/Gram 界。
例如 dyadic $V_i$ 的真 defect 作用于同一个未来源，不能称为独立输入。

若跳原来用普通 $h$ 给出，先准确恢复
$j_y=R_i j_h$（若 $R$ 也跳则使用完整实际两侧公式）；
若新 approximate kernel 直接给 $y$ 跳，则不再重复乘权。
最后腰端 $Q_{\rm waist}\to X_{\rm last}$ 的零长度接口仍在
(I.8)--(I.11) 中，即使其左侧 $L_-^W=0$：
腰闭合后的 $b v_-Z_{\rm load}$ 通道仍可能非零。

## 6. 消费与剩余范围

新消费者须逐字绑定原成功 Green 的端口、L2 缓存、完整系数身份、
保存顺序、原 waist margin 和所有 sec/tan no-pole 门。
只新增上述有限非负标量递推和有向平方运算；每个可复用前缀保存其
真实数据身份。原 cap 独立边界列和 mean 仍由原完整 Green 消费。

这些费用供同一个 approximate kernel 的真 dyadic-$V$ jumps 作
后验比较。它们不会把原96维 regular 提议锚变成完整传播子，
不会把未知高模或真实 cap cross-block 删掉，也不替代同一 patched
$F$、其 inverse、source Gram 和全部边界 defect 的原验证。

# R150：全余 W 的原首一 T 三次、F 二次与六列环境

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。AI-assisted GPT-6 Astra Pro。

**状态：全图原三次降维已证明。** [整个 lambda=3/2 分支排除](R150-appendix-unit211-W-lambda-three-halves-complete-original-exclusion.md)支付了唯一剩余的 T³ 几何首项因子。原两条四次现在准确等价于一条首一 T³ 与一条必须继续保留的至多 T² 余式；配合原均值首一 F²，得到明确的六列多项式环境。不宣称完整原方程已经排空。

## 1. 原域和两条原四次

沿用[原首一四二次环境](R150-appendix-unit211-W-global-monic-T-four-F-two-and-finite-original-environments.md)的当前原一般 LS、Delta=0、W=0 权域；新加入的已付因子只有 3−2lambda。原 D 非零条件的旧结论仍只在其原物理作用域使用，不外推到一般 hU=kU 碰撞。

记

$$m=u-\ell,\qquad d=1-Q,\qquad M=\ell^2d-m^2,$$

$$A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,$$

$$c=3-2\lambda,\qquad A_*=4uQ-J,\qquad
C_*=A_*m^2+Jd\ell^2,$$

$$D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell TA_\lambda+2T^3.$$

[两四次原身份](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)给出同一个原 T、lambda 上的必要式

$$a_D=M\ell^2Q(3-4\lambda)+MA_*T^2+2MuQc\ell T+C_*D,$$

$$b_D=2Mm(A_*T+uQc\ell),$$

$$R_4=Ma_D^2-Db_D^2,\qquad
C_4=2mDa_D+Kb_D.$$

二者都保持完整原 Delta、二阶矩和三阶矩组合来源。以下不倒置 D 或任何范数。

## 2. 准确三次头及其全域支付

将

$$a_D=a_2T^2+a_1T+a_0,\qquad b_D=b_1T+b_0.$$

由上式，

$$a_2=MA_*-C_*,\quad a_1=2MuQc\ell,\quad
b_1=2MmA_*,\quad b_0=2MmuQc\ell.$$

利用 M=ell²d−m²，直接得到

$$[T^4]C_4=8muQ\ell^2d=:\kappa,\qquad [T^3]C_4=0.\tag{1}$$

已刊首一四次正是

$$q_4=C_4/\kappa
=T^4+\alpha_2T^2+\alpha_1T+\alpha_0.$$

再记

$$L_4=[T^4]R_4=Ma_2^2+b_1^2.$$

因此 R4−L4q4 至多三次，且其 T³ 系数准确为

$$
\begin{aligned}
\theta
&=2Ma_2a_1+2b_1b_0\\
&=8M^2uQ(3-2\lambda)\ell^3d(2uQ-J).
\end{aligned}\tag{2}
$$

新自含 V8 源在八个自由符号的整系数多项式环中，只代入 M=ell²d−m²，实际核出 (1)、(2) 和完整原组合

$$\kappa R_4-L_4C_4.$$

其 T 次数恰为三，三次头实际为 kappa·theta；不是仅用次数或若干取样推断。

在当前 W 图中，

$$\Phi(J-2uQ)=P_f,\qquad P_f=T_0(J-Q).$$

Phi、T0、J−Q 都已在既定作用域支付，所以

$$2uQ-J=-P_f/\Phi$$

是已有权单位。M、u、Q、ell、d 也已经支付；而 c=3−2lambda 已由整支定理新支付。故 theta 在全余 W 图是单位，未留下新的头零面。

于是定义

$$q_3=\frac{R_4-L_4q_4}{\theta}
=T^3+\beta_2T^2+\beta_1T+\beta_0.\tag{3}$$

这是全余图的首一 T 三次原必要式。其分母只含已经支付的权因子和 3−2lambda；不使用 A143、B239 或其他未付首项。

## 3. 两四次的完整理想等价及仍须保留的二次原行

不能只保留 q3 而丢掉 q4。准确可用的理想身份是

$$
(q_4,R_4)=(q_4,q_3)
$$

因为 R4=L4q4+thetaq3，theta 为单位。再按首一 q3 除 q4，得到不需要新除法的完整身份

$$q_4=(T-\beta_2)q_3+r_2,\tag{4}$$

其中

$$
r_2=(\alpha_2-\beta_1+\beta_2^2)T^2
+(\alpha_1-\beta_0+\beta_2\beta_1)T
+\alpha_0+\beta_2\beta_0.
$$

所以

$$(q_4,R_4)=(q_3,r_2).\tag{5}$$

(5) 只说明这两个原派生四次之间的准确等价，不把它们与完整原 N、P 系统混同。r2 的 T² 首项可能为零；此处完全不倒置它，其整零纤维保留在 r2=0 中。

## 4. 首一 F² 与真正的六列环境

原中心坐标为 F=2f−u lambda。已刊均值身份给

$$q_F=\{mEBe+\ell dEBo\}/h_F,\qquad
h_F=u^2md\Phi/(eM),$$

且 qF 对 F 首一、次数二，系数在权局部环的 lambda、T 多项式环中。

令 A 为既定权局部环，置

$$A'=A[\lambda,(3-2\lambda)^{-1}].$$

先作首一 T³ 商，再作首一 F² 商：

$$\mathcal E=(A'[T]/(q_3))[F]/(q_F).\tag{6}$$

首一多项式除法在任意交换底环上成立，因此 (6) 是自由 A' 模，明确基底为

$$1,\ T,\ T^2,\ F,\ FT,\ FT^2.\tag{7}$$

也可以改用 S=T−2lambda 的同一六列；两组之间是可逆的三角基底变换。

对任意原 Gram 多项式，先按 qF 消去 F² 以上，再按 q3 消去 T³ 以上，就得到唯一的六列余式，并伴随完整原恒等式

$$p=\operatorname{rem}(p)+a_pq_F+b_pq_3.$$

该环境的自由性来自两个真正首一方程的次序构造，并不是假设完整原解的商环自由。将其再商掉 r2 和其他原 Gram 行，只得到由这六个元素生成的商；可能有额外关系。

本页不把随后对物理 D 或其他几何函数的局部化自动说成仍在同一个六维自由底环中。后续个别原值行应先清除其原 D 分母，再把得到的多项式返回 (6)，而不能未经证明倒置 D 的范数。

## 5. 后续必须保留的原输入

六列环境只支付了真正的归约规则。原均值、N1、NS、PS、二次 r2，以及个别 N/P 和完整 N4(Vval) 仍须保留为同点必要行。原 R4 与 C4 的替换由 (5) 完整控制，没有丢掉其中一条。

若使用原三阶矩恢复

$$s=K/(2mD),\qquad v_0=(T+ms)/\ell,$$

应先用无 D 逆的多项式表示

$$Dh_U=D(1+T/\ell)+(m/\ell-r)K/(2m),$$

$$Dk_U=D(1+T/\ell)+(m/\ell+r)K/(2m),\qquad r^2=d.$$

这样，个别 N 行乘 D²、个别 P 行乘 D³，完整 N4(Vval) 乘 D² 后，都可直接在 (6) 中归约。这里是下一原输入的准确接口，尚未宣称这些全部行的实际六列矩阵已经完成。

## 6. 真实新恒等式执行

自含源：

[2026-11-27-unit211-W-global-monic-T3-F2-exact-leading-identities-8542.js](../notes/2026-11-27-unit211-W-global-monic-T3-F2-exact-leading-identities-8542.js)

源 6224 字节，SHA256：

c3df64ed14ed5bca2434547789e35dd47b03fbecc59fe6fc1bfc76a10fa016c1。

实际 functions.exec V8 执行 53 毫秒，使用 BigInt 整系数多项式运算，没有数值代入。完整 kappa R4−L4C4 有 343 项；全部原组合与三次头恒等式均返回。规范完整证书 16509 字节，SHA256：

2887c7613b19b307f7816b07adfaaa16284dfa9f1e9073f32b39e8246d1176c4。

V8 无独立进程退出码或 RSS，不作推测。只保存小源、完整定义和回执，不保存可重算矩阵。整个 W 的排除仍未完成。

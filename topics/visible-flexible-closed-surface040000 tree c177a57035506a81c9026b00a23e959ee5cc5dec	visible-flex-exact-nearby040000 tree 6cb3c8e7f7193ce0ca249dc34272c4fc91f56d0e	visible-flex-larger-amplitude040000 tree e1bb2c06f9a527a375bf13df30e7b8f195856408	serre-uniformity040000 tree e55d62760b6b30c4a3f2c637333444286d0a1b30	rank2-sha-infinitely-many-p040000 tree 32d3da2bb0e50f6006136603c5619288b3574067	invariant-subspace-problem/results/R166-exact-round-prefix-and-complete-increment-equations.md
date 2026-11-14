# R166：准确圆形前缀的全段曲率界与完整增量方程

**状态：已证明。** 圆形前缀本身已见R136，末段已见R156；本结果把本次新补出的严格全段主曲率界正式登记，并给出不除未知n的完整增量恒等式。对象仅是指定base δ=0前缀与零控制平尾，未证明经过它的非圆分支、强目标闭曲面或全局reach。

本结果绑定候选 `notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json`，SHA256 `7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。定义、全部源定位与表示设计见[完整说明](../notes/2026-11-12-fd2d-geometry-whole-round-reference-and-gap-continuation.md)；所用严格标量包已由[R136](R136-peak-spacer-prefix-continuous-radius-and-outer-design-domain.md)闭存。

## 1. 准确参考及定向

R136给定物理弧长s上的准确半径a，中央a=a₀，切口a=4/5，且全段a≥4/5。在反馈Hermite段取φ=arcsin(a_s)，其已证|a_s|<1；后续取候选原有相位，a_s=sinφ，−π/2≤φ≤.3。记b=cosφ≥0，

\[
z_0(s)=\int_0^s b(t)\,dt,\qquad
X_0(s,u)=(a(s)\cos u,a(s)\sin u,z_0(s)).
\]

取e₁=sinφ e_r+cosφ e_z、e₂=e_θ和N=e₁×e₂=−cosφ e_r+sinφ e_z。直接微分有

\[
E=1,\quad F=0,\quad G=a^2,\qquad
S_0=(n_0,m_0,l_0)=\left(\frac{\cos\phi}{a},0,-\phi_s\right).
\tag{1}
\]

这里沿用当前三场的(n,m,l)顺序。令c₀=a_s/a、K₀=−a_{ss}/a，微分(1)得到

\[
n_0l_0=K_0,\qquad (n_0)_s=c_0(l_0-n_0),\qquad (m_0)_s=0.
\tag{2}
\]

这既有实际位置图也有完整Gauss–Codazzi恒等式。反馈段的等价求值是

\[
n_0=\sqrt{1-a_s^2}/a,\qquad
l_0=-a_{ss}/\sqrt{1-a_s^2},
\tag{3}
\]

仅在该段的已证正分母域使用，不能在切口计算0/0。

中央准确圆满足n₀=1/a₀、m₀=l₀=0，恰为现有`BalancedCurvatureCore(base_kind='circle',coefficients=0)`。即使使用固定非圆seed图u=U(s,ξ)，S₀也仍与角无关，不需要有限Fourier抵消非圆seed。

切口准确φ=−π/2、φ_s=0，因此S₀=0，X_s=−e_r、N=−e_z。设Z₀=z₀(s_cut)，零Bernstein控制的平尾位于真实高度Z₀；不能擅自改成预设常数高度。两侧X、X_s、X_u及全部二阶导数匹配：X_ss=0、X_su=−e_θ、X_uu=−(4/5)e_r。原片间共享a的两jet或相位的一jet同样保持实际C²接合。这里不要求l₀的径向一阶导数在切口与平尾相等；它在左侧一般非零，不能把C²曲面误加成C³条件。

## 2. 新补出的严格全段主曲率界

**定理1。** 对上述冻结δ=0前缀及其零控制平尾，处处

\[
\max(|\kappa_1|,|\kappa_2|)<7<7.2.
\tag{4}
\]

这一结论同时适用于R136明确保存并分别核验的准确binary64编码和准确书写十进制编码；两种编码没有混用。

**证明。** 因m₀=0，主曲率就是n₀,l₀。由a≥4/5及0≤cosφ≤1，得0≤n₀≤5/4。

对保留的51个Hermite片，取R136已闭Bernstein速度、加速度上界V,A。当前[有理消费者](../scripts/fd2d_round_prefix_curvature_bound.py)逐种编码核对

\[
0\le a_s\le V<1,\qquad |a_{ss}|\le A,
\qquad A^2<4(1-V^2).
\]

代入(3)得|l₀|<2。这一比较直接使用有理数平方，不把浮点开方当作证明。

普通cubic phase bridge的φ_s为二次Bernstein多项式，其三个控制值为

\[
\phi_s(0),\quad 3\frac{\phi(1)-\phi(0)}L-\phi_s(0)-\phi_s(1),\quad\phi_s(1).
\]

原严格相位包给出的控制区间绝对值均小于7/2，故整片|l₀|<7/2。两个soft-turn满足原准确长度L=|Δφ|/[K(23/25)]，其归一ramp在[0,1]，故|φ_s|≤K=3.4<7/2。coast上的l₀=0。

最后terminal brake两端相位导数为零，故相位差为cubic smoothstep，利用6t(1−t)≤3/2，

\[
|l_0|\le\frac{3(\pi/2-1.45)}{2(.026)}<7.
\tag{5}
\]

最后严格不等式由R136原π区间与各自准确长度编码作有理比较。报告显示的上界分别为6.969018853551731和6.969018853551728，但严格判断保留在有理端点中。上述片覆盖全部前缀；零控制平尾曲率为0。结合片间连续性得到(4)。∎

[实际报告](../notes/2026-11-12-fd2d-round-prefix-curvature-bound-01.json)及[4件闭清单](../notes/2026-11-12-fd2d-geometry-whole-round-reference-closed-manifest.json)绑定准确候选和原严格包。消费者真实session69373，9fddb8→1efb27，exit0，未求ODE/BVP。它没有为当前非零δ接受态证明曲率，也不由(4)单独推出全局reach。

## 3. 固定参考下的完整新度量强迫

令a_δ=a+Σδⱼψⱼ>0、c_δ=a_δ'/a_δ、K_δ=−a_δ''/a_δ，参考S₀仍固定。写实际完整场为

\[
(n,m,l)=(n_0+\eta,\mu,l_0+\lambda).
\tag{6}
\]

增量必须指实际完整函数，包含所有P1 raw、真实tail lifting及已声明的非线性代数映射；不是只取保留角模。固定atlas u=U(s,ξ)、U_ξ>0，记A=U_s/U_ξ，I=1/(a_δU_ξ)。

**定理2。** 在实际字段有定义的每一光滑子片上，其完整Gauss与移动图Codazzi缺陷准确等于

\[
G=l_0\eta+n_0\lambda+\eta\lambda-\mu^2+K_0-K_\delta,
\tag{7}
\]

\[
C_n=\eta_s-A\eta_\xi-I\mu_\xi-c_\delta(\lambda-\eta)
 +(c_0-c_\delta)(l_0-n_0),
\tag{8}
\]

\[
C_m=\mu_s-A\mu_\xi-I\lambda_\xi+2c_\delta\mu.
\tag{9}
\]

**证明。** 将(6)代入G=nl−m²−K_δ以及
C_n=n_s−A n_ξ−I m_ξ−c_δ(l−n)、C_m=m_s−A m_ξ−I l_ξ+2c_δm。
S₀与角无关，用(2)分别消去n₀l₀及(n₀)_s，余项恰为(7)–(9)。这是完整恒等式，不是小增量展开或忽略高阶项。∎

特别是δ≠0时，K₀−K_δ及(c₀−c_δ)(l₀−n₀)必须保留。新的a_δ不必还能写成某个回转面的弧长半径；参考固定并不删除真实度量变化。

对任意完整方向D，S₀及U均固定，DI=−I Da_δ/a_δ，故

\[
DG=lD\eta+nD\lambda-2\mu D\mu-DK_\delta,
\]

\[
DC_n=D\eta_s-A D\eta_\xi-I D\mu_\xi
-c_\delta(D\lambda-D\eta)-DI\,\mu_\xi
-Dc_\delta(\lambda-\eta+l_0-n_0),
\]

\[
DC_m=D\mu_s-A D\mu_\xi-I D\lambda_\xi
+2c_\delta D\mu-DI\,\lambda_\xi+2Dc_\delta\mu.
\tag{10}
\]

其中Dc_δ=(Da_δ'−c_δDa_δ)/a_δ，DK_δ=−(Da_δ''+K_δDa_δ)/a_δ。实际tail输入a_δsinU的全部链式导数和R153/R155合成导数属于Dη,Dμ,Dλ，不能省略。式(10)由(7)–(9)逐项微分，未除未知n，也不把切口一般平方根导数冒充准确tail端口导数。

## 4. 有限cell与零幅度行

在原cell长度h>0上，对固定正权平均规则Q可定义明确的新有限方程

\[
[\eta]/h-Q\{A\eta_\xi+I\mu_\xi+c_\delta(\lambda-\eta)
 +(c_\delta-c_0)(l_0-n_0)\},
\]

\[
[\mu]/h-Q\{A\mu_\xi+I\lambda_\xi-2c_\delta\mu\}.
\tag{11}
\]

准确圆参考已由(2)解析消去，全部真实增量端点、tail强迫及求积余项仍保留。δ=0且全部实际增量为零时，(7)与(11)在实数算术中对任何网格和Q严格为零。实际实现仍须诚实支付函数求值舍入与非零增量求积误差；不把解析恒等式冒充某次执行结果。若从现有非圆coast lifting改成S₀基准，这是明确的新表示，不是现有接受态的同函数加密。

中央采用circle-base曲率参数d时，令目标gap为ε≥0，选与ε无关的固定σ>0，使用

\[
\mathcal B_{\rm gap}(d,\varepsilon)=\frac{A(d)-B(d)-\varepsilon}{\sigma},
\qquad D_d\mathcal B_{\rm gap}=\frac{D_d(A-B)}{\sigma}.
\tag{12}
\]

式中A(d),B(d)是两条固定轴截距。σ可固定为.9；不能继续除以ε而直接传入ε=0。在d=ε=0时中央是准确圆，该行定义良好。

式(12)仅使零幅端点可表达，**不证明存在经过它的非圆分支**。切口n₀=l₀=0使Gauss线性化退化，非负tail控制零点还在允许锥边界；须由实际分支求解确定可行方向。全域同g加密、实际位置/两jet、全时held/刚体商变化/reach及固定帽闭合依然是主任务，不由本结果预支。
